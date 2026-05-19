# Self-Falsification as Method: A Cosmology Case Study

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20176660.svg)](https://doi.org/10.5281/zenodo.20176660)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

*An agricultural engineer's 1-year cosmology framework (CNSC), honestly tested and broken — and what the process taught.*

**A serious-amateur theoretical-cosmology inquiry by an agricultural engineer.**

- **Author**: Hong-Gu Lee (이홍구)
- **Affiliations**:
    - Department of Interdisciplinary Program in Smart Agriculture, Kangwon National University, Chuncheon, Republic of Korea
    - Department of Biosystems Engineering, Kangwon National University, Chuncheon, Republic of Korea
- **Status**: hobby project, taken seriously.  *Not* peer-reviewed.  *Not* an active research program in the author's primary domain.

**On tone**: the *content rigor* in this archive is real — derivations are explicit, results are reproducible, negative outcomes are stated as found.  The *time investment and intent* is hobby.  The two are not in tension: a hobby can be pursued with full intellectual honesty.

**Why this approach**: the author is *not a trained physicist* — the formal background is agricultural engineering / smart agriculture / biosystems engineering.  The cosmology inquiry was conducted *as a way to learn and audit*: by attempting to build a non-inflationary alternative framework from scratch, testing it honestly with mainstream-physics tools, and reporting what failed and what survived.  The point was *not* to advance cosmology research — it was to *learn cosmology through the discipline of self-falsification*.  See [`STORY.md`](STORY.md) (Korean) or [`STORY_en.md`](STORY_en.md) (English) for the personal narrative of how this inquiry began, evolved, and closed.

**One-line summary**: A one-year exploration of CNSC (Critical Null-Structured Cosmology), a non-inflationary cosmology framework.  Systematically tested in May 2026 — every novel quantitative claim found mathematically non-derivable (7 weaknesses in the original framework + 1 in a successor "framework v2").  The repository preserves the inquiry as an *idea archive*: what failed and what (small subset) survived.

**This is not a peer-reviewed publication.**  Do not cite the framework documents as validated cosmology theory.

For citation metadata, see [`CITATION.cff`](CITATION.cff).  The archive is published with a Zenodo DOI (visible as a badge above) for permanent citation.

---

## For agricultural engineers / non-cosmology readers (1-page summary)

You may be reading this because the author is *one of you* — an agricultural engineer who pursued theoretical cosmology as an extracurricular interest.  The cosmology content is not the deliverable for you; it is the *test case*.  The deliverable is the **methodology**, codified as M1–M8 in `framework_v2/03_methodology.md`:

| Rule | Short form |
|---|---|
| M1 | Axiomatic forward — classify every claim as verifiable / assumed / derived *before* writing |
| M2 | No negative existentials — "there is no mechanism for X" is forbidden |
| M3 | Derive before claim — predictions appear only after the derivation chain is closed |
| M4 | Periodic audit — hostile peer review on the current document set at every milestone |
| M5 | Mainstream alignment check — every assumption must have a literature precedent |
| M6 | Foundation coherence — new constructions must align with surviving foundations |
| M7 | Stop conditions accepted in advance — framework collapse is allowed, not feared |
| M8 | Single source of truth — each value defined in exactly one document |

These rules transfer directly to:
- **Precision-agriculture ML model verification**: do your model claims (accuracies, feature importances) have first-principles support, or are they post-hoc rationalizations on a particular test split?
- **Hyperspectral / sensor-fusion algorithm validation**: M1–M3 catch the *"it worked on our data, must generalize"* trap.
- **Robotics and autonomous-system safety claims**: M2's negative-existential ban catches *"this can't fail because…"* failure modes.

The cosmology case study in this repository is *training material* for the methodology.  A natural follow-up applied paper — *"axiomatic + honest-derive methodology in precision-agriculture ML"* — would be the transfer of this inquiry to the author's (and reader's) primary domain.

