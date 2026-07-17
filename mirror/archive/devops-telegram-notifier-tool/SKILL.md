---
name: telegram-notifier-tool
description: Create and use a lightweight Telegram notifier command for Hermes workflows when you want a reusable local tool for plain-text Telegram pings.
version: 1.2.0
author: Hermes Agent
tags: [telegram, notifier, messaging, cli, hermes]
---
# Telegram Notifier Tool

Use this skill when you need a simple reusable command for sending a Telegram ping from the shell or from Hermes-adjacent workflows.

## Recommended approach

- Keep the actual implementation in the Hermes repo as the source of truth.
- Keep a thin user-bin entrypoint for convenience.
- Keep the reusable workflow, usage notes, and conventions in a Hermes skill.
- If the notifier becomes a larger workflow, expand the repo-managed script first and let the skill point to it.

## Current layout

- Repo-managed script: `~/.hermes/hermes-agent/scripts/telegram_notify.py`
- Convenience CLI wrapper: `~/.local/bin/telegram-notify`
- Linked docs:
  - `references/README.md`
  - `references/usage.md`

## Usage

The notifier supports:
- plain-text messages
- photo/document uploads when the workflow needs media delivery
- `--stdin`
- `--target telegram:<chat_id>`
- `--dry-run`
- safe chunking for long messages
- optional fallback to `~/.hermes/.env`

## Reliable fallback

If a shell-based Telegram send is blocked or brittle, use a small Python `requests` sender that:
- loads credentials from `~/.hermes/.env`
- reads `TELEGRAM_BOT_TOKEN` and `TELEGRAM_HOME_CHANNEL`
- sends text with `sendMessage`
- sends images with `sendPhoto`
- includes the note prefix `Notes, by Telegram : ` for routed notes

This is a good fallback for one-off note delivery or when you need to upload an already-rendered image.
## Conventions

- Default to `TELEGRAM_HOME_CHANNEL` when sending to the home chat.
- Use explicit chat IDs for targeted delivery.
- Prefer `--dry-run` when testing new formatting.
- If a cron job already auto-delivers to Telegram, do not send a duplicate manual ping from inside the same cron run.

## Verification

- Confirm the target resolves correctly.
- Run a dry-run first.
- Then send a real short message.

## Notes

If you need a more integrated Hermes-native solution later, this skill can be updated to point at a gateway tool implementation or a fully tested repo module.
