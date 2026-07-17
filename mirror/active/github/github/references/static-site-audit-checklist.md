# Static-site audit checklist for GitHub Pages repos

Use this when a Pages-style repo has HTML/CSS/JS content, shared chrome, or generated data payloads.

## High-value checks

- **URL allowlist for rendered links**
  - Before inserting untrusted `href` or `src` values, normalize with `new URL(value, document.baseURI)` and accept only expected schemes.
  - For link targets in content feeds, reject `javascript:`, `data:`, protocol-relative URLs, and malformed inputs.

- **Hash hardening**
  - Wrap `decodeURIComponent(location.hash.slice(1))` in `try/catch`.
  - Prefer `document.getElementById(targetId)` for hash-driven navigation when the ID is known.
  - Avoid passing untrusted hash strings directly into `querySelector()`.

- **Image source hardening**
  - Treat content-managed thumbnails like links: allowlist schemes/origins before rendering into `<img src>`.
  - Use a dedicated helper such as `safeImageSrc()` so content pages and directory cards stay consistent.

- **Shared shell safety**
  - Avoid `document.write()` in shared chrome/bootstrap code when a DOM insertion alternative exists.
  - Keep one shared chrome source of truth; do not re-implement dock/menu behavior per page.

- **Target-blank hygiene**
  - Add `rel="noopener noreferrer"` to external/new-tab links.

- **Theme/readability checks**
  - Use theme-aware `theme-color` meta tags (`media="(prefers-color-scheme: ...)"`) where appropriate.
  - In dark mode, verify controls remain readable on blue/navy surfaces and that fallback initials/icons are visible on light and dark themes.

## Verification pass before commit

- Run `git diff --check`.
- Search for:
  - `document.write(`
  - raw `querySelector(hash)` or direct `decodeURIComponent(location.hash...)`
  - unguarded content URLs in `href`/`src`
  - `target="_blank"` without `rel="noopener noreferrer"`
  - leftover dark-mode override noise that duplicates base styles

## Notes

This checklist was distilled from a Pages-site audit where the highest-value fixes were:
- safe URL allowlisting for search results
- hash parsing hardening
- visible thumbnail fallbacks in cards
- replacement of `document.write()` in shared shell code
- cleanup of redundant dark-mode overrides and warm-toned drawer chrome
