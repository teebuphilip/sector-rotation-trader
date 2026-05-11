# Weekly Increase In Fred Data For Consumer Credit Delinquency Rate Signals Rising Financial Stress

**Idea ID:** `weekly-increase-in-fred-data-for-consumer-credit-delinquency`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising consumer credit delinquency rates signal financial distress affecting consumer spending. Consumer discretionary sector is vulnerable to consumer credit stress.

## Universe
- XLY

## Data Sources
- FRED series consumer credit delinquency rate

## Signal Logic
Enter short XLY when weekly consumer credit delinquency rate rises 0.1%+ week-over-week

## Entry / Exit
Entry: Enter short XLY when weekly consumer credit delinquency rate rises 0.1%+ week-over-week Exit: Exit after 6 weeks or when delinquency growth slows below 0.05%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series consumer credit delinquency rate via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Consumer credit metrics update regularly with steady volatility.

## Required Keys
- None
