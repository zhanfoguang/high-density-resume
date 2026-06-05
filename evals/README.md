# Evals

This folder contains lightweight, human-reviewed evaluations for the High Density Resume skill.

The goal is not automated benchmarking. The goal is to see whether the skill behaves correctly in real resume-writing situations.

## Cases

| Case | Input type | Expected behavior |
| --- | --- | --- |
| [from-scratch](cases/from-scratch.md) | Sparse personal information | Ask follow-up questions before drafting |
| [low-material-student](cases/low-material-student.md) | Student with few obvious achievements | Mine small truthful experiences and unusual signals |
| [single-experience](cases/single-experience.md) | One raw experience | Extract evidence units and bullet options |
| [existing-resume](cases/existing-resume.md) | Complete or partial resume | Diagnose and score before rewriting |
| [dual-ai-review](cases/dual-ai-review.md) | Another AI's critique | Classify suggestions instead of blindly accepting |
| [interview-risk](cases/interview-risk.md) | Resume or bullets | Identify follow-up risk and downgrade candidates |

## How To Run

1. Install or load the skill in the target agent.
2. Copy the prompt from one case file.
3. Paste the model output into the case file or a dated copy.
4. Score with [scorecard.md](scorecard.md).
5. Add notes under "Skill Improvements" if the behavior should be improved.

## Pass Criteria

A case passes when the model:

- Chooses the right workflow.
- Does not invent facts.
- Asks for missing evidence when needed.
- Preserves truthful personal recognition.
- Considers target-role fit and HR searchability.
- Flags interview follow-up risk.
