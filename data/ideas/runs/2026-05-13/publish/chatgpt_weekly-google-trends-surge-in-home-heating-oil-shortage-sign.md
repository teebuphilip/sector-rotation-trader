# Weekly Google Trends Surge In Home Heating Oil Shortage Signals Winter Utility Stress Favoring Utilities Sector

**Idea ID:** `weekly-google-trends-surge-in-home-heating-oil-shortage-sign`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased searches for heating oil shortages signal demand spikes that stress utility supply chains and boost utility sector pricing power. Utilities benefit from higher energy demand and pricing during shortages.

## Universe
- XLU

## Data Sources
- Google Trends weekly queries

## Signal Logic
If weekly Google Trends volume for 'heating oil shortage' rises 25% week-over-week

## Entry / Exit
Entry: If weekly Google Trends volume for 'heating oil shortage' rises 25% week-over-week Exit: After 6 weeks or when volume declines 20% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly queries via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Heating fuel concerns spike seasonally in cold months.

## Required Keys
- None
