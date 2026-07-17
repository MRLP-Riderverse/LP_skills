# 123m Adapter Architecture

## Two-Layer Pattern

This skill follows the same adapter pattern as `yt-launcher`:

1. **Upstream script** (`/home/midnight/ExoCortex/Agentic/Scripts/123m`) — human-friendly, opens browser, prints banner. Untouched by the skill.
2. **Hermes adapter** (`/home/midnight/ExoCortex/Agentic/Scripts/123m-hermes`) — wraps the upstream, captures output, emits a single JSON object on stdout for machine consumption.

## JSON Contract

The adapter always emits one JSON line on stdout:

```json
{
  "tool": "123m",
  "query": "original query string",
  "status": "ok" | "error",
  "opened_url": "https://ww8.123moviesfree.net/search/?q=...",
  "upstream": "/home/midnight/ExoCortex/Agentic/Scripts/123m",
  "exit_code": 0
}
```

## Upstream Script Notes

- URL-encodes query via `python3 -c 'urllib.parse.quote_plus(...)'`
- Opens browser via `xdg-open` (gracefully ignored if unavailable)
- Human-readable banner with author branding (`MidnightRider.sol`)
- No flags or modes (unlike `yt` which has `-p` for private mode)

## Adapter Responsibilities

- Verify upstream exists and is executable (exit 127 + JSON error if not)
- Run upstream, capture combined stdout+stderr
- Reconstruct the target URL independently (URL-encode the query the same way)
- Emit JSON regardless of upstream exit code
- Pass through the upstream exit code as its own exit code

## Why Not Parse the Banner?

The upstream prints decorated banner text (`*** Bet, now searching Blockbuster... ***`). This is human-friendly but fragile for machine parsing. The adapter reconstructs the URL independently and emits structured JSON, so Hermes never needs to parse banner text.

## Telegram Presentation

- Query text is the clickable hyperlink (markdown `[Title](url)`)
- Title-case the query for presentation
- `disable_link_previews: true` in Hermes config suppresses embed cards
