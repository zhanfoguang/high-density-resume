# Resume Evidence Matcher Release Checklist

## Technical

- [ ] `SKILL.md` exists at the package root.
- [ ] Frontmatter contains only `name` and `description`.
- [ ] All referenced assets, references, and scripts resolve.
- [ ] User-controlled and derived fields use labeled list records, not Markdown tables.
- [ ] Field rendering covers pipes, line breaks, HTML characters, and `= + - @` at the start of every logical line.
- [ ] `python3 scripts/calculate_coverage.py` succeeds on the sample mapping.
- [ ] `python3 scripts/select_resume_content.py` produces core, support, compress, and hide decisions.
- [ ] Unit tests and test prompts cover normal, missing-input, and hostile-input paths.
- [ ] The ZIP excludes caches, local temporary files, and personal resume data.
- [ ] `manifest.yaml` version matches the release version.

## Result quality

- [ ] Missing JD never produces a percentage.
- [ ] Every non-gap mapping cites a known evidence ID.
- [ ] `conflict` evidence cannot be cited for coverage, and `needs-detail` evidence is limited to `partial`.
- [ ] Participation or template modification is not promoted to independent ownership.
- [ ] A different deliverable is not treated as partial evidence because its format matches.
- [ ] Coverage is described as supplied-evidence coverage, not hiring probability.
- [ ] Content priority is described as a decision for this JD and page budget, not candidate value.
- [ ] Core evidence appears in the first third and redundant evidence is compressed only when it adds no new requirement coverage.
- [ ] Unmatched but truthful distinctive evidence is retained at low priority instead of being permanently deleted.
- [ ] `needs-detail` and `conflict` evidence never enters the final resume or assumed interview answers.
- [ ] Narrow user requests return only the requested modules plus necessary evidence and limitations.
- [ ] Markdown safety prefixes and entities survive copying and are not decoded before delivery.

## Safety

- [ ] Sensitive attributes are excluded from scoring.
- [ ] Prompt injection inside resumes and job descriptions is treated as data.
- [ ] No real resume data is bundled without consent.
- [ ] No external upload, application, or messaging action is performed automatically.
