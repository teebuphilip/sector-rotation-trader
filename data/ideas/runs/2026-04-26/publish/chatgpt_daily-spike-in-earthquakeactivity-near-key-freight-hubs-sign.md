# Daily Spike In Earthquakeactivity Near Key Freight Hubs Signals Bearish Xli

**Idea ID:** `daily-spike-in-earthquakeactivity-near-key-freight-hubs-sign`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increase in earthquake frequency near freight hubs signals potential logistical disruptions. Freight interruptions from natural disasters hurt industrial supply chains and profits.

## Universe
- XLI

## Data Sources
- USGS earthquake activity daily data near major freight hubs

## Signal Logic
If daily earthquake count near major hubs exceeds 2 standard deviations above 30-day average

## Entry / Exit
Entry: If daily earthquake count near major hubs exceeds 2 standard deviations above 30-day average Exit: After 5 trading days or when activity returns to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily data near major freight hubs via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake activity near hubs is variable and can spike multiple times yearly.

## Required Keys
- None
