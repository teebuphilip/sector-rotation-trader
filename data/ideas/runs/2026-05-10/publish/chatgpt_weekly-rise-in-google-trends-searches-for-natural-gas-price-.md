# Weekly Rise In Google Trends Searches For Natural Gas Price Spike Signals Energy Sector Input Cost Pressure

**Idea ID:** `weekly-rise-in-google-trends-searches-for-natural-gas-price-`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing concern about natural gas price spikes reflects rising fuel costs pressure on energy producers. Higher natural gas prices can increase costs and squeeze margins for energy sector companies.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest for 'natural gas price spike' via google_trends adapter

## Signal Logic
If weekly search interest rises more than 10% week-over-week

## Entry / Exit
Entry: If weekly search interest rises more than 10% week-over-week Exit: When weekly increase drops below 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'natural gas price spike' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Energy cost concerns regularly fluctuate with geopolitical and weather factors.

## Required Keys
- None
