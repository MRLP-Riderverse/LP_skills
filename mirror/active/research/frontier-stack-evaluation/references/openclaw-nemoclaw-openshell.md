# OpenClaw / NemoClaw / OpenShell — May 2026 Evaluation

## OpenClaw

- **What:** Personal AI assistant — "The AI that actually does things." Runs on WhatsApp, Telegram, Discord, Slack, iMessage, Signal, etc. 50+ integrations
- **Creator:** Peter Steinberger (`@steipete`) — joined OpenAI Feb 2026 (confirmed by TechCrunch and The Verge). Project continues open source under OpenAI sponsorship.
- **Repo:** `openclaw/openclaw` — **375K+ ⭐, 78K forks**, TypeScript, pnpm workspaces
- **Created:** Nov 24, 2025
- **Latest stable:** v2026.5.28 (May 30, 2026), beta v2026.5.30-beta.1 (May 31, 2026)
- **Size:** 1,468,384 KB
- **Integrations:** Gmail, Calendar, Spotify, Hue, Obsidian, Browser, GitHub, Twitter/X, Claude, GPT, Signal, iMessage, and 50+ more
- **Skill marketplace:** ClawHub.ai
- **macOS app:** Companion app (Beta), requires macOS 15+, Universal Binary
- **Install:** One-liner `curl -fsSL https://openclaw.ai/install.sh | bash`, or `npm i -g openclaw`, or git clone
- **Community:** ClawCon NYC (Mar 2026, covered by The Verge), Discord, strong community builds (multi-agent fleets, personal OS workflows, voice-guided deployments)
- **Sponsors:** OpenAI, GitHub, NVIDIA, Vercel, Blacksmith, Convex
- **Key distinction from Hermes:** OpenClaw = the "assistant" runtime (chat-first, integration-heavy). Hermes = orchestration/skill layer (cron, skills, delegation, session management). Complementary, not competing.

## NVIDIA NemoClaw

- **What:** Reference stack for running OpenClaw and Hermes more securely inside NVIDIA OpenShell sandboxes. Guided onboarding, hardened blueprint, routed inference, network policy, lifecycle management.
- **Repo:** `NVIDIA/NemoClaw` — **20.7K ⭐, 2.7K forks**, TypeScript
- **Created:** ~March 15, 2026 (barely 2.5 months old as of May 31)
- **Latest:** v0.0.55 (alpha — no formal GitHub releases, versioning through docs)
- **Docs:** `https://docs.nvidia.com/nemoclaw/latest/`
- **Stack architecture:** NemoClaw → orchestrates → OpenShell → isolates and runs → OpenClaw (or Hermes)
- **Hermes integration:** `NEMOCLAW_AGENT=hermes` flag or `nemohermes` alias lets you run Hermes inside the same hardened stack. NemoHermes dashboard on port 9119.
- **Inference backends:** NVIDIA Endpoints, OpenAI, Anthropic, Gemini, Ollama, vLLM on DGX Spark/Station
- **Pushed:** May 31, 2026 — iterating almost daily
- **Status:** Classic NVIDIA move — saw agent explosion, built enterprise-safe/GPU-optimized wrapper. Alpha and moving fast (55 versions in ~10 weeks). Release notes read like a war diary of edge cases being fixed.

## NVIDIA OpenShell

- **What:** The sandbox/isolation layer underneath NemoClaw. Seccomp, Landlock, network namespace isolation, credential proxying, no-new-privileges.
- **Repo:** `NVIDIA/OpenShell` — **6.3K ⭐, 775 forks**
- **Description:** "OpenShell is the safe, private runtime for autonomous AI agents."
- **Pushed:** May 30, 2026
- **Status:** Active. Powers NemoClaw's isolation layer.

## Relationship Summary

```
NemoClaw (orchestration/shipping wrapper)
    └── OpenShell (sandbox/isolation runtime)
            ├── OpenClaw (assistant runtime, 375K ⭐)
            └── Hermes (orchestration/skill layer, v0.14.0)
```

NemoClaw treats both OpenClaw and Hermes as first-class supported agents. They're complementary, not competing. The sandbox story (OpenShell) is the real value prop for anyone worried about agents running wild.

## Relevance to User's Stack

- **NemoClaw for "companies"**: User noted keeping NemoClaw in mind for extra guard-rail features in company/enterprise contexts
- **OpenClaw curiosity**: User increasingly interested but Hermes covers today's needs
- **Shared-tool repo idea**: User's instinct for a unified GitHub repo for streamlined installs mirrors what NemoClaw built, but NVIDIA's version is tightly coupled to OpenShell. A sovereign/local-first version is more aligned with user's philosophy.

---
*Researched: May 31, 2026*
*Sources: GitHub API (verified repo stats), openclaw.ai homepage, docs.nvidia.com, Google News*
