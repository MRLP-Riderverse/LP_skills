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

### D. Acadian Web3 Gateway / SNS Stewardship
Use when the user is shaping `acadie.sol` or a similar culturally sensitive namespace into a beginner-friendly public gateway rather than a crypto-native speculation page.

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
- Do **not** assume SNS subdomains automatically get their own `.sol.site` websites. Current SNS docs indicate `sol.site` is for eligible `.sol` domains and that subdomains are ineligible. Treat member subdomains as identifiers first, not standalone websites.
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

## Common Pitfalls (All Acadian Work)

1. **Identity Confusion** - Acadian ≠ Quebecois ≠ generic French
2. **Wrong emoji** - 🇦🇨 is Ascension Island, not Acadia
3. **Language exclusivity** - Always search in both French and English
4. **Dismissing lore** - Family stories often have geographic truth even if specifics are fuzzy
5. **Academic consensus as final** - "unknown origin" is a starting point, not dead end
6. **GBrain import quirks** - Use absolute paths, check backend status
7. **Browser dependencies** - Delegate web tasks if Camofox isn't running

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

---

## Related Skills

- `regional-news-monitoring` - Regional news monitoring
- `acadian-hive-mind-research` - Now absorbed into this umbrella
- `static-site-prototype-iteration` - Static site prototyping
- `opencode` - Opencode delegation

---

*Consolidated: May 2026*
*Source skills: acadian-tech-stewardship, acadian-hive-mind-research, acadian-website-builder*
