# Daily Spike In Rss Counts For Warehouse Automation Failure Signals Bearish Industrials

**Idea ID:** `daily-spike-in-rss-counts-for-warehouse-automation-failure-s`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
News spikes about warehouse automation failures raise concerns about logistics efficiency risks, pressuring industrial sector stocks. Failures in warehouse automation can delay shipments and increase costs.

## Universe
- XLI

## Data Sources
- RSS news feed counts for warehouse automation failure

## Signal Logic
Enter short on XLI if daily RSS counts for 'warehouse automation failure' mentions triple compared to 10-day average

## Entry / Exit
Entry: Enter short on XLI if daily RSS counts for 'warehouse automation failure' mentions triple compared to 10-day average Exit: Exit after 5 trading days or when mentions revert below average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for warehouse automation failure via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Automation glitches and failures are regularly reported and cause news volume spikes.

## Required Keys
- None
