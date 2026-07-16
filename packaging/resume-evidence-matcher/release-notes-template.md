# Resume Evidence Matcher {{VERSION}}

Release date: {{DATE}}

## Highlights

- Added atomic JD requirement parsing and traceable evidence IDs.
- Added deterministic overall, must-have, and preferred evidence coverage.
- Added grounded resume rewriting, material-gap separation, and interview-risk checks.
- Added fallbacks for missing input, unreadable files, conflicting facts, prompt injection, and biased requirements.

## Compatibility

- Standard `SKILL.md` package.
- Python 3.10+ for the optional deterministic coverage script.
- No third-party Python dependencies or network requests.

## Limits

- Requires a concrete JD before calculating coverage.
- Does not predict hiring outcomes or make employment decisions.
