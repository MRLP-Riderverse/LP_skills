---
name: current-hackathon-news-research
description: Research recent hackathon or event news using primary sources first, then corroborate with secondary coverage.
category: research
version: 1.0.0
---

# Current Hackathon / Event News Research

Use this skill when a user asks for recent updates about a hackathon, contest, launch event, or ecosystem program and you need fresh, date-sensitive information.

## Goal
Find the latest authoritative updates, summarize the event status, and surface articles with dates, winners, prize pools, participation numbers, and official links.

## Preferred Source Order
1. Official event landing page
2. Official blog / newsroom announcement
3. Organizer social posts or event hub pages
4. Secondary coverage only to add context or corroborate details

## Workflow
1. Search broadly with multiple keyword variants.
   - Include the event name, organizer, and likely terms like: winners, recap, announcement, launch, prize pool, builders, accelerator.
   - Try at least one query that targets official domains.
2. Open the most promising primary pages directly.
   - Prefer pages that expose metadata like title, description, date, and canonical URL.
3. Extract the core facts.
   - Event name
   - Date or date range
   - Status: announced / open / closed / winners announced
   - Prize pool or awards
   - Participation counts / projects / countries if available
   - Notable winners or tracks
4. Cross-check with one or two secondary sources only if the story is time-sensitive or unusually important.
5. Summarize clearly, separating confirmed facts from commentary.

## Practical Tips
- Search engine snippets can be incomplete; fetch the page itself whenever possible.
- If the official page is a marketing site, inspect page metadata and visible text for the event timeline.
- Event microsites often hide the useful facts in large client-rendered pages or escaped JSON-like blobs. Check page title, meta description, schema dates, agenda subpages, and repeated visible text snippets before falling back to secondary coverage.
- For conference-style ecosystem events, the most useful facts are usually in:
  - the main landing page
  - agenda / schedule subpages
  - FAQ / ticket pages that restate date, venue, and scope
  - official recap or announcement posts
- For hackathons, the most useful facts are usually in:
  - announcement posts
  - winners recap posts
  - event hub landing pages
  - live result/project pages
- If there are multiple related hackathons or sub-events, keep them distinct by organizer and date.
- See `references/solana-accelerate-miami-2026.md` for a worked example of extracting facts from an event microsite plus a secondary recap.

## Output Format
- Start with a brief overall read of the scene.
- Then list items in reverse chronological order.
- For each item include:
  - title
  - date
  - what happened
  - source link

## Pitfalls
- Don’t rely on one article if the organizer has an official announcement.
- Don’t merge similar-sounding events unless the organizer and dates match.
- Don’t state an event is “recent” without confirming the publication or event date.
- Don’t overstate winner counts or participation numbers unless the source is explicit.

## Verification Checklist
- [ ] At least one primary source checked
- [ ] Dates confirmed from page metadata or visible text
- [ ] Any prize / builder / project counts verified
- [ ] Secondary coverage used only for context
- [ ] Final summary distinguishes facts from interpretation
