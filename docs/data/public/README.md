# Public Data Contract

This directory is the nightly-generated public artifact contract for the website repo.

The rule is simple:

- compute facts once in the private repo
- write stripped public-safe JSON here
- render static pages from these files
- push only public-safe artifacts downstream

## Nightly Files

Top-level:

- `daily.json`
- `leaderboard.json`
- `families.json`
- `watchlist.json`
- `promoted.json`
- `graveyard.json`

Benchmarks:

- `benchmarks/spy.json`
- `benchmarks/qqq.json`

Signals:

- `signals/index.json`
- `signals/_sectors.json`
- `signals/_sectors/*.json`
- `signals/<ticker>.json`

## Source of Truth

These files are derived from:

- `data/product/*.json`
- `docs/signals/*.json`
- `docs/leaderboards/rolling_30d.json`
- `data/rank_history.csv`

Generator:

- `scripts/build_public_artifacts.py`
