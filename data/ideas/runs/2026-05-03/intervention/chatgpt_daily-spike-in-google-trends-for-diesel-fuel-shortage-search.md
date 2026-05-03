# Daily Spike In Google Trends For Diesel Fuel Shortage Searches Signals Macro Input Pressure On Energy Sector

**Idea ID:** `daily-spike-in-google-trends-for-diesel-fuel-shortage-search`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sharp daily spike in diesel fuel shortage searches signals rising supply constraints and input cost pressures in energy and industrial sectors. Energy input supply shocks often pressure energy sector profitability.

## Universe
- XLE

## Data Sources
- Google Trends daily diesel fuel shortage search volume

## Signal Logic
Enter short XLE if daily diesel shortage searches spike 30% above 7-day average

## Entry / Exit
Entry: Enter short XLE if daily diesel shortage searches spike 30% above 7-day average Exit: Exit after 5 trading days or when searches fall below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily diesel fuel shortage search volume via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Fuel supply concerns flare regularly due to geopolitical or weather disruptions.

## Required Keys
- None
