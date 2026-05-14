# Framework v2 — Path-Integral Coherence VSL: The Novel Seed

**Date**: 2026-05-13
**Status**: Hypothesis stage.  No derivation yet.

This document formalizes the user's *path-integral coherence VSL* insight as the starting point for the novel content of framework v2.  The insight was developed by the user during the CNSC inquiry but is *independent* of CNSC's failed components.

The full background and connection to mainstream physics is in `../memory/project_open_avenue_coherence_delay_vsl.md` (project memory).

## H1 — The core hypothesis

**Statement**: The effective propagation rate of a photon between two cosmologically separated regions can deviate from the *local* invariant speed $c_0$ if the photon's path integral traverses regions of *inhomogeneous spacetime curvature*, due to *partial decoherence of the path-integral amplitudes*.

Formally — *to be derived*:

$$c_{\text{eff}}(x, x') \;=\; c_0 \cdot \mathcal{C}\!\left[\,R_{\mu\nu\rho\sigma}; \, \gamma(x, x')\,\right]$$

where:
- $c_0$ is the *fundamental* local speed of light, Lorentz-invariant in any local inertial frame (F1 of foundations).
- $\mathcal{C}$ is a *coherence functional* of the Riemann curvature along (and around) the path $\gamma(x, x')$.
- $\mathcal{C} \to 1$ when the path traverses homogeneous curvature (flat or maximally symmetric).
- $\mathcal{C} < 1$ when the path traverses *inhomogeneous* curvature, due to phase-decoherence of contributing paths in the path integral.

## H2 — Why this is *not* fundamental Variable Speed of Light

Standard VSL theories (Albrecht-Magueijo, Moffat, etc.) propose that the *fundamental* $c$ varies in spacetime, breaking Lorentz invariance.  These theories are tightly constrained by:
- GRB observations of multi-wavelength simultaneity (Fermi-LAT GRB 090510: LIV scale $\gtrsim M_P$).
- CMB blackbody compatibility.
- Direct fine-structure constant constraints.

The coherence-VSL hypothesis **preserves Lorentz invariance** at the local level — $c_0$ is invariant in every local inertial frame.  The observable effect is a *global* coordinate-frame deviation arising from *quantum coherence* loss in the path integral, akin to:
- Shapiro delay (classical GR analogue, well-established).
- Quantum decoherence in curved spacetime (Hu-Verdaguer stochastic gravity, established).
- Gravitational time dilation accumulated over cosmological distances.

It is the *cosmological accumulation* of these established effects that produces the apparent VSL.  Therefore the GRB constraints **do not directly apply** if the coherence functional $\mathcal{C}$ is *energy-independent* (which it should be, since photon energy enters $c_0$ universally).

## H3 — Mainstream connections

The hypothesis is compatible with — and possibly derivable from — the following mainstream research programs:

| Connection | Reference |
|---|---|
| AdS/CFT and emergent spacetime | Maldacena 1998; Van Raamsdonk 2010 (*"Building up spacetime with quantum entanglement"*) |
| ER=EPR | Maldacena-Susskind 2013 |
| Information bound on propagation | Lieb-Robinson 1972 |
| Stochastic gravity (decoherence in curved spacetime) | Hu-Verdaguer 2008 (*Living Rev. Relativ.* 11, 3) |
| Emergent gravity from entanglement | Verlinde 2017 |
| Computational universe | Lloyd 2002 (Phys. Rev. Lett.) |
| Tensor networks → AdS | Swingle 2012 |

The conceptual claim *"photons traverse a coherent path-integral lattice that loses coherence over inhomogeneity"* sits naturally within this corpus.

## H4 — Open derivation questions

To convert H1 from hypothesis to derivation, three questions must be answered:

### Q1. What is the explicit form of $\mathcal{C}$?

Candidates from mainstream physics:
- **Berry phase** of the photon's geometric phase accumulated along the path: $\mathcal{C} = e^{i\oint A_\mu dx^\mu}$ where $A_\mu$ is a connection on the photon's polarization bundle.  Affects *polarization* rather than *amplitude*; needs modification.
- **Decoherence functional** (Hartle-Gell-Mann consistent histories): natural for amplitude loss, but technically heavy.
- **Entanglement entropy across curvature patches**: most mainstream-aligned, requires bipartite spatial decomposition.

Open: which is the correct form?  Or is a different formalism needed?

### Q2. Quantitative scale of the effect

GRB constraints place LIV at the Planck scale.  Therefore $\mathcal{C}$ must satisfy:

$$1 - \mathcal{C} \;\lesssim\; (E_\gamma / M_P)^n \quad\text{for some } n \geq 1,$$

*and* must be *energy-independent* in the leading approximation.  This is a non-trivial constraint on the form of $\mathcal{C}$.

Open: derive the leading energy scaling from the chosen formalism, verify GRB compatibility.

### Q3. Cosmological observable consequences

If H1 holds, what observable would distinguish it from $\mathcal{C} = 1$?  Candidates:

- *Apparent* magnitude–redshift relation deviations at very high $z$ (where curvature inhomogeneity was large).
- Anomalous *anisotropy* in CMB photon paths through specific large-scale structure (correlate with weak-lensing maps).
- Stochastic gravitational-wave background features from inhomogeneity decoherence in early universe.
- Possible connection to CMB hemispherical-power asymmetry (existing $\sim 3\sigma$ Planck anomaly).

Open: identify a *clean* observable that decouples coherence-VSL from other systematic effects.

## H5 — What this framework does NOT claim (yet)

To avoid falling into the CNSC trap of asserting predictions before deriving them:

- No specific $n_s$ value (the spectral index claim of CNSC was a numerical coincidence).
- No specific $r$ range (CNSC's $r$-window depended on CNSC ansätze that are no longer in use).
- No specific $f_{NL}$ shape.
- No specific cosmological scenario (whether the universe had a stiff-matter epoch, an inflationary epoch, or both, is not decided by H1).

The framework v2 *seed* is just H1 plus the 4 foundations.  Everything else must be *derived* before being claimed.

## H6 — Honest status

This document is a **starting point**, not a theory.  H1 is the *user's insight*, sharpened with mainstream-physics language; it has *not* been derived from first principles.

The mainstream connections (H3) suggest H1 *could* be derived from existing formalisms.  The open questions (H4) are the work needed.  If all three are answered convincingly, framework v2 becomes a *publishable* alternative.  If any of them resists derivation, framework v2 collapses — and that is acceptable, in the same spirit as the CNSC inquiry.

The CNSC experience teaches: **start from what is derivable, not from what is suggestive.**

## H7 — Why the *operational framing* is the user's contribution

The hypothesis H1, viewed as a mathematical object, has many overlapping antecedents in mainstream physics (H3 table).  *The user's contribution is the operational framing*: that the *photon traversing inhomogeneous curvature* is the natural probe, and that the *effective propagation rate* is the natural observable.  This *photon-centric perspective* is distinct from the *bulk-CFT* viewpoint of AdS/CFT, the *local-decoherence* viewpoint of stochastic gravity, and the *spacetime-as-computer* viewpoint of Lloyd.

See `04_user_specific_core.md` Core A for the precise statement of this distinction.

Practically: the user can proceed by *parameterizing $\mathcal{C}$ phenomenologically* (see `05_phenomenological_path.md`) without first solving OQ-1 from a fundamental quantum-gravity formalism.  This *bypasses* the most uncertain part of the program while preserving the user's framing.
