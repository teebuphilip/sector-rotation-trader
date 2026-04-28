# Daily Jump In Freight Rail Carload Volumes Signals Industrial Rebound

**Idea ID:** `daily-jump-in-freight-rail-carload-volumes-signals-industria`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden daily increases in rail carloads indicate inventory restocking and industrial activity acceleration. Industrial sector benefits from increased freight throughput signaling production growth.

## Universe
- XLI

## Data Sources
- Freight rail carload volume daily reports

## Signal Logic
Enter long XLI if daily rail carloads increase by more than 3% versus prior day

## Entry / Exit
Entry: Enter long XLI if daily rail carloads increase by more than 3% versus prior day Exit: Exit after 7 trading days or if daily volume drops by 2% for 2 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Freight rail carload volume daily reports via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily freight volumes regularly fluctuate with economic cycles and supply chain shifts.

## Required Keys
- None
