# Weekly Google Trends Spike For Summer Travel Cancellations Signals Travel Sector Weakness

**Idea ID:** `weekly-google-trends-spike-for-summer-travel-cancellations-s`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising cancellations interest signals consumer hesitation or disruptions affecting travel demand. Consumer discretionary travel and leisure sub-sectors suffer from cancellations.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLY if weekly searches for 'summer travel cancellations' rise 30% week-over-week

## Entry / Exit
Entry: Enter short XLY if weekly searches for 'summer travel cancellations' rise 30% week-over-week Exit: Exit after 4 weeks or if search interest drops below 10% weekly increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Travel cancellation concerns increase seasonally and with event risk news.

## Required Keys
- None
