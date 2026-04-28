# Airline Load Factor Stress Pricing Power Collapse

**Idea ID:** `airline-load-factor-stress-pricing-power-collapse`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly airline load factor (% seats filled) falls >2.5% from prior 4-week rolling average while available seat miles remain flat, pricing power collapses. Carriers cut fares and margins compress. Load factor collapse signals consumer travel demand softness and forces airlines to discount capacity, eroding margins and reducing equity valuations.

## Universe
- XLI

## Data Sources
- BTS airline load factor and available seat miles via FRED/BTS adapter, weekly series

## Signal Logic
Weekly load factor >2.5% below 4-week rolling average AND seat miles YoY flat to +1%

## Entry / Exit
Entry: Weekly load factor >2.5% below 4-week rolling average AND seat miles YoY flat to +1% Exit: Load factor rebounds above 4-week rolling mean or 14 trading days elapsed

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS airline load factor and available seat miles via FRED/BTS adapter, weekly series via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Airline load factors fluctuate seasonally; 2.5% swings occur 6–8 times annually. Trigger is sensitive enough to fire multiple times per quarter.

## Required Keys
- None
