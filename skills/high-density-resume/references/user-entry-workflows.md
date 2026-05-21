# User Entry Workflows

Classify the user's input before choosing a workflow. Do not force every user through the same process.

## Decision Tree

| Input | Workflow | Goal |
| --- | --- | --- |
| Sparse personal info only | From-scratch mining | Ask questions to extract experiences and evidence units |
| One raw experience | Evidence-unit extraction | Produce action + tool/method + result bullets |
| Existing resume | Resume diagnosis and reconstruction | Score, diagnose, ask follow-up questions, then rewrite |
| Multiple AI drafts/reviews | Dual-AI review | Help the user accept, reject, partially accept, or verify suggestions |

## From-Scratch Mining

Use when the user provides only basic information such as name, school, major, target role, or a few vague experiences.

Do not draft a full resume immediately. Ask:

1. Target role or direction.
2. Education, major, year, courses, GPA/rank if useful.
3. Projects, competitions, internships, activities, open-source work, or personal works from the last 1-2 years.
4. For each experience: what exactly did the user do?
5. Ownership level: led, independently completed, participated/assisted.
6. Tools, methods, platforms, software, or workflows used.
7. Deliverables, numbers, ranking, users, links, or before/after change.
8. What can and cannot be explained in an interview.
9. Target-role keywords that have real evidence.

Output in this order:

1. Evidence-unit table.
2. Current-info / missing-facts / possible-resume-direction table.
3. Missing facts and follow-up questions.
4. Positioning line.
5. Resume structure.
6. First draft only after enough facts exist.

For early-year students or users with few obvious projects, mine alternative evidence sources:

- Course experiments and lab reports.
- Course design or capstone-style assignments.
- Self-learning notes that produced reusable artifacts.
- Small hands-on builds, repairs, simulations, or debugging attempts.
- Club or team micro-tasks such as documentation, equipment checks, meeting notes, or data organization.
- AI-assisted learning cases where the user can explain the input, process, verification, and output.

Do not treat these as weak by default. Convert them into evidence only when the user can describe a real action, tool/method, and output.

## Single Experience

Use when the user sends one project, competition, activity, or internship note.

Output:

- Evidence unit.
- Follow-up questions.
- Conservative bullet.
- Standard bullet.
- High-density bullet only if key facts are confirmed. If numbers, ownership scope, tools, or results are missing, provide a high-density draft with placeholders instead of pretending the facts are known.

## Existing Resume

Use when the user sends a complete or partial resume.

Do not rewrite first. Diagnose first:

1. Score truthfulness, personal recognition, target-role fit, HR searchability, interview follow-up risk, and scan structure.
2. Identify strongest evidence, biggest risk, and narrative mismatch.
3. Add a compact keyword map: target keyword -> resume location -> evidence strength -> missing proof.
4. Ask 5-10 follow-up questions.
5. Give a revision plan.
6. Rewrite only the parts that are safe to rewrite with available facts.

## Dual-AI Review

Use `references/dual-ai-review.md` when the user brings another model's draft, critique, or suggested changes.

## Defaults

- If material is sparse, ask more and generate less.
- If material is rich, diagnose before rewriting.
- If facts are unclear, downgrade instead of inflating.
- If target role is unclear, ask for it first.
- Even when asked to "just optimize", surface interview-risk questions.
