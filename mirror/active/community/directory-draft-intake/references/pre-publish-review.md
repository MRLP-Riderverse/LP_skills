# Pre-publish Review — Card Copy and Draft Promotion

Use this pass when a batch of directory drafts is being reviewed before promotion, export, commit, or push.

## Review sequence

1. Build the payload without publishing and record `published_count` and `draft_count`.
2. Read each draft as a quick-card record, not only as Markdown.
3. Check that the description is a concise card one-liner and fits the applicable schema limit (Manila EDM's entry schema uses 160 characters for `short_description`).
4. Do not rely on Markdown line breaks to fix card readability: the exporter may collapse whitespace. Rewrite dense copy into a cleaner sentence instead.
5. Normalize canonical fields before promotion:
   - use one schema-allowed category, not slash-combined values
   - standardize area naming and punctuation across the batch
   - keep event lists in notes unless they are intentionally durable identity facts
   - preserve scene-specific language in tags or full notes when it does not belong in the one-liner
6. Treat roving collectives and clustered venues cautiously. A mailing/base address is not automatically a public venue address; label or retain the uncertainty rather than implying a fixed location.
7. Remove unresolved placeholders such as `?` from public-facing relationship lists. Keep them as admin follow-up if they matter.
8. Present proposed copy and field changes for approval when the user asked to review first. Do not edit, promote, or push in the same pass without approval.
9. After approval, promote to canonical `entries/<slug>/entry.md` + `meta.json`, export with stdout inspection, run tests, and only then commit/push.

## Manila EDM router note

The Manila repository's `scripts/route_inbox.py` default root calculation can target the parent workspace rather than the repository root. When running that repository's router, use an explicit root:

```bash
python3 scripts/route_inbox.py --root .
```

Verify that the top-level `inbox/` contains no routed drafts and that the expected files exist under `edm/inbox/` before continuing.

## Review output shape

Report each entry with:

- what is already strong
- concrete cleanup needed
- proposed card description
- category/location/contact concerns
- a clear publish-readiness verdict

Keep the review concise enough for the steward to approve or correct individual copy without wading through the entire raw record.
