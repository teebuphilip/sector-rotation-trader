# Xlf Intraday Volatility Spike Followed By Weekly Fade

**Idea ID:** `xlf-intraday-volatility-spike-followed-by-weekly-fade`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sharp intraday volatility spike on a single day often leads to a fade or mean reversion over the following week. Financial sector tends to mean revert after volatility shocks.

## Universe
- XLF

## Data Sources
- Yahoo Finance daily and weekly volatility for XLF

## Signal Logic
Enter short if daily intraday volatility (high-low/close) exceeds 3% and weekly close is below prior week

## Entry / Exit
Entry: Enter short if daily intraday volatility (high-low/close) exceeds 3% and weekly close is below prior week Exit: Exit after 1 week or if weekly close rises above prior week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily and weekly volatility for XLF via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Volatility spikes and weekly fades happen regularly in financial ETFs.

## Required Keys
- None
