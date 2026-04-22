# Freight Logistics Daily Rise In Railcar Load Counts With Xli Outperformance

**Idea ID:** `freight-logistics-daily-rise-in-railcar-load-counts-with-xli`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increasing railcar loads typically indicate rising industrial activity and supply chain momentum. Industrial sector benefits from increased freight movement signaling demand growth.

## Universe
- XLI

## Data Sources
- Freight Rail daily carloads and Yahoo Finance daily XLI prices

## Signal Logic
Enter long XLI when daily railcar loads increase >5% day-over-day and XLI outperforms SPY

## Entry / Exit
Entry: Enter long XLI when daily railcar loads increase >5% day-over-day and XLI outperforms SPY Exit: Exit after 5 trading days or if railcar loads decline 3% day-over-day

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Freight Rail daily carloads and Yahoo Finance daily XLI prices via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Railcar load data is daily and sensitive to industrial demand shifts.

## Required Keys
- None
