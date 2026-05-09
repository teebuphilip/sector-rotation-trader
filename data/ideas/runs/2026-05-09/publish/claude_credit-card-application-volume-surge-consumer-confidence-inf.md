# Credit Card Application Volume Surge Consumer Confidence Inflection

**Idea ID:** `credit-card-application-volume-surge-consumer-confidence-inf`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sudden spikes in credit card applications signal consumer confidence inflection. Rising applications precede consumer spending rallies and credit card company profitability expansion. Credit card volume and approval rates directly impact bank and fintech lending profitability.

## Universe
- XLF

## Data Sources
- FRED series ID TERMCBCCALLNS (Credit Card Applications Approved) through fred_series adapter

## Signal Logic
If weekly credit card applications approved exceed 8-week moving average by 12%+ and trend higher for 2 weeks

## Entry / Exit
Entry: If weekly credit card applications approved exceed 8-week moving average by 12%+ and trend higher for 2 weeks Exit: After 15 trading days or if approvals fall back below 8-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ID TERMCBCCALLNS (Credit Card Applications Approved) through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Card application cycles reset with holiday shopping, back-to-school, and quarterly rate change announcements; fires 2–4 times per quarter.

## Required Keys
- None
