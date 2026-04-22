# Daily Increase In Politicalinsiderfiling Purchases In Healthcare Stocks Signals Sector Rotation

**Idea ID:** `daily-increase-in-politicalinsiderfiling-purchases-in-health`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Insiders buying healthcare stocks may signal upcoming positive sector-specific developments or rotation. Insider buying often precedes positive performance in healthcare.

## Universe
- XLV

## Data Sources
- Political insider filings for healthcare sector

## Signal Logic
Entry when daily insider buying volume in healthcare ETFs exceeds 150% of 20-day average

## Entry / Exit
Entry: Entry when daily insider buying volume in healthcare ETFs exceeds 150% of 20-day average Exit: Exit after 10 trading days or when buying volume normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider filings for healthcare sector via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Insider filings regularly show bursts of buying activity.

## Required Keys
- None
