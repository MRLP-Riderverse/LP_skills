---
name: adaptive-research-system
description: Approach for building user-responsive research/monitoring systems that evolve based on feedback and changing requirements.
category: research
---

# Adaptive Research System Approach

A methodology for creating research and monitoring systems that adapt to user needs through iterative feedback, focusing on building reusable skills that evolve with changing requirements.

## Real-World Application: Hermes Personal Monitoring System

This approach was successfully applied to build a personalized technology and music monitoring system for a user who:
- Initially requested a narrow frontier stack tool comparison
- Redirected focus to broader technology monitoring (Solana, blockchain, Linux, real-world tech)
- Added cybersecurity monitoring after seeing the initial format
- Requested proper skills directory placement (~/.hermes/skills/ not ~/.hermes/frontier-stack/)
- Created a weekly music artist monitor for specific interests (Green Day, BMTH, Jaden, Joji, etc.)
- Implemented a #note capture system for Telegram notes to integrate with their notecore app
- Set up cron jobs for daily tech briefs (8:10am Halifax) and weekly music briefs (Wed 10:00am Halifax)
- Designed the system to preserve their notecore app as the primary note-taking system

## When to Use This Approach

Use this approach when:
- Building research or monitoring systems that need to evolve over time
- User requirements may change or become clearer during implementation
- You want to create reusable skills that can be refined based on experience
- The initial scope might need broadening or narrowing based on user feedback
- You're building systems that integrate with existing user workflows

## Core Principles

1. **Start with User's Current Language**: Begin with the user's terminology and framing
2. **Embrace Course Correction**: Treat location/direction changes as learning, not failure
3. **Iterate Based on Usage**: Refine focus areas as you learn what's actually valuable
4. **Preserve User Workflow**: Design to complement, not disrupt, existing systems
5. **Build Reusability First**: Create systems designed to be used repeatedly

## Step-by-Step Process

### Phase 1: Initial Implementation (Listen Closely)
1. Implement exactly what the user specifies initially
2. Use their exact terminology and preferred structure
3. Note any assumptions or ambiguities for later clarification
4. Deploy a minimal viable version quickly

### Phase 2: Feedback Integration (Expect Changes)
1. **Anticipate relocation requests**: Users often have strong preferences about where things belong
   - Example: Moving from `~/.hermes/frontier-stack/` to `~/.hermes/skills/research/...`
2. **Prepare for scope evolution**: Initial narrow focus often broadens
   - Example: Frontier stack review → broader tech monitoring with cybersecurity
3. **Welcome feature additions**: Users think of new needs as they see the system work
   - Example: Adding cybersecurity monitoring after seeing the tech brief format
4. **Respect workflow boundaries**: Users want to keep primary systems intact
   - Example: Keeping notecore as primary note system, using Hermes only for capture

### Phase 3: Reusability Focus (Build for Repeated Use)
1. **Create proper skill structure**: YAML frontmatter + organized supporting files
2. **Separate concerns**: System prompt, research task, philosophy, output template
3. **Make it cron-ready**: Design for scheduled, automated delivery
4. **Document user preferences**: Save timing, delivery method, specific interests
5. **Design for easy updating**: Simple process to modify focus areas or frequency

## Key Adaptation Patterns Observed

### Pattern 1: Location Correction
- **Signal**: User says "this should be in skills folder" or similar
- **Action**: Move files to `~/.hermes/skills/[category]/[skill-name]/`
- **Update**: Skill metadata to reflect correct category/path
- **Prevention**: When in doubt, ask preferred location before creating directories

### Pattern 2: Focus Broadening
- **Signal**: User says "actually I also want to track..." or "make it more general about..."
- **Action**: Update research task and standard analysis areas
- **Example**: Narrow tech stack → broad tech monitoring + cybersecurity
- **Indicator**: User feels initial scope is too restrictive or missing key areas

### Pattern 3: Feature Addition by Observation
- **Signal**: User sees output and thinks of related needs
- **Action**: Add new monitoring area or evaluation criterion
- **Example**: Adding cybersecurity after seeing tech brief format
- **Trigger**: User says "you know what we should also add..."

### Pattern 4: Workflow Preservation
- **Signal**: User wants to keep existing system as primary
- **Action**: Design capture-only or read-only integration points
- **Example**: #note capture for Telegram, symlink for notecore (read-only)
- **Principle**: Be a helpful adjunct, not a replacement

## Practical Implementation Tips

