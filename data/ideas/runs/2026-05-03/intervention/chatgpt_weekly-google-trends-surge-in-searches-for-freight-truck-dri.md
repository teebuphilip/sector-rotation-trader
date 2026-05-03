# Weekly Google Trends Surge In Searches For Freight Truck Driver Job Openings Signals Labor Tightness

**Idea ID:** `weekly-google-trends-surge-in-searches-for-freight-truck-dri`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A surge in job opening searches for freight truck drivers signals rising labor demand tightness in logistics sector. Labor shortages pressure industrial sector margins due to rising wage costs.

## Universe
- XLI

## Data Sources
- Google Trends weekly freight truck driver job opening searches

## Signal Logic
Enter short XLI when weekly freight truck driver job searches rise 25% above 4-week average

## Entry / Exit
Entry: Enter short XLI when weekly freight truck driver job searches rise 25% above 4-week average Exit: Exit after 5 weeks or if searches fall below 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly freight truck driver job opening searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor market tightness frequently fluctuates with economic cycles and strikes.

## Required Keys
- None
