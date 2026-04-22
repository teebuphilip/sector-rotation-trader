# Local Economy Weirdness Surge In Small Business Tax Delinquency Notices

**Idea ID:** `local-economy-weirdness-surge-in-small-business-tax-delinque`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spike in small business tax delinquency notices signals localized economic stress impacting retail sector. Rising small business financial stress often precedes consumer discretionary sector weakness.

## Universe
- XLY

## Data Sources
- Public scrape of municipal tax delinquency notices

## Signal Logic
Enter short XLY if tax delinquency notices rise 20% WoW for 2 consecutive weeks

## Entry / Exit
Entry: Enter short XLY if tax delinquency notices rise 20% WoW for 2 consecutive weeks Exit: Exit after notices fall below 10% WoW increase or after 6 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public scrape of municipal tax delinquency notices via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Municipal delinquency notices spike seasonally and with economic stress, reliably appearing multiple times yearly.

## Required Keys
- None
