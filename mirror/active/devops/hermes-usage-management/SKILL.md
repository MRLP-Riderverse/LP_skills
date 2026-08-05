---
name: hermes-usage-management
description: Explain Hermes usage safely without redeeming quota resets.
category: devops
---

# Hermes Usage Management

Use when a user asks about Hermes `/usage`, token consumption, provider quotas, Codex limits, banked resets, or whether an informational command has side effects.

## Core safety rule

Separate **inspection** from **redemption**. If the user asks what a usage/reset message means, explain it without invoking a reset command or changing provider state. A user explicitly asking for explanation is not authorization to redeem a quota reset.

## Telegram and slash-command interpretation

- `/usage` is an informational command. It reports usage for the current session and, on the `openai-codex` provider, may show banked usage-limit resets.
- `/usage reset` is an operational action that attempts to redeem a banked Codex limit reset.
- `/usage reset --force` explicitly permits redemption even when the current limit is not yet exhausted; this can waste a banked reset and should never be run merely to explain the status.
- Do not confuse provider quota reset with Hermes session controls: `/new` or `/reset` starts a fresh conversation, while `/compress` manages context. Neither redeems a Codex quota reset.

## Meaning of a banked reset

A banked reset is a saved provider-side usage allowance restoration. “1 reset banked” means one stored reset is available; it is not an extra current-session token balance, a context reset, or proof that the current quota is exhausted. Explain it as an emergency refill held in reserve.

Hermes is designed to refuse normal reset redemption while the current provider limit still has room, preserving the banked reset until it is useful. The force flag bypasses that protection.

## Response workflow

1. Determine whether the user wants explanation, inspection, or an actual redemption.
2. For explanation only, do not call shell commands, `/usage reset`, provider APIs, or any state-changing tool.
3. State clearly what `/usage` did and did not do.
4. Distinguish the three layers: Hermes session/context, current provider allowance, and banked provider reset.
5. Mention the force-action risk in plain language, without reproducing it as an invitation to run it.
6. Keep the answer concise unless the user asks for the underlying provider mechanics.

## Pitfalls

- Never treat “reset” in a status display as proof that a reset was consumed.
- Never use a live reset command to verify what a read-only `/usage` display means.
- Do not claim that the banked reset is a universal Hermes feature across all providers; qualify it as Codex/provider-specific when appropriate.
- Do not conflate token usage, context compression, session reset, and provider quota replenishment.

## Lifetime Token Audits

When a user wants to verify a lifetime-scale Hermes token milestone (for example, a public claim or a personal milestone), distinguish the dashboard-like report from the direct local accounting audit:

1. Run `hermes insights --days 9999` for the human-readable total, date span, models, and platforms.
2. For proof, audit `~/.hermes/state.db` directly. The `session_model_usage` table is the richer source because it records model-routed usage; sum `input_tokens + output_tokens + cache_read_tokens + cache_write_tokens`.
3. Explain the metric precisely: Hermes’ displayed **Total tokens** includes cached reads. This is legitimate for “AI tokens processed,” but it is not the same as uncached input + output, and it should not be casually framed as tokens “spent.”
4. Check whether other profile databases exist before calling it an all-Hermes lifetime total. A single default-profile database supports a verified local-history claim, not a claim about deleted, migrated, or other-machine history.
5. Expect a small difference between a prior Insights snapshot and a later direct query: the live session can add usage while the audit is being run.

Recommended public wording: **“1B+ AI tokens processed”** or **“1B+ Hermes tokens processed locally verified.”** Avoid “1B tokens spent” unless billing-specific usage is independently established.

## Reference

See `references/codex-banked-reset.md` for the authoritative documentation-derived behavior and terminology.
