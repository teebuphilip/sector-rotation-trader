# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Paper trading system implementing a sector rotation strategy. Tracks 11 SPDR sector ETFs, identifies the leading (accelerating) sector by 3M-6M performance spread, then enters individual stock positions in that sector when breakout + volume + Bollinger Band signals fire. Exits on 2 consecutive closes below the 20-day MA. Uses $100k base capital with up to $100k margin.

## Commands

```bash
# One-time bootstrap (downloads 2y of data, simulates 90 trading days)
python seed.py

# Daily run (meant for GitHub Actions, but can run locally)
python daily_run.py
```

There are no tests, linter, or build step. The project is pure Python with three dependencies: `yfinance`, `pandas`, `numpy`.

## Architecture

**Data flow:** `daily_run.py` orchestrates the full pipeline each day:
1. Downloads market data via `yfinance`
2. `scanner.py` finds the leading sector ETF and filters stock candidates that outperform it
3. `signals.py` checks entry/exit conditions on each candidate
4. `portfolio.py` manages state (cash, margin, positions, P&L) and persists to `state.json`
5. `dashboard.py` generates a static HTML dashboard at `docs/index.html`

**`seed.py`** does the same logic but walks day-by-day through a 90-day historical window to bootstrap realistic state. Run once before the first `daily_run.py`.

**State persistence:** All portfolio state lives in `state.json` (positions, trade log, daily snapshots). `docs/trades.json` is a subset exported for the dashboard. Both are auto-committed by the GitHub Actions workflow.

**`config.py`** holds all tunable parameters — capital limits, signal thresholds, lookback periods, file paths. Every other module imports from it.

**`scanner.py:SECTOR_STOCKS`** maps each sector ETF to its top 10 holdings. This is the candidate universe for stock-level signals.

## GitHub Actions

`.github/workflows/daily_run.yml` runs `daily_run.py` at 6:30 PM ET (22:30 UTC) Mon-Fri, then auto-commits `state.json`, `docs/index.html`, and `docs/trades.json`. The dashboard is served via GitHub Pages from `docs/`.

## Key Design Decisions

- Entry requires all 3 signals simultaneously: price breakout above 10-day high, volume >= 150% of 20-day avg, and BB bandwidth expanding
- Exit uses consecutive-day tracking (`consec_below_ma` stored per position in state)
- Margin positions track `using_margin` flag; on close, principal is repaid first from proceeds
- `yfinance` is the sole data source; no API keys needed
