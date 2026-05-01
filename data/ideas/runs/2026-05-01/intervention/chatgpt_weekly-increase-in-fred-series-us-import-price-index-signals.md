# Weekly Increase In Fred Series Us Import Price Index Signals Inflation Pressure On Materials Sector

**Idea ID:** `weekly-increase-in-fred-series-us-import-price-index-signals`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising import prices reflect increasing input cost pressures that weigh on materials producers. Cost inflation compresses margins for basic materials companies.

## Universe
- XLB

## Data Sources
- FRED API Import Price Index monthly data

## Signal Logic
Enter short XLB when weekly import price index rises 1.5% above its 8-week moving average

## Entry / Exit
Entry: Enter short XLB when weekly import price index rises 1.5% above its 8-week moving average Exit: Exit after 6 weeks or when index falls below 8-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED API Import Price Index monthly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Import price fluctuations are common and regularly prompt sector repricing.

## Required Keys
- None
