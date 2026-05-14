# 06 — Candidates for the Coherence Functional $\mathcal{C}$

**Date**: 2026-05-14
**Status**: First substantive analysis after the framework v2 outline. Compares three natural candidates for the functional form of $\mathcal{C}[R_{\mu\nu\rho\sigma}, \gamma]$ defined in `01_coherence_VSL_seed.md` (H1).

## 1. The minimal ansatz family

The hypothesis H1 states $c_{\text{eff}} = c_0 \cdot \mathcal{C}$ with $\mathcal{C}$ a functional of curvature along the photon path $\gamma$.  Natural single-integral forms:

$$\mathcal{C} = \exp\!\left[-\int_\gamma f(R, R_{\mu\nu}, R_{\mu\nu\rho\sigma}, \nabla R, \ldots)\,d\lambda\right]$$

To leading order in curvature invariants, three candidates dominate:

| ID | Form of $f$ | Mass dimension | Heuristic name |
|---|---|---|---|
| **C1** | $\xi_1\,R^2 / M_*^4$ | $-1$ × dim($d\lambda$) → dimensionless if $[\lambda]=[L]$ | Ricci scalar squared |
| **C2** | $\xi_2\,R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} / M_*^4$ | same | Kretschmann scalar |
| **C3** | $\xi_3\,(\nabla R)^2 / M_*^6$ | dimensionless | Curvature *gradient* |

(Other terms — $R_{\mu\nu}R^{\mu\nu}$, $\Box R$, cross terms — are subleading or related to these by Gauss-Bonnet identities.)

## 2. Behaviour on FLRW background

A homogeneous, isotropic FLRW background has

$$R = -\,6\!\left(\dot H + 2H^2\right) \quad\text{(nonzero)},$$
$$R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = 12\!\left(\dot H + H^2\right)^2 + 12 H^4 \quad\text{(nonzero)},$$
$$\nabla_\mu R \;=\; \delta_\mu^0 \dot R \quad\text{(time component only)},$$
$$(\nabla R)^2 = g^{\mu\nu}\nabla_\mu R\,\nabla_\nu R = -\dot R^2 \quad\text{(nonzero on background; }|\nabla R|^2 = -\dot R^2 < 0\text{)}.$$

**Subtle point on C3**: $(\nabla R)^2$ on FLRW is *not* spatial-gradient-only.  The time-derivative $\dot R$ contributes.  *True spatial-gradient-only* requires projecting onto the surface orthogonal to a timelike vector (e.g., the cosmic rest frame).  Define instead

$$|\nabla_\perp R|^2 \;\equiv\; (\delta^{\mu\nu} + u^\mu u^\nu)\,\nabla_\mu R\,\nabla_\nu R \quad\text{with } u^\mu \text{ cosmic rest frame.}$$

Then $|\nabla_\perp R|^2 = 0$ on homogeneous FLRW.  This is the *cosmologically meaningful* version of C3.

We use $|\nabla_\perp R|^2$ for C3 going forward.

## 3. Behaviour summary on FLRW

| Candidate | Value on homogeneous FLRW | $\Lambda$CDM auto-recovery? |
|---|---|---|
| C1 ($R^2$) | $\sim 36 H^4 \neq 0$ | ❌ Requires $\xi_1/M_*^4 \to 0$ tuning |
| C2 ($R_{abcd}R^{abcd}$) | $\sim H^4 \neq 0$ | ❌ Same problem |
| C3 ($\|\nabla_\perp R\|^2$) | $= 0$ identically | ✅ **Automatic** |

**C3 is the only candidate that automatically reduces to $\Lambda$CDM on the homogeneous background**.  C1 and C2 require *fine-tuning* of $\xi$ to be small enough that the background-level deviation doesn't violate observations.

This is the first substantial criterion that *separates* the candidates.

## 4. Alignment with H1 intuition

H1 states (rephrased): *"coherence loss arises when the photon traverses inhomogeneous curvature; uniform curvature does not affect propagation."*

| Candidate | Aligned with H1? |
|---|---|
| C1, C2 | ❌ — they fire even on perfectly uniform curvature |
| C3 | ✅ — fires only on spatial *gradients* of $R$ |

