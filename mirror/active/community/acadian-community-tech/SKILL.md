---
name: acadian-community-tech
description: Complete Acadian community technology workflow — tech stewardship, cultural research, hive mind activation, and website building for Acadian and similar distinct cultural/linguistic communities.
category: community
aliases: [acadian-tech-stewardship, acadian-hive-mind-research, acadian-website-builder]
---

# Acadian Community Technology Umbrella

This is the **class-level skill** for all Acadian and similar cultural community technology work. It consolidates tech stewardship, cultural research, hive mind activation, and website building workflows.

**Trigger:** User wants to monitor/build technology solutions for Acadian region (Péninsule acadienne, NB), research Acadian/Doucet lineage, activate community-driven "Hive Mind" for cultural preservation, or build culturally-focused community websites.

---

## Subsections

### A. Tech Stewardship Framework (from `acadian-tech-stewardship`)
Monitor, support, and build technology solutions for the Acadian region and similar distinct cultural/linguistic communities. Focus on resilience, connectivity, and cultural archiving.

**Core Philosophy:**
- **Identity:** Distinguish "Acadian Resilience/Survival" from generic "French Pride." Focus on pre-colonial/Grand Dérangement history (navigation, expulsion, return).
- **Symbolism:** Use **Lion + Star** (Stella Maris) motifs for ownership and navigation, rather than just the modern tricolor flag.
- **Approach:** "Redact-Then-Rich" for data; "Lore Hunting" for tourism; "Mesh Connectivity" for infrastructure gaps.

**Reusable Workflows:**
1. **Weekly Regional Briefing ("Mardi en Acadie" Pattern)** — See `regional-news-monitoring` skill for the full operational workflow (RSS fetching, WordPress site-search fallback, cron-safe archive append, Telegram notification). Cron job for Tuesday ~7:50 AM Atlantic, search terms: "Acadie", "Acadien", "Péninsule acadienne", sources: Radio-Canada Acadie, Acadie Nouvelle, L'Étoile
2. **Connectivity Solutions (Meshtastic Pilot)** - LoRaWAN mesh nodes for rural/coastal NB emergency comms, tourism trails, fishery data logging
3. **Fishery Traceability (Blockchain)** - QR/NFC ledger tracking catch-to-market for lobster/crab
4. **Tourism Tech ("Lore Hunting")** - NFC/QR markers at historical sites triggering voice notes, gamified with "Star Points" digital passport
5. **Cultural Archiving (PKM Integration)** - Structure: `~/acadian-lore/highlights.txt` for weekly logs, GBrain for full-text search

**Pitfalls:**
- **Identity Confusion:** Do not conflate Acadian with Quebecois or generic French. Acadian = Survival/Resilience; Quebecois = Political/French-centric.
- **Emoji Signal:** Avoid 🇦🇨 (Ascension Island). Use 🇫🇷⭐ or text "Acadia". Better yet: design custom Lion+Star totem.
- **Language:** Always search/monitor in **both** French and English. The community is bilingual, but primary sources are often French-only.

**See original:** Full stewardship workflows preserved from `acadian-tech-stewardship` skill.

---

### B. Hive Mind Research & Activation (from `acadian-hive-mind-research`)
Research Acadian/Doucet lineage, synthesize local data with online sources, verify historical claims, and activate community-driven "Hive Mind" for cultural preservation.

**Context:** User (MR LP) is building a decentralized platform for Acadian historical truth recovery. Core tension: Balancing family lore (Tarbes, Bishop Geraldus, "Armorican-Belgae") with academic consensus (Western France origins, unknown specifics).

**Approach: The "Two Eagles" Method** - parallel verification (archival vs. narrative) and narrative synthesis to turn genealogical gaps into meaningful mystery.

