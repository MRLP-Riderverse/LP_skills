# Local usage analytics from Hermes + OpenCode session stores

Use this when the user asks for prompt counts, daily averages, or rough usage analytics across Hermes and OpenCode without relying on cloud dashboards.

## Data sources

- Hermes session store: `~/.hermes/state.db`
  - `messages` table
  - count prompts with `role = 'user'`
- OpenCode session store: `~/.local/share/opencode/opencode.db`
  - `message` table
  - parse JSON in `data` and count rows where `role = 'user'`

## Working definition
Treat **one prompt = one user-role message**.

This is the cleanest comparable unit across both systems. Do not mix it with:
- assistant turns
- tool calls
- token totals
- session counts

## Recommended reporting
Always give both of these averages:

1. **Per active day**
   - total prompts / number of days with at least one prompt
   - best when the user wants to know their intensity on days they actually used the tools

2. **Per span day**
   - total prompts / inclusive calendar days from first recorded prompt to last recorded prompt
   - best when the user wants a broader long-range daily average including quiet days

## Why both matter
A single "average per day" is ambiguous.

- Active-day average answers: "How much do I prompt on days I use it?"
- Span-day average answers: "Across the whole recorded timeline, what's my daily average?"

Report both unless the user explicitly chooses one.

## Caveats

- Local DBs only reflect the histories present on disk.
- Archived, deleted, alternate-profile, or migrated databases may change the real lifetime total.
- If you use timestamps from mixed tools, normalize by local date before grouping.
- When reading OpenCode data, prefer the row timestamp if present; fall back to the embedded JSON time only if needed.

## Good response shape

- Hermes prompts: N
- OpenCode prompts: N
- Combined prompts: N
- Active days: N → avg X/day
- Full span: DATE to DATE (N days) → avg Y/day
- Short caveat about what was and wasn't included
