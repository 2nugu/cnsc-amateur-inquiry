# 12 — Physical Origins of All Fine-Tuned Parameters

**Date**: 2026-05-14
**Purpose**: Trace, for every fine-tuned parameter that appeared in CNSC (now archived) and that would appear in framework v2 + comparable alternative cosmologies, the *origin* of its assumed value or range.  This document establishes the *prior physical ranges* that the subsequent multi-parameter grid search will use.

**Framing — not a revival attempt**: CNSC is archived; this document does *not* attempt to resuscitate it.  The CNSC parameters appear here for *retrospective analysis only* — answering the question *"given the framework, where in parameter space could it have survived observational constraints?"*.  Whether such regions exist is a fact about the framework; identifying them is *not* the same as endorsing the framework.  All CNSC mechanism-level weaknesses (the 7 weaknesses of `docs/derivations/`) remain mathematically not-derivable regardless of grid search outcomes.

The user's principle (2026-05-14):
> *"피지컬 오리진부터 수행되어야 나머지 그리드 서칭이 명확하게 되겠는데?"*

Without explicit physical priors, brute-force grid search is *p-hacking*.  With them, it becomes *systematic parameter-window mapping*.

## 1. Tracing standards

For each parameter $\pi_i$ we record:

| Field | Meaning |
|---|---|
| **Symbol** | mathematical notation |
| **Domain** | range of dimension (mass, dimensionless, etc.) |
| **Assumed value** | what the framework took as fiducial |
| **Origin** | where the assumption came from — measured, derived, dimensional, ad hoc |
| **Natural prior** | range justified by physics |
| **Stretched prior** | range justified by being "not unreasonable" (for the grid search to test) |
| **Observational error bar** | tightest current measurement (if any) |
| **Bibliographic source** | one canonical reference where the origin can be traced |

## 2. CNSC parameters (archived; for retrospective grid search)

### 2.1 GUT scale $M_{\text{GUT}}$

| Field | Value |
|---|---|
| Symbol | $M$ in $\mathcal{L}_{\text{null}}$ |
| Domain | mass (GeV) |
| Assumed value | $10^{16}$ GeV |
| Origin | dimensional analysis: gauge-coupling unification in supersymmetric GUTs gives $\sim 2\times 10^{16}$ GeV |
| Natural prior | $[10^{15}, 10^{17}]$ GeV (GUT-scale uncertainty) |
| Stretched prior | $[10^{12}, 10^{19}]$ GeV (EW to Planck) |
| Observational error bar | indirect via $\sin^2\theta_W$, $\alpha_s(M_Z)$ → $M_{\text{GUT}}$ to factor ~ 3 |
| Source | Georgi-Quinn-Weinberg 1974; modern review Raby 2002 |

### 2.2 DBI coupling $\lambda$

| Field | Value |
|---|---|
| Symbol | $\lambda$ in $\gamma = \sqrt{1+\lambda\mathcal{I}/M^4}$ |
| Domain | mass$^2$ (GeV$^2$) |
| Assumed value | $10^{20}$ GeV$^2$ |
| Origin | matching condition: $\gamma$ should saturate near $k_*$; numerical convenience |
| Natural prior | not derived from any first principles; pure ansatz |
| Stretched prior | $[10^{16}, 10^{24}]$ GeV$^2$ (covers $\bar\gamma$ from near 1 to $\gg 1$) |
| Observational error bar | none direct |
| Source | none — assumed in CNSC_Paper_Draft_PRD.md §II.B |

### 2.3 Primordial amplitude $\Phi_0$

| Field | Value |
|---|---|
| Symbol | $\Phi_0$ in null-vector normalization |
| Domain | dimensionless |
| Assumed value | $10^{-5}$ |
| Origin | matched to observed CMB amplitude $A_s^{1/2} \approx 4.6\times 10^{-5}$; rounded to one significant figure |
| Natural prior | $[10^{-6}, 10^{-4}]$ (within 1 dex of observed $A_s$) |
| Stretched prior | $[10^{-10}, 10^{-2}]$ (covers all reasonable scalar amplitudes) |
| Observational error bar | $A_s = 2.10 \pm 0.03 \times 10^{-9}$ from Planck → $A_s^{1/2}$ at < 1% |
| Source | Planck 2018 cosmological parameters, A&A 641, A6 |

