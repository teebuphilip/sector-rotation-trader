# Weekly Jump In Google Trends For Hotel Cancellation Surge Signals Bearish Xly

**Idea ID:** `weekly-jump-in-google-trends-for-hotel-cancellation-surge-si`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased searches for hotel cancellations often precede travel demand softness weighing on consumer discretionary travel stocks. Travel and leisure discretionary spending drops when cancellations surge.

## Universe
- XLY

## Data Sources
- Google Trends weekly searches

## Signal Logic
Enter short XLY when weekly search interest for 'hotel cancellation' surges 25%+ above 4-week average

## Entry / Exit
Entry: Enter short XLY when weekly search interest for 'hotel cancellation' surges 25%+ above 4-week average Exit: Exit after 3 weeks or if interest normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Travel cancellations regularly spike with weather or economic uncertainty.

## Required Keys
- None
