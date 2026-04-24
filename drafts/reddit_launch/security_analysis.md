# r/SecurityAnalysis — First Post Draft
> UPDATE BEFORE POSTING: refresh [X days] and any numbers that have changed since 2026-04-24

---

**Title:** Testing economic leading indicators as systematic sector rotation signals — [X]-day live results and methodology

---

I've been running a public paper-trading lab (Stockarithm) that treats alternative economic data as leading indicators for sector rotation. [X] days of live paper trading. Posting the methodology and results.

**The thesis**

Economic activity data — consumer stress indices, freight volumes, job formation rates, airport throughput — should precede sector performance by weeks to months. If the misery index (unemployment + CPI) is rising, defensive positioning (XLP, XLU, XLV) should outperform. If TSA checkpoint counts are accelerating, consumer discretionary and industrials should follow.

These are not novel ideas. The sector rotation framework is well-documented. What I'm testing is whether lower-frequency alternative data sources carry rotation signal that isn't already priced in by the time the data is public.

**Data sources and signal structure**

115 algorithms, each using a single data source as its trigger:

- **FRED macro**: unemployment (UNRATE), CPI (CPIAUCSL), bankruptcy filings (BUSTHCONS), job openings (JTSJOL), retail sales momentum (RSXFS), small business optimism (SBUSV)
- **Transport throughput**: TSA checkpoint counts (weekly), AAR freight rail carloads (weekly), Port of LA container volumes (TEU), airline load factor proxy (BTS)
- **Sentiment proxies**: Google Trends sector-specific search volume (pytrends), Reddit activity signals

Each signal maps to a fixed sector ETF rotation rule. No discretionary override.

**Current results**

115 signals, [X] days live. 2 showing positive alpha vs SPY (+1.80% and +0.78%). The rest are neutral or negative.

The current signal ensemble consensus: Technology (XLK) is mixed — 41% of signals bullish. Consumer Defensive (XLP) and Industrials (XLI) are reading bearish across the suite. That's internally consistent with a late-cycle, risk-off positioning read — worth noting given where we are macro-wise.

One structural observation: the monthly FRED-sourced signals are almost uniformly flat at [X] days. Expected — monthly cadence doesn't generate enough signal events in this window to build a track record. The weekly-release signals (TSA, AAR freight) are showing earlier differentiation. That cadence difference alone is worth tracking.

**What I'm watching**

The divergence between force rank (full-window since seed) and rolling 30D momentum is the most diagnostic metric right now. **Biscotti** is #1 on rolling 30D (+7.8% in 30 days) and #98 on force rank. That kind of divergence — short-term regime fit against weak long-run record — is exactly the pattern I built dual-ranking to surface.

**Honest caveats**

[X] days of paper trading is directional data, not a verdict on any of these signals. The lab is designed to run for 12+ months. I'm publishing now because the methodology is fixed and the results are accumulating publicly whether I post about it or not.

Full leaderboard and signal methodology at stockarithm.com. All signals public, no survivorship bias filtering.
