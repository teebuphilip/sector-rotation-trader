# StockArithm Lab Report: 2026-05-19 — 3 of 292 Algos Beating SPY

We're running 292 signals across 105 tickers in live paper trading. Today's snapshot: **3 algos are beating SPY on force rank (full-window since seed), 2 on rolling 30D momentum.** That's a 1% win rate on the full window. The lab publishes failures as loudly as wins. Here's what the data shows.

## The Leaderboard Split

**Force Rank (103 days live):** Quantified Simple Monthly Rotation leads with +8.6% YTD and +0.91% alpha over SPY's +7.69%. Algo Baileymol (Chaos Monger) jumped 276 positions to rank #2 with +0.54% alpha—a dramatic reversal from rank 278 last period. Faber Momentum Rotation holds #3 with +0.07% alpha. Below that, the spread widens fast. Antonacci Dual Momentum Sector Rotation is already underwater at -1.64% alpha. The bottom tier—Copper Momentum, Port Container Volume, VIX Fear Rotation—are down 3–5% YTD.

**Rolling 30D Momentum:** A different story. Simple Monthly still leads (Sharpe 3.90, +8.6% in 30D). Faber ranks #2 (Sharpe 4.09, +3.77%). But VIX Fear Rotation—which sits at force rank 290 and -5.15% YTD—ranks #3 on the 30D window with +2.8% return and Sharpe 1.65. This is the divergence worth watching: some algos are recovering hard in the last month despite catastrophic full-window performance.

## Why Both Rankings Matter

We report force rank and rolling 30D because they answer different questions. Force rank measures consistency over the entire backtest window (103 days for most algos). Rolling 30D captures momentum and regime shifts. When they diverge sharply—like VIX Fear Rotation's 287-position gap—it signals either mean reversion or a structural break in the signal's underlying data source.

## The Honest Limitations

**Sample size:** 103 days of live paper trading is not statistically significant. A single month of outperformance (or underperformance) can reverse. Sharpe ratios above 3.0 are suspicious at this horizon; they suggest either genuine edge or overfitting to recent market conditions. We're flagging this explicitly because the quant audience will ask it first.

**Data sources:** Algos draw from FRED (economic releases), TSA (mobility), Reddit sentiment, job openings, freight rail carloads, copper futures, VIX term structure, and sector rotation mechanics. Some are standard (Simple Monthly, Faber, Dual Momentum). Others are experimental ("crazy" type)—commodity momentum, port container volume, VIX-based rotations. The experimental cohort is underperforming badly. That's not a bug; it's the point. We test them publicly and show the losses.

**Sector consensus:** Across 48 algos voting on Utilities (XLU), only 25% are bullish. Technology (XLK) is 20% bullish. The lab is broadly bearish across all major sectors. This is a signal, not a recommendation.

## What We're Not Saying

We're not claiming edge. We're not predicting where markets go. We're showing methodology: signal generation, ranking systems, live results, and failures. Three algos beat SPY. 289 don't. That's the data.

Methodology and full leaderboard at stockarithm.com.