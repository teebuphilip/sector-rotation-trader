# Airline Load Factor Collapse Fear Trade

**Idea ID:** `airline-load-factor-collapse-fear-trade`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp 2+ week drop in airline load factors signals demand weakness and signals bearish travel/discretionary sentiment. Airline load factor collapse is a leading indicator of consumer travel pullback and discretionary spending weakness.

## Universe
- XLY

## Data Sources
- BTS airline load factor and capacity data weekly aggregation

## Signal Logic
If weekly airline load factor drops 2+ points below its 8-week moving average

## Entry / Exit
Entry: If weekly airline load factor drops 2+ points below its 8-week moving average Exit: Exit after 3 weeks or when load factor rebounds above 8-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline load factor and capacity data weekly aggregation via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal travel demand swings and economic uncertainty produce 3–4 load factor dips per year of 2+ points.

## Required Keys
- None
