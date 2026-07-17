# Hermes Skills Mirror

Generated: `2026-07-17T00:39:02+00:00`
Source: `/home/midnight/.hermes/skills`

This repository contains a disaster-recovery mirror of the active Hermes skills.
The curated `agent-created/` layer is kept for human-selected recovery copies;
the `mirror/` layer is the broad deterministic backup.

## Counts

- Active skill directories: 70
- Active mirrored files: 435
- Archived mirrored files: 445
- Curated skills refreshed: 21

## Recovery

- Active skills: `mirror/active/`
- Archived skills: `mirror/archive/`
- SHA-256 manifest: `MIRROR_MANIFEST.json`
- Re-run: `python3 scripts/sync_from_hermes.py`

## Excluded

Runtime metadata, `.git` directories, `__pycache__`, weather caches, and Python bytecode are excluded.
Secrets are not copied from `.env` or other files outside the skills tree.
