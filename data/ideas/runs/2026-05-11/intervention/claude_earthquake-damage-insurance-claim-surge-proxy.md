# Earthquake Damage Insurance Claim Surge Proxy

**Idea ID:** `earthquake-damage-insurance-claim-surge-proxy`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When a region logs 3+ earthquakes >4.5 magnitude within 7 days, property/casualty insurance claims spike, and insurers reduce underwriting, creating economic friction that favors defensive financials. Insurance repricing and claims acceleration flow through premiums, reducing discretionary spending and boosting financials that benefit from rate normalization.

## Universe
- XLF

## Data Sources
- USGS earthquake activity daily magnitude >4.5 counts by region through earthquake_activity adapter

## Signal Logic
If 3+ earthquakes >4.5 magnitude occur within 7 days in same major fault zone

## Entry / Exit
Entry: If 3+ earthquakes >4.5 magnitude occur within 7 days in same major fault zone Exit: After 10 trading days or if no new quakes >4.5 occur for 5 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily magnitude >4.5 counts by region through earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic clusters occur naturally 6-8 times yearly in active US zones; California, Pacific Northwest quake swarms fire this signal 1-2x per quarter.

## Required Keys
- None