**Step-by-Step Workflow:**
1. **Capture the Concept (QuickThoughts)** - Use `note` CLI command to log insights with timestamp and context labels
2. **Synthesize Local Data (Opencode Delegation)** - Spawn subagent to find, read, and synthesize ALL local Acadian-related files in `~/Documents/Notes`
3. **Cross-Reference with Online Research** - Query: "Acadian origins [region]", "[Surname] [location] [century]", focus on Stephen A. White, diocesan records, etymology, heraldry
4. **Verify Specific Claims (Browser/Perplexity Pipeline)** - Extract dates, locations, titles from Catholic-Hierarchy.org, Gallia Christiana, Archives Départementales des Landes
5. **Generate Symbolic Artifacts (Optional)** - Use DALL-E 3 for totems (Lion, Eagle, Star) in ancient Celtic + modern 3D style
6. **Ingest into GBrain (Semantic Indexing)** - Import synthesis report with `gbrain import`
7. **Create Project Plan (Todo List)** - Phase: Data Foundation → Platform Architecture → Prototype → Community
8. **Draft the "Call for Stories" (Narrative Synthesis)** - Create manifesto: "The [Symbol] & The [Silence/Mystery]: Searching for [Lineage] in [Ancient Region]"

**Key Insights:**
- **Parallel Tracks:** Run archival verification AND narrative synthesis simultaneously
- **"Two Eagles" Framing:** Past (lore) and Future (synthesis) are both valid; tension is the truth
- **Subagent Delegation:** Use for multi-file synthesis and web research (saves 10+ tool calls)
- **Symbolic Anchors:** Totems, heraldry, etymology provide emotional resonance that raw dates don't

**Critical Distinctions:**
| Claim Type | Example | Treatment |
|------------|---------|-----------|
| **Verified** | Germain Doucet b.1595 | Anchor point, cite sources |
| **Lore** | Tarbes connection, Bishop scandal | Plausible, regionally accurate, needs archival proof |
| **Synthesis** | "Armorican-Belgae identity" | Valid cultural narrative, not historical continuity |
| **Pattern** | "Doux" = gentle strategy | Thematic truth, reveals family strategy across centuries |

**See original:** Full research workflow preserved from `acadian-hive-mind-research` skill.

---

### C. Website Builder (from `acadian-website-builder`)
Build culturally-focused Acadian community websites with iterative design improvements and Opencode delegation support.

**UI theming / readability pass:** when the user asks for a palette shift or dark-mode polish, do a full contrast sweep over full-detail/contact pages, tags/chips/pills, related links, and hover states. Prefer shared tokens over per-element hardcodes; see `references/dark-mode-ui-theming.md`.

### D. Directory Protocol Architecture
The Acadie.sol Directory Protocol — a decentralized, git-based community directory with RSS signaling and fork/merge contribution patterns.

**Site sync rule:** the website repo is a static mirror of an exported payload, not a live reader of the directory filesystem. See `references/directory-site-sync.md` and `references/directory-export-workflow.md` for the manual export flow and safe preview notes.

**Manual trigger phrase:** treat **"export to site"** as the operator cue to regenerate the website payload from the directory repo, then commit/push the site repo when you want the public snapshot to change.

**Promotion pitfall:** promoted entries still living in `inbox/` will export as draft duplicates. When a draft becomes official, move or remove the inbox draft before/after export so the public payload does not show both versions. See `references/directory-promotion-and-sol-site.md`.

**Batch sync sequence:** when the user asks for the full publish path, follow the repeatable order in `references/directory-batch-sync.md`: commit directory repo → push directory repo → run exporter → commit site payload → push site repo → verify the live asset.

**Commit combo / mobile preview sequence:** if the user says “commit combo” or asks to view the current site on mobile, treat it as the complete publish-and-verify path: export payloads, commit/push changed repo(s), wait for GitHub Pages `built`, verify live HTTP 200s, then run a deployed mobile browser render check. See `references/public-mobile-site-preview-workflow.md`.

