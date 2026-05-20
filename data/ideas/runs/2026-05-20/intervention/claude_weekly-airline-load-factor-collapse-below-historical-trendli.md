# Weekly Airline Load Factor Collapse Below Historical Trendline

**Idea ID:** `weekly-airline-load-factor-collapse-below-historical-trendli`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rapid load factor deterioration signals demand destruction and pricing power loss in leisure/business travel; precedes XLY and XLC weakness. Airline load factor collapse indicates consumer travel pullback and leisure spending compression.

## Universe
- XLY

## Data Sources
- BTS (Bureau of Transportation Statistics) weekly airline load factor via bts_airline_load_factor adapter

## Signal Logic
When weekly load factor falls 4% or more below the 13-week rolling average

## Entry / Exit
Entry: When weekly load factor falls 4% or more below the 13-week rolling average Exit: After 14 trading days or once load factor returns within 1.5% of rolling average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS (Bureau of Transportation Statistics) weekly airline load factor via bts_airline_load_factor adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal travel demand swings and economic cycles drive regular 4%+ dips; fires 2–3 times per quarter.

## Required Keys
- None
