# Steel Price Surge On China Manufacturing Pmi Surprise Triggers Industrials Rally

**Idea ID:** `steel-price-surge-on-china-manufacturing-pmi-surprise-trigge`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When China PMI beats expectations by >1 point AND steel prices surge >3%, global demand expectations improve. Industrials and materials rally on improved cycle outlook. Industrial companies depend on global construction and manufacturing demand; China PMI strength signals near-term capex and infrastructure spend.

## Universe
- XLI

## Data Sources
- FRED series CSCICP03CHM (China Manufacturing PMI) weekly + Yahoo Finance steel futures (USO proxy) daily

## Signal Logic
China PMI data beats consensus by >1 point; steel/materials ETF (DBB or SLV) rises >2% same week; XLI closes up >0.5%

## Entry / Exit
Entry: China PMI data beats consensus by >1 point; steel/materials ETF (DBB or SLV) rises >2% same week; XLI closes up >0.5% Exit: XLI closes down >0.6% from entry or 10 calendar days elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series CSCICP03CHM (China Manufacturing PMI) weekly + Yahoo Finance steel futures (USO proxy) daily via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: China PMI is released monthly; beats/misses occur ~40% of the time, making this a realistic signal 1–2 times per quarter.

## Required Keys
- None
