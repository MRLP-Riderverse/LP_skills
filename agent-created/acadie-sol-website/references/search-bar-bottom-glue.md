# Search bar bottom-glue fallback — Acadie.sol

Use this when the dedicated `search.html` result rendering is fine but the fixed search bar still feels like it is traveling with the result list.

## Signal
The user says some version of:
- the results look better now, but the search box is still acting weird
- the bar is leaving with the results
- just glue it to the bottom
- it should simply ride up with the keyboard and come back down with it

That is a product-direction correction, not just a bug report.

## Preferred fallback
When mobile search chrome becomes too stateful, simplify before adding more logic:
1. Keep `.search-controls` in one fixed bottom lane above the dock.
2. Hide/duck only the dock while the search input is focused.
3. Remove scroll-hide/show behavior for the search bar first.
4. Remove custom keyboard-lane math / viewport-driven bar repositioning first.
5. Let the browser's fixed-position + visible viewport behavior do the work while the keyboard opens/closes.

## Why
A search bar controlled by scroll state + focus state + keyboard state + sparse-results state becomes fragile on iPhone. Even if each piece is individually reasonable, together they create the feeling that the bar is attached to the result list instead of the viewport.

## Practical rule
If the user explicitly prefers the simple mental model — "glued to the bottom, pushed up by the keyboard, pulled back down when it closes" — stop being clever. Keep the bar stationary and treat any extra motion system as suspect.

## What to remove first
- `search-chrome-hidden` classes and related transforms/opacities for the bar
- `visualViewport` keyboard-inset calculations that change the bar's bottom offset
- JS functions that toggle the bar between multiple lanes based on scroll or keyboard state
- result-state-driven bar visibility changes

## What can stay
- focused-input class that hides the dock
- stable results lane / spacer logic for zero or one results
- Enter-to-blur and explicit touch-drag-to-dismiss keyboard behavior

## Verification
- While typing, the result list can change size but the bar should appear pinned to the viewport bottom lane.
- Zero-result and one-result states should not make the bar feel like it jumps.
- Keyboard open/close should feel browser-native, not custom-animated.
