# Multi-group static directory source-routing reference

Use this contract when deriving a new directory from an existing static directory system while keeping datasets independent.

## Source → route → export → render

```text
<project>/inbox/
  ├── explicit Group: <group>  -> <group>/inbox/
  ├── conservative unambiguous signals -> <group>/inbox/
  └── ambiguous/no group -> inbox/needs-review/

<project>/<group>/inbox/
  -> reviewed/promotion
<project>/<group>/entries/<slug>/entry.md + meta.json
  -> exporter --directory <project>/<group> --site <site>/<group>
<site>/<group>/assets/*.json
  -> static renderer
```

The browser/site must never infer or own group membership. Routing belongs to the source repository; the exporter consumes one group root at a time.

## Routing rules

1. Prefer an explicit `Group: <group>` field in the draft template.
2. If explicit metadata is absent, infer only from an unambiguous combination of category + domain tags.
3. Unknown or mixed signals go to `inbox/needs-review/`; never silently choose a group.
4. Refuse to overwrite a same-name destination draft.
5. Keep raw intake permissive; apply canonical identity, schema, privacy, and public/private decisions during promotion.

## Dry-test matrix

Before a public repository or deployment:

- explicit group routes to the intended group inbox;
- clear inferred signals route correctly;
- ambiguous input is quarantined for review;
- non-draft files are ignored;
- promoted entries and drafts both appear in the group payload as intended;
- generated payload has no records from the parent/derivative project;
- draft headings lose workflow prefixes such as `Draft:` in public display names;
- exporter fails closed when the target site repository is missing;
- Python syntax, unit tests, export, and a local HTTP response all pass.

## Derivative boundaries

For a fork/derivative, copy reusable protocol/tooling but do not copy parent records, language data, branding, geography fallbacks, or fixtures without adapting them. Search generated payloads and tests for parent-specific names before review.

## Handoff ergonomics

For a nontechnical steward, optimize for one top-level inbox and one obvious group marker. Keep generated site assets separate from source truth, and expose one repeatable route/export command. A dedicated entry-intake skill should wrap these deterministic actions, preview the result, and stop before commit/push unless explicitly approved.
