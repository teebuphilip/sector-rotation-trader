# StockArithm Lab Report: 97 Days In, 1 Algo Beating SPY

We're running 215 live paper-trading signals across 105 tickers. After 97 days, exactly one algorithm is outperforming SPY on a force-ranked (full-window) basis. That's the headline. Here's what the data actually says.

## The Spread

**Force rank (seed-to-date):** 1 of 215 algos beating SPY. Quantified Simple Monthly Rotation is up 11.51% YTD vs. SPY's 8.51%—a 3.0% alpha. The next 214 are underwater or barely treading water. Baileymol (Chaos Monger) sits at rank 215 with -6.22% YTD, a -14.73% alpha. This is not a typo. We publish failures.

**Rolling 30-day momentum:** 1 of 216 algos beating SPY over the last month. Same winner: Simple Monthly Rotation, +11.51% vs. SPY's +7.75%, Sharpe 6.01. But the 30D window reveals something the full-window ranking obscures: mean reversion and regime shifts. VIX Fear Rotation ranks 212 force-rank but 3rd in rolling 30D (+5.88%, Sharpe 4.99). VIX Term Structure: 209th force-rank, 2nd in 30D (+7.26%, Sharpe 5.78). These are not statistical flukes—they're real divergences worth naming.

## Why Both Rankings Matter

Force rank answers: "What works over the entire live period?" Rolling 30D answers: "What's working *now*?" The gap between them is signal. Baileymol's 204-rank gap (215 force vs. 11 rolling 30D) suggests recent mean reversion after a brutal drawdown. That's testable. VIX-based algos show the opposite pattern: they've been dead weight historically but are capturing current regime dynamics.

## Sample Size Caveat

97 days is not statistically significant. We have ~4.5 months of live paper trading. The standard error on a single algo's alpha is enormous at this N. Sharpe ratios above 6.0 are suspicious without out-of-sample validation. We're not claiming edge—we're publishing methodology and letting the market judge.

## Data Sources & Coverage

Signals derive from FRED macroeconomic data (retail sales, housing permits, mortgage rates), TSA mobility indices, Reddit sentiment aggregates, job openings (JOLTS), VIX term structure, and sector ETF consensus. 105 tickers span large-cap equities. No alternative data licensing claims. No black-box ML. Rebalance frequency varies by algo (monthly rotation, momentum-based, sector rotation).

## The Honest Read

The lab is a failure factory by design. Electricity Consumption ranks 211th (-10.65% alpha). Liquor Store Leading Indicator ranks 214th (-9.16% alpha). These aren't hidden in a private dashboard—they're public. The point is not to find the one winner and sell it; the point is to test whether alternative data and systematic rebalancing can generate alpha, and to show the distribution of outcomes when you don't cherry-pick.

One algo beating 214 others over 97 days is not an edge. It's a baseline. The methodology is the product.

Methodology and full leaderboard at stockarithm.com.