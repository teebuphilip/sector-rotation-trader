# Electricity Demand Collapse During Mild Weather

**Idea ID:** `electricity-demand-collapse-during-mild-weather`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Sharp electricity demand collapse during unseasonably mild weather signals reduced utility revenue and weak industrial activity. Declining electricity demand reduces utility earnings and signals softer industrial production and economic activity.

## Universe
- XLU

## Data Sources
- EIA total U.S. electricity demand (daily via eia_electricity adapter) combined with Open-Meteo temperature data

## Signal Logic
If daily electricity demand drops >8% below 30-day moving average AND average temperature is >5°F above normal for region

## Entry / Exit
Entry: If daily electricity demand drops >8% below 30-day moving average AND average temperature is >5°F above normal for region Exit: After 8 trading days or when demand rebounds above 30-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA total U.S. electricity demand (daily via eia_electricity adapter) combined with Open-Meteo temperature data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather volatility is constant; mild spells during heating/cooling seasons produce regular demand dips.

## Required Keys
- None
