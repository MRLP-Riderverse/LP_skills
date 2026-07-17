# Live job-market recon notes

Session-derived workflow for answering: "is there anything worth my time near Bathurst/Moncton/remote?"

## Query strategy
- Start from the user's actual labor shape: consultant / partner / bridge-builder, not generic employee slot.
- Derive keywords from function, not titles alone:
  - business analyst
  - systems analyst
  - technical support specialist
  - user support technician
  - technical sales representative
  - digital communications specialist
  - health services consultant
  - remote / hybrid / work from home
- Search current postings on Job Bank with `site:jobbank.gc.ca/jobsearch/jobposting` plus location and title keywords.
- Use DuckDuckGo snippets to get candidate job IDs quickly, then open the live Job Bank posting directly.

## Verification pattern
- Prefer the Job Bank HTML page with `?wbdisable=true` for extraction.
- Treat HTTP 200 + non-expired title as active.
- Treat HTTP 410 or title containing `Job posting expired` as stale.
- Pull a compact summary from the HTML:
  - employer
  - location
  - work mode (remote / hybrid / on-site)
  - salary
  - terms of employment
  - education / experience thresholds

## Ranking heuristic
Score each posting by:
1. **Autonomy** — can the user steer or shape the work?
2. **Pay** — is the compensation aligned with the user's experience floor?
3. **Transferability** — does the work build toward LP / consulting / systems work?
4. **Credential friction** — does the posting require a degree-only gate?
5. **Work mode** — remote/hybrid preferred over rigid on-site unless the pay is strong.

Treat the following as generally higher-fit:
- hybrid business analyst / systems analyst roles
- remote or hybrid technical support roles with decent pay
- consultative sales / solution roles only if they preserve autonomy
- institutional analyst roles if the pay materially clears the user's internal floor

Treat the following as lower-fit unless there is a strong strategic reason:
- student-shaped comms roles with low pay
- on-site support work that underpays relative to responsibility
- roles that are credential theater without enough upside

## Session example (2026-07)
Helpful active/posting patterns seen in live Job Bank recon:
- **business analyst – computer systems** — Moncton, hybrid, about **$45–$50/hr**
- **analyst, systems** — Vitalité Health Network, on-site, about **$67,600–$94,406/yr**
- **technical sales representative** — remote, about **$32/hr**
- **user support technician** — Dieppe, on-site
- **technical support specialist – IT** — Moncton, hybrid, lower pay band

These are examples of the user's current fit window, not durable facts; rerun live checks before citing availability.
