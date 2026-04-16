# Toiletpaperstockpilingsignalsshiftsinconsumersentiment

**Idea ID:** `toiletpaperstockpilingsignalsshiftsinconsumersentiment`
**Source:**  / 
**Frequency:** daily

## Thesis
Spikes in Google search interest for 'toilet paper' indicate heightened consumer fears and uncertainty, leading to hoarding behavior. Consumer staples companies that produce and distribute toilet paper tend to benefit from increased demand during periods of consumer anxiety.

## Universe
- XLP

## Data Sources
- Google Trends data for 'toilet paper'

## Signal Logic
If the daily Google Trends index for 'toilet paper' exceeds the 90-day moving average by 50%

## Entry / Exit
Entry: If the daily Google Trends index for 'toilet paper' exceeds the 90-day moving average by 50% Exit: When the index falls back below the 90-day moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends data for 'toilet paper' via api (daily).

## Required Keys
- None
