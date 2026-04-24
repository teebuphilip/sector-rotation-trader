# r/algotrading — Launch Post Template

---

**Title:** I've been running 115 alternative-data signals against SPY for 80 days. 2 are winning. Here's the full picture.

---

Background: I've been building a paper-trading lab called Stockarithm that runs sector rotation algorithms driven by alternative economic data — TSA checkpoint counts, bankruptcy filing rates, EV charger installation velocity, freight rail carloads, consumer misery index, and about 105 other weird things.

Everything is paper-traded (no real money), everything is public, and I publish the failures as clearly as the wins. That's the whole point.

**The current numbers**

- 115 signals running live
- 2 beating SPY on full-window alpha (5.78% / +1.80% alpha and 4.76% / +0.78% alpha)
- 0 beating SPY on rolling 30D
- 113 are flat, collecting data, or underperforming

I'm going to say that again: 2 out of 115. Not burying that.

**The methodology**

Each signal is a single alternative data source wired to a sector rotation rule:

- Data source fires (e.g., TSA passenger counts drop below 3-week MA threshold)
- Algo rotates to target sector ETFs or cash
- Entry/exit rules are fixed, not curve-fitted
- Tracked from seed date, SPY as benchmark

Data sources: FRED (unemployment, CPI, bankruptcy filings, retail sales, job openings, small business formation), TSA checkpoint tables, AAR freight rail carloads, EIA electricity consumption, Port of LA TEU volume, Google Trends via pytrends, Reddit sentiment proxies.

Two rankings, deliberately separate:

- **Force rank** — full-window/since-seed total return and alpha. Long-run trust metric.
- **Rolling 30D** — trailing momentum, Sharpe, max drawdown. Recent-regime metric.

An algo can be #1 on rolling 30D and #100 on force rank simultaneously. That's a feature, not a bug.

**The ones worth talking about**

Best on full-window: **Algo Baileymol** at 5.78% return, +1.80% alpha.

Best on rolling 30D: **Biscotti (Unconditional Loyalty)** — 7.67% in the last 30 days, currently ranked #1 on momentum. Force rank: #100. Named after my dog, who died in April 2025 while I was building the first version of this. Good month. Bad long-run record. I don't know yet if it's turned a corner or got lucky in a specific regime.

Worst: **VIX Fear Rotation** at -8.00% return, -11.99% alpha. Still running. Killing an algo after 30 bad days is how you get survivorship bias.

**What I'm not doing**

- Not cherry-picking the start date
- Not hiding the flat algos — they're all on the leaderboard
- Not claiming 80 days is statistically significant (it's not)
- Not selling anything yet

**Why I'm posting**

Gut-check time. What am I missing methodologically? What signals would you run that aren't on the board? What does 2-out-of-115 tell you about the data sources or the rotation rules?

Full leaderboard at stockarithm.com — all signals, failures included.