# StockArithm Lab Report: May 13, 2026 — Sector Rotation Signals Remain Cautious

The StockArithm paper-trading lab is running 234 sector rotation signals across 105 tickers, testing whether economic leading indicators can systematically predict sector outperformance. Today's results show a sharp divergence: one signal is beating the broad market, while the consensus across all sectors has turned decidedly bearish.

## The Winner: Simple Monthly Rotation

**Quantified Simple Monthly Rotation** continues to lead the force-ranked leaderboard with a 1.91% alpha advantage over SPY year-to-date. After 99 days of live paper trading, the signal has returned 10.87% versus SPY's 8.95%—a 192 basis point outperformance. Over the trailing 30 days, it has extended that lead with a 10.87% return and a Sharpe ratio of 5.21, suggesting the signal is capturing both magnitude and consistency.

The economic thesis here is straightforward: monthly rebalancing across sector rotation rules, without complexity, has outperformed more elaborate momentum and dual-momentum frameworks. This is a validation that simpler systematic approaches to sector timing can work when anchored to disciplined rebalancing discipline.

## The Failure: Baileymol's Reversal

Conversely, **Algo Baileymol (Chaos Monger)** has become the lab's most instructive failure. Once ranked 223rd, it has now fallen to 234th—dead last—with a -6.22% YTD return and -1.34% alpha. This is the "failure of the day" precisely because the lab publishes these losses openly. Baileymol's recent 30-day performance (+1.87%, rank 11) shows a brief recovery, but the full-window damage is substantial. The signal's underlying thesis—whatever chaos-driven rotation logic it employs—has not held up under live market conditions.

## Sector Consensus: Broad Bearish Tilt

Across all 42 signals covering sector rotation, the consensus is uniformly cautious. Industrials (XLI) shows the highest bullish conviction at only 29%, yet still registers as BEARISH in composite scoring (12 of 42 signals bullish). Consumer Defensive (XLP), Technology (XLK), Basic Materials (XLB), and Consumer Cyclical (XLY) all fall below 25% bullish, with XLY at just 13%.

This suggests the lab's leading-indicator framework—drawing from economic data like mobility indices, consumption patterns, and volatility structure—is currently signaling defensive positioning or sector underweight across the board. No sector has achieved bullish consensus, which is itself a signal: the lab is not finding strong economic confirmation for cyclical rotation at this moment.

## Notable Divergence: VIX-Based Signals

Two volatility-structure signals show an interesting pattern: **VIX Term Structure** (rank 2 in 30-day, rank 229 full-window) and **VIX Fear Rotation** (rank 3 in 30-day, rank 233 full-window) are performing well recently but have underperformed year-to-date. This suggests that fear-based sector rotation has worked tactically in the past month but has been a drag on longer-term positioning—a classic case of mean reversion or regime shift.

## The Takeaway

StockArithm's lab is transparent about both wins and losses. Simple monthly rotation is working; chaos-driven approaches are not. Sector consensus is bearish across the board. The divergence between 30-day and full-window performance hints at a market regime that may be shifting away from the economic signals that worked earlier in the year.

Full signal methodology and sector consensus at stockarithm.com.