# Retired Model / Deterministic Cron Migration

## Signal

A job with `last_error` containing HTTP 410 / end-of-life is a retired model route, not a retryable transient failure. Example observed: `z-ai/glm-5.1` on NVIDIA was unavailable after its retirement date.

## Triage

1. Read the full cron definition, including `script` and `no_agent`.
2. If `no_agent: true`, the model/provider fields are inert. Do not treat their stale values as the cause of a current script result.
3. If an agent job's prompt only tells it to run one fixed local executable and return stdout, convert it to a script-only cron instead of replacing its model.
4. For a pure fixed-text reminder, create a small executable script that prints the exact delivery body.
5. Verify the backing script directly before changing the cron. Avoid `cronjob run` when it would send an unwanted duplicate notification.
6. For remaining judgment-heavy cron jobs, pin an explicit supported provider/model rather than relying on an implicit default.

## Full configuration sweep

After a model retirement, search the main config for the retired model as well as cron definitions. Check fallback routing and auxiliary components (compression, skills hub, MCP, session search, vision). A stale fallback can turn otherwise unrelated errors into repeat failures.

## Routing pattern

- Deterministic mechanics: `no_agent: true` + script.
- Routine model-backed reports: explicit low-cost base model.
- Complex implementation/research and vision: stronger model only where its capability is needed.
