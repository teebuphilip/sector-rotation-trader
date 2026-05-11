# Freight Rail Congestion Rss Volume Explosion

**Idea ID:** `freight-rail-congestion-rss-volume-explosion`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When daily RSS article count on rail congestion/capacity topics spikes 150%+ above 20-day average, it signals logistics bottleneck fear, driving industrial transport stocks. Rail congestion scarcity premiums boost freight carrier revenues and industrial equipment demand for alternative logistics networks.

## Universe
- XLI

## Data Sources
- RSS feed count from freight industry news outlets (FreightWaves, Journal of Commerce) via rss_count adapter

## Signal Logic
If RSS count for rail congestion/capacity articles exceeds 20-day average by 150%

## Entry / Exit
Entry: If RSS count for rail congestion/capacity articles exceeds 20-day average by 150% Exit: After 8 trading days or if RSS count reverts to baseline for 2 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count from freight industry news outlets (FreightWaves, Journal of Commerce) via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Logistics bottlenecks are constant; RSS spikes fire weekly during peak shipping seasons and when derailments or weather shut corridors.

## Required Keys
- None
