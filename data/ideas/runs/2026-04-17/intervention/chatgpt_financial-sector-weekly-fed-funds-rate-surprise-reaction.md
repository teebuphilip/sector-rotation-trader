# Financial Sector Weekly Fed Funds Rate Surprise Reaction

**Idea ID:** `financial-sector-weekly-fed-funds-rate-surprise-reaction`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
If the Fed funds rate surprises above expectations, financial stocks often rally sharply the following week. Higher rates improve bank net interest margins boosting financials.

## Universe
- XLF

## Data Sources
- FRED series weekly effective federal funds rate vs market consensus for XLF

## Signal Logic
If weekly effective Fed funds rate > consensus by 5bps

## Entry / Exit
Entry: If weekly effective Fed funds rate > consensus by 5bps Exit: After 2 weeks or 4% XLF gain

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series weekly effective federal funds rate vs market consensus for XLF via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Fed funds rate movements occur regularly with monetary policy updates.

## Required Keys
- None
