# Daily Jump In Freight Railcar Loadings Signals Bullish Xli

**Idea ID:** `daily-jump-in-freight-railcar-loadings-signals-bullish-xli`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden increase in railcar loadings implies rising industrial demand and shipment activity, signaling strength in industrials. Increased freight railcar usage precedes industrial production and capital goods demand.

## Universe
- XLI

## Data Sources
- FRED weekly railcar loadings data

## Signal Logic
Enter long if daily railcar loadings increase by more than 5% from prior day

## Entry / Exit
Entry: Enter long if daily railcar loadings increase by more than 5% from prior day Exit: Exit after 7 trading days or if loadings decline 3 days in a row

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly railcar loadings data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Railcar loadings fluctuate frequently with industrial activity shifts.

## Required Keys
- None
