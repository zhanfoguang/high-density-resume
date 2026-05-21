---
name: high-density-resume
description: Transform raw personal experiences into high-density, evidence-backed resume content. Use when helping a user write, rewrite, review, or pressure-test a resume/CV/resume bullet; turn vague bullets into action + tool/method + result evidence units; build a personal positioning line; remove AI-sounding resume cliches. 中文场景也应触发：写简历、改简历、优化简历、简历润色、挖掘经历亮点、删除套话、构建证据链、准备面试追问。
---

# High Density Resume

Use this skill to turn raw experience into a resume evidence chain. The goal is not to make the user sound bigger; it is to make the truth sharper, denser, and easier to verify.

This skill supports English and Chinese resumes. Preserve the user's language unless they ask for translation.

This skill is designed to be portable across SKILL.md-compatible agents. Do not rely on platform-specific commands or hidden context. Use only the files bundled in this skill directory and the user's supplied resume facts.

## Workflow

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

## Output Rules

- Do not invent facts, numbers, tools, companies, awards, or outcomes.
- Do not upgrade participation into ownership.
- Use specific tool names when known.
- Use conservative wording when the exact number or scope is uncertain.
- Keep final bullets narrow enough to survive interview questioning.
- If evidence is weak, ask one focused follow-up before rewriting.

## Resource Guide

- For the complete method and pressure-test logic, read `references/method.md`.
- For rewrite patterns and Before/After examples, read `references/before-after.md`.
- For user-facing templates, copy or adapt files from `assets/`.
- For an interactive evidence-unit helper, run `scripts/evidence_builder.py`. Use `--lang zh` for Chinese prompts and `--output file.md` to save Markdown.
