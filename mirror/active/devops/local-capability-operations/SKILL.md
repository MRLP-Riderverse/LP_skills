---
name: local-capability-operations
description: "Build reliable local desktop capabilities with scripts."
category: devops
metadata:
  hermes:
    tags: [local-first, desktop, deterministic, verification, mirror-sync]
---

# Local Capability Operations

Use this class-level skill when exposing a local-machine action through Hermes, especially a desktop application launch, update trigger, or other remote control capability.

## Architecture: deterministic core plus agent wrapper

1. Put the actual operation in a small, executable local script.
2. Make the script idempotent: repeated requests should be safe and should not create duplicate processes or conflicting state.
3. Give the script structured, machine-readable status values such as `already_running`, `launched`, `launch_in_progress`, `verification_failed`, and `unavailable`.
4. Add a thin Hermes skill that invokes the script, interprets those statuses, and performs bounded diagnosis only when the script reports a problem.
5. Keep the agent wrapper from duplicating the operational logic. The script is the source of truth; the skill is the intent translation and evidence-reporting layer.

## Verification contract

- Verify the result using external state, not the launch command's exit code alone.
- Distinguish the primary application's process from helper, renderer, updater, or stale child processes.
- For an already-running check, prefer the primary client process as the authoritative signal. A helper-only process should not necessarily block a fresh launch.
- After launching, poll for a bounded interval and report failure if the expected primary or documented startup process never appears.
- Never claim a side effect completed without process, file, API, or other live evidence.
- Preserve the distinction between `already_running` and a fresh `launched` result in the user-facing response.

## Testing error paths safely

- Keep verification timing configurable through a narrowly scoped environment variable so tests can use a short timeout without changing normal behavior.
- Test at least: already-running, fresh-launch success, missing launcher prerequisite, and verification timeout.
- Use isolated command shims or fixtures for process/launcher probes rather than stopping the user's live application merely to force a branch.
- Do not report a simulated branch as validated if the harness itself timed out or failed to produce evidence.
- If a test harness is blocked by an execution guard, stop that test path; do not retry the same destructive or potentially hanging operation through a different wrapper.

## Mirror and Git workflow

When the user requests a copy in a recovery or mirror repository:

1. Inspect the repository and remote before copying.
2. Prefer the repository's existing deterministic sync script when one exists.
3. Copy the complete skill directory, including `references/`, `templates/`, and `scripts/`; do not mirror only `SKILL.md`.
4. Run the repository's verifier and inspect the resulting diff.
5. Keep runtime state, credentials, caches, bytecode, and VCS directories excluded.
6. Do not commit or push until the live capability tests and mirror verification have produced usable evidence.
7. Commit narrowly, inspect the commit, push only to the intended remote/branch, then verify clean working tree and zero local/remote divergence.
8. If any required verification remains unresolved, report that status instead of claiming a completed push.

## Failure handling

- A missing binary or desktop integration is setup state, not a permanent capability limitation; diagnose it from live output.
- A transient launch failure should be logged and retried only after checking current process state.
- Do not weaken global approval or security controls to make a local capability more convenient.
- Do not interact with password prompts, permission dialogs, payment UI, or account settings unless the user explicitly requests and authorizes that exact action.

## Supporting reference

For the Steam implementation pattern and verified observations from the first deployment, see `references/steam-launch-pattern.md`.
