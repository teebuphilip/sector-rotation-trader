# Healthcare Cost Google Search Acceleration Breakout

**Idea ID:** `healthcare-cost-google-search-acceleration-breakout`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When combined healthcare cost concern searches accelerate 15%+ week-over-week, consumer stress sentiment shifts sharply, impacting healthcare sector demand within 7-14 days. Rising cost concern searches predict lower healthcare utilization and pricing pressure on providers and insurers.

## Universe
- XLV

## Data Sources
- Google Trends weekly searches for 'medical bill payment plan' + 'pharmacy cost' + 'health insurance deductible' through google_trends adapter

## Signal Logic
If healthcare cost search index accelerates 15%+ WoW for 2 consecutive weeks, short XLV on Friday close

## Entry / Exit
Entry: If healthcare cost search index accelerates 15%+ WoW for 2 consecutive weeks, short XLV on Friday close Exit: Exit after 10 trading days or if search acceleration drops below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'medical bill payment plan' + 'pharmacy cost' + 'health insurance deductible' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Healthcare cost concern searches spike seasonally (January enrollment, medication renewals) and during inflation spikes; 15%+ acceleration occurs 3-4 times per year.

## Required Keys
- None
