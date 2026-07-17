# 2026-06-12 Session Notes

Compact addendum from the June 12/13 delta-brief run.

## Verified fresh signals
- **Solana:** Agave `v4.1.0-rc.0` (testnet) published 2026-06-12.
- **Ollama:** `v0.30.8` published 2026-06-12; body mentions prompt caching decoupled from context shift and MLX snapshots during prompt processing/speculative decoding.
- **LangGraph:** `1.2.5` published 2026-06-12; includes `updateState` empty-thread fix and HTTPS dev-server cert support.
- **x402:** no obvious release artifact; commit stream is the best freshness signal. On 2026-06-12 the repo showed a release commit, builder-code docs updates, and payment/error-handling fixes.
- **Open Wallet Standard core:** commit activity on 2026-06-10/11 includes x402 docs and x402 4xx payment-rejection messaging; releases lag behind commits.
- **OpenJarvis:** canonical repo appears to be `open-jarvis/OpenJarvis`; releases are stale, but commits continued on 2026-06-11 to 2026-06-13, including eval harness hardening and Windows/Ollama readiness fixes.
- **Simon Willison:** Atom feed parsing via regex worked reliably; 2026-06-13 item was a statement on the US government directive to suspend access to Fable 5 / Mythos 5.
- **Matt Webb:** 2026-06-12 essay coined "wet words" / "wet thoughts" as a human-authored framing.

## Workflow notes
- For delta-briefs, compare against the last 3 briefings and treat repeated items as stale unless there is a concrete new release/post/commit or a status change.
- For x402 and Open Wallet Standard, commits are first-class signal even when releases lag.
- For OpenJarvis, check the canonical repo commits every run; do not rely on release cadence.
- If a topic is quiet in the window, leave the section silent rather than re-explaining prior context.
