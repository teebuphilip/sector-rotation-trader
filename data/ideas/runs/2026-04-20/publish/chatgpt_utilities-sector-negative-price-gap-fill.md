# Utilities Sector Negative Price Gap Fill

**Idea ID:** `utilities-sector-negative-price-gap-fill`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A gap down of more than 1.5% that fills (closes back above previous day's close) within 3 days often leads to short-term rallies. Gap fills signal short-term demand overcoming initial sell pressure in utilities.

## Universe
- XLU

## Data Sources
- Yahoo Finance daily prices for XLU

## Signal Logic
Enter long XLU when a gap down >1.5% on day 1 is filled by close within 3 days

## Entry / Exit
Entry: Enter long XLU when a gap down >1.5% on day 1 is filled by close within 3 days Exit: Exit after 5 trading days or if XLU drops 2% from entry

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLU via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Gap down and fill patterns happen frequently in utilities due to sector defensiveness.

## Required Keys
- None
