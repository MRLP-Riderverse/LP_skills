# Telegram `/topic` mode in Hermes

## What it is
`/topic` is a Telegram gateway feature for Hermes, primarily for DM topic-mode workflows. It lets one Telegram DM host multiple isolated Hermes conversations by topic/thread instead of forcing all turns into a single linear chat.

## Practical model
- The root DM acts more like a lobby/system area.
- Individual topics become separate Hermes session lanes.
- This is useful when the user wants low-friction parallel conversations inside Telegram rather than switching platforms.

## Commands observed in source/workflow
- `/topic` — enable or enter topic-mode flow
- `/topic help` — show help
- `/topic off` — disable topic mode
- `/topic <session-id>` — bind an older Hermes session into a Telegram topic

## Operational notes
- Treat `/topic` as a gateway/runtime behavior, not a generic Hermes CLI command.
- When explaining it, frame it as a UX feature for session isolation in Telegram.
- Good default wording: one DM can host multiple isolated Hermes sessions via topics.

## When to mention caveats
Mention that actual UX should be validated in practice if the user is deciding whether to adopt it as a workflow. The concept is strong, but the real test is whether topic switching feels smooth enough in daily use.
