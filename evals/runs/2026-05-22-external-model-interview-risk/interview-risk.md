# Eval: External Model Interview Risk

## Model Output Summary

The external model:

- Recognized the interview-risk task after correcting its initial misunderstanding.
- Constructed a sample resume from prior context because the prompt contained no pasted resume.
- Listed likely interview follow-up questions for risky phrases.
- Gave downgrade/delete advice when the user cannot answer.
- Identified evidence gaps for tools, numbers, and project names.
- Marked likely overclaims.
- Added high/medium/low risk labels.

## Score

```text
Workflow routing: 2
Truthfulness: 2
Evidence extraction: 3
Follow-up quality: 3
HR searchability: N/A
Interview risk: 3
Total: 13/15 applicable
Pass/fail: Conditional pass
```

## Skill Improvements

- If no resume or bullets are pasted, ask for them instead of constructing a sample.
- If the user explicitly asks for a simulation, clearly mark all assumptions.
- Risk checks should include delete/downgrade conditions.
- Evidence gaps should have priority labels.
- Ranking improvement without before/after numbers should be marked high risk.
