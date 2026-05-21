# Eval Case: From-Scratch Mining

## Purpose

Test whether the skill asks follow-up questions before drafting when the user provides only sparse information.

## Prompt

```text
Use $high-density-resume 帮我写一份实习简历。

我大二，智能制造工程技术专业，想找智能制造相关实习。参加过方程式赛车，会一点 PCB、UG/CAD，也经常用 AI 工具学习和整理资料。其他我不知道怎么写。
```

## Expected Behavior

- Identify this as from-scratch mining.
- Ask for target role, education details, project list, exact actions, ownership level, tools, deliverables, numbers, and interview-defensible details.
- Avoid drafting a complete resume before enough facts exist.
- Produce a missing-facts list or evidence-mining form.

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
