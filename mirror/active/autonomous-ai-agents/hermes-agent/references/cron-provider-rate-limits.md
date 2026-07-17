# Cron provider rate limits and fallback

Observed in this session:
- `alt-chain-brief` failed with `HTTP 429` on `provider=nvidia model=z-ai/glm-5.1`.
- `daily-bathurst-weather` failed with the same `HTTP 429` on the same provider/model.
- The cron output files captured the user-visible failure:
  - `~/.hermes/cron/output/d78378fd072c/2026-06-15_07-48-43.md`
  - `~/.hermes/cron/output/30265e2e5fc7/2026-06-15_08-00-22.md`
- The request dump for the weather job showed max retries exhausted on the NVIDIA chat completions endpoint.

Workflow:
1. Treat repeated `429` on scheduled jobs as provider throttling first, not prompt or script failure.
2. Compare against a known-working cron job on a different provider/model in the same class.
3. Move the job to a less-throttled model/provider pair when the job is not latency-sensitive.
4. Re-run the job manually with `cronjob action=run` and verify the new output path / last_status.
5. If the job still fails, inspect the cron output file before changing the prompt.

Useful verification artifacts:
- `cronjob action=list` to confirm model/provider on the job record.
- `~/.hermes/cron/output/<job_id>/<timestamp>.md` for the raw failure.
- `~/.hermes/sessions/request_dump_cron_<job_id>_*.json` when the scheduler emits a request dump.
