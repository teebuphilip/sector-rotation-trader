# Daily Spike In Usgs Earthquake Activity Near Major Ports Signals Short-term Freight Logistics Disruption And Bearish Xli

**Idea ID:** `daily-spike-in-usgs-earthquake-activity-near-major-ports-sig`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased earthquake activity near ports tends to temporarily disrupt freight logistics and shipping schedules. Freight logistics stocks get pressured by potential shipment delays and infrastructure concerns.

## Universe
- XLI

## Data Sources
- USGS earthquake activity daily counts

## Signal Logic
Enter short XLI if daily earthquake count near top 5 US ports rises 50%+ above 30-day moving average

## Entry / Exit
Entry: Enter short XLI if daily earthquake count near top 5 US ports rises 50%+ above 30-day moving average Exit: Exit after 7 trading days or once daily counts normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake clusters near ports occur regularly and create predictable short-term freight disruptions.

## Required Keys
- None
