# Identity Correction and Compact Provenance

Use this when a community steward corrects an identity, SNS name, username, or public attribution after records and/or the site have already been published.

## Procedure

1. Search both repositories for the old spelling, case-insensitively where appropriate. Include source metadata, entry prose, homepage/About copy, generated JSON, templates, and documentation that may be public-facing.
2. Identify the canonical identity value and update source-of-truth metadata first. Do not hand-edit generated payloads as the primary fix.
3. Update every user-visible static surface. Keep the full canonical identity on a detailed provenance/About surface.
4. If mobile layout requires a shorter credit, use a deliberate display-only form on the homepage; do not overwrite the canonical source identity with the compact presentation.
5. Re-export the site payload from the source repository.
6. Run source tests, `git diff --check`, HTML/inline-JavaScript sanity checks, and a second stale-spelling search across both repositories.
7. Selectively stage source and generated/site changes. If the user supplies an exact commit message, use it verbatim for each repository commit.
8. Push source and site repositories, verify local HEAD equals each remote branch, wait for the Pages workflow to complete successfully, and fetch live HTML plus the generated payload with a cache-busting query.

## Verification invariants

- The stale identity has zero remaining occurrences in source and site repositories.
- The canonical identity appears in the fuller public provenance surface and source metadata.
- The compact homepage credit is visibly intentional and does not claim to be the canonical stored identity.
- Generated counts/statuses remain unchanged unless the identity correction itself changes records.
- Live HTML and live JSON reflect the correction after deployment; HTTP 200 alone is insufficient because Pages/CDN caching can serve an earlier revision.

## Common pitfall

A generated directory payload may intentionally omit internal metadata such as `meta.steward`. Verify canonical identity changes in the source metadata and the public surfaces that actually consume the exported fields; do not invent a payload assertion for a field the exporter does not publish.
