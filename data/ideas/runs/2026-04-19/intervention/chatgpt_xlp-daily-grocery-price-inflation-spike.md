# Xlp Daily Grocery Price Inflation Spike

**Idea ID:** `xlp-daily-grocery-price-inflation-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in grocery price inflation pressure consumer staples costs but may boost XLP as pricing power returns. Staples benefit from pricing power during inflation spikes.

## Universe
- XLP

## Data Sources
- FRED monthly CPI for food at home interpolated to daily estimates

## Signal Logic
Enter long if daily interpolated food CPI increases by more than 0.1% from prior day

## Entry / Exit
Entry: Enter long if daily interpolated food CPI increases by more than 0.1% from prior day Exit: Exit after 7 days or if CPI growth slows

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED monthly CPI for food at home interpolated to daily estimates via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food CPI data updates monthly but interpolation allows detection of rapid recent rises.

## Required Keys
- None
