# LP_skills — Hermes Skills Recovery Mirror

Backup and recovery repository for MidnightRider.sol's Hermes Agent skills.

This repo now has two layers:

- `agent-created/` — curated, human-oriented copies of important workflows.
- `mirror/` — broad deterministic mirror of the active Hermes skills plus the Hermes archive.

The broad mirror is the safety net. The curated layer is the short list worth restoring first.

## Current mirror

The generated inventory is recorded in:

- `MIRROR_MANIFEST.json` — file-level SHA-256 hashes and source metadata.
- `MIRROR_MANIFEST.md` — human-readable summary.

Run the sync from the repository root:

```bash
python3 scripts/sync_from_hermes.py
python3 scripts/verify_mirror.py
```

The sync source is the active Hermes profile at `~/.hermes/skills/`.

## Recovery

To restore an active skill manually, copy the matching directory from:

```text
mirror/active/<category>/<skill-name>/
```

to:

```text
~/.hermes/skills/<category>/<skill-name>/
```

Archived skills are under `mirror/archive/`. After restoring a cron-critical skill, verify its path and pin it with Hermes:

```bash
hermes curator pin <skill-name>
hermes skills list
```

Do not restore the entire archive blindly. Prefer the active mirror first, then recover individual archived skills as needed.

## Curated recovery tiers

### Tier 1 — Cron-critical

- `weatherAPI-home`
- `quickthoughts-daily-sync`
- `music-artist-monitor`
- `acadian-community-tech`
- `frontier-stack-tech-review`
- `mardi-en-acadie-newsletter`

### Tier 2 — Important workflows

- `gbrain-operations`
- `gpt-transfer-report`
- `note-capture-workflow`
- `opencode-delegation-pattern`
- `acadie-sol-website`
- `acadie-sol-gallery`
- `directory-card-lookup`
- `directory-draft-intake`

### Tier 3 — Supporting workflows

- `community-event-directory-linking`
- `cron-job-reliability`
- `git-secrets-hygiene`
- `hermes-provider-config`
- `mcp`
- `mcporter`
- `native-mcp`
- `frontier-stack-evaluation`

## Design choices

- The mirror is generated from the live Hermes profile, not from Git history.
- Skill matching uses frontmatter `name`, so folder renames do not silently break curated refreshes.
- Runtime metadata, `.git` directories, `__pycache__`, weather caches, and Python bytecode are excluded.
- Secrets are not copied from `.env` files or from outside the skills tree.
- `acadie-sol-gallery` is stored as a normal restorable skill directory rather than a loose note.

## Update policy

Refresh after meaningful skill changes, curator activity, or Hermes upgrades. Review the generated diff before committing. Do not commit credentials, runtime state, or generated caches.

Author: MidnightRider.sol
