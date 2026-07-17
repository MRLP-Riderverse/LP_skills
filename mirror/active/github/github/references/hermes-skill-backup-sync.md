# Hermes Skill Backup Mirror Sync

Use this when maintaining a sibling repo that mirrors *agent-made* Hermes skills from a live `~/.hermes/skills` tree.

## Workflow

1. Identify the live source root and the backup repo root.
2. Scope the audit from the live skill registry first:
   - use `~/.hermes/skills/.usage.json`
   - treat `created_by: "agent"` as the primary signal for agent-made skills
   - do not infer scope only from "not bundled"; that overcounts imported, hub, or manually added skills
3. Match skills by a normalized leaf name so `directory-card-lookup`, `directory_card_lookup`, and path-variant layouts resolve to the same skill.
4. Compare the full skill directory, not just `SKILL.md`.
5. Use content hashes or `diff -qr` to catch drift in `references/`, `templates/`, `scripts/`, and generated helper files.
6. If one skill needs a shared wrapper script or similar runtime helper, verify that file's checksum too.
7. Separate backup completeness from runtime risk:
   - check cron jobs for skill references
   - a missing mirror with no cron references is a backup gap, not necessarily an immediate operational break
8. Watch for alias drift between old backup naming and live naming. Example class: `note-taking-note-capture-workflow` in a backup repo is not proof that live `note-taking/note-capture-workflow` is covered unless the files actually match.
9. Commit the mirror refresh as a single chore, then push.
10. Re-run a read-only verification after push and expect a clean working tree.

## Pitfalls

- `SKILL.md` parity alone is insufficient; support files can drift independently.
- Do not assume hyphenated and underscored skill names are distinct.
- Do not assume every active non-bundled skill belongs in the backup; use `created_by: "agent"` to define the mirror set unless the user says otherwise.
- A similarly named backup folder can be stale or semantically different; verify with hashes before calling it covered.
- An older prefixed backup path does not necessarily cover the current live skill. Example: `note-taking-note-capture-workflow` and `note-capture-workflow` may both need to exist in the backup as separate restore points.
- When you refresh a missing skill, copy the whole directory tree first and then prove parity with a read-only directory diff.
- Treat runtime cache files and generated artifacts carefully; mirror only what the backup policy intends to preserve.
- If the backup repo is used as a restore point, keep the commit atomic so future recovery is unambiguous.
