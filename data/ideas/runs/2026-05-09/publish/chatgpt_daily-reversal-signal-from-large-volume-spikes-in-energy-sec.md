# Daily Reversal Signal From Large Volume Spikes In Energy Sector Etf Xlv After Macro Input Pressure Spike

**Idea ID:** `daily-reversal-signal-from-large-volume-spikes-in-energy-sec`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden volume surges combined with a macro input pressure spike (e.g., oil price jump) often trigger short-term reversals as traders quickly adjust positions. Energy sector stocks react sharply to input price shocks, causing volatility and reversals.

## Universe
- XLE

## Data Sources
- Yahoo Finance daily prices and volume for XLE

## Signal Logic
Enter short if XLE daily volume spikes 50% above 20-day average alongside a greater than 5% rise in crude oil futures price

## Entry / Exit
Entry: Enter short if XLE daily volume spikes 50% above 20-day average alongside a greater than 5% rise in crude oil futures price Exit: Exit after 3 trading days or upon 2% price bounce

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices and volume for XLE via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily volatility and volume surges in energy are common with frequent oil price shocks.

## Required Keys
- None
