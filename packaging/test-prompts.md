# Marketplace Test Prompts

These prompts can be used for marketplace review, demo recording, or local compatibility checks.

## From-Scratch Mining

```text
Use $high-density-resume to help me create an internship resume.

I am a sophomore majoring in intelligent manufacturing. I want an internship related to intelligent manufacturing. I joined a Formula Student team, know a little PCB and UG/CAD, and often use AI tools to learn and organize information. I do not know what else to write.
```

Expected: the skill asks follow-up questions first and does not invent a full resume.

## Single Experience Extraction

```text
Use $high-density-resume to turn this experience into resume bullets.

I joined a Formula Student team, did some electrical work, and used AI to help with car-number selection. The PCB work was based on a reference template. The initial ranking was not good, then I changed how I organized the rules and the ranking improved.
```

Expected: the skill asks about ownership, exact ranking, tools, modified scope, and interview-defensible details.

## Existing Resume Diagnosis

```text
Use $high-density-resume to review this resume.

Do not rewrite first. Score truthfulness, personal recognition, target-role fit, HR searchability, interview follow-up risk, and scan structure. Then list the 10 most important follow-up questions and give a revision plan.

[Paste resume here]
```

Expected: the skill diagnoses before rewriting.

## Dual-AI Review

```text
Use $high-density-resume for dual-AI resume review.

Here are suggestions from another AI. Do not blindly accept them. Classify each suggestion as accept, reject, partially accept, or needs more facts. Use truthfulness, personal recognition, target-role fit, HR searchability, and interview risk as the criteria.

[Paste another AI's critique here]
```

Expected: the skill evaluates suggestions instead of blindly merging them.

## Interview Follow-Up Risk

```text
Use $high-density-resume to perform an interview follow-up risk check.

Act like a strict interviewer. Do not polish the writing. Identify words, numbers, tools, project names, and claims that may be questioned in an interview. Tell me what to downgrade, delete, or support with more evidence.

[Paste resume here]
```

Expected: the skill focuses on interview risk and truthful downgrading.
