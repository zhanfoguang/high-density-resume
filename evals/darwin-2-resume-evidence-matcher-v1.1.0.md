# Darwin 2.0 Review · Resume Evidence Matcher v1.1.0

Scope: `skills/resume-evidence-matcher`

This review used two rounds of independent judges. The first round found a
cross-script blocker; the second round used fresh judges after the fix.

## Blocker Found And Fixed

The original v1.1.0 candidate allowed evidence marked `conflict` to support a
`direct` requirement in `calculate_coverage.py`. This could produce 100%
coverage while `select_resume_content.py` hid the same evidence.

The final candidate enforces:

- `conflict` evidence cannot be cited for coverage;
- `needs-detail` evidence can only support `partial` mappings;
- invalid mappings stop with an explicit error instead of producing a score.

Regression tests cover all three branches, including the valid
`needs-detail + partial` path.

## Independent Final Scores

| Judge | Score | Result |
| --- | ---: | --- |
| Fresh judge A | 94.5 / 100 normalized | Pass, no blocker |
| Fresh judge B | 93.3 / 100 | Pass, no blocker |
| Mean | 93.9 / 100 | Release gate passed |

Both judges confirmed runtime neutrality, resource resolution, narrow-output
routing, conflict handling, evidence-selection behavior, and ZIP hygiene.

## Verification Evidence

- Repository suite: 26 tests passed.
- Competition-directory suite: 17 tests passed.
- Tests rerun from the extracted competition ZIP: 17 tests passed.
- Agent Skill validator: passed for repository and competition copies.
- Release readiness checker: passed for `v1.1.0`.
- ZIP integrity: passed.
- ZIP paths and text: no registry-forbidden platform token, cache, bytecode,
  `.DS_Store`, or Git metadata.

## Evaluation Limit

The deterministic scripts and regression paths were executed as full tests.
Model-generated response quality was assessed by independent dry-run review;
no additional marketplace-runtime installation was performed in this pass.
