# Daily Surge In Earthquake Activity Near Major Warehouses Signals Short-term Bearish Xli

**Idea ID:** `daily-surge-in-earthquake-activity-near-major-warehouses-sig`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increase in seismic activity near warehouse hubs may disrupt supply chains and logistics operations. Disruptions to freight logistics from natural events can pressure industrial stocks.

## Universe
- XLI

## Data Sources
- USGS daily earthquake data near key logistics hubs

## Signal Logic
Enter short if daily earthquake count near hubs exceeds 3 times 30-day average

## Entry / Exit
Entry: Enter short if daily earthquake count near hubs exceeds 3 times 30-day average Exit: Exit after 7 trading days or when earthquake activity subsides

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS daily earthquake data near key logistics hubs via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake clusters occur intermittently near logistics hubs.

## Required Keys
- None
