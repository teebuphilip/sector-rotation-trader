# Daily Spike In Google Trends Searches For Truck Tire Replacement Signals Freight Logistics Stress

**Idea ID:** `daily-spike-in-google-trends-searches-for-truck-tire-replace`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased truck tire replacement searches indicate heightened wear and tear in freight trucking, signaling logistics stress. Logistics sector may face cost and capacity pressure when truck maintenance spikes sharply.

## Universe
- XLI

## Data Sources
- Google Trends daily searches

## Signal Logic
If daily searches for 'truck tire replacement' rise 25% day-over-day

## Entry / Exit
Entry: If daily searches for 'truck tire replacement' rise 25% day-over-day Exit: After 7 days or when searches fall below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily searches via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 13
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight trucking maintenance needs spike frequently due to seasonal and operational factors.

## Required Keys
- None
