# Travel Mobility Weekly Increase In Google Trends For Road Trip Searches Signals Leisure Travel Pickup

**Idea ID:** `travel-mobility-weekly-increase-in-google-trends-for-road-tr`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in road trips signals increased travel demand benefiting discretionary travel-related sectors. Consumer leisure spending typically rises with travel interest.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'road trip'

## Signal Logic
Enter long XLY if 'road trip' search interest rises at least 15% above 5-week average

## Entry / Exit
Entry: Enter long XLY if 'road trip' search interest rises at least 15% above 5-week average Exit: Exit after 3 weeks or if interest falls below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'road trip' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Travel interest spikes seasonally and with weather patterns, often multiple times per year.

## Required Keys
- None
