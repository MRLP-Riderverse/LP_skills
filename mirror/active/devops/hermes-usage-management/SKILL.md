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

## Reference

See `references/codex-banked-reset.md` for the authoritative documentation-derived behavior and terminology.
