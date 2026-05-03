# StockArithm Lab Report: May 1, 2026 — One Winner, Zero Momentum Survivors

**The Setup**

We're running 158 live paper-trading signals across 105 tickers, each built on alternative data sources: FRED macroeconomic feeds, TSA passenger flows, Reddit sentiment, job openings, VIX term structure, electricity consumption, Google Trends. The lab publishes both wins and losses. Today's report exposes a hard truth: in the rolling 30-day window, *zero algos are beating SPY*. Over the full window (88 days live), only one is.

**Force Rank vs. Rolling 30D: Why We Report Both**

We track two leaderboards because they answer different questions:

1. **Force rank** (full-window cumulative): Which signals have the most persistent edge since launch? This is your long-term signal quality metric.
2. **Rolling 30D**: Which signals are *currently* working? This catches regime shifts and recent momentum.

The divergence between them is the story today.

**The Numbers**

- **Force rank**: 158 algos tracked. Baileymol (Chaos Monger) is the sole outlier: +6.87% YTD, +1.1% alpha vs. SPY's +5.77%. Everyone else is underwater or barely treading water. Faber Momentum Rotation: +3.88%. Antonacci Dual Momentum Sector Rotation: +3.77%. The tail is brutal—VIX Fear Rotation sits at rank 158 with -6.79% YTD.

- **Rolling 30D**: SPY returned +9.98% in the last month. The top five algos returned 2.3% to 4.7%—all *negative alpha*. VIX Term Structure leads at +4.68% (Sharpe 3.73), but that's still -5.3% behind SPY. Baileymol (normal variant) is second at +4.31%, -5.67% delta. Even the "winners" are lagging.

- **The spread**: 1 of 158 beating SPY full-window. 0 of 159 beating SPY in the last 30 days. This is not a statistical anomaly—it's a regime where mean-reversion and momentum strategies are getting hammered by a sustained rally.

**Notable Divergences**

Three algos show extreme rank gaps between force and rolling windows:

- **VIX Term Structure**: Rank 156 full-window (YTD -5.1%), but rank 1 rolling 30D (+4.68%). This is a recent reversal, not a persistent edge.
- **Algo Biscotti**: Rank 155 full-window (-3.13% YTD), rank 4 rolling 30D (+2.67%). Same pattern.
- **Chaos Rotation Lab**: Rank 157 full-window (-5.98% YTD), rank 5 rolling 30D (+2.37%).

These gaps highlight the danger of short-window backtests. A 30-day hot streak doesn't validate a strategy that's been underwater for three months.

**Sector Consensus**

Across 34 sector-rotation signals, only 29% are bullish on Technology (XLK). Consumer Cyclical (XLY): 23% bullish. Basic Materials, Industrials, Consumer Defensive all sub-20%. The lab's consensus is decisively bearish—yet SPY rallied 10% anyway. This is a data point on signal decay or regime mismatch.

**What This Means**

Sample size: 88 days. Not statistically significant. One winner could be luck. The lab's value isn't the returns—it's the transparency. We're publishing failures (VIX Fear Rotation, Electricity Consumption) alongside the one success. We're naming the data sources (FRED, TSA, Reddit, job openings, VIX). We're showing you the rank gap problem: recent performance ≠ edge.

The quant takeaway: alternative data signals are underperforming a simple long-SPY hold in a strong bull regime. Whether that's signal decay, regime shift, or sample noise is the question the next 88 days will answer.

**Methodology and full leaderboard at stockarithm.com.**