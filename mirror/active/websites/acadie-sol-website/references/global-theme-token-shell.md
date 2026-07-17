# Global theme token shell for Acadie.sol

Use this when light/dark colors or design tokens have drifted across the static HTML pages.

## Pattern

- Create one shared palette file, e.g. `assets/site-colors.css`.
- Put all site-wide light tokens in one `:root` block.
- Put all site-wide dark tokens in one `[data-theme="dark"]` block.
- Include compatibility aliases used by older pages (`--bg`, `--page-bg`, `--panel`, `--card`, `--paper`, `--text`, `--ink`, etc.) so pages can migrate mechanically without breaking.
- Attach `assets/site-colors.css` before each page-local `<style>` block so page layout rules can reference the shared tokens.
- Keep page-local CSS for layout/component geometry only; do not leave page-local palette definitions behind.

## Mechanical cleanup

For every top-level page (`*.html`):

1. Add:
   ```html
   <link rel="stylesheet" href="assets/site-colors.css" />
   ```
   before the page-local `<style>` block.
2. Remove page-local `:root { ... }` token blocks.
3. Remove page-local `[data-theme="dark"] { ... }` token blocks.
4. Keep intentional selector rules such as `[data-theme="dark"] body { ... }`; those are theme-specific component styles, not token declarations.

## Verification contract

Run deterministic checks before committing:

- Every HTML page has exactly one `assets/site-colors.css` link.
- Every HTML page has zero page-local top-level `:root` token blocks.
- Every HTML page has zero page-local top-level `[data-theme="dark"]` token blocks.
- All `var(--token)` references across HTML and shared shell CSS resolve from shared global assets.
- Browser-computed checks confirm representative pages switch `--ink`, `--paper`, and body color between light/dark.
- Run the existing JS syntax checks and `git diff --check` because palette edits often move large style blocks.

## Pitfalls

- Do not call the palette unified while keeping a second late `:root` or `[data-theme="dark"]` block in a page. Later token blocks silently override the shared file and recreate drift.
- Do not attach the color file after page-local styles; page rules should consume tokens from the shared file, not define fallback palettes first.
- Do not remove theme-specific selector rules just because they include `[data-theme="dark"]`; remove token declaration blocks, not intentional dark-mode component behavior.
- Browser navigation with `networkidle0` can time out on data-rendered static pages; for token verification, use `domcontentloaded` plus selectors and computed styles instead of treating network-idle timeout as a palette failure.
