# Framework v2 — Phenomenological Path (P-α + P-γ)

**Date**: 2026-05-13
**Purpose**: Concrete starting plan that preserves the user's *photon-centric* framing while bypassing the heavy mainstream-formalism prerequisites (AdS/CFT, tensor networks).  This is the *minimal viable product* path of framework v2.

## 1. Path overview

| Stage | Description | Output |
|---|---|---|
| **P-α** | Phenomenological ansatz for $\mathcal{C}$ functional | Closed-form $c_{\text{eff}}(z, \mathbf{x})$ depending on a small number of parameters |
| **P-γ** | Observational fit of those parameters against cosmological survey data | Empirically-constrained $\mathcal{C}$ |

This combination yields a *quantitative testable claim* without requiring derivation of $\mathcal{C}$ from a fundamental quantum-gravity formalism (which is OQ-1 and may take years).

## 2. P-α — Phenomenological ansatz

### 2.1 Form-of-ansatz

A natural minimal ansatz consistent with the hypothesis H1 of `01_coherence_VSL_seed.md`:

$$\mathcal{C}[\gamma] \;=\; \exp\!\left[-\int_\gamma F(R)\,d\lambda\right]$$

where:
- $\gamma$ is the photon's null worldline from emitter to observer.
- $\lambda$ is the affine parameter along $\gamma$.
- $F(R)$ is a *scalar function of curvature invariants*, the simplest form being

$$F(R) \;=\; \xi\,\frac{R^2}{M_*^2} \quad\text{or}\quad F(R) \;=\; \xi\,\frac{R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}}{M_*^4} \quad\text{or}\quad F(R) \;=\; \xi\,\frac{|\nabla R|^2}{M_*^4}.$$

Here $\xi$ is a dimensionless coupling constant and $M_*$ is a characteristic mass scale (presumably near $M_{\text{Planck}}$).

The *inhomogeneity-sensitive* form $|\nabla R|^2$ is more aligned with H1's intuition (coherence loss only when crossing *inhomogeneity*, not when traversing homogeneous curvature).

### 2.2 Effective propagation rate

The phenomenological consequence is:

