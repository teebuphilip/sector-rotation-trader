# Earthquake Activity Reinsurance Volatility Spike

**Idea ID:** `earthquake-activity-reinsurance-volatility-spike`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Clustering of moderate-to-strong earthquakes in populated zones triggers rapid repricing of catastrophe reinsurance and property-linked derivatives, creating short-term financial sector rotation. Insurance and reinsurance stocks face claim reserve repricing; financial sector sentiment shifts on tail-risk realization.

## Universe
- XLF

## Data Sources
- USGS earthquake API magnitude 4.5+ events by week through earthquake_activity adapter

## Signal Logic
If 3+ magnitude 4.5+ earthquakes occur within a 7-day rolling window in the continental US or California, short XLF

## Entry / Exit
Entry: If 3+ magnitude 4.5+ earthquakes occur within a 7-day rolling window in the continental US or California, short XLF Exit: After 7 trading days or when weekly earthquake count drops to 0

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake API magnitude 4.5+ events by week through earthquake_activity adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: California and Western US experience earthquake clusters regularly; 3+ events in a week occurs 2–4 times per year.

## Required Keys
- None
