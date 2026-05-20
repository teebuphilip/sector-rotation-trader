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
| 1 | Quantified Simple Monthly Rotation | normal | +9.34% | +1.03% | +0 |
| 2 | Algo Baileymol (Chaos Monger) | normal | +8.51% | +0.19% | +264 |
| 3 | Faber Momentum Rotation | normal | +8.05% | -0.27% | +0 |
| 4 | Antonacci Dual Momentum Sector Rotation | normal | +6.29% | -2.03% | +0 |
| 5 | Retail Sales Momentum | crazy | +2.60% | -5.71% | +1 |
| 6 | Uber Mobility Index | crazy | +2.59% | -5.73% | -1 |
| 7 | Job Posting Acceleration | crazy | +1.16% | -7.16% | +0 |
| 8 | Insider Trading Signals | crazy | +0.61% | -7.71% | +0 |
| 9 | Weekly Google Trends Surge In Diy Electronics Repair Signals Tech Consumer Stress Lift | crazy | +0.08% | -8.24% | +0 |
| 10 | Weekly Surge In Google Trends Searches For Diy Electronics Repair Signals Bullish Xlk | crazy | +0.08% | -8.24% | +0 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 319 | Copper Momentum | crazy | -3.11% | -11.43% | -61 |
| 320 | Port Container Volume | crazy | -3.44% | -11.75% | -61 |
| 321 | VIX Fear Rotation | crazy | -4.47% | -12.79% | -57 |
| 322 | Electricity Consumption | crazy | -5.48% | -13.80% | -57 |
| 323 | Chaos Rotation Lab | crazy | -5.65% | -13.97% | n/a |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +4.12%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | standard | +9.34% | +5.22% |
| 2 | Faber Momentum Rotation | standard | +4.04% | -0.08% |
| 3 | VIX Fear Rotation | crazy | +3.54% | -0.58% |
| 4 | VIX Term Structure | crazy | +3.42% | -0.70% |
| 5 | Uber Mobility Index | crazy | +2.61% | -1.51% |
| 6 | Retail Sales Momentum | crazy | +2.60% | -1.52% |
| 7 | Antonacci Dual Momentum Sector Rotation | standard | +2.48% | -1.64% |
| 8 | Algo Baileymol (Chaos Monger) | standard | +2.25% | -1.87% |
| 9 | Algo Biscotti (Unconditional Loyalty) (crazy) | crazy | +1.66% | -2.47% |
| 10 | Job Posting Acceleration | crazy | +1.16% | -2.97% |

## Sector Consensus
- Top Bullish: XLK, XLI, XLU
- Top Bearish: XLC, XLF, XLRE

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 12 of 45 | BEARISH | 27% |
| XLI | Industrials | 13 of 52 | BEARISH | 25% |
| XLU | Utilities | 8 of 45 | BEARISH | 18% |
| XLP | Consumer Defensive | 7 of 41 | BEARISH | 17% |
| XLB | Basic Materials | 7 of 41 | BEARISH | 17% |
| XLE | Energy | 6 of 41 | BEARISH | 15% |
| XLY | Consumer Cyclical | 7 of 64 | BEARISH | 11% |
| XLV | Healthcare | 2 of 45 | BEARISH | 4% |
| XLC | Communication Services | 1 of 39 | BEARISH | 3% |
| XLRE | Real Estate | 1 of 40 | BEARISH | 2% |
| XLF | Financial Services | 1 of 42 | BEARISH | 2% |

## Content Facts
- Signal of day: Quantified Simple Monthly Rotation (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK BEARISH (Highest bullish percentage in precomputed sector consensus)
- Failure of day: Chaos Rotation Lab (Lowest full-window force rank)

## Notable Divergences
- VIX Fear Rotation: force rank #321, rolling 30D rank #3. Strong recent 30D rank despite weaker full-window force rank.
- VIX Term Structure: force rank #318, rolling 30D rank #4. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty) (crazy): force rank #313, rolling 30D rank #9. Strong recent 30D rank despite weaker full-window force rank.
- Healthcare Cost Shock Google Search Spike: force rank #303, rolling 30D rank #53. Strong recent 30D rank despite weaker full-window force rank.
- Oil Price Momentum Reversal Energy Sector Bounce: force rank #264, rolling 30D rank #17. Strong recent 30D rank despite weaker full-window force rank.