$$c_{\text{eff}}(z) \;=\; c_0 \cdot \mathcal{C}[\gamma_{\text{LOS}}(z)] \;=\; c_0 \cdot \exp\!\left[-\xi\int_0^z \frac{|\nabla R(z')|^2}{M_*^4}\,\frac{dz'}{H(z')}\right]$$

where $\gamma_{\text{LOS}}$ is the line-of-sight null geodesic and $z$ is redshift.

In FLRW background, $\nabla R = 0$ (homogeneous), so $\mathcal{C} = 1$.  Deviations arise only from *real-cosmological-perturbation-induced inhomogeneities* in $R$ along specific lines of sight (e.g., through large-scale structure overdensities/voids).

### 2.3 Two regimes

Two regimes give *distinct* observational signatures:

**Regime A — Average (sky-averaged) inhomogeneity**:
$\langle |\nabla R|^2 \rangle$ over the sky is set by the matter power spectrum.  This produces a *small, redshift-dependent* mean correction to $c_{\text{eff}}(z)$:

$$\frac{c_{\text{eff}}(z) - c_0}{c_0} \approx -\xi \int_0^z \frac{P_R(z', k)}{M_*^4}\,k^4 dk \cdot \frac{dz'}{H(z')}$$

with $P_R$ the power spectrum of curvature scalar fluctuations.

**Regime B — Directional anisotropy**:
$|\nabla R|^2$ varies across the sky.  This produces a *direction-dependent* $c_{\text{eff}}(\hat n, z)$ — correlated with weak-lensing convergence maps.

Regime B is the *more distinctive* signature.  Distance modulus to standard candles in direction $\hat n$ would deviate from the sky-averaged Hubble flow in proportion to integrated $|\nabla R|^2$ along the line of sight.

## 3. P-γ — Observational fit

### 3.1 Data sources

| Probe | What it constrains |
|---|---|
| **Type Ia supernovae (Pantheon+, DES-SN5YR, LSST)** | $d_L(z)$ vs $z$, statistical and directional |
| **CMB acoustic peaks (Planck, ACT, SPT)** | Sound horizon $r_s$ at $z\sim 1100$, *integrated* $\mathcal{C}$ across last-scattering |
| **BAO (DESI, Euclid)** | $d_A(z)$ vs $z$, multiple redshifts |
| **Weak-lensing maps (Euclid, LSST, Roman)** | $|\nabla R|^2$ along specific lines of sight, directly |
| **Strong-lensing time delays (H0LiCOW)** | $c_{\text{eff}}$ along specific lensed paths |

### 3.2 Fitting protocol

1. Adopt the ansatz of §2.1 with parameter set $\{\xi, M_*\}$.
2. Compute $c_{\text{eff}}(z, \hat n)$ from a fiducial matter distribution (e.g., $\Lambda$CDM with Planck-best-fit parameters).
3. Recompute predicted observables ($d_L, d_A, r_s$, etc.) under the modified light propagation.
4. Compare with data, derive posterior on $\{\xi, M_*\}$.

### 3.3 GRB Lorentz invariance constraint

Independent constraint: from Fermi-LAT GRB 090510 (Abdo et al. 2009), any energy-dependent deviation $\Delta c/c_0 \lesssim E/M_{\text{LIV}}$ with $M_{\text{LIV}} \gtrsim M_P$.  The ansatz §2.1 is *energy-independent* by construction (no $E$ enters), so this constraint is *automatically satisfied*.

However, the *magnitude* of $\xi/M_*^4$ must be bounded by the existence of GRB photons reaching us at all from $z \sim 1$–8.  Demanding $1 - \mathcal{C} < 1$ for typical GRB lines of sight gives

$$\xi \int_{\gamma_{\text{GRB}}} \frac{|\nabla R|^2}{M_*^4} d\lambda \;<\; 1.$$

This sets a *combined* upper bound on $\xi/M_*^4$ before any fit is performed.

### 3.4 Distinguishing from $\Lambda$CDM

The fitting protocol must show that the framework's deviations are *distinct* from $\Lambda$CDM systematics.  Two diagnostics:

(i) **Magnitude residual correlation with weak-lensing convergence**.  In $\Lambda$CDM, supernova magnitude is uncorrelated with foreground lensing of the line of sight (at first order).  In this framework, both depend on $|\nabla R|^2$ along the same line of sight — *predicting a correlation*.

(ii) **$H_0$ tension as a possible signature**.  The local-measurement vs CMB-inferred $H_0$ tension (~5σ) could *partially* be a $c_{\text{eff}}$ effect: late-time integrated $\mathcal{C}$ would bias local-distance-ladder $H_0$ downward relative to early-time CMB $H_0$.  If the framework's fit naturally produces $H_0^{\text{local}} - H_0^{\text{CMB}} \approx 6$ km/s/Mpc with the same $\{\xi, M_*\}$ that fits SNe and BAO, that is a *positive signature*.

## 4. Timeline

| Task | Estimate |
|---|---|
| Decide specific ansatz form ($R^2$ vs $|\nabla R|^2$ vs other) | 1 week |
| Write forward-model code ($c_{\text{eff}}(z, \hat n)$ given matter distribution) | 2 weeks |
| Fit to existing Pantheon+ + Planck + BAO joint chain | 3-4 weeks |
| Weak-lensing correlation test (Euclid early release) | 2 months *after* Euclid Y1 data release |
| Write hypothesis paper | 1-2 months after first fit |

**First publishable claim (success or null)**: ~2 months from start.

## 5. Stop conditions (M7 enforced)

The phenomenological path collapses if any of the following:

1. **GRB constraint** rules out *all* values of $\xi$ that could produce *any* observable effect.  (Unlikely given energy-independence, but possible if $M_*$ must be $\gg M_P$.)
2. **No fit improvement over $\Lambda$CDM**: if joint $\chi^2$ with $\{\xi, M_*\}$ as free parameters is not significantly better than fixing $\xi = 0$, the framework adds no value.
3. **Weak-lensing correlation null**: if the predicted correlation in §3.4(i) is *not observed* at the precision Euclid will deliver, the framework is falsified.

Any of these → archive framework v2 alongside CNSC.

## 6. What the user does NOT need to learn for this path

(Important — minimizes barrier to entry):

- AdS/CFT formalism
- Tensor networks / MERA
- Causal set theory
- Detailed quantum gravity literature

**What the user does need**:

- Cosmological survey data formats (Pantheon+, Planck CMB likelihoods)
- Basic MCMC (e.g., emcee or cobaya)
- Forward modeling of $d_L(z)$, $d_A(z)$, $r_s$ in modified-light-propagation cosmology
- Weak-lensing convergence map basics

This is *standard cosmological-data-analysis skill set*.  Achievable in 2-4 weeks of focused learning if not already familiar.

## 7. Honest expectation

This path *does not derive* the user's H1 from first principles.  It *tests it phenomenologically*.  If it succeeds, it produces a *publishable phenomenological cosmology hypothesis* analogous to early proposals of dark energy parameterizations (CPL, etc.) — papers that did not derive the parametrization from a deeper theory but constrained it empirically.

Subsequent work would then *attempt to derive* the surviving phenomenological form from a deeper theory (Path β or other) — but only *after* the phenomenology is established.

This is the *inverse* of the CNSC approach (CNSC: derive first, validate against data later — but derivation failed).  Phenomenological-first is the conventional path for novel cosmology hypotheses.
