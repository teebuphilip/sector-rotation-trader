# Xlb Weekly Rss News Count Spike On Commodity Shortage

**Idea ID:** `xlb-weekly-rss-news-count-spike-on-commodity-shortage`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
News spikes mentioning commodity shortages tend to lift materials sector ETFs as prices rise. Materials ETFs benefit from supply constraints priced in by markets.

## Universe
- XLB

## Data Sources
- RSS news feed counts for commodity shortage keywords

## Signal Logic
Enter long if weekly RSS news count on 'commodity shortage' keywords increases by 50%+ over prior week

## Entry / Exit
Entry: Enter long if weekly RSS news count on 'commodity shortage' keywords increases by 50%+ over prior week Exit: Exit after 3 weeks or if news count declines

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for commodity shortage keywords via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Commodity shortage news stories have frequent bursts especially during supply chain disruptions.

## Required Keys
- None
