# Deep Validation Report - 2026-04-24

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 133
- Force-ranked beating SPY: 2 of 133
- Rolling 30D algos: 134
- Rolling 30D beating SPY: 0 of 134
- Signals generated: 133
- Tickers covered: 105
- Sectors computed: 11

## Force Rank
Full-window/since-seed rank; not the same as recent 30D performance.

### Top 10
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 1 | Algo Baileymol (Chaos Monger) | normal | +7.06% | +2.28% | +109 |
| 2 | Antonacci Dual Momentum Sector Rotation | normal | +5.29% | +0.50% | +0 |
| 3 | Faber Momentum Rotation | normal | +3.85% | -0.94% | +0 |
| 4 | FINRA Dark Pool Signal | crazy | +1.62% | -3.17% | +0 |
| 5 | Retail Sales Momentum | crazy | +1.14% | -3.65% | +98 |
| 6 | Uber Mobility Index | crazy | +1.00% | -3.79% | -1 |
| 7 | Insider Trading Signals | crazy | +0.84% | -3.95% | -1 |
| 8 | Mortgage Rate Housing Proxy | crazy | +0.37% | -4.42% | -1 |
| 9 | Earthquake Aftershock Amplifier | crazy | +0.05% | -4.74% | -1 |
| 10 | Semiconductor Moonshot Warning | crazy | +0.05% | -4.74% | -1 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 129 | Algo Biscotti (Unconditional Loyalty) | normal | -1.04% | -5.83% | -20 |
| 130 | Algo Biscotti (Unconditional Loyalty) | crazy | -2.51% | -7.30% | -21 |
| 131 | VIX Term Structure | crazy | -4.88% | -9.67% | -20 |
| 132 | Chaos Rotation Lab | crazy | -6.23% | -11.02% | -22 |
| 133 | VIX Fear Rotation | crazy | -6.70% | -11.49% | -21 |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: +8.70%

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Algo Baileymol (Chaos Monger) | standard | +7.87% | -0.83% |
| 2 | Algo Biscotti (Unconditional Loyalty) | standard | +6.68% | -2.02% |
| 3 | VIX Term Structure | crazy | +5.08% | -3.62% |
| 4 | Antonacci Dual Momentum Sector Rotation | standard | +4.13% | -4.57% |
| 5 | Algo Biscotti (Unconditional Loyalty) | crazy | +2.08% | -6.61% |
| 6 | Chaos Rotation Lab | crazy | +1.99% | -6.70% |
| 7 | VIX Fear Rotation | crazy | +1.96% | -6.74% |
| 8 | FINRA Dark Pool Signal | crazy | +1.62% | -7.08% |
| 9 | Retail Sales Momentum | crazy | +1.14% | -7.56% |
| 10 | Uber Mobility Index | crazy | +1.00% | -7.69% |

## Sector Consensus
- Top Bullish: XLK, XLP, XLY
- Top Bearish: XLRE, XLV, XLF

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 7 of 19 | MIXED | 37% |
| XLP | Consumer Defensive | 6 of 19 | BEARISH | 32% |
| XLY | Consumer Cyclical | 5 of 23 | BEARISH | 22% |
| XLU | Utilities | 4 of 19 | BEARISH | 21% |
| XLI | Industrials | 4 of 22 | BEARISH | 18% |
| XLB | Basic Materials | 3 of 20 | BEARISH | 15% |
| XLRE | Real Estate | 1 of 19 | BEARISH | 5% |
| XLE | Energy | 1 of 20 | BEARISH | 5% |
| XLC | Communication Services | 1 of 19 | BEARISH | 5% |
| XLV | Healthcare | 0 of 20 | BEARISH | 0% |
| XLF | Financial Services | 0 of 18 | BEARISH | 0% |

## Content Facts
- Signal of day: Algo Baileymol (Chaos Monger) (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK MIXED (Highest bullish percentage in precomputed sector consensus)
- Failure of day: VIX Fear Rotation (Lowest full-window force rank)

## Notable Divergences
- Faber Momentum Rotation: force rank #3, rolling 30D rank #134. Strong full-window force rank but weaker recent 30D rank.
- VIX Term Structure: force rank #131, rolling 30D rank #3. Strong recent 30D rank despite weaker full-window force rank.
- Algo Biscotti (Unconditional Loyalty): force rank #129, rolling 30D rank #2. Strong recent 30D rank despite weaker full-window force rank.
- Chaos Rotation Lab: force rank #132, rolling 30D rank #6. Strong recent 30D rank despite weaker full-window force rank.
- VIX Fear Rotation: force rank #133, rolling 30D rank #7. Strong recent 30D rank despite weaker full-window force rank.

