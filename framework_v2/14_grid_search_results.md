# 14 — Grid Search Results and Final Verdict

**Date**: 2026-05-14
**Source**: `outputs/verification/multi_framework_grid.py` + `multi_framework_result.json`
**Scope**: CNSC retrospective + Framework v2 prospective parameter grids.

## 1. CNSC retrospective — confirmed Scenario 2

Grid search of 2D slice (M_GUT, T_c) with all 9 observational constraints from Doc 13 §6:

| Result | Value |
|---|---|
| Accepted fraction (full grid) | 1.000 (constraint set is information-poor for CNSC) |
| Accepted fraction (natural prior box) | 1.000 |
| Genuine constraints among 9 | 1 (BBN only; see Doc 13 §3.6) |
| Predetermined fine-tuned parameters | 3 ($\lambda$, $\beta/\alpha$, $S_{\text{crit}}$) |

**Interpretation**: CNSC, *had it been physically derivable*, would have *observationally survived* within natural priors of its 5 derivable parameters ($M_{\text{GUT}}, \Phi_0, H_*, \eta_{\text{Ising}}, T_c$).  But survival required *3 fine-tunings* (parameters with no natural prior) — placing CNSC in Doc 11's **Scenario 2: "phenomenologically works, theoretically unsatisfying"**.

This is *not* a revival of CNSC.  CNSC's *mechanism-level* failures (the 7 weaknesses of `docs/derivations/`) are mathematically *independent* of grid search outcomes.  The grid search merely confirms that *had the mechanism issues been ignored*, CNSC would have joined the standard family of fine-tuned cosmological alternatives.

See `outputs/figures/grid_cnsc_M_Tc.png`.

## 2. Framework v2 prospective — *negative*

Grid search of (xi_3, M_*) plane, exploring xi_3 ∈ $[10^{-30}, 10^{60}]$ and $M_* \in [10^8, 10^{22}]$ GeV (extended beyond Doc 12 stretched priors).

