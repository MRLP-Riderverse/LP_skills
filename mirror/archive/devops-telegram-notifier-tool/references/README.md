# Telegram Notifier Tool

This skill documents the local Telegram notifier workflow used in Hermes.

## Layout

- Repo-managed implementation: `~/.hermes/hermes-agent/scripts/telegram_notify.py`
- Thin CLI wrapper: `~/.local/bin/telegram-notify`
- Skill home: `~/.hermes/skills/devops/telegram-notifier-tool/`

## Why this exists

- Keep the implementation versionable inside the Hermes repo.
- Keep the command easy to call from the shell.
- Keep usage conventions close to the skill so future updates stay consistent.

## Quick start

- Dry run: `telegram-notify --dry-run "hello"`
- Send message: `telegram-notify "hello"`
- Pipe stdin: `printf 'hello' | telegram-notify --stdin`
- Specific target: `telegram-notify --target telegram:-1001234567890 "hello"`

## Notes

This workflow is intentionally plain-text only. If richer formatting or gateway integration becomes necessary, update the repo-managed implementation first and keep this reference in sync.
