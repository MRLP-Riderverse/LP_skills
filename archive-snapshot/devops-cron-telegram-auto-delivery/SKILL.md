---
name: cron-telegram-auto-delivery
description: Handle scheduled cron jobs whose final output should be delivered to Telegram, including the duplicate-send skip behavior when the cron job already targets the same Telegram home channel.
version: 1.0.0
author: Hermes Agent
tags: [cron, telegram, delivery, messaging, hermes]
---
# Cron → Telegram Auto-Delivery

Use this skill when a scheduled Hermes cron job is meant to notify a Telegram channel or home chat.

## Key behavior

If the cron job is already configured to deliver its final response to Telegram, **put the user-facing message directly in the final response**.

Do **not** additionally call `send_message` to the same Telegram target inside the cron run.

Why:
- Hermes cron jobs auto-deliver the final response.
- A manual `send_message` to the same `telegram:<home_channel>` target may be skipped as a duplicate (`cron_auto_delivery_duplicate_target`).
- The cleanest path is a single final response containing the notification text.

## Recommended workflow

1. Determine whether the cron job’s delivery target is Telegram.
2. If yes and the target is the same home channel that will receive the cron result, write the notification in the final response.
3. Only use `send_message` if you need an additional, separate destination.
4. If you must use `send_message`, make sure the target differs from the cron auto-delivery target.

## Verification

- Confirm the cron job’s delivery target is Telegram.
- Confirm the final response contains the intended message.
- If a direct `send_message` was attempted and skipped, check for:
  - `cron_auto_delivery_duplicate_target`
- If you are testing a model override, verify the job actually ran and inspect the cron output/logs for provider resolution errors.
- When testing a cron job from an active Telegram chat, distinguish between:
  1. the **parent chat reply** explaining the test, and
  2. the **cron auto-delivered final output**.
  These are two separate sends and can look like a duplicate if the parent also posts a full preview. For clean tests, either keep the parent reply short until the cron finishes, or test with `deliver="local"` / a temporary clone if you want zero user-facing output.

## Model/provider routing for cron jobs

Cron jobs can carry an explicit `model` override, but the provider must be a Hermes-recognized provider id.

Important findings:
- `model="gpt-5.4-mini"` is acceptable as a model override.
- `provider="openai"` failed in cron with: `Unknown provider 'openai'`.
- Hermes currently expects provider ids like `openai-codex`, `openrouter`, `anthropic`, etc., not plain `openai` in cron provider resolution.

Practical guidance:
1. If you want to pin a cron job, prefer a Hermes-native provider id.
2. If you have OpenAI OAuth/Codex access, try `provider="openai-codex"` rather than `openai`.
3. If the job is just a reminder and doesn’t need model reasoning, avoid a model override entirely and keep the prompt/output simple.
4. Test new routing with a one-shot cron job and inspect `~/.hermes/cron/output/<job_id>/...` plus `~/.hermes/logs/errors.log` if it fails.

## Pitfalls

- Don't assume `openai` is a valid provider id in Hermes cron jobs just because the model name starts with `gpt-`.
- Don't resend to the same Telegram home channel from inside the same cron run.
- Don't rely on environment variables being present unless explicitly sourced in an ad hoc terminal test; cron delivery itself should use Hermes' configured gateway path.
- Don't forget that cron jobs run in a fresh session; any provider auth or config assumptions need to be explicit and verified.
- If the job was created before a model swap in chat, the cron job may still be pinned to the old model. Explicitly update the job's model/provider before testing again.

## Headless practices: avoiding degraded AI function errors

**Problem:** Cron jobs that invoke AI models with function-calling capabilities can fail intermittently with:
```
RuntimeError: Error code: 400 - {'status': 400, 'title': 'Bad Request', 
'detail': "Function id '...': DEGRADED function cannot be invoked"}
```

This is an OpenAI API degradation issue where certain function-calling capabilities are marked as DEGRADED and unavailable in headless/automated contexts.

**Pattern:**
- **Simple deterministic tasks** (weather fetches, reminder messages, script outputs) should run **without AI model involvement** when possible.
- If a cron job consistently works at one time (e.g., midday) but fails at another (e.g., morning), suspect intermittent AI provider degradation rather than script failure.
- The same job may succeed on retry if the degradation is transient, but this is unreliable for production cron workloads.

**Symptoms:**
- Job shows `last_status: "error"` with DEGRADED function error in logs
- Manual execution of the underlying script works fine
- Similar jobs without AI model involvement succeed consistently
- Error message references OpenAI function-calling degradation

**Solutions (in priority order):**

1. **Remove AI involvement for simple tasks** (preferred):
   - For script-based cron jobs (weather, reminders, data fetches), ensure `model: null` and `provider: null`
   - Let the cron job execute the script and return output directly
   - This matches the pattern used by successful jobs like `midday-bathurst-weather`

2. **Restrict toolsets when AI is required**:
   - Add `"enabled_toolsets": ["terminal"]` to the cron job configuration
   - This prevents the job from attempting degraded function-calling APIs
   - Use when the task genuinely needs AI reasoning but not external function calls

3. **Use local models for headless reliability**:
   - Configure cron jobs to use local Ollama models (e.g., `qwen3:8b`) instead of cloud providers
   - Local models don't have function-calling degradation issues
   - Pattern: `model: "qwen3:8b"`, `provider: "ollama"` (if available)

4. **Add retry logic for transient failures**:
   - For critical jobs that must use cloud AI, implement retry with exponential backoff
   - Log failures to track degradation patterns
   - Consider fallback to cached data or [SILENT] mode on repeated failures

**Verification checklist:**
- [ ] Check `~/.hermes/cron/output/<job_id>/<timestamp>.md` for DEGRADED function errors
- [ ] Verify script runs successfully when executed manually
- [ ] Compare job configurations: working jobs vs failing jobs (look for model/provider differences)
- [ ] Inspect `jobs.json` to confirm `model` and `provider` are null for simple script jobs
- [ ] Test by running `hermes cron run <job-id>` and observing behavior
- [ ] If job succeeds on retry, suspect transient degradation rather than permanent fix

**Example: Morning vs Midday Weather Jobs**
```
Morning (FAILING): daily-bathurst-weather
  - model: null, provider: null
  - Still hitting DEGRADED error (may inherit tool config from context)
  - Fix: Ensure no toolset inheritance, or add enabled_toolsets: ["terminal"]

Midday (WORKING): midday-bathurst-weather
  - model: null, provider: null
  - No AI involvement, pure script execution
  - Always succeeds
```

**Key insight:** The phrase "headless practices" refers to the discipline of designing cron jobs that work reliably without human intervention. AI model providers deprecating or degrading function-calling capabilities in automated contexts is a known pattern. Simple, deterministic tasks should avoid AI overhead entirely; complex reasoning tasks should use local models or restricted toolsets to avoid degraded API errors.

## Reference Files

- `references/degraded-function-error.md` - Diagnostic guide for DEGRADED function errors in headless cron jobs
