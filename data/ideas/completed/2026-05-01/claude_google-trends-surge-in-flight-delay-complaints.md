# Google Trends Surge In Flight Delay Complaints

**Idea ID:** `google-trends-surge-in-flight-delay-complaints`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp spikes in Google search volume for flight delay complaints signal operational stress in airlines and airports, often preceding earnings pressure or guidance cuts. Consumer discretionary travel sentiment deteriorates; airlines and leisure stocks face margin and demand headwinds.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'flight delays' + 'airline cancellation' through google_trends adapter

## Signal Logic
If weekly Google Trends index for 'flight delays' exceeds 70 (out of 100) and rises 15+ points from prior week

## Entry / Exit
Entry: If weekly Google Trends index for 'flight delays' exceeds 70 (out of 100) and rises 15+ points from prior week Exit: After 10 trading days or when index falls below 55

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'flight delays' + 'airline cancellation' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal airline disruptions, weather events, and staffing crises drive this signal weekly in peak travel seasons; fires at least monthly year-round.

## Required Keys
- None
