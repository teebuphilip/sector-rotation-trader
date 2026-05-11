# Weekly Jump In Google Trends For Home Heating Oil Shortage Signals Winter Energy Stress

**Idea ID:** `weekly-jump-in-google-trends-for-home-heating-oil-shortage-s`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Searches for home heating oil shortages rise during winter supply issues, indicating utility cost pressure. Utilities often benefit from higher energy prices during supply constraints.

## Universe
- XLU

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long XLU when weekly Google Trends for 'home heating oil shortage' rises 25%+ week-over-week

## Entry / Exit
Entry: Enter long XLU when weekly Google Trends for 'home heating oil shortage' rises 25%+ week-over-week Exit: Exit after cold season ends or when trend falls below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Winter energy supply fears and search interest spike seasonally every year.

## Required Keys
- None
