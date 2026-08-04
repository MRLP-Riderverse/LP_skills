---
name: provider-usage-limit-observability
description: Use for safe provider quota and reset inspection.
category: devops
---

# Provider Usage-Limit Observability

Use this skill when a user asks what a usage counter, quota reset, banked allowance, or emergency refill means in an agent/provider integration. The goal is to explain live account state without accidentally redeeming a scarce provider-side resource.

## Core distinction

Separate three layers:

1. **Agent/session state** — conversation context, `/new`, `/reset`, compression, session history, and local token accounting.
2. **Provider account state** — plan allowance, rolling/daily/weekly limits, reset timing, credits, and account eligibility.
3. **Promotion or entitlement policy** — grants, referrals, campaigns, caps, expiration, stacking, and replenishment rules.

A provider-side reset does not erase an agent session; a fresh agent session does not replenish provider quota.

## Safe inspection workflow

1. Identify the active provider/model path, but do not switch models or redeem anything merely to inspect it.
2. Use the provider's read-only usage/status command or dashboard. For Hermes, `/usage` is observational; it should not be described as consuming a reset.
3. Record the exact visible fields: current usage, remaining allowance, ordinary reset time, banked-credit count, and any eligibility/expiry text.
4. Explain the narrow meaning supported by the display and the provider's authoritative documentation.
5. Explicitly list what is *not* documented. Do not infer a monthly entitlement, expiry policy, stacking cap, or automatic replenishment schedule from a single observed count.
6. Treat force/reset/redeem commands as consumptive actions. Never run them during explanation-only requests.
7. If the user is near exhaustion, frame a banked credit as an emergency reserve, not as a long-term capacity strategy, unless the provider explicitly guarantees recurring credits.

## Codex/Hermes pattern

With Hermes' `openai-codex` provider, `/usage` may display a banked usage-limit reset count. Hermes documentation describes a normal reset path that avoids redeeming while ordinary limits still have room, and an explicit force path such as `/usage reset --force` for early redemption. The account-level credit is supplied by OpenAI/Codex; Hermes reports or requests redemption but does not grant the credit.

A visible `1 reset banked` means one currently reported redeemable credit. It does **not** by itself prove that the account receives one credit per billing month, that credits persist forever, or that unused credits stack without limit.

## Explanation template

When documenting a discovery, preserve:

- **Observed:** exact read-only display or action that produced the evidence.
- **Current meaning:** the narrow operational interpretation.
- **Does not guarantee:** recurrence, expiration, stacking, persistence, cap, plan inclusion, or future eligibility unless explicitly documented.
- **Operational advice:** when to preserve the reserve and what command would consume it.

Use cautious terms such as “currently reported,” “account-level,” “promotion/eligibility-dependent,” and “not publicly specified” where appropriate.

## Pitfalls

- Do not call a provider reset a Hermes `/reset`; they affect different layers.
- Do not claim “one per month” merely because one credit is visible.
- Do not claim credits persist or stack indefinitely without explicit provider policy.
- Do not run a force-redemption command while answering a question about what the balance means.
- Do not treat community reports or a third-party tracker as stronger evidence than the provider's account display and official documentation.
- Do not overstate what a provider dashboard omits; say the policy is unspecified rather than asserting that no policy exists.

## References

- `references/codex-banked-reset-observations.md` — condensed source notes and the current Codex-specific interpretation; re-check upstream documentation before making entitlement claims.
