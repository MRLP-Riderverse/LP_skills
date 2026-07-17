---
name: qr-code-generation
description: Generate QR codes for URLs, text, or any shareable content using Python's qrcode library with reliable dependency handling and Opencode delegation fallback.
category: generation_tools
aliases: [qr-code-reliable, qr-code-generator-opencode]
---

# QR Code Generation Umbrella

This is the **class-level skill** for generating QR codes. It consolidates reliable QR generation with Python's qrcode library, Opencode delegation for dependency handling, and general QR code creation workflows.

**Trigger:** User asks to create a QR code for a URL, text, contact info, or any shareable content; need to share links in scannable format for chat, print, or presentation.

---

## Subsections

### A. Reliable QR Generation with Python (from `qr-code-reliable`)
Generate reliable QR codes using Python's qrcode library with proper user site-packages access.

**When to Use:**
- Generating QR codes for URLs, text, or other data
- Need reliable access to Python packages installed in user site-packages
- Creating shareable QR codes in Telegram chats
- Building skills that require consistent dependency resolution across environments

**Key Features:**
- ✅ Reliable access to user-installed Python packages
- ✅ Proper QR code generation with error correction (level M)
- ✅ Appropriate sizing (box_size=10, border=4) for good scannability
- ✅ Valid PNG output format
- ✅ Clear success/error messaging

**Technical Implementation:** Uses subprocess with explicit python3.10 and user site-packages path to access qrcode library.

**See original:** Full reliable generation workflow preserved from `qr-code-reliable` skill.

---

### B. Opencode Delegation Pattern (from `qr-code-generator-opencode`)
Generate QR codes by delegating to the Opencode AI coding agent, which reliably handles Python dependencies and environment issues.

**When to Use:**
- Direct Python package access is problematic in Hermes skills
- Need reliable dependency resolution
- Want to leverage Opencode's environment management capabilities

**Key Features:**
- ✅ Leverages Opencode's reliable Python environment
- ✅ Handles dependency installation/access automatically
- ✅ Generates valid PNG QR code images
- ✅ Works when direct skill execution fails due to dependencies

**Approach:** Use Hermes' `delegate_task` function to invoke Opencode with clear instructions for QR code generation.

**See original:** Full Opencode delegation pattern preserved from `qr-code-generator-opencode` skill.

---

### C. General QR Code Guidelines
General guidelines for QR code generation across all methods.

**Tips:**
- Works for any URL, plain text, or encoded data
- PNG format ensures compatibility with all QR scanners
- Keep the generated file path for reference if user needs to reuse it

**Pitfalls:**
- Ensure dependencies (qrcode, pillow) are available in the environment
- For complex URLs with special characters, ensure proper encoding
- Test QR code scans correctly before delivering to user

---

## Common Pitfalls

1. **Dependency access issues** - Python environment may not have qrcode installed
2. **Wrong file format** - Always output PNG for maximum compatibility
3. **Missing error correction** - Use at least ERROR_CORRECT_M for reliability
4. **Too small box size** - Use box_size=10 or larger for scannability
5. **No border** - Include border=4 for proper QR code framing

---

## Verification Checklist

After generating QR code:
- [ ] File exists at specified path
- [ ] File is valid PNG format
- [ ] QR code scans correctly to encoded data
- [ ] MEDIA: path returned for Telegram delivery
- [ ] User informed what the QR code links to

---

## Related Skills

- `python-user-packages` - Python user site-packages access
- `opencode` - Opencode CLI for delegation
- `opencode-delegation-pattern` - Opencode delegation patterns

---

*Consolidated: May 2026*
*Source skills: qr-code-reliable, qr-code-generator-opencode*