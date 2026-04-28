# Weekly Spike In Google Trends For Construction Permit Delay Signals Local Economy Stress

**Idea ID:** `weekly-spike-in-google-trends-for-construction-permit-delay-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search interest in construction permit delays reflects local bureaucratic or labor bottlenecks affecting real estate and construction sectors. Real estate sector suffers from delays increasing project costs and reducing completions.

## Universe
- XLRE

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLRE if weekly searches for 'construction permit delay' rise 20% week-over-week

## Entry / Exit
Entry: Enter short XLRE if weekly searches for 'construction permit delay' rise 20% week-over-week Exit: Exit after 4 weeks or if search interest drops 15% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Permit delays and bureaucratic issues typically see bursts tied to local political cycles.

## Required Keys
- None
