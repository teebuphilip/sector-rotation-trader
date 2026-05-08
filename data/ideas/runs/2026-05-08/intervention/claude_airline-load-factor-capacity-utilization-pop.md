# Airline Load Factor Capacity Utilization Pop

**Idea ID:** `airline-load-factor-capacity-utilization-pop`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When reported airline load factors exceed 85% (monthly BTS release), it signals demand strength. Consumer discretionary and hospitality stocks rally 3-7 days after release as investor sentiment shifts toward travel and leisure demand confidence. High airline load factors indicate strong leisure/business travel demand, benefiting consumer discretionary spending and hospitality valuations.

## Universe
- XLY

## Data Sources
- BTS Airline Load Factor (monthly via bts_airline_load_factor adapter) and XLY price_only daily

## Signal Logic
BTS monthly load factor >85%; enter long XLY one trading day after release

## Entry / Exit
Entry: BTS monthly load factor >85%; enter long XLY one trading day after release Exit: After 7 trading days OR if next month's load factor prints <82%, whichever first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use BTS Airline Load Factor (monthly via bts_airline_load_factor adapter) and XLY price_only daily via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: BTS releases load factor data monthly; capacity is consistently 83-87% in normal markets; seasonality creates predictable cycles; 7-day window captures post-release momentum.

## Required Keys
- None
