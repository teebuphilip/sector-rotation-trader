# Deep Validation Report - 2026-05-20

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 323 rows (323 unique algo_ids)
- Force-ranked beating SPY: 1 of 323 rows
- Rolling 30D algos: 324 rows (324 unique algo_ids)
- Rolling 30D beating SPY: 2 of 324 rows
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
| 1 | Quantified Simple Monthly Rotation | normal | +11.05% | +2.25% | +0 |
| 2 | Algo Baileymol (Chaos Monger) | normal | +8.15% | -0.64% | +264 |
| 3 | Faber Momentum Rotation | normal | +7.74% | -1.06% | +0 |
| 4 | Antonacci Dual Momentum Sector Rotation | normal | +6.34% | -2.46% | +0 |
| 5 | Uber Mobility Index | crazy | +3.96% | -4.84% | +0 |
| 6 | Retail Sales Momentum | crazy | +3.95% | -4.85% | +0 |
| 7 | Job Posting Acceleration | crazy | +2.37% | -6.42% | +0 |
| 8 | Insider Trading Signals | crazy | +1.02% | -7.78% | +0 |
| 9 | Weekly Google Trends Surge In Diy Electronics Repair Signals Tech Consumer Stress Lift | crazy | +0.08% | -8.72% | +0 |
| 10 | Weekly Surge In Google Trends Searches For Diy Electronics Repair Signals Bullish Xlk | crazy | +0.08% | -8.72% | +0 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 319 | Copper Momentum | crazy | -2.50% | -11.30% | -61 |
| 320 | Port Container Volume | crazy | -2.83% | -11.63% | -61 |
| 321 | VIX Fear Rotation | crazy | -3.44% | -12.24% | -57 |
| 322 | Electricity Consumption | crazy | -4.89% | -13.68% | -57 |
| 323 | Chaos Rotation Lab | crazy | -6.03% | -14.83% | n/a |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +4.59%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | standard | +11.05% | +6.46% |
| 2 | VIX Fear Rotation | crazy | +4.65% | +0.06% |
| 3 | VIX Term Structure | crazy | +4.50% | -0.09% |
| 4 | Uber Mobility Index | crazy | +3.98% | -0.61% |
| 5 | Retail Sales Momentum | crazy | +3.95% | -0.64% |
| 6 | Faber Momentum Rotation | standard | +3.75% | -0.84% |
| 7 | Antonacci Dual Momentum Sector Rotation | standard | +2.54% | -2.05% |
| 8 | Job Posting Acceleration | crazy | +2.37% | -2.22% |
| 9 | Algo Biscotti (Unconditional Loyalty) (alt) | crazy | +1.97% | -2.62% |
| 10 | Algo Baileymol (Chaos Monger) | standard | +1.92% | -2.67% |

## Sector Consensus
- Top Bullish: XLK, XLB, XLE
- Top Bearish: XLV, XLC, XLRE

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 12 of 37 | BEARISH | 32% |
| XLB | Basic Materials | 7 of 36 | BEARISH | 19% |
| XLE | Energy | 6 of 34 | BEARISH | 18% |
| XLP | Consumer Defensive | 6 of 35 | BEARISH | 17% |
| XLI | Industrials | 8 of 49 | BEARISH | 16% |
| XLU | Utilities | 5 of 41 | BEARISH | 12% |
| XLY | Consumer Cyclical | 6 of 58 | BEARISH | 10% |
| XLF | Financial Services | 2 of 35 | BEARISH | 6% |
| XLV | Healthcare | 2 of 38 | BEARISH | 5% |
| XLRE | Real Estate | 1 of 33 | BEARISH | 3% |
| XLC | Communication Services | 1 of 31 | BEARISH | 3% |

## Content Facts
- Signal of day: Quantified Simple Monthly Rotation (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK BEARISH (Highest bullish percentage in precomputed sector consensus)
- Failure of day: Chaos Rotation Lab (Lowest full-window force rank)

## Notable Divergences
- VIX Fear Rotation: force rank #321, rolling 30D rank #2. Strong recent 30D rank despite weaker full-window force rank.
- VIX Term Structure: force rank #316, rolling 30D rank #3. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty) (alt): force rank #314, rolling 30D rank #9. Strong recent 30D rank despite weaker full-window force rank.
- Oil Price Momentum Reversal Energy Sector Bounce: force rank #267, rolling 30D rank #19. Strong recent 30D rank despite weaker full-window force rank.
- Healthcare Cost Shock Google Search Spike: force rank #303, rolling 30D rank #55. Strong recent 30D rank despite weaker full-window force rank.

