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

## Deterministic-job triage

Before changing a failing model route, inspect whether the job is actually doing model work:

1. Read the full job definition, including `script`, `no_agent`, and the exact prompt.
2. If the job only invokes a known local script and returns its stdout, convert it to `no_agent: true` with that script instead of paying for an agent to relay command output.
3. For a fixed reminder, use a small executable script which prints the exact notification body.
4. Test the backing script directly before updating the cron. Do not use `cronjob run` for a scheduled notification if it would send the user an unwanted duplicate.
5. `model` and `provider` values retained on a `no_agent: true` job are inert; the script and stdout are what matter.

When a model is retired (for example an HTTP 410 / end-of-life response), audit both cron definitions and main configuration: fallback routing plus auxiliary compression, skills, MCP, session-search, and vision routes can preserve the dead dependency.

### Retired-model audit nuance

- A `no_agent: true` cron job does not invoke its stored `model` / `provider`; its script and stdout are authoritative. Still update those inert metadata fields when the operational policy is to fully retire a model, so later audits do not misread them as active routes.
- Search results may contain the retired model solely inside historical `last_error` text. Treat that as evidence of the incident, not a live dependency. Verify active model/provider fields, fallback routing, and auxiliary routes separately.
- Do not rely only on a summary config display for auxiliary routing. Inspect the persisted YAML keys—especially both `compression.*` and `auxiliary.compression.*`—before declaring a provider migration complete.

See `references/retired-model-and-no-agent-migration.md` for the migration checklist and routing pattern.

## Pitfalls
- `cronjob run` can change `next_run_at`; verification still requires a real output file.
- A successful config update is not proof of success. Always verify an intentional rerun or, when delivery would be intrusive, test the backing script directly.
- Do not assume a report was captured from a failed run unless there is a matching file in cron/output.
- For rate-limited briefs, rerun after routing changes instead of asking the user to wait for the next schedule.
- Do not mistake an end-of-life HTTP 410 for rate limiting or a scheduler failure; replace the route or remove the agent from deterministic work.

## References
- See `references/provider-routing-notes.md` for the current provider/model quirks and a verified rerun pattern.
