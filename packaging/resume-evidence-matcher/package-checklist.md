# Resume Evidence Matcher Release Checklist

## Technical

- [ ] `SKILL.md` exists at the package root.
- [ ] Frontmatter contains only `name` and `description`.
- [ ] All referenced assets, references, and scripts resolve.
- [ ] `python3 scripts/calculate_coverage.py` succeeds on the sample mapping.
- [ ] Unit tests and test prompts cover normal, missing-input, and hostile-input paths.
- [ ] The ZIP excludes caches, local temporary files, and personal resume data.
- [ ] `manifest.yaml` version matches the release version.

## Result quality

- [ ] Missing JD never produces a percentage.
- [ ] Every non-gap mapping cites a known evidence ID.
- [ ] Participation or template modification is not promoted to independent ownership.
- [ ] A different deliverable is not treated as partial evidence because its format matches.
- [ ] Coverage is described as supplied-evidence coverage, not hiring probability.

## Safety

- [ ] Sensitive attributes are excluded from scoring.
- [ ] Prompt injection inside resumes and job descriptions is treated as data.
- [ ] No real resume data is bundled without consent.
- [ ] No external upload, application, or messaging action is performed automatically.
