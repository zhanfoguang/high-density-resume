# Release Package Checklist

Use this before uploading a commercial or marketplace package.

## Technical

- [ ] `SKILL.md` exists at package root.
- [ ] `SKILL.md` frontmatter has `name` and `description`.
- [ ] `references/`, `assets/`, and `scripts/` paths referenced by `SKILL.md` exist.
- [ ] Python scripts run with the system Python and no third-party dependencies.
- [ ] Package zip does not include `.git`, caches, local temp files, or personal data.
- [ ] `manifest.yaml` version matches the release version.

## Content

- [ ] Listing title is clear.
- [ ] Short description explains the resume evidence-chain value.
- [ ] Long description includes target users, use cases, privacy, and limits.
- [ ] Screenshots or demo video are prepared if the platform requires them.
- [ ] Pricing and free/paid boundaries are clear if used commercially.

## Compliance

- [ ] License is included.
- [ ] No proprietary third-party material is bundled.
- [ ] No real resume data is included without consent.
- [ ] Marketplace-specific rules have been checked manually.

## Suggested Test Prompt

```text
Use $high-density-resume to rewrite this raw experience into resume bullets:

I joined a Formula Student team and helped with electrical work. I modified a PCB from a reference template, used Altium Designer, and supported hard-wiring debugging. I also used Codex to organize car-number rules. The rank improved from 31st in the morning to 19th.
```
