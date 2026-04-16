# Deep Validation Report - 2026-04-15

## Definitions
- force_rank: Full-window/since-seed rank from data/rank_history.csv. Use for long-term trust, promotion, demotion, and kill review.
- rolling_30d: Recent trailing 30-day return rank from docs/leaderboards/rolling_30d.json. Use for tactical spotlight and recent momentum.
- sector_consensus: Precomputed sector verdicts from docs/signals/index.json. Use for current directional sector context.

## System State
- Force-ranked algos: 47
- Force-ranked beating SPY: 3 of 47
- Rolling 30D algos: 48
- Rolling 30D beating SPY: 0 of 48
- Signals generated: 47
- Tickers covered: 104
- Sectors computed: 11

## Force Rank
Full-window/since-seed rank; not the same as recent 30D performance.

### Top 10
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 1 | Algo Baileymol (Chaos Monger) | normal | +4.99% | +4.99% | +1 |
| 2 | Faber Momentum Rotation | normal | +3.85% | +3.85% | -1 |
| 3 | Antonacci Dual Momentum Sector Rotation | normal | +2.74% | +2.74% | +0 |
| 4 | Airport Shopping Spree | crazy | +0.00% | +0.00% | +0 |
| 5 | Bankruptcy Filing Rate | crazy | +0.00% | +0.00% | +0 |
| 6 | 311 Call Rotation | crazy | +0.00% | +0.00% | +0 |
| 7 | Cardboard Box Index | crazy | +0.00% | +0.00% | +0 |
| 8 | Cloud Storage Demand Surge | crazy | +0.00% | +0.00% | +0 |
| 9 | Congress Trading Fade | crazy | +0.00% | +0.00% | +0 |
| 10 | Craigslist Desperation Index | crazy | +0.00% | +0.00% | +1 |

### Bottom 5
| Rank | Algo | Type | Return | Alpha vs SPY | Rank Change |
| --- | --- | --- | --- | --- | --- |
| 43 | Consumer Sentiment | crazy | -0.02% | -0.02% | -33 |
| 44 | Liquor Store Leading Indicator | crazy | -0.02% | -0.02% | -24 |
| 45 | Algo Biscotti (Unconditional Loyalty) | normal | -0.53% | -0.53% | +0 |
| 46 | Algo Biscotti (Unconditional Loyalty) | crazy | -4.57% | -4.57% | -1 |
| 47 | Algo Baileymol (Chaos Monger) | crazy | -6.77% | -6.77% | -45 |

## Rolling 30D
Trailing 30-day return rank; useful for recent momentum and tactical spotlight.
SPY 30D: n/a

| Rank | Algo | Category | 30D Return | 30D vs SPY |
| --- | --- | --- | --- | --- |
| 1 | Algo Biscotti (Unconditional Loyalty) | standard | +7.86% | n/a |
| 2 | Algo Baileymol (Chaos Monger) | standard | +6.15% | n/a |
| 3 | Antonacci Dual Momentum Sector Rotation | standard | +2.02% | n/a |
| 4 | Faber Momentum Rotation | standard | +1.47% | n/a |
| 5 | NRWise Acceleration | standard | +0.06% | n/a |
| 6 | Quantified Simple Monthly Rotation | standard | +0.00% | n/a |
| 7 | Reddit Subreddit Mention Spike | crazy | +0.00% | n/a |
| 8 | Cardboard Box Index | crazy | +0.00% | n/a |
| 9 | Reddit Sentiment Spike Trend | crazy | +0.00% | n/a |
| 10 | Crypto Derivative Arbitrage | crazy | +0.00% | n/a |

## Sector Consensus
- Top Bullish: XLK, XLY, XLI
- Top Bearish: XLC, XLB, XLRE

| ETF | Sector | Composite | Label | Bullish % |
| --- | --- | --- | --- | --- |
| XLK | Technology | 4 of 7 | MIXED | 57% |
| XLY | Consumer Cyclical | 3 of 7 | MIXED | 43% |
| XLP | Consumer Defensive | 2 of 7 | BEARISH | 29% |
| XLI | Industrials | 2 of 7 | BEARISH | 29% |
| XLU | Utilities | 1 of 7 | BEARISH | 14% |
| XLE | Energy | 1 of 8 | BEARISH | 12% |
| XLV | Healthcare | 0 of 7 | BEARISH | 0% |
| XLRE | Real Estate | 0 of 7 | BEARISH | 0% |
| XLF | Financial Services | 0 of 7 | BEARISH | 0% |
| XLC | Communication Services | 0 of 7 | BEARISH | 0% |
| XLB | Basic Materials | 0 of 8 | BEARISH | 0% |

## Content Facts
- Signal of day: Algo Biscotti (Unconditional Loyalty) (Ranked #1 on rolling 30D leaderboard)
- Call of day: XLK MIXED (Highest bullish percentage in precomputed sector consensus)
- Failure of day: Algo Baileymol (Chaos Monger) (Lowest full-window force rank)

## Notable Divergences
- Algo Biscotti (Unconditional Loyalty): force rank #45, rolling 30D rank #1. Strong recent 30D rank despite weaker full-window force rank.
- Bankruptcy Filing Rate: force rank #5, rolling 30D rank #41. Strong full-window force rank but weaker recent 30D rank.
- Quantified Simple Monthly Rotation: force rank #42, rolling 30D rank #6. Strong recent 30D rank despite weaker full-window force rank.
- Twitter Sentiment Spike: force rank #38, rolling 30D rank #12. Strong recent 30D rank despite weaker full-window force rank.
- 311 Call Rotation: force rank #6, rolling 30D rank #30. Strong full-window force rank but weaker recent 30D rank.