**Connected site preview bridge (V1):**
- When the public site needs to show the directory before everything is normalized, render a separate `directory.html` page in the site repo.
- Feed that page from a generated JSON export of `acadie_sol_directory/inbox/*.md` rather than hand-copying listings.
- Mark entries whose source file is still a draft with a visible `DRAFT` badge in the UI so the preview stays honest.
- Point the main nav button to the dedicated directory page instead of an in-page anchor when the goal is a browsable directory view.
- Keep the first version plain and functional; polish can come after the data bridge works.
- See `references/directory-site-bridge-v1.md` for the minimal repeatable pattern.
- See `references/directory-mobile-public-ux.md` for the mobile-first public UX correction: moods/filters as dropdowns, one primary listing display, no duplicate A–Z section.
- See `references/public-mobile-site-preview-workflow.md` for the public mobile site pass: warm local landing, unified Find local places intent, event bulletin cards, no duplicated related-place UI, proportion-tightening after mobile screenshot feedback, screenshot contact-sheet workaround, and deployed mobile verification.
- See `references/batch-cleanup-and-relation-mapping.md` for the alphabetic cleanup slices and relation-hint pass used during inbox reformatting.

**Directory display preference (user-specific):**
- Design **mobile-first and calm by default**. If the page feels “big” or attention-heavy on mobile, reduce hero/card size, spacing, and visible filter surfaces before adding more features.
- Default to **Show all** as the primary browse state. The full list should be visible without extra friction; keep Clear as the reset action.
- Keep **A–Z** and **Category** out of the primary action row when the dropdowns already cover that filtering. Avoid duplicate controls that repeat the same affordance.
- Prefer a **single public browse/card list with sorting and filters** over large parallel sections. A–Z can be a sort option, not a separate repeated directory.
- Put “mood”/route ideas (Hungry, Waterfront, Family, Night out) behind a **Mood / route dropdown** or similarly compact selector on mobile; large mood cards are useful conceptually but too attention-heavy as persistent top-level blocks.
- Put categories, quick filters, and area selectors behind **dropdown controls** when the category set gets large. Avoid long chip rows on mobile; they overwhelm the page.
- Normalize city display to the public city level only; Bathurst-area variants should collapse to **Acadie-Bathurst** in browsing and dropdowns.
- Keep **full-page contact cards** as an optional detail route later, not the main launch surface.
- Preserve the export payload and data shape when changing display style; UI refactors should not break the directory source-of-truth workflow.
- Keep the page calm by default, but if the user explicitly prefers a full-browse first impression, make **Show all** the default state and keep **Clear** as the reset action.
- Avoid redundant controls: if dropdowns already provide the needed city/category filtering, do not keep separate A–Z or category sort buttons just to mirror the same function.

**Renderer guardrail:** if the user asks to make the site less overwhelming, favor presentation changes in `directory.html` over changes to `assets/directory-data.json` or the directory repo schema.

**Session note:** see `references/directory-view-controls.md` for the current resolved directory control pattern (Show all default, Clear retained, no duplicate sort buttons).

**Two-repo split (non-negotiable):**
- **Data repo** (`acadie-sol-directory`): entries, schemas, RSS feed. Git IS the API. No database.
- **Site repo** (`acadie-sol`): rendering layer only. Pulls from data repo on build.
- Data survives site rebuilds. Site is disposable; data is sacred.

**Protocol stack (corrected June 2026):**
- **Layer 0 — Identity**: `did:web` (primary, no chain needed). NOT Solana — no W3C DID method exists for it. Optional on-chain anchor later.
- **Layer 1 — Intent**: ActivityStreams 2.0 vocabulary (Offer, Request, Join, Invite) published as RSS/Atom items.
- **Layer 2 — Propagation**: proximity-based routing by cultural + geographic proximity (novel — no existing protocol does this).

