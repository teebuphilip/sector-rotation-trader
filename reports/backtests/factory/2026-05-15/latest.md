# Professional Backtest V1

- Run date: 2026-05-15
- Window: 2024-01-01 to 2026-05-15
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- LIVE_ONLY_NON_PRICE: 12

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Commodity Shortage News Volume Burst | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Consumer Stress Spike From Google Trends On Urgent Appliance Repair Searches | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Spike In Google Trends For Emergency Roadside Assistance Searches Signals Consumer Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Spike In Google Trends For Emergency Vehicle Battery Replacement Searches Signals Auto Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Spike In Google Trends For Flu Symptom Searches Boosting Healthcare Services Demand | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Surge In Google Trends For Urgent Dental Care Searches Lifting Healthcare Sector | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Ev Charger Buildout Acceleration Play | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Truck Driver Wage Search Surge | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weather Extreme Disruption Energy Demand Spike | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Weekly Rise In Google Trends For Warehouse Automation Interest Signals Industrial Demand | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends For Freight Congestion Complaints Correlating With Industrial Sector Risk | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends For Used Car Price Searches Signaling Consumer Cost Pressure | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |

This is experimental research, not investment advice. Past performance does not predict future results.
