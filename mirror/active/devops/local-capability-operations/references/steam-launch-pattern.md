# Steam launch pattern

## Verified implementation

The first local deployment used the Linux desktop entry rather than a guessed binary path:

```bash
gtk-launch steam
```

This successfully started Steam and its update UI in the user's desktop session. The deterministic wrapper lives at `~/.local/bin/launch-steam` and returns structured status output.

## Process-state distinction

- `steam` is the authoritative primary-client signal for `already_running`.
- `steamwebhelper` is useful startup evidence after a fresh launch, but helper-only state should not prevent a new client launch because helpers may outlive or precede the main client.
- A successful result must be checked against live process state.

## Expected statuses

- `status=already_running`
- `status=launched` with `launcher_pid`
- `status=launch_in_progress`
- `status=verification_failed` with a log path
- `status=unavailable` with a reason

## Evidence boundary

The live already-running path was verified successfully. The fresh-launch and verification-timeout branches should be tested with isolated command shims and a short `LAUNCH_STEAM_VERIFY_SECONDS` value before being described as fully validated. If a test harness hangs or is blocked by a safety guard, preserve that uncertainty and do not claim the branch passed.

## Mirror rule

When backing up this capability, preserve both the Hermes skill directory and any separately managed executable script. A mirror containing only `SKILL.md` is not sufficient to restore the working capability.
