# Derivative Pages Launch and Provenance

Use this reference when launching a small sibling community directory whose public site is still a scaffold.

## Provenance

Identity and domain capability are separate concerns. If a steward is known as `JOSH.sol` or `MidnightRider.sol`, display those names as plain identity text unless the steward explicitly requests official outbound links. Do not silently append `.site`, add `https://`, or turn a credit line into a navigation surface. A compact homepage credit plus a fuller About page is appropriate while the render is unfinished.

## Two-repository launch

Keep the source-of-truth repository and public rendering repository separate. For a new public launch:

1. Confirm the GitHub account and whether the target repositories already exist.
2. Create public repositories only after the user authorizes the push.
3. Stage selectively. Before the first commit, inspect `git status --short` and reject generated artifacts, especially `__pycache__/` and `*.py[cod]`.
4. Add root-level ignore rules before committing, even if a nested project already has an ignore file.
5. If the user supplies an exact commit message, use it verbatim for the initial source and site commits.
6. Push and verify each repository's remote branch and commit SHA.

## Nested GitHub Pages site

If the site files live under a directory such as `edm/`, do not assume the default Pages source will serve them. Add a workflow that uploads the nested directory:

```yaml
- uses: actions/upload-pages-artifact@v3
  with:
    path: edm
- uses: actions/deploy-pages@v4
```

The workflow needs `contents: read`, `pages: write`, and `id-token: write` permissions, plus `actions/configure-pages@v5`. Enable Pages through the repository's Pages API with the Actions build source before expecting `configure-pages` to work. A missing Pages site produces a `Not Found` error from `configure-pages`; the fix is enabling Pages, not changing the HTML.

## Deployment proof

A successful push is not deployment proof. Verify:

- the Pages workflow has `completed` / `success`;
- the run head SHA matches the pushed site commit;
- the Pages API reports the expected project URL;
- homepage, About, and directory routes each return HTTP `200`;
- a cache-busted fetch contains a unique marker from the change;
- identity text is correct in the live HTML and does not contain stale domain suffixes.

Only then hand the live URL to the user for mobile feel-out testing.
