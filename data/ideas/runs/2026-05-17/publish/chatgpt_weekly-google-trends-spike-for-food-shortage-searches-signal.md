# Weekly Google Trends Spike For Food Shortage Searches Signals Consumer Staples Pressure

**Idea ID:** `weekly-google-trends-spike-for-food-shortage-searches-signal`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A spike in food shortage searches signals consumer anxiety about availability and inflation in staples. Consumer staples sector often underperforms amid concerns about supply shortages.

## Universe
- XLP

## Data Sources
- Google Trends weekly search interest for 'food shortage'

## Signal Logic
Enter short XLP if weekly Google Trends for 'food shortage' rises 35%+ WoW

## Entry / Exit
Entry: Enter short XLP if weekly Google Trends for 'food shortage' rises 35%+ WoW Exit: Exit after 4 weeks or if trend falls below 15% WoW increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'food shortage' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food supply concerns tend to spike with weather and geopolitical events.

## Required Keys
- None
