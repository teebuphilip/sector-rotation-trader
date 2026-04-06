# Sector Rotation Trader

Paper trading system implementing the sector rotation strategy from NRWise / DataDrivenInvestor.

**Rules:**
- $100k base capital, $10k max per position
- Up to $100k additional margin when fully deployed and signal fires
- 8.5% annual margin rate (daily accrual)
- Sector scan daily: leading SPDR ETF by 3M-6M performance spread
- Entry: price > 10-day high + volume > 150% of 20-day avg + BB expanding
- Exit: 2 consecutive closes below 20-day MA

**Simulation window:** 6 months live tracking (seeded with 90 days historical)

---

## Setup

```bash
git clone <your-repo>
cd sector-rotation-trader
pip install -r requirements.txt

# Run once to bootstrap 90-day historical state
python seed.py

# Commit the generated state.json
git add state.json docs/
git commit -m "seed: bootstrap 90-day historical state"
git push
```

## GitHub Pages

1. Go to repo **Settings → Pages**
2. Source: **Deploy from branch**
3. Branch: `main`, folder: `/docs`
4. Dashboard URL: `https://<you>.github.io/<repo>/`

## GitHub Actions

Runs automatically at **6:30 PM ET Mon–Fri** after market close.

Manual trigger: **Actions → Daily Sector Rotation Run → Run workflow**

---

## Files

| File | Purpose |
|------|---------|
| `config.py` | All tunable parameters |
| `scanner.py` | Sector ETF momentum scan + stock leadership filter |
| `signals.py` | Entry (BB + volume + breakout) and exit (20MA) logic |
| `portfolio.py` | State management: cash, margin, positions, P&L |
| `dashboard.py` | HTML dashboard generator |
| `daily_run.py` | Main daily orchestration script |
| `seed.py` | One-time 90-day historical bootstrap |
| `state.json` | Live portfolio state (auto-committed daily) |
| `docs/index.html` | Dashboard (served via GitHub Pages) |
| `docs/trades.json` | Full trade log (consumed by dashboard) |

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
