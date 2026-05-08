# StockArithm Lab Report: 2026-05-07 — A Brutal Week for Systematic Signals

**TL;DR:** 194 algos running live paper trades. Zero beating SPY over the full window. SPY +7.38% YTD; median algo -0.97% alpha. The lab is publishing this failure transparently because that's the point.

---

## The Blunt Numbers

As of today, 194 force-ranked algorithms and 195 rolling 30-day variants are live on paper. **Not a single one is beating SPY on a full-window basis.** The top performer, Algo Baileymol (Chaos Monger), sits at +6.41% YTD—still 97 bps underwater versus SPY's 7.38%. The median is worse: -0.97% alpha across the board.

This is not a marketing moment. This is a data moment.

---

## Two Ranking Systems, Two Stories

StockArithm publishes both **force rank** (cumulative since seed, ~95 days) and **rolling 30-day momentum** because they tell different stories. The spread matters.

**Force Rank (Full Window):** Baileymol, Simple Monthly Rotation, and Antonacci Dual Momentum Sector Rotation occupy the top three slots. All three are negative alpha. The bottom three—VIX Term Structure, Biscotti (both variants)—are down 2.91% to 3.42% YTD.

**Rolling 30D:** VIX Term Structure ranks #1 with +7.22% return and a 5.12 Sharpe ratio over the last month. SPY returned +10.98% in the same window; VIX Term Structure lagged by 3.75 percentage points. But the *volatility profile* is tighter. This is the divergence: recent momentum ≠ full-window edge.

**The gap is real.** Three algos show rank gaps of 189 positions between force rank and rolling 30D rank. VIX Term Structure is #190 all-time, #1 in the last 30 days. That's either mean reversion waiting to happen or a regime shift the full-window model hasn't captured yet. We don't know. That's why we publish both.

---

## Data Sources & Coverage

The lab ingests 105 tickers across 194 signals. Sources include FRED (macro), TSA (mobility), Reddit sentiment, job openings, commodity futures, VIX term structure, and sector rotation mechanics. Each algo is deterministic and reproducible.

**Sample size caveat:** 95 days of live paper trading is *not* statistically significant. A single tail event, a regime shift, or a crowded trade can flip rankings. We're publishing this because the methodology is sound, not because the results are conclusive.

---

## The Spread

- **0 of 194** beating SPY on force rank.
- **0 of 195** beating SPY on rolling 30D.
- Median alpha: **-0.97%**.
- Worst performer: Biscotti (normal variant), **-10.8%** alpha, **-3.42%** YTD.
- Best performer: Baileymol, **-0.97%** alpha, **+6.41%** YTD.

SPY is the benchmark. The algos are not beating it. That's the honest read.

---

## Sector Consensus

Across 34 signals covering Technology (XLK), only 35% are bullish. Consumer Cyclical (XLY) is worse: 18% bullish. The lab's composite stance is **bearish across all major sectors**—a rare alignment that suggests either genuine macro caution or crowded short positioning. Neither is actionable without forward testing.

---

## Why This Matters

StockArithm's differentiator is not returns. It's transparency. We publish losses as loudly as wins. We name the ranking systems, state the sample size limits, and show the spread. Quants and academics can audit the methodology, stress-test the assumptions, and replicate the results.

The lab is a public laboratory, not a fund pitch.

**Methodology and full leaderboard at stockarithm.com.**