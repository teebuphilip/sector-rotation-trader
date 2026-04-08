# Sector Rotation Trader

Paper trading system implementing the sector rotation strategy from NRWise / DataDrivenInvestor. Designed as a realistic simulator so that if the strategy proves profitable, it can transition to live trading with minimal surprises.

## Strategy Rules

- $100k base capital, $10k max per position
- Up to $100k additional margin when fully deployed and signal fires
- 8.5% annual margin rate (daily accrual, settled proportionally on position close)
- Sector scan daily: leading SPDR ETF by 3M-6M performance spread (acceleration)
- Entry: price > 10-day high + volume > 150% of 20-day avg + BB expanding (all 3 required)
- Exit: 2 consecutive closes below 20-day MA OR 8% hard stop-loss (whichever hits first)

**Simulation window:** 6 months live tracking (seeded with 90 days historical)

---

## Recent Improvements (v2)

### Bug Fixes
- **Margin repayment**: Fixed phantom debt bug where losing margin positions left unpaid borrowed principal. Shortfall now correctly deducted from cash.
- **Interest settlement**: Accrued interest is now settled proportionally when closing margin positions (previously accumulated forever without being deducted).
- **Available cash**: `available_cash()` now subtracts accrued interest, preventing entries with money owed to margin.

### Risk Management (New)
- **8% hard stop-loss** (`STOP_LOSS_PCT`): Positions are force-exited if price drops 8% below entry, regardless of MA signal.
- **15% drawdown circuit breaker** (`MAX_DRAWDOWN_PCT`): No new entries when portfolio equity is >15% below its peak. Existing positions still managed normally.
- **Sector concentration limit** (`MAX_POSITIONS_PER_SECTOR = 5`): Prevents loading up on correlated positions in the same sector.

### Robustness
- **Retry logic on data downloads**: All yfinance calls now retry once after 30s on failure. Graceful degradation (skip run instead of crash) if data is unavailable.
- **Stale ticker fix**: Replaced PXD (acquired 2024) with FANG in XLE holdings.
- **GitHub Actions failure alerts**: Workflow now auto-creates a GitHub issue with log link on any run failure.

### Dashboard & Analytics (New)
- **Sharpe Ratio**: Annualized, risk-free rate 4.5%
- **Max Drawdown %**: Peak-to-trough tracking
- **Avg Win / Avg Loss**: Per-trade breakdown
- **Drawdown chart**: Separate chart showing drawdown % over time
- **SPY benchmark overlay**: Portfolio equity vs. SPY (normalized to $100k) on the same chart
- **Redesigned KPI grid**: 10 metrics across 2 rows

### Operational
- **`--dry-run` flag**: `python daily_run.py --dry-run` runs the full pipeline without saving state or generating the dashboard. Useful for testing config changes.
- **Failure notifications**: GitHub Actions creates an issue automatically if the daily run fails.

---

## Not Yet Implemented

- **Tax simulation (advanced)**: No wash sale rule detection or capital gains carryforward. Basic short/long estimated tax is now supported.
- **Slippage model**: Entries/exits use closing price with no bid-ask spread or slippage estimate.
- **Additional entry filters**: RSI, MACD, or ATR-based filters to improve signal quality.
- **Profit-taking exit**: No rule to take profits at a target % (e.g., exit if up 25% in 5 days).
- **Monthly P&L breakdown**: Dashboard doesn't show month-by-month performance.
- **Auto-refresh ticker lists**: SECTOR_STOCKS is static; should periodically pull actual ETF holdings.

---

## Setup

```bash
git clone https://github.com/teebuphilip/sector-rotation-trader.git
cd sector-rotation-trader
pip install -r requirements.txt

# Run once to bootstrap 90-day historical state
python seed.py

# Commit the generated state.json
git add state.json docs/
git commit -m "seed: bootstrap 90-day historical state"
git push
```

## Crazy Algos (No-Key Set)

Separate runner for the no‑API‑key “crazy” algos (TSA, Craigslist, 311, LinkedIn PDF, Congress).

```bash
# Seed 90-day history (best-effort; some algos require live data)
python crazy_seed.py

# Daily run (writes per‑algo dashboards + combined overview)
python crazy_run.py
```

Notes:
- LinkedIn algo will use `data/crazy/linkedin_workforce.csv` if present (columns: `date,sector,hire_rate,layoff_rate`). Otherwise it attempts a best‑effort PDF parse and may hold cash if parsing fails.

## Blocked Queue (Missing Keys)

Blocked algos are recorded here:
- `data/blocked/algos.jsonl`

## Daily Crazy Idea Pipeline (Minimal)

Generates one new “crazy idea” from ChatGPT and Claude daily, stores JSON + Markdown, and scores for completeness.

