# GitHub Pages Static-Site Sync

This note captures the safe two-repo export/publish sequence for a data repo that feeds a separate GitHub Pages repo.

## Pattern

- **Source repo**: holds the canonical data and any export script.
- **Site repo**: holds the generated payload consumed by the Pages site.
- Exporting from the source repo is not enough; the site repo still needs its own commit and push.

## Safe order

1. Commit and push the source repo change.
2. Run the export script from the source repo.
3. Verify the generated payload in the site repo working tree.
4. Commit the generated file in the site repo.
5. Push the site repo.
6. Verify the payload contains the new entry before telling the user it is live.

## Verification checklist

- source repo clean or committed after the content change
- export script completed without errors
- site repo has the generated payload in its working tree
- generated JSON actually includes the new title / item
- site repo commit and push succeeded

## Pitfalls

- Export success is not publication.
- A helper script should be committed if it is part of the repeatable workflow.
- Do not infer the public site state from the source repo alone.
