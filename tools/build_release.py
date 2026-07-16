#!/usr/bin/env python3
"""Build a clean release package for a skill in this repository."""

from __future__ import annotations

import argparse
import shutil
import zipfile
from datetime import date
from pathlib import Path


DEFAULT_SKILL = "high-density-resume"
SUPPORTED_SKILLS = (DEFAULT_SKILL, "resume-evidence-matcher")
REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGING_DIR = REPO_ROOT / "packaging"
ROOT_ASSETS_DIR = REPO_ROOT / "assets"
LICENSE_FILE = REPO_ROOT / "LICENSE"


def clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copytree(src: Path, dst: Path) -> None:
    ignore = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")
    shutil.copytree(src, dst, ignore=ignore)


def replace_tokens(text: str, version: str) -> str:
    return text.replace("{{VERSION}}", version).replace("{{DATE}}", date.today().isoformat())


def skill_packaging_dir(skill: str) -> Path:
    if skill == DEFAULT_SKILL:
        return PACKAGING_DIR
    return PACKAGING_DIR / skill


def read_template(packaging_dir: Path, name: str, version: str) -> str:
    return replace_tokens((packaging_dir / name).read_text(encoding="utf-8"), version)


def manifest(packaging_dir: Path, version: str) -> str:
    text = (packaging_dir / "manifest.yaml").read_text(encoding="utf-8")
    lines = []
    for line in text.splitlines():
        if line.startswith("version:"):
            lines.append(f"version: {version}")
        else:
            lines.append(line)
    return "\n".join(lines) + "\n"


def write_release_files(
    release_dir: Path, package_dir: Path, skill: str, version: str
) -> None:
    skill_dir = REPO_ROOT / "skills" / skill
    if not skill_dir.exists():
        raise SystemExit(f"Skill source not found: {skill_dir}")
    packaging_dir = skill_packaging_dir(skill)
    if not packaging_dir.exists():
        raise SystemExit(f"Skill packaging files not found: {packaging_dir}")

    copytree(skill_dir, package_dir)
    (package_dir / "manifest.yaml").write_text(
        manifest(packaging_dir, version), encoding="utf-8"
    )
    shutil.copy2(LICENSE_FILE, package_dir / "LICENSE")

    if skill == DEFAULT_SKILL and ROOT_ASSETS_DIR.exists():
        copytree(ROOT_ASSETS_DIR, release_dir / "assets")

    release_files = {
        "listing.zh.md": (packaging_dir / "listing.zh.md").read_text(encoding="utf-8"),
        "listing.en.md": (packaging_dir / "listing.en.md").read_text(encoding="utf-8"),
        "package-checklist.md": (packaging_dir / "package-checklist.md").read_text(encoding="utf-8"),
        "test-prompts.md": (packaging_dir / "test-prompts.md").read_text(encoding="utf-8"),
        "test-report.md": read_template(packaging_dir, "test-report-template.md", version),
        "release-notes.md": read_template(
            packaging_dir, "release-notes-template.md", version
        ),
    }
    if skill == DEFAULT_SKILL:
        release_files.update(
            {
                "check_launch_ready.py": (
                    REPO_ROOT / "tools" / "check_launch_ready.py"
                ).read_text(encoding="utf-8"),
                "install_support_qr.py": (
                    REPO_ROOT / "tools" / "install_support_qr.py"
                ).read_text(encoding="utf-8"),
            }
        )
    for filename, content in release_files.items():
        (release_dir / filename).write_text(content, encoding="utf-8")


def zip_package(package_dir: Path, zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(package_dir.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(package_dir))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a skill package from this repository."
    )
    parser.add_argument(
        "--skill",
        choices=SUPPORTED_SKILLS,
        default=DEFAULT_SKILL,
        help=f"Skill slug to build. Default: {DEFAULT_SKILL}.",
    )
    parser.add_argument(
        "--version",
        required=True,
        help="Release version, for example 1.0.0.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT / "dist",
        help="Directory for release outputs. Default: ./dist",
    )
    parser.add_argument(
        "--keep-workdir",
        action="store_true",
        help="Keep the expanded package directory next to the zip.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    skill = args.skill.strip()
    version = args.version.strip().lstrip("v")
    release_dir = args.output_dir / f"{skill}-v{version}"
    package_dir = release_dir / skill
    zip_path = release_dir / f"{skill}-skill-v{version}.zip"

    clean_dir(release_dir)
    write_release_files(release_dir, package_dir, skill, version)
    zip_package(package_dir, zip_path)

    if not args.keep_workdir:
        shutil.rmtree(package_dir)

    print(f"Built release package: {zip_path}")
    print(f"Listing copy: {release_dir / 'listing.zh.md'}")
    print(f"Checklist: {release_dir / 'package-checklist.md'}")


if __name__ == "__main__":
    main()
