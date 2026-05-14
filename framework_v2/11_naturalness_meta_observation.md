# 11 — Meta-Observation: All Candidates Face the Same Naturalness Trap

**Date**: 2026-05-14
**Origin**: User observation during the review of `06_C_functional_candidates.md`:
> *"각자가 걸림돌이 되는 부분이 다 다르네 흥미로운데, 아마도 가정한 계수들의 차이 때문에 기각되는 방향으로 가는 것 같기도 하고."*

This document records that meta-observation in technical terms and traces its consequence for framework v2.

## 1. The pattern, restated

Doc 06 examined three candidates for the coherence functional:

| Candidate | Failure mode | Symptom |
|---|---|---|
| C1 ($R^2$) | $\Lambda$CDM not auto-recovered | Requires $\xi_1 / M_*^4 \lesssim 10^{-?}$ tuning |
| C2 ($R_{abcd}R^{abcd}$) | Same | Requires $\xi_2 / M_*^4 \lesssim 10^{-?}$ tuning |
| C3 ($\|\nabla_\perp R\|^2$) | EFT naturalness disfavour | Requires *suppression* of C1, C2 to elevate C3 to leading |

At surface level, the three candidates fail for *different reasons*.  But the deeper observation is: **all three failures reduce to the same question — what value should the dimensionless coefficient $\xi_i / M_*^n$ take, and why?**

For C1, C2: $\xi/M_*^4$ must be *small enough* not to spoil $\Lambda$CDM, but *large enough* to produce an observable effect.  *Two-sided bound* → fine-tuned.

For C3: $\xi_3/M_*^6$ has *no upper bound from $\Lambda$CDM* (auto-recovered), but its *natural EFT order of magnitude is below all the leading dimension-4 operators*.  Why should it be the dominant coupling?  No microscopic answer.

The user's observation: **the failure modes look superficially different, but they are all instances of the same problem — *the framework's predictions depend critically on coefficient values that have no first-principles motivation*.**

## 2. This is the *Naturalness Problem*

