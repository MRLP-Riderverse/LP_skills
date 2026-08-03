---
name: directory-draft-intake
description: Hyper-low-friction workflow for staging Acadie.sol directory inbox entries from live conversation or public research. Inbox layer is Name + Notes first; cleanup and normalization happen later.
version: 1.2.0
category: community
metadata:
  hermes:
    tags: [directory, intake, inbox, drafting, community, capture, scraping, raw-capture, low-friction]
    related_skills: [hermes-agent, software-development-workflow]
---

# Directory Draft Intake

Use this skill when the user wants to add, draft, or stage an entry for the `acadie_sol_directory` inbox.

This is the **hyper-low-friction inbox layer**.
At this stage, the draft should feel closer to **Name + Notes** than to a form.

## Trigger phrases

Treat the following as intake commands, not open-ended discussion:

- "add this to the acadie directory inbox"
- "add this to the acadian directory inbox"
- "draft this as a manual entry"
- "capture this in person"
- "put this in the inbox"
- any live owner / on-foot intel the user wants preserved as a directory draft

## Intent

The goal is to preserve raw local intelligence with minimal friction and minimal meaning loss.

Core goals:
- capture the entry even when the information is incomplete
- preserve the user’s live wording when it carries local meaning
- avoid making the intake feel like a form
- prevent over-sorting too early
- keep the inbox easy to read later during cleanup
- move structure and parsing pressure to the later normalization pass

## Default attribution rules

Use these defaults unless the user explicitly overrides them:

- **Submitted by:** `Acadie.sol`
- If the user explicitly says they are there, witnessed it, or captured it live, preserve that in notes or admin notes.
- Do **not** force `Source: In person` when the user did not actually say it.
- Public URLs are welcome when present, but never required for inbox capture.

## Inbox principle

**The inbox is not the final schema.**

It is a staging layer.
The point is to preserve raw intelligence in a way that is easy to create now and easy to revisit later.

At this stage, the assistant should optimize for:
- fidelity
- speed
- recoverability
- readability during cleanup

## Minimum viable intake shape

Only one field is truly mandatory:

- **Name**

Everything else can be captured as:

- **Notes**
- If the user provides a city / area / neighborhood, keep it visibly in the draft header or early notes so it is not easy to miss in the echoed confirmation.

That means the entry can succeed even if the user gives:
- rough location
- address
- public details
- features
- vibe
- hours caveat
- verification hints
- source context
- owner observations
- mixed notes

All of that can stay in notes at draft stage.

## Preferred inbox draft shape

Use this shape by default for live intake.
Treat `inbox/_template.md` as the canonical reference, with the matching copy in `references/draft-template.md` for the skill backup.

When a raw intake already includes structured facts (address, phone, hours, source, related places), keep the capture readable and preserve those facts in the template blocks instead of inventing a separate formatting step.

```md
# Draft: <Name>

Category: <coarse type, if obvious>
Area: <public browse area, if known>
Tags: <optional search hints separated by |>

## Description
<one short public-facing line, if obvious>

## Notes
<raw local wording, useful context, vibe, caveats, landmarks, and uncertain details>

## Public data to carry forward
- Address: <if known>
- Hours: <if known>
- Phone: <if known>
- Email: <if known>
- Website: <if known>

## Related places
- <nearby venue / sibling branch / corridor anchor, if applicable>

## Public source
- <public link, In person, or leave empty>

## Admin notes
- Submitted by : Acadie.sol
- Follow-up: <only if there is a real verification or cleanup task>
```

Do not pad drafts with process placeholders. `## Public source` and `## Details and sources` still work as backward-compatible aliases in older drafts/exporters, but `## Public data to carry forward` is the preferred section when the draft needs address/hours/phone/email to appear in the public card preview. `## Related places` is optional in draft/proper source data, but should not automatically be rendered on the main quick-card UI; reserve relation clusters for full pages or intentional discovery features.

If the entry has no separate contact block, keep the body lean, but still prefer short paragraphs over one long blob.

If there are no true admin notes beyond attribution, keep only:

```md
## Admin notes
- Submitted by : Acadie.sol
```

## Field behavior

### Name
- Required if the user is asking to draft a place.
- Preserve the best available business/place name.
- If the user later corrects the name, patch the title directly.

### Notes
This is the main inbox capture bucket.

