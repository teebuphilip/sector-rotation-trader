# One Signal Beat SPY This Month. Here's What Happened.

StockArithm is running 151 signals across 105 tickers, and the results this month are a textbook case of why you can't just pick a strategy and forget it.

## The Setup

The lab tests signals that measure real economic data—things like sector momentum, dark pool activity, mobility indices, and volatility term structure. Each signal gets ranked two ways: full-window performance (since launch) and rolling 30-day performance. The idea is to see which signals actually work and which ones don't.

SPY returned **10.5% over the last 30 days**. That's the bar.

## The Winner (and the Asterisk)

**Algo Baileymol** is the only signal beating SPY on full-window returns: **+6.26% YTD vs. SPY's +5.48%**. It's up 0.78% in alpha. Over 87 days, that's real outperformance.

But here's the catch: **only 1 out of 151 signals beat SPY over the full window**. That's 0.66%. The other 150 are underwater or treading water.

## The Weird Divergence

Two signals are doing something strange: they're *tanking* on full-window returns but *crushing it* in the last 30 days.

- **Algo Biscotti (Unconditional Loyalty)** is ranked #148 overall (down 2.57% YTD) but #1 on the 30-day leaderboard (+4.98% in 30 days, Sharpe of 2.28).
- **VIX Term Structure** is ranked #149 overall (down 5.74% YTD) but #3 in 30 days (+3.89%, Sharpe of 3.08).

This is the lab's transparency at work: both signals are published as failures on the full window, but they've reversed hard in recent weeks. Whether that sticks is an open question.

## The Failure

**VIX Fear Rotation** is the worst performer: **-7.41% YTD**, ranked dead last at #151. It's measuring volatility structure as a rotation signal, and it's been wrong for months.

## Sector Consensus

The signals are mostly bearish. Technology is the only sector with mixed sentiment (38% bullish). Everything else—Utilities, Consumer Defensive, Industrials—is red.

---

The lab publishes wins and losses equally. One signal beat the market. 150 didn't. Some are recovering fast; others are stuck. That's the data.

**Everything is public at stockarithm.com.**