**RSS architecture:**
- `feed.xml` at repo root = main aggregated feed (all signals)
- `feeds/<name>.xml` = per-profile feeds for Tier 2 hosting (people without their own server)
- Active feed keeps ~50 most recent `<item>` blocks; older items move to `archive/YYYY-MM.xml`
- Archives are still in git, still accessible, just not in the active subscription feed
- Entries are appended to feed.xml; the file grows but gets curated/archived over time
- The `note` CLI command cannot handle complex content with parentheses — use simple quoted strings only

**Fork & merge pattern (how communities contribute):**
1. Community forks `acadie-sol-directory`
2. Adds their entries in their own region subdirectory
3. Discovers cross-community entry → submits PR to main directory
4. Steward reviews → merges → credit lives in git history forever
5. Main directory grows because local directories feed it
6. Each local directory stays independently functional

**Channel architecture (5 channels, each with purpose):**
- **RSS**: the record, the pipe, permanent archive, machines read it
- **Telegram**: the pulse, announcements only, 1-2/week, like a notification app
- **Discord**: the conversation, kitchen table, messy alive, raw RSS feeds via bot, subthreads
- **Signal**: the action, logistics, DND bypass, invite-only small groups
- **Hero banner**: the boost, one thing, max reach, zero noise, rotates

**Tier 2 hosting (cork board pattern):**
- People who don't want their own GitHub/servers get a feed under `feeds/their-name.xml`
- URL: `acadie.sol/feeds/marie-boudreau.xml` — works in any RSS reader
- When they graduate to their own server, move the file and update the directory entry — zero migration pain
- You pin their card until they build their own wall

**Full details:** `references/directory-protocol-architecture.md`
**Relationship layer:** `references/directory-relationship-layer.md` — preserve adjacency, corridor, and event backlinks during inbox capture so clean entries can expose a social/location graph.

**Events + location V1:** `references/acadie-events-location-v1.md` — keep events/locations inside the directory data repo for V1, model events as first-class records linked by IDs to entries/locations/regions, use nested `en`/`fr`/`shiac` language fields for clean records, generate static `.ics` calendar files, and expose last-updated/snapshot counters without visitor tracking.
**Facebook event link parsing:** `references/facebook-event-link-parsing.md` — how to mine public FB meta tags, avoid guessing time, and remember that `--all` is the real event export path.

#### Events and locations architecture guardrails

- For V1, keep `events/`, `locations/`, `offers/`, `regions/`, and `archive/` inside `acadie_sol_directory`; do **not** split events into a separate repo until scale/stewardship boundaries demand it.
- Do **not** hand-maintain every adjacent-business pair. Model related businesses through `location_id`, reusable corridor/community `locations/`, `street_id`, explicit `nearby_location_ids`, and later coordinate/radius scripts.
- Do **not** embed event lists inside venue/contact entries. Events are independent time-based records that link to `host_entry_ids`, `performer_entry_ids`, `sponsor_entry_ids`, `location_id`, and `region_id`; venue pages render chronological event feeds by relationship lookup.
- Treat `entries = who/what exists`, `events = what happens in time`, `locations = where physically`, `regions = cultural/geographic grouping`, `offers = temporary opportunity`, and `archive = what it meant afterward`.
- Make `locations/` first-class even if minimal at first: multiple entries/events can share places, one entry can have multiple physical contexts, and future wayfinding/day-trip/archive/search logic needs stable location IDs.
- For clean/published records, prefer nested language objects such as `title: {en, fr, shiac}` and `description: {en, fr, shiac}`. The `shiac` tier is manually authored for local voice/memes; do not force it into raw inbox drafts.
- Mark example/non-real events as `placeholder` or keep them out of public rendering by default. If the user explicitly asks to test the public/mobile site with demo events visible, temporarily publish them while keeping IDs/titles clearly placeholder-like.
- Add-to-calendar should be implemented before heavy PWA work by generating static `.ics` files during export under `acadie_sol/assets/calendar/`.
- For proof-of-life, prefer export/build metadata (`last_updated`, `snapshot_refresh_count`, counts) over visitor tracking. A static site cannot maintain a true global refresh counter without a writable backend; avoid that for V1.

