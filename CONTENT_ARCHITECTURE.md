# StockArithm Content Architecture

## Purpose

StockArithm content turns validated market artifacts into channel-specific public drafts.

It exists so the lab can publish daily posts, signal spotlights, failure reports, and future dispatcher-ready bundles without inventing new facts or manually rewriting the same idea for every channel.

The content system is intentionally separate from the trading system.

It does not run algos. It does not seed algos. It does not generate ideas. It only reads already-produced artifacts and formats validated facts.

## Core Rule

```text
If it is not in the deep validation report, it does not exist.
```

The content system must not invent metrics, recompute returns, infer unstated causes, or add market commentary that is not already supported by the report.

## Guide Docs

These are the two operating guides for the content layer:

- `soul.md` — voice, standards, and what the content should feel like
- `mechanism.md` — output contract, flow, and responsibility split

## Current Flow

```text
data/rank_history.csv
+ docs/leaderboards/rolling_30d.json
+ docs/signals/index.json
-> scripts/write_deep_validation_report.py
-> reports/deep_validation/latest.json
-> scripts/generate_content.py
-> content/*.txt

reports/deep_validation/latest.json
-> scripts/post_generator.py
-> drafts/YYYY-MM-DD.md
-> scripts/morning_content_email.py
-> email to operator

reports/deep_validation/latest.json
-> scripts/social_content_generator.py
-> drafts/social/YYYY-MM-DD/
```

## Current Outputs

### Deep Validation

- `reports/deep_validation/YYYY-MM-DD.md`
- `reports/deep_validation/YYYY-MM-DD.json`
- `reports/deep_validation/latest.md`
- `reports/deep_validation/latest.json`

### Deterministic Content

- `content/daily/YYYY-MM-DD.txt`
- `content/signal_of_day/YYYY-MM-DD.txt`
- `content/failures/YYYY-MM-DD.txt`
- `content/call_of_day/YYYY-MM-DD.txt`
- `content/weekly/YYYY-WW.txt`

### Social Drafts

- `drafts/social/YYYY-MM-DD/reddit_algotrading.md`
- `drafts/social/YYYY-MM-DD/reddit_investing.md`
- `drafts/social/YYYY-MM-DD/reddit_stocks.md`
- `drafts/social/YYYY-MM-DD/reddit_quant.md`
- `drafts/social/YYYY-MM-DD/reddit_security_analysis.md`
- `drafts/social/YYYY-MM-DD/twitter_x.md`

### Reddit Launch Refresh

- `drafts/reddit_launch/YYYY-MM-DD/algotrading.md`
- `drafts/reddit_launch/YYYY-MM-DD/investing.md`
- `drafts/reddit_launch/YYYY-MM-DD/stocks.md`
- `drafts/reddit_launch/YYYY-MM-DD/quant.md`
- `drafts/reddit_launch/YYYY-MM-DD/security_analysis.md`

## Voice System

The content voice has four fixed attributes:

- honest
- curious
- human
- transparent

The exact voice guidance lives in `soul.md`.

## Mechanism

The system is a formatting layer, not a trading layer.

The exact operating contract lives in `mechanism.md`.

## What This Must Not Become

The content system must not become:

- a hidden trading engine;
- a hype machine;
- a generic AI content farm;
- a place where the report and the copy drift apart.

If the content does not reflect the validated artifacts, it is not useful.
