# Eval Run: 2026-05-22 External Model Existing Resume Missing Input

Agent/model: External model output supplied by user  
Case: Existing resume diagnosis with missing resume text  
Date: 2026-05-22  

## Score

This case is evaluated as an input-completeness behavior rather than a normal 18-point resume diagnosis.

```text
Workflow routing: 3
Truthfulness: 3
Evidence extraction: N/A
Follow-up quality: 3
HR searchability: N/A
Interview risk: N/A
Pass/fail: Pass
```

## Notes

The model correctly identified that the user requested existing-resume diagnosis but did not paste a resume. It did not invent a resume, did not simulate facts, and asked the user to provide the resume text before scoring.

## Follow-Up Changes

Implemented after this run:

- Added an input-completeness check for existing-resume diagnosis.
- If the resume is missing, the skill should ask for the resume text and specify acceptable formats.
- The skill may show a diagnostic output template so the user understands what will happen next, but must not fabricate a diagnosis.
