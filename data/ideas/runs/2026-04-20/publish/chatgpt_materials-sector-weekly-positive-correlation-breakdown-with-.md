# Materials Sector Weekly Positive Correlation Breakdown With Xlb

**Idea ID:** `materials-sector-weekly-positive-correlation-breakdown-with-`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
When XLB weekly returns decouple negatively from SPY returns for 2 consecutive weeks, a rebound in XLB often follows. Short-term negative divergence from broad market is often overdone in materials.

## Universe
- XLB

## Data Sources
- Yahoo Finance weekly returns for XLB and SPY

## Signal Logic
Enter long XLB if weekly returns are negative while SPY returns are positive for 2 weeks in a row

## Entry / Exit
Entry: Enter long XLB if weekly returns are negative while SPY returns are positive for 2 weeks in a row Exit: Exit after 4 weeks or if XLB gains 6%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance weekly returns for XLB and SPY via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Materials sector often exhibits short-term divergences from SPY.

## Required Keys
- None
