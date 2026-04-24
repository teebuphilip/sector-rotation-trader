# Feature Virality Force Rank — 2026-04-23
Total features ranked: 12

## Scoring Key
- **Adjusted Score** = viral_total × (6 − build_complexity) × stockarithm_fit / 25
- **Verdict**: BUILD_NOW | BUILD_LATER | SKIP
- **Detail**: link to the dated score report for full dimension breakdown

---

| Rank | Feature | Adj Score | Viral/20 | Complexity | Fit | Verdict | Detail |
|:---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Receipts Guy's Trade History Scroll | 11.2 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-23.md#receipts-guy-s-trade-history-scroll) |
| 2 | Bucket Thesis Statement | 9.6 | 8 | 2 | 5 | BUILD_NOW | [scores](2026-04-23.md#bucket-thesis-statement) |
| 3 | Alt-Data Nerd's Divergence Spotlight | 9.6 | 8 | 2 | 4 | BUILD_NOW | [scores](2026-04-23.md#alt-data-nerd-s-divergence-spotlight) |
| 4 | Receipts Export | 9.0 | 9 | 2 | 5 | BUILD_NOW | [scores](2026-04-22.md#receipts-export) |
| 5 | Force Rank Divergence View | 8.96 | 7 | 2 | 4 | BUILD_NOW | [scores](2026-04-23.md#force-rank-divergence-view) |
| 6 | Divergence View | 8.75 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-22.md#divergence-view) |
| 7 | Bucket Audit Log | 8.4 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-22.md#bucket-audit-log) |
| 8 | Trade-Level Signal Audit Trail | 8.4 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-23.md#trade-level-signal-audit-trail) |
| 9 | Receipts Ledger: Loss Flags | 8.4 | 7 | 2 | 5 | BUILD_NOW | [scores](2026-04-23.md#receipts-ledger-loss-flags) |
| 10 | Signal Hunter's Bucket View | 7.2 | 6 | 2 | 4 | BUILD_LATER | [scores](2026-04-23.md#signal-hunter-s-bucket-view) |
| 11 | Cross-Algo Pattern Spotter | 6.4 | 8 | 2 | 5 | BUILD_LATER | [scores](2026-04-22.md#cross-algo-pattern-spotter) |
| 12 | Bucket Migration Log | 5.76 | 6 | 2 | 4 | BUILD_LATER | [scores](2026-04-23.md#bucket-migration-log) |

---

## BUILD_NOW List

### 1. Receipts Guy's Trade History Scroll (score=11.2)
- **Top mechanic:** Foregrounds losses publicly with red/green color coding, exploiting stockarithm's radical transparency angle to let power users prove their due diligence to skeptical communities.
- **Weakness:** Zero network effects or invitation mechanics—a Receipts Guy auditing trades alone doesn't create incentive or reason to share with others, making it purely consumptive.
- **Source:** `drafts/features/2026-04-23/openai-feature-04-receipts-guy-s-trade-history-scroll.md`

### 2. Bucket Thesis Statement (score=9.6)
- **Top mechanic:** Operator thesis becomes a public proof artifact—readers can screenshot/share the explicit failure logic and prediction criteria, which is rare and credible in fintech.
- **Weakness:** No incentive for users to *invite others* to see theses; it's consumption-only and doesn't leverage the two-sided market (winners/losers) as a shared discovery mechanism.
- **Source:** `drafts/features/2026-04-23/anthropic-feature-03-bucket-thesis-statement.md`

### 3. Alt-Data Nerd's Divergence Spotlight (score=9.6)
- **Top mechanic:** Lets expert traders spot anomalies others miss and share 'Biscotti found a weird pattern' moments that prove their edge.
- **Weakness:** No built-in sharing mechanism or leaderboard footprint—divergence discovery stays private unless user manually screenshots and posts.
- **Source:** `drafts/features/2026-04-23/openai-feature-03-alt-data-nerd-s-divergence-spotlight.md`

### 4. Receipts Export (score=9.0)
- **Top mechanic:** Data exports with explicit 'no survivorship bias' headers let skeptical traders prove to peers that stockarithm is genuinely transparent—the anti-hype flex in a hype category.
- **Weakness:** Zero network effects or invitation mechanics; a user exporting data doesn't pull anyone else into the product, so growth is entirely dependent on individual conversion.
- **Source:** `drafts/features/2026-04-22/anthropic-feature-04-receipts-export.md`

### 5. Force Rank Divergence View (score=8.96)
- **Top mechanic:** Lets skeptical traders spot and share algos that are visibly recovering from failure — pure narrative ammunition for the 'receipts guy' archetype who loves proving others wrong with data.
- **Weakness:** No incentive loop or sharing mechanic; a user finds a hot divergence but has zero reason to tell anyone else — it's pure consumption, not co-creation or social proof.
- **Source:** `drafts/features/2026-04-23/anthropic-feature-01-force-rank-divergence-view.md`

### 6. Divergence View (score=8.75)
- **Top mechanic:** Data-literate traders can spot and call out algos caught in lucky streaks, creating native credibility plays on r/algotrading by showing they read the fine print.
- **Weakness:** No incentive to share the finding—spotting a divergence is personal alpha, not social proof, so users hoard rather than broadcast.
- **Source:** `drafts/features/2026-04-22/anthropic-feature-01-divergence-view.md`

### 7. Bucket Audit Log (score=8.4)
- **Top mechanic:** Transparency of failure reasons (algo moved to noise: 40% win rate) lets users share audit logs as proof of rigorous methodology, exploiting the core unfair advantage of publishing failures.
- **Weakness:** No invitation mechanic or network effect—users audit algos alone; sharing a bucket transition log is interesting only to existing users, not a recruitment tool.
- **Source:** `drafts/features/2026-04-22/anthropic-feature-02-bucket-audit-log.md`

### 8. Trade-Level Signal Audit Trail (score=8.4)
- **Top mechanic:** Inspection-level transparency (signal conditions, SPY comparison) lets alt-data nerds prove signal legitimacy publicly in Reddit debates without screenshots—'Biscotti fired on [condition] while SPY did [this]' is shareable proof.
- **Weakness:** Read-only audit with no export or share button means users must manually transcribe findings to social; feature lives inside the product and doesn't naturally become a social artifact or conversation starter.
- **Source:** `drafts/features/2026-04-23/anthropic-feature-02-trade-level-signal-audit-trail.md`

### 9. Receipts Ledger: Loss Flags (score=8.4)
- **Top mechanic:** Loss flags directly amplify stockarithm's core unfair advantage (transparency) and give skeptical traders proof-of-honesty social currency when they cite it to peers.
- **Weakness:** Loss flags are table stakes for credibility, not shareable content—users don't screenshot loss data to flex or tell friends about, so invitation loop and public evidence are near zero.
- **Source:** `drafts/features/2026-04-23/openai-feature-01-receipts-ledger-loss-flags.md`

---

## BUILD_LATER List

- **Signal Hunter's Bucket View** (score=7.2) — Bucket classification directly leverages stockarithm's unique failures-published transparency—users can visibly filter ALPHA signals and share their curation, turning data triage into credible signal curation.
- **Cross-Algo Pattern Spotter** (score=6.4) — Users can publicly claim they spotted a signal-type pattern before others (e.g., 'I saw weather algos were noise 3 months ago'), turning data analysis into social proof.
- **Bucket Migration Log** (score=5.76) — Shows classification volatility as proof of rigor—users can cite 'Biscotti bounced 4x in 60 days' to warn peers, leveraging the failures-published credibility angle.

---

## SKIP List

_None._
