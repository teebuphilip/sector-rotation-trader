# StockArithm Lab Report: May 7, 2026 — When Recent Wins Hide Longer Losses

We're running 194 signals across 105 tickers. Today's snapshot is a textbook case of *recency bias* — and we're publishing both sides of it.

## The Headline: VIX Term Structure Just Won the Last 30 Days

**VIX Term Structure** crushed it over the past month: **+7.22%** while SPY returned **+10.98%**. It ranks #1 on the rolling 30-day leaderboard with a Sharpe of 5.1. That's real.

But here's the catch: over the full 95-day window, it's ranked **#190 out of 194**. YTD it's down **-2.91%**. The signal measures volatility curve dynamics to rotate between risk-on and risk-off positioning. It worked *this month*. It hasn't worked most of the time.

This is the divergence we highlight. A signal can be hot for 30 days and still be a net loser. Both facts matter.

## The Failures Are Louder

**Algo Biscotti (Unconditional Loyalty)** — the normal version — is down **-3.42% YTD** and ranks dead last at #192. It's measuring something that isn't working. We're running it anyway and reporting it.

**Chaos Rotation Lab** (another Baileymol variant) is our "failure of the day": **-6.21% YTD**, ranked #194. It's trying to exploit chaos in market microstructure. It's not.

Meanwhile, **Baileymol** (the standard version) is our top performer: **+6.41% YTD**, up **+0.97%** alpha vs. SPY. It's been running 95 days and has held the #1 rank. That one is working — so far.

## What the Signals Actually Measure

These aren't black boxes. They're sector rotation strategies triggered by:
- Economic data (momentum, dual momentum, Faber-style trend following)
- Volatility structure (VIX term curve, fear rotation)
- Commodity momentum (copper, lumber, mortgage rates as housing proxies)

194 different takes on the same question: *Can alternative data or economic indicators beat buy-and-hold?*

**Current answer:** Not yet. Zero algos are beating SPY over the full window. But the lab publishes failures as loudly as wins — that's the point.

## Sector Consensus: Broadly Bearish

Across 34 signals, only 35% are bullish on Technology (XLK). Consumer Cyclical (XLY) is at 18% bullish. Everything is red.

---

Everything is public at stockarithm.com.