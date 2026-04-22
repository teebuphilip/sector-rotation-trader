# CrazyStockAlgo — Product Context

## What It Is

CrazyStockAlgo is a public paper-trading lab for people who think weird real-world signals might beat the usual market bullshit.

It is a signal lab, a paper-trading system, and a public record. Every algo runs live. Every trade is logged. Every failure is shown.

## What It Is NOT

- Not an AI stock-picking app.
- Not a chatbot advisor.
- Not a retail autopilot.
- Not a magic picker that tells you what to buy.
- Not a backtested-only claims machine.
- Not a hedge fund in a box.
- Not another fintech dashboard with a gradient hero and a "leverage your portfolio" CTA.

If someone describes it as "an AI stock picking app," that is completely wrong.

## The Three User Archetypes

**The Receipts Guy**
Thinks most finance products are hiding survivorship bias. Wants the losses shown as clearly as the wins. Pays because the lab leaves the receipts on the table — bad signals, failed algos, honest force rank — instead of burying them.

**The Signal Hunter**
A trader or PM type who wants new signal ideas but only if someone is actually running them and keeping score against SPY. Pays for the inside view: which signals are holding up, which bucket they belong in, what the real win rate is after enough days to matter.

**The Alt-Data Nerd**
Believes alternative data can matter but wants to see which weird ideas are real, which are dead, and which are still unresolved. Pays to follow the experiment — not for a conclusion, but for the running record.

## The Core Interaction

When the site is working perfectly, a visitor scans the leaderboard to see which weird signals are actually holding up.

That is the product. One action. No wizard. No onboarding flow. No notification triage. The leaderboard is the front door.

## Free vs Paid

**Free user** gets proof that the lab is real. Stripped leaderboard, family summaries, public daily report, signal lab overview, blog. Enough to trust the system is running and honest.

**Paying subscriber** gets the inside view: which signals are worth taking seriously, which bucket they belong in (ALPHA / noise / unresolved), and what the lab is actually learning from them. Full leaderboard, per-algo detail, trade history, equity curves, comparator grading.

The free layer proves it. The paid layer explains it.

## Interaction Principles

These are UX stances the product holds on principle. Any feature idea that violates these is wrong for this product, regardless of how reasonable it sounds.

- **Lab notebook, not SaaS dashboard.** No wizard flows, no onboarding sequences, no activity feeds. A user who knows what a signal lab is should land and immediately understand what they're looking at.
- **Losses are first-class.** The failure report, the bottom of the force rank, the algos that haven't fired in 30 days — these are not embarrassments. They are the product. A feature that hides or softens failures breaks the brand.
- **Named things stay named.** Biscotti is Biscotti. Baileymol is Baileymol. Never replace algo names with IDs or generic labels in any user-facing surface.
- **No fake certainty.** No "our signals predict X." No "AI-powered." No win rate presented without days-running context. Every number needs honest framing.
- **Honest divergence is a feature.** An algo that is force rank #45 but rolling 30D rank #1 is not a contradiction — it is interesting. The product should surface that, not smooth it over.
- **The operator is visible.** The product sounds like it is run by a specific human. Not a team. Not a company. A guy. That is the brand. Features that make it feel corporate are wrong.

## What "On Brand" Means for Features

A feature fits if it answers YES to all of these:

- Does it help a user understand which signals are real vs noise?
- Does it show losses and failures as clearly as wins?
- Does it require zero explanation for someone who knows what a signal lab is?
- Does it sound like it was built by the guy who named an algo after his dead dog — not by a marketing team?

A feature fails if it:

- Assumes the user needs to be onboarded or guided.
- Hides or softens a bad result.
- Uses language from the forbidden list (cutting-edge, proprietary, AI-powered, seamless, robust, unlock your potential).
- Turns the product into something a fintech VC would recognize as normal.

## Positioning in One Line

Weird signals. Live results. No bullshit.

## The Story That Sells It

The author was reading a Medium article about algo trading with his dog Biscotti. Built a system. Named the first algo after the dog. Biscotti died. The algo kept running. That is the origin. That is the brand. The product exists because a real person built a real thing and kept score honestly.

That story is not marketing copy. It is the reason the product feels different from every other finance tool. Any feature, any post, any email that loses that thread is off brand.
