#!/usr/bin/env python3
"""Install the high-density-resume skill into common agent skill folders."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SKILL_NAME = "high-density-resume"
REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "skills" / SKILL_NAME


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


def copy_skill(destination_parent: Path, force: bool) -> Path:
    if not SOURCE.exists():
        raise SystemExit(f"Skill source not found: {SOURCE}")

    destination = destination_parent / SKILL_NAME
    if destination.exists():
        if not force:
            raise SystemExit(
                f"Destination already exists: {destination}\n"
                "Run again with --force to replace it."
            )
        shutil.rmtree(destination)

    destination_parent.mkdir(parents=True, exist_ok=True)
    ignore = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")
    shutil.copytree(SOURCE, destination, ignore=ignore)
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install the high-density-resume skill for local agents."
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

    destination = copy_skill(destination_parent.expanduser().resolve(), args.force)
    print(f"Installed {SKILL_NAME} to {destination}")


if __name__ == "__main__":
    main()
