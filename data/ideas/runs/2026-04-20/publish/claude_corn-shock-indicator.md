# Corn Shock Indicator

**Idea ID:** `corn-shock-indicator`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Corn prices can spike rapidly due to drought, floods, or other supply shocks, signaling inflationary pressure and economic stress. Corn is a key agricultural commodity that feeds into consumer staples and food prices.

## Universe
- XLP

## Data Sources
- FRED weekly corn price index through fred_series adapter

## Signal Logic
If the weekly corn price index jumps more than 5% in a single week

## Entry / Exit
Entry: If the weekly corn price index jumps more than 5% in a single week Exit: After 3 weeks or once the index retreats by 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly corn price index through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Extreme weather events and geopolitical tensions can lead to sudden spikes in corn prices, even within a 30-day timeframe.

## Required Keys
- None
