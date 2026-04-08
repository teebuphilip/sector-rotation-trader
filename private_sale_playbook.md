# Private Sale Playbook — Single Algo

This is a private, internal checklist for packaging a single crazy algo for sale.

## 1) What the buyer gets
- Clean standalone repo for one algo only
- Runner script (daily or weekly)
- Config + env keys + README
- Backtest script (optional but recommended)
- Sample outputs (ledger, dashboard, signals)

## 2) What we do NOT promise
- No performance guarantees
- No advice, no personalized recommendations
- Clear “research only” language

## 3) Packaging steps
1. Extract algo into its own repo (one module, one runner).
2. Replace any shared helpers with local copies.
3. Remove unrelated algos, dashboards, and idea pipeline.
4. Add a minimal web page or CLI output showing the signal.
5. Add a clean README with setup, inputs, and known risks.
6. Add a license or custom usage terms.

## 4) Required artifacts
- `README.md`
- `requirements.txt`
- `algo.py`
- `runner.py`
- `backtest.py` (optional)
- `sample_output/` with a small CSV or JSON

## 5) Pricing logic
- $15K one‑time license = implementation + provenance + research time saved
- Price includes 30–180 days of live receipts (if available)
- Offer optional add‑on: quarterly refresh of the algo (paid)

## 6) Disclosure language (example)
“This is an experimental research system. It generates signals from public data. It is not investment advice. Past performance does not predict future results.”

## 7) Handoff checklist
- Confirm buyer can run locally with provided keys
- Provide a 30‑minute walkthrough call
- Make clear there is no ongoing support unless contracted
