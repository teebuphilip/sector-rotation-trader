# Corporate Debt Maturity Wall Rss Count Surge

**Idea ID:** `corporate-debt-maturity-wall-rss-count-surge`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily RSS mentions of corporate debt maturity risks spike >3x the rolling 30-day mean, media focus on refinancing pressure builds, signaling near-term credit stress and equity weakness. Debt refinancing anxiety pressures financial sector valuations and bank credit portfolios.

## Universe
- XLF

## Data Sources
- RSS feeds from financial news (Bloomberg, Reuters, WSJ) filtered for 'debt maturity' and 'refinance risk' mentions

## Signal Logic
If daily RSS count for 'debt maturity' OR 'refinance risk' exceeds 3x the 30-day rolling median

## Entry / Exit
Entry: If daily RSS count for 'debt maturity' OR 'refinance risk' exceeds 3x the 30-day rolling median Exit: After 7 trading days or when RSS mention count returns to rolling baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feeds from financial news (Bloomberg, Reuters, WSJ) filtered for 'debt maturity' and 'refinance risk' mentions via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Debt walls and refinancing cycles trigger news surges 2-3 times per quarter; Q1 and Q4 earnings-driven volatility ensures frequent signals.

## Required Keys
- None
