# Eval Case: Existing Resume Diagnosis

## Purpose

Test whether the skill diagnoses and scores an existing resume before rewriting.

## Prompt

```text
Use $high-density-resume 审查下面这份简历。

请先不要直接重写。请按真实性、个人识别度、求职方向匹配、HR 搜索率、面试可追问性、结构扫读性打分，然后指出最该追问的 10 个问题，最后给出修改计划。

[Paste resume here]
```

## Expected Behavior

- Identify this as existing-resume diagnosis.
- Score all six dimensions.
- Identify strongest evidence, biggest risk, and narrative mismatch.
- Ask 5-10 specific follow-up questions.
- Give a revision plan before rewriting.

## Model Output

Paste output here.

## Score

```text
Workflow routing:
Truthfulness:
Evidence extraction:
Follow-up quality:
HR searchability:
Interview risk:
Total:
Pass/fail:
```

## Skill Improvements

Record anything that should be changed in the skill.
