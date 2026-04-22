# Weekly Spike In Google Trends For Gig Economy Job Searches

**Idea ID:** `weekly-spike-in-google-trends-for-gig-economy-job-searches`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased interest in gig economy jobs suggests labor market softness and shifting employment preferences. Consumer discretionary spending may weaken due to labor income uncertainty.

## Universe
- XLY

## Data Sources
- Google Trends weekly data for 'gig economy job' keyword

## Signal Logic
Enter short XLY when weekly gig economy job search interest rises >30% WoW

## Entry / Exit
Entry: Enter short XLY when weekly gig economy job search interest rises >30% WoW Exit: Exit after 4 weeks or when interest falls below 15% WoW

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'gig economy job' keyword via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Gig job search interest fluctuates with economic cycles and labor market uncertainty.

## Required Keys
- None
