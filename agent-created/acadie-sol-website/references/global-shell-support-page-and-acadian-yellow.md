# Global shell update notes

Session-derived contract for the shared Acadie.sol shell.

## Menu copy
- The dock/drawer menu should use `View Everyone` instead of `Full directory`.
- Add a third drawer item: `Support Acadie.sol`.
- Keep the drawer copy aligned with the actual links so `site-shell.js` does not drift from page-local copy blocks.

## Support page
- Create `support.html` as a blank shell page for now.
- Do not add body content, cards, or explanatory containers until the user supplies the support-page layout/content.
- The page should still load the shared shell so the dock/menu remain available.

## Header colour
- The global top banner `Vive l’Acadie` should use the Acadian Yellow token, not the dim gold tint.
- Prefer a dedicated token alias (`--acadian-yellow`) in `assets/site-colors.css` if the site needs to keep the original `--gold` token for other surfaces.

## Verification notes
- After updating shared shell copy, search the project for stale `Full directory` strings in page-local copies.
- Verify the shared shell renderer updates both the visible drawer labels and the sync routine that hydrates them.