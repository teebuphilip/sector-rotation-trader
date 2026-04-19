# Tracking Construction Dumpster Activity To Predict Housing Starts

**Idea ID:** `tracking-construction-dumpster-activity-to-predict-housing-s`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Analyzing the volume and frequency of construction dumpster requests can provide an early signal for upcoming housing starts. Housing starts are a leading indicator for the homebuilding and related sectors.

## Universe
- XHB

## Data Sources
- GarbageDay API (garbage collection service provider)

## Signal Logic
If dumpster requests in a metro area increase 10% month-over-month

## Entry / Exit
Entry: If dumpster requests in a metro area increase 10% month-over-month Exit: After 30 trading days or if the dumpster requests stop rising

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use GarbageDay API (garbage collection service provider) via api (daily).

## High Action Metadata
- Expected Fire Rate: 
- Historical Backfill: 
- Minimum History Months: 
- Adapter Status: 
- Trigger Sensitivity: 
- Why It Should Fire Soon: 

## Required Keys
- None
