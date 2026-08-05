---
name: official-capability-research
description: "Use when verifying official product capabilities."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research, official-docs, capability-verification, source-review, citations]
    category: research
---

# Official Capability Research

Use this skill when a user asks whether a product, framework, or integration
supports a specific feature, especially when the answer must be grounded in
official documentation and official source code.

## Evidence hierarchy

Classify every finding before reporting it:

1. **Documented and user-facing** — official docs state the feature, command,
   configuration, schema, example, callback contract, or limit.
2. **Implemented internally** — official source code demonstrates behavior, but
   that does not prove the behavior is a supported extension point.
3. **Proposed/requested** — an official issue or pull request asks for the
   feature, exposes a gap, or describes a workaround. Do not call it shipped.

Keep these categories separate in the final answer. If the requested feature
is absent from docs, say so directly and identify the closest documented
mechanism.

## Workflow

1. Search the official documentation domain for the exact feature terms and
   likely adjacent mechanisms.
2. Fetch or inspect the relevant official documentation page. Record exact
   URLs and short quotes for claims about behavior, limits, and examples.
3. Search the official source repository for implementation evidence. Prefer
   stable file URLs and name the relevant class/function/module only when
   verified.
4. Search official issues only to identify gaps, feature requests, regressions,
   or internal callback paths. Label issue evidence as proposal/maintenance
   evidence, not as API documentation.
5. Answer in an actionable structure: supported types/features, configuration
   or extension points, callback/event handling, limits, examples, and nearest
   supported alternative.
6. Do not invent configuration keys, public schemas, callback prefixes, or
   examples from generic library knowledge. If a detail is not documented or
   verified in source, mark it as undocumented.

## Citation discipline

Use exact official URLs, with inline citations or a compact Sources list. Quote
only small snippets. Search-result snippets can help locate a page, but claims
about implementation or limits should be tied to the underlying official page
or source whenever available. Distinguish a source file's built-in behavior
from a supported customization surface.

## Reusable reference

See `references/official-capability-research.md` for the evidence checklist and
reporting template.

## Pitfalls

- Treating an internal implementation as a supported plugin/API contract.
- Treating an open feature request as evidence that the feature is released.
- Reporting generic platform limits without confirming the product's own
  documented cap or clamping behavior.
- Giving a workaround without stating whether it is documented, source-level,
  or maintenance-heavy.
- Omitting the nearest supported mechanism when the requested capability is
  not covered.
