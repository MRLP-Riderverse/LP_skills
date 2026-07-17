# Shared Surface Regression Checks

Use this when a change touches a shared UI shell across multiple static pages (home / events / directory / entry / etc.).

## What to check
- Search *all* related templates for the shared component, not just the page you started on.
- Look for page-specific class names that drifted (`.dock` vs `.site-dock`, etc.).
- Look for base rules that hide the component on one page and override it elsewhere.
- Check for duplicated selectors, stray partial rules, or accidental copy/paste fragments that can override the intended style.

## Dock / nav checklist
- Confirm the dock is present in the markup on every page that should show it.
- If the dock is intended to be permanent, verify the same markup/state contract on every page instead of treating each page as a separate dock implementation.
- Confirm the dock is not hidden by a base selector in any page stylesheet.
- Confirm mobile media queries still leave enough bottom padding so the dock does not cover content.
- Test the entire interval where dock and page-layout breakpoints overlap. If the dock hides at 900px but page tablet rules begin at 760px, probe an intermediate width such as 820px and assert `padding-bottom >= dock height + 16px`; phone/desktop endpoint checks alone miss this regression.
- Confirm active-state styling is consistent across pages.
- If one page’s dock suddenly falls back to plain text or its icons resize differently, inspect the shared dock spans/selectors first (`.site-dock a span:first-child`, `button.active`, page-specific overrides) before assuming the markup changed.
- If a dock button is meant to be a stable navigation affordance, don’t leave it pre-marked as the active state when that state changes the icon sizing or layout on mobile.

## Menu / destination link pattern
- When the drawer’s centered `✟` is meant to open a page, make it an actual link/button to that target instead of a decorative span or a separate text link elsewhere.
- Keep the centered icon contract consistent on every page so a page-specific copy split cannot accidentally remove the click target.
- If the user says the dock should always be the same, do not add a second, page-local navigation option inside the drawer that duplicates the dock.

## Toggle / focus checklist
- Do not let click focus become the selected-state visual.
- Keep `:focus-visible` separate from toggle/selected styling.
- If a toggle should read as “paired opposites,” use icon or color contrast directly (for example moon vs sun) rather than a generic selection blue.
- If the button must stay keyboard-friendly, preserve a clear custom focus ring while making the click-state purely semantic.
- A clickable `<label>` controlling a hidden checkbox is not keyboard-operable by default. Either use a real button with explicit state wiring or add `role="button"`, `tabindex="0"`, Enter/Space handling, `aria-controls`, and synchronized `aria-expanded` to every launcher. Escape should close the shared drawer and restore focus to the launcher that opened it.

## Overlay / drawer simplification checks
- If a menu drawer is the canonical overlay, remove legacy sibling closers from popovers, filters, or helper panels unless they still serve a distinct state.
- Count the visible close affordances after the change. "One drawer, one close contract" is the goal when the user asked for a single icon/button in the menu system.
- When a menu toggle opens, close any lower-priority popovers first so overlays do not stack visually.
- Verify the drawer and any subordinate overlays cannot both be open at the same time unless that stacking is intentionally part of the interaction model.

## Mobile input zoom checks
- On iOS and similar browsers, search/text inputs can auto-zoom if the computed font size is too small. Check the actual rendered size, not just the stylesheet token.
- If a search field is supposed to be stable on mobile, verify focus behavior at phone width and ensure the field stays at or above the browser’s no-zoom threshold.
- Test the page before and after focus so you can see whether the viewport jumps or the user must pinch back out.

