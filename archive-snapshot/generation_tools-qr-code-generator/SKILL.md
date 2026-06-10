---
name: qr-code-generator
description: "Generate QR codes reliably in Hermes. Use when the user asks to create, save, or send a QR code for a URL or text. Works best by calling Python 3.10 in a subprocess, adding the Python 3.10 user site-packages path if needed, saving a PNG to /tmp, and returning a Telegram-ready MEDIA: path."
license: Proprietary
---

# QR Code Generator

Generate QR code PNGs for URLs or plain text and return a Telegram-friendly `MEDIA:/path/to/file.png` response.

## Reliable runtime approach

Use a small Python subprocess instead of trying to call agent delegation from inside the skill runtime.
In this environment, the stable pattern is:

1. Use `python3.10` explicitly.
2. Add `/home/midnight/.local/lib/python3.10/site-packages` to `sys.path` before importing `qrcode`.
3. Create the QR with `qrcode.QRCode(...)`.
4. Save to a unique temp file under `/tmp/`.
5. Verify the file exists and is a valid PNG before responding.
6. For Telegram delivery, return `MEDIA:/absolute/path/to/file.png` on the first line.

## Supported inputs

- URLs, with or without scheme
- Plain text
- Long text strings
- Anything that can be encoded as a QR payload

## Recommended generation settings

- Error correction: `M`
- Box size: `10`
- Border: `4`
- Output format: PNG

These settings balance scannability and file size for chat delivery.

## Example output format

For Telegram, return:

```text
MEDIA:/tmp/qr_example_123.png
QR code generated for: https://example.com
🔗 Encoded: https://example.com
```

If generation fails, return a short error message instead of a file path.

## Implementation notes

- Use a unique filename such as `/tmp/qr_<hash>_<timestamp>.png`.
- Prefer `python3.10` if the environment has multiple Python versions.
- Keep the subprocess timeout short and reasonable.
- Validate PNG bytes by checking the PNG header if you need extra confidence.
- Do not hardcode `~/.hermes` paths inside generated file paths.
- Do not rely on agent delegation APIs from within this skill; that path was not reliable in practice for this use case.

## Quick test case

Generate a QR code for:

```text
google.com
```

Expected result: a scannable PNG saved to `/tmp/` and a `MEDIA:` response for Telegram.

## Troubleshooting

### `ModuleNotFoundError: qrcode`

Add the Python 3.10 user site-packages path before import:

```python
sys.path.insert(0, "/home/midnight/.local/lib/python3.10/site-packages")
```

### Output path exists but Telegram does not show the image

Make sure the response starts with exactly `MEDIA:` followed by an absolute file path on the first line.

### QR code scans poorly

Increase quiet zone or error correction, or shorten the payload.

## Notes from field use

A direct Python subprocess with `python3.10` proved more dependable than trying to route QR generation through agent delegation in this environment. Keep this skill simple and deterministic.
