# Backup Manifest — Hermes Mirror

Generated from the active Hermes profile at `~/.hermes/skills/`.

Canonical machine-readable inventory:

- `MIRROR_MANIFEST.json`

Human-readable inventory:

- `MIRROR_MANIFEST.md`

## Current coverage

- Active skills: 70 unique frontmatter names
- Active mirrored files: 469
- Archived mirrored files: 445
- Curated recovery copies refreshed: 21
- Mirror size: approximately 28 MB

## Recovery layers

### Broad mirror

- Active skills: `mirror/active/`
- Archived skills: `mirror/archive/`
- Verification: `python3 scripts/verify_mirror.py`

### Curated recovery layer

The curated copies under `agent-created/` prioritize cron-critical and user-specific workflows:

- Weather delivery and QuickThoughts sync
- Music and Acadian briefings/newsletter
- GBrain and note capture
- Website and directory workflows
- Hermes/provider/MCP troubleshooting
- Git hygiene and Opencode delegation

## Naming note

Some backup folder names are historical paths while Hermes loads the frontmatter name. Examples:

- `leisure-music-artist-monitor` → `music-artist-monitor`
- `mcp-mcporter` → `mcporter`
- `mcp-native-mcp` → `native-mcp`
- `research-frontier-stack-tech-review` → `frontier-stack-tech-review`
- `software-development-opencode-delegation-pattern` → `opencode-delegation-pattern`

The sync script matches these by frontmatter name to avoid silent drift.

## External recovery artifact

The Bathurst cron also uses:

```text
~/.hermes/scripts/bathurst_weather_telegram.sh
```

A recovery copy is retained at:

```text
agent-created/weatherAPI-home/bathurst_weather_telegram.sh
```

## Exclusions

Runtime metadata, credentials outside the skills tree, `.git` directories, caches, `__pycache__`, and Python bytecode are excluded.
