# StockArithm Lab Report: 202 Algos, 1 Beating SPY (And That's the Point)

As of May 8, 2026, StockArithm's public paper-trading lab is running 202 live signals across 105 tickers. One is beating SPY on a force-ranked (full-window) basis. One. That asymmetry is not a bug—it's the methodology.

## The Setup

We publish two ranking systems because they answer different questions:

**Force rank** (cumulative since seed, ~96 days): Which algos have generated alpha over the entire live window? This is the long-term signal. Currently, **Quantified Simple Monthly Rotation** is the sole outperformer at +1.77% alpha (10.03% YTD vs. SPY's 8.27%). Everything else is underwater relative to the benchmark.

**Rolling 30D momentum**: Which algos are *currently* hot? This captures regime shifts and recent edge. Here, 203 algos are tracked, and the spread is wider—Quantified Simple Monthly Rotation leads at +10.03% (30D), but VIX Term Structure ranks #2 at +7.61%, and even Algo Biscotti (Unconditional Loyalty), a "crazy" category signal, posts +4.60% over the last month despite -3.94% YTD.

## The Honest Spread

Of 202 force-ranked algos:
- **1 beats SPY** (0.5%)
- **201 underperform** (99.5%)

Of 203 rolling 30D algos:
- **1 beats SPY on 30D delta** (Quantified Simple Monthly Rotation, +0.92% vs. SPY's 9.11% in 30D)
- The rest lag the benchmark in recent weeks

This is not a failure of the lab. It's a failure of most signals to generate alpha in this regime. We publish that failure.

## Notable Divergences

Three algos show sharp rank gaps between force rank and 30D rank—a red flag for overfitting or regime-dependent edge:

- **VIX Fear Rotation**: Force rank 199, rolling 30D rank 3 (gap: 196). Returns +4.60% in 30D but -3.2% YTD.
- **VIX Term Structure**: Force rank 197, rolling 30D rank 2 (gap: 195). Returns +7.61% in 30D but -1.45% YTD.
- **Algo Baileymol (Chaos Monger)**: Force rank 202, rolling 30D rank 10 (gap: 192). Returns +1.75% in 30D but -6.2% YTD.

These are candidates for survivorship bias or data-snooping. We flag them explicitly.

## Data Sources & Limitations

Signals draw from FRED (macro), TSA (mobility), Reddit sentiment, job openings, VIX term structure, retail sales, mortgage rates, and sector ETF flows. Sample size: 86–96 days of live paper trading. **This is not statistically significant.** A single month of outperformance proves nothing. We report it anyway because transparency beats silence.

Sharpe ratios on 30D windows are noise. Max drawdowns under 2% are margin-of-error territory. The lab's value is in the *methodology*—alternative data ingestion, signal composition, public failure logging—not in the returns themselves.

## Sector Consensus

Across 32 algos tracking Technology (XLK), 41% are bullish (composite: MIXED). Consumer Defensive, Utilities, Basic Materials, and Industrials all show <20% bullish consensus (BEARISH).

---

**Methodology and full leaderboard at stockarithm.com.**