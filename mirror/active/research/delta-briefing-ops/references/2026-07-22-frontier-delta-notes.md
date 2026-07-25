# 2026-07-22 Frontier Delta Notes

## Dedup retrieval
- The required `session_search` query can surface unrelated maintenance/debug sessions when titles are noisy.
- For cron-backed briefs, inspect `~/.hermes/cron/output/<job_id>/` and read the latest three dated artifacts' `## Response` sections. This distinguishes delivered content from failed or empty attempts and is the strongest dedup record.

## Probe lessons
- Use saved, separate HTTP fetches for RSS and GitHub JSON; parse only after the files are written.
- GitHub repository paths can move: x402 activity was under `x402-foundation/x402`, not the older Coinbase path. If a canonical endpoint returns 404, verify the maintained organization/repository before concluding silence.
- A release-candidate item reported in the previous brief may receive a new, reportable status change when the stable tag lands (Ollama `v0.32.2`).
- Commits that follow a previously reported hardening burst are still reportable when they change operational behavior, such as preserving request bodies across retries or propagating settlement storage errors (x402).
- Treat routine generated traffic commits as noise; OpenJarvis clone-traffic updates were not briefing-worthy.

## Synthesis
- The useful cross-stack pattern this cycle was explicit, composable boundaries: Ollama skills/tool rounds, local MLX through a localhost API, and x402 failure propagation/retry correctness.
