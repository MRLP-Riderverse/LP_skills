# Recovery-Mirror Maintenance

Use this checklist when backing up an agent's skills or operational workflows.

## Before copying

- Identify the live source tree and repository destination.
- Check repository status, remote, branch, and current manifest.
- Decide whether the backup is curated, broad-active, archived, or all three.

## Copy rules

- Match skills by frontmatter `name`, not only directory names.
- Preserve each skill's `SKILL.md`, `references/`, `scripts/`, and `templates/`.
- Back up wrappers or cron dependencies that live outside the skill directory.
- Exclude credentials, runtime metadata, caches, bytecode, `__pycache__`, `.git`, and temporary output.
- Repair loose notes or renamed folders into normal restorable skill layouts.

## Manifest and verification

Record:

- source path
- generation time
- active and archived counts
- file paths, sizes, and SHA-256 hashes
- excluded artifact classes
- curated items refreshed

Verify:

- every manifest file exists
- no unlisted files exist
- hashes and sizes match
- excluded artifacts are absent
- helper scripts compile or pass syntax checks
- repository diff has no whitespace errors

## Reporting

Report separately:

- what was copied and verified
- what was stale or repaired
- what is missing from the live source
- what is intentionally excluded
- repository size and whether commit/push approval is still needed

Never claim a full backup based only on an old manifest or a matching filename.
