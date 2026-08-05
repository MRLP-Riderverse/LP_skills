---
name: canada-fresh-human-signal
description: "Fetch canada fresh: Canadian human-signal research."
category: research
aliases: [fetch-canada-fresh, canada-fresh, canadian-peer-signal]
---

# Fetch Canada Fresh

Use this skill when the user says **“fetch canada fresh”** or clearly asks for a fresh read on what people in Canada are building, gathering around, making, caring about, or quietly experimenting with.

The purpose is to answer:

> What does Canada feel like from the inside right now?

This is not a generic Canadian news brief. It is a **peer-signal map**: a compact set of recent, human-centered stories that can help the user feel less isolated and notice where culture, community, and local innovation are alive.

## Default scope

- Reference date: establish the live date at the start of the run.
- Freshness: prefer the last 90 days. Do not silently widen the window.
- Default result count: 6 strong items, usually 3 from each lane.
- Geographic priority: Acadia / Atlantic Canada first; Montréal / Québec second; broader Canada third.
- If the evidence is weak, return fewer than six items and say so.

## Search lanes

### Lane A — Community innovation

Look for real people and community use involving:

- youth-led projects;
- local technology use;
- community-owned or repeatable social infrastructure;
- cultural and maker spaces;
- independent local media;
- community enterprises and mutual aid;
- local discovery tools, maps, platforms, or digital projects;
- online-to-offline participation;
- projects that create low-pressure entry points for belonging.

Technology is an enabling layer, not a requirement. A keychain exchange, rehearsal room, local media map, or youth enterprise may be more relevant than a conventional startup.

### Lane B — Youth and social/pop culture

Look for:

- independent music scenes;
- DIY venues and artist-run spaces;
- small festivals and bilingual or hybrid cultural projects;
- gaming, creator, or maker communities;
- local art scenes;
- youth organizing and informal gatherings;
- identity and genre experimentation;
- projects where online discovery leads to physical participation.

## Source rules

Prefer, in order:

1. local and independent outlets;
2. campus papers and community newsrooms;
3. regional magazines and local radio;
4. scene publications and artist-run media;
5. national outlets only when the story has strong human texture.

Avoid using these as substitutes for peer signal:

- Netflix or streaming rankings;
- celebrity gossip;
- generic trendicles;
- national political misery without a concrete community response;
- corporate press releases with no evidence of lived use;
- startup funding announcements without community impact;
- institutional summaries that contain no people, place, ritual, object, or friction.

## Required evidence per result

For each selected story, capture:

- title and canonical URL;
- publication date and outlet;
- place or community;
- who is involved;
- what they are repeatedly doing, making, hosting, or preserving;
- one or two concrete human details;
- why it may matter to someone feeling isolated;
- verification/access note when full text could not be read.

Keep interpretation separate from source fact. Do not invent quotes, motivations, ages, or article-body details from a headline or thin search snippet.

## Verification discipline

- Verify the URL, title, outlet, and date with the source page when possible.
- If direct extraction or browser access fails, use exact-title/date search metadata only and clearly label the limitation.
- Treat delegated worker summaries as research leads, not unquestionable proof.
- If an async result is truncated, read the complete saved summary before synthesizing.
- State whether the sample shows a broad pattern, several distributed pockets, or merely illustrative examples.
- Never treat weak indexing as proof that a community is inactive.

## Output format

Use a compact Telegram-friendly structure:

## Canada Fresh — [date]

### [Lane A or Lane B] — [title](URL)
**Date/outlet:** ...
**Place/community:** ...
**Human signal:** ...
**Why it matters:** ...

Repeat for 3–7 items.

End with:

### What seems alive
Three or four cross-story patterns.

### Isolation counter-signal
Say directly whether the run suggests active distributed participation, fragmentation, both, or insufficient evidence.

### What seems missing
Name gaps in the search without converting absence of coverage into absence of activity.

Include a short sources/limitations note when search metadata rather than full article text was used.

## Acadie.sol interpretation

When relevant, connect the stories back to the user's community-first ladder:

1. local artifacts and relationships;
2. a conversational social room such as Discord;
3. accumulated public record and cultural memory;
4. monthly video or series as a harvest of community life.

Media should document and amplify an existing community rather than manufacture one. The goal is cultural concentration and sustained attention, not maximum global reach.

## Optional modifiers

Modifiers are intentionally deferred until repeated use reveals real friction. Future examples may include:

- `fetch canada fresh — acadie`
- `fetch canada fresh — youth`
- `fetch canada fresh — tech`
- `fetch canada fresh — culture`
- `fetch canada fresh — montreal`
- `fetch canada fresh — atlantic`
- `fetch canada fresh — hopeful`
- `fetch canada fresh — difficult realities`

The bare trigger must remain useful without modifiers.

## Non-recursive scheduling note

For a future Monday 05:00 local cron run, attach this skill to an LLM-driven cron prompt such as: `Fetch Canada Fresh. Use the default scope and output format in the attached skill. Deliver the compact brief to the origin.` Do not make the skill recursively schedule another cron job.