**If you only have 15 minutes**: read `framework_v2/03_methodology.md` and `framework_v2/04_user_specific_core.md`.  Skip everything else unless the cosmology case itself is of interest.

---

## What this repository is — and what it isn't

This is a *personal exploration* of an alternative non-inflationary cosmology framework that the author pursued as an extracurricular interest while working in agricultural engineering / smart agriculture / biosystems engineering at Kangwon National University.  The project ran for approximately one year and culminated in May 2026 in a systematic seven-weakness derivation program that *honestly tested* whether the framework's quantitative claims could be derived from the stated assumptions.

**It IS**:
- A *fully documented record* of what was attempted and what failed.
- A *case study* of the *axiomatic + honest-derive* methodology developed during the inquiry.
- A *catalog* of which intuitions about photon-perspective cosmology survived mathematical testing.
- An *idea archive* — useful as a learning resource for anyone considering a similar alternative-cosmology attempt.

**It is NOT**:
- A peer-reviewed scientific publication.
- A claim that the CNSC framework is a valid cosmological theory.  (Most of its novel quantitative content was found *not derivable*.)
- An active research program in the author's primary academic domain.
- A submission to any astrophysics journal.

## Quick navigation — what survived the inquiry

After the seven-weakness derivation program:

- ✅ **Fully defensible** (2 intuitions): SR null kinematics; stiff-matter horizon resolution.  *Both standard physics.*
- 🟡 **Partial defensible** (2 intuitions): hypersurface-orthogonal eikonal null field; cosmological phase transitions occur generically.  *Restrictions required.*
- ❌ **Not defensible** (7 intuitions): DBI saturation envelope, Ising universality $n_s$ mapping, scale-dependent $f_{NL}$, quadrupolar $f_{NL}^{(2)}$, photon → cosmology metaphorical leap, horizon-crossing inheritance, shear-coupling $r$.

All seven novel quantitative claims of the original framework collapsed.  Standard cosmology pieces and a separate path-integral coherence VSL hypothesis (developed late in the inquiry) survived.  Full details: `docs/derivations/00_intuition_catalog.md`.

## Original Project Directory Notes (Post-Pivot State, 2026-05-13)

This directory underwent a major **pivot** on 2026-05-13.  The original CNSC paper-form work was archived after a systematic 7-weakness derivation program found that the framework's quantitative skeleton is *not mathematically derivable* from its stated assumptions.

The pivot's full record is in `docs/PROJECT_STATUS.md`.  The honest derivation results are in `docs/derivations/`.  The new direction is in `framework_v2/`.

## Current Directory Layout