Use it for:
- what the place is
- location / address / wayfinding
- public-facing features
- useful local recommendations
- hours caveats
- vibe / felt impression
- witnessed details
- mixed public/admin-ish fragments when early sorting would cause loss

Examples of details that can stay in notes:
- `local foods restaurant at 1395 Miramichi Ave`
- `amazing Donair and Steak Subs`
- `great Poutine`
- `daily open hours are short`
- `worth trying if you can catch them during open hours`
- `nice`
- `near Daly Point`
- `up Bridge St`

At inbox stage, preserving the phrasing is usually better than prematurely converting it into categories.
Light punctuation or capitalization cleanup is fine if it improves readability, but do not rewrite in a way that changes tone, confidence, or meaning.

### Admin notes
Use for:
- attribution
- explicit verification reminders
- clearly internal follow-up
- known uncertainty the user would want remembered during cleanup

Always keep:
- `Submitted by : Acadie.sol`

Keep admin notes short.
Do not dump half the capture into admin notes just because it is imperfect.

## Multi-location handling

When the user gives a batch of businesses, a chain with multiple local branches, or a shared-venue brand with more than one physical site:

- write one draft per physical location
- disambiguate the title with the street address, neighborhood, or branch name when needed
- do not collapse distinct branches into one card just because the brand is shared
- if there are two known locations and the user mentions both, stage both drafts immediately
- preserve any unresolved location ambiguity in `## Notes` instead of forcing a guess
- when a venue has a mall branch and a marina / waterfront branch, treat them as separate entries even if the public brand name is almost the same
- keep the official branch label in `## Notes` if it helps future search or cleanup

This is especially useful for restaurant chains, campuses, libraries, and waterfront clusters where multiple branches or sub-locations are part of the same conversation.

## Reliability rules

- Never fail the draft because phone, hours, email, address, category, or source label are missing.
- Never force a URL.
- Never force an address into a dedicated field at inbox stage.
- Never force wayfinding into its own field at inbox stage.
- Never pad the draft with placeholders like `not provided`.
- Never over-summarize if that would lose the raw felt meaning of the user’s note.
- If a detail is uncertain but useful, preserve it in notes or brief admin notes instead of dropping it.
- Prefer readability over pseudo-structure.
- Before writing a new draft, check `inbox/` for an existing same-name or obvious twin entry.
- When the name is common or the place is in a dense corridor (mall, plaza, shared street), search for nearby landmark / address / brand variants too — not just exact-name matches.
- If a likely duplicate already exists, do **not** silently overwrite or create a second draft.
- In that case, report back exactly in this shape: `I believe you already have an entry for this: <path>` and wait for the user to decide what to do next.

## Manual capture workflow

1. Read the user’s instruction as an intake command.
2. Extract the name.
3. Check `inbox/` for an existing same-name or obvious twin entry before writing.
4. If a likely duplicate exists, stop and report: `I believe you already have an entry for this: <path>`.
5. If no likely duplicate exists, put everything else into `## Notes` with minimal cleanup.
6. Preserve meaningful wording, including rough location, praise, caveats, and local feel.
7. Add `Submitted by : Acadie.sol` in admin notes unless told otherwise.
8. Only add extra admin notes when there is a real follow-up or verification point worth carrying.
9. Write the draft into `inbox/` without waiting for more fields.

### Batch release workflow

Use this when the user follows draft capture with commands like `commit`, `push`, or `export to site`.

1. Commit the new inbox drafts in `acadie_sol_directory`.
2. Push `acadie_sol_directory` to `origin/main`.
3. Run `scripts/export_to_site.py --all --site ~/ExoCortex/websites/projects/acadie_sol` from `acadie_sol_directory`. The `--all` mode is important: it refreshes the full public payload chain, and inbox drafts should appear in `assets/directory-data.json` as `Draft: <Name>` records rather than being silently treated as clean entries.
4. Verify the generated payload before touching the site repo: confirm the expected `entry_count`, `draft_count`, exact draft titles/slugs, descriptions, categories, area, and public-data/source fields. Do not hand-edit generated JSON.
5. Commit the updated `acadie.sol/assets/directory-data.json` plus any intentionally requested site changes (for example homepage metadata) in `acadie.sol`.
6. Push `acadie.sol` to `origin/main`.
7. Verify both local `HEAD` values equal their remote `origin/main` values. If Pages deployment is triggered, wait for the workflow tied to the pushed site SHA to complete successfully, then fetch the live homepage and `assets/directory-data.json` with a cache-busting query and confirm HTTP 200 plus the exact metadata/draft markers.

