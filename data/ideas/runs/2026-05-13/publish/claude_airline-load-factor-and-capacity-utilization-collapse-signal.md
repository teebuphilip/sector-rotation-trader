# Airline Load Factor And Capacity Utilization Collapse Signals Travel Demand Destruction

**Idea ID:** `airline-load-factor-and-capacity-utilization-collapse-signal`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Airlines cut capacity and load factors fall when bookings weaken. A 4%+ drop in load factor over 2 weeks signals business/leisure travel decline, hitting hospitality, financials, and transportation. Declining load factors indicate reduced corporate travel spending and leisure trips, both core to discretionary consumer and hospitality revenue.

## Universe
- XLY

## Data Sources
- BTS airline load factor and available seat miles via bts_airline_load_factor adapter, weekly aggregates

## Signal Logic
When weekly load factor (all carriers aggregate) declines 4% or more from 4-week moving average

## Entry / Exit
Entry: When weekly load factor (all carriers aggregate) declines 4% or more from 4-week moving average Exit: After 8 trading days or when load factor recovers to within 1% of 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline load factor and available seat miles via bts_airline_load_factor adapter, weekly aggregates via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Airline demand cycles turn seasonally and with economic shocks. Holiday weeks, recession signals, and fuel/macro events regularly produce 4-8% swings in load factor.

## Required Keys
- None
