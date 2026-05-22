# Dual-AI Resume Review

Use this optional workflow when the user wants to refine a resume through multiple AI passes while keeping human control over the final version.

## Core Loop

```text
User facts
-> AI A drafts or maintains the main version
-> AI B reviews and challenges it
-> User selects what to accept, reject, partially accept, or verify
-> AI A updates the version with those decisions
-> Human read-through checks interview risk near the end
```

## Human Control Points

The user should control:

- Truthfulness: what was really done, participated in, or only observed.
- Personal recognition: what makes this person memorable.
- Target-role fit: whether the resume supports the intended role.
- HR searchability: whether real keywords appear naturally.
- Interview risk: whether each claim can survive follow-up questions.

## Reviewer Prompt

Use this prompt when sending a version to another AI or another review pass:

```text
Review this resume from five angles: truthfulness, personal recognition, target-role fit, HR searchability, and interview follow-up risk. Classify each suggestion as accept, reject, partially accept, or needs facts. Do not rewrite everything by default.
```

## Decision Labels

| Label | Meaning |
| --- | --- |
| Accept | Clearly improves truth, structure, keywords, or evidence density |
| Reject | Makes the resume generic, less true, or less distinctive |
| Partially accept | Direction is useful, wording or intensity needs adjustment |
| Needs facts | Could be useful but current evidence is insufficient |

For every risky suggestion, add an interview follow-up scenario:

```text
If interviewer asks "...", can the candidate answer with facts?
```

## Accept More Often

- More precise numbers, dates, tools, audiences, and deliverables.
- Replacing "learned/improved ability" with action and output.
- Downgrading overclaims into truthful scope.
- Aligning target role with first-third evidence.
- Adding real, natural role keywords.

## Reject More Often

- Removing distinctive but truthful signals only to look standard.
- Turning concrete facts into generic capability claims.
- Deleting the strongest engineering or delivery evidence just to be shorter.
- Adding concepts the user cannot explain in an interview.
- Flattening the summary into a template sentence.

## Distinctiveness-Retention Check

Before accepting a suggestion to delete an unusual but truthful experience, check:

- Does it create a memorable signal?
- Can it support cross-domain transfer, craft, precision, communication, judgment, social trust, helping behavior, or team integration?
- Can it be moved to a lower-priority section instead of deleted?
- Would deleting it make the candidate more generic?
- Can the user explain it without distracting from the target role?

Some unusual experiences are valuable because they help the candidate build trust in new groups. For example, basic acupuncture practice may not be a core manufacturing skill, but if the user has repeatedly used it in campus teams to help classmates or teachers with basic relaxation support, it can signal memorability, warmth, offline relationship-building, and team integration. Keep this kind of signal low-priority and conservative. Avoid medical claims such as "treat", "cure", or guaranteed improvement.

Safer wording:

```text
Basic acupuncture theory and practice; used in campus team settings to provide basic relaxation support and build trust in collaborative environments.
```

## Integrity Red Lines

Automatically reject and warn when a suggestion:

- Turns `participated/assisted` into `led`.
- Turns a template-based modification into original design.
- Adds "proficient", "expert", "skilled", or "deep understanding" without project evidence.
- Uses "significant improvement", "greatly improved", or similar wording without exact before/after facts.
- Adds concepts, tools, awards, rankings, or outcomes the user did not provide.

## Summary Rule

The final summary may keep personal texture, but it must be supported by evidence. A strong summary line names a repeated behavior pattern across multiple experiences, not a generic virtue.
