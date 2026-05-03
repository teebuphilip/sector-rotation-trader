# Rss News Volume Spike On Food Supply Chain Disruptions

**Idea ID:** `rss-news-volume-spike-on-food-supply-chain-disruptions`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in food supply chain disruption news coverage signal pricing pressure and logistics cost inflation, typically benefiting transportation and energy stocks while pressuring consumer staples margins. Food supply disruptions compress staples margins and force price increases that reduce consumer purchasing power.

## Universe
- XLP

## Data Sources
- RSS feed count aggregation for keywords: 'food supply', 'crop failure', 'transportation delay' from logistics/agriculture news feeds; weekly volume comparison

## Signal Logic
If weekly RSS article count for supply chain keywords exceeds 50-article threshold and is >30% above 4-week average

## Entry / Exit
Entry: If weekly RSS article count for supply chain keywords exceeds 50-article threshold and is >30% above 4-week average Exit: Exit after 8 trading days or if article volume returns below 35-article weekly run rate

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count aggregation for keywords: 'food supply', 'crop failure', 'transportation delay' from logistics/agriculture news feeds; weekly volume comparison via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Agricultural and logistics disruptions occur seasonally; weather, pest outbreaks, and transport strikes trigger multiple events per quarter.

## Required Keys
- None
