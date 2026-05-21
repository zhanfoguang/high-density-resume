# Evaluation Scorecard

Use this scorecard for each test case. Total score: 18. A solid pass is 14+ with no fabrication.

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Workflow routing | Wrong workflow | Partly right but misses input type | Correct workflow with minor gaps | Clearly chooses the right workflow and explains why |
| Truthfulness | Invents facts | Some unsupported claims | Mostly grounded | Strictly grounded and marks unknowns |
| Evidence extraction | No evidence units | Finds actions only | Finds action + tool/result | Produces clear action + tool/method + result units |
| Follow-up quality | No useful questions | Generic questions | Useful missing-fact questions | Precise questions about ownership, scope, tools, results, and risk |
| HR searchability | Ignores keywords | Adds generic keywords | Finds relevant keywords | Uses only truthful, natural target-role keywords |
| Interview risk | Ignores risk | Mentions risk vaguely | Flags some fragile claims | Clearly marks what to downgrade, delete, or support |

## Automatic Fail

Mark the case as failed if the model:

- Invents awards, numbers, tools, companies, rankings, or outcomes.
- Turns participation into ownership.
- Writes a full resume from sparse input without asking questions.
- Deletes the user's strongest truthful evidence without reason.
- Optimizes for style while ignoring interview risk.

## Result

```text
Case:
Agent/model:
Date:
Score:
Pass/fail:
Main failure:
Skill improvements:
```
