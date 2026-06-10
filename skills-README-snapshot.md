# Hermes Skills Directory

This directory is the runtime source of truth for active skills.

## Canonical paths

- Runtime skills: `~/.hermes/skills/`
- Hermes repo: `~/.hermes/hermes-agent/`
- Bundled skill sources in the repo: `~/.hermes/hermes-agent/skills/`

## How to think about it

- Edit skills here when you want the live Hermes installation to change.
- Edit the repo under `~/.hermes/hermes-agent/skills/` when you are changing bundled upstream skill sources.
- The repo's `skills/` directory is copied into this runtime directory during install/update workflows.

## Avoiding routing confusion

- Treat `~/.hermes/skills/` as the default location for skill discovery, loading, and agent-created skills.
- Treat the repo as the development source for bundled skills and code.
- Do not assume both trees should be edited independently unless you are intentionally syncing them.

## Notes

If a skill appears in both places, the runtime copy wins for live execution.
