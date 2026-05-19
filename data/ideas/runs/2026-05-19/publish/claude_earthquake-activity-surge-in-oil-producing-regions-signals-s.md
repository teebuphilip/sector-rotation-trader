# Earthquake Activity Surge In Oil-producing Regions Signals Supply Disruption Risk Premium

**Idea ID:** `earthquake-activity-surge-in-oil-producing-regions-signals-s`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When seismic activity (M>3.5) near shale basins increases >200% vs. 30-day average, energy markets price in production disruption risk; crude rallies 2-3%. Earthquake risk near drilling operations creates supply uncertainty and commodity risk premium expansion.

## Universe
- XLE

## Data Sources
- USGS earthquake magnitude and location data for Texas, Oklahoma, New Mexico through earthquake_activity adapter

## Signal Logic
When daily earthquake count in oil-producing regions exceeds 200% of 30-day rolling average

## Entry / Exit
Entry: When daily earthquake count in oil-producing regions exceeds 200% of 30-day rolling average Exit: After 5 trading days or when earthquake count normalizes below 130% of average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake magnitude and location data for Texas, Oklahoma, New Mexico through earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic clusters in shale regions occur sporadically but reliably several times per year; each triggers 2-5 day crude rallies.

## Required Keys
- None
