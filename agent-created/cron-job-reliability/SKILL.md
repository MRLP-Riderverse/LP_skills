---
name: cron-job-reliability
description: Manage Hermes cron jobs that fail, need provider/model routing changes, or must be rerun and verified after a fix.
---
# Cron Job Reliability and Model Routing

Use this when managing Hermes scheduled jobs that fail with 429/503/timeouts, need a model/provider swap, or need a rerun to prove the fix worked.

## Triggers
- The user mentions cron, scheduled jobs, briefs, sync jobs, delivery failures, rate limits, timeouts, or provider swaps.
- A job needs to be updated and then immediately verified by rerunning it.

## Workflow
1. Inspect the job first: `cronjob list` or `cronjob` read/update output.
2. Identify whether the failure is a provider/routing issue, a prompt issue, or a script issue.
3. If the job is agent-driven and the provider is throttling, prefer a routing fix over blind retries.
4. Known-good routing on this setup:
   - `gpt-5.4-mini` via `openai-codex` works for Hermes cron jobs.
   - `openai-api` can also be valid when a cron job is explicitly meant for that provider.
   - `provider: openai` is not a valid cron/provider id here; do not use it.
   - `z-ai/glm-5.1` on `nvidia` has shown recurring 429 / timeout pressure for some brief and sync jobs.
5. After `cronjob update`, run the job immediately with `cronjob run` when the user asked to resend/verify.
6. Verify the rerun by checking the newest file under `~/.hermes/cron/output/<job_id>/`.
7. Confirm the output body exists and matches the intended delivery shape; do not rely only on job metadata.
8. If the job is `no_agent:true`, leave model/provider alone and focus on the script path plus the emitted stdout.

## Pitfalls
- `cronjob run` can change `next_run_at`; verification still requires a real output file.
- A successful config update is not proof of success. Always verify the immediate rerun.
- Do not assume a report was captured from a failed run unless there is a matching file in cron/output.
- For rate-limited briefs, rerun after routing changes instead of asking the user to wait for the next schedule.

## References
- See `references/provider-routing-notes.md` for the current provider/model quirks and a verified rerun pattern.
