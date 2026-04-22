# Weekly Surge In Google Trends Search Interest For Gasoline Shortage

**Idea ID:** `weekly-surge-in-google-trends-search-interest-for-gasoline-s`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spike in gasoline shortage searches signals consumer anxiety about fuel availability and costs. Energy sector volatility and consumer stress weigh on markets.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest for 'gasoline shortage'

## Signal Logic
If weekly search interest rises 30% above 4-week average

## Entry / Exit
Entry: If weekly search interest rises 30% above 4-week average Exit: After 3 weeks or interest drops below 15% gain threshold

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'gasoline shortage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Fuel supply concerns tend to spike unpredictably with weather or geopolitical events.

## Required Keys
- None
