# Community Sentiment Recon

Use for requests such as “find recent testimony,” “what are users saying,” or “compare current public sentiment” across products, platforms, or communities.

## Evidence rubric

Classify each finding before synthesis:

- **Direct testimony:** first-person account by a user/merchant/creator, with a date and permalink.
- **Community response:** replies that corroborate, challenge, or add detail to the original account.
- **Vendor testimony/marketing:** official case study, creator story, or promotional quote; useful context but not independent sentiment.
- **Review content:** Trustpilot, G2, YouTube, or blog review; only count as in-window if the publication/review date is verifiable.
- **Visibility signal:** whether the community is public, indexed, searchable, or mostly private. This describes evidence availability, not product quality.

Never convert “no qualifying public posts found” into “users are satisfied” or “users are unhappy.” Report it as an evidence limitation.

## Recommended workflow

1. Compute the date window from the live current date. State it explicitly, e.g. “June 20–July 20, 2026.”
2. Search the platform’s own community first. For Discourse-based forums, try:
   - `/latest.json`
   - `/search.json?q=...`
   - `/t/<slug>/<id>.json`
3. Select posts that contain a concrete experience, lesson, complaint, result, or comparison. Avoid generic prompts unless a reply contains the actual testimony.
4. Extract the author, timestamp, direct quote, thread URL, and useful replies.
5. Cross-check the second community through its official forum, Discord/community landing page, Reddit, YouTube, or review source. Record if access/indexing is structurally weaker.
6. Keep stale but relevant material in a clearly marked “near miss,” never silently mix it into the requested window.
7. Synthesize only what the evidence supports. Give each community a confidence level and separate sentiment from platform design/visibility differences.

## Example pattern from the Shopify/Fourthwall recon

A public Shopify Community Discourse endpoint exposed a July 20, 2026 merchant reply: the user learned that more traffic did not automatically produce sales; product pages, site speed, and trust signals mattered more, so they now optimize customer experience before scaling traffic. This is direct, in-window testimony.

Fourthwall’s official community landing page directs creators to Discord. When no in-window public testimony can be verified from that mostly private channel, the correct conclusion is limited public observability—not positive or negative sentiment. Older YouTube reviews may be useful background but must be labeled out-of-window.

## Output shape

- **Window:** exact dates
- **Community A:** quote, date, source, observed sentiment, confidence
- **Community B:** same fields, or explicit evidence limitation
- **Cross-community read:** one or two defensible patterns
- **Caveat:** what cannot be inferred from the available public evidence

Keep the answer short enough for Telegram. Use bullets, not tables; include direct links.