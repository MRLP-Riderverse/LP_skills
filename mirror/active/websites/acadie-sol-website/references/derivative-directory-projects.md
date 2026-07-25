# Derivative community directory projects

Use this reference when a local steward wants a focused directory derived from the Acadie.sol architecture without joining the Acadie dataset.

## Recommended shape

```text
<community>-directory/       # source-of-truth repository
└── <group>/                  # first local directory subset
    ├── entries/
    ├── inbox/
    ├── schemas/
    ├── scripts/
    └── tests/

<community>/                 # static site repository
└── <group>/
    ├── index.html
    ├── directory.html
    ├── entry.html
    ├── search.html
    └── assets/
```

The source repo remains human-readable Markdown plus metadata; the site repo receives generated JSON only through the exporter.

## Controlled derivation checklist

1. Inspect the parent data/site repositories and their working-tree status before copying.
2. Copy reusable protocol infrastructure: exporter, schema, validation, tests, templates, docs, and empty data folders.
3. Explicitly exclude parent entries, inbox drafts, events, locations, regions, media, branding, slogans, and geography.
4. Patch exporter defaults and tests for the new group’s geography and language contract.
5. Build a minimal English-first site: landing page, browse/search surface, detail route, and generated payloads. Add local-language fields only from steward-supplied copy.
6. Export against an empty dataset and verify counts are zero, payloads are valid, and no parent records appear.
7. Run unit tests, syntax checks, `git diff --check`, and a local HTTP smoke test before creating remotes or committing.
8. Keep remote creation, commit, and push as separate approval points when the user prefers review before publication.

## Common failure modes

- Blindly copying the parent repo leaks records or embeds the parent community’s geography and branding.
- Flattening the first group at the new repo root makes future Manila groups harder to add cleanly.
- Reusing the full parent homepage imports features the new steward did not ask to maintain.
- Leaving the parent shell’s slogan, wordmark, language detector, or storage keys in the derivative creates visible identity leakage and browser-state collisions.
- Treating a successful exporter run as sufficient: verify the generated payload and a served HTML route too.
