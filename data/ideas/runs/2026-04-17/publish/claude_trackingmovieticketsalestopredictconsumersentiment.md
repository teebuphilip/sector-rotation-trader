# Trackingmovieticketsalestopredictconsumersentiment

**Idea ID:** `trackingmovieticketsalestopredictconsumersentiment`
**Source:**  / 
**Frequency:** weekly

## Thesis
Consumers spend more on discretionary entertainment when they are confident about the economy. Consumer discretionary stocks are sensitive to changes in consumer spending and sentiment.

## Universe
- XLY

## Data Sources
- Box Office Mojo

## Signal Logic
If 4-week total box office revenue increases >10% vs 3 months ago

## Entry / Exit
Entry: If 4-week total box office revenue increases >10% vs 3 months ago Exit: After 3 weeks or if the 4-week average stops increasing

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Box Office Mojo via scrape (weekly).

## Required Keys
- None
