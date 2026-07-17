# Static site global shell extraction

Use this when repeated static HTML pages recreate the same dock/menu/drawer instead of consuming one global shell.

## Extraction contract

- Move chrome-only CSS into `assets/site-shell.css` or equivalent.
- Move repeated chrome markup and global UI state into one renderer script such as `assets/site-shell.js`.
- Pages should include the shared CSS/JS and should not hardcode shell markup.
- Pages may listen for global shell events like `acadie:languagechange` to rerender page content, but they should not attach their own click handlers to global shell controls.
- The global shell owns: dock links, drawer labels, menu open/close, theme toggle, language toggle.
- Page renderers own only page data and content copy.

## Verification contract

For every top-level page:

- Exactly one shared shell CSS link.
- Exactly one shared shell JS script.
- Exactly one rendered dock, drawer, and menu toggle in the browser.
- Zero hardcoded shell markup such as `<nav class="site-dock">` or `<input class="menu-toggle">` in page HTML.
- Zero inline shell selectors left in page-local styles (`.site-dock`, `.drawer`, `.menu-toggle`, `.theme-button`, `.lang-button`, etc.).
- Menu opens on every page.
- Theme toggle and language toggle work on every page.
- Drawer/dock links are identical across pages.

## Practical browser check

When using Puppeteer on static pages, avoid over-relying on `networkidle0` for data-rendered pages that can hold requests open or time out. Prefer:

1. `page.goto(url, { waitUntil: 'domcontentloaded' })`
2. `page.waitForSelector('.site-dock')`
3. DOM counts and click checks
4. Console/pageerror collection

## Pitfalls

- Removing visible markup but leaving stale page-prefixed IDs (`events-menu-*`, `entry-dock-*`) or copy writes means the page still thinks it owns the shell.
- Reusing page-local theme/language listeners after extraction can double-toggle or fight the global shell.
- A page-local CSS selector can still override the shared shell even if markup is global. Search selectors, not just HTML tags.
- Same-page dock search links should not rely on hash jumps when the destination page owns the search UI. Dispatch a shell event and let the page focus the real input with `focus({ preventScroll: true })`; see `references/directory-search-dock-focus.md`.
