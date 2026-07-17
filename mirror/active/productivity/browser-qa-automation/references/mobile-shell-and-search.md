# Mobile shell and search consolidation QA

Use this checklist when a shared dock/menu/header overlaps content, or when a dedicated search page is being folded into an existing directory/browse surface.

## What to verify
- Compare the same chrome element across multiple routes:
  - `getBoundingClientRect()` for the dock/menu/header/footer
  - `position: fixed` elements should match across pages and hashes
- Check for *visual overlap* separately from *routing*:
  - inspect the target anchor `href`
  - use `document.elementFromPoint()` or click tests to ensure the topmost hit target is the intended control
  - verify the same tap area does not open a neighbor control or global menu
- If results are hidden by default, verify the visibility toggle path:
  - search surface starts hidden
  - click/tap on search exposes the same result list used by browse mode
  - a “show all” action should only change visibility/state, not navigate away
- For intent-state splits on the same page, verify `#browse` and `#search` (or equivalent flags) separately and confirm the dock points to the right state in each case.

## Search consolidation pattern
- Prefer one interactive surface when the directory already has rich browse/filter controls.
- Preserve old URLs with a redirect to the new surface or hash state so bookmarks keep working.
- Keep discovery broad enough to include attached content terms (for example, event or related-item keywords) so search quality does not regress when pages are merged.
- Keep the search box minimal; put explanatory copy in nearby labels, not inside the input chrome.
- Center search/filter pill rows on mobile so the control cluster reads as one intentional surface.

## Fast probe recipe
1. Load several representative routes.
2. Measure the shared chrome rect on each route.
3. Scroll near the bottom and confirm no actionable content sits under the fixed dock.
4. Trigger the suspected link/button and inspect the resulting `href` or click target.
5. Re-test on a mobile viewport.

## Notes
- Use this for dock drift, sticky footer overlap, drawer collision, and “wrong page opened” reports where the bug may be hit-testing rather than bad URLs.
- This file is intentionally compact so it can be reused as a checklist during browser QA.
- When data-driven rendering is involved, wait for the page to settle before measuring geometry; a hash change can be visible in the URL before content has finished rendering.