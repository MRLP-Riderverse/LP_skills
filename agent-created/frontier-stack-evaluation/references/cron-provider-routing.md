# Cron provider routing note

## Verified on this Hermes setup
- `hermes chat -q "reply exactly OK" --provider openai-api --model gpt-5.4-mini` → `OK`
- `hermes chat -q "reply exactly OK" --provider openai-codex --model gpt-5.4-mini` → `OK`
- Plain `openai` is **not** a valid provider id in cron/job resolution here; it produced `RuntimeError: Unknown provider 'openai'`.

## Practical rule
When a frontier-stack cron brief fails on provider mismatch, check the persisted job config first:
- `hermes cron list`
- `~/.hermes/cron/jobs.json`

Common failure mode:
- model is pinned correctly (`gpt-5.4-mini`)
- provider is stale (`openai` instead of `openai-codex` or `openai-api`)

## Recommended default
For this user's frontier-stack brief, prefer `openai-codex` unless there is a specific reason to route through the direct API.

## Verification pattern
Dry-test both providers with the same trivial prompt before changing the cron:
```bash
hermes chat -q "reply exactly OK" --provider openai-api --model gpt-5.4-mini
hermes chat -q "reply exactly OK" --provider openai-codex --model gpt-5.4-mini
```
