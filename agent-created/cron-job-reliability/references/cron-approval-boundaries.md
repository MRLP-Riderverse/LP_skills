# Cron approval-boundary reference

## Durable distinction

A user-approved cron definition authorizes the schedule and prompt. It does not authorize every future terminal command generated during the run. Hermes keeps this boundary because prompts, loaded skills, fetched content, and model-generated commands can change after job creation.

## Runtime path

Scheduled runs bind `HERMES_CRON_SESSION=1`. The approval implementation explicitly treats cron as **not** a gateway approval context, even when delivery is to Telegram or another gateway. This prevents a pending approval from waiting forever for a listener that is not part of the unattended run.

The terminal pre-exec path is approximately:

```text
terminal tool
  -> _check_all_guards(command)
     -> user deny rules / bypass state
     -> permanent command allowlist
     -> dangerous-command detection
     -> Tirith/content security (when enabled)
     -> cron approval policy
```

With:

```yaml
approvals:
  mode: manual
  timeout: 60       # interactive approval wait; not a cron fix
  cron_mode: deny   # cron approval-gated actions fail closed
```

`cron_mode: approve` is the explicit unattended mode, but it is global to cron jobs and should not be enabled without reviewing the trust implications.

## Diagnostic evidence pattern

Look for all of these before concluding an RSS/network outage:

- `status: pending_approval` and `approval_pending: true` in Hermes error logs.
- A command field containing `curl`, `wget`, or another terminal invocation.
- Cron output saying RSS collection was blocked by the command-approval gate.
- The active config containing `approvals.cron_mode: deny`.
- A delivered report with scheduler success metadata but a stale/continuity-report disclaimer.

Do not infer the exact dangerous pattern from the presence of `curl` alone. Plain `curl` is not necessarily a dangerous-command regex match; the final guard may combine command detection, Tirith, and approval context. Preserve the actual `description`/`pattern_key` from the terminal result when available.

## Repair decision

Prefer this order for recurring RSS/news jobs:

1. Move fetching/parsing into a deterministic local collector (`no_agent: true` or a precomputed local artifact).
2. Add per-feed timeout, retry/backoff, XML validation, cache, and explicit fresh/stale/error status.
3. Let the agent summarize verified local results rather than inventing shell commands.
4. Keep `cron_mode: deny` unless all cron terminal actions are intentionally trusted.
5. If using a command allowlist, test the exact command shape and remember the allowlist is global.
6. Use `cron_mode: approve` only as a deliberate global policy change.

Increasing `approvals.timeout` to 300 seconds can help interactive Telegram approval buttons but does not resolve unattended cron behavior while `cron_mode` remains `deny`.
