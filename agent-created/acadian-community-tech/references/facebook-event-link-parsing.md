# Facebook Event Link Parsing Notes

Use this when the user sends a Facebook event URL and asks you to capture it into the Acadie.sol directory.

## What to extract first
- `og:title` for the event title
- canonical URL for the stable public event page
- `og:description` / meta description for host + date clues
- location text from the canonical URL path when present

## Practical note
- Public Facebook event HTML can expose useful metadata even when the mobile page redirects to login.
- If the public page does **not** expose the start time, do **not** guess it from the URL.
- Use the user-provided time as the source of truth when the page only gives the date.

## Export reminder
- For event records, `python3 scripts/export_to_site.py --all` is the full site export path.
- `--stdout` only prints the legacy directory payload; it does not write events/calendar/search assets.
- After export, verify `assets/events-data.json` and `assets/calendar/<event-id>.ics`.
