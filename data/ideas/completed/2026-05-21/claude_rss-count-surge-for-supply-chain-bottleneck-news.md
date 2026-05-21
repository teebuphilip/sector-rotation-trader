# Rss Count Surge For Supply Chain Bottleneck News

**Idea ID:** `rss-count-surge-for-supply-chain-bottleneck-news`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily RSS article count for supply chain topics spikes >60% above 7-day MA, signaling acute logistics stress in news cycle. Supply chain stress in news correlates with logistics cost inflation, manufacturing delays, and earnings miss risk for industrials.

## Universe
- XLI

## Data Sources
- RSS feed article count for 'supply chain delay', 'port congestion', 'container shortage' via rss_count adapter

## Signal Logic
If daily RSS count exceeds 7-day MA by >60% and closes above prior day

## Entry / Exit
Entry: If daily RSS count exceeds 7-day MA by >60% and closes above prior day Exit: After 5 trading days or when RSS count falls below 7-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed article count for 'supply chain delay', 'port congestion', 'container shortage' via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Supply chain news is frequent and volatile; 60% daily spikes occur 2-3 times per month due to seasonal or weather shocks.

## Required Keys
- None