C3 is the *intuition-consistent* choice.  C1 and C2 are *more standard EFT terms* but contradict H1.

## 5. EFT naturalness

In a general curvature-EFT expansion, $R^2$ and $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ appear at the same order ($M_*^{-4}$) as the leading dimension-4 operators beyond Einstein-Hilbert.  $(\nabla R)^2$ is *higher* in derivatives and therefore *subleading* at $M_*^{-6}$.

| Candidate | EFT power counting | Naturalness |
|---|---|---|
| C1, C2 | Leading | Natural |
| C3 | Subleading | **Less natural** — requires a mechanism to suppress C1, C2 |

There is a *tension*: C3 is the *physically intuitive* choice but the *naturalness-disfavoured* choice.

**Possible resolution**: if there is a *symmetry* that forbids $R^2$ and $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ at the level of the relevant coupling — for example, a *shift symmetry* $R \to R + \text{const}$ on the propagation amplitude — then $(\nabla R)^2$ becomes the *leading* allowed term.  Whether such a shift symmetry is natural in the photon path-integral context is *not* settled here.

This is a *case where the inquiry surfaces a sub-question* that would require its own derivation.

## 6. Photon-coupling form

C1 and C2 couple to *all* curvature; C3 couples only to *gradients*.  Physically: in a uniformly curved universe (uniform $R$), C3 predicts $c_{\text{eff}} = c_0$ identically — photons are not slowed by curvature, only by *changes* in curvature along the path.

This matches the user's H1 intuition: *"the photon coherence is lost when crossing patches with *different* spacetime structures."*

C1 and C2 would predict $c_{\text{eff}} < c_0$ even in pure de Sitter space (uniform $R$), which is *not* the user's intuition.

## 7. Preliminary verdict on C-form choice

| Criterion | Preferred candidate |
|---|---|
| Auto $\Lambda$CDM recovery | **C3** |
| Aligned with H1 intuition | **C3** |
| EFT naturalness | C1, C2 |
| Photon-coupling form | **C3** |

**Tentative choice**: C3 ($|\nabla_\perp R|^2$).  Three out of four criteria favour it.  The one criterion against (EFT naturalness) requires a *symmetry argument* to resolve, which is an open sub-question (call it OQ-1a) but does not invalidate C3 as a working ansatz.

## 8. What this analysis is NOT

- It is *not* a derivation of $\mathcal{C}$ from a fundamental theory.  All three candidates remain *phenomenological ansätze*.
- It is *not* a proof that C3 is the *unique* correct form.  Other terms (e.g., $R_{\mu\nu}R^{\mu\nu}$, Weyl tensor invariants) could also be added.
- It is *not* a quantitative prediction.  $\xi_3$ and $M_*$ remain free parameters.

## 9. What this analysis IS

- A *qualitative narrowing* of the ansatz space: from "general functional of curvature" to "use $|\nabla_\perp R|^2$ as leading term, accept the naturalness sub-question OQ-1a as open".
- A *transparent record* of the trade-off (intuition vs naturalness) and the reasoning that selected C3.
- A *starting point* for the next docs: GRB constraint (`07`), $\Lambda$CDM recovery (`08`), and $\xi$ order-of-magnitude estimate (`09`) will use C3 as the working form.

## 10. Status update for the intuition catalog

This analysis does not move any of the existing 11 user intuitions in the catalog (`docs/derivations/00_intuition_catalog.md`).  It is a *new working step* in framework v2.  However, it introduces:

- **New explicit assumption** (call it T2.7, framework v2): *"the coherence functional is dominated by $|\nabla_\perp R|^2$ at leading order, justified by H1 alignment and $\Lambda$CDM auto-recovery, despite EFT naturalness disfavour."*
- **New sub-question** (OQ-1a): *"is there a symmetry that elevates $|\nabla R|^2$ to leading-order in the photon path-integral context?"*  Open.

The intuition catalog could be extended to include framework-v2 working assumptions as a separate tier, but this is left for the catalog's next revision.
