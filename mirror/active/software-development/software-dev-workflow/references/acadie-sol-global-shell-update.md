# Acadie.sol global shell update pattern

Session-derived notes for shared shell changes on the Acadie.sol static site.

## What changed
- The drawer/menu labels are owned by `assets/site-shell.js`.
- Several pages also keep their own localized copy maps, so label changes can drift unless both layers are updated.
- A new drawer item can be added even if the destination page is just a blank scaffold for now.
- The global header color can be switched by introducing a dedicated accent token instead of reusing a generic gold token.

## Useful workflow
1. Update the shared shell renderer first.
2. Patch page-local copy objects that still duplicate the same labels.
3. Create the new page as a minimal shell-only document if content is not ready yet.
4. Verify with `git diff --check` and a quick local static-server check when useful.
5. If local LAN/mobile preview is more friction than value, commit/push and test on the hosted site instead.

## Pitfalls
- Changing the shell text without updating page-local copies leaves inconsistent UX in different pages.
- A blank destination page still needs a valid title and shell include so the nav target resolves cleanly.
- Local test servers are only for verification; they do not affect the committed site state.
