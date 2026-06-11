# GBrain sync verification for QuickThoughts notes

Use this when a user asks whether a note has reached GBrain, not just whether it exists in `QuickThoughts.txt`.

## Core distinction

- `note` capture → appends to `QuickThoughts.txt`
- GBrain sync → indexes the note into GBrain's searchable page store

A QuickThoughts append is **not** proof of GBrain sync.

## Verification steps

1. Confirm the note landed in `QuickThoughts.txt` via the `note` CLI output or the new bottom entry.
2. Check GBrain directly for the indexed page or daily page that should contain the note.
3. Prefer inspecting the page content itself over relying only on search snippets or partial search hits.
4. If search results are ambiguous, list pages / locate the relevant daily page and read the page body.
5. Only claim sync when the note is visible in GBrain content, not merely in the inbox file.

## Practical caution

- Search hits can be noisy or low-relevance.
- Empty page lists or weak search results should be treated as evidence that sync may not have happened yet.
- If the user asks for verification, say whether the note is present in GBrain proper or only in the QuickThoughts inbox.