### 2.4 Transition Hubble $H_*$

| Field | Value |
|---|---|
| Symbol | $H_*$ (Hubble parameter at phase transition) |
| Domain | mass (GeV); also expressed as $H_*/M_P$ |
| Assumed value | $H_*/M_P \approx 10^{-10}$ → $H_* \approx 10^9$ GeV |
| Origin | chosen so $T_c \sim$ GUT scale and Friedmann gives this $H$ |
| Natural prior | $H_*/M_P \in [10^{-12}, 10^{-8}]$ |
| Stretched prior | $H_*/M_P \in [10^{-30}, 10^{-5}]$ |
| Observational error bar | for inflationary frameworks: $H_*/M_P < 6\times 10^{-6}$ from $r < 0.06$ (BICEP/Keck 2021); for non-inflationary CNSC, no direct bound |
| Source | derived from $T_c$ + Friedmann; T_c assumed |

### 2.5 β/α hierarchy

| Field | Value |
|---|---|
| Symbol | $\beta_{\text{eff}}/\alpha_{\text{eff}}$ in null action $\mathcal{I} = \alpha\theta^2 + \beta\sigma^2$ |
| Domain | dimensionless |
| Assumed value | $[10^{-3}, 10^{-1}]$ |
| Origin | "natural hierarchy" assertion in CNSC; not derived |
| Natural prior | none — the assertion *is* the prior |
| Stretched prior | $[10^{-6}, 1]$ (covers strong hierarchy to no hierarchy) |
| Observational error bar | none direct |
| Source | CNSC_Beta_Alpha_Derivation.md (archived) — argument is dimensional, not first-principles |

### 2.6 Ising anomalous dimension $\eta_{3\text{D Ising}}$

| Field | Value |
|---|---|
| Symbol | $\eta$ in 3D Ising CFT |
| Domain | dimensionless |
| Assumed value | $0.036298(2)$ |
| Origin | conformal bootstrap |
| Natural prior | $0.0363 \pm 0.0001$ (bootstrap precision) |
| Stretched prior | $[0.03, 0.05]$ (covers various 2-pt function fitting methods) |
| Observational error bar | matched to $n_s = 0.9649 \pm 0.0042$ via $n_s = 1 - \eta$ → *consistency check, not measurement of $\eta$ itself* |
| Source | Simmons-Duffin 2017 (JHEP 03, 086); Pelissetto-Vicari 2002 review |

### 2.7 Critical-point suppression $S_{\text{crit}}$

| Field | Value |
|---|---|
| Symbol | $S_{\text{crit}}$ (introduced post-hoc in 2026-05-13 audit) |
| Domain | dimensionless |
| Assumed value | $10^{-6}$ |
| Origin | *ad hoc adjustment* to make $r$-window match observational sensitivity range; no derivation |
| Natural prior | none — this parameter is *constructed* for the framework |
| Stretched prior | $[10^{-15}, 10^{0}]$ (no upper or lower bound) |
| Observational error bar | none |
| Source | docs/CNSC_Verification_Audit_2026.md §7bis (archived) |

### 2.8 Critical temperature $T_c$

| Field | Value |
|---|---|
| Symbol | $T_c$ (cosmological phase transition temperature) |
| Domain | mass (GeV) |
| Assumed value | $10^{15}$ GeV |
| Origin | chosen near GUT scale to match $n_s$ derivation chain |
| Natural prior | $[10^{14}, 10^{16}]$ GeV (GUT-related range) |
| Stretched prior | $[10^{2}, 10^{18}]$ GeV (EW to Planck-1) |
| Observational error bar | none — no measurement |
| Source | CNSC_Phase_Transition_Dynamics.md (archived) |

## 3. Framework v2 parameters

### 3.1 Coherence coupling $\xi_3$

