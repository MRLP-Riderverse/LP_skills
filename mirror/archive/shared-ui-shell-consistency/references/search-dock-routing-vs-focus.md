# Search Dock Routing vs Programmatic Focus

Use this for multipage sites where a global dock Search control tries to open/focus a page-local search input.

## Durable lesson
A global shell control should not depend on page-specific delayed focus after navigation. On mobile, a route/hash jump followed by async render and `.focus()` often fails to open the soft keyboard. Even if focus technically lands, the interaction feels broken.

## Better shell contract
- Global dock Search should link to a stable search route (`search.html`, `/search`, etc.).
- The search route owns search UI and search state.
- Browse pages should not carry hidden search panels only to satisfy the dock.
- Remove custom shell events once the control becomes a normal route. Examples of drift hooks to search for:
  - `data-shell-search`
  - `directory.html#search`
  - `acadie:searchdock`
  - page-local `focusSearchTool` / `focusSearchInput`

## When to use an overlay instead
A same-page overlay can be valid when the product goal is true app-like one-tap keyboard behavior. In that case the shell must open/focus the input synchronously from the trusted tap event, not after route navigation. If the team/user chooses a page route instead, accept that users may tap the big input once on arrival and optimize visual clarity rather than forcing the keyboard.

## Verification
- Every page has the same Search href.
- The old hash target is absent site-wide.
- The route loads without console/page errors.
- Search page typing and filters update results.
- Browse pages render their primary content without hidden search-shell dependencies.
