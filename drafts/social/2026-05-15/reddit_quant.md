# StockArithm Lab Report: 266 Algos, 1 Beating SPY—And Why That Matters

We're 101 days into live paper trading across 266 algorithmic signals covering 105 tickers. One algo is beating SPY on force rank. One on rolling 30D. The spread is brutal. This is the point.

## The Honest Baseline

SPY returned 8.49% YTD. Our median algo is underwater. Of 266 force-ranked strategies, only **Quantified Simple Monthly Rotation** has positive alpha (+2.0%, +10.5% YTD). The rest are chasing or losing. On the 30D rolling window, the same algo leads with 10.5% return vs. SPY's 5.6%—a 4.9% delta. But that's one signal. The distribution below it is a graveyard: Lumber Momentum, Port Container Volume, and Copper Momentum all down 1.8–2.4% in the last month.

This is not a marketing problem. This is a data problem.

## Two Ranking Systems, Two Stories

We report both **force rank** (full-window cumulative since seed) and **rolling 30D momentum** because they answer different questions:

- **Force rank** shows which algos have survived longest without catastrophic drawdown. Quantified Simple Monthly Rotation: rank 1, -1.8% max DD, 4.5 Sharpe over 30D.
- **Rolling 30D** isolates recent edge. VIX Fear Rotation ranks 264 on force but 2 on 30D—it's been dead for months, then suddenly worked. That's a signal worth examining, not hiding.

The gap matters. Algo Biscotti (Unconditional Loyalty) sits at rank 262 force but rank 9 on 30D, a 253-rank divergence. It's been a disaster YTD (-2.87%), but the last 30 days it returned 2.3%. Noise or regime shift? The data doesn't yet say. Sample size is 101 days. That's not statistically significant for any claim.

## What We're Actually Testing

Each signal ingests alternative data: FRED macroeconomic releases, TSA passenger volumes, Reddit sentiment, job openings, VIX term structure, commodity momentum, port container throughput. The algos are mechanical rotations and momentum filters applied to sector ETFs and individual equities. No machine learning black box. No backtested overfitting (we're live). No survivorship bias (we publish failures).

Today's **failure of day**: Chaos Rotation Lab (Baileymol) is down 6.1% YTD, -14.6% alpha vs. SPY. It's ranked 266 on force. We're running it anyway and reporting it.

Today's **sector consensus**: 30% of algos are bullish on Industrials (XLI), 19% on Tech (XLK). Both sectors show BEARISH composite signals. The algos disagree with each other. That's expected when you're testing 266 independent hypotheses on 101 days of data.

## The Real Question

Can we find repeatable edges in alternative data? Not yet. One algo beating SPY over 101 days is not an edge—it's luck until proven otherwise. But the methodology is transparent, the failures are public, and the data sources are named. That's the differentiator.

We're not claiming victory. We're publishing the loss function.

Methodology and full leaderboard at stockarithm.com.