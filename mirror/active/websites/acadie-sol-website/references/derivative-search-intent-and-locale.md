# Derivative directory: search intent, explore intent, and locale defaults

Use this pattern for sibling community nodes such as Manila, without changing the parent Acadie implementation automatically.

## Search/discovery contract

- Do not force users through an intent-choice screen when the product already has a clean search surface.
- During the first usable pass, let **Discover** and **Search** route to the same search-oriented page.
- Start with all published results visible; a query narrows the same result set. **View all** clears the query and restores the full set.
- Keep the surface small: basic search, View all, and a project-log/view-logs link. Remove unused filter/options popovers and dead choice-panel DOM rather than merely hiding them.
- Treat a future Explore/display page as a separate product intention: browse-oriented composition, richer editorial grouping, and different rendering. Do not invent that page while implementing the simpler search contract; capture it as the next IA decision.

## Localization contract

- English is the explicit fallback regardless of `navigator.language`.
- Use a node-specific toggle such as `EN / TL`; do not inherit the parent node's `EN / FR` copy table.
- Persist only supported values (for example `en` and `tl`). Invalid or stale values such as `fr` must fall back to English.
- Provide a complete parallel copy object for the future language, but use steward-supplied translations; do not fabricate localized public copy merely to fill the table.
- Audit static HTML, shared shell copy, dynamic renderer copy, placeholders, result counts, empty states, and data-localization fallbacks together.

## Shared menu geometry

- Menu geometry belongs in the shared shell stylesheet, not page-local styles.
- Set explicit width, max-width, and `box-sizing: border-box` at the mobile breakpoint; use the same explicit desktop width on every route.
- Verify the popup bounds on the homepage and search page at the same viewport, including safe-area offsets. Different apparent sizes usually indicate page-local overrides or inconsistent box sizing.

## Verification

Run an English-first copy audit for stale parent-language strings and keys, syntax-check every inline script, run `git diff --check`, serve every route locally, and verify local/remote commit parity after an authorized push. Review the actual rendered search state at mobile width before declaring the IA change complete.
