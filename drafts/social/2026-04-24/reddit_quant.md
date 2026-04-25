# StockArithm Lab Report: 2026-04-24 — Two Algos Beat SPY, 131 Did Not

We're running 133 signals across 105 tickers in live paper trading. Today's snapshot: **2 algos are beating SPY on force rank (full-window since seed). Zero are beating SPY on the rolling 30-day window.** This is the data. Here's what it means.

## The Ranking Split

We publish two leaderboards because they answer different questions:

**Force rank** (cumulative since launch ~82 days ago): Baileymol sits at +7.06% YTD with +2.28% alpha over SPY's +4.79%. DMSR (Antonacci Dual Momentum Sector Rotation) is +5.29% YTD, +0.50% alpha. Everyone else trails. This is the long-term persistence question.

**Rolling 30-day momentum**: SPY returned +8.70% in the last month. Baileymol returned +7.87% (−0.83% delta). Biscotti (normal variant) returned +6.68% (−2.02% delta). VIX Term Structure returned +5.08% (−3.62% delta). The 30D window isolates recent regime fit—and right now, nothing is outrunning the broad market on that horizon.

The divergence matters. Faber Momentum Rotation ranks #3 force but #134 rolling 30D (−131 rank gap). It's up 3.85% YTD but down −0.52% in the last month. VIX Term Structure is the inverse: #131 force, #3 rolling 30D (+128 gap). Down −4.88% YTD but up +5.08% in April. These aren't contradictions—they're regime shifts. We show both.

## What's Actually Working

Baileymol (Chaos Monger) is the outlier. It's beating SPY on both metrics. Sharpe of 4.38 over 30 days, max drawdown −1.8%. That's the signal of the day. But: 82 days of live trading is not statistically significant. Confidence interval is wide. We're publishing it because it's real, not because it's predictive.

DMSR is steadier—lower volatility, consistent alpha, but smaller edge. Faber has been solid on the full window but has completely whiffed the recent rally. That's a failure we're naming.

## The Failures

VIX Fear Rotation is the failure of the day: −6.7% YTD, ranked #133. Biscotti (crazy variant) is −2.51% YTD. Electricity Consumption, XLE Weekly Drawdown Rebound Signal, and Daily Spike In Earthquake Activity Near Major Logistics Hubs are all negative on 30D returns. Yes, we're running earthquake signals. Some work. Most don't. We publish both.

## Sector Consensus

Algos are mixed on Technology (XLK, 37% bullish), bearish on everything else. Consumer Cyclical, Utilities, and Industrials all show <25% bullish conviction. This is weak consensus—not a strong directional call.

## The Honest Caveat

133 signals, 82 days of live data, 2 beating SPY. That's a 1.5% hit rate on force rank. On rolling 30D, it's 0%. Sample size is too small to claim edge. Survivorship bias is real—we're not showing dead algos. Overfitting is possible. We're showing this because transparency is the methodology, not because the results are conclusive.

Methodology and full leaderboard at stockarithm.com.