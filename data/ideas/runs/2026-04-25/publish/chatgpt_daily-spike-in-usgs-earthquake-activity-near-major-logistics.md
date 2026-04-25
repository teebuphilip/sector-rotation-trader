# Daily Spike In Usgs Earthquake Activity Near Major Logistics Hubs Signals Bearish Xli

**Idea ID:** `daily-spike-in-usgs-earthquake-activity-near-major-logistics`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased seismic activity disrupts supply chains and port operations causing short-term freight delays. Logistics companies face operational risk and revenue disruption from natural disaster events.

## Universe
- XLI

## Data Sources
- USGS earthquake daily activity near key logistics hubs

## Signal Logic
Enter short XLI if daily earthquake count near hubs exceeds 3 standard deviations above 30-day average

## Entry / Exit
Entry: Enter short XLI if daily earthquake count near hubs exceeds 3 standard deviations above 30-day average Exit: Exit after 10 trading days or when activity normalizes below 1 deviation

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake daily activity near key logistics hubs via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake activity clusters and aftershocks create frequent volatility spikes in logistics.

## Required Keys
- None
