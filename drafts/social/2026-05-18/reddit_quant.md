# StockArithm Lab Report: 278 Algos, 1 Beating SPY—And Why That Matters

We're 102 days into live paper trading across 278 algorithmic signals covering 105 tickers. One algo is beating SPY on force rank. One on rolling 30D. The spread is brutal. This is the point.

## The Leaderboard State

**Force rank (full-window since seed):** Quantified Simple Monthly Rotation leads with +9.31% YTD vs. SPY's +8.42%, generating +0.89% alpha. Behind it: Baileymol at +8.04% (−0.37% alpha), Faber at +7.59% (−0.82%), Antonacci Dual Momentum Sector Rotation at +6.23% (−2.19%). At the bottom: Algo Biscotti at −2.75%, VIX Term Structure at −2.81%, VIX Fear Rotation at −4.53%.

**Rolling 30D momentum:** Simple Monthly again ranks #1 with +9.31% over the last month (Sharpe 4.35), +5.08% ahead of SPY's +4.22%. Faber ranks #2 at +3.61% (Sharpe 3.98). But Copper Momentum, Lumber Momentum, and Port Container Volume are down −2.06%, −2.08%, and −2.49% respectively over the same window.

**The critical fact:** 277 of 278 algos are underperforming SPY on force rank. 278 of 279 on rolling 30D. This is not a marketing problem. This is the data.

## Why We Report Both Rankings

Force rank measures consistency over the full 102-day window—signal stability. Rolling 30D captures recent momentum shifts. They diverge sharply. Algo Biscotti sits at force rank 274 but rolling 30D rank 11, a 261-position gap. VIX Fear Rotation: force rank 276, rolling 30D rank 3 (273-position gap). These divergences flag regime changes or mean reversion. They're worth studying, not hiding.

## The Honest Limitations

102 days is not statistically significant. One algo beating SPY across 278 independent signals is consistent with random noise at this sample size. The lab does not claim predictive edge. We claim transparency: every signal, every loss, every failure published in real time.

The sector consensus today is uniformly bearish—Technology (XLK) at 25% bullish, Energy (XLE) at 15%. This reflects algos trained on FRED macroeconomic data, TSA mobility indices, Reddit sentiment, job openings, and volatility term structure. No single data source dominates. No algo is "proprietary." The methodology is reproducible.

## What Matters Here

The differentiator is not returns. It's that we publish the 277 failures as loudly as the 1 winner. Baileymol is flagged as "FAILING" with −6.12% YTD. Copper Momentum and Lumber Momentum are down −2.06% and −2.08% in the last 30 days. These are live, not backtested, not cherry-picked.

For quants and academics: this is a live laboratory for signal decay, regime sensitivity, and the cost of overfitting. For practitioners: it's a reminder that most alternative-data signals don't work. The ones that do are worth reverse-engineering.

**Methodology and full leaderboard at stockarithm.com.**