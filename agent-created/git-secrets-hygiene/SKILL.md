---
name: git-secrets-hygiene
description: Safely demonstrate, verify, and remediate secret exposure risk in Git/GitHub repositories without ever using a real secret.
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Git Secrets Hygiene

Use this skill when the user wants to understand whether something in a repo is public, how GitHub visibility works, whether a file is exposed to anonymous users, or how to test "secret" behavior safely.

## Core rule

If a value is committed to a **public** Git repository, treat it as **published**, not secret.

That remains true even if:
- the file is deleted later
- the branch is cleaned up later
- the user only intended it as a temporary test

Git history and downstream mirrors may preserve the value.

## Preferred teaching pattern

Never test with a real credential.

Instead, use a harmless marker file such as:
- `hello.txt`
- `public-test.txt`
- `visibility-check.txt`

with obvious dummy content like:
- `hello world!`
- `not a real secret`
- `public visibility test`

This lets the user learn the visibility model without creating an actual incident.

## Workflow

1. **Confirm repo identity and branch**
   - Check `git status --short --branch`
   - Check `git remote -v`
   - Confirm whether push auth is available

2. **Create a harmless marker file**
   - Write the test file directly in the target repo
   - Keep content obviously non-sensitive

3. **Commit and push**
   - Use the exact commit message requested by the user if provided
   - Push to the intended branch

4. **Verify public visibility as an anonymous consumer would**
   - Check repo visibility (`gh repo view ... --json isPrivate,url,nameWithOwner` or equivalent)
   - Fetch the raw file URL without relying on local git state
   - Optionally check the blob URL returns a public success response

5. **Explain the result plainly**
   - If the repo is public and the raw URL works, state directly that the file is public
   - Say explicitly: a committed value in a public repo is not a secret

6. **Offer cleanup/remediation**
   - If the test was only educational, offer to remove the file in a follow-up commit
   - If a real secret was exposed, switch immediately to incident response steps

## Verification targets

For GitHub, verify at least one of:
- Raw URL content is retrievable
- Repo metadata shows `isPrivate: false`
- Blob URL returns a public success response

Best practice: verify both repo visibility and direct file access.

## If a real secret was committed

Do not minimize it. Treat it as compromised.

Immediate steps:
1. Revoke/rotate the secret first
2. Remove it from the working tree
3. Rewrite history if appropriate
4. Force-push only after the user understands impact
5. Check forks, caches, Actions logs, deployment configs, and any copied artifacts

## Safe explanation to the user

Use language like:
- "This proves the file is publicly visible."
- "If this had been a real key, it should be considered compromised."
- "Deletion later does not make it secret again because Git history may retain it."

Avoid vague phrasing like "might be visible" once you have verified public access.

## Pitfalls

- Do **not** use a real API key, token, password, or private certificate for a visibility test.
- Do **not** describe secrecy abstractly when you can verify it with a real anonymous fetch.
- Do **not** stop after commit/push; public visibility must be checked explicitly.
- Do **not** imply that deleting a public commit fully repairs exposure.

## References

- `references/github-public-visibility-checks.md` — concise GitHub-specific verification and remediation patterns.