```
.
├── README.md                                   ← you are here
├── LICENSE                                     ← CC BY 4.0
├── CITATION.cff                                ← citation metadata (Zenodo auto-reads)
├── .gitignore
├── docs/
│   ├── PROJECT_STATUS.md                       ← project history + final verdict
│   └── derivations/                            ← 7-weakness derivation inquiry (intellectual output)
│       ├── 00_intuition_catalog.md             ← 11+1 intuitions classified by mathematical defensibility
│       ├── 01_gamma_k_second_order.md          ← weakness 1: γ(k) bare expansion, negative
│       ├── 02_gamma_k_with_metric_coupling.md  ← weakness 1 Path 2 (metric coupling), confirms negative
│       ├── 03_stiff_matter_mukhanov_sasaki.md  ← weakness 2 (n_s inheritance), no freeze-in mechanism
│       ├── 04_photon_to_null_cosmology.md      ← weakness 5, metaphorical leap not derivable
│       ├── 05_null_dynamics_well_posedness.md  ← weakness 6, partial under hypersurface-orthogonal restriction
│       ├── 06_Z2_LG_microscopic_origin.md      ← weakness 7, fine-tuned ansatz; Kibble-Zurek produces defects not spectrum
│       ├── 07_r_formula_cascade.md             ← weakness 3 cascade, no well-defined P_ζ to take ratio
│       └── 08_what_remains_and_what_next.md    ← 4 surviving intuitions + four next-direction options
├── framework_v2/                               ← post-CNSC redirect (started after weakness inquiry)
│   ├── README.md                               ← reading order: 14 → 11 → 04 → 03
│   ├── 00_foundations.md                       ← F1-F4 (4 surviving intuitions, all standard substrate)
│   ├── 01_coherence_VSL_seed.md                ← H1 path-integral coherence VSL hypothesis
│   ├── 02_open_questions.md                    ← OQ1-OQ5 with realistic time estimates
│   ├── 03_methodology.md                       ← M1-M8 axiomatic + honest-derive rules ★ (transferable)
│   ├── 04_user_specific_core.md                ← what is uniquely the user's vs borrowed
│   ├── 05_phenomenological_path.md             ← P-α + P-γ concrete starting plan
│   ├── 06_C_functional_candidates.md           ← three candidate ansätze; C3 (|∇_⊥R|²) tentatively selected
│   ├── 11_naturalness_meta_observation.md      ← user's meta-observation: alternative cosmologies face the naturalness trap
│   ├── 12_physical_origins.md                  ← physical-origin trace of every fine-tuned parameter; priors defined
│   ├── 13_forward_models_and_root_cause.md     ← forward maps for CNSC and framework v2; root-cause methodology
│   └── 14_grid_search_results.md               ← ★ final substantive deliverable: grid search executed, framework v2 H1 also fails
└── outputs/
    ├── figures/                                ← PNG + CSV + desc.md triples from the inquiry
    └── verification/                           ← reproduction and audit scripts (Python + JSON)
```

★ marks the *single most transferable artifact* (M1-M8 methodology) and the *final substantive deliverable* (grid search verdict).

## What Happened on 2026-05-13

A systematic test of the 7 weaknesses identified by the audit (`archive_cnsc_paper_2026-05-13/supporting_docs/CNSC_Verification_Audit_2026.md`) was performed.  Each weakness was approached as an *honest derivation attempt* — success, partial, or negative results were reported as found.

**Result**: 7 of 7 weaknesses returned negative or cascade-negative.  The CNSC framework's *novel* quantitative content (DBI-saturation $f_{NL}(k)$ shape, Ising universality $n_s$ derivation, quadrupolar $f_{NL}^{(2)}$, $r$-window) is not mathematically derivable from the stated assumptions.

The catalog of which 11 user-intuitions survived mathematically (`docs/derivations/00_intuition_catalog.md`) is the inquiry's primary intellectual output.  The new framework v2 starts from the 4 surviving intuitions plus the user's independent *path-integral coherence VSL* insight, which was developed during the inquiry but is independent of CNSC's failed components.

## Navigation

- *I want the human story behind this archive*: read [`STORY.md`](STORY.md) (Korean original) or [`STORY_en.md`](STORY_en.md) (English version).
- *I want the final verdict in one document*: read `framework_v2/14_grid_search_results.md`.
- *I want the methodology (most transferable)*: read `framework_v2/03_methodology.md`.
- *I want the meta-observation on naturalness*: read `framework_v2/11_naturalness_meta_observation.md`.
- *I want the full intuition catalog*: read `docs/derivations/00_intuition_catalog.md`.
- *I want the technical detail of any one weakness*: read the corresponding `0X_*.md` derivation document.
- *I want the original CNSC paper drafts*: they are *not* in this repository.  The author kept them privately as a learning archive; the public release omits them to prevent misuse as if validated theory.

## Status

- **Inquiry**: complete (2026-05-14).  No novel quantitative cosmological content surviving in either CNSC (7 weaknesses) or framework v2 (1 ansatz inadequacy).
- **Methodology M1-M8**: codified, domain-transferable, ready to apply in the author's primary domain (agricultural-engineering ML verification).
- **Intuition catalog**: 12 intuitions classified into 4 defensibility tiers.
- **This repository**: a *closed* archive of the inquiry's results.  Subsequent work (if any) would be in a *different* repository on a *different* topic.
