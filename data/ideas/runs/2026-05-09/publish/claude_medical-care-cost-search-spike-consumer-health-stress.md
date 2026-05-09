# Medical Care Cost Search Spike Consumer Health Stress

**Idea ID:** `medical-care-cost-search-spike-consumer-health-stress`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in healthcare cost and debt-related searches indicate consumer financial stress from medical expenses. Precedes credit card delinquencies and reduced discretionary spending. Medical cost stress reduces disposable income and consumer confidence, depressing discretionary sector.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'medical debt', 'prescription drug cost', 'health insurance denied claim' through google_trends adapter

## Signal Logic
If combined healthcare cost search index rises above 60th percentile of 26-week rolling window

## Entry / Exit
Entry: If combined healthcare cost search index rises above 60th percentile of 26-week rolling window Exit: After 14 calendar days or if index falls below 40th percentile for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'medical debt', 'prescription drug cost', 'health insurance denied claim' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare cost searches spike during open enrollment, post-deductible resets (Jan), and high-inflation periods; fires 2–3 times per quarter.

## Required Keys
- None
