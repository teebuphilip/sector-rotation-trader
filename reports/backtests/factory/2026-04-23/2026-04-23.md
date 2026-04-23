# Professional Backtest V1

- Run date: 2026-04-23
- Window: 2024-01-01 to 2026-04-23
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- LIVE_ONLY_NON_PRICE: 3

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Attention Sentiment Spike Daily Surge In News Rss Counts Mentioning Cyberattack Triggers Bullish Xlc | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Weekly Surge In Google Trends Searches For Diy Home Repair Signals Consumer Stress Lifting Xly | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Openchargemap Ev Charger Installations Signals Bullish Xlc | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |

This is experimental research, not investment advice. Past performance does not predict future results.
