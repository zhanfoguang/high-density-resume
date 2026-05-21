# Compatibility Test Report

Package: High Density Resume  
Version: {{VERSION}}  
Date: {{DATE}}  

## Package Contents

- [ ] `SKILL.md`
- [ ] `references/method.md`
- [ ] `references/before-after.md`
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
| Claude Code | user-level / project-level | Rewrite raw resume experience |  |
| Codex | Skills CLI / local copy | Rewrite raw resume experience |  |
| OpenClaw-style agent | local copy | Rewrite raw resume experience |  |

## Notes

- The package runs locally.
- No network access is required.
- No third-party dependencies are required.
- Marketplace-specific validation must be performed with the target platform's official tools.
