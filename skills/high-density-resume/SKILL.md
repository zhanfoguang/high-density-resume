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

- Sparse personal info only, or "I have nothing to write": use the from-scratch / low-material mining workflow.
- One raw experience: extract evidence units and produce bullet options.
- Existing resume: diagnose and score before rewriting.
- Another AI draft or review: use the dual-AI review workflow.

1. Extract evidence units.
   Ask what the user actually did, which tools/methods they used, what changed, and what deliverable exists. Separate `led`, `independently completed`, and `participated/assisted`.

2. Mine overlooked value.
   For early-year, low-experience, or "nothing to write" users, do not stop at internships, awards, and big projects. Mine course labs, coursework, club micro-tasks, helping behavior, unusual skills, small repairs/builds, part-time work, and AI-assisted learning artifacts. Convert them only when there is a real action, method, result, and target-role or enterprise value.

3. Build a positioning line.
   Summarize the user as:

   ```text
   professional base + leverage/tooling + distinctive working habit/background
   ```

4. Rewrite bullets.
   Prefer:

   ```text
   action + tool/method + result
   ```

   Remove claims like "improved ability", "learned knowledge", "responsible and proactive", "familiar with", or "deep understanding" unless backed by evidence.

   If the user mentions STAR, CAR, PAR, XYZ, Google resume formula, accomplishment bullets, or ATS optimization, treat those as external lenses for missing facts. Do not mechanically force the format. Convert them into evidence-chain wording with verified ownership, method, result, and interview defensibility. See `references/common-frameworks.md` when needed.

5. Arrange the resume.
   Use conservative, ATS-friendly structure. Put the strongest, most interview-defensible evidence in the first third. Group more than four experiences into scan-friendly sections such as technical practice, business practice, open source, or community work.

6. Pressure-test.
   For every tool, number, project name, and strong verb, check whether the user can explain the background, action, method, difficulty, and result within a few seconds. Downgrade or delete anything they cannot defend.

When diagnosing an existing resume, include a compact keyword map:

```text
target keyword -> where it appears -> evidence strength -> missing proof
```

Also check enterprise value:

```text
experience -> target-role value -> evidence -> scarcity/recognition signal
```

For weak or non-obvious experiences, translate value before deleting:

```text
experience -> concrete action -> who benefited -> enterprise value -> safe resume placement
```

Useful value categories include professional skill, execution, reduced communication/management cost, team trust, service mindset, organizing ability, fast adaptation, and memorable scarcity.

When checking interview risk, group fragile claims by severity: high, medium, low.

For each interview-risk item, include the claim, likely follow-up question, missing evidence, and delete/downgrade condition.

## CHECKPOINTS

Use these checkpoints to prevent premature or unsafe resume generation:

| Checkpoint | Trigger | Required action |
| --- | --- | --- |
| CHECKPOINT 1: facts before draft | User provides sparse facts or says they have nothing to write | Ask targeted mining questions; do not draft a full resume |
| CHECKPOINT 2: ownership boundary | A claim uses led, owned, responsible for, independently built, expert, proficient, or significantly improved | Verify ownership, tool, scope, and result; downgrade if unverified |
| CHECKPOINT 3: publishable wording | Before producing final resume bullets | Confirm every strong verb, number, tool, ranking, and unusual signal can survive interview follow-up |
| CHECKPOINT 4: health/care signals | User mentions acupuncture, health support, bodywork, counseling, care, or similar personal skills | Use only conservative team/trust wording; do not claim treatment, cure, diagnosis, or medical qualification |

If a checkpoint fails, stop final rewriting and output: missing facts, safest conservative wording, and the exact questions needed to unlock a stronger version.

## Failure Modes And Fallbacks

