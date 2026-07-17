# Cron rate-limit resilience for frontier briefs

## Symptom
A frontier-stack cron run can make it through source collection, then fail during synthesis with a provider error like:

```text
RuntimeError: HTTP 429: Error code: 429 - {'status': 429, 'title': 'Too Many Requests'}
```

In the observed run, the job had already performed a broad delta sweep across Solana, LangChain, Simon Willison, x402, and related sources before the final model call hit rate limiting.

## Durable fix pattern
- Treat the failure as a **synthesis-layer throttle**, not a source-fetch bug.
- Retry once with backoff if the provider allows it.
- Reduce prompt weight before retrying:
  - narrower delta window
  - fewer source calls
  - cached dedup baseline instead of re-reading the full prior brief
- If the job is recurring, split it into two stages:
  1. collection job writes source snapshots / candidate deltas
  2. synthesis job reads the cached bundle and writes the brief
- If a provider keeps 429ing on heavy synthesis, move the cron to a less rate-limited model/provider.

## What not to assume
- Do not assume a 429 means the RSS/feed/probe step is broken.
- Do not treat a single 429 as a permanent skill or source failure.
- Do not keep expanding the prompt after a rate-limit failure; trim first, then retry.

## Verification
When debugging a failed run, check the cron output file for the last successful tool-call section and the final error line. If source collection completed and the failure occurs at the final response stage, the job needs retry/backoff or prompt-shaping, not source hunting.
