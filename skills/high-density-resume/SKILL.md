---
name: high-density-resume
description: Transform raw personal experiences into high-density, evidence-backed resume content. Use when helping a user write, rewrite, review, or pressure-test a resume/CV/resume bullet; turn vague bullets into action + tool/method + result evidence units; build a personal positioning line; remove AI-sounding resume cliches. 中文场景也应触发：写简历、改简历、优化简历、简历润色、挖掘经历亮点、删除套话、构建证据链、准备面试追问。
---

# High Density Resume

Use this skill to turn raw experience into a resume evidence chain. The goal is not to make the user sound bigger; it is to make the truth sharper, denser, and easier to verify.

This skill supports English and Chinese resumes. Preserve the user's language unless they ask for translation.

This skill is designed to be portable across SKILL.md-compatible agents. Do not rely on platform-specific commands or hidden context. Use only the files bundled in this skill directory and the user's supplied resume facts.

## Workflow

First classify the user input:

- Sparse personal info only: use the from-scratch mining workflow.
- One raw experience: extract evidence units and produce bullet options.
- Existing resume: diagnose and score before rewriting.
- Another AI draft or review: use the dual-AI review workflow.

1. Extract evidence units.
   Ask what the user actually did, which tools/methods they used, what changed, and what deliverable exists. Separate `led`, `independently completed`, and `participated/assisted`.

2. Build a positioning line.
   Summarize the user as:

   ```text
   professional base + leverage/tooling + distinctive working habit/background
   ```

3. Rewrite bullets.
   Prefer:

   ```text
   action + tool/method + result
   ```

   Remove claims like "improved ability", "learned knowledge", "responsible and proactive", "familiar with", or "deep understanding" unless backed by evidence.

4. Arrange the resume.
   Put the strongest, most interview-defensible evidence in the first third. Group more than four experiences into scan-friendly sections such as technical practice, business practice, open source, or community work.

5. Pressure-test.
   For every tool, number, project name, and strong verb, check whether the user can explain the background, action, method, difficulty, and result within a few seconds. Downgrade or delete anything they cannot defend.

When diagnosing an existing resume, include a compact keyword map:

```text
target keyword -> where it appears -> evidence strength -> missing proof
```

When checking interview risk, group fragile claims by severity: high, medium, low.

## Output Rules

- Do not invent facts, numbers, tools, companies, awards, or outcomes.
- Do not upgrade participation into ownership.
- Use specific tool names when known.
- Use conservative wording when the exact number or scope is uncertain.
- Keep final bullets narrow enough to survive interview questioning.
- If evidence is weak, ask one focused follow-up before rewriting.
- Do not finalize high-density bullets that depend on missing numbers, rankings, ownership scope, or tool details. Use placeholders or conservative wording until the user confirms them.
- For from-scratch users, show a current-info / missing-facts / possible-resume-direction table before listing follow-up questions.
- For early-year or low-experience users, mine course labs, coursework, self-learning artifacts, small builds, team micro-tasks, and AI-assisted learning cases before concluding there is not enough experience.

## Resource Guide

- For input classification and from-scratch/resume-review workflows, read `references/user-entry-workflows.md`.
- For the complete method and pressure-test logic, read `references/method.md`.
- For rewrite patterns and Before/After examples, read `references/before-after.md`.
- For multi-model review or second-opinion workflows, read `references/dual-ai-review.md`.
- For user-facing templates, copy or adapt files from `assets/`.
- For an interactive evidence-unit helper, run `scripts/evidence_builder.py`. Use `--lang zh` for Chinese prompts and `--output file.md` to save Markdown.
