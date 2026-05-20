# Deep Validation Report - 2026-05-20

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 323 rows (323 unique algo_ids)
- Force-ranked beating SPY: 2 of 323 rows
- Rolling 30D algos: 324 rows (324 unique algo_ids)
- Rolling 30D beating SPY: 1 of 324 rows
- Signals generated: 323
- Tickers covered: 105
- Sectors computed: 11

## Data Hygiene
- Force-rank duplicate rows: 0
- Rolling 30D duplicate rows: 0
- Rolling-only algo_ids with no force-rank row: 1

## Force Rank
Full-window/since-seed rank; not the same as recent 30D performance.

### Top 10
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | normal | +10.32% | +2.01% | +0 |
| 2 | Algo Baileymol (Chaos Monger) | normal | +8.53% | +0.22% | +264 |
| 3 | Faber Momentum Rotation | normal | +8.09% | -0.22% | +0 |
| 4 | Antonacci Dual Momentum Sector Rotation | normal | +6.54% | -1.77% | +0 |
| 5 | Retail Sales Momentum | crazy | +3.16% | -5.15% | +1 |
| 6 | Uber Mobility Index | crazy | +3.16% | -5.14% | -1 |
| 7 | Job Posting Acceleration | crazy | +1.66% | -6.65% | +0 |
| 8 | Insider Trading Signals | crazy | +0.95% | -7.36% | +0 |
| 9 | Misery Rotation | crazy | +0.14% | -8.17% | +243 |
| 10 | Housing Permit Velocity | crazy | +0.12% | -8.19% | +243 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 319 | Copper Momentum | crazy | -2.69% | -10.99% | -61 |
| 320 | Port Container Volume | crazy | -2.99% | -11.30% | -61 |
| 321 | VIX Fear Rotation | crazy | -4.19% | -12.49% | -57 |
| 322 | Electricity Consumption | crazy | -5.05% | -13.35% | -57 |
| 323 | Chaos Rotation Lab | crazy | -5.66% | -13.96% | n/a |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +4.11%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | standard | +10.32% | +6.20% |
| 2 | Faber Momentum Rotation | standard | +4.09% | -0.03% |
| 3 | VIX Fear Rotation | crazy | +3.85% | -0.26% |
| 4 | VIX Term Structure | crazy | +3.71% | -0.40% |
| 5 | Uber Mobility Index | crazy | +3.18% | -0.93% |
| 6 | Retail Sales Momentum | crazy | +3.16% | -0.95% |
| 7 | Antonacci Dual Momentum Sector Rotation | standard | +2.72% | -1.39% |
| 8 | Algo Baileymol (Chaos Monger) | standard | +2.27% | -1.84% |
| 9 | Algo Biscotti (Unconditional Loyalty) (alt) | crazy | +2.07% | -2.04% |
| 10 | Job Posting Acceleration | crazy | +1.66% | -2.45% |

## Sector Consensus
- Top Bullish: XLK, XLE, XLI
- Top Bearish: XLV, XLC, XLRE

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 12 of 37 | BEARISH | 32% |
| XLE | Energy | 6 of 34 | BEARISH | 18% |
| XLP | Consumer Defensive | 6 of 35 | BEARISH | 17% |
| XLI | Industrials | 8 of 48 | BEARISH | 17% |
| XLB | Basic Materials | 6 of 35 | BEARISH | 17% |
| XLU | Utilities | 5 of 41 | BEARISH | 12% |
| XLY | Consumer Cyclical | 5 of 59 | BEARISH | 8% |
| XLF | Financial Services | 2 of 34 | BEARISH | 6% |
| XLV | Healthcare | 2 of 38 | BEARISH | 5% |
| XLRE | Real Estate | 1 of 33 | BEARISH | 3% |
| XLC | Communication Services | 1 of 31 | BEARISH | 3% |

## Content Facts
- Signal of day: Quantified Simple Monthly Rotation (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK BEARISH (Highest bullish percentage in precomputed sector consensus)
- Failure of day: Chaos Rotation Lab (Lowest full-window force rank)

## Notable Divergences
- VIX Fear Rotation: force rank #321, rolling 30D rank #3. Strong recent 30D rank despite weaker full-window force rank.
- VIX Term Structure: force rank #318, rolling 30D rank #4. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty) (alt): force rank #313, rolling 30D rank #9. Strong recent 30D rank despite weaker full-window force rank.
- Oil Price Momentum Reversal Energy Sector Bounce: force rank #268, rolling 30D rank #21. Strong recent 30D rank despite weaker full-window force rank.
- Healthcare Cost Shock Google Search Spike: force rank #303, rolling 30D rank #57. Strong recent 30D rank despite weaker full-window force rank.