Do not stop after the draft exists if the user asked for release actions too.

### Commit/push-only requests

If the user says only `commit`, `push`, or `commit n push` immediately after drafting an inbox entry, default to committing and pushing **only the directory source repo** (`acadie_sol_directory`).

Do **not** auto-export to the site repo unless the user explicitly asks for `export to site`, `publish`, `sync`, or otherwise indicates they want the public payload regenerated.

This preserves the intended two-stage flow:
- inbox/source-truth capture can be saved immediately
- public site export remains an explicit publication step

## Batch cleanup / spruce-up passes

When the user asks to "spruce up" a large draft set, prefer alphabetic slices instead of trying to normalize everything in one go:
- work in chunks like `A-C`, `D-H`, `I-O`, `P-Z`
- normalize `Category`, `Area`, and `Tags` first
- then split raw notes into short readable blocks
- add `Related places` when a listing clearly belongs to a corridor, plaza, shared site, or venue cluster.
- Keep `Related places` in its own section so it survives export cleanly and can power compare/adjacency later.

## Template reference
- Use `inbox/_template.md` as the canonical draft-shaping reference.
- It is intentionally ignored by export so it can live beside raw intake without becoming a listing.
- Raw intake can stay messy; the template is the post-intake restructuring target.
- Keep the intake result close to the template during the first capture so a separate formatting tool is usually unnecessary.
- Preserve the user’s raw wording when it carries local meaning.
- Keep uncertain facts in notes or brief admin notes instead of forcing a guess.
- Keep clear public contact facts in structured fields so the public renderer can turn them into tap-to-call / map actions later.
- During a cleanup pass, promote confirmed phone/address values out of prose and into `## Public data to carry forward` so the exported site can link them directly.
- Keep the wording exact enough to round-trip cleanly; do not over-normalize contact data.
- New sessions can repeat this workflow reliably as long as they load this skill and the inbox template remains in place.

Good relation-mapping candidates:
- mall branch ↔ marina branch
- dine-in ↔ nearby entertainment venue
- campus ↔ other campus / satellite site
- hotel ↔ airport / event / corridor businesses
- waterfront / promenade / main-street clusters

When doing a cleanup slice, work in chunks like `A-C`, `D-H`, `I-O`, `P-Z`, then sanity-check the slice before moving on.
Normalize Description/Notes/Public data/Related places first, then export once the full requested batch is done.
For large inbox-wide formatting passes, the safe release rhythm is: normalize drafts → verify section shape/template compliance → export to site → commit/push `acadie_sol_directory` → commit/push `acadie_sol`.

## Public research shortcuts

When the user asks for a batch of places and the web data is fragmented:
- prefer official municipal/service pages or official brand/location pages first
- use result titles/snippets from search as backup for branch names, addresses, and hours
- keep one draft per physical location
- if a chain has multiple branches in the same region, disambiguate the title with the street address or branch label
- keep partial uncertainty in `## Notes` rather than blocking the draft
- when a claim is useful but not explicitly confirmed by the source (for example: fire tolerance, access rules, seasonal operations), keep it out of public claims and mark it as unverified in `## Admin notes`
- capture operational details from authoritative city pages when present (hours, parking, lifeguards, designated zones, access notes, pets, camping, rentals, cleanup schedules)

## Later normalization

A later pass can parse the notes into cleaner structure such as:
- category
- area
- address
- wayfinding
- hours
- public notes
- public source
- admin follow-up
- relationship notes (`related_places`, `nearby_places`, `shared_events`)

That parsing is intentionally postponed.

## Pre-publish review pass

Before committing or pushing a batch that promotes drafts alongside existing official entries, pause for a content review rather than treating routed drafts as publish-ready. Inspect the generated payload in memory or with the exporter’s stdout mode and report the current published/draft counts. Review each description as a card-level one-liner: keep it readable, concrete, and within the schema’s `short_description` limit (currently 160 characters where that schema applies). For identity cards, community projects, and creator/steward records, prefer one compact sentence or short prose paragraph over a bullet-list description; reserve bullets for genuinely scannable public notes. The exporter may collapse Markdown whitespace, so apparent paragraph breaks are not a reliable card-layout control; improve dense copy by rewriting the sentence, not by adding line breaks.