### For File Organization:
- Always check: "Should this be in the skills directory?" when creating new systems
- Use standard skill structure: SKILL.md + supporting files in same directory
- Let user specify category during creation when possible

### For Evolution-Friendly Design:
1. **Make research tasks modular**: Easy to add/remove monitoring areas
2. **Parameterize timing/delivery**: Simple to adjust cron schedule
3. **Separate what changes**: User interests vs evaluation framework vs output format
4. **Save user preferences**: In memory or skill notes for future reference

### For Novelty-First Digests:
- When the user asks for a vague "highlights this week" or "what might I not know" report, do a local novelty pass before writing the summary.
- Search the user's local notes first, then GBrain, using broad keywords and nearby synonyms.
- Treat no local hit as a strong signal that the topic is new; keep weak hits caveated.
- Keep the final output short, high-signal, and Telegram-friendly.
- For recurring monitoring jobs, do a **delta-first pass**: read the last delivered brief in full, treat the last 3 briefings as stale unless there is a concrete new release/post/commit/status change, and report silence instead of rehashing.
- If the discovery query misses the target session, browse recent sessions and open the named cron run directly before concluding there is no prior brief.
- See `references/novelty-pass-digest.md` for the compact comparison recipe.
- See `references/public-signal-recon.md` for the compact workflow when the ask is really a public-signal briefing or a high-fit shortlist.
- See `references/job-market-recon.md` for live Job Bank / local-fit job search patterns, keyword strategy, and posting triage.
- See `references/crypto-weekly-briefing.md` for a primary-source-first workflow for 7-day crypto / L2 / protocol briefs.
- See `references/delta-briefing-protocol.md` for the recurring delta-brief protocol and session-finding fallback.

### For live job-market recon / role-fit shortlisting:
- Start from the user's actual labor shape, not a generic job title.
- Derive search keywords from function and work mode (e.g. systems, analyst, support, hybrid, remote) rather than relying only on exact title matches.
- Use current postings only: treat Job Bank `200 + active title` as live, and `410` / `expired` as stale before ranking anything.
- Rank postings by autonomy, pay, transferability, credential friction, and work mode; prefer roles that can support or fund the user's own project work.
- When several roles are close, call out which ones are true fits versus bridge jobs versus low-leverage distractions.

### For policy / legal research:
- Treat the statute or regulation text as the primary source of truth before secondary reporting.
- Separate three questions explicitly: what was enacted, what is already in force, and what is deferred to proclamation or regulation.
- Call out thresholds, commencement dates, filing deadlines, and enforcement mechanisms separately; those are the bits users actually operationalize.
- Translate the legal change into system properties when the user asks about philosophy: transparency, auditability, power asymmetry, compliance burden, and whether the rule changes incentives or just paperwork.
- If generic search results mix in vendor content, re-anchor on official government / statute text before synthesizing.
### For User Communication:
1. **Explicitly ask about location**: "Should I put this in ~/.hermes/skills/...?"
2. **Confirm scope**: "Is this focused enough, or should we broaden to include X?"
3. **Invite observation**: "Once you see the output, let me know if you'd like to track anything else"
4. **Respect primary workflows**: "How can I work with your existing [system] instead of replacing it?"

## Verification Checklist
Before considering an adaptive research system complete:
- [ ] Files are in correct skills directory structure
- [ ] Skill has proper YAML frontmatter with category
- [ ] Supporting files exist (system prompt, research task, philosophy, template)
- [ ] Cron job is set with user-specified timing and delivery
- [ ] System incorporates user's specific interests and preferences
- [ ] Design allows for easy modification of focus areas
- [ ] User's primary workflow remains undisturbed
- [ ] Approach captures lessons from any course corrections made

## Files to Create When Using This Approach
1. `SKILL.md` (with YAML frontmatter: name, description, category)
2. `system-prompt.md` - Core instructions for the agent's role
3. `research-task.md` - Specific questions/goals for the monitoring
4. `philosophy.md` - Guiding principles (adapt user's builder philosophy)
5. `output-template.md` - Format for consistent reporting
6. Optional: `references/`, `templates/`, `scripts/` directories as needed

## Remember
The most valuable adaptive systems aren't those that never change direction, but those that:
- Make course corrections visible and intentional
- Learn from each adaptation
- Become more aligned with user needs over time
- Maintain usability throughout the evolution process

This approach turns user feedback from a source of frustration into the primary driver of system improvement.