# Static Site Audit Checklist

Session-derived checklist for public static sites like Acadie.sol.

## 1) Input and rendering safety
- Validate any data-driven `href`, `src`, or URL-like fields before rendering.
- Treat `location.hash`, query params, and generated JSON as untrusted input.
- Guard `decodeURIComponent()` against malformed fragments.
- Prefer `getElementById()` over selector parsing when targeting IDs from hashes.
- Watch for content rendered via `innerHTML`; verify every user-controlled branch is escaped.

## 2) Shell and renderer drift
- Look for duplicated theme/lang logic across pages when a shared shell already owns it.
- Flag class mismatches where CSS targets one class and the renderer emits another.
- Flag stacked page-level overrides that redefine the same selectors multiple times.
- If a shared dock/menu exists, verify it as one site-wide contract rather than per page.

## 3) Dark-mode coherence
- Check whether text accents still use a dark anchor token on dark/glass surfaces.
- Check hard-coded borders/fills that disappear against the current palette.
- Check browser chrome color (`theme-color`) against the active dark-mode surface.
- Prefer tokenized fills/borders for badges, pills, chips, and related inline UI.

## 4) Practical remediation priorities
1. Lock down untrusted URLs.
2. Harden hash parsing.
3. Fix class/selector drift.
4. Normalize repeated shell overrides.
5. Re-run visual verification on the live site.
