# Sector Rotation Lab: Simple Monthly Outperforms as Consensus Tilts Defensive

StockArithm's paper-trading lab is publishing results for May 8, 2026. Of 202 active signals across 105 tickers, only one is beating SPY year-to-date. The macro picture is mixed—and the data shows why.

## The Winner: Simplicity Over Complexity

**Quantified Simple Monthly Rotation** leads the force-ranked leaderboard with +10.03% YTD and +1.77% alpha versus SPY's +8.27%. Over the past 30 days, it returned 10.03% with a Sharpe ratio of 5.15 and minimal drawdown (−0.20%). The signal is straightforward: rotate monthly across sectors based on relative strength. No exotic indicators. No chaos.

This matters because it validates a core thesis: sector rotation driven by systematic rebalancing can outperform broad-market buy-and-hold, even in a rising market. The economic rationale is simple—momentum persistence within monthly windows—and the paper-trading results confirm it works in this regime.

## The Failures: Chaos and Fear Don't Translate

At the bottom of the leaderboard, **Algo Biscotti** (−3.94% YTD, −12.21% alpha) and **VIX Fear Rotation** (−3.20% YTD, −11.46% alpha) are underwater. Both are "crazy" category algos—meaning they test unconventional leading indicators. Biscotti's 30-day Sharpe is −1.12. VIX Fear Rotation's is −3.38 over 30 days, despite ranking #3 on the rolling leaderboard.

This reveals a critical divergence: fear-based and volatility-driven signals are whipsawing. VIX Term Structure ranks #2 over 30 days (+7.61%) but sits at force rank 197 (−1.45% YTD). The lab is publishing these failures openly because they matter—they show that short-term tactical wins in volatility signals don't persist into medium-term alpha.

## Sector Consensus: Defensive Skepticism

The sector consensus reflects caution. Technology (XLK) is the only sector with mixed sentiment (41% bullish, 13 of 32 signals). Consumer Defensive (XLP), Utilities (XLU), Basic Materials (XLB), and Industrials (XLI) are all bearish—19%, 18%, 16%, and 14% bullish respectively.

This is the macro thesis test: if leading indicators are signaling economic slowdown or rotation away from growth, we'd expect defensive sectors to show stronger signal consensus. Instead, they're weak. That suggests either (1) the slowdown narrative is overstated, or (2) the lab's leading indicators aren't yet capturing the shift. Both are worth monitoring.

## What This Means

One algo beating SPY across 202 signals is not a bullish signal. It's a reality check. The lab's job is to test whether economic leading indicators—TSA checkpoints, mortgage rates, retail sales, mobility indices—can predict sector rotation. Most aren't working. The ones that are (simple monthly rebalancing) succeed because they're disciplined, not clever.

The divergences matter too: Baileymol jumped from rank 202 to rank 10 in 30 days, then fell back. That's noise, not signal. The lab publishes it anyway.

**Full signal methodology and sector consensus at stockarithm.com.**