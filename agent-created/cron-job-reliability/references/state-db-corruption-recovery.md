# state.db corruption recovery reference

## Incident signature

Observed failure chain:

- Telegram receives a turn but Hermes returns `No reply` or says session storage could not be written.
- Gateway logs show transcript lag (`disk=0, memory=N`) and possible FTS write corruption.
- `hermes doctor` reports malformed `~/.hermes/state.db` schema, commonly an invalid index rootpage.
- A provider/API error may appear on the same turn because delegation or tool persistence fails while the model loop is running.
- Gateway shutdown can drain for 60 seconds, interrupt active work, and leave the systemd service failed.

## Tested recovery sequence

Run while the gateway is stopped or isolated:

```bash
hermes doctor
hermes sessions repair
```

If repair reports `database disk image is malformed`, keep the generated backup and inspect it without modifying the source:

```bash
hermes sessions recover \
  --source ~/.hermes/state.db.malformed-backup-<timestamp> \
  --inspect-only
```

Recover into a new database, never directly over the active one:

```bash
hermes sessions recover \
  --source ~/.hermes/state.db.malformed-backup-<timestamp> \
  --output ~/.hermes/recovered-state.db
```

If complete recovery fails, a best-effort salvage can be used only with explicit loss reporting:

```bash
hermes sessions recover \
  --source ~/.hermes/state.db.malformed-backup-<timestamp> \
  --output ~/.hermes/recovered-state-partial.db \
  --allow-partial
```

Review `<output>.recovery.json`. Accept the output only when it opens cleanly, reports `integrity_check: ok`, has an empty foreign-key check, and FTS checks pass. Record skipped rows/ranges and any reconstructed placeholder sessions.

Install safely by moving the existing database and sidecars aside, then moving the verified recovery output to `~/.hermes/state.db`. Immediately verify:

```bash
sqlite3 ~/.hermes/state.db 'PRAGMA integrity_check; PRAGMA foreign_key_check;'
hermes sessions list
```

Confirm the current Telegram session appears before restarting the gateway.

## Service-level verification

A manual `hermes gateway run` can prove Telegram connectivity but is not durable. Return control to systemd and verify:

```bash
systemctl --user is-active hermes-gateway.service
hermes gateway status
hermes cron status
```

Fresh gateway logs must contain all of:

- `Connected to Telegram (polling mode)`
- `Gateway running with 1 platform(s)`
- `Gateway housekeeping started`

Also verify no new `malformed database schema` lines appear after startup. A stale failed systemd status alongside a healthy manual process is not a completed fix.

## Evidence discipline

Preserve the malformed source and recovery report. Report database loss honestly; do not imply that a partial salvage restored every historical session. Distinguish:

- Telegram transport health
- session database integrity and current-session continuity
- gateway service persistence
- cron scheduler heartbeat
