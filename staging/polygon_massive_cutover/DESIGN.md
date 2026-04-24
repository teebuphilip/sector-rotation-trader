# Polygon/Massive Runtime Migration Design

## Goal

Move the live runtime pipeline off Yahoo/yfinance without making the nightly run slow or flaky.

The required outcome is not "replace imports". The required outcome is:

- one market-data fetch boundary
- one cached snapshot per run
- all runtime consumers read from the snapshot
- no repeated per-algo network fetches during the run

Until that exists, the Yahoo-backed runtime remains the safer launch path.

## Why The First Cutover Was Incomplete

The first cutover changed the core tactical path and some downstream reporting paths, but the normal/crazy runtime stack still calls `scanner.safe_download()` directly in multiple places.

That means two bad options:

1. Leave it as-is: runtime still relies on Yahoo in multiple places.
2. Blindly swap all imports to `scanner_polygon`: runtime explodes in duration because Polygon free tier is rate-limited and the current code fetches data repeatedly inside per-algo loops.

The fix is architectural, not cosmetic.

## Design Principle

Only one component should talk to Polygon/Massive during a nightly run:

- `scripts/build_market_snapshot.py`

Everything else should consume the local snapshot.

## Target Architecture

### 1. Shared market snapshot builder

Add a new script:

- `scripts/build_market_snapshot.py`

Responsibilities:

- collect the full ticker universe needed by the run
- fetch all prices once from Polygon/Massive
- normalize the data into a stable schema
- write the snapshot to disk
- fail loudly if coverage is too low or the snapshot is stale

Suggested outputs:

- `data/market_cache/latest_snapshot.json`
- `data/market_cache/latest_metadata.json`

Optional better format if we want later:

- parquet for price tables
- json for metadata

### 2. Shared snapshot loader

Add a small module:

- `market_data.py`

Responsibilities:

- load snapshot from disk
- expose helpers like:
  - `load_snapshot()`
  - `get_close_series(ticker)`
  - `get_latest_price(ticker)`
  - `get_price_frame(tickers)`
- hide the storage format from callers

### 3. Runtime consumers move to snapshot reads

These should stop talking to Yahoo directly and stop doing live network fetches during the run.

Primary runtime consumers:

- `daily_run.py`
- `normal/runner.py`
- `crazy/runner.py`
- `normal/seed.py`
- `crazy/seed.py`
- `scripts/rolling_30d_leaderboard.py`
- `scripts/rank_daily.py`
- `scripts/quality_check.py`
- `precompute_signals.py` replacement path

Price-sensitive algos/adapters to review:

- `normal/algos/bailey.py`
- `crazy/algos/biscotti.py`
- `crazy/algos/bailey.py`
- `crazy/algos/tsa.py`
- `crazy/adapters/price_only.py`
- `crazy/algos/glassdoor.py`
- any other algo/adapter that currently calls `safe_download()` or `yfinance`

### 4. Validation moves to snapshot completeness

The nightly validator should check:

- snapshot exists
- snapshot date matches run date
- sector ETF coverage is complete
- required ticker universe coverage is above threshold
- missing tickers are listed explicitly

This is better than discovering broken freshness later through downstream signal files.

## Snapshot Schema

### Metadata

Suggested `latest_metadata.json` shape:

```json
{
  "run_date": "2026-04-24",
  "generated_at": "2026-04-24T22:30:12Z",
  "source": "polygon_massive",
  "universe_count": 128,
  "covered_count": 124,
  "missing_tickers": ["XYZ"],
  "periods": ["1y", "2y", "3mo"],
  "notes": []
}
```

### Price data

If JSON:

```json
{
  "AAPL": {
    "dates": ["2026-04-20", "2026-04-21"],
    "close": [201.1, 202.4],
    "volume": [12345678, 11876543]
  }
}
```

If parquet:

- one row per date/ticker
- columns: `date`, `ticker`, `close`, `volume`

Parquet is cleaner long-term, but JSON is simpler to inspect at first.

## Universe Construction

The snapshot builder should derive the runtime universe from code and state, not from a hardcoded guess.

Required sources:

- `config.SECTOR_ETFS`
- current `state.json` open positions
- all normal algo universes
- all crazy algo universes that use price data
- benchmark tickers like `SPY`

Optional future extension:

- maintain a persisted universe file for review/debugging

## Workflow Order

Nightly order should become:

1. build market snapshot
2. run tactical/core path
3. run normal algos
4. run crazy algos
5. comparator suite
6. precompute signals
7. leaderboard/rank/quality/public pages
8. publish public repo

Important rule:

- if snapshot build fails critically, runtime should abort early
- if snapshot coverage is partial but still acceptable, metadata should record it and validation should decide whether to fail or warn

## Migration Phases

### Phase 1: reliability-first staging

Do not touch the live runtime yet.

Build:

- `scripts/build_market_snapshot.py`
- `market_data.py`
- local validation helpers

Goal:

- prove we can fetch and store the full nightly universe once

### Phase 2: switch low-risk readers first

Move these first because they are simpler readers:

- `scripts/rolling_30d_leaderboard.py`
- `scripts/rank_daily.py`
- `scripts/quality_check.py`

Goal:

- verify downstream reporting works from the snapshot

### Phase 3: switch runtime runners

Move:

- `normal/runner.py`
- `crazy/runner.py`
- `normal/seed.py`
- `crazy/seed.py`

Goal:

- remove repeated live fetches from the runtime loops

### Phase 4: switch price-sensitive algos/adapters

Move any algo or adapter still calling Yahoo or `safe_download()` directly.

Goal:

- complete the runtime cutover

### Phase 5: remove or quarantine Yahoo paths

After multiple clean nightly runs:

- remove remaining Yahoo runtime dependencies
- leave research-only Yahoo code clearly marked if we still need it temporarily

## Risks

### 1. Free-tier Polygon/Massive latency

Fetching the whole universe can still be slow.

Mitigation:

- one fetch boundary only
- aggressive local caching for sector/ticker metadata
- fail-fast coverage reports

### 2. Mixed lookback needs

Some consumers need different periods.

Mitigation:

- snapshot builder fetches a longest needed window once
- consumers slice locally

### 3. Hidden Yahoo usage in algos

Some algos import `safe_download()` or `yfinance` inside their own modules.

Mitigation:

- explicit inventory pass before cutover
- grep-based CI check later to block new Yahoo runtime imports

## Recommended Deliverables For The Real Build

1. `scripts/build_market_snapshot.py`
2. `market_data.py`
3. `docs/ops/market_snapshot_contract.md`
4. workflow step added before any runtime consumer
5. validation check for snapshot freshness and coverage
6. grep-based lint/check to prevent new runtime Yahoo imports

## Recommendation

For launch reliability:

- keep the current Yahoo-backed runtime live for now
- build the snapshot architecture in parallel
- cut over only after we have multiple clean nightly runs through the snapshot path

That preserves data continuity for May 15 while still moving toward the commercial-safe architecture the right way.
