---
name: directory_draft_intake
description: Hyper-low-friction workflow for staging Acadie.sol directory inbox entries from live conversation or public research. Inbox layer is Name + Notes first; cleanup and normalization happen later.
version: 1.4.0
category: community
aliases: [directory-draft-intake, acadie-directory-intake, directory-inbox-draft]
---

# Directory Draft Intake

Use this skill when the user wants to add, draft, or stage an entry for the `acadie_sol_directory` inbox.

This is the **hyper-low-friction inbox layer**.
At this stage, the draft should feel closer to **Name + Notes** than to a form.

## Trigger phrases

Treat the following as intake commands, not open-ended discussion:

- "add this to the acadie directory inbox"
- "add this to the acadian directory inbox"
- "draft this as a manual entry"
- "capture this in person"
- "put this in the inbox"
- any live owner / on-foot intel the user wants preserved as a directory draft

## Intent

The goal is to preserve raw local intelligence with minimal friction and minimal meaning loss.

Core goals:
- capture the entry even when the information is incomplete
- preserve the user’s live wording when it carries local meaning
- avoid making the intake feel like a form
- prevent over-sorting too early
- keep the inbox easy to read later during cleanup
- move structure and parsing pressure to the later normalization pass

## Default attribution rules

Use these defaults unless the user explicitly overrides them:

- **Submitted by:** `Acadie.sol`
- If the user explicitly says they are there, witnessed it, or captured it live, preserve that in notes or admin notes.
- Do **not** force `Source: In person` when the user did not actually say it.
- Public URLs are welcome when present, but never required for inbox capture.

## Inbox principle

**The inbox is not the final schema.**

It is a staging layer.
The point is to preserve raw intelligence in a way that is easy to create now and easy to revisit later.

At this stage, the assistant should optimize for:
- fidelity
- speed
- recoverability
- readability during cleanup

## Minimum viable intake shape

Only one field is truly mandatory:

- **Name**

Everything else can be captured as:

- **Notes**

That means the entry can succeed even if the user gives:
- rough location
- address
- public details
- features
- vibe
- hours caveat
- verification hints
- source context
- owner observations
- mixed notes

All of that can stay in notes at draft stage.

## Preferred inbox draft shape

Use this shape by default for live intake.
Treat `inbox/_template.md` as the canonical reference, with the matching copy in `references/draft-template.md` for the skill backup.

```md
# Draft: <Name>

Category: <coarse type>
Area: <region>
Tags: <optional search hints>

## Description
<short plain-language description of the place>

## Notes
<additional readable context, vibe, and useful local details>

## Public data to carry forward
- Address: <...>
- Hours: <...>
- Phone: <...>
- Email: <...>
- Website: <...>

## Related places
- <nearby venue / sibling branch / corridor anchor>

## Admin notes
- Submitted by : Acadie.sol
- Telegram pass-through complete: [yes/no]
- Raw intake preserved: [yes/no]
- Restructured to template: [yes/no]
```

If there are no true admin notes beyond attribution, keep only:

```md
## Admin notes
- Submitted by : Acadie.sol
```

## Field behavior

### Name
- Required if the user is asking to draft a place.
- Preserve the best available business/place name.
- If the user later corrects the name, patch the title directly.

### Notes
This is the main inbox capture bucket.

Use it for:
- what the place is
- location / address / wayfinding
- public-facing features
- useful local recommendations
- hours caveats
- vibe / felt impression
- witnessed details
- mixed public/admin-ish fragments when early sorting would cause loss

At inbox stage, preserving the phrasing is usually better than prematurely converting it into categories.
Light punctuation or capitalization cleanup is fine if it improves readability, but do not rewrite in a way that changes tone, confidence, or meaning.

### Admin notes
Use for:
- attribution
- explicit verification reminders
- clearly internal follow-up
- known uncertainty the user would want remembered during cleanup

Always keep:
- `Submitted by : Acadie.sol`

Keep admin notes short.
Do not dump half the capture into admin notes just because it is imperfect.

## Reliability rules

- Never fail the draft because phone, hours, email, address, category, or source label are missing.
- Never force a URL.
- Never force an address into a dedicated field at inbox stage.
- Never force wayfinding into its own field at inbox stage.
- Never pad the draft with placeholders like `not provided`.
- Never over-summarize if that would lose the raw felt meaning of the user’s note.
- If a detail is uncertain but useful, preserve it in notes or brief admin notes instead of dropping it.
- Prefer readability over pseudo-structure.
- Before writing a new draft, check `inbox/` for an existing same-name or obvious twin entry.
- If a likely duplicate already exists, do **not** silently overwrite or create a second draft.
- In that case, report back exactly in this shape: `I believe you already have an entry for this: <path>` and wait for the user to decide what to do next.

## Manual capture workflow

1. Read the user’s instruction as an intake command.
2. Extract the name.
3. Check `inbox/` for an existing same-name or obvious twin entry before writing.
4. If a likely duplicate exists, stop and report: `I believe you already have an entry for this: <path>`.
5. If no likely duplicate exists, put everything else into `## Notes` with minimal cleanup.
6. Preserve meaningful wording, including rough location, praise, caveats, and local feel.
7. Add `Submitted by : Acadie.sol` in admin notes unless told otherwise.
8. Only add extra admin notes when there is a real follow-up or verification point worth carrying.
9. Write the draft into `inbox/` without waiting for more fields.

## Later normalization

A later pass can parse the notes into cleaner structure such as:
- category
- area
- address
- wayfinding
- hours
- public notes
- public source
- admin follow-up

That parsing is intentionally postponed.

## Why this shape is preferred

This format is better for live work because:
- it lowers expectations during capture
- it preserves meaning instead of forcing early sorting
- it makes drafts faster to create in person or on the move
- it makes later cleanup easier because the whole raw thought is still visible in one place

## Scrape-ready deterministic helper

The linked `scripts/draft_intake.py` script now mirrors the same notes-first workflow.
It can:
- render a Name + Notes inbox draft
- derive notes from older structured fields when needed
- check `inbox/` for duplicates before writing
- emit the exact duplicate warning message when a twin is found

## Success criteria

A good result is:
- the user can draft an entry quickly during live work
- only the name is required
- the notes preserve the raw local meaning
- the draft is easy to read later during cleanup
- missing structure does not block capture
- later normalization still has enough material to work from
