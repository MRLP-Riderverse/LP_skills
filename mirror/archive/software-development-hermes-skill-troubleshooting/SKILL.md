---
name: hermes-skill-troubleshooting
description: Troubleshoot Hermes skill installation, dependencies, and execution issues - covers common problems when skills don't work as expected
version: 1.0.0
author: MidnightRider.sol
---
name: hermes-skill-maintenance
description: Complete Hermes skill maintenance — troubleshooting installation, dependencies, execution issues, TTS/voice configuration, and platform enablement.
category: software-development
aliases: [hermes-skill-troubleshooting, hermes-voice-tts]
---

# Hermes Skill Maintenance Umbrella

This is the **class-level skill** for all Hermes Agent skill maintenance operations. It consolidates skill troubleshooting, TTS/voice configuration, and platform enablement workflows.

**Trigger:** User needs to troubleshoot skill installation/execution issues, configure TTS or voice input, verify skill dependencies, or enable skills for specific platforms.

---

## Subsections

### A. Skill Troubleshooting (from `hermes-skill-troubleshooting`)
Troubleshoot Hermes skill installation, dependencies, and execution issues - covers common problems when skills don't work as expected.

**When to Use:**
- A skill installs but doesn't appear to work
- Getting "ModuleNotFoundError" when trying to use a skill
- Skills install but are blocked by security scans
- Unclear how to test skill functionality directly
- Need to understand difference between skill installation and platform enablement
- Want to execute skill functionality outside of normal chat command flow

**Systematic Approach:**

1. **Verify Skill Installation Status**
```bash
hermes skills list | grep -i <skill-name>
```
Look for the skill in the output with proper category, source, and trust status.

2. **Check Installation Details**
```bash
hermes skills inspect <skill-name>
```
This shows the skill's source, version, author, and other metadata.

3. **Troubleshoot Installation Issues**
- **Security Scan Blocks:** Community skills often trigger security scans that block installation
  - Fix: `hermes skills install /path/to/skill --force`
- **Installation Path Issues:** Skills must be in proper directory structure
  - Correct: `~/.hermes/skills/<category>/<skill-name>/`
  - Wrong: `~/.hermes/skills/<skill-name>/` (missing category directory)

4. **Diagnose Dependency Problems**
When skills fail with import errors (ModuleNotFoundError):
- Check Python environment: Hermes Agent uses its own virtual environment
- Install missing dependencies: `source ~/.hermes/hermes-agent/venv/bin/activate && pip install <package>`
- Or install to user site and adjust PYTHONPATH

5. **Test Skill Functionality Directly**
When skills don't work via chat commands, test the underlying code directly:
- Locate skill files: `ls -la ~/.hermes/skills/<category>/<skill-name>/`
- Examine skill structure: Look for `__init__.py`, implementation files, `SKILL.md`
- Execute core functionality: Run skill's core logic directly with Python

6. **Handle Platform Enablement Issues**
Skills often need explicit enablement for specific platforms:
- Check current configuration: `hermes skills config` (requires interactive terminal)
- Understand the difference:
  - **Installation:** Makes skill available to Hermes system
  - **Enablement:** Makes skill active for specific platforms (CLI, Telegram, Discord, etc.)
  - A skill can be installed but not enabled for your current platform

7. **Execute Underlying Scripts Directly**
When "one-shot" or utility skills don't work via normal channels:
- Look for actual implementation in skill directory
- Run underlying scripts with appropriate parameters

8. **Verify Output and Delivery**
- For Media-Generating Skills: Look for MEDIA: paths in output
- For Text-Based Skills: Verify returned content matches expectations

**Common Error Patterns:**
- **"ModuleNotFoundError: No module named 'X'"** → Missing dependency in execution environment
- **"Error: Could not find '/path/to/skill/'"** → Skill not in expected directory structure
- **Installation blocked by security scan** → Use `--force` flag
- **Skill installs but doesn't respond** → Skill not enabled for current platform

**See original:** Full troubleshooting workflow preserved from `hermes-skill-troubleshooting` skill.

---

### B. Voice & TTS Configuration (from `hermes-voice-tts`)
Configure, troubleshoot, and use text-to-speech (TTS) and voice input features in Hermes Agent.

**When to Use:**
- User asks about voice input (`hermes --voice`)
- User wants TTS output in CLI or Telegram
- Configuring or changing TTS providers (OpenAI, ElevenLabs, Edge, etc.)
- Troubleshooting voice playback or recording issues
- Setting up voice reactions or audio delivery

**TTS Configuration:**

TTS settings live in `~/.hermes/config.yaml` under the `tts` section:
```yaml
tts:
 providers:
 - name: openai
 api_key_env: OPENAI_API_KEY
 voice: alloy
 - name: elevenlabs
 api_key_env: ELEVENLABS_API_KEY
 voice_id: <voice-id>
 default_provider: openai
```

**CLI Usage:**
- **Inline TTS:** `/tts <text>` - speak text immediately
- **Tool call:** Use `text_to_speech` tool for programmatic TTS
- **Voice reactions:** Configured via `telegram.reactions` in config.yaml

**Voice Input:**
- **CLI:** `hermes --voice` to start voice-to-text session
- Uses configured STT provider (typically Whisper via OpenAI or local)

**Common Pitfalls:**
- **Don't guess TTS config paths** - Always verify actual config structure by reading `~/.hermes/config.yaml`
- **CLI vs Gateway TTS** - TTS in CLI uses local audio playback; TTS via Telegram gateway uses Telegram's audio file delivery
- **No `/reload` for TTS changes** - Config changes to TTS typically require restarting the CLI rather than `/reload` command

**Verification Steps:**
1. Check current TTS config: Read `~/.hermes/config.yaml` tts section
2. Test TTS: `/tts hello` in CLI
3. Verify provider API keys in `~/.hermes/.env`
4. Check logs: `~/.hermes/logs/agent.log` for TTS errors

**See original:** Full TTS configuration workflow preserved from `hermes-voice-tts` skill.

---

## Common Pitfalls

1. **Guessing TTS config paths** - verify actual config in `~/.hermes/config.yaml`
2. **Confusing CLI vs Gateway TTS** - different delivery mechanisms
3. **Assuming `/reload` works for TTS** - requires CLI restart
4. **Security scan blocks** - use `--force` for community skills
5. **Wrong directory structure** - skills need category subdirectory
6. **Missing platform enablement** - installed ≠ enabled for your platform
7. **Dependency access issues** - Hermes venv may not have user packages

---

## Verification Checklist

After troubleshooting or configuration:
- [ ] Skill appears in `hermes skills list`
- [ ] No import errors when testing core functionality directly
- [ ] Skill produces expected output when tested manually
- [ ] For platform-specific skills: verify enablement in config
- [ ] End-to-end test via intended interaction method (Telegram command, etc.)
- [ ] TTS config verified in `~/.hermes/config.yaml`
- [ ] TTS test successful: `/tts hello` in CLI
- [ ] Provider API keys present in `~/.hermes/.env`

---

## Related Skills

- `context-window-adjustment` - Context window configuration
- `plan` - Creating troubleshooting plans
- `telegram-notifier-tool` - Telegram delivery including audio messages
- `cron-telegram-auto-delivery` - Scheduled delivery with TTS support

---

*Consolidated: May 2026*
*Source skills: hermes-skill-troubleshooting, hermes-voice-tts*