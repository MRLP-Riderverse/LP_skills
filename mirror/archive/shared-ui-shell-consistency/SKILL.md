---
name: shared-ui-shell-consistency
description: Normalize shared chrome (dock, menu, drawer, header, footer, overlays) so every page in a multipage site renders the same shell and only the page content changes.
---

# Shared UI Shell Consistency

Use this when a user says the dock/menu/header/footer is drifting between pages, especially in static multipage sites where the shell should be identical everywhere.

## Core principle
The shell is global chrome, not a page-local mood ring.
If the dock/menu looks or behaves differently on different pages, treat it as a shared-component regression and normalize it across all pages.

## What to enforce
- One canonical structure for the shell across pages.
- Same element type for the same control everywhere (`a` vs `button` vs `label` should not drift page to page without a functional reason).
- Same order of items.
- Same iconography / labels policy across the site.
- Same drawer/overlay geometry and control placement across the site.
- No page-specific active-state styling unless it is part of the approved global system.
- Remove dead per-page hooks after deleting or changing shell elements.

## Workflow
1. Identify the canonical page or canonical shell block.
2. Compare the problem pages against the canonical structure, not just the visuals.
3. Normalize the markup first.
4. Normalize CSS selectors and spacing next.
5. Remove stale JS hooks, IDs, and label writes that referenced the old structure.
6. Verify by searching all affected pages for leftover page-specific shell IDs/classes/text.
7. If the same shell is repeated across static HTML pages, factor it into one shared shell stylesheet and one shared renderer/state script so drift cannot return. The page should include the shell, not recreate it.

## Static multipage extraction pattern
When the user explicitly says the dock/menu should be global and not page-specific, treat repeated inline shell blocks as architecture debt, not a styling bug.

- Move chrome-only CSS into a shared file such as `assets/site-shell.css`.
- Move the repeated dock/menu/drawer markup and shared state into a single renderer such as `assets/site-shell.js`.
- Let the renderer own only global chrome concerns: dock links, drawer labels, menu open/close, theme toggle, language toggle.
- If you add a fixed global header/banner, treat its spacing as shell-owned too: put the header in shared shell markup/CSS and offset page content globally (for example with shared `body` padding or a shared layout wrapper offset). Do **not** compensate on only one page, or the header will drift into a page-local special case.
- On iPhone/notch-era layouts, plan for safe-area review when adding top-fixed chrome. Keep the header implementation centralized so `env(safe-area-inset-top)` can be introduced once in the shell instead of patching individual pages.
- Let content pages listen for shared events such as `acadie:languagechange`; pages should not attach their own click listeners to global shell controls.
- If a dock control represents a primary page action like Search, prefer a stable route (`search.html`) over hash navigation plus delayed page-local `.focus()`. Mobile soft keyboards often refuse focus after route/render delays. If the product needs one-tap keyboard behavior, design a synchronous same-page overlay instead; do not leave the shell half-global and half-page-local. When using the dedicated route, the first render should be a clean prompt rather than a pre-populated directory feed; keep results reactive to query/filter intent.
- Remove old per-page shell IDs and copy writes after extraction. Page-prefixed shell IDs (`events-menu-*`, `entry-dock-*`) are drift markers.

See `references/static-site-global-shell-extraction.md` for the concrete extraction and verification contract.

## Common pitfalls
- A page uses a `button` where the other pages use an `a`, causing interaction drift.
- A drawer/menu gets slightly different spacing, opacity, or controls ordering on one page.
- A page-local script still writes labels into controls that have become icon-only.
- Page-local theme/language click handlers keep fighting the shared shell after markup extraction.
- Search/hash navigation keeps working on the canonical page but not the normalized pages.
- Programmatic input focus after dock hash navigation technically focuses an input but does not open the mobile keyboard; this is a product-shape problem, not just a JS bug. Promote the interaction to a dedicated route or synchronous overlay. See `references/search-dock-routing-vs-focus.md`.
- Fixed global headers need global layout compensation. If the shell injects a top bar across pages, add the offset in shared shell CSS (`body`/layout root padding) rather than page-local one-offs, or the header will overlap content on some pages and drift on others.
- On iPhone/notched devices, top chrome must use `env(safe-area-inset-top)` and the content offset must match that same calculation. Do not hardcode the header height alone and hope Safari protects it.
- For fixed mobile search chrome above a bottom dock, keyboard-open state should usually hide/duck the dock only. Do not also move the search controls downward into the keyboard lane, or the input bar will appear to drop under the keyboard while typing/results update.
- Cleaning the visible markup but leaving stale event listeners, IDs, or inline shell selectors behind.

See also `references/fixed-header-safe-area-and-mobile-search-chrome.md` for the notch-safe header + keyboard-stable search pattern.
- Adding a new fixed global header and then solving overlap on only one page. If the chrome is global, the content offset must be global too; otherwise the shell regresses into page-specific layout drift.
- Adding top-fixed chrome without explicitly checking notch/safe-area behavior on mobile Safari. Centralize the header so a single safe-area adjustment can cover the whole site.

## Verification
Prefer deterministic checks over eyeballing:
- Search for old shell IDs/classes/text labels across the whole site.
- Count matches and make sure the count is uniform.
- Compare the relevant shell block between pages.
- Check that the same target URLs/hashes are used everywhere.
- Confirm no page keeps a special dock/menu variant.
- For Search specifically, confirm the old hash/focus path is gone (`directory.html#search`, `data-shell-search`, custom search-dock events) and that the dedicated route/overlay handles typing and filtering on its own.
- When adding a fixed header/banner, verify across at least a few representative pages that the first visible content starts at or below the header bottom. This catches the classic regression where shared chrome is fixed but page content still starts at `top: 0`.
- For top-fixed mobile chrome, include a quick iPhone/notch review step so safe-area issues are caught before the user does.

## Support files
- `references/global-shell-consistency.md` — canonical invariants, drift patterns, and a compact checklist for multipage shell normalization.
- `references/search-dock-routing-vs-focus.md` — when to replace dock hash navigation/programmatic focus with a stable search route or synchronous overlay.
