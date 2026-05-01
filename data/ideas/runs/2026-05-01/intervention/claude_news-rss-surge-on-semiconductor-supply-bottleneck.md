# News Rss Surge On Semiconductor Supply Bottleneck

**Idea ID:** `news-rss-surge-on-semiconductor-supply-bottleneck`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Spikes in news article volume about semiconductor supply constraints correlate with short-term panic selling in tech and industrial sectors, creating oversold rebound opportunities. Extreme attention to chip shortages often precedes capitulation and technical rebound in semiconductor-exposed tech.

## Universe
- XLK

## Data Sources
- RSS feed article count (via rss_count adapter) filtering for 'semiconductor shortage' + 'chip supply' from major tech/finance outlets, daily

## Signal Logic
If daily RSS article count on semiconductor bottleneck exceeds 50 articles and is 2 standard deviations above 30-day mean

## Entry / Exit
Entry: If daily RSS article count on semiconductor bottleneck exceeds 50 articles and is 2 standard deviations above 30-day mean Exit: After 6 trading days or if article count falls below 20

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed article count (via rss_count adapter) filtering for 'semiconductor shortage' + 'chip supply' from major tech/finance outlets, daily via scrape (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Supply chain disruption narratives resurge monthly; 50+ articles in a day fires multiple times per quarter.

## Required Keys
- None
