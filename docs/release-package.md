# Release Package Guide

This repository is the open-source home of High Density Resume. Marketplace distribution should use a generated release package instead of depending on the GitHub repository directly.

## Build

```bash
python3 tools/build_release.py --version 1.0.0
```

Output:

```text
dist/high-density-resume-v1.0.0/
├── high-density-resume-skill-v1.0.0.zip
├── listing.zh.md
├── listing.en.md
├── package-checklist.md
├── test-report.md
└── release-notes.md
```

The zip contains:

```text
SKILL.md
agents/openai.yaml
assets/
references/
scripts/
manifest.yaml
LICENSE
```

## What To Upload

Upload `high-density-resume-skill-vX.Y.Z.zip` to the target marketplace if it accepts a generic `SKILL.md` package.

Use the extra Markdown files for:

- Marketplace description copy.
- Review checklist.
- Compatibility test report.
- Release notes.

## What To Edit Per Platform

Before uploading, adapt platform-specific fields:

- Price and license terms.
- Screenshots or demo video.
- Platform category and tags.
- Required manifest fields.
- Payment and support contact.
- Any platform-specific validator output.

Do not claim compatibility with a marketplace unless you have tested it against that marketplace's official validator or upload flow.

## Open Source Boundary

The GitHub repository should stay useful as a free, open-source version. Commercial packages can be generated from it, but paid distribution should not require users to clone the repository.
