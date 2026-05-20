# Deep Validation Report - 2026-05-20

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 323 rows (323 unique algo_ids)
- Force-ranked beating SPY: 1 of 323 rows
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
| 1 | Quantified Simple Monthly Rotation | normal | +10.48% | +1.85% | +0 |
| 2 | Algo Baileymol (Chaos Monger) | normal | +8.17% | -0.47% | +264 |
| 3 | Faber Momentum Rotation | normal | +7.74% | -0.89% | +0 |
| 4 | Antonacci Dual Momentum Sector Rotation | normal | +6.40% | -2.23% | +0 |
| 5 | Uber Mobility Index | crazy | +3.57% | -5.07% | +0 |
| 6 | Retail Sales Momentum | crazy | +3.55% | -5.09% | +0 |
| 7 | Job Posting Acceleration | crazy | +2.01% | -6.62% | +0 |
| 8 | Insider Trading Signals | crazy | +1.14% | -7.50% | +0 |
| 9 | Misery Rotation | crazy | +0.19% | -8.45% | +243 |
| 10 | Housing Permit Velocity | crazy | +0.14% | -8.50% | +243 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 319 | Copper Momentum | crazy | -2.49% | -11.13% | -61 |
| 320 | Port Container Volume | crazy | -2.78% | -11.42% | -61 |
| 321 | VIX Fear Rotation | crazy | -3.80% | -12.44% | -57 |
| 322 | Electricity Consumption | crazy | -4.85% | -13.48% | -57 |
| 323 | Chaos Rotation Lab | crazy | -6.03% | -14.66% | n/a |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +4.43%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | standard | +10.48% | +6.05% |
| 2 | VIX Fear Rotation | crazy | +4.26% | -0.17% |
| 3 | VIX Term Structure | crazy | +4.12% | -0.32% |
| 4 | Faber Momentum Rotation | standard | +3.75% | -0.68% |
| 5 | Uber Mobility Index | crazy | +3.59% | -0.84% |
| 6 | Retail Sales Momentum | crazy | +3.55% | -0.88% |
| 7 | Antonacci Dual Momentum Sector Rotation | standard | +2.59% | -1.84% |
| 8 | Job Posting Acceleration | crazy | +2.01% | -2.42% |
| 9 | Algo Baileymol (Chaos Monger) | standard | +1.93% | -2.50% |
| 10 | Algo Biscotti (Unconditional Loyalty) (alt) | crazy | +1.71% | -2.73% |

## Sector Consensus
- Top Bullish: XLK, XLI, XLB
- Top Bearish: XLF, XLC, XLRE

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 12 of 47 | BEARISH | 26% |
| XLI | Industrials | 13 of 55 | BEARISH | 24% |
| XLB | Basic Materials | 8 of 44 | BEARISH | 18% |
| XLU | Utilities | 8 of 48 | BEARISH | 17% |
| XLP | Consumer Defensive | 7 of 44 | BEARISH | 16% |
| XLE | Energy | 6 of 44 | BEARISH | 14% |
| XLY | Consumer Cyclical | 7 of 67 | BEARISH | 10% |
| XLV | Healthcare | 2 of 48 | BEARISH | 4% |
| XLRE | Real Estate | 1 of 43 | BEARISH | 2% |
| XLF | Financial Services | 1 of 44 | BEARISH | 2% |
| XLC | Communication Services | 1 of 42 | BEARISH | 2% |

## Content Facts
- Signal of day: Quantified Simple Monthly Rotation (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK BEARISH (Highest bullish percentage in precomputed sector consensus)
- Failure of day: Chaos Rotation Lab (Lowest full-window force rank)

## Notable Divergences
- VIX Fear Rotation: force rank #321, rolling 30D rank #2. Strong recent 30D rank despite weaker full-window force rank.
- VIX Term Structure: force rank #317, rolling 30D rank #3. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty) (alt): force rank #315, rolling 30D rank #10. Strong recent 30D rank despite weaker full-window force rank.
- Oil Price Momentum Reversal Energy Sector Bounce: force rank #268, rolling 30D rank #21. Strong recent 30D rank despite weaker full-window force rank.
- Healthcare Cost Shock Google Search Spike: force rank #303, rolling 30D rank #57. Strong recent 30D rank despite weaker full-window force rank.

