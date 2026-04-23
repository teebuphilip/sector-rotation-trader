# Airline Load Factor Compression From Weak Business Travel

**Idea ID:** `airline-load-factor-compression-from-weak-business-travel`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Load factors fall when business travel weakens (corporate cost-cutting, recession fear). Falling load factors below 80% compress airline pricing power, which then ripples into hospitality and leisure discretionary weakness. Load factor compression signals demand destruction in high-margin business travel; airlines cut capacity and pricing, hotels face lower occupancy.

## Universe
- XLY

## Data Sources
- BTS airline load factor (weekly average via bts_airline_load_factor adapter) plus XLY (consumer discretionary) weekly close via price_only adapter

## Signal Logic
If BTS weekly load factor drops >2 percentage points in a single week AND load factor < 81% AND XLY closes below 50-day SMA

## Entry / Exit
Entry: If BTS weekly load factor drops >2 percentage points in a single week AND load factor < 81% AND XLY closes below 50-day SMA Exit: After 14 calendar days OR if load factor recovers above 82% for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline load factor (weekly average via bts_airline_load_factor adapter) plus XLY (consumer discretionary) weekly close via price_only adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal business travel cycles and quarterly earnings cuts trigger load factor drops every 6–8 weeks.

## Required Keys
- None
