# Coffee Shop WiFi Usage

**Idea ID:** `coffee-shop-wifi-usage`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
By monitoring the number of devices connected to public WiFi networks in popular coffee shop chains, we can infer trends in foot traffic and consumer activity, which can be used to inform investment decisions.

## Universe
- SBUX
- DNKN
- PEET
- DPGCX

## Data Sources
- Foursquare API for location data
- Public WiFi usage data from coffee shop chains

## Signal Logic
Track the number of devices connected to public WiFi networks in a sample of popular coffee shop locations. Look for sudden spikes or sustained increases in WiFi usage as an indicator of increased foot traffic and consumer activity.

## Entry / Exit
Buy when WiFi usage increases significantly above the recent average. Sell when usage returns to normal levels.

## Position Sizing
Allocate a small percentage of the portfolio (e.g., 5-10%) to this signal, and scale position size based on the magnitude of the WiFi usage change.

## Risks
Factors other than foot traffic (e.g., seasonal trends, device usage patterns) may impact WiFi usage. The signal may be noisy and require careful interpretation.

## Implementation Notes
Obtain public WiFi usage data from coffee shop chains, potentially through partnerships or web scraping. Develop a model to filter out background noise and identify meaningful changes in usage. Integrate this data with Foursquare location data to map usage to specific stores.

## Required Keys
- Foursquare API key