---

### D2. Acadian Web3 Gateway / SNS Stewardship
Use when shaping `acadie.sol` or a similar culturally sensitive namespace into a beginner-friendly public gateway.

**Positioning rule:**
- Frame the project as a **trusted local web3 gateway** and **community ownership/onboarding rail**.
- Treat Solana as the **rail**, not the loud public identity. Avoid leading with "crypto" or token language unless the audience is already native.
- The emotional first impression should feel like: **"wow, this was locally made?"** followed by seriousness, style, and belonging.

**Recommended product split:**
1. **Identifier product** — claim a community identifier/subdomain.
2. **Page/profile product** — optional profile/page setup later for builders, merchants, or organizations.
3. **Guided support product** — optional scheduled call / concierge onboarding for non-technical users.

**SNS / Sol.site architecture rule:**
- Main website can live at the root domain's Web2 bridge (e.g. `acadie.sol.site`).
- Prefer normal site routes like `/claim`, `/members`, `/faq`, `/about`, `/u/name` for pages and profiles.
- Treat `.sol.site` as a DNS bridge for the primary `.sol` identity and host, not as proof that every identifier/subdomain has a separate website. Verify the specific record target before assuming the bridge is live.
- Treat `.sol.site` as a branding / access layer, not proof that hosting is live. Verify the domain actually resolves to the chosen host before rebranding away from `.sol` or migrating off GitHub Pages.
- A good pattern is: one public gateway site + many on-chain identifiers + optional member pages hosted under the main site.

**Payments / compliance ladder:**
- V1 should optimize for trust and legibility, not payment novelty.
- Prefer a hybrid ladder:
  1. self-serve web3-native path,
  2. standard fiat checkout (e.g. Square),
  3. scheduled call / e-transfer / manual concierge fallback.
- Keep bookkeeping/receipt logic separate from identity onboarding. Do not let compliance complexity block the main identity rail.
- For early non-technical communities, a familiar payment provider often beats advanced crypto-native schemes.

**Community input / repo governance:**
- Start private if stewardship/admin logic is still forming.
- Open-source the public trust-building layer later if helpful, but keep sensitive ops/admin/anti-abuse logic private until mature.
- Community suggestions are best gated to actual members once the identity layer exists; public issue trackers can be added later for generic bugs/docs.

**Visual / cultural direction:**
- Aim for: local, stylish, future-facing, inclusive, and non-kitschy.
- Do not reduce Acadian identity to just France colors + star symbolism.
- Make room for historical alliances and neighboring peoples, including Indigenous ties, with humility and sourcing.
- Avoid presenting speculative origin theories as doctrine before research is strong enough.

**Reference:** `references/sns-sol-site-gateway-notes.md`

**When to use:** Creating Acadian/Cajun cultural preservation websites, building community-focused local websites with heritage elements, iterative design improvements based on user feedback.

