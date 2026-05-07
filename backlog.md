# Post-July 1 Backlog

## Purpose

This is the backlog for features and product work that are explicitly out of scope for the May 15 free launch and should only be considered after the July 1 traction decision.

## Premium Workflows

### Weekly Lab Notes Generator
- Generate a premium weekly memo from fresh leaderboard moves, SPY comparisons, promoted/watchlist/graveyard changes, and notable algo updates.
- Output should be clean enough to publish with light human review, not raw model text.
- Goal: make the paid layer feel like ongoing operator coverage, not just gated pages.

### Per-Algo Explainer
- For any premium algo page, generate a concise explanation of:
  - what the signal is trying to capture
  - what changed this week
  - how it is doing versus SPY
  - whether the recent move looks like noise, regime fit, or deterioration
- Goal: make premium algo pages feel actively interpreted, not just stat dumps.

### Graveyard Autopsy Workflow
- For algos that fail badly enough to move to graveyard, generate a structured postmortem:
  - thesis
  - what actually happened
  - where performance broke
  - whether the failure looks structural or temporary
- Goal: turn failed signals into differentiated research content.

### Signal Family Analyst
- Generate family-level summaries for clusters like:
  - travel proxies
  - consumer stress proxies
  - macro/liquidity proxies
  - alternative sentiment proxies
- Goal: make the premium layer useful at the cluster level, not only single-algo level.

## Product / Agent Architecture

### Shared Skills Layer
- Build a shared reasoning layer used across premium workflows:
  - signal explanation
  - leaderboard interpretation
  - regime analysis
  - graveyard evaluation
  - risk/disclaimer style
- Goal: avoid one-off prompt drift across tools and pages.

### Named Workflow Agents
- Package post-July workflows as bounded agents/modules rather than one monolithic assistant.
- Candidate agents:
  - `weekly-lab-notes-agent`
  - `signal-review-agent`
  - `graveyard-autopsy-agent`
  - `family-analyst-agent`
- Goal: clearer ownership, testing, and future automation.

### Connector Separation
- Separate:
  - data collection
  - signal generation
  - explanation
  - publishing
- Goal: reduce hidden coupling in the paid workflow stack.

### Managed Orchestration
- Add a simple orchestration layer for premium workflows:
  - pull fresh data
  - run the right explainer/autopsy/note generator
  - write structured outputs
  - queue for human review
- Goal: make premium outputs repeatable and operable without manual chaos.

## Support / Operations

### Support and Bot Planning Session
- Decide what support layer is actually needed after July 1:
  - FAQ bot
  - member support bot
  - operator support console
  - internal issue triage helper
- Goal: avoid shipping a generic chatbot that does not solve a real problem.

### Overnight Status Feed Hardening
- Finish Google Drive auth for the overnight status sync.
- Validate that Gemini-facing files stay current without manual babysitting.
- Goal: make the morning ops feed dependable before expanding it.

## Content / Research

### Publishable Plain-English Algo Spec
- Add a plain-English spec block to algo pages shortly after the May 15 launch.
- Each algo page should answer:
  - what this signal is trying to detect
  - what data it uses
  - what makes it fire
  - when it exits
  - why it could fail
- Goal: make each algo page legible to a normal reader without requiring them to infer the strategy from stats and trade logs alone.

### Legacy Algo Thesis Backfill
- Backfill full structured thesis inventory for legacy algo pages that still rely on thin copy.
- Include:
  - thesis
  - universe
  - data sources
  - signal logic
  - entry / exit
  - position sizing
  - risks
- Goal: bring older algos up to the same descriptive standard as ideation-pipeline algos.

### Premium Signal Change Notes
- Add short premium change logs for signals that moved materially in rank, alpha, or drawdown.
- Goal: give subscribers a reason to come back beyond static dashboards.

## Public Ops Visibility

### Public Ops Notes / Daily Changelog Page
- Add a visible ops notes page shortly after launch.
- It should log operationally meaningful daily events in plain English, for example:
  - `6:30am - 5 new signals generated`
  - `6:30pm - market analysis complete`
  - `preview publish succeeded`
  - `daily run recovered manually`
- Goal: make the lab feel alive, transparent, and inspectable instead of opaque.
- Secondary goal: create a lightweight public-facing audit trail without forcing users into raw logs.

## Rule

Nothing in this file is launch-critical for May 15.
Nothing in this file should preempt domain, MailerLite, launch stability, or the July 1 traction decision.
