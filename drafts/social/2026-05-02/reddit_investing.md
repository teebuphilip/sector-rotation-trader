# StockArithm Lab Report: When Signals Flip (May 1, 2026)

We're running 158 signals across 105 tickers. Today's results are a reminder that alternative-data sector rotation doesn't always work—and that's exactly why we publish everything.

## The Setup

Most of our signals measure economic activity—things like electricity consumption, job posting surges, dark pool flows—and use them to rotate between sectors. The idea: real economic data moves faster than price. Let's see what actually happened.

## The Winner (and the Asterisk)

**Algo Baileymol (Chaos Monger)** is the only signal beating SPY today. It's up **6.87% YTD** vs SPY's **5.77%**, with **+1.1% alpha**. Over 88 days, it's turned $100k into $106.8k.

But here's the catch: over the last 30 days, it's actually *underperforming* SPY by 5.7 percentage points. It's winning on older trades. That matters.

## The Failures (and They're Real)

**VIX Fear Rotation** is our worst performer: **-6.79% YTD**, ranked dead last at #158. It's trying to use volatility term structure to time sector rotations. It's not working.

**Algo Biscotti** (both versions) is down **-2.83% to -3.13% YTD**. It's a sector-rotation signal that's been wrong for months.

The interesting part? In the last 30 days, Biscotti ranked #4 and returned +2.67%. VIX Term Structure (our worst full-window performer at rank #156) just posted **+4.68% in 30 days** and ranks #1 on the rolling leaderboard. These signals are *flipping*.

## What the Sector Consensus Says

Across all 158 signals, the consensus is **bearish across the board**:
- Technology (XLK): 29% bullish
- Consumer Cyclical (XLY): 23% bullish  
- Basic Materials (XLB): 19% bullish

That's not a strong conviction in any direction. Most signals are sitting on the sidelines or hedged.

## The Real Story

One signal beat SPY. Zero signals beat SPY over the last 30 days. The lab is publishing both wins and losses because that's how you actually learn whether alternative data works. Some signals are reversing hard—what failed for 88 days is suddenly working. That's either mean reversion or a regime shift. We'll find out.

Everything is public at stockarithm.com.