# r/algotrading — Launch Post Template

---

**Title:** I've been running 234 alternative-data signals against SPY for 98 days. 1 are beating it. Here's the full picture.

---

Background: I've been building a paper-trading lab called StockArithm that runs sector rotation algorithms driven by alternative economic data — TSA checkpoint counts, bankruptcy filing rates, EV charger installation velocity, freight rail carloads, consumer misery index, and about 224 other weird things.

Everything is paper-traded (no real money), everything is public, and I publish the failures as clearly as the wins. That's the whole point.

**The current numbers**

- 234 signals running live
- 1 beating SPY on full-window alpha (9.83% / +1.49% alpha and 7.72% / +-0.62% alpha)
- 1 beating SPY on rolling 30D
- 233 are flat, collecting data, or underperforming

I'm going to say that again: 1 out of 234. Not burying that.

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

An algo can be #1 on rolling 30D and #221 on force rank simultaneously. That's a feature, not a bug.

**The ones worth talking about**

Best on full-window: **Quantified Simple Monthly Rotation** at 9.83% return, +1.49% alpha.

Best on rolling 30D: **Biscotti (Unconditional Loyalty)** — -1.10% in the last 30 days, currently ranked #234 on momentum. Force rank: #221. Named after my dog. Good month. Bad long-run record. I don't know yet if it turned a corner or just fit a short regime.

Worst: **Chaos Rotation Lab** at -6.12% return, -14.47% alpha. Still running. Killing an algo after 30 bad days is how you get survivorship bias.

**What I'm not doing**

- Not cherry-picking the start date
- Not hiding the flat algos — they're all on the leaderboard
- Not claiming 98 days is statistically significant (it's not)
- Not selling anything yet

**Why I'm posting**

Gut-check time. What am I missing methodologically? What signals would you run that aren't on the board? What does 1-out-of-234 tell you about the data sources or the rotation rules?

Full leaderboard at stockarithm.com — all signals public, failures included.