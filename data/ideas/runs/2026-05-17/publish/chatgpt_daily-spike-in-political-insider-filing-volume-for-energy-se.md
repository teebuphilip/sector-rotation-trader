# Daily Spike In Political Insider Filing Volume For Energy Sector Executives Signals Imminent Volatility

**Idea ID:** `daily-spike-in-political-insider-filing-volume-for-energy-se`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased insider sales or purchases in energy firms often precede sector volatility or news. Energy insiders buying large blocks signal confidence and potential positive catalysts.

## Universe
- XLE

## Data Sources
- Political insider trading filings for energy sector executives

## Signal Logic
Enter long XLE if daily insider filings volume for energy executives doubles relative to 30-day average with net buying

## Entry / Exit
Entry: Enter long XLE if daily insider filings volume for energy executives doubles relative to 30-day average with net buying Exit: Exit after 10 trading days or if insider filings normalize

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider trading filings for energy sector executives via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider filings cluster around earnings and regulatory events causing frequent volume bursts.

## Required Keys
- None
