# QuickThoughts Snapshot Retention Policy

This is the operational snapshot cadence for QuickThoughts integrity backups.

## Current pattern

- **One-time baseline snapshot**: take a full copy of the current QuickThoughts file when establishing the scheme or after a major recovery.
- **Daily check**: run a quiet local-only tail of the last 40 lines. This is for lightweight verification and should not be sent to Telegram.
- **Weekly snapshot**: take a full copy every Saturday at 3:00 AM Atlantic time.

## Storage location

Store snapshots under:

`~/Documents/Notes/notecore/snapshots/QuickThoughts/`

Recommended structure:

- `~/Documents/Notes/notecore/snapshots/QuickThoughts/YYYY-MM-DD/QuickThoughts_<timestamp>.txt`

## Why this shape

- The daily tail keeps Telegram noise low.
- The weekly snapshot preserves a full recovery point.
- Putting snapshots near the inbox keeps the recovery chain local and easy to inspect.
- A baseline snapshot gives the new cadence a known starting point.

## Operational rule

If the task is just to see whether QuickThoughts is healthy, prefer the daily tail.
If the task is to preserve a recoverable archive point, use the weekly full snapshot.
Do not default to a full-file dump every day.
