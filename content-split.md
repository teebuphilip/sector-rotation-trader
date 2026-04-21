# Content Split

## TL;DR

Ship the product as a static public site plus a later premium layer.

The nightly `6:30 PM ET` run computes the facts once.
Those facts then generate:

1. public-safe JSON
2. static public pages
3. private/internal artifacts that do not leave the private repo

This keeps the publishing model simple and stable enough to ship in July.

## Product Split

### Free

Free exists to prove the lab is real.

Include:

- homepage
- stripped leaderboard
- family summaries
- promoted algos summary
- watchlist summary
- graveyard / failures summary
- blog
- launch logs
- selected quality checks / lab notes
- public daily report
- public signal summary pages

Free should answer:

- is the lab real?
- is it active?
- is it honest?
- is it interesting?

### Paid

Paid exists to deliver the useful operating layer.

Include:

- full leaderboard
- full per-algo pages
- full per-ticker pages
- detailed signal context
- full trade history
- equity curves
- premium summaries
- downloadable CSVs later
- private benchmark / backtest detail later

Paid should answer:

- what matters now?
- what actually traded?
- what is beating SPY?
- what is the evidence?

## Architecture Rule

Use static generation for public pages.

Do not make the browser reconstruct product state from many random files.

Preferred flow:

```text
nightly run computes facts
-> publish stripped public JSON
-> render static HTML from that JSON
-> push static site artifacts to the public repo
```

Not preferred:

```text
nightly run dumps mixed artifacts
-> browser fetches many repo files
-> page logic rebuilds state client-side
```

## Public vs Private

### Public Artifacts

Generate every night:

- `docs/data/public/daily.json`
- `docs/data/public/leaderboard.json`
- `docs/data/public/families.json`
- `docs/data/public/watchlist.json`
- `docs/data/public/promoted.json`
- `docs/data/public/graveyard.json`
- `docs/data/public/benchmarks/spy.json`
- `docs/data/public/benchmarks/qqq.json`
- `docs/data/public/signals/index.json`
- `docs/data/public/signals/<symbol>.json`

### Static Public Pages

Render every night from the public JSON:

- homepage
- leaderboard
- families
- promoted
- graveyard
- blog index
- daily report page
- ticker/signal pages

### Private/Internal Artifacts

Do not publish to the public repo:

- raw ideas
- factory intervention/failed specs
- codegen logs
- full state files
- full trade logs
- full equity curves
- premium leaderboard payloads
- private benchmark detail
- internal debugging outputs

## Immediate Goal

Before auth or premium plumbing gets serious, the site must have:

1. a clean nightly public artifact contract
2. deterministic static page generation
3. a strict public/private split

That is the shortest path to a July ship.