The pattern above has a name in physics: the **Naturalness Problem** (Wilson 1971; 't Hooft 1980).  It states:

> *A dimensionless parameter much smaller (or much larger) than $\mathcal{O}(1)$ requires a microscopic explanation; otherwise it constitutes a fine-tuning.*

In cosmology, this problem appears at several scales:

| Cosmological instance | Required fine-tuning |
|---|---|
| Inflation $\epsilon_V$, $\eta_V$ slow-roll | $\sim 10^{-2}$ |
| Inflation $V \sim (10^{15}\,\text{GeV})^4$ vs Planck $M_P^4$ | $\sim 10^{-12}$ |
| Cosmological constant $\Lambda / M_P^4$ | $\sim 10^{-120}$ |
| Strong CP, $\bar\theta$ | $\sim 10^{-10}$ |
| Higgs mass / Planck mass | $\sim 10^{-17}$ |

Each of these is an *unsolved* problem in mainstream physics, in the sense that *no widely-accepted microscopic explanation exists*.  They are *naturalness puzzles*.

## 3. CNSC inquiry instances

The CNSC framework, before its quantitative skeleton was found non-derivable, contained *several* such fine-tuned coefficients:

| CNSC parameter | Value required to match observation | Naturalness comment |
|---|---|---|
| $\beta / \alpha$ | $10^{-3}$ to $10^{-1}$ | Asserted as "natural hierarchy from symmetry" but never derived |
| $S_{\text{crit}}$ (critical-point sound-speed suppression) | $\sim 10^{-6}$ | Hidden parameter; introduced ad hoc to make the $r$-window match |
| $\eta_{\text{Ising}} = 0.0363$ | Matched Planck via $n_s = 1 - \eta$ | The exponent is mathematically fixed; the *application* to cosmology is the tuned step |
| $T_c \sim 10^{15}$ GeV | Set by hand to give observed energy scales | Microscopic origin unaddressed |
| $\lambda \sim 10^{20}$ GeV² | Same | Same |

Each parameter had *its own argument* in the paper, but together they constituted the *fine-tuning skeleton* of the framework.  When the seven-weakness derivation program ran, the chain broke not because *each parameter individually was unjustified* but because *the chain of inferences linking them did not derive*.

The naturalness problem is *structural*, not localized.

## 4. The meta-observation for framework v2

If framework v2 proceeds with $\mathcal{C}_3 = \exp[-\xi_3 \int |\nabla_\perp R|^2 d\lambda / M_*^6]$, *the same trap awaits*:

- $\xi_3$ must be *large enough* to produce an observationally detectable $c_{\text{eff}}$ deviation (P-α + P-γ of `05_phenomenological_path.md`).
- $\xi_3$ must be *small enough* to satisfy the GRB Lorentz invariance bound (`07_grb_constraint_analysis.md`, to be written).
- The *ratio* of allowed window vs natural EFT value is the *naturalness gap*.  If the window is narrow, the framework is *fine-tuned*; if wide, it is *natural but observationally unconstrained*.

Concrete prediction: when doc 09 ($\xi_3$ order-of-magnitude estimate) is computed, the gap between *observationally allowed $\xi_3$* and *naturally-expected EFT $\xi_3$* will likely be *many orders of magnitude*.  This will be *another fine-tuning*.

**Therefore framework v2, *by construction*, joins the naturalness-puzzle family**.  This does not invalidate it — *all cosmological frameworks face naturalness problems* — but it means framework v2 cannot resolve them either.

## 5. Implications for the inquiry

This meta-observation changes how the *result* of framework v2's continued work should be interpreted:

| If docs 07-09 yield... | Interpretation |
|---|---|
| Working $\xi_3$ window matching observation, *natural* $\xi_3$ | Major success.  But *historically extremely rare* in cosmology. |
| Working $\xi_3$ window matching observation, *fine-tuned* $\xi_3$ | "Phenomenological success but theoretically unsatisfying" — the typical fate of alternative cosmologies. |
| No working $\xi_3$ window | Negative result.  Framework v2 collapses on the same axis as CNSC. |
| GRB constraint excludes all $\xi_3$ | Falsification.  Framework v2 collapses *cleanly*. |

The user's intuition — *"기각되는 방향으로 가는 것 같다"* — corresponds to the third or fourth row, but *also includes the second row*: even if the framework *technically works*, the naturalness problem ensures it remains *theoretically unsatisfying* unless a deeper derivation is found.

## 6. The honest learning

The seven-weakness CNSC inquiry and this meta-observation together point to a *general lesson*:

> *Alternative cosmology frameworks tend to fail not at any single weakness but at a common axis — coefficient fine-tuning.  Each framework's *specific* failure mode is different, but the *root cause* is shared.*

This is **not a flaw of CNSC or framework v2 specifically**.  It is a *structural feature of attempting to build cosmological theories from finite-parameter EFTs*.  Even inflation, the dominant paradigm, faces the same problem (slow-roll fine-tuning).

The pragmatic implication: **a phenomenologically successful alternative cosmology requires *measurement of the relevant coefficient*, not its derivation**.  Inflation survives because $n_s$, $r$, $A_s$ are *measured*, not derived from first principles.  Framework v2's $\xi_3$ would need to be *measured* (e.g., from line-of-sight $c_{\text{eff}}(z)$ correlations) to enter the same category.

This refocuses framework v2's *minimum viable contribution*:

- Not "derive $\xi_3$ from quantum gravity" (impossible in the current state of physics).
- But "*provide a clean phenomenological framework in which $\xi_3$ is *measurable*, and demonstrate that current data either constrains or excludes it*".

That is achievable with `05_phenomenological_path.md` (P-α + P-γ), and it is *the same standard inflation meets*.

## 7. Status update

This meta-observation does *not* require any change to docs 01-08 of `docs/derivations/`.  It is a *post-inquiry reflection* that crystallized in 2026-05-14 during framework v2 work.

It *does* add a new working item to framework v2: **whenever a new candidate or formulation is introduced, explicitly identify the coefficient(s) it depends on and assess whether they fall in the natural EFT range**.  This is now part of `framework_v2/03_methodology.md` (M5 mainstream check) but stated more sharply: *check naturalness alongside derivability*.

The user's observation is now formally captured as an *insight gained during the inquiry*, not a *weakness of framework v2* per se.  Framework v2 inherits the naturalness problem because *all cosmological frameworks do*.

## 8. What this changes about expectation

For the continued work on docs 07, 08, 09:

- *Maintain* the work — concrete derivations of GRB constraint, $\Lambda$CDM recovery, and $\xi_3$ bound are *still valuable*.
- *Expect* the naturalness gap to appear in doc 09.  When it does, *do not retrofit* (do not invent a symmetry to make it small).  *State it explicitly* as another instance of the cosmological naturalness problem.
- *Document* the parallel with mainstream cosmology naturalness puzzles in the doc 09 closing section.

This converts what could be a *disappointing result* ("our $\xi_3$ is fine-tuned") into an *intellectually honest learning artifact* ("our $\xi_3$ is fine-tuned in the same family as Λ, inflation slow-roll, Higgs mass; this is the cosmological naturalness problem and our framework instantiates rather than solves it").

The user has effectively *predicted* the framework's likely fate.  Framework v2's value, in that scenario, becomes its *contribution to the documented family of naturalness instances*, not its *resolution* of any single instance.
