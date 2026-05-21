# Eval: Existing Resume Diagnosis Missing Input

## Model Output Summary

The external model:

- Recognized the user asked for existing-resume review.
- Noticed the resume body was missing.
- Asked the user to paste the resume text.
- Listed the intended diagnostic steps.
- Offered to provide a fictional example only if the user explicitly asks.
- Did not fabricate a resume or diagnosis.

## Result

Pass.

## Skill Improvements

- Add input-completeness check before existing-resume diagnosis.
- Ask for acceptable resume formats: plain text, Markdown, sectioned text, or bullet list.
- Show a diagnosis template if useful, without inventing content.
