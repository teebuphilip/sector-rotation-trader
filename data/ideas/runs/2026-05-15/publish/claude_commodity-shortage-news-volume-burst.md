# Commodity Shortage News Volume Burst

**Idea ID:** `commodity-shortage-news-volume-burst`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily spike in supply chain and commodity shortage news mentions signals market anxiety about logistics constraints and inflation. Shortage narratives boost commodity and materials equity valuations as investors price in scarcity premiums.

## Universe
- XLB

## Data Sources
- RSS/news feed count for 'supply chain bottleneck' and 'commodity shortage' articles via rss_count adapter

## Signal Logic
If daily news article count for 'supply chain' OR 'commodity shortage' exceeds 90-day median by 60% or more

## Entry / Exit
Entry: If daily news article count for 'supply chain' OR 'commodity shortage' exceeds 90-day median by 60% or more Exit: Exit after 5 trading days or when article count falls to median

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS/news feed count for 'supply chain bottleneck' and 'commodity shortage' articles via rss_count adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Geopolitical events, weather, and logistics disruptions reliably produce supply chain news spikes weekly.

## Required Keys
- None
