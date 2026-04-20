# Healthcare Sector Google Trends Spike In Flu Symptoms

**Idea ID:** `healthcare-sector-google-trends-spike-in-flu-symptoms`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A 20%+ weekly increase in flu symptom searches often precedes healthcare sector strength due to expected increased demand. Rising illness-related searches correlate with higher healthcare utilization.

## Universe
- XLV

## Data Sources
- Google Trends weekly data for 'flu symptoms' US searches

## Signal Logic
Enter long XLV if 'flu symptoms' search interest rises >20% week-over-week

## Entry / Exit
Entry: Enter long XLV if 'flu symptoms' search interest rises >20% week-over-week Exit: Exit after 4 weeks or if XLV drops 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'flu symptoms' US searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal flu outbreaks cause regular weekly spikes in symptom searches.

## Required Keys
- None
