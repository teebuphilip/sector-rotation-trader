# r/SecurityAnalysis — Launch Post Template
# Run: python scripts/refresh_reddit_drafts.py
# Output lands in drafts/reddit_launch/YYYY-MM-DD/security_analysis.md with numbers filled in

---

**Title:** Testing economic leading indicators as systematic sector rotation signals — {days_running}-day live results and methodology

---

I've been running a public paper-trading lab (StockArithm) that treats alternative economic data as leading indicators for sector rotation. {days_running} days of live paper trading. Posting the methodology and results.

**The thesis**

Economic activity data — consumer stress indices, freight volumes, job formation rates, airport throughput — should precede sector performance by weeks to months. If the misery index (unemployment + CPI) is rising, defensive positioning (XLP, XLU, XLV) should outperform. If TSA checkpoint counts are accelerating, consumer discretionary and industrials should follow.

These are not novel ideas. The sector rotation framework is well-documented. What I'm testing is whether lower-frequency alternative data sources carry rotation signal that isn't already priced in by the time the data is public.

**Data sources and signal structure**

{total_algos} algorithms, each using a single data source as its trigger:

- **FRED macro**: unemployment (UNRATE), CPI (CPIAUCSL), bankruptcy filings (BUSTHCONS), job openings (JTSJOL), retail sales momentum (RSXFS), small business optimism (SBUSV)
- **Transport throughput**: TSA checkpoint counts (weekly), AAR freight rail carloads (weekly), Port of LA container volumes (TEU), airline load factor proxy (BTS)
- **Sentiment proxies**: Google Trends sector-specific search volume (pytrends), Reddit activity signals

Each signal maps to a fixed sector ETF rotation rule. No discretionary override.

**Current results**

{total_algos} signals, {days_running} days live. {beating_spy} showing positive alpha vs SPY (+{top1_alpha}% and +{top2_alpha}%). The rest are neutral or negative.

The current signal ensemble consensus: {security_macro_note}

One structural observation: the monthly FRED-sourced signals are almost uniformly flat at {days_running} days. Expected — monthly cadence doesn't generate enough signal events in this window to build a track record. The weekly-release signals (TSA, AAR freight) are showing earlier differentiation.

**What I'm watching**

The divergence between force rank (full-window since seed) and rolling 30D momentum is the most diagnostic metric. **Biscotti** is #{biscotti_rolling_rank} on rolling 30D ({biscotti_30d_return}% in 30 days) and #{biscotti_force_rank} on force rank. Short-term regime fit against a weak long-run record — exactly the pattern dual-ranking is designed to surface.

**Honest caveats**

{days_running} days of paper trading is directional data, not a verdict on any of these signals. The lab is designed to run for 12+ months. Publishing now because the methodology is fixed and the results are accumulating publicly regardless.

Full leaderboard and signal methodology at stockarithm.com. All signals public, no survivorship bias filtering.
