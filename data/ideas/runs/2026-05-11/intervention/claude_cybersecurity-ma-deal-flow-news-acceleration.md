# Cybersecurity Ma Deal Flow News Acceleration

**Idea ID:** `cybersecurity-ma-deal-flow-news-acceleration`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily RSS count for cybersecurity acquisition/investment news spikes 100%+ above 15-day baseline, it signals sector consolidation momentum and risk appetite for XLK. Cybersecurity M&A acceleration signals strong enterprise IT budgets and security investment tailwinds for software and tech sector.

## Universe
- XLK

## Data Sources
- RSS feed count from tech/security deal outlets (Crunchbase, Deal Reporter) for cybersecurity M&A via rss_count adapter

## Signal Logic
If cybersecurity M&A RSS count exceeds 15-day average by 100%

## Entry / Exit
Entry: If cybersecurity M&A RSS count exceeds 15-day average by 100% Exit: After 10 trading days or if count reverts to <110% of baseline for 2 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count from tech/security deal outlets (Crunchbase, Deal Reporter) for cybersecurity M&A via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cybersecurity deal flow is constant; news spikes fire weekly when major breaches occur or strategic buyers announce campaigns.

## Required Keys
- None
