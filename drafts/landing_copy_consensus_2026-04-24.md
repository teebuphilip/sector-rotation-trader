# Landing Copy Consensus — 2026-04-24

This is the agreed direction for the next public landing/leaderboard copy pass.

Purpose:

- improve first-visit comprehension
- improve mailing-list conversion before May 15 / June 15
- keep scope tight
- avoid adding product complexity before pricing/checkout are real

## Core Agreement

The highest-value copy change is not a new feature.
It is a tighter public explanation of what Stockarithm is and why the visitor should care.

The agreed implementation should focus on:

1. sharper hero copy
2. better weekly-notes CTA language
3. one plain-English explainer block
4. a proof strip that uses live numbers, not hardcoded stale counts

## What To Drop For Now

Do not add the free-vs-paid bridge yet.

Reason:

- it raises questions the site cannot answer yet
- before June 15 / July 1 it creates friction instead of anticipation
- bring it back only when pricing and checkout are real

## What To Change

### 1. Hero

Keep the public, honest tone.

Preferred direction:

- headline: `Weird market signals, run in public.`
- subhead should explain that this is a public paper-trading lab for strange sector-rotation signals, with winners and failures both visible

### 2. CTA Language

Prefer:

- `Get the weekly lab notes`

Over:

- `Join the mailing list`

Supporting line should keep the tone:

- `No hype. Just the state of the lab.`

### 3. Explainer Block

This is the most important consensus addition.

The explainer should make the leaderboard feel human, not anonymous.

Agreed copy:

> Each row is one live paper-traded signal. Some are working. Some are failing. One of them is named after my dog. That is the point.

Reason:

- explains what the user is seeing
- signals honesty immediately
- adds personality without sounding polished or fake

### 4. Proof Strip

The proof strip should not hardcode the algo count.

Reason:

- stale numbers kill credibility faster than missing numbers

Requirement:

- pull the algo count dynamically from the public JSON during the code pass

The rest of the proof-strip direction remains sound:

- public
- updated
- honest
- not hype

## Agreed Page Order

1. hero
2. proof strip
3. explainer block
4. leaderboard intro / CTA
5. weekly lab notes CTA
6. disclaimer/footer

## Explicit Non-Goals

Do not do these in this pass:

- no free-vs-paid bridge
- no pricing language
- no thesis feature panel
- no extra product complexity
- no multi-section feature dump

## Implementation Timing

Recommended sequence:

1. Tuesday, April 28, 2026:
   apply the agreed copy/code pass
2. Wednesday, April 29, 2026:
   review the updated public surface with Grok
3. only then move on to the next launch-facing task
