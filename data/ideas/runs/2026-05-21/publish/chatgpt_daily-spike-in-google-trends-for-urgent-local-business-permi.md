# Daily Spike In Google Trends For Urgent Local Business Permit Complaints Signals Local Economic Stress

**Idea ID:** `daily-spike-in-google-trends-for-urgent-local-business-permi`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in searches complaining about local business permits indicate regulatory or economic stress. Local business regulatory issues can slow commercial real estate activity and development.

## Universe
- XLRE

## Data Sources
- Google Trends daily local business permit complaint searches

## Signal Logic
Enter short when daily searches spike 35% above 14-day average

## Entry / Exit
Entry: Enter short when daily searches spike 35% above 14-day average Exit: Exit when searches return to within 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily local business permit complaint searches via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Local regulatory complaints spike frequently due to permit delays or policy changes.

## Required Keys
- None
