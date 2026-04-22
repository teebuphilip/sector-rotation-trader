# Google Trends Spike In Diy Home Repair Searches

**Idea ID:** `google-trends-spike-in-diy-home-repair-searches`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased interest in DIY home repair indicates consumers delaying professional services, signaling local economic stress. Industrial sector containing home improvement and construction exposure may slow with reduced service demand.

## Universe
- XLI

## Data Sources
- Google Trends weekly data for 'DIY home repair' keyword

## Signal Logic
Enter short XLI when weekly DIY home repair searches increase by 25% over prior 4-week average

## Entry / Exit
Entry: Enter short XLI when weekly DIY home repair searches increase by 25% over prior 4-week average Exit: Exit after 4 weeks or when search growth falls below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'DIY home repair' keyword via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: DIY search interest frequently spikes seasonally and during economic slowdowns.

## Required Keys
- None
