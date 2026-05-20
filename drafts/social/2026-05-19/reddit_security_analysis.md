# Sector Rotation Lab Update: May 19, 2026 — Macro Signals Diverge on Defensive Positioning

StockArithm's paper-trading lab is running 292 sector rotation signals across 105 tickers, and the results reveal a market in transition. Only 3 algos are beating SPY year-to-date, while the 30-day rolling window shows a sharper divergence: simple monthly rotation is outperforming by 507 basis points, yet commodity-linked signals are collapsing.

## The Winners: Simplicity and Momentum Confirmation

**Quantified Simple Monthly Rotation** leads the force-ranked leaderboard with +8.6% YTD and +91 bps of alpha. Over the past 30 days, it's returned 8.6% against SPY's 3.5%, posting a 3.9 Sharpe ratio with minimal drawdown. The economic thesis is straightforward: monthly rebalancing across sector baskets captures rotation without timing noise. In a market where macro signals are mixed, this mechanical discipline is outperforming discretion.

**Algo Baileymol** jumped 276 ranks to #2 force-ranked, now beating SPY with +54 bps of alpha despite a YTD return of 8.23%. This is a notable recovery—the algo was ranked 278th just days ago. **Faber Momentum Rotation** holds steady at #3, with +7 bps of alpha and a 4.1 Sharpe over 30 days.

## The Failures: Commodity Weakness and Fear Signals

The lab publishes losses as clearly as wins. **Copper Momentum** and **Port Container Volume** are down 3.5% and 3.8% YTD respectively, trailing SPY by 700+ basis points. These signals were designed to capture industrial demand via commodity prices and logistics volume—both are signaling contraction. **VIX Fear Rotation**, despite ranking #3 on the 30-day leaderboard, is down 5.15% YTD, a 287-rank gap that suggests recent volatility mean-reversion is masking a longer-term bearish thesis.

## The Divergence: Recent Strength, Full-Window Weakness

Three algos show striking rank gaps between 30-day and full-window performance:

- **VIX Fear Rotation**: +2.8% in 30 days, but -5.15% YTD
- **VIX Term Structure**: +2.66% in 30 days, but -3.44% YTD  
- **Algo Biscotti**: +2.1% in 30 days, but -1.38% YTD

This pattern suggests that fear-based and volatility-structure signals caught a recent tactical bounce but have been wrong on the macro setup for months. The economic rationale—that elevated VIX or inverted term structures predict defensive rotation—has not held.

## Sector Consensus: Broad Bearish Tilt

The lab's sector consensus across all 292 signals shows uniform skepticism. Utilities (XLU) is the "least bearish" at 25% bullish signals, followed by Technology (20%), Industrials (19%), Consumer Defensive (17%), and Basic Materials (15%). No sector has majority bullish conviction. This aligns with the commodity weakness and suggests the lab is pricing in either economic slowdown or persistent rate pressure.

## What This Means

Simple, rebalanced sector rotation is working. Commodity-linked and fear-based signals are not. The lab's macro thesis—that leading indicators like freight, copper, and volatility structure would predict sector rotation—is being tested in real time, and the results are mixed. The winners are those that avoid timing altogether.

Full signal methodology and sector consensus at stockarithm.com.