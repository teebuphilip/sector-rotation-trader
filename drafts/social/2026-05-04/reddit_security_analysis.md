# StockArithm Lab: May 4 Report — Sector Rotation Signals Broadly Bearish as Baileymol Leads

The StockArithm paper-trading lab published its May 4 signal report across 179 sector rotation algorithms tracking 105 tickers. The headline: only one algorithm beat SPY's 5.39% return over the 92-day window, and the sector consensus across all leading-indicator signals is decidedly bearish.

## The Macro Setup

StockArithm tests a core thesis: economic leading indicators—freight tonnage, electricity consumption, TSA checkpoints, yield curve positioning, volatility structure—should predict sector rotation before price moves. The lab publishes both wins and losses to validate whether these signals actually work.

Today's results suggest the indicators are flashing caution.

**Sector consensus is uniformly defensive.** Technology (XLK) shows the highest bullish signal penetration at 35%, but that still translates to only 11 of 31 algorithms bullish—a bearish composite. Consumer Defensive (XLP), Utilities (XLU), Industrials (XLI), and Energy (XLE) all register 14–21% bullish agreement. This is not a market rotated toward growth or cyclicals; it's a market where leading indicators are warning of contraction or sideways consolidation.

## Performance Divergence: Recent vs. Full-Window

The most interesting tension in today's report is between long-term and recent performance.

**Algo Baileymol (Chaos Monger)** ranks #1 on force (full-window alpha: +1.41%, YTD: +6.79%) and also dominates the rolling 30-day leaderboard with +5.34% return and a 2.84 Sharpe ratio. This is the rare case where a signal is working both in-sample and out-of-sample. Its outperformance versus SPY over 30 days: –3.63%, meaning it's capturing something the broad market isn't.

Conversely, **VIX Term Structure** and **Chaos Rotation Lab** (a Baileymol variant) rank 177th and 178th on full-window force but place 3rd and 2nd on rolling 30-day returns. Both are up ~3.8% in the last month despite being down 5–6% year-to-date. This suggests a recent regime shift—possibly a flight to volatility hedges or a tactical mean-reversion bounce—that contradicts their longer-term thesis.

**Algo Biscotti (Unconditional Loyalty)** sits at rank 175–176 on force (down 3.4% YTD) but ranks 5th over 30 days with +2.26% return. Again, recent performance is decoupling from the full-window signal.

## The Failures

At the bottom: **VIX Fear Rotation** (rank 179, –7.0% YTD, –12.39% alpha) and **Truck Tonnage Index** / **Freight Rail Carloads** (both negative over 30 days, suggesting logistics weakness). These are economic leading indicators that should predict cyclical demand. Their failure to generate positive returns implies either (a) the economic slowdown they're signaling hasn't yet priced into equities, or (b) the relationship between tonnage/carloads and equity returns has broken down.

## What This Means

The lab is testing whether macro leading indicators can systematize sector rotation. Today's report shows:

1. **Consensus is bearish across all major sectors**, with Technology (the highest conviction) still only 35% bullish.
2. **One algorithm beat SPY**—a low hit rate that underscores the difficulty of timing sector rotation.
3. **Recent performance is diverging sharply from full-window results**, suggesting either a tactical bounce or a regime change that the longer-term signals haven't yet captured.
4. **Economic tonnage and freight signals are failing**, which may indicate either a lag in price discovery or a structural break in the indicator relationship.

This is not a lab claiming victory. It's publishing the data: most sector rotation signals are underwater, the consensus is defensive, and the economic leading indicators that should predict growth are flashing red.

Full signal methodology and sector consensus at stockarithm.com.