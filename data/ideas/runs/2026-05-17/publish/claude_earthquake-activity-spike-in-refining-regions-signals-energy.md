# Earthquake Activity Spike In Refining Regions Signals Energy Supply Risk Premium

**Idea ID:** `earthquake-activity-spike-in-refining-regions-signals-energy`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When earthquake activity picks up in major refining regions (Gulf Coast, California), energy prices spike on supply-disruption fear. Crude and refined-product margins widen. Energy stocks benefit from higher crude prices and refinery margin expansion when supply disruption fears emerge.

## Universe
- XLE

## Data Sources
- USGS earthquake activity API for magnitude >4.0 events in US Gulf Coast / California refining zones

## Signal Logic
USGS logs 1+ magnitude >4.0 earthquake in Gulf Coast / California refining zone; crude oil (CL=F) closes up >2% same day; XLE closes up >1.5%

## Entry / Exit
Entry: USGS logs 1+ magnitude >4.0 earthquake in Gulf Coast / California refining zone; crude oil (CL=F) closes up >2% same day; XLE closes up >1.5% Exit: XLE closes down >0.8% from entry or 6 trading days elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity API for magnitude >4.0 events in US Gulf Coast / California refining zones via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Refining-zone earthquakes >4.0 occur 1–2 times per month on average; crude is highly sensitive to supply shock fears.

## Required Keys
- None