| Field | Value |
|---|---|
| Symbol | $\xi_3$ in $\mathcal{C} = \exp[-\xi_3 \int |\nabla_\perp R|^2 d\lambda / M_*^6]$ |
| Domain | dimensionless |
| Assumed value | unspecified; grid search target |
| Origin | introduced as a free parameter in framework_v2/06 |
| Natural prior | $\xi_3 \sim \mathcal{O}(1)$ (EFT natural) |
| Stretched prior | $[10^{-30}, 10^{30}]$ (no prior from physics; allow brute search) |
| Observational error bar | none direct; bounded by GRB 090510 indirectly |
| Source | framework_v2/06_C_functional_candidates.md |

### 3.2 Characteristic mass $M_*$

| Field | Value |
|---|---|
| Symbol | $M_*$ in framework v2 ansatz |
| Domain | mass (GeV) |
| Assumed value | unspecified; grid search target |
| Origin | introduced as a free parameter in framework_v2/06 |
| Natural prior | $M_* \sim M_P$ (Planck-scale natural) |
| Stretched prior | $[10^{10}, 10^{20}]$ GeV (mid-EFT to super-Planck) |
| Observational error bar | none |
| Source | framework_v2/06_C_functional_candidates.md |

## 4. Other alternative cosmology parameters (reference context)

For cross-framework grid-search comparison, brief catalog:

### 4.1 Inflation

| Parameter | Value | Natural prior | Comment |
|---|---|---|---|
| $\epsilon_V$ (1st slow-roll) | $\sim 10^{-2}$ | $[10^{-4}, 10^{-1}]$ | tighter from $r$ constraint |
| $\eta_V$ (2nd slow-roll) | $\sim 10^{-2}$ | $[10^{-4}, 10^{-1}]$ | tighter from $n_s$ |
| $V^{1/4}$ inflaton potential | $\sim 10^{16}$ GeV | $[10^{14}, 10^{17}]$ GeV | from $H_*$ |
| $N_e$ e-foldings | $50 - 60$ | $[40, 70]$ | from horizon problem solution |

### 4.2 Ekpyrotic

| Parameter | Value | Natural prior | Comment |
|---|---|---|---|
| Brane separation $d$ | model-dependent | order $M_P^{-1}$ | string-theoretic |
| Potential exponent $\bar p$ | $\sim 10^{-2}$ | $[10^{-3}, 10^{-1}]$ | for fast-roll |
| Energy scale | $\sim 10^{16}$ GeV | $[10^{14}, 10^{17}]$ GeV | |

### 4.3 Cyclic (Steinhardt-Turok)

| Parameter | Value | Natural prior | Comment |
|---|---|---|---|
| Cycle period | $\sim 10^{12}$ yr | $[10^{10}, 10^{14}]$ yr | model-dependent |
| Dark-energy slow-roll | $\epsilon \sim 10^{-2}$ | $[10^{-3}, 10^{-1}]$ | |

### 4.4 Pre-Big Bang (Veneziano-Gasperini)

| Parameter | Value | Natural prior | Comment |
|---|---|---|---|
| Dilaton coupling | string-derived | tightly constrained | |
| String coupling $g_s$ | $< 1$ | $[10^{-2}, 10^0]$ | |

These reference data come from review articles (Lyth-Riotto 1999 for inflation; Lehners 2008 for ekpyrotic; Steinhardt-Turok 2002 for cyclic; Gasperini-Veneziano 2003 for pre-Big Bang).

## 5. Summary of priors for the grid search

Compact table of CNSC + framework v2 priors actually usable in the grid search (`outputs/verification/multi_framework_grid.py`, to be written next turn):

