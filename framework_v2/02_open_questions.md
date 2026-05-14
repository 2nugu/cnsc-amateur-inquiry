# Framework v2 — Open Questions

**Date**: 2026-05-13
**Status**: An inventory of what must be answered *before* any quantitative claim in framework v2.

These questions are stated *before* any derivation is attempted — this is the *axiomatic + honest-derive* methodology learned from the CNSC inquiry (see `03_methodology.md`).

## OQ-1: Explicit form of the coherence functional $\mathcal{C}$

The hypothesis H1 of `01_coherence_VSL_seed.md` introduces $\mathcal{C}[R_{\mu\nu\rho\sigma}, \gamma]$ as a functional of curvature along the photon path.  The question:

**Among (a) Berry phase, (b) Hartle-Gell-Mann decoherence functional, (c) entanglement entropy across curvature patches, or (d) something else, which gives the correct form of $\mathcal{C}$ for the photon path integral in inhomogeneous curvature?**

This question has *no a priori* answer.  Each candidate has theoretical baggage:
- Berry phase modifies polarization, not amplitude — incompatible with simple VSL interpretation.
- Decoherence functional gives amplitude loss but its derivation from first principles is technically involved.
- Entanglement entropy is the most mainstream but requires choosing a bipartition prescription.

**Required action**: a careful derivation comparing the candidates against the *operational definition* — what does $c_{\text{eff}}$ mean as an observable? — should select among them.

## OQ-2: Energy-independence at leading order

GRB constraints on Lorentz invariance violation require that any deviation from $c_0$ be either *Planck-suppressed* or *energy-independent* (or both).

Specifically, the Fermi-LAT GRB 090510 analysis (Abdo et al. 2009) constrains the deviation

$$\frac{\Delta c}{c_0}(E) \lesssim \frac{E}{M_P}$$

at $E \sim$ GeV scales.  For a *cosmological* coherence effect to be *non-Planck-suppressed*, $\mathcal{C}$ must produce a *common* $\Delta c$ for all photon energies.

**Required action**: derive the energy-dependence of $\mathcal{C}$ from the chosen formalism (OQ-1), and verify it is energy-independent at leading order.  If this fails, the entire framework collapses against GRB constraints.

## OQ-3: Distinct observational signature

If H1 holds, what *distinct* observable distinguishes it from standard $\Lambda$CDM + GR?  Candidates:

(a) **Apparent magnitude-redshift relation deviations**: $d_L(z)$ would deviate from standard if $c_{\text{eff}}$ varies with $z$ via accumulated curvature inhomogeneity.  Currently we measure $d_L(z)$ with Type Ia supernovae and BAO; *both* would have to be re-analyzed with this hypothesis.

(b) **Correlate-with-LSS anisotropy**: photon paths through over-dense regions might have a different $c_{\text{eff}}$ than through under-dense regions.  Correlate the *anomalous magnitude* with weak-lensing maps of the same line-of-sight.

(c) **CMB hemispherical asymmetry**: the existing $\sim 3\sigma$ Planck anomaly *could* — speculatively — be a coherence-VSL effect along the asymmetry axis.

(d) **Stochastic gravitational-wave background**: decoherence of metric perturbations in early universe could produce a specific SGW spectrum, possibly testable by PTA / DECIGO.

**Required action**: derive at least one *quantitative prediction* with controlled error bars, and show it is *distinguishable* from $\Lambda$CDM at current or near-future observational precision.

## OQ-4: Connection to standard cosmology

If framework v2 (foundations + H1) is to be a *publishable* cosmological framework, it must:

- Reproduce standard $\Lambda$CDM in the homogeneous limit ($\mathcal{C} \to 1$).
- Not contradict BBN constraints, Planck CMB precision, BAO measurements, etc.
- Not introduce additional fine-tuned parameters beyond standard $\Lambda$CDM.

**Required action**: explicit check that the homogeneous limit recovers $\Lambda$CDM, and that the coherence effect is *small* in regimes where $\Lambda$CDM is observationally tight.

## OQ-5: Theoretical consistency with quantum gravity programs

Framework v2's H1 is compatible *in spirit* with AdS/CFT, ER=EPR, etc.  But *compatibility in spirit* is weak.

**Required action**: derive H1 *within* one of these programs (e.g., from a tensor-network model of cosmological spacetime), rather than asserting it as an independent hypothesis.  Without such derivation, H1 remains a *suggestive analogy*, not a theory.

## Prioritization

| Question | Priority | Difficulty | Estimated time | Notes |
|---|---|---|---|---|
| OQ-1 (form of $\mathcal{C}$ — derive from QG formalism) | High but bypassable | **Very high** — actually an open research problem | 6 months to years | Can be **bypassed** by phenomenological ansatz (see `05_phenomenological_path.md`) |
| OQ-2 (energy independence) | **Critical** — passes/fails GRB test | Low if ansatz is energy-independent by construction | 1 week | Phenomenological ansatz of `05_*.md` is energy-independent by construction → automatically passes |
| OQ-3 (distinct observable) | High | Medium (with §2.4 of `05_*.md`) | 2-3 weeks | Weak-lensing correlation diagnostic is the cleanest |
| OQ-4 ($\Lambda$CDM limit) | High | Low (built into ansatz: $\mathcal{C}\to 1$ when $\nabla R \to 0$) | 1 week | Automatic for the $|\nabla R|^2$ ansatz |
| OQ-5 (QG embedding) | Low for first paper; high for long-term | Very high | months to years | Defer to follow-up work after phenomenological success |

**Honest revision** (after `05_phenomenological_path.md` was added):
- Original estimate "6-10 weeks to first quantitative claim" was *optimistic in the derive-first interpretation*.
- For the *derive-first* path (closing OQ-1 from a fundamental theory first), the realistic time is **6 months to years**, with **30-40% probability of negative cascade** similar to CNSC.
- For the *phenomenological-first* path (P-α + P-γ of `05_*.md`), the realistic time is **~2 months to first publishable claim**.  This is the **recommended starting path**.

## Stop condition

If OQ-1 cannot be answered (no consistent form of $\mathcal{C}$ exists), or OQ-2 fails (GRB falsifies any form), the framework collapses.  In that case the CNSC inquiry's *negative-result methodology* applies again, and framework v2 joins CNSC as a *learning artifact*, not a publishable result.

This stop condition is *explicit and accepted* — see `../memory/feedback_truth_over_theory.md`.

**For the phenomenological path (`05_*.md`)**, the stop conditions are *different*:
1. GRB constraint rules out all $\xi$.  (Unlikely given construction.)
2. Joint fit to $\Lambda$CDM data shows no improvement.
3. Weak-lensing correlation diagnostic returns null at Euclid precision.

These are *clean observational stop conditions*, faster to reach than the derive-first stop conditions on OQ-1.  The phenomenological path is *more efficient as a falsifiability machine*.
