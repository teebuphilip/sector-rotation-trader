# StockArithm Lab Report: May 15, 2026 — One Signal Beating SPY, Sector Consensus Broadly Bearish

The StockArithm paper-trading lab is running 266 sector rotation signals across 105 tickers. As of today, exactly one is beating SPY year-to-date: **Quantified Simple Monthly Rotation**, which has delivered 10.5% against SPY's 8.49%—a 2.0% alpha advantage over 101 days of live trading.

## The Winner: Simplicity Over Complexity

The outperforming signal uses straightforward monthly sector rotation mechanics. No exotic indicators, no chaos-driven positioning. It ranks first on both the full-window force leaderboard and the rolling 30-day performance window, posting a 10.5% return in the past month alone (4.9% ahead of SPY's 5.6% move). The Sharpe ratio of 4.51 over 30 days reflects consistent execution with minimal drawdown—a 1.8% peak decline.

This matters because it tests a fundamental thesis: *Does systematic monthly rebalancing across sectors, driven by economic leading indicators, outperform buy-and-hold?* The data says yes, at least in this 101-day window. The economic rationale is straightforward—sectors rotate on measurable macro cycles, and monthly rebalancing captures those turns without overtrading.

## The Failures: Transparency as Differentiator

The lab publishes losses as openly as wins. **Algo Biscotti (Unconditional Loyalty)** is down 3.17% YTD and ranks 263rd out of 266. **VIX Fear Rotation** is down 4.04% YTD and ranks 264th overall—yet it ranks 2nd on the rolling 30-day leaderboard, up 5.2% in the past month. This divergence is instructive: a signal that works recently but has failed over the full window suggests either regime change or overfitting to current volatility conditions.

The lab flags this explicitly. When a signal ranks 264th all-time but 2nd in the last 30 days, that's a 262-rank gap worth examining. It suggests the signal may be capturing a temporary market condition rather than a durable economic relationship.

## Sector Consensus: Broad Bearish Tilt

Across 266 signals, the sector consensus is decidedly defensive. Industrials (XLI) show the highest bullish conviction at 30%—still a minority view. Technology (XLK), Consumer Defensive (XLP), Basic Materials (XLB), and Consumer Cyclical (XLY) all register below 20% bullish. This alignment across multiple independent signals suggests the lab's leading indicators are pointing toward economic caution: slower growth, tighter financial conditions, or demand softening.

The economic rationale: if TSA checkpoint counts, initial jobless claims, and yield curve positioning are all signaling contraction risk, sector rotation should favor defensive positioning. The consensus reflects that thesis.

## What This Means

One signal beating SPY in a 266-signal lab is not a marketing claim—it's a baseline. The real insight is *why* it works (monthly rebalancing on macro cycles) and *why* most others don't (complexity without predictive edge). The lab's transparency about failures—Biscotti down 3%, VIX Fear Rotation's recent strength masking full-window weakness—is the differentiator.

Full signal methodology and sector consensus at stockarithm.com.