**Workflow:**
1. **Project Setup** - Use `/new_website` scaffold or create manually
2. **Initial Mockup Creation** - Focus on reduction: preserve core content, split secondary content, prototype one strong hero component first
3. **Iterative Design Refinement** - Present visual mockup → gather feedback → implement improvements → repeat
4. **Technical Implementation Support** - Use Opencode delegation for complex implementations
5. **Key Acadian Website Elements:**
   - **Visual Identity:** Slate Grey (#2C3E50), Bronze (#B87333), Glowing Blue (#3498DB), Verdure Green (#27AE60), Cream (#F5E6D3)
   - **Symbols:** Lion 🦁 (Dugas/strength), Star ⭐ (navigation), Verdure 🌿 (Doucet/growth)
   - **Tagline:** "Finding Ourselves in This Universe" / "Doux et Fier"
   - **Author attribution:** acadie.sol (or user's preference)

**Tone calibration:**
- Keep Acadien copy *lightly* regional and welcoming rather than heavily dialectal
- A few regional markers go a long way: `icitte`, `pis`, `asteure`, `d'icitte`, `chez nous`
- Language toggle should read **English / Acadien**; avoid framing as generic French/Français
- Use subtle parallax/background motion for first-impression polish
- Keep nav/title logic page-aware for cohesive feel

**Pitfalls to Avoid:**
- Don't treat Acadian culture as monolithic - recognize regional variations
- Avoid superficial cultural appropriation - focus on authentic representation
- Don't over-engineer simple community information sites
- Ensure content is accessible to elders and non-tech-savvy community members
- Remember that many Acadian communities value simplicity and direct communication

**See original:** Full website building workflow preserved from `acadian-website-builder` skill.

---

### D3. Directory Draft Intake / Inbox Staging
Use when building or populating the Acadie.sol directory from either public research or live/manual conversation.

**Core rule:** keep the capture shape stable, but do not block on missing fields. The intake must preserve useful detail even when the source is imperfect.

**Default attribution and trust labels:**
- **Submitted by:** `Acadie.sol` unless the user explicitly overrides it
- **Manual/live source label:** `In person`
- **Public sources:** keep URL bullets for traceability when available

**Stable draft buckets:**
- **Public data to carry forward** — the narrow, reusable directory facts
  - business name
  - address
  - public phone number
  - business hours
  - email only if publicly posted
  - any other truly public fact that should survive into the entry
- **Public notes** — shareable extra detail that enriches the public page
- **Public source** — URLs for scraped research, or `In person` for live/manual capture
- **Admin notes** — steward-only reminders, follow-up items, source caveats, return-later prompts

**Workflow:**
1. Read the user’s trigger as an intake command, not a discussion request.
2. Decide whether the input is manual/live or public scrape.
3. Write the draft into `inbox/` using the stable bucket shape.
4. Preserve unexpected details in the nearest safe bucket instead of dropping them.
5. Promote to `entries/<slug>/` later when the page shape is clear.
6. Keep brand/collective pages separate from location pages when the business has multiple branches.

**Practical pattern:**
- Prefer a "quiet ones first" intake sequence so the inbox accumulates raw material before schema work.
- Do not fail the whole capture because phone, email, or hours are missing.
- If a source is live/manual, use `In person` instead of pretending there is a public URL.
- Keep `Submitted by : Acadie.sol` as the default in every assistant-made draft unless explicitly overridden.
- When the user supplies new fields not anticipated by the current shape, route them into Public notes or Admin notes rather than rejecting the entry.
- Manual-first intake should be the primary path; scrape mode can reuse the same formatter later.

**Reference:** `references/directory-draft-intake.md`

---

### E. Private Legacy Capture -> Capturer Training -> Community Memory Rituals
Use when the user is exploring Acadian cultural preservation through family story capture, elder wisdom transmission, checkpoint/legacy interviews, or later-stage community prompt rituals.

**Phased stewardship ladder:**
1. **Private family checkpoint capture first** — start with one family member, 3-5 themed conversations, privacy-first ownership, and explicit consent/boundaries.
2. **Teach capturers second** — train trusted people to run their own family interviews and archives rather than centralizing all capture in one steward.
3. **Community memory rituals later** — only after trust/governance exists, consider weekly creative prompts or seasonal contributions that help a living culture continuously describe itself.
4. **Incentives last** — sponsor-backed collectibles, badges, or tokens should reward stewardship and sincerity, not content farming or speculative extraction.

**Pilot session pattern:**
- Prefer themed sessions over one giant life interview:
  1. origins / childhood / formative influences
  2. hardship / failure / turning points
  3. relationships / family / forgiveness
  4. work / craft / principles / mistakes
  5. what should future generations remember
- Record raw audio first, preserve it, then transcribe and review.
- Distinguish three layers in later outputs: **memory** (what happened), **meaning** (what it meant), and **judgment** (how decisions are made now because of it).

**Privacy / architecture rule:**
- Default to **private-by-default, family-owned-by-default, exportable-by-default** archives.
- Treat files as the durable source of truth; software is a helper layer, not the inheritance itself.
- For pilot stacks, prefer local recording + local Whisper/faster-whisper transcription + portable files/metadata before committing to always-on hosted infrastructure.
- Avoid promising one VPS per family as the default long-term model; lifetime hosting costs and maintenance responsibility become unclear fast.

**Interactive endpoint rule:**
- A chat interface (Open WebUI or similar) can be a useful endpoint, but it is only the front door.
- The underlying archive should preserve citations, permissions, and the distinction between direct quotes, summaries, and inferences.
- Use retrieval/search as an access layer over structured family archives, not as a replacement for them.

**Prompt design rule:**
- Ask open-ended questions that invite story, meaning, and transferability, not just facts.
- Strong prompts include: "What changed who you became?", "What do people misunderstand about a good life?", "What kind of judgment took the longest to earn?", and "Tell me about a time when life corrected you."

**Ethical will / testament distinction:**
- Legacy systems can help people verbalize wishes, values, context, and messages for descendants.
- Do not confuse this with the legally operative will. Treat AI-assisted capture as support for reflection, family guidance, and estate-planning preparation unless proper legal formalities are separately handled.

**Future Acadian community ritual direction:**
- Community prompts can later capture evolving language, humor, recipes, local places, sayings, and seasonal memory — not just elder biography.
- If incentives are introduced, bias toward recognition, stewardship, and cultural contribution rather than raw volume or financialized posting.
- A useful test for new features: **does this add soul back, or just add noise?**

---

**Common Pitfalls (All Acadian Work)**

1. **Identity Confusion** - Acadian ≠ Quebecois ≠ generic French
2. **Wrong emoji** - 🇦🇨 is Ascension Island, not Acadia
3. **Language exclusivity** - Always search in both French and English
4. **Dismissing lore** - Family stories often have geographic truth even if specifics are fuzzy
5. **Academic consensus as final** - "unknown origin" is a starting point, not dead end
6. **GBrain import quirks** - Use absolute paths, check backend status
7. **Browser dependencies** - Delegate web tasks if Camofox isn't running
8. **Solana for DID** - No W3C DID method exists for Solana. Use did:web primary.
9. **note CLI with complex content** - Parentheses and special chars break `note` bash parsing. Use simple quoted strings.
10. **Facebook event links** - Public metadata often yields title/date/host, but time may be missing; use the user’s stated time rather than guessing.
11. **Event export mode** - `--stdout` is inspection-only for the legacy directory payload; use `--all` when the site needs events, calendars, and search assets.

---

## Verification Checklist

- [ ] Cron job runs successfully and appends to archive
- [ ] Telegram delivery confirms with `deliver: origin`
- [ ] QuickThoughts updated with strategic pivot and file paths
- [ ] Visual design reflects Acadian cultural sensitivity
- [ ] Navigation is intuitive for community members of all ages
- [ ] Core cultural information is prominent and accurate
- [ ] Site loads quickly on typical community internet connections
- [ ] Content is available in relevant languages (French/English)
- [ ] Directory data repo and site repo both pushed to GitHub
- [ ] RSS feed.xml is valid and contains recent signals
- [ ] No secrets/credentials in either repo
- [ ] .gitignore present in both repos

---

## Related Skills

- `regional-news-monitoring` - Regional news monitoring
- `acadian-hive-mind-research` - Now absorbed into this umbrella
- `static-site-prototype-iteration` - Static site prototyping
- `opencode` - Opencode delegation

---

*Consolidated: May 2026*
*Source skills: acadian-tech-stewardship, acadian-hive-mind-research, acadian-website-builder*
