# Manila EDM Pages public-root verification

Observed deployment shape for the sibling repositories:

- Source repo: `manila-directory`
- Source group root: `manila-directory/edm/`
- Site repo: `manila`
- Static site subtree in the repository: `manila/edm/`
- GitHub Pages publishes that **subtree as its public root**, not as `/edm/` beneath the Pages URL.

## Correct export command

From `manila-directory/`:

```bash
python3 edm/scripts/export_to_site.py --directory edm --site ../manila/edm --all
```

Commit and push the source repository first. Then run the export, verify the generated site payload, commit and push the site repository.

## Live verification URLs

For Pages URL `https://mrlp-riderverse.github.io/manila-site/`, verify:

```text
https://mrlp-riderverse.github.io/manila-site/assets/directory-data.json?rev=<site-sha>
https://mrlp-riderverse.github.io/manila-site/directory.html
```

Do **not** use `/edm/assets/...` or `/edm/` after the Pages URL; those paths return 404 even when deployment succeeds.

## Deployment check

Use the site repository’s Pages action, filtered by the pushed site SHA. A successful run plus a cache-busted live payload containing the promoted slugs is the publication proof. GitHub’s Pages-build API may be unavailable for this Action-deployed site; the workflow result and live HTTP check are the reliable pair.