| Parameter | Natural prior | Stretched prior | Type |
|---|---|---|---|
| $M_{\text{GUT}}$ | $[10^{15}, 10^{17}]$ GeV | $[10^{12}, 10^{19}]$ GeV | log-uniform |
| $\lambda$ | none | $[10^{16}, 10^{24}]$ GeV$^2$ | log-uniform |
| $\Phi_0$ | $[10^{-6}, 10^{-4}]$ | $[10^{-10}, 10^{-2}]$ | log-uniform |
| $H_*/M_P$ | $[10^{-12}, 10^{-8}]$ | $[10^{-30}, 10^{-5}]$ | log-uniform |
| $\beta/\alpha$ | none | $[10^{-6}, 1]$ | log-uniform |
| $\eta_{\text{Ising}}$ | $0.0363 \pm 0.0001$ | $[0.03, 0.05]$ | Gaussian (natural) or uniform (stretched) |
| $S_{\text{crit}}$ | none | $[10^{-15}, 10^{0}]$ | log-uniform |
| $T_c$ | $[10^{14}, 10^{16}]$ GeV | $[10^{2}, 10^{18}]$ GeV | log-uniform |
| $\xi_3$ (frw v2) | $\mathcal{O}(1)$ around 1 | $[10^{-30}, 10^{30}]$ | log-uniform |
| $M_*$ (frw v2) | $\sim M_P$ | $[10^{10}, 10^{20}]$ GeV | log-uniform |

10 parameters total.  Full *outer-product grid* with 10 points per dimension = $10^{10}$ points (intractable).  Practical approach:

1. **2D slices**: pick 2 parameters at a time, hold others at natural values.
2. **Monte Carlo random sampling**: uniformly sample in stretched priors, ~$10^5$ points.
3. **Conditional grids**: condition on subset of parameters being at observational central values.

## 6. Observational constraints to apply

Constraints that the grid search will evaluate at each parameter point:

| Constraint | Source | Tolerance |
|---|---|---|
| $A_s$ matching | Planck CMB amplitude | within 5% |
| $n_s$ matching | Planck CMB tilt | $n_s = 0.9649 \pm 0.0042$ |
| $r$ upper bound | BICEP/Keck 2021 | $r < 0.06$ |
| GRB LIV bound | Fermi-LAT 2009 | $M_{\text{LIV}} > M_P$ |
| BBN compatibility | $\Delta N_{\text{eff}}$ < 0.3 | $\rho_{\text{exotic}}/\rho_r < 0.1$ at BBN |
| Sound horizon $r_s$ | Planck | $r_s = 147 \pm 0.3$ Mpc |
| H0 (local) | Riess et al. SH0ES | $73.0 \pm 1.0$ km/s/Mpc |
| H0 (CMB) | Planck | $67.4 \pm 0.5$ km/s/Mpc |
| Supernova $d_L(z)$ | Pantheon+ | ~ 1% systematic |

## 7. What this document achieves

By tracing the *physical origin* of every fine-tuned parameter and defining *natural vs stretched priors* explicitly:

- The next-turn grid search will have **well-defined search ranges**.
- Each "viable region" output will be **physically interpretable** (within natural priors vs requires stretched priors).
- The CNSC retrospective question — *"could any of CNSC's 7 weaknesses be saved by parameter-window rebound?"* — becomes **quantitatively answerable** for weaknesses #4 (S_crit) and #7 (T_c, η).
- The framework v2 prospective question — *"does an observable-and-allowed window exist for (ξ_3, M_*) + any companion parameters?"* — becomes **directly testable**.

## 8. What this document does NOT do

- It does *not* solve the naturalness problem.  Each parameter's natural prior is bounded but the *combined* fine-tuning across all parameters can be arbitrarily severe.
- It does *not* claim to enumerate *all* possible alternative cosmology parameters.  §4 is a sketch.
- It does *not* derive any parameter from first principles.  Origin tracing is *historical* (where did the value come from in published work), not *theoretical* (why must it have that value).

The first-principles derivation question remains open — and is exactly what the CNSC inquiry showed *cannot* be answered with the current framework.  Grid search is the *pragmatic substitute*: instead of deriving, **map the parameter window that is consistent with observation**.

## 9. Next step

`outputs/verification/multi_framework_grid.py` (next turn) will implement the grid search using:

- All 10 parameters with natural and stretched priors from §5.
- All 9 observational constraints from §6.
- 2D-slice + Monte Carlo + conditional-grid strategies from §5.
- Output: `outputs/figures/multi_framework_viable_region_*.png` (one per 2D slice) + `outputs/verification/multi_framework_result.json` (full posterior summary).
