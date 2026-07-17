---
name: qr-code-generator
description: Generates QR codes from URLs or text for sharing in chats
category: media
author: MidnightRider.sol
version: 1.0.0
---

# QR Code Generator Skill

## Overview
This skill provides QR code generation capabilities for the Hermes Agent. It allows users to create QR codes from URLs, text, or other data and share them directly in chat platforms like Telegram.

## Features
- Generate QR codes from URLs or arbitrary text
- High-quality PNG output with configurable size and error correction
- Base64-encoded image return for seamless platform integration
- Simple command interface: `/qr <url-or-text>`

## Installation
The skill should be installed in the `media` category:

```bash
hermes skills install media/qr-code-generator
```

## Usage
Once installed, you can generate QR codes by:

1. **Direct command**: `/qr drip.haus/riderverse`
2. **Natural language**: "Generate a QR code for drip.haus/riderverse"
3. **With parameters**: `/qr https://example.com --size 10 --border 4`

## Technical Details
- Uses the Python `qrcode` library for generation
- Supports standard QR code features:
  - Adjustable size (box_size)
  - Configurable border width
  - Error correction levels (L, M, Q, H)
  - Customizable colors (future enhancement)
- Outputs PNG images encoded as base64 for chat delivery

## Files
- `SKILL.md` - This documentation file
- `__init__.py` - Skill interface and command handling
- `qr_generator.py` - Core QR generation logic

## Example Output
When invoked with `/qr drip.haus/riderverse`, the skill returns:
- A PNG image of the QR code encoding "drip.haus/riderverse"
- Ready for direct display in Telegram or other chat platforms

## Extensibility
This skill can be extended to:
- Add logo embedding in QR codes
- Support for dynamic QR codes with tracking
- Integration with web3/x402 for paid generations
- Batch QR code generation from CSV/files
- Template system for common use cases (WiFi, contacts, etc.)

## Author
MidnightRider.sol

## License
MIT