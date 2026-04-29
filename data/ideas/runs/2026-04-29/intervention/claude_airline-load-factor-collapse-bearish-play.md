# Airline Load Factor Collapse Bearish Play

**Idea ID:** `airline-load-factor-collapse-bearish-play`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When load factors (seats sold / seats available) drop 3+ percentage points week-over-week, airlines cut capacity and raise fares; near-term bookings weaken, signaling demand deterioration. Airline load factor weakness signals recession-like travel demand pullback affecting leisure and hospitality.

## Universe
- XLY

## Data Sources
- BTS weekly airline load factor via bts_airline_load_factor adapter

## Signal Logic
If weekly BTS load factor falls 3+ points vs. prior week and falls below its 8-week rolling average

## Entry / Exit
Entry: If weekly BTS load factor falls 3+ points vs. prior week and falls below its 8-week rolling average Exit: After 4 weeks or when load factor recovers 2+ points from entry level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS weekly airline load factor via bts_airline_load_factor adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Load factor swings of 3+ points occur most months; seasonal dips create reliable signal fire.

## Required Keys
- None
