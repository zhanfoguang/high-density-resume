# Darwin 2.0 Dry-Run Review

Date: 2026-06-05

Scope: `skills/high-density-resume`

This review applies the Darwin Skill 2.0 rubric as a local dry-run gate. It is not a full independent judge evaluation because no separate with-skill vs baseline model run was executed in this pass.

## Gate Results

| Gate | Evidence | Result |
| --- | --- | --- |
| Runtime neutrality scan | `grep -nE "(在 Claude Code|Claude Code skill|Claude Code 用户|Cursor only|Codex 中|^\[!\[Claude Code|~/\.claude/skills/[a-z]|/plugin install\b)" skills/high-density-resume/SKILL.md README.md` | Pass |
| Test prompts | `skills/high-density-resume/test-prompts.json` contains 3 core scenarios | Pass |
| Failure modes | `SKILL.md` has `Failure Modes And Fallbacks` | Pass |
| Checkpoints | `SKILL.md` has explicit `CHECKPOINTS` | Pass |
| Risk blacklist | `SKILL.md` has `Risk-Action Blacklist` | Pass |
| Resource self-containment | HR/ATS rules moved into `references/hr-ats-screening.md` | Pass |

## 9-Dimension Dry-Run Score

| # | Dimension | Weight | Score | Evidence |
| --- | --- | ---: | ---: | --- |
| 1 | Frontmatter quality | 7 | 9.0 | Clear trigger description in English and Chinese; under 1024 chars |
| 2 | Workflow clarity | 12 | 9.0 | Input routing + ordered evidence-chain workflow |
| 3 | Failure-mode encoding | 12 | 9.0 | Explicit failure/fallback table |
| 4 | Checkpoint design | 6 | 8.5 | Four explicit checkpoints; no autonomous publishing actions |
| 5 | Actionable specificity | 17 | 9.0 | Tables, formulas, fallback wording, blacklist replacements |
| 6 | Resource integration | 4 | 9.5 | Bundled references, assets, script, and test prompts resolve inside the skill package |
| 7 | Architecture | 12 | 8.5 | Core SKILL stays compact; details are progressively disclosed through references |
| 8 | Tested behavior | 23 | 8.0 | Dry-run only; full with-skill vs baseline comparison still needed |
| 9 | Counterexamples / blacklist | 6 | 9.0 | Strong risk-action blacklist covers overclaiming, vague mastery, medical claims, activity-count claims |

Dry-run total:

```text
86.1 / 100
```

## Remaining Darwin Work

To complete a full Darwin 2.0 loop, run the three prompts in `skills/high-density-resume/test-prompts.json` twice:

1. With the skill loaded.
2. Without the skill as a baseline.

Then compare:

- Whether the skill asks better follow-up questions.
- Whether it avoids more overclaims.
- Whether low-material users get more usable evidence-mining paths.
- Whether non-obvious health/care signals are kept conservative.

Record outputs under `evals/runs/YYYY-MM-DD-darwin-2/`.
