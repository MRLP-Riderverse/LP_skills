# Directory/search dock focus regressions

Use this when a global bottom dock has a search button that should open/focus a page-owned search UI, especially on mobile where focus can summon the keyboard and disturb viewport scroll.

## Durable lesson
A global shell link like `directory.html#search` is fine for cross-page navigation, but on the destination/search page itself it should not rely on a same-page hash jump. Same-page hash navigation can scroll the target under fixed chrome, blur/refocus at odd times, and create mobile keyboard/layout artifacts that look like the dock moved.

## Pattern
- Keep the shell global: do not add page-specific dock markup.
- Mark the shared dock search link with a neutral hook, e.g. `data-shell-search`.
- In the shared shell, if already on the directory/search page:
  - `event.preventDefault()`
  - dispatch a page-content event such as `acadie:searchdock`
- In the directory/search page:
  - listen for `acadie:searchdock`
  - open/show the search panel
  - close any page-owned filter popover first
  - scroll the search panel deliberately if needed
  - focus the real input with `focus({ preventScroll: true })`
- If the search panel is already open, refocus the actual `#search` input; do not only scroll the panel.

## Menu/dock layering check
Search pages often have fixed top navs, filter popovers, or local tool docks. The global drawer/backdrop/dock should sit above these with one shared z-index ladder, not page-local overrides.

Suggested ordering:
- page-local fixed header/search UI: lower layer
- drawer backdrop: higher layer
- drawer panel: above backdrop
- bottom dock: highest shared chrome layer

Use `isolation: isolate` on the dock if page stacking contexts interfere.

## Verification probe
In a mobile Puppeteer viewport:
1. Load `directory.html`.
2. Click `.site-dock a[data-shell-search]`.
3. Assert `document.activeElement.id === 'search'`.
4. Type text and assert `#search.value` changed.
5. Click the dock search button again while already in search mode.
6. Type more text and assert the same `#search` value changed.
7. Assert `location.hash` did not change on the same-page click.
8. Compare `.site-dock.getBoundingClientRect().top` before/after click/type; it should remain stable.
9. Open the menu and assert the drawer z-index is above page-local fixed nav/popovers.
