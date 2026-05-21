# High Density Resume

## One-line Summary

Write resumes with evidence chains: turn raw experience into specific, verifiable, interview-ready resume bullets.

## Who It Is For

- Students, interns, career switchers, and early-career candidates.
- Engineering, technical, product, operations, and business-practice candidates.
- People who have real experience but struggle to extract strong resume evidence.
- Anyone trying to avoid generic AI-written resume cliches.

## Core Capabilities

- Convert raw experience into `action + tool/method + result` evidence units.
- Route users into from-scratch mining, single-experience extraction, existing-resume review, or multi-model review workflows.
- Separate led, independently completed, and participated/assisted scopes.
- Build a positioning line from professional base, leverage/tooling, and distinctive working habit/background.
- Rewrite vague resume bullets into interview-defensible bullet points.
- Support an optional dual-AI review workflow where one model drafts, another reviews, and the user controls truthfulness, personal recognition, target-role fit, HR searchability, and interview risk.
- Provide templates, evidence-unit tables, Before/After examples, and pressure-test checklists.

## How To Use

After installing the skill, ask your agent:

```text
Use $high-density-resume to rewrite the following raw experience into resume bullets and tell me what needs follow-up evidence.
```

You can also run the local helper:

```bash
python3 scripts/evidence_builder.py --lang en --output evidence.md
```

## Highlights

- Does not invent facts or inflate ownership.
- Supports Chinese and English resumes.
- No third-party dependencies and no server required.
- Works with Claude Code, Codex, OpenClaw-style agents, and other `SKILL.md`-compatible tools.

## Privacy

The skill runs locally, makes no network requests, and does not store resume data. Users should avoid entering unredacted sensitive information.
