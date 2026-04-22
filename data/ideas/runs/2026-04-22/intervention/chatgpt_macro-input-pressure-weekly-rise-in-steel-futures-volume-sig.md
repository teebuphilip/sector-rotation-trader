# Macro Input Pressure Weekly Rise In Steel Futures Volume Signals Industrial Sector Momentum

**Idea ID:** `macro-input-pressure-weekly-rise-in-steel-futures-volume-sig`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing futures volume usually precedes price moves and signals growing industrial demand. Steel demand is a direct proxy for industrial activity strength.

## Universe
- XLI

## Data Sources
- Yahoo Finance weekly volume for steel futures

## Signal Logic
Enter long XLI if weekly steel futures volume increases >20% compared to prior 4-week average

## Entry / Exit
Entry: Enter long XLI if weekly steel futures volume increases >20% compared to prior 4-week average Exit: Exit after 4 weeks or if volume drops below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance weekly volume for steel futures via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Steel futures volume is volatile and spikes multiple times per year aligned with industrial cycles.

## Required Keys
- None
