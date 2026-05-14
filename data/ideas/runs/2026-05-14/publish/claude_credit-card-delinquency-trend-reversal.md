# Credit Card Delinquency Trend Reversal

**Idea ID:** `credit-card-delinquency-trend-reversal`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rising credit card delinquency rates signal consumer financial distress and reduced creditworthiness, foreshadowing discretionary spending collapse. Delinquency spikes indicate consumer balance sheet stress; retail and leisure spending deteriorates as households reduce discretionary outlays.

## Universe
- XLY

## Data Sources
- Federal Reserve weekly delinquency rate data (30+ days late) via FRED series TERMCBCCALLNS

## Signal Logic
If weekly delinquency rate rises >15 basis points above 12-week moving average

## Entry / Exit
Entry: If weekly delinquency rate rises >15 basis points above 12-week moving average Exit: After 20 trading days or when delinquency rate declines below entry level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Federal Reserve weekly delinquency rate data (30+ days late) via FRED series TERMCBCCALLNS via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Credit cycle peaks occur regularly; economic stress events and seasonal payment cycles create predictable delinquency spikes.

## Required Keys
- None
