# Health Insurance Deductible Shock Searches

**Idea ID:** `health-insurance-deductible-shock-searches`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in insurance deductible and medical billing searches, especially in January and post-open enrollment, signal consumer health cost stress and reduced discretionary spending. Rising health cost anxiety compresses consumer discretionary budgets and spending confidence.

## Universe
- XLY

## Data Sources
- Google Trends weekly searches for 'high deductible health plan' and 'medical bill payment plans'

## Signal Logic
When combined search volume for deductible/payment plan searches exceeds 8-week average by 35%

## Entry / Exit
Entry: When combined search volume for deductible/payment plan searches exceeds 8-week average by 35% Exit: After 10 trading days or when searches fall below 1.5x baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'high deductible health plan' and 'medical bill payment plans' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Health cost searches spike predictably post-enrollment and at fiscal year boundaries; 2-3 spikes per year minimum.

## Required Keys
- None
