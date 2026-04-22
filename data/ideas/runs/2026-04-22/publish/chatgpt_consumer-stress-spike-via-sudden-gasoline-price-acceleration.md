# Consumer Stress Spike Via Sudden Gasoline Price Acceleration

**Idea ID:** `consumer-stress-spike-via-sudden-gasoline-price-acceleration`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rapid gasoline price increases quickly raise consumer stress and reduce discretionary spending ability. Consumer staples may see margin pressure as consumers trade down or cut other expenses.

## Universe
- XLP

## Data Sources
- FRED weekly gasoline prices series

## Signal Logic
Enter short XLP when weekly gasoline prices rise >4% WoW

## Entry / Exit
Entry: Enter short XLP when weekly gasoline prices rise >4% WoW Exit: Exit after 4 weeks or price growth slows below 1% WoW

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly gasoline prices series via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Gas price weekly spikes >4% occur multiple times annually in volatile energy markets.

## Required Keys
- None
