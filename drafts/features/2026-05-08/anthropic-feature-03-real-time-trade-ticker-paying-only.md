# Real-Time Trade Ticker (Paying Only)
Status: Draft
Generated: 2026-05-08 | Provider: anthropic

## 1. The "Why" (Context)

- **Problem:** The Signal Hunter and Alt-Data Nerd have to refresh the page or dig into trade history to see if an algo fired today. They're checking back because they want to know if the signal is still alive and trading, not just sitting idle for the last 45 days.
- **Goal:** Show the last 5-10 trades (buys and sells) across all algos in a simple, persistent, no-fluff ticker at the bottom of the leaderboard. Paid users only. Updates every 15 seconds. No notifications, no popups.
- **Metric:** Paid user session length; return visit frequency; paid user retention week-over-week.

## 2. User Stories

- As a Signal Hunter, I want to glance at the bottom of the leaderboard and see which algos are actually trading today, so I know which ones are still running hot and which are stuck.
- As the Alt-Data Nerd, I want to see the live tick of trades from all signals so I can get a feel for the lab's activity level without leaving the page.

## 3. Functional Requirements (The "What")

- **Requirement 1:** A fixed footer bar (30–40px tall) appears below the leaderboard on paying user views; it shows the 5–10 most recent trades (buy or sell) from any algo, in order of execution time (newest first); each row shows: algo name, BUY/SELL, ticker, price, time (HH:MM ET).
- **Requirement 2:** The ticker auto-refreshes every 15 seconds; no polling indicator, no 'loading' state — just new rows slide in from the right if a new trade arrives.
- **Requirement 3:** Free users do not see the ticker.

## 4. Design & UX

- **Mockups:** TBD
- **Key Interaction:** Keep it minimal: one line per trade, monospace font, dark background. No color coding, no emoji, no sparkles. On mobile, the ticker is full-width below the leaderboard; entries wrap if needed. Clicking a trade scrolls the leaderboard to that algo's row. No animation except the slide-in of new trades. The operator's voice: 'Here's what's happening right now in the lab.'

## 5. Acceptance Criteria (AC)

- Ticker shows the last 10 trades; when a new trade executes, the oldest trade drops off the bottom.
- Ticker refreshes every 15 seconds; no manual refresh button.
- Each trade row is clickable and scrolls the leaderboard to the corresponding algo; clicking on 'BUY' or 'SELL' does nothing (non-interactive text).

## 6. Out of Scope

- Filters or search within the ticker.
- Notifications or alerts when a specific algo trades.
- Trade replay or historical ticker archive.
