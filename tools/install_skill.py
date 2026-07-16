#!/usr/bin/env python3
"""Install a skill from this repository into a local agent skill folder."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


DEFAULT_SKILL = "high-density-resume"
SUPPORTED_SKILLS = (DEFAULT_SKILL, "resume-evidence-matcher")
REPO_ROOT = Path(__file__).resolve().parents[1]


def default_target_dir(target: str, project: Path | None) -> Path:
    home = Path.home()
    if target == "claude":
        return home / ".claude" / "skills"
    if target == "claude-project":
        if project is None:
            raise SystemExit("--project is required for --target claude-project")
        return project / ".claude" / "skills"
    if target == "codex":
        return home / ".codex" / "skills"
    if target == "openclaw":
        return home / ".openclaw" / "skills"
    raise SystemExit(f"Unsupported target: {target}")


def copy_skill(destination_parent: Path, skill: str, force: bool) -> Path:
    source = REPO_ROOT / "skills" / skill
    if not source.exists():
        raise SystemExit(f"Skill source not found: {source}")

    destination = destination_parent / skill
    if destination.exists():
        if not force:
            raise SystemExit(
                f"Destination already exists: {destination}\n"
                "Run again with --force to replace it."
            )
        shutil.rmtree(destination)

    destination_parent.mkdir(parents=True, exist_ok=True)
    ignore = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")
    shutil.copytree(source, destination, ignore=ignore)
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install a skill from this repository for a local agent."
    )
    parser.add_argument(
        "--skill",
        choices=SUPPORTED_SKILLS,
        default=DEFAULT_SKILL,
        help=f"Skill slug to install. Default: {DEFAULT_SKILL}.",
    )
    parser.add_argument(
        "--target",
        choices=("claude", "claude-project", "codex", "openclaw", "custom"),
        required=True,
        help="Agent target to install for.",
    )
    parser.add_argument(
        "--path",
        type=Path,
        help="Parent skills directory for --target custom.",
    )
    parser.add_argument(
        "--project",
        type=Path,
        help="Project directory for --target claude-project.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed skill.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.target == "custom":
        if args.path is None:
            raise SystemExit("--path is required for --target custom")
        destination_parent = args.path
    else:
        destination_parent = default_target_dir(args.target, args.project)

    skill = args.skill.strip()
    destination = copy_skill(
        destination_parent.expanduser().resolve(), skill, args.force
    )
    print(f"Installed {skill} to {destination}")


if __name__ == "__main__":
    main()
