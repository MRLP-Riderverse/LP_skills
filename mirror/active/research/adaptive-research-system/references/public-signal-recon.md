# Public-Signal Recon for Weekly Briefs & High-Fit Shortlists

Use this when the user asks for:
- "highlights/happenings of the week"
- "what might I not know yet"
- a short report of recent online activity
- a shortlist of organizations to approach with custom offers

## Compact Workflow
1. **Local novelty pass first**
   - Search the user's local notes for broad keywords, proper nouns, and near-synonyms.
   - Search GBrain for the same terms.
   - Treat no hit as a strong signal the topic may be new; treat weak hits as possibly related.

2. **Broad public scan**
   - Pull 3-5 high-signal sources before writing a summary.
   - Prefer headlines, descriptions, and metadata over deep scraping when that's all that is available.
   - Use simple HTTP/RSS/HTML parsing fallbacks and keep the method lightweight.

3. **Evidence discipline**
   - If you only have headlines or snippets, label the result as headline-level evidence.
   - Don't overstate certainty; keep claims proportional to the source quality.

4. **Rank by novelty and fit**
   - Prioritize items that are both new to the user and relevant to their goals.
   - For company shortlists, rank by public signals: product/service fit, hiring language, geography, scale, and obvious pain points.

5. **Translate "85% acceptance" into honest language**
   - Do not present invented precision.
   - Reframe as: "highest-probability fit if approached well" or "strongest likely response candidates."
   - The goal is to identify unusually good prospects, not to pretend we know the true acceptance rate.

## Useful Heuristics
- High-fit companies often show one or more of:
  - customer-success / implementation / onboarding language
  - systems delivery, consulting, or managed-services language
  - multi-site operations with lots of coordination friction
  - public hiring for roles adjacent to the user's strengths
  - product or service descriptions that emphasize adoption, workflow, or human support

- Strong weekly briefs should stay short:
  - 3 to 7 bullets of novelty
  - 1-line why-it-matters
  - 1-line source note when needed

## Reuse Note
This reference is the compact recipe for turning a vague "what happened lately?" request into a novelty-filtered, source-triangulated briefing or a high-fit prospect shortlist.