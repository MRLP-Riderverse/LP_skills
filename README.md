# LP_skills

Backup of MidnightRider.sol's personal Hermes agent skills — the ones I created, before the curator prunes them again.

## Why This Exists

The Hermes curator has a recurring habit of off-spec pruning (June 5, June 8, 2026):
- LLM review pass uses raw `terminal mv` to `.archive/` bypassing `skill_manage`
- Doesn't update cron job paths that reference pruned skills
- Skills with `created_by: null` are invisible to curator status display
- Pins can be bypassed via raw terminal commands

This repo is the off-site backup. If a skill gets pruned, it can be restored from here.

## What's Backed Up

- `agent-created/` — The 23 skills created by the agent (me, Hermes, for MidnightRider.sol)
- `pinned/` — Symlinks or copies of the 21 pinned skills (most overlap with agent-created)
- `archive-snapshot/` — Full snapshot of the .archive/ folder as of the backup date
- `usage.json` — Snapshot of .usage.json for pin/created_by audit

## How to Restore

If a skill gets pruned:
1. Check this repo for the last known good version
2. Copy the skill directory back to `~/.hermes/skills/`
3. Ensure `created_by: "agent"` and `pinned: true` in `.usage.json`
4. Verify with `hermes curator pin <name>`

## Update Schedule

Run backup manually after significant skill changes, or set up a cron to sync weekly.

## Author

MidnightRider.sol — created June 9 2026
