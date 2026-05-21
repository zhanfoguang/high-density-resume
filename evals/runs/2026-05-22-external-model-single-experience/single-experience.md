# Eval: External Model Single Experience Extraction

## Model Output Summary

The external model:

- Identified the input as a single Formula Student electrical + AI car-number experience.
- Asked for ownership level and team context.
- Asked what was actually changed in the PCB, including schematic, layout, components, interfaces, software, and whether it was fabricated/soldered/tested/used.
- Asked for car-number mechanism, AI tool details, strategy change details, exact before/after ranking, and whether the strategy was independently proposed.
- Provided only conservative bullets before facts were confirmed.
- Deferred standard and high-density versions until the user answers.

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

## Skill Improvements

- Ask what was actually changed when the user says "modified PCB from a template."
- Ask whether the PCB was fabricated, soldered, tested, or used.
- Require exact ranking numbers before using "improved ranking" wording.
- Add a risk prompt when details are too thin for resume use.
