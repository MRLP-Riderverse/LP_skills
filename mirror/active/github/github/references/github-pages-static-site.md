# GitHub Pages static site publishing notes

## Observed pattern
- `GitHub Pages` at repository root will serve `index.html` if present.
- If no `index.html` exists, the repo root may surface `README.md` content instead.
- A tiny/placeholder `index.html` in the repo will be what Pages serves, even if the local working tree has richer uncommitted content.

## Recommended split for paired repos
- **Data repo**: canonical source of truth, markdown/JSON/inbox entries, no public Pages dependency.
- **Site repo**: static mirror / rendered output, committed artifacts only.
- Use a manual export step from data repo into site repo, then commit + push the generated site assets.

## Verification sequence
1. Export generated payload into the site repo.
2. Inspect `git status` in the site repo.
3. Commit the site repo changes.
4. If `git push` is rejected with `fetch first`, run `git fetch origin` and `git rebase origin/main` before retrying.
5. Confirm the deployed branch/root now contains the intended `index.html` and generated assets.
