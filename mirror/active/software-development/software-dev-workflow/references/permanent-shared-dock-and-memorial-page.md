# Permanent Shared Dock and Memorial Page Notes

Session-derived notes for static multi-page community sites with a global dock and a sparse memorial/obituary page.

## Permanent dock contract
- Treat the bottom dock as one shared shell component, not as a per-page widget.
- If the dock is meant to be persistent, every page should render the same dock semantics, spacing, and active-state logic.
- Do not verify the dock page-by-page in isolation; search the full site for selector drift, duplicated controls, and page-specific overrides.
- A shared dock should always behave the same regardless of page context unless the product intentionally models a different app state.

## Control duplication pitfall
- If replacing an icon with a new symbol, ensure the old control is removed everywhere, not left behind as a duplicate shortcut.
- If the symbol is decorative, the actual clickable target must still be the real toggle control.
- If the symbol is the target, make it keyboard-accessible and tied to the shared toggle state.

## Memorial/obituary page pitfall
- A stripped memorial page can look detached if it loses the site’s shell/background language.
- Minimal content is fine, but keep enough branded surface treatment—shared gradient, paper tone, typography rhythm, or framing—to read as part of the same unit.
- Respectful pages should feel low-friction and quiet, not “modernized” just to look different.
