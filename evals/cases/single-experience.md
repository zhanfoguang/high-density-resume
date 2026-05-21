# Eval Case: Single Experience Extraction

## Purpose

Test whether the skill extracts evidence units from one raw experience and avoids overclaiming.

## Prompt

```text
Use $high-density-resume 帮我把这段经历写进简历。

我参加过方程式赛车队，做过电器相关工作，也用 AI 帮队里抢车号。PCB 是基于参考模板改的，抢车号一开始成绩不太好，后来我调整了一下整理规则的方法，结果排名变好了。
```

## Expected Behavior

- Ask whether the user led, independently completed, or participated.
- Ask what PCB parts were modified, which tools were used, and what results are verifiable.
- Ask for exact ranking and whether the strategy change was the user's own judgment.
- Produce conservative, standard, and high-density bullet options.
- Avoid writing "led electrical system design" or other overclaims.

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
