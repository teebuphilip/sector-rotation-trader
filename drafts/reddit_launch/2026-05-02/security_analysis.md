# r/SecurityAnalysis — Launch Post Template

---

**Title:** Testing economic leading indicators as systematic sector rotation signals — 88-day live results and methodology

---

I've been running a public paper-trading lab (StockArithm) that treats alternative economic data as leading indicators for sector rotation. 88 days of live paper trading. Posting the methodology and results.

**The thesis**

Economic activity data — consumer stress indices, freight volumes, job formation rates, airport throughput — should precede sector performance by weeks to months. If the misery index (unemployment + CPI) is rising, defensive positioning (XLP, XLU, XLV) should outperform. If TSA checkpoint counts are accelerating, consumer discretionary and industrials should follow.

These are not novel ideas. The sector rotation framework is well-documented. What I'm testing is whether lower-frequency alternative data sources carry rotation signal that isn't already priced in by the time the data is public.

**Data sources and signal structure**

167 algorithms, each using a single data source as its trigger:

- **FRED macro**: unemployment (UNRATE), CPI (CPIAUCSL), bankruptcy filings (BUSTHCONS), job openings (JTSJOL), retail sales momentum (RSXFS), small business optimism (SBUSV)
- **Transport throughput**: TSA checkpoint counts (weekly), AAR freight rail carloads (weekly), Port of LA container volumes (TEU), airline load factor proxy (BTS)
- **Sentiment proxies**: Google Trends sector-specific search volume (pytrends), Reddit activity signals

Each signal maps to a fixed sector ETF rotation rule. No discretionary override.

**Current results**

167 signals, 88 days live. 1 showing positive alpha vs SPY (+1.10% and +-1.90%). The rest are neutral or negative.

The current signal ensemble consensus: Technology (XLK) leads current bullish share at 29%. I update the actual macro read by hand before posting so I do not overstate what the nightly data says.

One structural observation: the monthly FRED-sourced signals are almost uniformly flat at 88 days. Expected — monthly cadence doesn't generate enough signal events in this window to build a track record. The weekly-release signals (TSA, AAR freight) are showing earlier differentiation.

**What I'm watching**

The divergence between force rank (full-window since seed) and rolling 30D momentum is the most diagnostic metric. **Biscotti** is #4 on rolling 30D (2.67% in 30 days) and #155 on force rank. Short-term regime fit against a weak long-run record — exactly the pattern dual-ranking is designed to surface.

**Honest caveats**

88 days of paper trading is directional data, not a verdict on any of these signals. The lab is designed to run for 12+ months. Publishing now because the methodology is fixed and the results are accumulating publicly regardless.

Full leaderboard and signal methodology at stockarithm.com. All signals public, no survivorship bias filtering.