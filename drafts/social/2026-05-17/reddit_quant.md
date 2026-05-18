# StockArithm Lab Report: 266 Algos, 1 Beating SPY—And Why That Matters

We're 101 days into live paper trading across 266 algorithmic signals covering 105 tickers. One algo is beating SPY on force rank. One is also leading the rolling 30-day leaderboard. The rest are underwater or treading water. This is the report.

## The Brutal Spread

**Force rank (full-window since seed):** 266 algos tracked. SPY returned 8.49% YTD. Only **Quantified Simple Monthly Rotation** (+10.5%, +2.0% alpha) cleared that bar. The next 265 are negative alpha or flat. The bottom quartile is down 2–12% YTD while the market rallied.

**Rolling 30-day momentum:** Same story. SPY gained 5.6% in the last month. **Simple Monthly** led at +10.5% (Sharpe 4.51). **VIX Fear Rotation** and **VIX Term Structure**—both ranked 264th and 260th on force rank—posted 5.2% and 4.7% respectively over 30 days. That's the divergence we're watching: mean reversion or regime shift? Too early to call.

The bottom three 30-day performers (Copper Momentum, Port Container Volume, Lumber Momentum) all went negative, lagging SPY by 7–8 percentage points.

## Why We Report Both Rankings

Force rank measures consistency over 101 days. Rolling 30D captures recent momentum. They tell different stories. **Algo Biscotti** exemplifies this: ranked 262nd overall (down 3.17% YTD) but 9th in the last 30 days (+2.3%). Is it recovering or noise? The data doesn't yet say. Sample size is the killer here—101 days is not statistically significant for any claim about edge. We're publishing it anyway because the methodology is transparent and the failures are real.

## Data Sources & Methodology

Signals derive from standard momentum rotations (Faber, Antonacci dual momentum), alternative data (TSA mobility, port container volume, lumber futures, copper), and volatility structure (VIX term curve). Each algo runs daily on paper. No transaction costs modeled. No slippage. That's a known bias toward the long side.

## The Honest Critique

- **N = 101 days.** Not significant. Luck and regime dominate signal.
- **266 algos, 1 winner.** That's a 0.4% hit rate. Survivorship bias is baked in—we're not showing the algos that were killed mid-run.
- **No cost model.** Real trading would bleed 5–15 bps per rebalance. Many of these algos would flip negative.
- **Sector consensus is bearish across the board** (Industrials 30% bullish, Tech 19%, Defensive 18%). The lab's algos are not contrarian; they're following the same signals. That's a concentration risk.

## What We're Actually Testing

The point is not to claim an edge. It's to publish the methodology, the leaderboard, and the failures in real time. **Simple Monthly** is winning. **Biscotti** is losing. **VIX Fear Rotation** is a rank-gap anomaly worth monitoring. These are observations, not predictions.

Methodology and full leaderboard at stockarithm.com.