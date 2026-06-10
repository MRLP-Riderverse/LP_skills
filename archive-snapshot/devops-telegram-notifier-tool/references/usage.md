# Usage Notes

## Defaults

- Uses `TELEGRAM_HOME_CHANNEL` when no target is provided.
- Falls back to `~/.hermes/.env` when the environment variable is not already set.

## Supported flags

- `--stdin`
- `--target telegram:<chat_id>`
- `--dry-run`

## Behavior

- Chunks messages safely if they get long.
- Resolves known Telegram channel names from `~/.hermes/channel_directory.json`.
- Avoids duplicate manual sends inside cron jobs that already auto-deliver to Telegram.
