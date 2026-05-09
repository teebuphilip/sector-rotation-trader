# Daily Google Trends Spike For Home Heating System Failure Predicts Utility Sector Demand Surge

**Idea ID:** `daily-google-trends-spike-for-home-heating-system-failure-pr`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden rise in heating system failure searches occurs during cold snaps, increasing utility usage and defensive demand. Utility sector benefits from increased energy consumption during heating failures.

## Universe
- XLU

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long if daily home heating failure searches increase 30% above 7-day average

## Entry / Exit
Entry: Enter long if daily home heating failure searches increase 30% above 7-day average Exit: Exit after 7 days or if interest falls below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Cold weather and heating issues regularly cause consumer search spikes.

## Required Keys
- None