Key files:
- Prompt: `prompts/crazy_ideas_prompt.txt`
- Run artifacts: `data/ideas/runs/YYYY-MM-DD/`
- Published markdown: `docs/ideas/YYYY-MM-DD.md`

GitHub Action:
- `.github/workflows/crazy_ideas_daily.yml`

## Daily Pipeline Email

Script:
- `scripts/daily_stats_email.py`

## 30-Day Rolling Leaderboard

Generated daily by the algo runners and written to:
- `docs/leaderboards/rolling_30d.md`
- `docs/leaderboards/rolling_30d.json`

## Landing Page

CTA landing page (links to the two products + latest winners):
- `docs/landing.html`

## Architecture

Repo layout and workflow overview:
- `architecture.md`

## What This Is (And Isn’t)

This is a public experiment: we run weird alternative‑data trading signals every day, publish the receipts, and refuse to hide the failures. It’s research, not advice. The goal is to see which ugly signals survive real time and which die in public.

What this is:
- A live, timestamped paper‑trading lab
- Daily algo ideas (ChatGPT + Claude) with full specs
- Public ledgers, dashboards, and failure logs

What this isn’t:
- Investment advice
- A promise of performance

If you’re here, you’re either curious, skeptical, or both. That’s the right mindset.

## Algo Biscotti Page

Dedicated page for Algo Biscotti:
- `docs/biscotti.html`

## Algo Baileymol Page

Dedicated page for Algo Baileymol:
- `docs/bailey.html`

## GitHub Pages

1. Go to repo **Settings > Pages**
2. Source: **Deploy from branch**
3. Branch: `main`, folder: `/docs`
4. Dashboard URL: `https://teebuphilip.github.io/sector-rotation-trader/`

## GitHub Actions

Runs automatically at **6:30 PM ET Mon-Fri** after market close.

Manual trigger: **Actions > Daily Sector Rotation Run > Run workflow**

---

## Files

| File | Purpose |
|------|---------|
| `config.py` | All tunable parameters (capital, signals, risk limits) |
| `scanner.py` | Sector ETF momentum scan + stock leadership filter + `safe_download()` helper |
| `signals.py` | Entry (BB + volume + breakout) and exit (20MA + stop-loss) logic |
| `portfolio.py` | State management: cash, margin, positions, P&L, analytics |
| `dashboard.py` | HTML dashboard generator (equity curve, drawdown, SPY overlay) |
| `daily_run.py` | Main daily orchestration script (supports `--dry-run`) |
| `seed.py` | One-time 90-day historical bootstrap |
| `state.json` | Live portfolio state (auto-committed daily) |
| `docs/index.html` | Dashboard (served via GitHub Pages) |
| `docs/trades.json` | Full trade log (consumed by dashboard) |

## Config Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `STARTING_CASH` | $100,000 | Base portfolio cash |
| `MAX_POSITION_SIZE` | $10,000 | Max $ per trade |
| `MAX_BORROW` | $100,000 | Max margin borrowing |
| `BORROW_RATE_ANNUAL` | 8.5% | Annual margin interest rate |
| `STOP_LOSS_PCT` | 8% | Hard stop-loss per position |
| `MAX_DRAWDOWN_PCT` | 15% | Portfolio drawdown circuit breaker |
| `MAX_POSITIONS_PER_SECTOR` | 5 | Max open positions per sector |
| `BREAKOUT_LOOKBACK` | 10 days | Price breakout window |
| `VOLUME_MULT` | 1.5x | Volume surge threshold |
| `BB_PERIOD` / `BB_STD` | 20 / 2.0 | Bollinger Band parameters |
| `EXIT_MA_PERIOD` | 20 days | Exit moving average |
| `EXIT_CONSEC_DAYS` | 2 | Consecutive closes below MA to exit |

## Sector ETF Map

| ETF | Sector | Top Holdings Tracked |
|-----|--------|----------------------|
| XLK | Technology | AAPL, MSFT, NVDA, AVGO, ORCL... |
| XLV | Healthcare | UNH, JNJ, LLY, ABBV, MRK... |
| XLF | Financials | BRK-B, JPM, V, MA, BAC... |
| XLY | Consumer Discretionary | AMZN, TSLA, HD, MCD, NKE... |
| XLI | Industrials | GE, RTX, CAT, HON, UNP... |
| XLC | Communication | META, GOOGL, NFLX, DIS... |
| XLP | Consumer Staples | PG, KO, PEP, COST, WMT... |
| XLE | Energy | XOM, CVX, COP, EOG, SLB... |
| XLB | Materials | LIN, APD, SHW, FCX, NEM... |
| XLRE | Real Estate | PLD, AMT, EQIX, CCI, PSA... |
| XLU | Utilities | NEE, DUK, SO, D, AEP... |
