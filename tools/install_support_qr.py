#!/usr/bin/env python3
"""Install a real WeChat support QR image and update README."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
README = REPO_ROOT / "README.md"
TARGET = REPO_ROOT / "assets" / "support-wechat.png"
PLACEHOLDER = "assets/support-wechat-placeholder.svg"
REAL_IMAGE = "assets/support-wechat.png"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Replace the support QR placeholder with a real image.")
    parser.add_argument("image", type=Path, help="Path to the real WeChat support QR image.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Check what would change without copying the image or editing README.",
    )
    return parser.parse_args()


def validate_image(path: Path) -> Path:
    source = path.expanduser().resolve()
    if not source.exists():
        raise FileNotFoundError(f"image not found: {source}")
    if not source.is_file():
        raise ValueError(f"image path is not a file: {source}")
    if source.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
        raise ValueError("image must be .png, .jpg, .jpeg, or .webp")
    return source


def update_readme(dry_run: bool) -> bool:
    text = README.read_text(encoding="utf-8")
    if REAL_IMAGE in text and PLACEHOLDER not in text:
        return False
    updated = text.replace(PLACEHOLDER, REAL_IMAGE).replace("微信赞赏码占位图", "微信赞赏码")
    updated = updated.replace(
        "\n发布前请把占位图替换为真实微信赞赏码：`assets/support-wechat.png`，并把上面的图片路径改成真实文件。\n",
        "\n",
    )
    if updated == text:
        raise RuntimeError("README does not contain the expected support QR placeholder")
    if not dry_run:
        README.write_text(updated, encoding="utf-8")
    return True


def install_image(source: Path, dry_run: bool) -> None:
    if dry_run:
        return
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() == ".png":
        shutil.copy2(source, TARGET)
        return

    sips = shutil.which("sips")
    if not sips:
        raise RuntimeError("non-PNG image requires macOS sips to convert to assets/support-wechat.png")
    subprocess.run([sips, "-s", "format", "png", str(source), "--out", str(TARGET)], check=True)


def main() -> int:
    args = parse_args()
    source = validate_image(args.image)

    print(f"Source image: {source}")
    print(f"Target image: {TARGET}")

    install_image(source, args.dry_run)
    changed = update_readme(args.dry_run)

    if args.dry_run:
        print("Dry run only: no files changed.")
    else:
        print("Installed real support QR image.")
    print(f"README updated: {'yes' if changed else 'already up to date'}")
    print("Next: run python3 tools/check_launch_ready.py")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (FileNotFoundError, RuntimeError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
