# Daily Spike In Google Trends Searches For Truck Driver Shortage Signals Bullish Xli

**Idea ID:** `daily-spike-in-google-trends-searches-for-truck-driver-short`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising concern about truck driver shortages suggests pricing power and increased freight rates for logistics firms. Logistics sector benefits from supply constraints driving higher revenue per shipment.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'truck driver shortage'

## Signal Logic
Enter long XLI when daily searches increase 20% vs 5-day moving average

## Entry / Exit
Entry: Enter long XLI when daily searches increase 20% vs 5-day moving average Exit: Exit after 7 trading days or if searches revert below 5-day moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'truck driver shortage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor shortage concerns ebb and flow frequently with news cycles and wage reports.

## Required Keys
- None
