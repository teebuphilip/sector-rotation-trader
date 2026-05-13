# Weekly Spike In Google Trends For Fuel Shortage Predicts Energy Sector Volatility

**Idea ID:** `weekly-spike-in-google-trends-for-fuel-shortage-predicts-ene`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in fuel shortage searches signals mounting supply stress that often leads to energy price spikes and sector volatility. Energy producers benefit from supply constraints pushing prices higher.

## Universe
- XLE

## Data Sources
- Google Trends weekly data

## Signal Logic
If weekly search volume for 'fuel shortage' rises over 20% week-over-week

## Entry / Exit
Entry: If weekly search volume for 'fuel shortage' rises over 20% week-over-week Exit: After 4 weeks or when searches fall 15% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Fuel supply concerns spike frequently due to geopolitical and weather events.

## Required Keys
- None
