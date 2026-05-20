# Deep Validation Report - 2026-05-20

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 304 rows (304 unique algo_ids)
- Force-ranked beating SPY: 3 of 304 rows
- Rolling 30D algos: 305 rows (305 unique algo_ids)
- Rolling 30D beating SPY: 2 of 305 rows
- Signals generated: 304
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
| 1 | Quantified Simple Monthly Rotation | normal | +8.60% | +0.91% | +0 |
| 2 | Algo Baileymol (Chaos Monger) | normal | +8.23% | +0.54% | +264 |
| 3 | Faber Momentum Rotation | normal | +7.76% | +0.07% | +0 |
| 4 | Antonacci Dual Momentum Sector Rotation | normal | +6.06% | -1.64% | +0 |
| 5 | Uber Mobility Index | crazy | +2.12% | -5.58% | +0 |
| 6 | Retail Sales Momentum | crazy | +2.11% | -5.59% | +0 |
| 7 | Insider Trading Signals | crazy | +1.35% | -6.34% | +1 |
| 8 | Job Posting Acceleration | crazy | +0.69% | -7.01% | -1 |
| 9 | Misery Rotation | crazy | +0.20% | -7.50% | +243 |
| 10 | Housing Permit Velocity | crazy | +0.17% | -7.52% | +243 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 300 | Copper Momentum | crazy | -3.50% | -11.19% | -42 |
| 301 | Port Container Volume | crazy | -3.80% | -11.49% | -42 |
| 302 | VIX Fear Rotation | crazy | -5.15% | -12.84% | -38 |
| 303 | Electricity Consumption | crazy | -5.83% | -13.53% | -38 |
| 304 | Chaos Rotation Lab | crazy | -5.96% | -13.65% | n/a |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +3.53%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Quantified Simple Monthly Rotation | standard | +8.60% | +5.07% |
| 2 | Faber Momentum Rotation | standard | +3.77% | +0.24% |
| 3 | VIX Fear Rotation | crazy | +2.80% | -0.72% |
| 4 | VIX Term Structure | crazy | +2.66% | -0.87% |
| 5 | Antonacci Dual Momentum Sector Rotation | standard | +2.26% | -1.27% |
| 6 | Uber Mobility Index | crazy | +2.14% | -1.39% |
| 7 | Retail Sales Momentum | crazy | +2.11% | -1.42% |
| 8 | Algo Biscotti (Unconditional Loyalty) | crazy | +2.10% | -1.43% |
| 9 | Algo Baileymol (Chaos Monger) | standard | +2.00% | -1.53% |
| 10 | Insider Trading Signals | crazy | +1.35% | -2.18% |

## Sector Consensus
- Top Bullish: XLK, XLE, XLI
- Top Bearish: XLC, XLRE, XLF

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 12 of 38 | BEARISH | 32% |
| XLE | Energy | 6 of 34 | BEARISH | 18% |
| XLP | Consumer Defensive | 6 of 37 | BEARISH | 16% |
| XLI | Industrials | 8 of 50 | BEARISH | 16% |
| XLB | Basic Materials | 6 of 37 | BEARISH | 16% |
| XLU | Utilities | 5 of 43 | BEARISH | 12% |
| XLY | Consumer Cyclical | 5 of 60 | BEARISH | 8% |
| XLV | Healthcare | 2 of 40 | BEARISH | 5% |
| XLRE | Real Estate | 1 of 35 | BEARISH | 3% |
| XLC | Communication Services | 1 of 33 | BEARISH | 3% |
| XLF | Financial Services | 0 of 36 | BEARISH | 0% |

## Content Facts
- Signal of day: Quantified Simple Monthly Rotation (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK BEARISH (Highest bullish percentage in precomputed sector consensus)
- Failure of day: Chaos Rotation Lab (Lowest full-window force rank)

## Notable Divergences
- VIX Fear Rotation: force rank #302, rolling 30D rank #3. Strong recent 30D rank despite weaker full-window force rank.
- VIX Term Structure: force rank #299, rolling 30D rank #4. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty): force rank #294, rolling 30D rank #8. Strong recent 30D rank despite weaker full-window force rank.
- Xle Weekly Drawdown Rebound Signal: force rank #280, rolling 30D rank #21. Strong recent 30D rank despite weaker full-window force rank.
- Healthcare Cost Shock Google Search Spike: force rank #285, rolling 30D rank #53. Strong recent 30D rank despite weaker full-window force rank.

