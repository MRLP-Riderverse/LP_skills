---
name: human-signal-recon
description: "Use when research must reveal lived community experience."
category: research
aliases: [peer-signal-research, lived-experience-recon, community-culture-monitoring]
---

# Human-Signal Reconnaissance

Use this skill when the user wants to feel what people are actually living, caring about, making, gathering around, or quietly building. It is for research where institutional summaries, policy updates, rankings, and algorithmic trend lists are insufficient.

## Core distinction

Separate two layers:

- **Human signal:** first-person testimony, local scenes, physical places, ordinary routines, creative work, small acts of care, reasons people gather, and the texture of participation.
- **System context:** policies, institutions, platform changes, economic conditions, and official announcements that shape the human signal.

System context can explain a situation, but it cannot substitute for lived experience.

## Research workflow

1. Define the desired feeling or evidence. Ask whether the user wants testimony, local energy, youth culture, community innovation, social gathering, creative scenes, or signs of isolation.
2. Set an explicit cutoff date and preferred window. Prefer recent work, but retain older pieces when they illuminate a durable local pattern; label the age clearly.
3. Search for small social worlds rather than rankings. Prefer local outlets, independent publications, first-person interviews, artist-run spaces, youth projects, DIY scenes, community enterprises, low-cost gatherings, online-to-offline activity, and cultural infrastructure.
4. Avoid substituting celebrity coverage, streaming rankings, generic trend articles, startup funding announcements, or institutional press releases for community evidence.
5. For broad requests, split research into parallel lanes such as:
   - place/community innovation and technology-enabled participation;
   - youth, music, art, DIY, gaming, creator, or pop-cultural scenes.
6. Extract concrete human details: who, where, what they do repeatedly, what friction they face, what object/place/ritual matters, and how a newcomer might enter.
7. Prefer stories about repeatable social infrastructure—rooms, exchanges, local maps, rehearsal spaces, festivals, workshops, community enterprises, and low-pressure invitations—because these reveal how belonging is actually produced.
8. Synthesize the cross-story pattern without pretending the sample represents a whole country. State whether the findings show a broad pattern, several local pockets, or only illustrative examples.
9. Distinguish poor indexing from genuine absence. If few stories surface, do not conclude that people do not care; they may be distributed across weakly indexed local scenes.

## Delegation pattern

For evidence-heavy research, delegate parallel, self-contained lanes. Each worker should receive:

- geographic/cultural scope;
- cutoff window;
- source-quality requirements;
- explicit exclusions;
- required fields: title, date, outlet, URL, place/community, lived signal, and relevance to the user;
- a requirement to verify dates and URLs and disclose access limitations.

Treat worker summaries as research leads, not unquestionable proof. When an async summary is truncated, read the complete saved summary before synthesizing. Review the source list, omitted details, limitations, and whether verification was actually performed.

## Verification boundaries

If direct article extraction is unavailable, say so. It is acceptable to confirm title, date, outlet, and URL through search metadata, but do not imply that snippets constitute full-text review. Separate:

- directly read article content;
- search-result metadata;
- agent-reported details awaiting independent confirmation.

Never fabricate quotes or enrich a thin search snippet with invented narrative detail.

## Output shape

Return a compact, Telegram-friendly set of links, usually 3–7 items. For each include:

- title and linked URL;
- date and outlet;
- place/community;
- one or two concrete lived details;
- why it may matter to the user.

Then add a short synthesis answering: What are people doing? What kinds of spaces or rituals recur? Does this suggest isolation, distributed participation, or both?

## Application to local cultural projects

For a project such as Acadie.sol, treat the research as a **peer-signal map**, not a media leaderboard. Track:

- who is gathering;
- what they are making or preserving;
- which small spaces enable participation;
- how online tools lead to offline contact;
- what low-pressure entry points exist;
- what signals could later become a community artifact, monthly video, or recurring series.

Media should document and amplify an existing community rather than manufacture one. A local community can come first, a conversational social room second, and public media/discoverability third.

## Common pitfalls

- Reporting systems and policies without showing what life feels like.
- Treating YouTube or search visibility as a complete map of culture.
- Mistaking a lack of indexed articles for a lack of activity.
- Overgeneralizing from conflict stories, major cities, or one demographic.
- Calling a startup announcement community innovation without evidence of community use.
- Delivering a bibliography without explaining the shared human pattern.
- Trusting a truncated delegation preview instead of reading the full saved result.

## Reference

See `references/session-pattern-community-first.md` for the session-derived pattern: local artifacts → conversational community → accumulated cultural record → public media.
