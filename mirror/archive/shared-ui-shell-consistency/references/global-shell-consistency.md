# Global shell consistency notes

This reference captures a recurring failure mode in multipage static sites: the dock/menu/drawer is visually or behaviorally tweaked per page instead of staying a single shared shell.

## Canonical invariants
- The dock should be identical across all pages.
- The menu overlay should be identical across all pages.
- Same element type for each control across pages unless the interaction model truly differs.
- Same item order, same icon set, same spacing, same drawer geometry.
- No page-specific labels or active-state variants inside the dock unless the site has an explicit global state model.

## Drift patterns to look for
- One page uses a `button` while others use an `a` for the same dock slot.
- One page keeps old label text while others are icon-only.
- One page rewrites dock text via JS even after the dock becomes icon-only.
- One page uses different drawer control placement, opacity, or close-button styling.
- A stale ID or click listener remains after the visible control is removed.

## Practical fix pattern
1. Diff the shell markup against a known-good page.
2. Normalize the markup in the outlier pages.
3. Normalize CSS so the shared shell uses the same rules.
4. Delete stale JS hooks and label injection.
5. Search for leftover shell IDs/classes/text across the site.
6. Update the search target/hash so it works consistently on every page.

## Verification checklist
- Search all pages for old shell IDs/classes/text labels: expected count is zero.
- Search for the canonical shell snippet and confirm it appears on every page.
- Confirm the dock link targets are consistent site-wide.
- Confirm the menu overlay uses the same geometry and controls ordering everywhere.
