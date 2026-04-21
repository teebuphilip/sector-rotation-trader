# Quality Check — 2026-04-21

## SPY Benchmark
- Could not fetch SPY data

## Baseline (NRWise)
- Equity: $100,055.50 (+0.06%)
- Sector: XLU
- Last Snapshot: 2026-04-20
- Snapshots: 80
- Trades: 10
- Positions: 0

## Normal Algos
  Algo                        Equity       YTD     Alpha  Trades      Signal    Last Run
  --------------------------------------------------------------------------------------
  baileymol              $106,117.24     6.12%     0.00%      30        HOLD  2026-04-20
  faber                  $103,846.61     3.85%     0.00%       8        HOLD  2026-04-20
  dmsr                   $103,710.55     3.71%     0.00%      15        HOLD  2026-04-20
  simple_monthly         $100,000.00     0.00%     0.00%       0        HOLD  2026-04-20
  biscotti                $99,783.24    -0.22%     0.00%       5        HOLD  2026-04-20

## Crazy Algos — Active (24/92)
  Algo                        Equity       YTD     Alpha  Trades      Signal    Last Run
  --------------------------------------------------------------------------------------
  lumber-momentum        $100,409.58     0.41%     0.00%       2        HOLD  2026-04-20
  copper-momentum        $100,362.35     0.36%     0.00%       2        HOLD  2026-04-20
  electricity-consumption   $100,228.91     0.23%     0.00%      10        HOLD  2026-04-20
  earthquake-aftershock-amplifier   $100,047.52     0.05%     0.00%       2        HOLD  2026-04-20
  semiconductor-moonshot-warning   $100,045.62     0.05%     0.00%       6        HOLD  2026-04-20
  materials-sector-weekly-positive-correlation-breakdown-with-   $100,025.87     0.03%     0.00%       2        HOLD  2026-04-20
  staples-sector-drawdown-rapid-recovery   $100,024.70     0.02%     0.00%       2        HOLD  2026-04-20
  google-gusts            $99,990.05    -0.01%     0.00%       1        HOLD  2026-04-20
  xlb-weekly-rss-news-count-spike-on-commodity-shortage    $99,990.05    -0.01%     0.00%       1        HOLD  2026-04-20
  industrial-sector-weekly-earthquake-activity-correlation-dip    $99,979.84    -0.02%     0.00%       2        HOLD  2026-04-20
  consumer-discretionary-google-trends-surge-for-sale-keywords    $99,960.96    -0.04%     0.00%       6        HOLD  2026-04-20
  real-estate-sector-weekly-google-trends-home-buying-surge    $99,954.77    -0.05%     0.00%       2        HOLD  2026-04-20
  utilities-sector-negative-price-gap-fill    $99,921.53    -0.08%     0.00%      14        HOLD  2026-04-20
  healthcare-sector-google-trends-spike-in-flu-symptoms    $99,917.38    -0.08%     0.00%       6        HOLD  2026-04-20
  retail-roulette         $99,913.43    -0.09%     0.00%      12        HOLD  2026-04-20
  xlu-daily-electricity-demand-surge    $99,898.68    -0.10%     0.00%      12        HOLD  2026-04-20
  tremor-tension          $99,864.21    -0.14%     0.00%       8        HOLD  2026-04-20
  electricity-enlightenment    $99,857.33    -0.14%     0.00%      10        HOLD  2026-04-20
  uber-mobility           $99,848.33    -0.15%     0.00%       2        HOLD  2026-04-20
  mortgage-rate-housing-proxy    $99,679.68    -0.32%     0.00%       2        HOLD  2026-04-20
  xle-weekly-drawdown-rebound-signal    $99,667.30    -0.33%     0.00%      32        HOLD  2026-04-20
  xlc-weekly-google-trends-surge-in-5g-rollout    $99,592.39    -0.41%     0.00%      46        HOLD  2026-04-20
  biscotti                $96,510.18    -3.49%     0.00%       5        HOLD  2026-04-20
  baileymol               $94,178.37    -5.82%     0.00%      62        HOLD  2026-04-20

