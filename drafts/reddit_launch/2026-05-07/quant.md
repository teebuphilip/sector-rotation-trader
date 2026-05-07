# r/quant — Launch Post Template

---

**Title:** Alternative economic data as sector rotation signals — methodology notes and 94-day paper-trading results [OC]

---

I've been running a paper-trading lab (StockArithm) for approximately 94 days using single alternative-data sources as sector rotation triggers. Posting here for methodological feedback, not validation.

**Setup**

Each algorithm:
- Uses one alternative data source as its signal
- Triggers a sector ETF rotation (SPDR family)
- Has fixed entry/exit rules, no curve fitting, no parameter optimization
- Runs as a paper trade from seed date with SPY as benchmark

Data sources: FRED series (UNRATE, CPIAUCSL, BUSTHCONS, JTSJOL, RSXFS, SBUSV), TSA checkpoint counts (weekly), AAR freight rail carloads (weekly), EIA electricity consumption, Port of LA TEU volumes, Google Trends via pytrends, Reddit activity proxies.

**Ranking structure**

Two separate rankings, intentionally not collapsed:

1. **Force rank** — full-window since-seed total return and alpha. Long-run trust metric.
2. **Rolling 30D** — trailing return, Sharpe, max drawdown. Regime-specific momentum metric.

An algo at #9 rolling 30D and #177 force rank is diagnostic, not a contradiction. That pattern indicates short-term regime fit, not durable edge.

**Results**

194 algos, 94 days live. 0 showing positive alpha vs SPY (+-0.59% and +-1.12%). 0 beating SPY on rolling 30D.

I'll say the obvious: 94 days is not a sufficient sample for any statistical inference about edge. The lab is designed to run for 12+ months before I'd claim anything meaningful. The current data is directional at best.

Most interesting observation: **Biscotti** is #9 on rolling 30D (2.73% in 30 days) and #177 on force rank. Classic regime-specificity pattern. Whether it's real signal or noise in a specific market environment is exactly what longer runtime will answer.

Worst performer: **Chaos Rotation Lab** at -5.59% return, -13.30% alpha. Not retired — removing underperformers on short windows produces survivorship bias and I'm trying to avoid that explicitly.

**Questions I'd genuinely like input on**

1. For FRED monthly-release signals, what's the correct handling of the look-ahead bias boundary at release date? I'm currently using release date as the signal trigger date, not the reference period end date.

2. For algos with very low signal frequency (some monthly FRED series fire once per month at most), is full-window total return a reasonable primary rank metric, or should I normalize by trading days active?

3. Any sector rotation literature worth reading on non-price alternative data specifically? The Moskowitz-Grinblatt momentum work is the baseline I'm thinking against.

Full methodology and live leaderboard at stockarithm.com. All signals public, failures included, no survivorship bias filtering.