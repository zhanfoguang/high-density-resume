# Compatibility Test Report

Package: High Density Resume  
Version: {{VERSION}}  
Date: {{DATE}}  

## Package Contents

- [ ] `SKILL.md`
- [ ] `references/user-entry-workflows.md`
- [ ] `references/method.md`
- [ ] `references/hr-ats-screening.md`
- [ ] `references/distinctive-signals.md`
- [ ] `references/before-after.md`
- [ ] `references/dual-ai-review.md`
- [ ] `assets/resume-template.md`
- [ ] `assets/evidence-units.md`
- [ ] `scripts/evidence_builder.py`
- [ ] `manifest.yaml`
- [ ] `test-prompts.json`
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
| Any compatible agent | local copy | Low-material student mining prompt |  |

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
| Low-material student mining |  |  |  |

## Darwin 2.0 Dry-Run Gate

- [ ] Runtime-neutrality scan passes.
- [ ] `SKILL.md` has explicit checkpoints.
- [ ] `SKILL.md` has failure-mode fallbacks.
- [ ] `SKILL.md` has risk-action blacklists.
- [ ] `test-prompts.json` is valid JSON.
- [ ] Skill references resolve inside the packaged skill directory.

## HR/ATS Checks

- [ ] Target keywords appear in evidence bullets, not only in the skills section.
- [ ] Template is conservative and machine-readable.
- [ ] Core information is not stored only in images.
- [ ] The resume states what value the candidate can bring to the target role.

## Marketplace / Monetization Checks

- [ ] `coze-store-listing.zh.md` exists in the release folder.
- [ ] Case cover assets exist if referenced by the Coze listing.
- [ ] Support QR image is real or clearly marked as a placeholder.
- [ ] No copy promises offers, ATS pass, platform approval, or guaranteed income.
- [ ] Public issue templates warn users to remove private resume data.

## Notes

- The package runs locally.
- No network access is required.
- No third-party dependencies are required.
- Marketplace-specific validation must be performed with the target platform's official tools.
