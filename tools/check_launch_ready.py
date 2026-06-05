#!/usr/bin/env python3
"""Check whether the project is ready for public GitHub release."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "skills" / "high-density-resume"


REQUIRED_FILES = [
    "README.md",
    ".github/FUNDING.yml",
    ".github/ISSUE_TEMPLATE/evidence-case.md",
    ".github/ISSUE_TEMPLATE/resume-diagnosis-request.md",
    "assets/support-wechat-placeholder.svg",
    "assets/support-wechat.png",
    "tools/check_launch_ready.py",
    "tools/install_support_qr.py",
    "skills/high-density-resume/SKILL.md",
    "skills/high-density-resume/test-prompts.json",
    "skills/high-density-resume/references/common-frameworks.md",
    "skills/high-density-resume/references/hr-ats-screening.md",
    "skills/high-density-resume/references/distinctive-signals.md",
]


REQUIRED_RELEASE_FILES = [
    "listing.zh.md",
    "listing.en.md",
    "package-checklist.md",
    "test-prompts.md",
    "test-report.md",
    "release-notes.md",
    "assets/support-wechat-placeholder.svg",
    "assets/support-wechat.png",
    "check_launch_ready.py",
    "install_support_qr.py",
]


SKILL_ZIP_REQUIRED = [
    "SKILL.md",
    "manifest.yaml",
    "LICENSE",
    "test-prompts.json",
    "references/hr-ats-screening.md",
    "references/distinctive-signals.md",
    "references/common-frameworks.md",
]


def check(condition: bool, level: str, message: str, rows: list[tuple[str, str]]) -> None:
    rows.append((level if condition else "FAIL" if level == "OK" else level, message))


def file_exists(path: str) -> bool:
    return (REPO_ROOT / path).exists()


def read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def latest_release_dir() -> Path | None:
    dist = REPO_ROOT / "dist"
    if not dist.exists():
        return None
    candidates = sorted(dist.glob("high-density-resume-v*"), key=lambda p: p.stat().st_mtime)
    return candidates[-1] if candidates else None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check public GitHub release readiness.")
    parser.add_argument(
        "--skip-release",
        action="store_true",
        help="Skip dist/release-folder checks. Use in CI before building release artifacts.",
    )
    parser.add_argument(
        "--release-dir",
        type=Path,
        help="Specific release folder to check, for example dist/high-density-resume-v0.2.0.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    rows: list[tuple[str, str]] = []

    for path in REQUIRED_FILES:
        check(file_exists(path), "OK", f"required file exists: {path}", rows)

    if file_exists("skills/high-density-resume/test-prompts.json"):
        try:
            prompts = json.loads(read("skills/high-density-resume/test-prompts.json"))
            check(isinstance(prompts, list) and len(prompts) >= 3, "OK", "skill test-prompts.json has at least 3 prompts", rows)
        except json.JSONDecodeError as exc:
            rows.append(("FAIL", f"test-prompts.json is invalid JSON: {exc}"))

    if file_exists("skills/high-density-resume/SKILL.md"):
        skill = read("skills/high-density-resume/SKILL.md")
        for marker in ("## CHECKPOINTS", "## Failure Modes And Fallbacks", "## Risk-Action Blacklist"):
            check(marker in skill, "OK", f"SKILL.md includes {marker}", rows)
        missing_refs = []
        for match in re.finditer(r"`([^`]+)`", skill):
            ref = match.group(1)
            if ref.startswith(("references/", "assets/", "scripts/")) and not (SKILL_DIR / ref).exists():
                missing_refs.append(ref)
        check(not missing_refs, "OK", f"skill internal references resolve: {missing_refs or 'all ok'}", rows)

    if file_exists("README.md"):
        readme = read("README.md")
        check("## Support" in readme, "OK", "README has Support section", rows)

    real_qr = REPO_ROOT / "assets" / "support-wechat.png"
    readme_text = read("README.md") if file_exists("README.md") else ""
    placeholder = "assets/support-wechat-placeholder.svg" in readme_text
    real_image_link = "assets/support-wechat.png" in readme_text
    if real_qr.exists():
        rows.append(("OK", "real WeChat support image exists: assets/support-wechat.png"))
        check(real_image_link, "OK", "README points to real WeChat support image", rows)
        check(not placeholder, "OK", "README no longer points to support QR placeholder", rows)
    elif placeholder:
        rows.append(("WARN", "README still uses support QR placeholder; replace with assets/support-wechat.png before public launch"))
    else:
        rows.append(("FAIL", "no real support QR and no clear placeholder found"))

    release_dir = None if args.skip_release else args.release_dir or latest_release_dir()
    if release_dir is not None:
        release_dir = release_dir.expanduser().resolve()
    if args.skip_release:
        rows.append(("OK", "release folder checks skipped"))
    elif release_dir is None:
        rows.append(("FAIL", "no dist/high-density-resume-v* release folder found"))
    else:
        try:
            release_label = str(release_dir.relative_to(REPO_ROOT))
        except ValueError:
            release_label = str(release_dir)
        rows.append(("OK", f"latest release folder: {release_label}"))
        for rel in REQUIRED_RELEASE_FILES:
            check((release_dir / rel).exists(), "OK", f"release file exists: {rel}", rows)
        zips = sorted(release_dir.glob("high-density-resume-skill-v*.zip"))
        if not zips:
            rows.append(("FAIL", "release skill zip missing"))
        else:
            zip_path = zips[-1]
            with zipfile.ZipFile(zip_path) as archive:
                names = set(archive.namelist())
            for name in SKILL_ZIP_REQUIRED:
                check(name in names, "OK", f"skill zip contains {name}", rows)

    for level, message in rows:
        print(f"[{level}] {message}")

    has_fail = any(level == "FAIL" for level, _ in rows)
    has_warn = any(level == "WARN" for level, _ in rows)
    if has_fail:
        print("\nRelease readiness: FAIL")
        return 1
    if has_warn:
        print("\nRelease readiness: PASS WITH WARNINGS")
        return 0
    print("\nRelease readiness: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
