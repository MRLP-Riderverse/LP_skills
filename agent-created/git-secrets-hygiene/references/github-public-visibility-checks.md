# GitHub Public Visibility Checks

## Anonymous verification pattern

Use harmless content only.

1. Confirm the repo exists and identify its canonical URL.
2. Confirm repository visibility:
   - `gh repo view OWNER/REPO --json isPrivate,url,nameWithOwner`
3. Verify direct file access through the raw endpoint:
   - `https://raw.githubusercontent.com/OWNER/REPO/BRANCH/PATH`
4. Optionally verify the blob page responds publicly:
   - `https://github.com/OWNER/REPO/blob/BRANCH/PATH`

If the repo is public and the raw file fetch succeeds, the file is public to unauthenticated users.

## What this demonstrates

- GitHub public repositories expose committed files to anonymous users.
- Raw URLs are often the clearest proof because they bypass local repo state.
- A successful public fetch is stronger evidence than merely saying "the repo is public."

## Remediation when the file was only a harmless test

- Make a follow-up commit deleting the file if the user no longer wants it visible.
- Explain that the file remains in history unless history is rewritten.

## Remediation when the file contained a real secret

1. Rotate/revoke immediately.
2. Remove from the current tree.
3. Assess whether history rewrite is necessary.
4. Check for spread into CI logs, releases, screenshots, docs, forks, and local clones.

## Explanation shortcut

Use this plain-language summary:

> Because the repository is public and the raw file URL is reachable without auth, this content is publicly visible. If it were a real secret, it should be treated as compromised.
