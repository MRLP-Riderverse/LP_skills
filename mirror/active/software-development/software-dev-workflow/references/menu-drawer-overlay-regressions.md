# Menu / Dock Overlay Regression Notes

## Context
Acadie.sol pages use a shared bottom dock plus a floating drawer menu. When simplifying these shells, regressions often come from stale per-page menu items, duplicated close affordances, or a secondary overlay that still exposes its own close control.

## What to check
- Search *all* affected HTML files for stale drawer items, especially old obituary links or page-specific menu labels that should no longer exist.
- Count visible close affordances across the whole shell. The intended pattern is one centered `✟` control in the drawer overlay and no extra close icon inside a secondary panel.
- If a secondary overlay exists (filter popover, modal, side panel), make it collapse when the main drawer opens so the page does not look like it has duplicate cross icons.
- If a dock looks like plain text on one page, inspect the dock icon spans and shared dock selectors for missing sizing / specificity drift before assuming the markup is gone.
- When the user sees different results on a phone/tablet, verify source first, then consider cached assets or device-specific rendering differences.

## Verification pattern
1. Search for stale ids, links, and labels across every page.
2. Read the live markup for the drawer and dock on the page the user named.
3. Patch the shared shell first; avoid page-local fixes unless the page truly differs.
4. Re-run search to confirm the old affordance is fully gone.
5. Run `git diff --check` before commit.

## Useful search patterns
- `menuObituaries|obituaries-menu-obituaries|href="obituaries.html"`
- `drawer-close|close-filters|drawer-actions-right|drawer-actions-left`
- `site-dock a span:first-child|site-dock label span:first-child`
