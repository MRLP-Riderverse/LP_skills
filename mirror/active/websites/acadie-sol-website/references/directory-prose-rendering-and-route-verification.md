# Directory prose rendering and route verification

## Why this exists

The Acadie directory once rendered a card's visible summary from semantic metadata (`category` and derived `tags`), so authored Markdown bullets appeared to the visitor as inferred labels rather than as prose. The Manila renderer's useful pattern is to derive the visible rail from `item.description` / localized description and keep structured metadata for filtering/search.

## Preferred card contract

- Use the authored/exported description for the visible card summary.
- Keep category/tags as machine/filter metadata; do not surface them as the card's primary intention unless explicitly requested.
- If a description uses an em dash as a deliberate summary separator, split it into `first` for the collapsed summary and `rest` for the expanded body. If it has no separator, show the complete sentence in the summary and use notes for additional prose.
- Keep `notes` as readable prose or note content. Do not reinterpret each bullet as a category/tag.
- Full entry pages should show the source description and notes, then structured public/contact rows. Do not duplicate tag chips when the user asked for authored wording.
- Preserve useful public links from `public_data`; linkify URLs and common handles at the renderer boundary.

## Navigation contract

Full-page entry links should return to the unified browse stream with `directory.html#browse`, not the directory splash route. Use `target="_top"` for entry links launched from expandable cards or nested shells.

## Verification recipe

1. Compare the sibling renderer before changing the schema: inspect Manila's `renderCard`, `descriptionParts`, note rendering, and full-page link construction.
2. Validate both source and generated payload fields (`description`, `notes`, `public_data`, `category`, `tags`) before deciding whether the bug is exporter-side or renderer-side.
3. Extract inline scripts and run `node --check` on each temporary JS file; run the directory repo's test suite.
4. Serve the site locally and use headless Chrome with `--virtual-time-budget=3000 --dump-dom` so async JSON rendering completes.
5. Assert that authored prose and notes are present, category/tag chips are absent from the rendered user-facing surface, and the back link contains `directory.html#browse`.
6. After push, repeat the same DOM assertions against the deployed HTTPS route with a cache-busting query when needed, and verify the Pages workflow completed successfully for the pushed SHA.

## Pitfalls

- A successful export does not prove the card uses the source prose; the exporter can produce correct `description` and `notes` while the page chooses `category`/`tags` for its summary.
- A static HTML grep is insufficient for data-driven cards; wait for fetch/render completion in headless Chrome.
- `entry.html` and `directory.html` are separate renderers. Fixing the card does not automatically fix the full-page entry or its back route.
