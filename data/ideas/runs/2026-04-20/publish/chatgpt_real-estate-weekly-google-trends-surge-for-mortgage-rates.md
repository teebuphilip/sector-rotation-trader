# Real Estate Weekly Google Trends Surge For Mortgage Rates

**Idea ID:** `real-estate-weekly-google-trends-surge-for-mortgage-rates`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 25%+ weekly spike in mortgage rate searches often signals increased market focus on housing costs, sometimes preceding real estate sector weakness due to rate concerns. Rising mortgage rate concerns weigh on real estate valuations.

## Universe
- XLRE

## Data Sources
- Google Trends weekly data for 'mortgage rates' US searches

## Signal Logic
Enter short XLRE if 'mortgage rates' search interest rises >25% week-over-week

## Entry / Exit
Entry: Enter short XLRE if 'mortgage rates' search interest rises >25% week-over-week Exit: Exit after 4 weeks or if XLRE rallies 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'mortgage rates' US searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Mortgage rate search interest spikes frequently in response to Fed announcements and rate moves.

## Required Keys
- None
