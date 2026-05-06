# Daily Jump In Google Trends Searches For Home Renovation Permits

**Idea ID:** `daily-jump-in-google-trends-searches-for-home-renovation-per`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
An uptick in searches for home renovation permits signals increased local construction activity and consumer spending on housing. Building materials sector benefits from increased construction and remodeling.

## Universe
- XLB

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily searches for 'home renovation permit' increase by over 10% compared to 7-day average

## Entry / Exit
Entry: If daily searches for 'home renovation permit' increase by over 10% compared to 7-day average Exit: After 5 trading days or when growth falls below 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Construction and renovation interest fluctuates with seasonal buying and local policy changes.

## Required Keys
- None
