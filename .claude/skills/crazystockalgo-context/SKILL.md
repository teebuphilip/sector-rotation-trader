---
name: crazystockalgo-context
description: >
  Product context for CrazyStockAlgo. Load when discussing features, product backlog,
  marketing copy, user experience, positioning, post-launch roadmap, subscriber value,
  leaderboard, signal lab, brand voice, what to build next, content, Substack,
  pricing, launch, Reddit post, waitlist, or anything product-facing.
---

# CrazyStockAlgo Product Skill — Router

## When to load what

| Task | Load |
|------|------|
| Feature ideas, backlog, what to build next | `product.md` |
| Copy, email, Reddit post, Substack draft | `product.md` + `../../../content-generation.md` §Voice System |
| Pricing, paid vs free, subscriber value | `product.md` §Free vs Paid |
| Architecture, pipeline, algo questions | `../../../CLAUDE.md` |
| Brand voice, forbidden language | `product.md` §Interaction Principles + `../../../content-generation.md` §Forbidden |

## Hard constraints (apply to every task)

- Never suggest features that require onboarding wizards, notification centers, or activity feeds.
- Never soften or hide failures in any user-facing surface.
- Never describe the product as an AI stock-picking app, chatbot advisor, or retail autopilot.
- Named algos (Biscotti, Baileymol) are never replaced with IDs or generic labels.
- The operator is a specific human. Features that make it feel corporate are wrong.

## The one-line test

Before suggesting a feature or writing copy, ask:
"Does this sound like it was built by the guy who named an algo after his dead dog — or by a marketing team?"

If marketing team: rewrite or reject.
