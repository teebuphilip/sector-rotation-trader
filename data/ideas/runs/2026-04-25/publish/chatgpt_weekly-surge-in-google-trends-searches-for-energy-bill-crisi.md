# Weekly Surge In Google Trends Searches For Energy Bill Crisis Signals Bearish Xle

**Idea ID:** `weekly-surge-in-google-trends-searches-for-energy-bill-crisi`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising consumer concern over energy bills signals demand destruction risk and regulatory pressure on energy firms. Energy companies may face margin compression and demand slowdown from consumer stress.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest for 'energy bill crisis'

## Signal Logic
Enter short XLE if weekly searches rise 25% week-over-week

## Entry / Exit
Entry: Enter short XLE if weekly searches rise 25% week-over-week Exit: Exit after 3 weeks or if weekly searches decline 15%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'energy bill crisis' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy cost concerns intensify seasonally and during geopolitical events.

## Required Keys
- None
