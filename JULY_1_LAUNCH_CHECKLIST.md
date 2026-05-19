# July 1 Launch Readiness Checklist

**Purpose**

This is the working checklist for the July 1 traction review / paid-path decision.
It is not a feature backlog. It is the list of things that must be true, or at least clearly understood, before the July 1 decision point.

## 1) Launch Boundary

- [DONE] Confirm what is in scope for July 1.
- [DONE] Confirm what stays deferred until after July 1.
- [NEED] Do not add new features unless they unblock launch readiness.
- [DONE] Keep the public launch story stable and consistent across the site, profiles, and posts.

## 2) Public Surface

- [NEED] Homepage loads cleanly. Final browser smoke test still needed.
- [NEED] Algo pages load cleanly. Final browser smoke test still needed.
- [DONE] How-it-works page is current.
- [NEED] Plain-English spec appears first on algo pages. The explainer exists; page-order smoke test still needed.
- [NEED] No broken links, stale labels, or placeholder copy on public pages. Final link sweep still needed.
- [DONE] Hidden / private pages are not referenced from public navigation.

## 3) Ops Loop

- [NEED] Nightly status report writes successfully. Morning artifact freshness is still stale/uneven.
- [DONE] Drive sync continues to work.
- [NEED] Morning artifacts are current, not stale.
- [DONE] GitHub workflow runs are green.
- [DONE] Public ops notes / changelog path is defined, even if not yet visible.

## 4) Validation Integrity

- [DONE] Deep validation snapshot is current.
- [DONE] Full-window and rolling-30D views still agree with the intended interpretation.
- [NEED] No new leakage or survivorship issue has been introduced. This needs an ongoing review, not a one-time assumption.
- [DONE] Failures remain visible in the board and in the story.

## 5) Paid-Path Decision Inputs

- [NEED] Decide whether July 1 is a real paid launch or only a traction review.
- [NEED] If paid launch is real, confirm Stripe checkout and backend gating exist.
- [DONE] If paid launch is not ready, keep July 1 as a review point only.
- [NEED] Keep premium promises aligned with what is actually implemented.

## 6) Trust / Narrative

- [DONE] Public explanation is honest and readable.
- [DONE] The site still looks like evidence, not marketing wallpaper.
- [DONE] The product story matches the current system state.
- [DONE] The launch narrative does not overclaim signal quality.

## 7) Final Go / No-Go

- [NEED] Public site is stable.
- [NEED] Ops are boring.
- [DONE] Validation is current.
- [NEED] Paid-path choice is explicit.
- [NEED] July 1 decision can be made without guessing what the system is doing.
