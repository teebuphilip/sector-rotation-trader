# StockArithm Lab Report: 266 Algos, 1 Beating SPY—And Why That Matters

We're 101 days into live paper trading across 266 algorithmic signals covering 105 tickers. One algo is beating SPY on force rank. One is also leading the 30-day rolling window. The rest are underwater or treading water. This is the report.

## The Spread

**Force rank (full-window since seed):** 1 of 266 algos beating SPY.  
**Rolling 30D:** 1 of 267 algos beating SPY.  
**SPY YTD return:** 8.49%.

Quantified Simple Monthly Rotation sits at +10.5% YTD, +2.0% alpha. Baileymol (Chaos Monger) ranks #2 on force return but trails SPY by 20 bps. Faber Momentum Rotation, Antonacci Dual Momentum Sector Rotation, and Uber Mobility Index round out the top five—all negative alpha.

At the bottom: Algo Biscotti (both variants) and VIX Fear Rotation are down 2–4% YTD, with alpha ranging from −11.4% to −12.5%. These are live failures. We publish them.

## Two Ranking Systems, Two Stories

We report both force rank (cumulative return since inception) and rolling 30D momentum because they answer different questions.

**Force rank** answers: "Which signal has actually made money over the full test window?" Answer: almost none.

**Rolling 30D** answers: "Which signals are working *right now*?" This reveals regime sensitivity. VIX Fear Rotation ranks #264 on force but #2 on 30D—a 262-rank gap. It returned 5.17% in the last month while SPY returned 5.60%, but its full-window YTD is −4.04%. Biscotti shows similar divergence: rank 262 force, rank 9 rolling 30D. These algos are recent performers in a market that has not favored their historical logic.

## Data Sources & Methodology

Signals draw from FRED macroeconomic data, TSA mobility indices, Reddit sentiment aggregates, job openings (JOLTS), VIX term structure, commodity momentum (copper, lumber), and port container volume. Each algo generates a daily signal across its covered universe. We rank by total return, Sharpe ratio (30D), and maximum drawdown.

## The Honest Critique

**Sample size:** 101 days is not statistically significant. One algo beating SPY over ~3 months could be luck. Sharpe ratios computed on 30 days are noisy. Drawdown estimates on rolling windows are unstable. We know this. You should too.

**Survivorship:** We're not filtering. Failed algos stay live and ranked. Biscotti's −11.66% alpha is real and public.

**Sector consensus:** Across 46 algos covering Industrials (XLI), only 30% are bullish. Technology (XLK): 19% bullish. Consumer Defensive (XLP): 18%. The lab is broadly bearish, and it's losing money.

## What This Tells Us

The edge, if it exists, is narrow and regime-dependent. Simple Monthly Rotation works. Everything else is noise or drawdown. The VIX-based algos are catching a recent volatility dislocation but have bled capital over the full window. Commodity momentum (Copper, Lumber) is deeply underwater.

This is not a marketing report. It's a transparency report. The methodology works because we show losses as clearly as wins.

Methodology and full leaderboard at stockarithm.com.