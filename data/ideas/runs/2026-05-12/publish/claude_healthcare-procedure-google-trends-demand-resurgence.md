# Healthcare Procedure Google Trends Demand Resurgence

**Idea ID:** `healthcare-procedure-google-trends-demand-resurgence`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in elective procedure searches signal consumer confidence and disposable income recovery; bullish for consumer discretionary and healthcare services. Elective healthcare spending is a proxy for consumer financial health and willingness to spend on non-essentials.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'cosmetic surgery near me', 'dental implant cost', 'laser eye surgery'

## Signal Logic
If weekly Google Trends for elective procedure searches rises >50% YoY and XLY closes up >0.5% that week

## Entry / Exit
Entry: If weekly Google Trends for elective procedure searches rises >50% YoY and XLY closes up >0.5% that week Exit: After 3 weeks or if search interest falls below baseline for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'cosmetic surgery near me', 'dental implant cost', 'laser eye surgery' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal consumer confidence waves (post-bonus, tax refunds, holiday spending) reliably drive elective procedure searches.

## Required Keys
- None
