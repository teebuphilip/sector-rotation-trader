# Renewable Energy Rss News Volume Surge

**Idea ID:** `renewable-energy-rss-news-volume-surge`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly renewable energy news story counts spike 50%+ above 12-week moving average, it correlates with policy announcements, funding approvals, and sector rotation momentum. Renewable energy news volume spikes often precede clean tech capex cycles and utility renewable procurement announcements.

## Universe
- XLI

## Data Sources
- RSS/news feed counts for clean energy, solar, and wind keywords via rss_count adapter, weekly aggregation

## Signal Logic
When weekly clean energy RSS count exceeds 12-week average by 50% or more

## Entry / Exit
Entry: When weekly clean energy RSS count exceeds 12-week average by 50% or more Exit: After 10 trading days or when story count reverts to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS/news feed counts for clean energy, solar, and wind keywords via rss_count adapter, weekly aggregation via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Renewable energy news volume is volatile and tied to policy cycles; spikes occur 2-4 times per quarter.

## Required Keys
- None
