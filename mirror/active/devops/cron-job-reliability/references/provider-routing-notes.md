# Provider routing notes for Hermes cron jobs

Session-derived notes for rerouting and verifying scheduled jobs after provider failures.

## Known-good routing
- `gpt-5.4-mini` via `openai-codex` worked for the Acadian brief jobs and the daily GBrain sync status job after rerouting.
- `openai` should not be used as a cron provider id here.
- `z-ai/glm-5.1` on `nvidia` showed repeated `HTTP 429` pressure on multiple brief/sync jobs in this setup.

## Verified rerun pattern
1. Update the job model/provider.
2. Run the job immediately with `cronjob run`.
3. Check `~/.hermes/cron/output/<job_id>/` for a new timestamped output file.
4. Treat the new file contents as the real proof of success, not the job metadata alone.

## Example evidence from this session
- Québec-Acadie brief (`2d22b8433a28`) reran successfully after switching to `gpt-5.4-mini` via `openai-codex`.
- Nouvelle-Aquitaine brief (`6efc7fe740ed`) reran successfully after the same swap.
- Daily GBrain sync status (`a39e977fa5b0`) was also moved to `gpt-5.4-mini` via `openai-codex` after a 429 failure.
