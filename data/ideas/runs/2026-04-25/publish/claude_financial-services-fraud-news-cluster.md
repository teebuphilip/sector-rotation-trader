# Financial Services Fraud News Cluster

**Idea ID:** `financial-services-fraud-news-cluster`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Elevated fraud news clusters indicate regulatory scrutiny cycles and compliance cost inflation for financial services, driving sector rotation and risk repricing. Fraud clusters trigger regulatory crackdowns and compliance cost spikes, pressuring financial services profitability and valuation multiples.

## Universe
- XLF

## Data Sources
- RSS feed count from financial crime and regulatory news sources, daily article count mentioning fraud cases and SEC enforcement

## Signal Logic
If 5-day rolling count of fraud/enforcement news exceeds 8 and is 55% above 60-day average

## Entry / Exit
Entry: If 5-day rolling count of fraud/enforcement news exceeds 8 and is 55% above 60-day average Exit: After 11 trading days or if fraud news count drops below 60-day average for 3 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count from financial crime and regulatory news sources, daily article count mentioning fraud cases and SEC enforcement via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Regulatory and fraud news is continuous; enforcement action clusters naturally occur throughout the year as regulators work through investigation pipelines.

## Required Keys
- None
