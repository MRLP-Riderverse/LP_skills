# Derivative node mood and menu pass

Use this reference when a sibling/community directory inherits the Acadie.sol rendering bones but needs its own identity and a small mobile-first visual pass.

## Proven pattern

1. Keep the niche label explicit and stable (for Manila, `MANILA - EDM`).
2. Strip homepage explanatory copy before adding new features. A useful early homepage can be only:
   - identity heading;
   - dynamic entry count from the exported database payload;
   - one `Discover!` route to the directory;
   - a literal decorative divider such as `✧❅✦❅✧`;
   - creation/steward provenance.
3. Use a local display font selectively. Wire the copied font with `@font-face`, use it for short identity headings/credits, and keep constrained utility chrome in system monospace or sans-serif because pixel fonts can be unusually wide on mobile.
4. For a strong palette change, centralize tokens in the shared color asset. For a green/gold/black-outline mood, define the green field, gold ink, dark control surfaces, and outline/shadow once; do not scatter page-local hex values.
5. Add the shared shell script to every public route that must expose the menu. Static pages that omit the script will silently lack global navigation.
6. Make About a drawer route rather than a standalone homepage CTA when the homepage is intentionally minimal.

## Right-edge drawer variant

The shared shell can use a right-edge drawer on mobile when the sibling node’s visual language calls for it:

- top-right fixed three-bar launcher;
- full-height drawer with `transform: translateX(100%)` closed and `translateX(0)` open;
- `visibility: hidden`, `pointer-events: none`, and `opacity: 0` while closed so the hidden drawer cannot steal taps;
- dim/blur backdrop, explicit close button, Escape/backdrop close, focus trap, and inert background while open;
- width around `min(340px, 88vw)` on a 390px phone gives readable route rows without covering the whole canvas;
- desktop may use a smaller anchored right panel while keeping the same shared state and keyboard behavior.

Do not copy this geometry into Acadie.sol automatically. Choose the drawer placement from the current node’s mobile feel and user direction.

## Verification contract

Use a real local server and a browser probe, not only static inspection:

- fetch homepage, About, Directory, Entry, shared CSS/JS, and font assets and require `200`;
- verify the dynamic count resolves from `directory-data.json`;
- verify the heading uses the intended display font and computed background is the new palette;
- open the menu at a phone viewport, assert the drawer is visible and includes About, then close it with the explicit close control;
- repeat on desktop and verify the drawer geometry is not still using mobile full-height positioning;
- capture browser console/page errors and fix missing favicon/manifest/media references before publishing;
- after Pages deployment, fetch key routes with a cache-busting query and assert a unique visible marker.

A missing favicon or stale manifest reference is small but should be cleaned up during a console-clean visual pass; it obscures real regressions in browser QA.
