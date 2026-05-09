# Fed Liquidity Drain Rate Shock Dollar Strength Rally

**Idea ID:** `fed-liquidity-drain-rate-shock-dollar-strength-rally`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Sharp increases in Fed reverse repo usage or Treasury bill drains signal sudden liquidity tightening. Dollar strengthens, emerging markets weaken, commodity prices compress. Dollar strength and liquidity drains compress commodity and emerging market revenues; energy exporters underperform.

## Universe
- XLE

## Data Sources
- FRED series ID WIMFSL (Factors Affecting Reserve Balances – Liquidity Drain) through fred_series adapter

## Signal Logic
If Fed liquidity drain (weekly average) increases 10%+ versus prior week and closes at 10-week high

## Entry / Exit
Entry: If Fed liquidity drain (weekly average) increases 10%+ versus prior week and closes at 10-week high Exit: After 8 trading days or if drain rate falls 5% below the spike peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ID WIMFSL (Factors Affecting Reserve Balances – Liquidity Drain) through fred_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Liquidity drains occur with quarter-end, tax date, and seasonal treasury issuance cycles; 10% spikes fire 2–3 times per quarter.

## Required Keys
- None
