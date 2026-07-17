# Frontier Stack Research Task

Deep dive the following tools/protocols and compare them as parts of a resilient builder stack:

TARGETS:
- OpenCode
- OpenHarness
- OpenSpace
- MassGen
- Open Wallet Standard (OWS)
- x402

GOALS:
- explain what each one actually is
- identify the layer it belongs to:
  - cockpit/interface
  - harness/wrapper
  - orchestration
  - wallet/signing rail
  - payment/access rail
  - memory/evolution layer
- determine whether it is usable today
- determine whether it is safe or mature enough for real workflows
- identify overlap and non-overlap
- compare OpenCode vs MassGen directly
- evaluate whether OpenCode work is portable/recoverable if the app crashes or disappears
- evaluate whether x402 can be implemented today in practice
- evaluate whether OWS is mature enough for policy-aware agent signing
- assess where OpenHarness/OpenSpace fit relative to a local-first, provider-agnostic philosophy

FRAMEWORK:
For each tool/project, answer:
1. What is it?
2. What problem does it solve?
3. What layer of the stack is it?
4. What makes it different?
5. Is it usable today?
6. What are the lock-in / resilience implications?
7. Is it best as a foundation, an add-on, or R&D only?

Then provide:
- a comparison table
- a recommended stack for a local-first builder
- practical next actions
- cautions
- plain-language conclusion

Important:
- treat interface as replaceable
- treat harness/workspace/policy/payment/signing layers as the real long-term stack
- do not overvalue hype, branding, or lab loyalty