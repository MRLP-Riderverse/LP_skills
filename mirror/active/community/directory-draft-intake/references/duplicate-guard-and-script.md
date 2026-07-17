# Duplicate guard and deterministic script notes

## What changed

The directory draft intake workflow now carries the duplicate-safety rule in three places:

1. the live `directory-draft-intake` skill guidance
2. the Telegram `/draftload` preload wording
3. the deterministic `scripts/draft_intake.py` helper

## Duplicate rule

Before writing a new inbox draft, check `inbox/` for a same-name or obvious twin entry.

If a likely duplicate exists:
- do not create a second draft
- do not overwrite silently
- report exactly:

```text
I believe you already have an entry for this: <path>
```

## Deterministic script behavior

The helper script now supports the notes-first inbox shape while remaining backward-compatible with older structured flags.

Useful patterns:

### Render a notes-first draft to stdout

```bash
python3 scripts/draft_intake.py \
  --title 'A&W' \
  --note "A&W on St-Peters Ave in Acadie-Bathurst, next to Place Bathurst Mall and Home Hardware. 24/7 drive-thru accessible. Indoors is open as late as midnight, I believe. I've been there in person; it's quite nice. Home of the A&W Famous Root Beer."
```

### Check duplicates before writing

```bash
python3 scripts/draft_intake.py \
  --title 'Bowlarama Bathurst Bowling & Arcade' \
  --check-duplicate-in /path/to/inbox
```

Expected duplicate outcome:
- exact warning string on stdout
- exit code `2`

### Write directly into an inbox directory

```bash
python3 scripts/draft_intake.py \
  --title 'A&W' \
  --note 'raw local wording here' \
  --check-duplicate-in /path/to/inbox \
  --write-to-inbox /path/to/inbox
```

## Durable lesson

For this directory workflow, duplicate protection should not live only in conversational prompting. It should also exist in the deterministic helper so backup skills and future automation inherit the same safety behavior.
