# Dedicated Search Surface Pattern

Use this when the dock/search interaction on Acadie.sol starts feeling like a patched subsection inside another page.

## Lesson
Do not keep fighting `directory.html#search` when the product intent is a primary finding action. Mobile browsers often refuse to open the soft keyboard after a route/hash jump plus delayed `.focus()`, even when the input technically becomes `document.activeElement`. That makes programmatic focus a brittle foundation for search feel.

## Preferred product shape
- Dock Search routes to a first-class `search.html` page.
- `search.html` owns the primary search interaction, but its **entry state must stay quiet**: matching site background, one large centered search input, no visible heading/lede except accessible text, no instructional copy, no preloaded results, no empty-state box, and no visible tag/filter row.
- Put filters behind a compact `Filters` pill/menu. Expanding filters is user intent; only then expose Places/Events/Food/etc. and render matching results.
- `search.html` owns the primary search interaction: a minimal input surface, optional filters, result feed, and a clear `View All` / directory escape hatch.
- For Acadie.sol, keep the initial search render non-influential: no preloaded cards, no empty-state card, no instructional paragraph, and no visible suggestion chip row. Filters can exist, but should stay behind a compact control until requested.
- Put `View All` / `Filters` above the input, and place the input lower on mobile near the dock/finger zone. Prefer a transparent underlined input line over a pill/searchbar cage.
- `directory.html` becomes browse-only: full directory cards, entry expansion, no top search box/control-panel mode.
- All stale `directory.html#search`, `data-shell-search`, and custom search-dock event hooks should be removed after the route changes.

## Closed loop
```text
Dock Search → search.html
search.html → results OR View all directory
directory.html → browse cards; dock Search returns to search.html
```

## Data/source pattern
Use `assets/search-index.json` as the all-type feed. A compact item shape can combine:
- `type`
- `id`
- `title`
- `subtitle`
- `badges`
- `terms`
- `url`

This supports search across entries, events, badges/categories, areas, and future keyword/media exports without putting search logic back into the directory page.

## Verification checklist
- Every global dock Search link points to `search.html`.
- No `directory.html#search`, `data-shell-search`, `acadie:searchdock`, `#search-panel`, or old `id="search"` remains in page HTML.
- Browser check: fresh `search.html` has no result cards, no empty-state card, hidden filters, and body background stays on the global token (computed `background-image: none` if no special surface was requested).
- Browser check: type into `#search-input`; result count and cards update.
- Browser check: quick filters such as Events/Places/Food narrow the feed.
- Browser check: `View all directory` points to `directory.html`.
- Browser check: `directory.html` has no old search panel/input and still renders directory cards.
- Run JS syntax, `git diff --check`, shell consistency, and contrast checks before committing.
- Scroll-chrome behavior: scroll down on search page hides fixed controls (`body.search-chrome-hidden`); scroll up restores; input focus always restores; filter menu open blocks hiding.
