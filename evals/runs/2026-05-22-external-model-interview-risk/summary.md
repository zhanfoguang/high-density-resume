# Eval Run: 2026-05-22 External Model Interview Risk

Agent/model: External model output supplied by user  
Case: Interview follow-up risk  
Date: 2026-05-22  

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

## Notes

The model produced a useful interview-risk report with concrete follow-up questions, downgrade/delete conditions, evidence gaps, and high/medium/low risk labels.

However, because the prompt did not include a real resume body, the model constructed a sample resume from prior context. That is acceptable only when the user explicitly requests a simulation. For production skill behavior, interview-risk checks should first confirm that resume text or bullets were provided. If missing, ask for the content instead of inventing or reconstructing a sample.

## Follow-Up Changes

Implemented after this run:

- Interview-risk checks now require input completeness checks just like existing-resume diagnosis.
- If no resume/bullets are provided, ask for content and do not simulate unless explicitly requested.
- Risk output should include "delete/downgrade if you cannot answer..." conditions.
- Evidence gaps should use priority labels: red = must prove or delete, yellow = should prove, green = optional context.
- Ranking-improvement claims without before/after numbers are explicitly high risk.
