# Rss Feed Count Surge On Freight Congestion News Triggers Bearish Logistics Rotation

**Idea ID:** `rss-feed-count-surge-on-freight-congestion-news-triggers-bea`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When logistics/freight RSS mentions spike (>25% daily jump), transportation bottlenecks are intensifying. This predicts higher costs and demand headwinds. Industrial transport and logistics companies face margin pressure; supply-chain stress triggers sector rotation out of cyclicals.

## Universe
- XLI

## Data Sources
- RSS feed count aggregation for 'freight congestion', 'trucking backlog', 'port delay' across major logistics news feeds

## Signal Logic
RSS count for freight/congestion keywords jumps >25% day-over-day; IYT (transportation ETF) closes down >1% same day

## Entry / Exit
Entry: RSS count for freight/congestion keywords jumps >25% day-over-day; IYT (transportation ETF) closes down >1% same day Exit: IYT closes up >1.2% from entry or 5 trading days elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed count aggregation for 'freight congestion', 'trucking backlog', 'port delay' across major logistics news feeds via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight news volatility generates >25% RSS spikes 1–2 times per week on average.

## Required Keys
- None
