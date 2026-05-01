# Daily Spike In Fred Cpi Food At Home Index Signals Inflation Pressure In Consumer Staples Sector

**Idea ID:** `daily-spike-in-fred-cpi-food-at-home-index-signals-inflation`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden jump in food-at-home inflation pressures grocery and staple product margins. Rising input prices compress margins and reduce consumer disposable income for staples.

## Universe
- XLP

## Data Sources
- FRED API Consumer Price Index Food at Home daily interpolated

## Signal Logic
Enter short XLP when daily CPI Food at Home index rises 0.2% above 5-day moving average

## Entry / Exit
Entry: Enter short XLP when daily CPI Food at Home index rises 0.2% above 5-day moving average Exit: Exit after 7 trading days or when index reverts below 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED API Consumer Price Index Food at Home daily interpolated via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Food inflation experiences frequent daily changes due to supply shocks.

## Required Keys
- None
