# Plain-English Algo Spec

## Purpose

This document defines the post-launch plain-English explanation layer for algo pages.

The goal is simple:
- every built algo page should explain, in normal language, what the signal is trying to do before the user sees the structured thesis inventory.

This is not the same thing as the raw thesis markdown.
This is a derived, reader-facing explanation layer.

## Why This Exists

Right now many algo pages require the reader to infer too much from:
- title
- one-line summary
- thesis block
- stats
- trades

That is too much work for a first-time visitor.

The plain-English spec should solve that by answering:
- what this signal is
- what it is trying to detect
- why that might matter
- how it behaves in plain terms
- why it could fail

## Gating Rule

Do not generate this spec at ideation time.

Generate it only after the algo exists as a built artifact.

That means:
- idea exists
- algo was actually built
- algo has entered the system as a real page/stateful artifact
- sandbox/live-only/backtested status may vary

The gate is:
- built algo exists

The gate is not:
- validated
- promoted
- profitable
- fully backtested

If the algo exists in the system, it can have a plain-English spec.
Its status still needs to be represented honestly.

## Display Order On Algo Pages

The plain-English spec should appear before the structured thesis/spec inventory.

Recommended page order:
1. title
2. one-line public summary
3. plain-English spec
4. structured signal brief
5. stats
6. chart
7. trade log

This is important.
The simple explanation comes first.
The structured detail supports it afterward.

## Inputs

The spec should be derived from existing source material, not invented from scratch.

Primary inputs:
- ideation markdown / publish markdown
- structured algo copy registry fields
- algo status metadata

Expected source fields:
- thesis
- universe
- data_sources
- signal_logic
- entry_exit
- position_sizing
- risks
- status / evidence class / family when helpful

## Output Shape

The plain-English spec should be short, structured, and readable.

Recommended sections:

### What This Signal Is Trying To Detect
- one short paragraph
- plain language
- no jargon unless necessary

### Why It Might Matter
- one short paragraph
- connect the signal to price/sector behavior
- do not overclaim

### How It Works
- 3 to 5 bullets max
- explain:
  - what data it watches
  - what condition makes it fire
  - what it buys / rotates into
  - how / when it exits

### Why It Could Fail
- 2 to 4 bullets max
- practical failure modes only

## Tone Rules

The spec must:
- stay plain-English
- stay faithful to source fields
- avoid fake certainty
- avoid AI fluff
- avoid invented rationale not supported by source material

The spec must not:
- sound like marketing copy
- sound like an academic abstract
- restate every raw field mechanically
- hide uncertainty

## Status Handling

The explanation must respect the algo's real state.

Examples:
- if sandbox only:
  - do not imply proven edge
- if live-only:
  - explain the idea, not fake confidence
- if promoted:
  - still explain the mechanism plainly, not boast

Possible status line near the spec:
- `Status: sandbox`
- `Status: live-only`
- `Status: promoted`

But the explanatory prose itself should stay neutral.

## Generation Rules

The spec should be generated after build, not before.

Recommended lifecycle:
1. algo build succeeds or algo page exists
2. structured fields are available
3. plain-English spec is generated
4. page render includes spec before the structured brief

If source fields are too thin:
- do not hallucinate
- either:
  - generate a short constrained spec from what exists
  - or omit the richer section and fall back cleanly

## Initial Constraints

For the first implementation:
- do not redesign the whole algo page
- do not build a large CMS
- do not version every sentence
- do not create a separate workflow unless needed

Just:
- derive the plain-English block
- place it before the structured thesis block
- keep it consistent

## Example Questions The Spec Must Answer

If a user lands on the page, they should be able to answer:
- What is this signal looking for?
- Why would that affect a sector ETF?
- What data is it using?
- What makes it actually take a trade?
- Why might this fail?

If the spec does not answer those questions quickly, it failed.

## Near-Term Priority

This is a post-May-15 clarity improvement.

It should happen soon after launch because it improves:
- comprehension
- trust
- public readability

But it should not preempt launch-critical plumbing or stability work.
