# Healthcare Cost Google Trends Acceleration Index

**Idea ID:** `healthcare-cost-google-trends-acceleration-index`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp spikes in healthcare cost-related searches signal consumer stress and inability to afford medical services, often preceding healthcare system margin compression and policy-driven sector rotation. Rising healthcare cost searches correlate with consumer financial distress, increasing defaults on medical debt and forcing payers to tighten reimbursement rates.

## Universe
- XLV

## Data Sources
- Google Trends weekly search volume for 'medical bill debt', 'prescription cost', 'health insurance claim denial'; calculate acceleration week-over-week

## Signal Logic
If combined search volume index rises >25% week-over-week and exceeds 60 on 0-100 scale

## Entry / Exit
Entry: If combined search volume index rises >25% week-over-week and exceeds 60 on 0-100 scale Exit: Exit after 9 trading days or if search index drops >15% over 2-week period

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'medical bill debt', 'prescription cost', 'health insurance claim denial'; calculate acceleration week-over-week via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare cost stress is cyclical; earnings seasons and policy announcements trigger spikes 4–6 times annually.

## Required Keys
- None
