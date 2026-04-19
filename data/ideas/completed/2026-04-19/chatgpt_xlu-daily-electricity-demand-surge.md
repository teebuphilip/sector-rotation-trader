# Xlu Daily Electricity Demand Surge

**Idea ID:** `xlu-daily-electricity-demand-surge`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Unexpected daily surges in electricity demand tend to lift utilities ETFs as prices and revenues rise. Utilities revenue and prices respond to electricity consumption spikes.

## Universe
- XLU

## Data Sources
- EIA daily electricity demand data

## Signal Logic
Enter long if daily electricity demand increases by more than 3% versus prior day

## Entry / Exit
Entry: Enter long if daily electricity demand increases by more than 3% versus prior day Exit: Exit after 3 trading days or if demand reverts

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA daily electricity demand data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Electricity demand fluctuates daily with weather and economic activity causing frequent spikes.

## Required Keys
- None
