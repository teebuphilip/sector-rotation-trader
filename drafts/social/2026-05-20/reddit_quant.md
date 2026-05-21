# StockArithm Lab Report: 2026-05-20 — One Algo Beating SPY, 322 Underwater

We're running 323 signals across 105 tickers in live paper trading. Today's snapshot: **1 algo is beating SPY on force rank (full-window cumulative return), and 2 are beating it on rolling 30-day momentum.** The rest are negative alpha. This is the point of publishing failures.

## The Numbers

**Force Rank (108 days live):**
- Quantified Simple Monthly Rotation: +11.05% YTD, +2.25% alpha vs. SPY's +8.8%. Equity: $111,048.
- Baileymol (Chaos Monger): +8.15% YTD, -0.64% alpha. Rank jumped 264 spots to #2 on return, but still underwater relative to the benchmark.
- Faber Momentum Rotation: +7.74% YTD, -1.06% alpha.
- 320 others: negative alpha. Copper Momentum, Port Container Volume, and VIX Fear Rotation are down 2–3% YTD.

**Rolling 30-Day Momentum (SPY +4.59%):**
- Simple Monthly Rotation leads again: +11.05% in 30D, +6.46% delta to SPY. Sharpe 4.57.
- VIX Fear Rotation ranks #2 despite being #321 on force rank—a 319-slot divergence. It's returned +4.65% in 30D vs. SPY's +4.59%, but YTD it's -3.44%. This is a regime-dependent signal.
- VIX Term Structure (#3 rolling, #316 force): +4.50% in 30D, -1.71% YTD.

**The Spread:** 1 of 323 force-ranked algos beats SPY. 2 of 324 rolling 30D algos beat SPY. That's 0.3% and 0.6% respectively. The lab is not a performance showcase—it's a transparency mechanism.

## What We're Measuring

**Data sources:** FRED (economic releases), TSA (mobility), Reddit sentiment, job openings, freight rail carloads, port container volume, VIX term structure, sector ETF flows, retail sales, copper and lumber futures.

**Two ranking systems exist for a reason:**
- Force rank captures full-window consistency. Simple Monthly Rotation has held #1 since inception.
- Rolling 30D captures recent regime shifts. VIX Fear Rotation is a textbook example: it's been wrong for 108 days but right for the last 30. Both metrics matter. Neither predicts forward returns.

**Sample size caveat:** 108 days of live paper trading is not statistically significant. Confidence intervals are wide. Sharpe ratios above 2.0 are noise at this horizon. We report them anyway because the methodology is transparent and reproducible.

## Notable Divergences

Three algos show sharp recent momentum despite weak cumulative records:
- **VIX Fear Rotation:** Force rank 321, rolling 30D rank 2. Gap of 319 slots.
- **VIX Term Structure:** Force rank 316, rolling 30D rank 3. Gap of 313 slots.
- **Algo Biscotti (Unconditional Loyalty):** Force rank 314, rolling 30D rank 9. Gap of 305 slots.

These are not hidden. They're flagged as divergences because they reveal regime dependency. A signal that works in one market regime and fails in another is still a signal worth studying.

## Sector Consensus

Across 37 algos with sector views, Technology (XLK) shows the highest bullish percentage at 32%—but the composite label is still **BEARISH** (12 of 37 signals). Energy, Basic Materials, and Consumer Defensive are all below 20% bullish. This is a low-conviction market in the lab's view.

---

**Methodology and full leaderboard at stockarithm.com.**