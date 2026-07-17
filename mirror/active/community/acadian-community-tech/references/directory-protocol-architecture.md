# Directory Protocol Architecture

Session: 2026-06-09 — architecture crystallized after research + design session.

## Two-Repo Split

**Non-negotiable: data and site are separate repos.**

- `acadie-sol-directory` (data repo): entries, schemas, RSS feed, fork/merge pattern. Git IS the API. No database.
- `acadie-sol` (site repo): rendering layer only. Pulls from data repo on build.

GitHub repos:
- Site: github.com/MRLP-Riderverse/acadie.sol
- Data: github.com/MRLP-Riderverse/acadie-sol-directory

Data survives site rebuilds. Site is disposable; data is sacred.

## Protocol Stack (corrected June 2026)

- **Layer 0 — Identity**: `did:web` (primary, no chain needed). NOT Solana — no W3C DID method exists for Solana. Optional on-chain anchor later via ethr-did or similar.
- **Layer 1 — Intent**: ActivityStreams 2.0 vocabulary (Offer, Request, Join, Invite) published as RSS/Atom items. Don't reinvent — extract from ActivityPub silos into open RSS.
- **Layer 2 — Propagation**: proximity-based routing by cultural + geographic proximity. Novel — no existing protocol does this. Not follow-based, but proximity-based (cultural + geographic routing).

## RSS Architecture

- `feed.xml` at repo root = main aggregated feed (all signals)
- `feeds/<name>.xml` = per-profile feeds for Tier 2 hosting
- Active feed keeps ~50 most recent `<item>` blocks
- Older items move to `archive/YYYY-MM.xml` (still in git, still accessible, just not in active subscription feed)
- Entries are appended to feed.xml; the file grows but gets curated/archived over time
- RSS is just a text file on a web server — edit, git push, live
- Backup: every RSS reader that subscribes keeps a local copy. Git repo is also backup. Self-replicating by design.

### Pitfall: `note` CLI and complex content

The `note` CLI command (used for QuickThoughts) breaks on content with parentheses — bash syntax error. Use simple quoted strings only. For complex notes, write to a temp file first or use the hermes note capture workflow.

## Hosting Architecture

- **Mac Mini** = authoring station, NOT public server (Rogers blocks incoming on residential)
- **GitHub Pages** = public server (free, CDN-backed, 99.9% uptime)
- Workflow: edit locally → git push → GitHub serves it
- No VPS needed initially. Add one later for cron tasks or dynamic features.
- The feed.xml doesn't care where it lives. GitHub Pages, VPS, Cloudflare Pages — all serve the same file.

## Fork & Merge Pattern

How communities contribute back to the main directory:

1. Community forks `acadie-sol-directory`
2. Adds their entries in their own region subdirectory
3. Discovers cross-community entry → submits PR to main directory
4. Steward reviews → merges → credit lives in git history forever
5. Main directory grows because local directories feed it
6. Each local directory stays independently functional

This is the open-source contribution model, but for community data instead of code.

## Channel Architecture (5 channels, each with purpose)

| Channel | Purpose | Flavor |
|---------|---------|--------|
| RSS | The record, the pipe | Permanent archive, machines read it |
| Telegram | The pulse, announcements | 1-2/week, like a notification app |
| Discord | The conversation | Kitchen table, messy alive, raw RSS feeds via bot |
| Signal | The action, logistics | DND bypass, invite-only small groups |
| Hero banner | The boost | One thing, max reach, zero noise, rotates |

## Tier 2 Hosting (Cork Board Pattern)

People who don't want their own GitHub/servers get a feed under `feeds/their-name.xml` on the directory repo. URL: `acadie.sol/feeds/marie-boudreau.xml`. Works in any RSS reader.

When they're ready to graduate to their own server, they move the file and update the directory entry. Zero migration pain. You pin their card until they build their own wall.

## Content Moderation by Channel

- Site = curated clean (steward-controlled)
- Discord = firehose, community-moderated
- Telegram = you control the broadcast
- Signal = private by default

## Directory Seeds Itself

The Acadian briefings (regional news research) create directory entries as a byproduct. Briefing research = directory population. The two workflows compound.

## Research Findings (June 2026)

- **Decidim**: wrong fork — municipal governance monolith, too heavy, no federation, no cultural identity layer
- **ActivityStreams 2.0**: already has intent vocab (Offer, Request, Invite) — don't reinvent
- **No minority-language community** has working SSI + directory + intent system — genuine gap worth filling
- **Nouvelle-Aquitaine**: doing infra-first (satellite WiFi), we're doing protocol-first — same direction, different altitude
- **Catalan**: has Decidim + guifi.net but no identity/discovery/intent composition
- **Basque**: drought parallel (climate stress hitting minority-language regions is structural, not coincidental), new communication strategy worth monitoring

## Entry Schema

Full schema at `schemas/entry.schema.yaml` in the data repo. Key fields:
- slug, name, category (person/organization/venue/project), location, links, meta, tags, related, verification
- Phase 1: Open Directory — no gate, community submissions welcome, verification optional
- Phase 2: Solana ID anchors (optional, did:web primary)
- Phase 3: Coordination layer (intent signals, matchmaking)

## What's Next

- First real directory entry (MR LP as reference implementation)
- Feed generator script (entries → feed.xml automatically, no hand-editing forever)
- Four-doors site: Know, Find, Offer, Show Up
- Test RSS subscription on phone
- Weekly meetup practice
