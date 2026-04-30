# Airline Load Factor Decline Stress Test

**Idea ID:** `airline-load-factor-decline-stress-test`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly average airline load factor drops 3%+ from prior week, signaling sudden demand weakness or capacity glut in air travel. Airline load factor collapse signals consumer travel pullback and discretionary spending recession.

## Universe
- XLY

## Data Sources
- BTS (Bureau of Transportation Statistics) airline load factor and capacity reports through bts_airline_load_factor adapter

## Signal Logic
If latest week load factor is 3%+ below prior week and below 52-week median

## Entry / Exit
Entry: If latest week load factor is 3%+ below prior week and below 52-week median Exit: After 7 trading days or once load factor recovers to within 1% of prior-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS (Bureau of Transportation Statistics) airline load factor and capacity reports through bts_airline_load_factor adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Load factors are volatile week-to-week due to seasonality; 3% drops occur 1-2 times monthly on average.

## Required Keys
- None