Forward model: $\Delta\mathcal{C}(z) = \xi_3 / M_*^6 \cdot \int_0^z |\nabla_\perp R|^2 / H(z') dz'$ with LCDM background curvature.

Computed line integrals:

| $z_{\max}$ | $\int |\nabla_\perp R|^2 / H dz'$ (GeV^5) |
|---|---|
| 0.1 | $6.3 \times 10^{-216}$ |
| 1.0 | $3.0 \times 10^{-214}$ |
| 1100 | $2.3 \times 10^{-191}$ |

The integral at $z = 1$ is *astronomically small*.  For $\Delta\mathcal{C} \sim 1$ at $z=1$ (observable scale), we'd need

$$\xi_3 / M_*^6 \sim 10^{214}\;\mathrm{GeV}^{-5} \quad\Rightarrow\quad M_* \lesssim 10^{-35}\;\mathrm{GeV}\;(\text{with }\xi_3 \sim 1)$$

or $M_* \sim M_P$ with $\xi_3 \sim 10^{327}$ — both physically meaningless.

### 2.1 Final grid-search verdict for framework v2

| Question | Answer |
|---|---|
| Allowed & observable region exists? | **No** (within explored grid) |
| H_0 tension window exists? | **No** |
| Natural region produces observable effect? | **No** |

**Framework v2 in its present ansatz form is cosmologically unobservable at any plausible parameter value.**  The LSS-curvature line-of-sight integral is too small by ~200 orders of magnitude to produce any observable distance-redshift modification.

See `outputs/figures/grid_frameworkv2_xi_Mstar.png` for the visual confirmation: the natural EFT point (white star) sits in a region where $\Delta\mathcal{C} \sim 10^{-330}$.  Even pushing into stretched priors does not bring the effect within observability.

## 3. Why the ansatz fails

The functional choice $\mathcal{C}_3 \propto \exp[-\xi |\nabla_\perp R|^2 / M_*^6]$ has *three suppression factors* stacked:

1. *$|\nabla R|$ is a derivative of curvature*, smaller than $R$ by $1/L$ for characteristic length $L$.
2. *$|\nabla_\perp R|^2$ is squared*, doubling the smallness.
3. *$M_*^6$ in the denominator with $M_*$ at Planck-scale* is enormous.

In LCDM, $R(z=1) \sim H^2 \sim 10^{-84}$ GeV² and $|\nabla R| / R \sim 10^{-5}$ at LSS scale.  Multiplying these:

$$|\nabla_\perp R|^2 / M_*^6 \sim (10^{-84})^2 \cdot (10^{-5})^2 / (10^{19})^6 \sim 10^{-292}\;\mathrm{GeV}^{-2}$$

Integrated over Hubble length $\sim 10^{42}$ GeV$^{-1}$: $\Delta\mathcal{C} \sim 10^{-250}$ at $\xi = 1$.

This is *fundamental* to the ansatz, not a numerical accident.

## 4. Implications

### 4.1 Framework v2 H1 in its minimal form is dead

The user's intuition (path-integral coherence VSL with $|\nabla_\perp R|^2$ as the operative curvature invariant) is *not observable* under the natural EFT scaling.  Two recovery paths:

(a) **Switch to C1 ($R^2$) or C2 (Kretschmann)**: these are $R^2$ or $R_{abcd}R^{abcd}$ — without the gradient squared.  Magnitude ~ $H^4 \sim 10^{-168}$ — still small but *much larger* than the gradient form.  However C1, C2 do not auto-recover LCDM (Doc 06 §3) → require separate fine-tuning of $\xi$ to be small enough.  *Returns to the fine-tuning trap*.

(b) **Sub-leading operator suppression mechanism**: assume the leading C1, C2 are forbidden by some symmetry (Doc 06 §7 sub-question OQ-1a), making $|\nabla_\perp R|^2$ leading.  The required *amplification* would still need to overcome 200+ orders of magnitude — *infeasible*.

(c) **Different physical content of $\mathcal{C}$**: not curvature-driven but something else (entanglement entropy density, quantum complexity, etc.).  Requires deriving from a different formalism — *opens back into OQ-1 of Doc 02, with all its difficulty*.

### 4.2 Intuition catalog update

Add I-12 to the intuition catalog (initial user H1 framing — operational path-integral coherence):

| ID | Intuition | Verdict (post grid search) | Reason |
|---|---|---|---|
| I-12 | Path-integral coherence VSL with curvature-gradient ansatz produces observable cosmological effect | ❌ **Not defensible** | `multi_framework_grid.py` shows $\Delta\mathcal{C}$ is ~250 orders of magnitude below observability |

This raises framework v2's *novel content* failure count to **1**, parallel to the 7 CNSC failures.  Total: **8 failures, 0 surviving novel quantitative content**.

### 4.3 The naturalness verdict, sharpened

Doc 11's prediction was *Scenario 2 (fine-tuned but works)*.  The framework v2 grid search reveals a *worse* scenario:

> **Scenario 5**: *Even with fine-tuning, no observable signal emerges*.  The ansatz is *intrinsically too weak* regardless of parameter values.

Doc 11 §5 table is therefore extended:

| Outcome | CNSC | Framework v2 |
|---|---|---|
| 1. Natural + observational fit | — | — |
| 2. Fine-tuned, fit | ✅ (would have been) | — |
| 3. No working window | — | — |
| 4. Clean falsification | — | — |
| 5. Too weak even with tuning | — | **✅ (actual)** |

## 5. Root-cause tracking — summary

Per Doc 13 §7, the root cause of each parameter fine-tuning is identified:

| Parameter | Root cause | Naturalness gap |
|---|---|---|
| CNSC $\lambda$ | No physics-motivated value | ∞ (predetermined) |
| CNSC $\beta/\alpha$ | "Natural hierarchy" assertion not derived | ∞ (predetermined) |
| CNSC $S_{\text{crit}}$ | Ad-hoc audit fix | ∞ (predetermined) |
| CNSC $M_{\text{GUT}}, \Phi_0, H_*, \eta, T_c$ | Acceptable within natural priors | 0 (no gap) |
| Framework v2 $\xi_3$ | None — no value works | grid empty |
| Framework v2 $M_*$ | Same | grid empty |

The framework v2 *failure mode* is not "$\xi_3$ is fine-tuned" but "no value of $\xi_3, M_*$ produces an observable effect".  This is qualitatively *different* from the CNSC fine-tuning — it's an *ansatz inadequacy*, not a *parameter problem*.

See `outputs/figures/naturalness_gap_bar.png`.

## 6. Final inquiry verdict

After:
- 7 CNSC weaknesses tested honestly (`docs/derivations/01-08`): all negative or partial.
- 4 surviving intuitions cataloged (`docs/derivations/00_intuition_catalog.md`).
- Framework v2 outlined with H1 hypothesis and methodology (`framework_v2/01-05`).
- Naturalness meta-observation crystallized (`framework_v2/11`).
- Physical origins traced for all 10 parameters (`framework_v2/12`).
- Forward models defined and root-cause tracked (`framework_v2/13`).
- Grid search executed (`outputs/verification/multi_framework_grid.py`).

**The final verdict**: 

> **No novel quantitative cosmological content has survived honest derivation or grid search in either CNSC or framework v2.**
>
> CNSC's mechanism issues invalidate it independently of parameters.  Framework v2's minimal ansatz is observationally invisible even at extreme parameter values.  All combined: *the inquiry's quantitative output is null*.
>
> The *non-quantitative* outputs — the methodology M1-M8, the intuition catalog, the failure-mode case studies, the AI-collaborative honest-derivation record — remain as the *intellectual artifacts* of the inquiry.

## 7. What is left for the user

Per `docs/derivations/08_what_remains_and_what_next.md`, four options were available before this grid search.  After it:

| Option | Status after grid search |
|---|---|
| A. Hobby closure | ✅ Cleanly available — the inquiry has reached a *complete* state with no remaining ambiguity |
| B. Methodology transfer to user's primary domain (agricultural engineering) | ✅ Unchanged — M1-M8 are domain-independent |
| C. New framework starting from H1 in mainstream physics tools (AdS/CFT etc.) | △ Possible but requires significant new learning; framework v2's minimal form is not the path |
| D. Negative-result methodology paper | ✅ Strengthened — the grid-search evidence is now part of the record |

**Recommendation**: Option A (hobby closure) is now *natural*.  The inquiry has reached every conclusion it can reach with the user's available time and primary domain.  Further work on this framework family is *not productive*; if the user wishes to continue, it should be a *different framework* under *different premises*.

## 8. Files produced by this turn

- `framework_v2/14_grid_search_results.md` (this file)
- `outputs/verification/multi_framework_grid.py`
- `outputs/verification/multi_framework_result.json`
- `outputs/figures/grid_cnsc_M_Tc.png`
- `outputs/figures/grid_frameworkv2_xi_Mstar.png`
- `outputs/figures/naturalness_gap_bar.png`

## 9. Closure

This document is *the inquiry's final substantive deliverable*.  Subsequent work on this inquiry is administrative (file packaging, release execution) — *not* further derivation.

The intellectual content is complete.
