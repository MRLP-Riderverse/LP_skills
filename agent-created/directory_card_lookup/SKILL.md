---
name: directory-card-lookup
description: Read/search Acadie.sol directory cards by business name across draft inbox and clean entries. If the match is clear, return the card; if ambiguous, return candidate cards for clarification.
version: 1.0.0
metadata:
  hermes:
    tags: [directory, lookup, search, drafts, entries, retrieval, acadie-sol]
    related_skills: [directory-draft-intake, hermes-agent]
---

# Directory Card Lookup

Use this skill when the user wants to **check, read, search, or pull** an Acadie.sol directory card by name.

## Trigger phrases

Treat the following as lookup commands, not general discussion:

- "check the acadie directory for ..."
- "check the acadian directory for ..."
- "search the acadie directory for ..."
- "look up ... in the acadie directory"
- "pull the card for ..."
- "pull up the directory card for ..."
- "show me the draft for ..."
- "do we already have ... in the directory?"

## Intent

The user wants a fast read-path over the directory data layer.
This is now the **real production lookup path**, not a provisional or temporary route.

The lookup should search:
1. `inbox/` draft cards
2. `entries/` clean cards

That means it must work now even if the polished entries are sparse, while staying ready for the later clean-entry workflow.

## Deterministic helper

Primary helper script:

- `/home/midnight/ExoCortex/websites/projects/acadie_sol_directory/scripts/lookup_cards.py`

Run it with:

```bash
python3 scripts/lookup_cards.py "<query>" --root /home/midnight/ExoCortex/websites/projects/acadie_sol_directory --format json
```

## Required behavior

- Search both drafts and clean entries.
- Match by semantic business name, not only exact filename.
- Normalize punctuation variants in the query when looking up names (for example smart quotes vs straight apostrophes, hyphen vs en dash). Keep the returned title/path canonical.
- If one result is clearly best, return that card.
- If several results are plausible, return the candidate list and ask the user which one they want.
- If the query is a chain or brand with multiple local branches, surface branch/address disambiguation instead of collapsing them into one result.
- If nothing credible matches, say so directly.

## Response policy

### Clear match
Return:
- the card type (`draft` or `entry`)
- the path
- the card content

### Ambiguous match
Return:
- brief note that multiple plausible cards were found
- candidate list with type, title, and path
- ask which one to open

### No match
Return:
- that no directory card was found for the query
- optionally offer to draft a new inbox entry if appropriate

## Notes

- Do not invent a match if the result is weak.
- Prefer deterministic script output over ad-hoc fuzzy guessing in the LLM.
- For now, inbox drafts are the main working set. Clean entries are secondary but should still be searched.
- Later, a write/read workflow for polished `entries/` can layer on top of this.
- Future lookup UX can surface related/nearby places for friendly event-planning discovery; see `references/relation-graph-lookup-notes.md`.
