# Freight Logistics Squeeze From Weekly Fred Producer Price Index For Transportation Rising Faster Than Industrial Ppi

**Idea ID:** `freight-logistics-squeeze-from-weekly-fred-producer-price-in`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising transport PPI relative to industrial PPI signals cost pressure on logistics that may squeeze manufacturing margins. Industrial sector profitability pressured by rising freight costs.

## Universe
- XLI

## Data Sources
- FRED API: PPI Transportation and PPI Industrial

## Signal Logic
Enter short XLI if Transportation PPI increases more than 1% week-over-week and exceeds Industrial PPI by 0.5%

## Entry / Exit
Entry: Enter short XLI if Transportation PPI increases more than 1% week-over-week and exceeds Industrial PPI by 0.5% Exit: Exit after 4 weeks or when spread narrows below 0.3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED API: PPI Transportation and PPI Industrial via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly PPI data often shows transportation cost spikes aligned with supply chain disruptions.

## Required Keys
- None
