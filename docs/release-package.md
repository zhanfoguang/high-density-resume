# Release Package Guide

This repository is the open-source home of the High Density Resume skill suite. Marketplace distribution should use a generated release package instead of depending on the GitHub repository directly.

## Build

```bash
python3 tools/build_release.py --version 1.0.0
```

The default is `high-density-resume`. Build the JD evidence matcher with:

```bash
python3 tools/build_release.py --skill resume-evidence-matcher --version 1.0.0
```

Output:

```text
dist/high-density-resume-v1.0.0/
├── high-density-resume-skill-v1.0.0.zip
├── listing.zh.md
├── listing.en.md
├── package-checklist.md
├── test-prompts.md
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

For `high-density-resume`, `references/` includes user-entry workflow routing, the core method, Before / After patterns, and the optional dual-AI review workflow. For `resume-evidence-matcher`, it includes the evidence-chain method, matching rubric, and employment-safety boundaries.

## What To Upload

Upload the selected `<skill>-skill-vX.Y.Z.zip` to the target marketplace if it accepts a generic `SKILL.md` package.

Use the extra Markdown files for:

- Marketplace description copy.
- Review checklist.
- Test prompts.
- Compatibility test report.
- Release notes.

Before building a final marketplace package, run `python3 -m unittest discover -s tests -v` for both skills. The original `high-density-resume` skill also has deeper model behavior cases in `evals/`.

Run the selected skill's release checks with:

```bash
python3 tools/check_launch_ready.py --skill resume-evidence-matcher --skip-release
```

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
