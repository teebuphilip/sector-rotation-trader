# Deep Validation Report - 2026-04-24

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 115
- Force-ranked beating SPY: 2 of 115
- Rolling 30D algos: 116
- Rolling 30D beating SPY: 0 of 116
- Signals generated: 115
- Tickers covered: 105
- Sectors computed: 11

## Force Rank
Full-window/since-seed rank; not the same as recent 30D performance.

### Top 10
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 1 | Algo Baileymol (Chaos Monger) | normal | +6.50% | +2.31% | +109 |
| 2 | Antonacci Dual Momentum Sector Rotation | normal | +4.85% | +0.66% | +0 |
| 3 | Faber Momentum Rotation | normal | +3.85% | -0.34% | +0 |
| 4 | FINRA Dark Pool Signal | crazy | +1.75% | -2.43% | +0 |
| 5 | Uber Mobility Index | crazy | +1.16% | -3.03% | +0 |
| 6 | Insider Trading Signals | crazy | +1.11% | -3.08% | +0 |
| 7 | Retail Sales Momentum | crazy | +0.55% | -3.63% | +96 |
| 8 | Mortgage Rate Housing Proxy | crazy | +0.52% | -3.67% | -1 |
| 9 | Earthquake Aftershock Amplifier | crazy | +0.05% | -4.14% | -1 |
| 10 | Semiconductor Moonshot Warning | crazy | +0.05% | -4.14% | -1 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 111 | Algo Biscotti (Unconditional Loyalty) | normal | -1.15% | -5.33% | -2 |
| 112 | Algo Biscotti (Unconditional Loyalty) | crazy | -1.99% | -6.18% | -3 |
| 113 | VIX Term Structure | crazy | -5.45% | -9.64% | -2 |
| 114 | Chaos Rotation Lab | crazy | -6.23% | -10.42% | -4 |
| 115 | VIX Fear Rotation | crazy | -7.25% | -11.44% | -3 |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +8.46%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Algo Baileymol (Chaos Monger) | standard | +7.30% | -1.16% |
| 2 | Algo Biscotti (Unconditional Loyalty) | standard | +6.56% | -1.90% |
| 3 | VIX Term Structure | crazy | +4.45% | -4.01% |
| 4 | Antonacci Dual Momentum Sector Rotation | standard | +3.68% | -4.78% |
| 5 | Algo Biscotti (Unconditional Loyalty) | crazy | +2.62% | -5.84% |
| 6 | Chaos Rotation Lab | crazy | +1.99% | -6.47% |
| 7 | FINRA Dark Pool Signal | crazy | +1.75% | -6.71% |
| 8 | VIX Fear Rotation | crazy | +1.35% | -7.11% |
| 9 | Uber Mobility Index | crazy | +1.16% | -7.31% |
| 10 | Insider Trading Signals | crazy | +1.11% | -7.35% |

## Sector Consensus
- Top Bullish: XLK, XLI, XLP
- Top Bearish: XLE, XLV, XLF

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 6 of 19 | BEARISH | 32% |
| XLP | Consumer Defensive | 5 of 18 | BEARISH | 28% |
| XLI | Industrials | 5 of 18 | BEARISH | 28% |
| XLY | Consumer Cyclical | 5 of 22 | BEARISH | 23% |
| XLB | Basic Materials | 4 of 21 | BEARISH | 19% |
| XLU | Utilities | 3 of 19 | BEARISH | 16% |
| XLRE | Real Estate | 1 of 18 | BEARISH | 6% |
| XLE | Energy | 1 of 20 | BEARISH | 5% |
| XLC | Communication Services | 1 of 19 | BEARISH | 5% |
| XLV | Healthcare | 0 of 20 | BEARISH | 0% |
| XLF | Financial Services | 0 of 17 | BEARISH | 0% |

## Content Facts
- Signal of day: Algo Baileymol (Chaos Monger) (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK BEARISH (Highest bullish percentage in precomputed sector consensus)
- Failure of day: VIX Fear Rotation (Lowest full-window force rank)

## Notable Divergences
- Faber Momentum Rotation: force rank #3, rolling 30D rank #116. Strong full-window force rank but weaker recent 30D rank.
- VIX Term Structure: force rank #113, rolling 30D rank #3. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty): force rank #111, rolling 30D rank #2. Strong recent 30D rank despite weaker full-window force rank.
- Chaos Rotation Lab: force rank #114, rolling 30D rank #6. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty): force rank #112, rolling 30D rank #5. Strong recent 30D rank despite weaker full-window force rank.

