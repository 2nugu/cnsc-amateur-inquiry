# Framework v2 — Methodology

**Date**: 2026-05-13
**Source**: lessons from the CNSC inquiry (`../docs/derivations/`).

The CNSC framework was developed *forward* — from intuition to predictions, with derivation deferred.  The 7-weakness inquiry showed that this approach allowed *ansätze* to be promoted to *predictions* without anyone noticing the gap.  Framework v2 *will not repeat this*.

## M1 — Axiomatic forward direction

**Rule**: every quantitative claim must be classified into one of three tiers *before* it appears in any document:

- **T1 (Verifiable axiom)**: established physics with literature citation.
- **T2 (Explicit assumption)**: stated as assumption, with *the data program that confirms or refutes it* attached.
- **T3 (Derived consequence)**: follows from {T1, T2} by an explicit derivation, with the derivation written out *in this directory*.

No claim is *promoted* from T2 to T3 without the derivation being written.  No T3 claim appears in any output without the T1+T2 + derivation chain being explicit.

## M2 — Negative existential ban

**Rule**: statements of the form *"there is no mechanism for X"* are *forbidden*.

These are negative existentials and cannot be numerically verified — they would require enumerating all possible mechanisms.  Replace with positive constructive statements:

- Forbidden: *"CNSC has no de Sitter phase, so r = 0."*
- Required: *"Under assumption T2.x (no de Sitter), the formula T3.y yields r = ..."*

## M3 — Derive before claim

**Rule**: a numerical prediction cannot appear in any abstract, conclusion, summary, or headline before the derivation chain is closed.

This avoids the CNSC trap: the user (and the AI) repeatedly wrote *"we predict $n_s = 0.9637$"* before the derivation chain was checked.  When checked, the chain broke at step 5 (horizon-crossing inheritance, Derivation 03).  Reversing the order — derivation first, claim second — prevents this.

## M4 — Periodic *external audit*

**Rule**: at every major milestone (e.g., after stating axioms, after first quantitative derivation, before drafting any paper), perform a *hostile peer review* on the current document set.  Specifically:

1. List every numerical claim.
2. For each, identify the derivation step that establishes it.
3. For each derivation step, identify the *weakest* link.
4. Attempt to *break* that link.

The CNSC inquiry's `01-08` derivation docs are the model: each weakness is explicitly tested, results reported as found (success/partial/negative), and the cascade is tracked.

## M5 — Mainstream alignment check

**Rule**: every assumption (T2) and every derivation (T3) must be checked against the mainstream physics literature for analogue or precedent.

Specifically:
- *"Is there a similar setup in standard cosmology / quantum gravity / EFT?"*
- *"Does the answer agree with established results in that setup?"*
- *"If not, what is the specific point of departure, and is it justified?"*

The CNSC inquiry's failure on weakness 1 — that $\gamma(k)$ as an envelope has no DBI literature precedent — would have been caught earlier with this check.

## M6 — Coherence with surviving foundations

**Rule**: every new construction in framework v2 must be checked for coherence with the 4 foundations F1–F4 of `00_foundations.md`.

If a new construction conflicts with a surviving foundation, *either* the construction is wrong *or* the foundation needs revision — *both* options must be explicitly considered before proceeding.

## M7 — Stop conditions accepted in advance

**Rule**: the user (and the AI) accept *in advance* that the framework can collapse at any step.  Specifically, the stop conditions of `02_open_questions.md` (OQ-1 failure or OQ-2 failure) are *real* — they terminate the framework, not trigger ad-hoc rescue attempts.

This is the user's stance (`../memory/feedback_truth_over_theory.md`).  It is encoded as methodology to prevent it from eroding under the pressure of "we've invested so much already".

## M8 — Single source of truth

**Rule**: each numerical value, each formula, each definition has *one* document where it is defined.  Other documents may *reference* it but must not *redefine* it.

The CNSC paper had four different values for $r$ across five documents.  This was caught only by audit, late in the inquiry.  Framework v2 prevents this by enforcing single source of truth from the start.

---

## Application to OQ-1 through OQ-5

Each open question of `02_open_questions.md` will be addressed by:

1. Stating the precise mathematical content of the question (one document per OQ).
2. Selecting candidate formalisms with *literature citations*.
3. Performing the derivation in *one direction at a time* — no parallel optimism.
4. Reporting results as found, including negatives.
5. Updating the intuition catalog (analog of `../docs/derivations/00_intuition_catalog.md`) progressively.

If, at any point, the chain breaks irreparably, the framework joins CNSC in the archive — not as a failure, but as a *learning artifact* that taught us *which intuitions matched mathematics and which did not*.

This is the methodology of *honest science*, encoded.
