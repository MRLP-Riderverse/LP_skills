# Duplicate Guard and Script Notes

Deterministic helper behavior for directory draft intake:

- check inbox drafts before creating a new one
- if a likely duplicate exists, do not overwrite it silently
- if the user asks to draft something that already exists, surface the existing path first
- keep the draft intake workflow focused on preserving raw local meaning

Script reference:
- `scripts/draft_intake.py` is the deterministic renderer/helper for later structured normalization or conversion

Fallback wording for duplicates:
- `I believe you already have an entry for this: <path>`

This note keeps the duplicate rule and helper usage close to the workflow.