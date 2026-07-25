# Directory Content Authority and Route Verification

Use this reference when reviewing a static directory whose source records contain both authored Markdown and structured metadata.

## Source → payload → renderer audit

Trace one representative entry end to end:

1. Read `entries/<slug>/entry.md` and `meta.json` side by side.
2. Identify which source owns each public field:
   - title/identity: heading plus metadata identity fields;
   - visible prose: Markdown preamble or an explicitly designated metadata summary;
   - public notes/bullets: Markdown notes section;
   - category/tags: structured metadata taxonomy;
   - contact/social bullets: normalized contact fields plus an explicit `public_data` fallback.
3. Inspect the exporter function that builds the item payload. Record precedence when both Markdown and metadata provide a value.
4. Inspect the client renderer and map every payload field to visible DOM. Search for fields that are used only for filtering/search but accidentally rendered as public content.
5. Compare a known-good derivative implementation, but verify the live artifact rather than assuming the source template and generated site are synchronized.

## Durable content invariant

Do not silently replace authored public prose with inferred or stale metadata. If Markdown is the editorial source of truth, use its non-empty prose as the visible description and use metadata summary only as fallback. Preserve note bullets as visible notes/list items; never derive category or tags from those bullets unless that behavior is explicitly part of the content contract. Keep taxonomy and verification/routing fields available for search/filtering without presenting them as the authored card copy.

A useful regression fixture has deliberately different Markdown prose and `meta.json.short_description`; the exported `description` must match the declared authority, while `category` and `tags` must remain the explicit metadata values.

## Public-data completeness

A renderer that only displays normalized keys such as address, hours, phone, email, and website can drop authored social/contact bullets. Carry an explicit `public_data` array through the payload and render it in expanded cards/full pages, or document and test a deliberate omission policy.

## Hash-route verification

For static entry pages, test all navigation variants:

- no slug fallback;
- not-found fallback;
- normal footer Back link;
- draft redirect;
- full-page link from a card.

If the directory has an intro state and a browse state, `directory.html` and `directory.html#browse` are not equivalent. The back link must target the state users expect, and the deployed/generated artifact must be checked because a local source fix may not be reflected in the served HTML.

## Review evidence format

Report exact file/function/line ranges and one concrete source-to-payload mismatch. State whether the local artifact is still faulty or already contains the proposed fix; do not claim a current defect from an older copy. If no files may be changed, provide a minimal patch plan and regression tests instead of editing or regenerating outputs.
