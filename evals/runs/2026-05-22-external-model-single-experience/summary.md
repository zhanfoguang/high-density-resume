# Eval Run: 2026-05-22 External Model Single Experience

Agent/model: External model output supplied by user  
Case: Single experience extraction  
Date: 2026-05-22  

## Score

```text
Workflow routing: 3
Truthfulness: 3
Evidence extraction: 3
Follow-up quality: 3
HR searchability: 2
Interview risk: 3
Total: 17
Pass/fail: Pass
```

## Notes

The model correctly identified the input as a single experience and did not overclaim. It asked about ownership level, PCB modification scope, tools, whether the board was fabricated/soldered/tested/used, the car-number mechanism, exact ranking change, AI tool details, and whether the strategy change was the user's own idea.

HR searchability is scored 2 because final role-specific keywords were deferred until the user confirms details, which is appropriate but not fully expressed yet.

## Follow-Up Changes

Implemented after this run:

- For template-based PCB work, require questions about actual changed circuit/parameters/interfaces/layout and whether the board was fabricated, soldered, tested, or used.
- For ranking improvement claims, require exact before/after numbers or percentage/range before using improvement wording.
- Add a risk-box rule: if the user cannot provide verifiable details or numbers, recommend excluding the item or keeping only a conservative learning/participation statement.
