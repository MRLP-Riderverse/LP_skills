---
name: cognitive-profile-review
description: Use for learning profile reviews from archives.
category: research
---

# Cognitive Profile Review

Use this class-level workflow when the user asks for a rough assessment of intellectual progress, learning strengths, reasoning style, or why conventional tests may not reflect their ability. The output is a grounded qualitative profile, not a psychometric diagnosis or precise IQ estimate.

## Core rule

Do not equate the presence or absence of literal academic vocabulary with the presence or absence of the underlying ability. A user may express mathematics through budgets, pricing, allocations, incentives, unit economics, token mechanics, and sustainability models without naming algebra or probability.

## Evidence hierarchy

1. User-authored raw notes and direct answers.
2. Verified implementation artifacts and session logs showing the user framing, debugging, testing, and documenting real systems.
3. Durable project notes and structured GBrain pages.
4. AI-generated recaps or summaries, used only as secondary evidence and clearly labeled.
5. Tiny informal question probes, useful for a snapshot of specific skills but never sufficient for a numeric IQ estimate.

## Workflow

### 1. Establish the actual question

Clarify whether the user wants a learning-gap map, reasoning-style profile, comparison between applied and formal skills, test-performance interpretation, study plan, or psychometric evaluation. If the request is obvious, act without unnecessary clarification. Redirect requests for a clinical score toward a qualified standardized assessment.

### 2. Cross-reference the archive

Inspect the relevant raw note folder, GBrain retrieval, project artifacts, and past-session records. Search both exact terms and semantic proxies. For quantitative reasoning, search for: budget, split, percentage, per-member, monthly, pricing, distribution, allocation, pool, revenue, cost, reserve, incentives, sustainability, token, Solana, x402, and community economics.

If session search returns no hits, do not conclude that no history exists. Fall back to local archive/project files and disclose the evidence limitation.

### 3. Separate the profile into domains

Report each domain independently: applied economics and allocation; systems thinking and abstraction; technical building and debugging; verbal synthesis and explanation; formal logic; probability/statistics; traditional mathematics and notation; pattern/puzzle fluency; metacognition and learning strategy; and test-taking conditions/format sensitivity.

Use labels such as strong, established, developing, underformalized, or unclear. Avoid flattening an uneven profile into one score.

### 4. Assess informal questions carefully

For each response, distinguish exact correctness, method quality, notation/transcription slips, conceptual misunderstanding, failure to answer the prompt's narrow target, useful broader insight, and context effects such as phone use, interruptions, tool switching, time pressure, or subject aversion.

The user should answer the formal question first, then expand into systems implications. If they answer the larger real-world question instead, preserve the insight but identify the missing formal specification.

### 5. Handle tool use correctly

Calculator, Notes, code, search, and external references are cognitive instruments. Do not label tool use as dependence without evidence. In applied work, assess whether the user can frame the problem, select a model, identify what needs calculation, verify outputs, and interpret consequences.

For a clean probe, offer an optional retest with paper, a quiet setting, no context switching, and explicit timing. Do not require an artificial no-tool condition unless the user wants test-like measurement.

### 6. Communicate the result

Lead with the correction if the earlier assessment was too literal. State what the archive supports and what it cannot establish. A useful synthesis may be: “Applied reasoning and systems synthesis are strong; formal probability or notation may be undertrained. A small informal probe cannot establish an IQ score.”

Do not invent a numeric IQ or narrow range from five questions. If the user asks for a score, explain why the evidence is insufficient and offer a standardized-assessment route or a broad qualitative band only with strong caveats.

## Common pitfalls

- Counting occurrences of “math” and calling the result a measure of mathematical ability.
- Treating a missed puzzle as evidence of low general intelligence.
- Treating probability mistakes as global reasoning failure when the user has subject aversion or little formal practice.
- Ignoring applied economics because it appears as community/product language.
- Rewarding a broad systems answer without noting that the formal prompt was not fully answered.
- Ignoring testing conditions or the user's correction that the environment was distracting.
- Presenting AI-generated archival prose as proof of the user's own accomplishment.
- Defending an initial ranking after the user supplies better evidence.

## Verification checklist

- [ ] Raw notes and GBrain were both considered where available.
- [ ] Search terms included applied quantitative proxies, not only academic labels.
- [ ] AI-generated summaries were separated from direct/user-authored evidence.
- [ ] At least five domains were assessed separately.
- [ ] Context and tool-switching were recorded.
- [ ] Arithmetic and probability claims were verified deterministically.
- [ ] No precise IQ was inferred from an informal probe.
- [ ] User corrections changed the assessment where warranted.

See `references/cognitive-profile-review.md` for the session-derived rubric and examples.
