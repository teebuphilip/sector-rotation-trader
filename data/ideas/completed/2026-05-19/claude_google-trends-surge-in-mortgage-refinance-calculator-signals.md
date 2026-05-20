# Google Trends Surge In Mortgage Refinance Calculator Signals Rate-sensitive Financial Stress

**Idea ID:** `google-trends-surge-in-mortgage-refinance-calculator-signals`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Household financial decision-making spikes when mortgage rates move sharply; refinance inquiry volume predicts consumer confidence and housing demand shifts 1-2 weeks ahead. Rising refinance inquiry volume signals rate shock and housing affordability stress, which historically precedes financial sector weakness.

## Universe
- XLF

## Data Sources
- Google Trends weekly search volume for 'mortgage refinance calculator' through google_trends adapter

## Signal Logic
When weekly search volume exceeds 80th percentile of 52-week rolling average

## Entry / Exit
Entry: When weekly search volume exceeds 80th percentile of 52-week rolling average Exit: When search volume falls below 60th percentile over 2 consecutive weeks or after 14 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'mortgage refinance calculator' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Rate volatility is endemic to markets; mortgage rate moves trigger search spikes reliably every 3-4 weeks on average.

## Required Keys
- None
