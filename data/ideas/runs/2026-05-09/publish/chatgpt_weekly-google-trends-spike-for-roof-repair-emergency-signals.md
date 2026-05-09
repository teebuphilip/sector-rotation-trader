# Weekly Google Trends Spike For Roof Repair Emergency Signals Construction And Industrials Demand

**Idea ID:** `weekly-google-trends-spike-for-roof-repair-emergency-signals`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A spike in emergency roof repair searches reflects weather damage or housing stress, boosting demand for construction-related industries. Industrials sector benefits from increased repair and construction activity.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long if weekly 'roof repair emergency' searches increase by 35% or more

## Entry / Exit
Entry: Enter long if weekly 'roof repair emergency' searches increase by 35% or more Exit: Exit after 5 weeks or if interest falls below 20% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weather-related roof damage occurs seasonally and unpredictably.

## Required Keys
- None
