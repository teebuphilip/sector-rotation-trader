# Airline Load Factor Contraction Fare Collapse Signal

**Idea ID:** `airline-load-factor-contraction-fare-collapse-signal`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When airline load factors drop >5% week-over-week, it signals weakening travel demand and airlines will cut fares aggressively, pressuring XLY and supporting XLP. Falling load factors and fare wars erode airline and leisure travel margins; consumer is trading down or reducing discretionary trips.

## Universe
- XLY

## Data Sources
- BTS (Bureau of Transportation Statistics) weekly airline load factor data via bts_airline_load_factor adapter

## Signal Logic
If weekly load factor falls >5% WoW and is below 12-week MA

## Entry / Exit
Entry: If weekly load factor falls >5% WoW and is below 12-week MA Exit: After 4 weeks or when load factor recovers above 12-week MA for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS (Bureau of Transportation Statistics) weekly airline load factor data via bts_airline_load_factor adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal travel patterns and economic news cause load factor swings monthly; signal fires 2–4 times per quarter.

## Required Keys
- None