The source `entry.md` is canonical prose, but the current static Acadie renderer primarily consumes the generated JSON payload and does not automatically render arbitrary Markdown links or every source section. Treat source-level Markdown as preservation, not proof of a clickable public link. During promotion verification, inspect the generated item fields and the actual entry-page renderer: confirm that any link the user expects to click is represented in a renderer-supported structured field (currently contact `website`, `address`, `phone`, or `email`, each with its own label/action behavior), or explicitly record it as a follow-up renderer enhancement. Do not claim a source Markdown link is live-clickable without checking the deployed page.

Normalize schema-facing fields before promotion:
- choose one allowed canonical category; do not publish slash-combined values such as `venue / collective`
- standardize area/location punctuation across the batch
- keep uncertain addresses, roving locations, and unresolved relationship hints cautious and visibly labeled rather than presenting guesses as facts
- keep event recency notes separate from the durable description
- preserve rich scene language in tags or full notes when it does not belong in the card one-liner

Do not push while the entries are still only drafts unless the user explicitly wants draft previews released. The review should end with proposed copy and concrete field changes, then wait for approval before editing/promotion when the user asked to review first. Use `references/pre-publish-review.md` for the repeatable checklist and the Manila EDM router-root correction documented in the 2026-07 review.

## Official promotion workflow

When the user asks to promote a draft into a proper entry, switch from intake mode to promotion mode:

- keep capture permissive, but make promotion canonical
- judge missing information separately for MVP card readiness vs future full-page richness
- use `entries/<slug>/entry.md` for human-readable public prose; it is a live public source, not just a dev note
- use `entries/<slug>/meta.json` for machine-readable public-card fields and stable IDs
- treat the entry folder slug as the canonical entry identifier; do **not** casually rename it during cleanup
- treat `location_id` as a foreign key into `locations/*`; do **not** rename it just to match wording or display copy
- remove the inbox draft only when the official entry replaces the same record, so the public payload does not double-count both versions
- after promotion, verify the exported payload contains the new `slug` values (legacy item scans may use `slug`, not `id`)
- when the user supplies a thumbnail/photo for a proper entry, wire it through the source-of-truth path: add a `thumbnail` object in `meta.json`, store the image under the site repo at `assets/entries/<slug>/thumbnail.<ext>`, run the exporter, and verify the generated payload carries `thumbnail_src` and `thumbnail_alt` instead of hand-editing exported JSON
- preserve local neighborhood language when it helps wayfinding. If the user gives a local area cue such as `St Anne`, `near the airport`, `up Bridge St`, or similar, keep the public browse area broad (`Acadie-Bathurst` when appropriate) while carrying the finer-grain cue in `location.geocircle` and/or the public notes so the local meaning survives promotion
- for bulk inbox promotion, promote by moving drafts out of `inbox/`, add `summary.fr` plus an `## Résumé français` source section, normalize inbox-only categories to schema-safe categories, and verify `draft_count: 0`, no duplicate slugs, no `Draft:` titles, and no missing `description_localized.fr` before site export
- run tests/export verification before committing
- for the two-repo GitHub Pages flow, commit/push the directory repo first, then commit/push the generated site payload and verify the live Pages payload
- see `references/bulk-promotion-validation.md` for the deterministic bulk-promotion checklist and validation script

See `references/official-promotion-workflow.md`, `references/promotion-slug-location-id-notes.md`, `references/pre-publish-review.md`, `references/manila-promotion-release-pattern.md`, `references/manila-pages-public-root.md`, `templates/official-entry.md`, and `templates/official-meta.json`.

### Derivative-node promotion release pattern

For a derivative node with a separate source repository and GitHub Pages site repository, treat promotion as one release unit:

1. Inspect each inbox draft and decide the canonical public category before moving it. Normalize draft-only or slash-combined categories to an allowed schema value; do not export values such as `venue / collective` or `collective` when the schema does not allow them.
2. Create `entries/<slug>/entry.md` and `meta.json` from the draft. Keep the public card description in `meta.json.short_description` and keep it within the schema limit (currently 160 characters); preserve richer scene/context prose in `entry.md` notes.
3. Put relationships in one canonical place. If `meta.json.related` is populated, do not also add a `## Related places` section to `entry.md`, because the exporter concatenates both and produces duplicate relationship values.
4. Remove the replaced `inbox/<slug>.md` draft only after the canonical entry exists. This prevents duplicate preview + published records.
5. Run the exporter with `--stdout` first, then run the site export. Assert `draft_count: 0`, the expected `published_count`, unique slugs, all statuses `published`, and card descriptions within the schema limit. Run the source tests and `git diff --check` before staging.
6. Commit and push the source repository first. Then selectively stage the generated site payload, commit, and push the site repository. Verify both local HEADs equal their remote branch SHAs.
7. Wait for the Pages deployment and fetch the deployed `assets/directory-data.json` with a cache-busting query. A successful push is not sufficient proof; confirm the live payload contains the promoted slugs and the expected published/draft counts, and check the key HTML routes return HTTP 200.

The repeatable commands and validation shape are captured in `references/manila-promotion-release-pattern.md`.

When the user gives UX feedback on a promoted/proper entry, treat it as schema and renderer calibration, not just copyediting. For the main quick-search page:

- separate proper entries and draft previews into distinct collapsible sections
- keep proper entries first; drafts can be collapsed by default with a clear `View drafts` jump button
- keep Search as a lightweight quick tool instead of a large stacked panel; a single floating bottom-right FAB is acceptable when it keeps first impression minimal
- prefer a normal top navigation banner for global options; it may auto-hide on scroll down and reappear on slight scroll up, following common mobile UX. Avoid floating menu FABs for primary navigation when they feel gimmicky or get in the way
- use the floating FAB only for a simple return-to-top action when needed; keep it visually quiet, blue, and bordered
- first-run directory UX can use an interactive splash/landing choice, not a merged control block: Discover = show all official entries for open-ended browsing; Search = open a clean static search/filter panel feeding the same results. Hide the directory mechanics until the user chooses a path
- Fresh drafts/Recents should be a dedicated page when the list needs room; avoid popup-within-popup UI for draft intake browsing, and do not duplicate the draft container on the main directory page once the dedicated page exists
- keep Search available from the top nav and provide an explicit Search/Enter behavior so mobile users can close the keyboard and jump to results while live filtering remains active; once Search is selected, keep the search box static in the body so users can refine later
- keep advanced filters behind a Filter action instead of always showing multiple dropdowns
- do not auto-hide the search UI on scroll/focus events; mobile browser focus/zoom can trigger tiny scroll events and accidentally close the search panel
- group official/proper entries by city-level containers when browsing, while search still scans all entries
- keep city-level containers collapsed by default and visually light; avoid nested card-within-card wrappers that shrink the result cards
- avoid showing city/public-area as a collapsed-card pill when address appears on expansion
- do not render duplicate tag rows; tags are quick-scan metadata, not expanded-card content
- do not display official-entry website URLs on main cards; reserve links for full profiles unless the record is still a draft preview
- prefer intentional bullet lists for expanded focus points when public notes are bullet-like
- keep photos, accreditations, source trails, reviews, and related-place clusters for future full pages unless explicitly requested on cards
- keep related-place/source data in the directory payload if useful, but do not automatically render it on the main quick card

See `references/public-directory-quick-card-ux.md`.

When a useful corridor or cluster shows up, leave a lightweight reminder in the clean-entry area so future work can find it quickly (for example a small graph notes page or equivalent relation note), instead of burying the idea only in inbox drafts.

## Spruce-up passes on existing drafts

When the user asks to "spruce up" a batch of drafts, treat it as a light normalization pass rather than a schema rewrite.

Default moves:
- add `Category` and `Tags` when the type is obvious from the notes
- split one-line raw notes into short readable lines
- keep the original local meaning and confidence level intact
- promote obvious public facts into a small `Public data to carry forward` block when helpful
- add `Related places` for natural corridors, paired branches, or neighborhood adjacency
- keep leading-number names intact (`13 Barrels Brewing` is a normal title, not a special-case exception)
- avoid inventing facts just to complete a field
- during a broad formatting pass, normalize section order first and treat missing sections as acceptable placeholders rather than forcing new semantics into them
- only promote prose into structured `Address` / `Hours` / `Phone` / `Email` lines when the value is explicit and unambiguous; do **not** guess field labels from a sentence that merely contains an address or operating detail
- if a sentence mixes place description with an address (for example `restaurant at 2050 St. Peter Avenue`), keep the sentence in `Description` or `Notes` unless you can cleanly separate the raw address without changing meaning

