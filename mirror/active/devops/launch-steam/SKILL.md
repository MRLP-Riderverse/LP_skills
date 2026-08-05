---
name: launch-steam
description: "Launch Steam remotely via a verified local script."
category: devops
metadata:
  hermes:
    tags: [steam, desktop, remote-launch, local-first]
---

# Launch Steam reliably

Use this skill when the user asks to launch Steam, wake Steam, or start Steam updates on the local Linux desktop.

## Procedure

1. Run the deterministic launcher:

   ```bash
   ~/.local/bin/launch-steam
   ```

2. Treat the script's structured output as authoritative:
   - `status=already_running`: report that Steam was already running.
   - `status=launched`: report that Steam was launched and process verification succeeded.
   - `status=launch_in_progress`: another launch request is already being handled; do not retry immediately.
   - `status=verification_failed`: inspect the reported log path and process state before retrying.
   - `status=unavailable`: report the missing prerequisite instead of improvising a different launcher.

3. For `verification_failed`, inspect the local launcher log and current Steam processes. Retry only after identifying a transient failure. Never claim Steam launched without process evidence.

## Design contract

- The script is the source of truth for launching Steam.
- It is idempotent and uses a lock to avoid duplicate launches.
- It launches through the user's desktop entry with `gtk-launch steam`, preserving the normal desktop session and Steam's automatic update behavior.
- It treats the main `steam` client as the already-running signal and confirms it remains present for one second; a transient/flapping process does not produce a false-positive success.
- It verifies `steam` or `steamwebhelper` appears before returning success.
- `LAUNCH_STEAM_VERIFY_SECONDS` may override the 20-second verification window for controlled tests.
- Do not type passwords, interact with permission dialogs, or alter Steam account settings.

## Verification commands

```bash
pgrep -a -x steam
pgrep -a -x steamwebhelper
```

The launcher log is normally:

```text
~/.local/state/launch-steam.log
```

Keep responses concise and distinguish `already_running` from a fresh `launched` result. Nya, but only if it fits the user's tone.
