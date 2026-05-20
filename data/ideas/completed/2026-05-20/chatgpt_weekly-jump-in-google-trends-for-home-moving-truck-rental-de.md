# Weekly Jump In Google Trends For Home Moving Truck Rental Demand Signals Housing Market Activity

**Idea ID:** `weekly-jump-in-google-trends-for-home-moving-truck-rental-de`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Higher demand for moving truck rentals indicates rising residential relocations and housing market activity. Real estate sector benefits from increased moving demand and housing transactions.

## Universe
- XLRE

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends for 'moving truck rental' rises 40% WoW

## Entry / Exit
Entry: If weekly Google Trends for 'moving truck rental' rises 40% WoW Exit: After 4 weeks or if trend falls below 20% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Moving demand varies seasonally and with housing market conditions, producing frequent signals.

## Required Keys
- None
