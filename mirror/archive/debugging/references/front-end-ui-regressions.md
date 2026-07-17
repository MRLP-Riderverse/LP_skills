# Front-end UI regression debugging notes

Scope: static HTML/JS pages where nav controls, search panels, and theme/language toggles share state.

## Lessons from a search/dock regression
- If a control's label is split into multiple spans/icons for styling, do **not** overwrite the element with `textContent` during updates. Update attributes (`aria-label`, `title`, `data-*`) and keep the child markup intact.
- A button that means "go to the current mode" should focus/scroll the existing panel instead of toggling closed or resetting state.
- Reserve clear/reset behavior for explicit clear/reset actions only.
- For same-page search controls, prefer a button or `preventDefault()` + in-place state change over an anchor navigation that can refresh or re-render the page.
- Fast double-click / smash-click bugs often mean the render path is being entered in the wrong order. Reproduce with rapid clicks and inspect whether the UI is rendering the old mode before the new state settles.

## Dock visibility
- If a dock is missing on one page but visible on others, look for page-local CSS overrides such as `.site-dock { display: none; }` or media-query-specific hiding rules.
- Prefer one visible fixed dock rule per page and adjust bottom padding so content does not collide with it.

## Verification
- Run `git diff --check` after editing.
- Run syntax checks on inline scripts (for example, extract `<script>` blocks and run `node --check`).
- Confirm the control's behavior in a browser: same click should preserve state, not reset it.
