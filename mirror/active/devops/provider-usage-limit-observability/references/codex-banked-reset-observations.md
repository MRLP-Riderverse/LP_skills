# Codex banked-reset observations

## Evidence gathered

- Hermes' current CLI documentation says `/usage` can show OpenAI Codex usage details and banked usage-limit resets.
- The same documentation says Hermes avoids redeeming a banked reset while ordinary limits still have capacity, because early redemption wastes the reserve; an explicit ` /usage reset --force` path can redeem early.
- OpenAI Help Center guidance describes a banked reset as an available reset count in the Codex usage summary and explains how to use one. It also notes that referral rewards vary by offer and plan.
- Public OpenAI guidance located during this review did not state a universal monthly grant, expiry duration, stacking cap, or automatic replenishment schedule.

## Operational interpretation

A visible `1 reset banked` is best reported as one currently available account-level Codex reset credit. It is not evidence of a permanent subscription entitlement. It may be associated with a promotion, account eligibility, plan behavior, or another provider-side grant whose terms are not visible in Hermes.

Keep these separate:

- ordinary Codex allowance and its normal reset window;
- banked reset credits;
- Hermes session reset/context controls;
- promotional or referral terms.

## Safe wording

Prefer: “OpenAI currently reports one redeemable reset credit for this account; public documentation does not establish whether this specific credit expires, recurs monthly, or stacks indefinitely.”

Avoid: “You get one every month,” “they never expire,” or “unused credits always roll over,” unless the user's specific offer explicitly says so.

## Re-check rule

Provider policy can change. Before making a future entitlement claim, inspect the current provider account display and current OpenAI documentation again. Treat the visible account balance as authoritative for present state, not as proof of future distribution policy.

## Links

- Hermes CLI: https://hermes-agent.nousresearch.com/docs/user-guide/cli
- OpenAI Help Center: https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
