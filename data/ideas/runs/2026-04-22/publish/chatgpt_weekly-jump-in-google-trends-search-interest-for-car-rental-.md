# Weekly Jump In Google Trends Search Interest For Car Rental Deals Indicating Travel Surge

**Idea ID:** `weekly-jump-in-google-trends-search-interest-for-car-rental-`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in car rentals signals increased travel activity and mobility demand. Travel-related consumer discretionary firms benefit from rising mobility.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'car rental deals'

## Signal Logic
If weekly search interest rises 25% week-over-week

## Entry / Exit
Entry: If weekly search interest rises 25% week-over-week Exit: After 3 weeks or search interest falls below 10% gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'car rental deals' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Travel interest regularly surges seasonally and during holiday periods.

## Required Keys
- None