See `references/batch-cleanup-and-relation-mapping.md` for the batch rhythm and relation-hint patterns that emerged from the A-Z polish pass.
See `references/export-parser-quirks.md` for the parser-safe section names and heading pitfall to avoid during cleanup.

Good relation-mapping candidates:
- mall branch ↔ marina branch
- dine-in ↔ nearby entertainment venue
- campus ↔ other campus / satellite site
- hotel ↔ airport / event / corridor businesses
- waterfront / promenade / main-street clusters

The goal is to make drafts easier to search, compare, and cluster later without forcing them into the final page shape too early.

## Why this shape is preferred

This format is better for live work because:
- it lowers expectations during capture
- it preserves meaning instead of forcing early sorting
- it makes drafts faster to create in person or on the move
- it makes later cleanup easier because the whole raw thought is still visible in one place

## Loading tool / preflight wrapper

In Telegram, the session preflight command is `/draftload`.

Its role should be:
- act like an "I’m about to input some draft entries" mode
- tell the agent that only **Name** is mandatory
- tell the agent that everything else can remain in **Notes**
- reduce live expectations
- avoid turning capture into a mini-form

The loader is a readiness layer, not the real intake requirement.

## Session lessons captured

- `Frost Bite` proved that local visitor-helpful notes matter.
- `Theriault’s Grocers` proved that rough wayfinding and observed description can be enough for a valuable draft.
- `Bowlarama Bathurst Bowling & Arcade` showed that features + vibe survive better when not over-sorted.
- `Eastside Deli` showed that address + praise + hours caveat are easier to preserve as notes than as forced mini-fields.
- The inbox stage should optimize for preservation first, parsing second.

## Success criteria

A good result is:
- the user can draft an entry quickly during live work
- only the name is required
- the notes preserve the raw local meaning
- the draft is easy to read later during cleanup
- missing structure does not block capture
- later normalization still has enough material to work from

## Capture confirmation

When the user asks to confirm a newly captured draft, keep the reply short but include the normalized title plus any explicit top-level location field that was captured. Do not omit a location field from the confirmation if it is present in the draft.

See `references/capture-confirmation-note.md` for the session-specific reminder.

## Linked support files

- `references/draft-template.md` — canonical Name + Notes inbox draft skeleton
- `references/session-notes.md` — compact lessons and pitfalls from batch intake, chain branches, and waterfront cluster handling
- `references/batch-location-research-notes.md` — workflow notes for batch franchise/location research and branch disambiguation
- `references/duplicate-guard-and-script.md` — duplicate-warning rule, exact fallback wording, and deterministic helper usage
- `references/public-source-verification.md` — source-order and verification notes for enriching drafts from official city/service pages
- `references/recent-capture-patterns.md` — compact examples of one-line live capture bundles and landmark phrasing
- `references/public-venue-location-research.md` — branch-disambiguation notes for mall / marina / waterfront venue research
- `references/site-sync-workflow.md` — commit / push / export / publish sequence for the two-repo setup
- `references/cleanup-pass.md` — session-derived light normalization and relation-mapping cues for inbox polish passes
- `references/formatting-pass-guardrails.md` — safe order of operations and anti-overinference rules for broad A–Z formatting passes
- `references/batch-cleanup-and-relation-mapping.md` — alphabetic cleanup passes, relation hints, and batch export rhythm for inbox polish passes
- `references/export-parser-quirks.md` — exporter-recognized headings, related-places handling, and a common heading pitfall
- `references/contact-action-links.md` — how structured phone/address/email fields become tap targets in the public renderer
- `references/official-promotion-workflow.md` — draft-to-official-entry promotion threshold, verification, and two-repo publish sequence
- `references/manila-intake-routing.md` — explicit-root inbox routing, creator identity normalization, and two-repository release sequence
- `references/bulk-promotion-validation.md` — deterministic checklist for promoting many inbox drafts at once, including French summaries, category normalization, duplicate-slug checks, and export validation
- `references/public-directory-quick-card-ux.md` — main directory quick-card UX rules: separate drafts, avoid duplicate tags/location/relations, keep rich material for full pages
- `templates/official-entry.md` — starter `entry.md` for proper entries
- `templates/official-meta.json` — starter `meta.json` for proper entries
- `scripts/draft_intake.py` — deterministic renderer for later structured normalization or conversion