## Crazy Algos — Idle (68/92)
  These algos are running but have no recorded trades in the current state history.
  That is not a crash; it means the trigger has not fired yet, the adapter returned no usable signal, or the strategy is still waiting for live evidence.

  airline-load-factor                  airport-security-surge               airport-shopping-spree               bankruptcy-filing-rate             
  calls311                             cardboard                            cloud-storage-demand-surge           congress                           
  consumer-sentiment                   craigslist                           credit-card-delinquency              crypto-capitulation-countdown      
  crypto-derivative-arbitrage          earthquake-energy-demand             electric-vehicle-charge-station-density  energy-sector-weekly-drawdown-exhaustion
  ev-charging-boom                     ev-charging-station-stampede         ev-euphoria                          financial-sector-momentum-divergence-with-spy
  fintech-disruption-wave              freight-rail-carloads                glassdoor                            global-tech-earnings-momentum      
  high-yield-spread-regime             housing-permit-velocity              insider-trading-signals              job-posting-acceleration           
  linkedin                             liquor                               lumber-futures-rollercoaster         misery-rotation                    
  online-ad-impression-volatility      pet-food-supply-chain                port-congestion-squeeze              port-container-volume              
  reddit-emoji-sentiment-spike         reddit-gaming-thread-spike           reddit-mentions-volatility-spike     reddit-sentiment-spike-trend       
  reddit-sentiment-spike               reddit-sentiment-volatility-spike    reddit-subreddit-mention-spike       reddit-subreddit-sentiment-spike   
  reddit-subreddit-surge-momentum      reddit-volatility-spike              retail-rush-ahead-of-holidays        retail-sales-momentum              
  rss-roar                             small-business-formation             social-media-sentiment-spike         solar-storm-scorcher               
  superbowl-futures-trade              technology-sector-daily-ev-charger-count-surge  truck-tonnage                        tsa                                
  twitter-sentiment-spike              utilities-sector-weekly-temperature-drop-signal  utility-power-grid-stress            volatility-spike-follow-through    
  weather-disruption-ripple-effects    weather-volatility-spike             weather-windfall                     work-from-home-frenzy              
  xlb-daily-volatility-contraction-breakout  xlu-weekly-cold-snap-weather-correlation  xlv-google-trends-flu-search-spike   yield-curve-regime                 

## Blocked Algos
- **EIA_API_KEY** (1 algos): Electricity Consumption
- **GLASSDOOR_KEY** (1 algos): Glassdoor Misery Gradient
- **GLASSDOOR_PARTNER_ID** (1 algos): Glassdoor Misery Gradient

## Flags & Warnings

- WARN: Could not fetch SPY benchmark data
- POSITIONS WITH HOLD: baileymol has 2 positions but signal is HOLD
- POSITIONS WITH HOLD: biscotti has 1 positions but signal is HOLD
- POSITIONS WITH HOLD: dmsr has 3 positions but signal is HOLD
- POSITIONS WITH HOLD: baileymol has 2 positions but signal is HOLD
- POSITIONS WITH HOLD: biscotti has 1 positions but signal is HOLD
- POSITIONS WITH HOLD: copper-momentum has 2 positions but signal is HOLD
- POSITIONS WITH HOLD: electricity-consumption has 2 positions but signal is HOLD
- POSITIONS WITH HOLD: google-gusts has 1 positions but signal is HOLD
- POSITIONS WITH HOLD: lumber-momentum has 2 positions but signal is HOLD
- POSITIONS WITH HOLD: mortgage-rate-housing-proxy has 2 positions but signal is HOLD
- POSITIONS WITH HOLD: uber-mobility has 2 positions but signal is HOLD
- POSITIONS WITH HOLD: xlb-weekly-rss-news-count-spike-on-commodity-shortage has 1 positions but signal is HOLD
- CHURNING: baileymol has 62 trades but is down -5.82% — overtrading?

---
_Generated by `scripts/quality_check.py` at 2026-04-21 09:28 UTC_