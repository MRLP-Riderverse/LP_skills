# Timezone management in Hermes

This reference captures the current timezone model used by Hermes Agent.

## Config shape
- `timezone` in `~/.hermes/config.yaml` is a single IANA timezone string.
- Examples: `America/Halifax`, `America/New_York`, `UTC`, `Asia/Kolkata`.
- Empty string or missing key means: use server-local time.
- No extra structured data is required in the config.

## Resolution order
1. `HERMES_TIMEZONE` environment variable
2. `timezone` in `config.yaml`
3. server-local time via `datetime.now().astimezone()`

## Where it is consumed
- `hermes_time.now()` for the agent clock / conversation timestamps
- `cron/jobs.py` and `cron/scheduler.py` for schedule calculations
- `gateway/run.py` bridge that exports `config.yaml -> HERMES_TIMEZONE`
- `tools/code_execution_tool.py` injects `TZ` into child processes
- migration code in `hermes_cli/config.py` can seed `timezone` from older `HERMES_TIMEZONE`

## Important caveats
- The resolved timezone is cached in `hermes_time`; changes require a restart or cache reset/new session to take effect.
- Invalid timezone strings log a warning and fall back safely to server-local time.
- Not every `datetime.now()` in the codebase is meant to use the Hermes timezone; internal/auth/logging/platform timestamps often stay UTC or server-local by design.

## Practical guidance
- For user-facing “what time is it?” behavior, set only the IANA string in `timezone`.
- Do not add extra fields unless a new feature explicitly needs them.
- When debugging scheduling bugs, check both `config.yaml` and any stale `HERMES_TIMEZONE` in the environment.