| Failure mode | Detection | Fallback |
| --- | --- | --- |
| Missing resume text for review | User asks for review/risk check but provides no resume or bullets | Ask for plain text, Markdown, sectioned text, or copied bullets; do not simulate unless asked |
| Missing target role | Keywords or positioning cannot be judged | Ask for target role/JD; if unavailable, use a broad direction and mark keyword mapping as provisional |
| Weak ownership evidence | User cannot say whether they led, independently completed, or assisted | Use participated/assisted wording and remove ownership-heavy verbs |
| Missing numbers or rankings | User says improved, better, top, significant, many, or high without context | Ask for before/after numbers and denominator; otherwise use non-quantified conservative wording |
| Tool claim is vague | User says AI tools, CAD, PCB, Python, Excel, or design software without a concrete use case | Ask what input, action, output, and verification existed; otherwise keep only "used/learned" with scope |
| Non-obvious experience looks unrelated | Another reviewer suggests deletion only because it is not target-role technical evidence | Test for trust, service, team integration, scarcity, or cross-domain value; move to low-priority section if defensible |
| Health-related signal risks overclaiming | Wording implies medical effect or professional treatment | Rewrite as learning experience, basic support, trust-building, or team integration; remove effect claims |
| User asks to make it sound stronger | Requested wording exceeds supplied facts | Explain the risk and provide conservative/standard/high-density versions with placeholders for missing proof |

## Risk-Action Blacklist

Automatically reject or downgrade these patterns:

| Do not write | Replace with |
| --- | --- |
| Led/owned/built/designed when the user only participated | Participated in, assisted with, supported, contributed to |
| Proficient/expert/deep understanding without repeated evidence | Used X to complete Y, learned X through Z, familiar with a defined scope |
| Significant improvement without numbers | Improved after [confirmed before/after], or "supported optimization" if numbers are missing |
| Independently designed from scratch when based on a template | Modified from a reference template, adjusted specific components/layout/docs |
| Medical treatment, cure, diagnosis, or guaranteed improvement | Basic learning/practice, relaxation support, trust-building, team integration |
| Activity count as ability | Specific role, action, beneficiary, deliverable, and enterprise value |
| Keyword list detached from evidence | Natural keyword placement inside evidence-backed bullets |
| Formula-perfect bullet with unverified facts | Conservative bullet plus questions for missing ownership, metric, or method |

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
- When the user says they "only participated in activities", do not treat activity count as evidence. Ask what role they held, what they did, who benefited, what changed, and what ability or enterprise value it proves.
- Do not mechanically delete truthful but unusual experiences. First test whether they show personal recognition, scarcity, helping behavior, team integration, trust-building, organizing ability, service mindset, or cross-domain learning.
- For health-related or care-related distinctive signals, never claim treatment, cure, medical qualification, or guaranteed improvement. Frame them only as personal skill, helping behavior, trust-building, or team integration when truthful and low-risk.
- For template-based PCB claims, ask what actually changed and whether the board was fabricated, soldered, tested, or used.
- For "ranking improved" or similar claims, require exact before/after numbers or context before using improvement wording.
- If a single-experience claim lacks verifiable details, output a risk note recommending exclusion or conservative participation wording.
- For existing-resume review, check that resume text is actually provided. If missing, ask for plain text, Markdown, sectioned text, or copied bullets; do not simulate a diagnosis.
- For interview-risk checks, also require resume text or bullets. If missing, ask for content and do not construct a sample unless the user explicitly asks for a simulation.
- Do not encourage visual-template novelty. Use familiar, machine-readable resume structure; make the content distinctive, not the layout.
- Treat HR searchability as real keyword distribution: target keywords should appear naturally in evidence bullets, not only in a keyword list.
- Treat STAR/CAR/PAR/XYZ/ATS advice as adapters, not overrides. The strongest formula is still unsafe if the user cannot prove the ownership, metric, method, or result.

## Resource Guide

- For STAR/CAR/PAR/XYZ and widely shared resume formulas, read `references/common-frameworks.md`.
- For HR/ATS screening, conservative templates, and enterprise-value checks, read `references/hr-ats-screening.md`.
- For input classification and from-scratch/resume-review workflows, read `references/user-entry-workflows.md`.
- For the complete method and pressure-test logic, read `references/method.md`.
- For rewrite patterns and Before/After examples, read `references/before-after.md`.
- For low-material users and unusual-but-truthful signals, read `references/distinctive-signals.md`.
- For multi-model review or second-opinion workflows, read `references/dual-ai-review.md`.
- For user-facing templates, copy or adapt files from `assets/`.
- For an interactive evidence-unit helper, run `scripts/evidence_builder.py`. Use `--lang zh` for Chinese prompts and `--output file.md` to save Markdown.
