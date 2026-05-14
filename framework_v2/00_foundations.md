# Framework v2 — Foundations: What Survives Mathematically

**Date**: 2026-05-13

The 7-weakness derivation program of `../docs/derivations/` reduced the user's original 11 intuitions to the following 4 *defensible* core (2 fully, 2 partial).

## F1 (from I-1) — SR null kinematics

Photons move along null geodesics, and their proper time vanishes along the worldline:

$$d\tau^2 = -dx^\mu dx_\mu = 0 \quad\text{along a null geodesic in any Lorentzian manifold.}$$

This is a trivial consequence of the Minkowski / Lorentzian metric structure.  **Status: fully defensible (textbook SR/GR).**

What it does *not* say:
- It does *not* say all spacetime points are null-connected.
- It does *not* define a "photon's rest frame" — that limit is mathematically singular.
- The intuition *"the universe is a single point from the photon's perspective"* is metaphorical, not derivable.

## F2 (from I-10) — Stiff-matter cosmology resolves the horizon problem

A cosmological epoch with equation of state $w = +1$ (stiff matter, $\rho \propto a^{-6}$) has the property that the comoving Hubble radius

$$r_H \equiv \frac{1}{aH} \propto a^{(1+3w)/2} = a^2 \quad\text{(growing)}.$$

For a sufficiently long stiff-matter epoch *before* radiation domination, all observed CMB modes were inside the comoving Hubble radius at sufficiently early times, resolving the horizon problem *without inflation*.

This is **fully defensible** within standard cosmological perturbation theory.  Note that it does *not require* CNSC's specific framework — any source of $w \geq +1$ at sufficiently early times works (e.g., kinetic-energy-dominated scalar field, free massless field, etc.).

What it does *not* say:
- It does *not* by itself produce the observed scalar perturbation spectrum (cf. F5 below).
- It does *not* explain the *origin* of the stiff-matter epoch.

## F3 (from I-3, partial) — Hypersurface-orthogonal null vector fields are well-posed

A null vector field $\ell^\mu$ that is *hypersurface-orthogonal* (i.e., $\ell_\mu = f(x)\,\partial_\mu S$ for scalars $f, S$, equivalently $\omega_{\mu\nu} = \nabla_{[\mu}\ell_{\nu]} = 0$) reduces to the **eikonal field** of $S$, satisfying

$$g^{\mu\nu}\,\partial_\mu S\,\partial_\nu S = 0.$$

This is a first-order non-linear PDE, well-posed as a Cauchy problem.  *Standard PDE theory*.

What it does *not* say:
- It does *not* say generic null vector fields are well-posed — twisting null fields ($\omega_{\mu\nu}\neq 0$) require additional structure.
- The choice to restrict to hypersurface-orthogonal $\ell^\mu$ is an *assumption*, not a derivation.

**Status: partial — defensible under explicit restriction, no further.**

## F4 (from I-4, partial) — Cosmological phase transitions occur

Standard particle physics + cosmology predict the universe undergoes phase transitions during its thermal history (electroweak, QCD, possible GUT-scale).  *Phase transitions exist as physical events*.

What it does *not* say:
- It does *not* identify the *specific universality class* of any given transition (Ising, mean-field, first-order with latent heat, smooth crossover, etc.).
- It does *not* explain why the universe would be *tuned to criticality* at any particular moment.
- 3D Ising universality for cosmological transitions is *not* observationally or theoretically supported in any specific transition.

**Status: partial — generic phase transitions are defensible, but *Ising critical phenomena* are not.**

## What is *not* in the foundations

The following 7 intuitions from the original CNSC framework are **not defensible** and therefore are *excluded* from the foundations of framework v2:

- I-2 *Null-connected initial geometry as a cosmological state* — metaphorical extension of F1; no mathematical support.
- I-5 *Z₂ 3D Ising universality of the cosmological transition* — no microphysical model; produces defects via Kibble-Zurek, not the assumed spectrum.
- I-6 *Model A relaxation produces freeze-in of $\zeta$* — false; no freeze-in mechanism in $w=+1$.
- I-7 *DBI saturation produces $\gamma(k) = \sqrt{1+(k/k_*)^4}$* — derive-failed.
- I-8 *Horizon-crossing inheritance of static critical 2-point function* — no such mechanism in stiff matter.
- I-9 *Null geometry uniquely sources quadrupolar $f_{NL}^{(2)}$* — cascade-fail.
- I-11 *Shear coupling produces small but nonzero observable $r$* — cascade-fail (no well-defined $P_\zeta$ to take ratio with).

These are *not* part of framework v2.  Any attempt to use them would re-enter the CNSC trap.

## Implications for framework v2

The 4 foundations above are *all* standard physics.  Therefore, *to be a non-trivial new framework*, framework v2 must introduce **new content** beyond the foundations.  That new content is the user's *path-integral coherence VSL* insight (next document, `01_coherence_VSL_seed.md`).

The 4 foundations supply the *cosmological substrate* (stiff-matter era, eikonal null field, phase transitions); the new content supplies the *novel physical hypothesis* (coherence-delay-induced effective propagation rate).

Whether the combination yields anything *publishable* is *open*.  The CNSC inquiry taught us that *publishable* requires *derivable*, not just *suggestive*.

## Note on the *combination*

While F1-F4 individually are *all standard*, the **simultaneous use of all four** as the substrate of a cosmological framework is *not standard*.  Most non-inflationary alternatives pick one (bouncing, ekpyrotic, cyclic, pure stiff matter).  The user's choice to combine all four is itself a structural decision that survives from CNSC — see `04_user_specific_core.md` Core B.  This composite substrate is *defensible* (no contradictions among F1-F4) but *unusual*, and is the user's *organizational contribution* even though no individual element is novel.
