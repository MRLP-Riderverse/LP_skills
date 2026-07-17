# Degraded Function Error in Headless Cron Jobs

## Error Signature

```
RuntimeError: Error code: 400 - {'status': 400, 'title': 'Bad Request', 
'detail': "Function id '<uuid>': DEGRADED function cannot be invoked"}
```

## Context

This error occurs when a Hermes cron job attempts to use OpenAI's function-calling API in a headless/automated context where those functions have been marked as DEGRADED by the provider.

## Diagnostic Steps

1. **Check cron output logs:**
   ```bash
   ls -lt ~/.hermes/cron/output/<job_id>/
   cat ~/.hermes/cron/output/<job_id>/<latest-timestamp>.md
   ```

2. **Verify script works manually:**
   ```bash
   cd /home/midnight/.hermes/skills/weatherAPI-home
   python3 weather_telegram.py
   ```
   If this succeeds but the cron fails, the issue is AI model involvement, not the script.

3. **Compare job configurations:**
   ```bash
   python3 -c "import json; jobs = json.load(open('~/.hermes/cron/jobs.json'))['jobs']; 
   print([(j['name'], j.get('model'), j.get('provider')) for j in jobs if 'weather' in j['name']])"
   ```

4. **Check for toolset inheritance:**
   - Look for `enabled_toolsets` in job configuration
   - Compare with working jobs (e.g., `daily-session-review-notes` uses `["terminal"]`)

## Known Patterns

### Morning Weather (FAILING)
- Job: `daily-bathurst-weather` (ID: 30265e2e5fc7)
- Schedule: `0 8 * * *`
- Error: DEGRADED function cannot be invoked
- Root cause: Intermittent AI function-calling degradation

### Midday Weather (WORKING)
- Job: `midday-bathurst-weather` (ID: b12143ed4ced)
- Schedule: `0 10 * * *`
- Status: Always succeeds
- Reason: No AI model involvement, pure script execution

## Resolution

See the "Headless practices" section in `cron-telegram-auto-delivery` skill for complete guidance.

Quick fix options:
1. **Best:** Ensure `model: null` and `provider: null` for simple script jobs
2. **Alternative:** Add `enabled_toolsets: ["terminal"]` to restrict AI capabilities
3. **Fallback:** Use local Ollama models instead of cloud providers

## Related Files

- Skill: `devops/cron-telegram-auto-delivery/SKILL.md`
- Cron logs: `~/.hermes/cron/output/<job_id>/`
- Job config: `~/.hermes/cron/jobs.json`
