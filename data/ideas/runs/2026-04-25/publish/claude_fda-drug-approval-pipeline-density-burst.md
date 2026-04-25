# Fda Drug Approval Pipeline Density Burst

**Idea ID:** `fda-drug-approval-pipeline-density-burst`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of FDA approvals signal acceleration in pharma innovation cycles and often precede healthcare equity rallies and biotech rotation rotations. Drug approvals reduce pipeline risk for pharma companies and drive revenue growth expectations and sector sentiment rotation.

## Universe
- XLV

## Data Sources
- RSS feed aggregation from FDA press releases and biotech news wires, daily count of approval announcements

## Signal Logic
If 5-day rolling count of FDA approval announcements exceeds 4 and is 50% above 60-day average

## Entry / Exit
Entry: If 5-day rolling count of FDA approval announcements exceeds 4 and is 50% above 60-day average Exit: After 12 trading days or if approval count falls to baseline for 3 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed aggregation from FDA press releases and biotech news wires, daily count of approval announcements via scrape (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: FDA maintains a regular approval calendar; approval clusters naturally occur throughout the year with predictable cycles.

## Required Keys
- None
