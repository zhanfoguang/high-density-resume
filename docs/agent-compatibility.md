# Agent Compatibility

This repository ships a standard `SKILL.md` package at:

```text
skills/high-density-resume/
```

The skill avoids platform-specific instructions. It uses only the portable core that most SKILL.md-compatible agents understand:

- A skill folder.
- A required `SKILL.md`.
- YAML frontmatter with `name` and `description`.
- Optional `references/`, `assets/`, and `scripts/` folders.

## Install Targets

| Agent / client | Typical install location | Command |
| --- | --- | --- |
| Claude Code, user-level | `~/.claude/skills/high-density-resume` | `python3 tools/install_skill.py --target claude` |
| Claude Code, project-level | `.claude/skills/high-density-resume` | `python3 tools/install_skill.py --target claude-project --project .` |
| Codex / Skills CLI | Managed by Skills CLI | `npx skills add zhanfoguang/high-density-resume@high-density-resume` |
| Local Codex folder | `~/.codex/skills/high-density-resume` | `python3 tools/install_skill.py --target codex` |
| OpenClaw-style local agents | `~/.openclaw/skills/high-density-resume` | `python3 tools/install_skill.py --target openclaw` |
| Any SKILL.md-compatible agent | Custom skills directory | `python3 tools/install_skill.py --target custom --path /path/to/skills` |

## Claude Code

Claude Code can load skills from user-level and project-level skill folders. For this project:

```bash
python3 tools/install_skill.py --target claude
```

Project-local install:

```bash
python3 tools/install_skill.py --target claude-project --project /path/to/project
```

Then ask Claude Code:

```text
Use $high-density-resume to rewrite this resume bullet...
```

## Codex

Install through Skills CLI when published:

```bash
npx skills add zhanfoguang/high-density-resume@high-density-resume
```

For a direct local copy:

```bash
python3 tools/install_skill.py --target codex
```

## OpenClaw And Other Agents

If your agent supports SKILL.md-style skills, copy `skills/high-density-resume/` into its configured skills directory.

For OpenClaw-style local layouts:

```bash
python3 tools/install_skill.py --target openclaw
```

If your agent uses a different directory:

```bash
python3 tools/install_skill.py --target custom --path /path/to/skills
```

The destination path should be the parent skills directory. The script creates:

```text
/path/to/skills/high-density-resume/
```

## Human Use

Humans do not need to install the skill. Use:

- [README](../README.md) for the quick start.
- [method](method.md) for the full method.
- [resume template](../templates/resume-template.md) for writing.
- [rubric](rubric.md) for scoring.
