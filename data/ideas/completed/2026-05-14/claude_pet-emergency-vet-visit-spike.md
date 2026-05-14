# Pet Emergency Vet Visit Spike

**Idea ID:** `pet-emergency-vet-visit-spike`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in emergency veterinary care searches indicate pet health crises (food contamination, seasonal illness), driving urgent consumer spending and signaling underlying economic stress. Veterinary and animal health services see demand surge; signals consumer financial resilience for premium health spending.

## Universe
- XLV

## Data Sources
- Google Trends weekly search volume for 'emergency vet near me' and 'pet urgent care'

## Signal Logic
If weekly Google Trends volume for 'emergency vet' rises >50% above 8-week moving average

## Entry / Exit
Entry: If weekly Google Trends volume for 'emergency vet' rises >50% above 8-week moving average Exit: After 10 calendar days or when volume returns to baseline + 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'emergency vet near me' and 'pet urgent care' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Pet health emergencies occur sporadically but reliably; seasonal patterns (hot weather, dietary shifts) ensure multiple triggers per quarter.

## Required Keys
- None
