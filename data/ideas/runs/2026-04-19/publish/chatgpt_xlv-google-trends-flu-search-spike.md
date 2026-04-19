# Xlv Google Trends Flu Search Spike

**Idea ID:** `xlv-google-trends-flu-search-spike`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising flu-related searches often precede increased healthcare sector activity and defensive buying in XLV. Healthcare ETFs benefit from increased public health concerns.

## Universe
- XLV

## Data Sources
- Google Trends weekly data for 'flu symptoms' search term

## Signal Logic
Enter long if weekly flu symptom search interest increases by 20%+ compared to prior week

## Entry / Exit
Entry: Enter long if weekly flu symptom search interest increases by 20%+ compared to prior week Exit: Exit after 3 weeks or if search interest declines for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'flu symptoms' search term via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal flu cycles and search interest spikes occur annually and within shorter windows.

## Required Keys
- None
