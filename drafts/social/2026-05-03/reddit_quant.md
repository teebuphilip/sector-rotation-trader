# StockArithm Lab Report: 2026-05-03 — One Winner in 167 Algos

We're running 167 signals across 105 tickers in live paper trading. Today's snapshot is instructive precisely because it's brutal: **only 1 algo is beating SPY on force rank (full-window cumulative return since seed), and 0 are beating SPY on the rolling 30-day leaderboard.**

Let's be direct about what that means and what it doesn't.

## The Numbers

**Force Rank (Full Window):**
- Baileymol (Chaos Monger) is +6.87% YTD, +1.1% alpha vs. SPY's +5.77%. That's the sole winner.
- 166 algos are underwater relative to the benchmark.
- Faber Momentum Rotation and Antonacci Dual Momentum Sector Rotation are close behind at +3.88% and +3.77%, but both trail SPY.
- VIX Fear Rotation sits at the bottom: -6.79% YTD, -12.56% alpha.

**Rolling 30-Day (Momentum Window):**
- Baileymol leads at +4.55% (30D), Sharpe 3.03, but SPY returned +9.98% in the same window.
- VIX Term Structure ranks #2 at +4.28% (30D), Sharpe 3.02—yet still -10.88% alpha vs. SPY.
- The entire 30D leaderboard is negative alpha. SPY is dominating the recent period.

This is not a bug report. This is the lab working as designed.

## Why We Show Losses

StockArithm publishes failures publicly because that's where the methodology lives. We're testing alternative data sources—FRED macroeconomic feeds, TSA passenger flows, Reddit sentiment, job openings via Google Trends, FINRA dark pool signals, VIX term structure, electricity consumption—against a live market. Most don't work. Some work in certain regimes and fail in others. A few show promise.

Baileymol's +1.1% alpha over 89 days is not statistically significant. N=89 trading days is a small sample. Volatility clustering, regime shifts, and luck are all plausible explanations. We're not claiming an edge; we're documenting the attempt.

## The Divergence Signal

Three algos show a notable pattern: strong 30D momentum despite weak full-window returns. VIX Term Structure (+4.28% in 30D, Sharpe 3.02) ranks 165th on force rank but 2nd on rolling 30D. Biscotti (Unconditional Loyalty) is -3.13% YTD but +3.09% in the last month. This suggests regime sensitivity—they may be catching a recent market structure that didn't persist earlier in the year.

## Sector Consensus

Across 31 algos covering Technology (XLK), only 12 are bullish (39%). Utilities, Consumer Defensive, Industrials, and Consumer Cyclical all show bearish consensus (14–21% bullish). This is a weak signal environment.

## The Honest Take

One algo beating SPY in a 167-signal lab is a null result. It's consistent with random walk hypothesis. The value here is methodological transparency: you can see the data sources, the sample sizes, the ranking systems (force rank vs. rolling 30D), and the failures. We're not hiding underwater algos or cherry-picking winners.

If you want to audit the methodology, replicate the signals, or propose alternative data sources, the full leaderboard and signal definitions are public.

**Methodology and full leaderboard at stockarithm.com.**