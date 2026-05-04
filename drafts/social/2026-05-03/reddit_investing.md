# One Signal Beat SPY This Month. Here's What It Measures.

We're running 167 signals across 105 tickers at StockArithm—a public paper-trading lab that publishes results, wins *and* losses. Today's snapshot is interesting because it shows exactly what happens when most signals fail.

## The Setup

These aren't black-box "AI" systems. Each signal measures something concrete: sector rotation based on economic data, momentum shifts, volatility structure, alternative data like job postings or electricity consumption. We rank them all on a 30-day rolling window and a full-window "force rank" to catch both recent winners and consistent performers.

SPY returned **9.98%** over the last 30 days. Out of 168 signals tracked in that window, **zero beat it**. That's a failure worth publishing.

## The One Winner

**Algo Baileymol (Chaos Monger)** is the only signal beating SPY on the full-window force rank. It returned **6.87% YTD** vs SPY's 5.77%, a **+1.1% alpha**. Over 30 days it pulled **4.55%** while SPY climbed 9.98%—so it's underperforming recently, but it's still the least-bad performer in a month where almost everything lagged.

Sharpe ratio: 3.03. Max drawdown: -2.07%.

## The Failures

**VIX Fear Rotation** is the worst: **-6.79% YTD**, ranked dead last at 167. **Algo Biscotti** (both variants) is down **-2.83% to -3.13%**. These aren't edge cases—they're live experiments showing what doesn't work.

Here's the weird part: **VIX Term Structure** ranks 165th on force (down 5.1% YTD) but **2nd on the 30-day leaderboard** with 4.28% returns. Same with **Biscotti**—it's 164th overall but 5th in the last month. This gap matters. It suggests recent market conditions favor volatility-based signals, but they haven't proven durable.

## What the Signals Measure

- **Sector rotation**: Momentum shifts across XLK, XLY, XLI, XLU, XLP
- **Economic data**: Electricity consumption, job openings (Google Trends), FINRA dark pool activity
- **Volatility structure**: VIX term curve slopes
- **Simple rules**: Monthly rebalancing, dual momentum

**Sector consensus today**: Technology (XLK) is the only mixed signal at 39% bullish. Everything else is bearish—Utilities, Consumer Defensive, Industrials, and Consumer Cyclical all under 21% bullish.

## The Point

Most signals are losing. One is barely winning. The lab publishes both because that's how you learn what actually works. No hype, no promises—just 89 days of live results on 167 different bets.

Everything is public at stockarithm.com.