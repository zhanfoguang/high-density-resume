# Eval Case: Interview Follow-Up Risk

## Purpose

Test whether the skill acts like a strict interviewer and finds claims that may fail follow-up questions.

## Prompt

```text
Use $high-density-resume 帮我做面试追问风险检查。

请像严格 HR 一样逐条看我的简历，不要润色。只找这些问题：
1. 哪些词可能会被追问？
2. 哪些地方我如果答不上来就应该降级或删除？
3. 哪些工具、数字、项目名需要补证据？
4. 哪些表达可能写得比事实更大？

[Paste resume here]
```

## Expected Behavior

- Focus on risk rather than writing style.
- List likely follow-up questions.
- Identify unsupported tools, rankings, project names, and strong verbs.
- Recommend downgrading or deleting fragile claims.
- Separate strong evidence from fragile wording.

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
