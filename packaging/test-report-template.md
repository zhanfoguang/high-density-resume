# Compatibility Test Report

Package: High Density Resume  
Version: {{VERSION}}  
Date: {{DATE}}  

## Package Contents

- [ ] `SKILL.md`
- [ ] `references/user-entry-workflows.md`
- [ ] `references/method.md`
- [ ] `references/before-after.md`
- [ ] `references/dual-ai-review.md`
- [ ] `assets/resume-template.md`
- [ ] `assets/evidence-units.md`
- [ ] `scripts/evidence_builder.py`
- [ ] `manifest.yaml`
- [ ] `LICENSE`

## Local Script Tests

| Test | Command | Result |
| --- | --- | --- |
| Python compile | `python3 -m py_compile scripts/evidence_builder.py` |  |
| Chinese output | `python3 scripts/evidence_builder.py --lang zh --output evidence-zh.md` |  |
| English output | `python3 scripts/evidence_builder.py --lang en --output evidence-en.md` |  |

## Agent Tests

| Agent | Install Method | Prompt | Result |
| --- | --- | --- | --- |
| Claude Code | user-level / project-level | From-scratch mining prompt |  |
| Claude Code | user-level / project-level | Existing resume diagnosis prompt |  |
| Codex | Skills CLI / local copy | Single experience extraction prompt |  |
| Codex | Skills CLI / local copy | Dual-AI review prompt |  |
| OpenClaw-style agent | local copy | Interview follow-up risk prompt |  |

See `test-prompts.md` for the full prompt text.

## Human Eval Summary

Use the repository `evals/scorecard.md` if you run deeper manual evaluations.

| Case | Score | Pass/Fail | Notes |
| --- | --- | --- | --- |
| From-scratch mining |  |  |  |
| Single experience extraction |  |  |  |
| Existing resume diagnosis |  |  |  |
| Dual-AI review |  |  |  |
| Interview follow-up risk |  |  |  |

## Notes

- The package runs locally.
- No network access is required.
- No third-party dependencies are required.
- Marketplace-specific validation must be performed with the target platform's official tools.
