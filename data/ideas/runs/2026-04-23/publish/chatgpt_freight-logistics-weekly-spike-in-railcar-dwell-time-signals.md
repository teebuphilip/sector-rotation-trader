# Freight Logistics Weekly Spike In Railcar Dwell Time Signals Bearish Xli

**Idea ID:** `freight-logistics-weekly-spike-in-railcar-dwell-time-signals`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased railcar dwell time suggests supply chain slowdowns, pressuring industrial production and transportation. Supply chain bottlenecks typically signal industrial sector headwinds.

## Universe
- XLI

## Data Sources
- Railcar dwell time weekly averages from public rail data

## Signal Logic
Enter short XLI when railcar dwell time rises above 90th percentile of last 12 weeks

## Entry / Exit
Entry: Enter short XLI when railcar dwell time rises above 90th percentile of last 12 weeks Exit: Exit after 4 weeks or when dwell time falls below 75th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Railcar dwell time weekly averages from public rail data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Railcar dwell time fluctuates regularly with seasonal and macro disruptions.

## Required Keys
- None
