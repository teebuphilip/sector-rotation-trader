# Utility Sector Outflow On Mild Weather Pivot

**Idea ID:** `utility-sector-outflow-on-mild-weather-pivot`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When rolling 7-day average HDD drops sharply from seasonal baseline, heating demand collapses, reducing utility stock appeal and triggering rotation out of XLU into risk assets. Lower heating demand directly reduces utility revenue and crushes relative valuation of defensive utility stocks.

## Universe
- XLU

## Data Sources
- Open-Meteo daily heating degree days (HDD) and cooling degree days (CDD) for US population-weighted centers

## Signal Logic
If 7-day rolling HDD falls below historical seasonal average by >15% and XLU closes down 1%+ that day

## Entry / Exit
Entry: If 7-day rolling HDD falls below historical seasonal average by >15% and XLU closes down 1%+ that day Exit: After 10 trading days or when HDD returns to seasonal norm

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily heating degree days (HDD) and cooling degree days (CDD) for US population-weighted centers via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weather patterns shift weekly; mild snaps occur multiple times per winter/spring season, reliably triggering HDD collapses.

## Required Keys
- None
