# r/algotrading — Launch Post Template
# Run: python scripts/refresh_reddit_drafts.py
# Output lands in drafts/reddit_launch/YYYY-MM-DD/algotrading.md with numbers filled in

---

**Title:** {algotrading_title}

---

Background: I've been building a paper-trading lab called StockArithm that runs sector rotation algorithms driven by alternative economic data — TSA checkpoint counts, bankruptcy filing rates, EV charger installation velocity, freight rail carloads, consumer misery index, and about {total_algos_minus_10} other weird things.

Everything is paper-traded (no real money), everything is public, and I publish the failures as clearly as the wins. That's the whole point.

**The current numbers**

- {total_algos} signals running live
- {beating_spy} beating SPY on full-window alpha ({top1_return}% / +{top1_alpha}% alpha and {top2_return}% / +{top2_alpha}% alpha)
- {rolling_30d_beating_spy} beating SPY on rolling 30D
- {losing_count} are flat, collecting data, or underperforming

I'm going to say that again: {beating_spy} out of {total_algos}. Not burying that.

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

An algo can be #1 on rolling 30D and #{biscotti_force_rank} on force rank simultaneously. That's a feature, not a bug.

**The ones worth talking about**

Best on full-window: **{top1_name}** at {top1_return}% return, +{top1_alpha}% alpha.

Best on rolling 30D: **Biscotti (Unconditional Loyalty)** — {biscotti_30d_return}% in the last 30 days, currently ranked #{biscotti_rolling_rank} on momentum. Force rank: #{biscotti_force_rank}. Named after my dog. Good month. Bad long-run record. I don't know yet if it turned a corner or just fit a short regime.

Worst: **{worst_name}** at {worst_return}% return, {worst_alpha}% alpha. Still running. Killing an algo after 30 bad days is how you get survivorship bias.

**What I'm not doing**

- Not cherry-picking the start date
- Not hiding the flat algos — they're all on the leaderboard
- Not claiming {days_running} days is statistically significant (it's not)
- Not selling anything yet

**Why I'm posting**

Gut-check time. What am I missing methodologically? What signals would you run that aren't on the board? What does {beating_spy}-out-of-{total_algos} tell you about the data sources or the rotation rules?

Full leaderboard at stockarithm.com — all signals public, failures included.
