# Codex banked reset behavior

Source: Hermes Agent documentation, CLI Interface and Messaging Gateway pages, consulted 2026-08-03.

## Verified semantics

- `/usage` shows token usage for the session.
- With the `openai-codex` provider, `/usage` can also show banked usage-limit resets.
- A normal `/usage reset` redemption is guarded: Hermes refuses to redeem while the current limit still has capacity.
- The documented override is `/usage reset --force`; it redeems even before exhaustion, so using it early can waste the banked reset.
- A banked reset restores the full provider allowance; it is not a Hermes conversation reset or context compression operation.

## Safe explanation pattern

When the user only asks what the status means, say that `/usage` was read-only and did not consume the banked reset. Explain “1 banked” as one saved provider-side allowance restoration held in reserve. Do not execute a reset command to inspect or confirm this state.

## Source excerpts captured during research

- CLI documentation search result: “Hermes refuses to redeem while your limits aren't exhausted (a banked reset restores the full allowance, so spending it early wastes it) — pass `/usage reset --force` to redeem anyway.”
- Messaging documentation search result: “Show token usage for this session (`/usage reset [--force]` redeems a banked Codex limit reset).”
