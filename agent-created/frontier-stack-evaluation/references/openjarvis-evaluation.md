# OpenJarvis Evaluation (May 2026)

**Source:** Stanford SAIL / Hazy Research / Ré lab
**GitHub:** https://github.com/open-jarvis/OpenJarvis
**Paper:** arXiv 2605.17172
**Project site:** https://scalingintelligence.stanford.edu/blogs/openjarvis/
**Docs:** https://open-jarvis.github.io/OpenJarvis/
**License:** Apache 2.0
**Sponsors:** Laude Institute, Stanford Marlowe, Google Cloud, Lambda Labs, Ollama, IBM Research, Stanford HAI

## What It Is

OpenJarvis = framework for local-first personal AI. Not a chatbot. Not an Ollama wrapper. A modular architecture for running AI agents on personal devices.

Five composable primitives:
1. **Intelligence** — on-device model catalog (Qwen, Gemma, GLM, Granite, etc.), auto-selects based on hardware capability
2. **Engine** — hardware-aware inference backend (Ollama, vLLM, SGLang, llama.cpp, Apple Foundation Models, etc.)
3. **Agents** — composable reasoning patterns designed for constrained contexts (ReAct, Orchestrator, Operative, etc.)
4. **Tools & Memory** — MCP support, Google A2A inter-agent comms, semantic indexing, messaging/webhook integration
5. **Learning** — closed-loop optimization from local trace data (SFT, LoRA, GRPO, bandit routing)

## Key Differentiator vs Ollama

| Aspect | Ollama | OpenJarvis |
|--------|--------|------------|
| Role | Model runner | Model system |
| Model selection | Manual | Hardware-aware auto-selection |
| Efficiency tracking | None | Energy, FLOPs, latency, dollar cost alongside accuracy |
| Learning loop | None | Fine-tunes from local traces (GRPO/LoRA) |
| Cloud fallback | None | Routes cloud vs local intelligently |
| Agent framework | None | 8 built-in agents across 3 execution modes |
| Skills | None | Imports from Hermes (~150), OpenClaw (~13,700), any GitHub repo |

## Hermes Compatibility

**Companion, not competitor.** Architecture:

```
┌─────────────────────────┐
│ Hermes (orchestration)  │ ← skills, cron, memory, gateways, delegation
├─────────────────────────┤
│ OpenJarvis (inference)  │ ← local models, engine selection, learning loop
├─────────────────────────┤
│ Hardware (device)       │ ← GPU/CPU/NPU
└─────────────────────────┘
```

OpenJarvis already imports Hermes skills via `jarvis skill install hermes:arxiv` and `jarvis skill sync hermes --category research`. They follow the agentskills.io open standard.

## Evaluation (Frontier Stack Framework)

- **Maturity**: ✅ Shippable — one-liner install, desktop GUI, 8 built-in agents, Rust extensions
- **Portability**: ✅ macOS, Linux, WSL2, Native Windows, Desktop GUI (.exe/.dmg/.deb/.rpm/.AppImage)
- **Resilience**: ✅ Local-first by design, cloud as fallback only
- **Lock-in Risk**: ⚠️ Low — Apache 2.0, standard model formats, agentskills.io spec. Learning loop data is local.
- **Orchestration Fit**: ✅ Designed as infrastructure layer, not UI — complements Hermes as orchestration
- **Real-world Usability**: ✅ `jarvis init` detects hardware, recommends config. `jarvis doctor` for health checks.

## Installation

```bash
# macOS / Linux / WSL2
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash

# Then
jarvis                    # start chatting
jarvis init --preset <n>  # switch config
jarvis doctor             # health check
```

## Built-in Presets

| Preset | What it does |
|--------|-------------|
| morning-digest-mac/linux/minimal | Spoken daily briefing from email, calendar, health, news |
| deep-research | Multi-hop research across indexed docs with citations |
| code-assistant | Agent with code execution, file I/O, shell access |
| scheduled-monitor | Stateful agent on a schedule with memory |
| chat-simple | Lightweight conversation, no tools |

## Research Context

From the "Intelligence Per Watt" study: local models handle 88.7% of single-turn chat/reasoning at interactive latencies. Intelligence efficiency improving 5.3× from 2023 to 2025. The hardware is ready; the software stack wasn't. OpenJarvis is that stack.

## Use Case for This User

Older device, constrained VRAM, hand-picking models and praying = current pain. OpenJarvis solves this with hardware-aware auto-config + learning loop that tunes models to specific workflows over time. The flywheel: Hermes skills generate real agent traces → OpenJarvis collects traces → Learning loop fine-tunes local model for those workflows → Same skills run better locally → repeat.

*Evaluated: May 30, 2026*
