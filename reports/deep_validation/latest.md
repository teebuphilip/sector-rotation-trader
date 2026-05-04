# Deep Validation Report - 2026-05-04

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 179
- Force-ranked beating SPY: 1 of 179
- Rolling 30D algos: 180
- Rolling 30D beating SPY: 0 of 180
- Signals generated: 179
- Tickers covered: 105
- Sectors computed: 11

## Force Rank
Full-window/since-seed rank; not the same as recent 30D performance.

### Top 10
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 1 | Algo Baileymol (Chaos Monger) | normal | +6.79% | +1.41% | +165 |
| 2 | Faber Momentum Rotation | normal | +4.23% | -1.16% | +0 |
| 3 | Antonacci Dual Momentum Sector Rotation | normal | +3.74% | -1.65% | +0 |
| 4 | Quantified Simple Monthly Rotation | normal | +1.59% | -3.80% | +1 |
| 5 | FINRA Dark Pool Signal | crazy | +0.92% | -4.46% | -1 |
| 6 | Uber Mobility Index | crazy | +0.59% | -4.80% | +1 |
| 7 | Retail Sales Momentum | crazy | +0.58% | -4.81% | +1 |
| 8 | Insider Trading Signals | crazy | +0.43% | -4.96% | -2 |
| 9 | Housing Permit Velocity | crazy | +0.27% | -5.12% | +0 |
| 10 | Mortgage Rate Housing Proxy | crazy | +0.21% | -5.18% | +0 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 175 | Algo Biscotti (Unconditional Loyalty) | crazy | -3.11% | -8.50% | -11 |
| 176 | Algo Biscotti (Unconditional Loyalty) | normal | -3.42% | -8.80% | -12 |
| 177 | VIX Term Structure | crazy | -5.32% | -10.70% | -12 |
| 178 | Chaos Rotation Lab | crazy | -5.87% | -11.26% | -12 |
| 179 | VIX Fear Rotation | crazy | -7.00% | -12.39% | -12 |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +8.97%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Algo Baileymol (Chaos Monger) | standard | +5.34% | -3.63% |
| 2 | Chaos Rotation Lab | crazy | +3.88% | -5.08% |
| 3 | VIX Term Structure | crazy | +3.79% | -5.18% |
| 4 | Antonacci Dual Momentum Sector Rotation | standard | +2.91% | -6.05% |
| 5 | Algo Biscotti (Unconditional Loyalty) | standard | +2.26% | -6.71% |
| 6 | Quantified Simple Monthly Rotation | standard | +1.59% | -7.38% |
| 7 | FINRA Dark Pool Signal | crazy | +0.92% | -8.04% |
| 8 | VIX Fear Rotation | crazy | +0.86% | -8.10% |
| 9 | Uber Mobility Index | crazy | +0.59% | -8.38% |
| 10 | Retail Sales Momentum | crazy | +0.58% | -8.39% |

## Sector Consensus
- Top Bullish: XLK, XLP, XLI
- Top Bearish: XLV, XLRE, XLF

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 11 of 31 | BEARISH | 35% |
| XLP | Consumer Defensive | 6 of 28 | BEARISH | 21% |
| XLU | Utilities | 5 of 29 | BEARISH | 17% |
| XLI | Industrials | 5 of 30 | BEARISH | 17% |
| XLE | Energy | 4 of 28 | BEARISH | 14% |
| XLB | Basic Materials | 4 of 29 | BEARISH | 14% |
| XLY | Consumer Cyclical | 5 of 41 | BEARISH | 12% |
| XLC | Communication Services | 2 of 26 | BEARISH | 8% |
| XLV | Healthcare | 2 of 29 | BEARISH | 7% |
| XLRE | Real Estate | 1 of 27 | BEARISH | 4% |
| XLF | Financial Services | 0 of 29 | BEARISH | 0% |

## Content Facts
- Signal of day: Algo Baileymol (Chaos Monger) (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK BEARISH (Highest bullish percentage in precomputed sector consensus)
- Failure of day: VIX Fear Rotation (Lowest full-window force rank)

## Notable Divergences
- Chaos Rotation Lab: force rank #178, rolling 30D rank #2. Strong recent 30D rank despite weaker full-window force rank.
- VIX Term Structure: force rank #177, rolling 30D rank #3. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty): force rank #176, rolling 30D rank #5. Strong recent 30D rank despite weaker full-window force rank.
- VIX Fear Rotation: force rank #179, rolling 30D rank #8. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty): force rank #175, rolling 30D rank #18. Strong recent 30D rank despite weaker full-window force rank.

