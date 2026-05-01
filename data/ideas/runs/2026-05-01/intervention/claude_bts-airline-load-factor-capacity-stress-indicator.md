# Bts Airline Load Factor Capacity Stress Indicator

**Idea ID:** `bts-airline-load-factor-capacity-stress-indicator`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When airline load factors exceed 88% and rise >2 percentage points week-over-week, it signals capacity stress and pricing power, supporting airline stock but stressing seat availability and customer satisfaction. High load factors indicate pricing strength and full planes; airlines benefit from margin expansion.

## Universe
- XLY

## Data Sources
- BTS (Bureau of Transportation Statistics) airline load factor (passenger utilization %) weekly through bts_airline_load_factor adapter

## Signal Logic
If weekly load factor >88% AND increases >2 pts from prior week, long XLY

## Entry / Exit
Entry: If weekly load factor >88% AND increases >2 pts from prior week, long XLY Exit: After 8 trading days or if load factor falls below 86%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS (Bureau of Transportation Statistics) airline load factor (passenger utilization %) weekly through bts_airline_load_factor adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Peak travel seasons and capacity constraints drive load factors >88% regularly; fires 4–6 times annually.

## Required Keys
- None
