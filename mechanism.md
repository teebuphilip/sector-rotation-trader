# StockArithm Content Mechanism

## The Goal

**Primary:** Build trust and analyst credibility by publishing public, testable market ideas with visible winners and losers.

**Secondary:** Create qualified traffic and returning readers who understand the lab, the process, and the limits.

**Tertiary:** Earn downstream product pull when a signal, explanation, or pattern is strong enough to matter.

## The Home Base

**The repo is the source of truth.**

StockArithm content should be generated from validated artifacts and not from memory, vibes, or post-hoc storytelling.

Everything else feeds from that.

## The Content Loop

```text
validated facts
  -> content generator
  -> per-channel drafts
  -> review / copy / publish
  -> feedback
  -> improved rules
```

The content system is a formatting layer, not a trading layer.

It does not invent metrics.
It does not change the lab.
It does not hide failures.

## Operating Rule

If it is not in the validated facts package, it does not exist.

That means:

- no invented returns;
- no invented reasons;
- no invented certainty;
- no pretending a short sample is proof.

The content layer can interpret, but it cannot fabricate.

## The Output Contract

For any post date and slug, emit a dispatcher-ready bundle:

```text
marketing/content/{YYYY-MM-DD}-{slug}/
  meta.json
  x.md
  medium.md
  substack.md
  substack_note.md
  reddit_algotrading.md
  reddit_investing.md
  reddit_stocks.md
  reddit_quant.md
  reddit_security_analysis.md
```

If a channel is not used for a given post, the file can be omitted or marked `skip` in `meta.json`, but the schema should stay stable.

## Status File

Each bundle should include a `meta.json` that tells the dispatcher:

- what the post is;
- when it should run;
- which channels are ready;
- which Reddit targets are included;
- which files to post.

The dispatcher should own posting and write-back status.
The generator should own preparation.

## Channel Roles

| Channel | Purpose | Role |
|---------|---------|------|
| X | Short hook and reach | Fast, sharp, direct |
| Medium | Secondary funnel | Optional broader reach |
| Substack | Home base | Full long-form article |
| Substack Note | Discovery | Short teaser or question |
| Reddit | Community discussion | Targeted, subreddit-specific version |

## What The Generator Should Do

The generator should:

- read the validated facts;
- choose the right theme or angle;
- write channel-specific drafts;
- write the `meta.json`;
- keep the output folder self-contained;
- leave posting to the dispatcher.

## What The Generator Should Not Do

The generator should not:

- post directly;
- guess channel credentials;
- invent facts;
- create a new schema per repo;
- force the operator to copy/paste between systems.

## Success Condition

The system is working if:

- the draft bundle can be picked up by the dispatcher without hand editing;
- the copy feels native to the target channel;
- the content stays honest when the signal is ugly;
- the operator can scale across multiple products without living on social media.

## Final Rule

The content system exists to turn validated truth into channel-ready drafts, not to become another job.

If the output is not dispatcher-ready, it is not done.
