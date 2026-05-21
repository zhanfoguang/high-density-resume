# Eval Run: 2026-05-22 External Model From-Scratch

Agent/model: External model output supplied by user  
Case: From-scratch mining  
Date: 2026-05-22  

## Score

```text
Workflow routing: 3
Truthfulness: 3
Evidence extraction: 2
Follow-up quality: 3
HR searchability: 3
Interview risk: 3
Total: 17
Pass/fail: Pass
```

## Notes

The model correctly recognized sparse input and asked follow-up questions instead of drafting a full resume. It covered target role, education, Formula Student details, ownership, tools, measurable outcomes, interview risk, and HR keywords.

The only missing behavior was an explicit current-info / missing-facts / possible-resume-direction table before the question list.

## Follow-Up Changes

Implemented after this run:

- From-scratch workflow now requires a current-info / missing-facts / possible-resume-direction table.
- Low-experience user mining now explicitly includes course labs, coursework, self-learning artifacts, small builds, team micro-tasks, and AI-assisted learning cases.
