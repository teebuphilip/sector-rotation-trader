# Communications Sector Rss News Count Spike

**Idea ID:** `communications-sector-rss-news-count-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Sudden jumps in news volume around communications companies often precede volatility and price moves. Increased news flow signals potential corporate developments or earnings surprises.

## Universe
- XLC

## Data Sources
- RSS feed counts of major telecom and media news mentions mapped to XLC weekly

## Signal Logic
If weekly RSS news mentions rise >40% compared to prior 4-week average

## Entry / Exit
Entry: If weekly RSS news mentions rise >40% compared to prior 4-week average Exit: After 3 weeks or 4% price gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts of major telecom and media news mentions mapped to XLC weekly via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Communications news volume fluctuates often with corporate activity.

## Required Keys
- None
