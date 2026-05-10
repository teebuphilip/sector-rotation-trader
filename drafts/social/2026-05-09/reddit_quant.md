# StockArithm Lab Report: 202 Algos, 1 Beating SPY (Full Window)

We're running 202 signals across 105 tickers in live paper trading. After 96 days, exactly **one algorithm is beating SPY on a force-ranked (full-window) basis**. That's the honest headline. The other 201 are underwater or treading water. This is why we publish the leaderboard publicly.

## The Numbers

**Force Rank (seed-to-date):**
- Total algos: 202
- Beating SPY: 1
- SPY YTD return: 8.27%

**Quantified Simple Monthly Rotation** leads at +10.03% YTD, +1.77% alpha. It's a straightforward monthly rebalance across sector ETFs—no alternative data, no complexity. Baileymol (Chaos Monger) ranks #2 in force return but still trails SPY by 72 bps. Faber Momentum Rotation, Antonacci Dual Momentum Sector Rotation, and Uber Mobility Index round out the top five, all negative alpha.

The bottom tier is worse. Algo Biscotti (Unconditional Loyalty), VIX Fear Rotation, and Electricity Consumption are down 3–4% YTD while SPY climbs. These are the failures we keep running. They're instructive.

## Rolling 30-Day Tells a Different Story

This is where methodology matters. We report two rankings because they answer different questions:

- **Force rank** = cumulative edge (or lack thereof) over 96 days
- **Rolling 30D** = recent momentum, Sharpe, drawdown

Over the last 30 days, Quantified Simple Monthly Rotation again leads (10.03% return, 5.15 Sharpe). But VIX Term Structure ranks #2 at +7.61% despite sitting at force rank #197 overall. VIX Fear Rotation is #3 in rolling 30D (+4.60%, 3.38 Sharpe) but #199 in force rank. These divergences matter: they suggest regime shifts or mean reversion, not alpha.

SPY returned 9.11% over the same 30 days. Only Quantified Simple Monthly Rotation beat it in that window.

## What We're Actually Testing

The signals draw from:
- FRED macroeconomic data (mortgage rates, retail sales, electricity consumption)
- TSA mobility indices (Uber Mobility Index)
- VIX term structure and fear gauges
- Sector rotation heuristics (Faber, Antonacci, simple monthly)
- Alternative sentiment proxies (liquor store traffic, Reddit signals)

Sample size: 96 days. That's **not statistically significant**. A single lucky streak or regime alignment can dominate. We know this. We're publishing it anyway because the point is transparency, not the illusion of edge.

## The Spread

Of 202 algos, 1 beats SPY on force rank. On rolling 30D, still 1 (Quantified Simple Monthly Rotation). The median algo is down 1–2% YTD. The distribution is wide: winners at +10%, losers at −4%.

Sector consensus is mixed-to-bearish. Technology (XLK) shows 41% bullish signals (13 of 32 algos). Everything else—Consumer Defensive, Utilities, Materials, Industrials—is in the red zone (14–19% bullish).

## Why This Matters

We're not claiming an edge. We're documenting the absence of one in real time. Most alternative-data signals underperform a simple monthly rotation. Some fail spectacularly. That's the lab's value: it kills bad ideas publicly and forces you to ask *why* the simple approach works when the complex ones don't.

Methodology and full leaderboard at stockarithm.com.