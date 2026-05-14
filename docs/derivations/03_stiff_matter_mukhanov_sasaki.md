# Derivation 3 — Stiff-Matter Mukhanov-Sasaki Analogue

**Date**: 2026-05-13
**Purpose**: Test whether a *freeze-in mechanism* analogous to the inflationary Mukhanov-Sasaki freeze-out exists in the stiff-matter ($w=+1$) era of CNSC.  The paper's spectral index claim $n_s = 1 - \eta$ (T3.3) requires that the static critical 2-point function of $\theta$ be *imprinted* on the comoving curvature perturbation $\zeta$ at some moment.  In inflation this happens at horizon exit ($k = aH$).  In CNSC the comoving horizon $r_H = 1/(aH) \propto a^2$ is *growing*, so modes *enter* the horizon — the inflationary mechanism does not apply.

The honest question: **Is there any moment in the CNSC stiff-matter era at which $\zeta_k$ becomes constant (freezes), inheriting the critical correlator pattern?**

## 1. Setup: comoving curvature perturbation

The comoving curvature perturbation in flat-slice gauge is

$$\zeta = \Psi + H\,\frac{\delta\rho}{\dot{\bar\rho}}.$$

In our gauge $\Psi = 0$, so

$$\zeta = H\,\frac{\delta\rho_{\text{total}}}{\dot{\bar\rho}_{\text{total}}} = -\frac{1}{3(1+w)}\,\frac{\delta\rho}{\bar\rho},$$

using $\dot{\bar\rho} = -3H(1+w)\bar\rho$.

For $w = +1$ (stiff matter):

$$\zeta = -\frac{1}{6}\,\frac{\delta\rho}{\bar\rho}.$$

The cosmological observable is the *constant* (super-Hubble) value of $\zeta$ at the moment of imprinting.

## 2. Background dynamics for $w = +1$

In stiff matter era:

$$a(t) \propto t^{1/3}, \qquad H = \dot a/a = \frac{1}{3t}, \qquad aH = \frac{1}{3t}\cdot t^{1/3} \cdot \text{const} \propto t^{-2/3}.$$

Comoving Hubble radius:

$$r_H \equiv \frac{1}{aH} \propto t^{2/3} \propto a^2.$$

So $r_H$ *grows* with time.  A mode with comoving wavenumber $k$ has $k\cdot r_H = k/(aH)$, which *grows* with time.  At early times $k/(aH) \ll 1$ (mode is *outside* horizon); at late times $k/(aH) \gg 1$ (mode is *inside* horizon).

This is the *opposite* of inflation:
- **Inflation**: modes start inside horizon ($k > aH$), exit horizon when $k = aH$, freeze on super-Hubble scales.
- **Stiff matter**: modes start outside horizon ($k < aH$), enter horizon when $k = aH$, oscillate on sub-Hubble scales.

The "freezing" mechanism that gives inflation its scale-invariant power spectrum **does not have a stiff-matter analogue at the level of free-field perturbations**.

## 3. Mode equation for $\zeta$ in $w=+1$

The Mukhanov-Sasaki equation (in conformal time $\tau$):

$$v_k'' + \left(c_s^2 k^2 - \frac{z''}{z}\right) v_k = 0, \qquad v = z\zeta, \qquad z = a\sqrt{2\epsilon}/c_s.$$

For stiff matter $\epsilon = -\dot H/H^2 = 3$ (constant).  With $c_s$ constant (Derivation 1 result):

$$z \propto a, \qquad z''/z = a''/a.$$

In conformal time for $w = +1$: $a \propto \tau$ (since $a\propto t^{1/3}$ and $d\tau = dt/a$ gives $\tau \propto t^{2/3}$, so $a \propto \tau^{1/2}$).  Let me redo: $d\tau = dt/a$, so $\tau = \int dt/a \propto \int t^{-1/3}dt = (3/2)t^{2/3}$, so $\tau \propto t^{2/3}$ and $a \propto t^{1/3} \propto \tau^{1/2}$.

Then $a' = \frac{1}{2}\tau^{-1/2}\propto 1/\sqrt\tau$, $a'' = -\frac{1}{4}\tau^{-3/2}\propto -1/\tau^{3/2}$.

$$\frac{a''}{a} = -\frac{1}{4\tau^2}.$$

The mode equation becomes:

$$v_k'' + \left(c_s^2 k^2 + \frac{1}{4\tau^2}\right) v_k = 0.$$

**Critical observation**: the effective "mass" $z''/z$ is *negative* (=$-1/(4\tau^2)$ has the same sign as $-k^2$ would give for a normal oscillator).  At very early times ($\tau \to 0^+$), the $1/\tau^2$ term dominates and the equation becomes

$$v_k'' + \frac{1}{4\tau^2} v_k = 0,$$

with solutions $v_k = c_1 \tau^{1/2 + i 0} + c_2 \tau^{1/2 - i 0}$ — but this is the degenerate case at the boundary of oscillatory and power-law behaviour.  More carefully, the equation $v_k'' + (1/(4\tau^2))v_k = 0$ has solutions $v_k \propto \tau^{1/2}, \tau^{1/2}\ln\tau$.

At very late times ($\tau \to \infty$), the $k^2$ term dominates: $v_k'' + c_s^2 k^2 v_k = 0$ → oscillatory.

## 4. The fundamental problem

In inflation, $z''/z = 2/\tau^2$ (positive), and modes transition from oscillatory (sub-Hubble, $k > 1/|\tau|$) to *frozen* (super-Hubble, $k < 1/|\tau|$) — the freezing happens because $z''/z$ dominates over $k^2$ and the mode equation becomes $v_k'' = (z''/z) v_k$, which has growing/decaying solutions; the growing solution gives the frozen $\zeta_k = v_k/z = $ const.

In stiff matter, $z''/z = -1/(4\tau^2)$ — *negative and smaller in magnitude*.  This term is *always sub-dominant* compared to $c_s^2 k^2$ for any reasonable $\tau$.  The mode equation is *always oscillatory*, never freezing.

**Verdict at free-field level**: **there is no mode-freezing mechanism for $\zeta$ in stiff matter**.  Every mode keeps oscillating; no mode acquires a constant super-Hubble value to inherit as a primordial perturbation.

This is the well-known "stiff matter does not source super-Hubble perturbations" result from cosmological perturbation theory.

## 5. The CNSC-specific freeze-in attempt

The paper's T2.5 conjectures that *something* about the critical phase transition acts as an *external source* that imprints the static critical correlator on $\zeta$ at some moment.  The candidate mechanism is:

(i) Before the transition, $\theta$ fluctuations follow the static 3D Ising critical correlator $\langle\theta(\mathbf{x})\theta(\mathbf{0})\rangle \sim |\mathbf{x}|^{-(1+\eta)}$.

(ii) At the moment of the phase transition (some specific $\tau_c$), $\theta$ "freezes" into a classical configuration whose statistical properties are the static critical 2-point function.

(iii) That classical $\theta$ then sources the metric perturbation $\zeta$ via Einstein's equations.

The conjectured "freeze-in scale" of the Mukhanov-Sasaki analogue, suggested earlier in `CNSC_Axiom_Derivation_Map.md` §L.6, was $k = a\sqrt{H\,\Gamma_\theta}$ where $\Gamma_\theta$ is the Model A relaxation rate.  Let me test whether this scale is the *correct* freeze-in scale.

### 5.1 Model A relaxation rate

For Hohenberg-Halperin Model A:

$$\partial_t\theta = -\Gamma_\theta\,\frac{\delta F}{\delta\theta},\qquad \Gamma_\theta \sim \frac{1}{H^{-1}} = H \quad\text{(Hubble friction)}.$$

So $\Gamma_\theta \sim H$.  The conjectured freeze-in scale becomes

$$k_{\text{freeze}} = a\sqrt{H \cdot H} = aH.$$

But $aH$ is *exactly the Hubble horizon scale*!  The conjectured freeze-in scale coincides with the Hubble horizon.  In stiff matter, $aH$ is *decreasing* in time, so modes go from $k > aH$ (sub-Hubble, oscillating) to $k < aH$ (super-Hubble, ...?) — but the previous section showed that no freezing happens on super-Hubble scales.

This means the conjectured T2.5 mechanism *coincides with Hubble horizon crossing* but **does not produce freezing**: modes on super-Hubble scales in stiff matter continue to evolve, not freeze.

### 5.2 Alternative freeze-in: at the phase transition itself

Perhaps the freeze-in is instantaneous at $\tau = \tau_c$ (the moment of the phase transition), driven by the *non-linearity* of the Landau-Ginzburg potential.

At $\tau_c$, $\theta$ undergoes symmetry breaking from $\bar\theta = 0$ to $\bar\theta \neq 0$ (the ordered phase).  The fluctuations $\delta\theta$ at this moment carry the critical correlator pattern.  If the post-transition expansion *redshift-freezes* these fluctuations (analogous to topological defects in Kibble mechanism), then the critical pattern *can* be imprinted.

However, this is a *Kibble-Zurek* mechanism, not a Mukhanov-Sasaki freeze.  And Kibble-Zurek produces **topological defects** (cosmic strings, domain walls), not Gaussian curvature perturbations with the static 2-point function.

**Honest verdict on T2.5**: the imprinting mechanism conjectured in the paper does *not* exist at the level of standard cosmological perturbation theory.  The closest analogue is Kibble-Zurek defect production, but that produces *defects*, not the curvature perturbation pattern $\zeta(k)$ with the spectral index $n_s = 1-\eta$.

## 6. Cascade to T3.3 ($n_s = 1 - \eta$)

If T2.5 fails, then the chain

> static critical 2-point function $\langle\theta(\mathbf x)\theta(\mathbf 0)\rangle \sim |\mathbf x|^{-(1+\eta)}$
> → Fourier transform $\mathcal{P}_\theta(k) \propto k^{1+\eta}$
> → inheritance by $\zeta$
> → $\mathcal{P}_\zeta(k) \propto k^{n_s - 1}$ with $n_s = 1 - \eta$

is broken at the *inheritance* step.  The first three lines are mathematics; the fourth requires a freeze-in mechanism.

**The paper's central claim $n_s = 0.9637$ is therefore *not derived* either** — it has the same status as the $\gamma(k)$ envelope of weakness 1: a numerical match without a derivation.

## 7. What survives, what doesn't

| Component of paper's $n_s = 1 - \eta$ argument | Status |
|---|---|
| Z$_2$ symmetry of $\theta$ (T3.1) | ✅ Defensible (one-line, from $\theta$ scalar nature) |
| 3D Ising critical exponent $\eta = 0.036298$ (T1.2) | ✅ Defensible (external math result) |
| Static real-space 2-point function scaling | ✅ Defensible (textbook critical phenomena) |
| Fourier → $k^{1+\eta}$ in momentum space | ✅ Defensible (Fourier convention) |
| **Inheritance by $\zeta$ at "horizon crossing" (T2.5)** | ❌ **Not defensible — no mechanism in stiff matter** |
| $n_s = 1 - \eta = 0.9637$ matching Planck | ❌ **Numerical coincidence, not derived** |

## 8. Are there other freeze-in mechanisms?

Three possibilities for rescue:

(a) **Quantum vacuum freeze-out during a brief de Sitter phase** *before* the stiff matter era.  But then CNSC reduces to (variant of) inflation — defeats the non-inflationary claim.

(b) **Thermal fluctuations at the critical point** with subsequent classical evolution.  But thermal fluctuations have $\mathcal{P}_\theta \sim T \delta(\mathbf x)$ (white noise) until critical phenomena modify them.  The critical *correlations* require the system to be *near criticality for a long time*, which in stiff matter $\Gamma_\theta \sim H$ would require an arbitrarily prolonged near-critical epoch.

(c) **Out-of-equilibrium dynamics at the transition with Kibble-Zurek**.  Produces defects, *not* the curvature spectrum.

None of these recovers $n_s = 1 - \eta$ as a derived spectral tilt.

## 9. Update to intuition catalog

Cascade to `00_intuition_catalog.md` §2:

- **I-6** (Model A dynamics): 🟡 Partial → ❌ Not defensible *for the specific role T2.5 plays*. Model A classification of $\theta$ is fine, but it does not yield a freeze-in mechanism for $\zeta$.
- **I-8** (Horizon-crossing inheritance): ⏸ Pending → ❌ **Not defensible**.  No mechanism exists.
- **Cascade**: $n_s = 1 - \eta$ is *not derived* from the assumption set; it is a *numerical match* that happens to fit Planck within 0.29σ.

## 10. Honest verdict on weakness 2

**The stiff-matter Mukhanov-Sasaki analogue does not exist.**

The paper's chain from "3D Ising critical phenomena" to "$n_s = 0.9637$" is broken at the inheritance step.  $n_s = 0.9637$ remains a *numerical coincidence* that motivates the CNSC framework, but it cannot be derived from the assumption set.

Combined with weakness 1's negative result, this means:

**No quantitative prediction of the paper survives as derivable from the explicit assumption set.**

This is the *full* picture the user asked about: their intuitions I-7, I-8, I-9 are *not* mathematically defensible.  The intuitions I-1 through I-5 may still survive, but they yield no quantitative cosmological predictions on their own.

## 11. Cascade to remaining weaknesses

- **Weakness 3** ($r$ formula): depends on T2.5 implicitly (the *imprinting* of perturbations).  Likely cascades to negative.
- **Weakness 4** ($S_{\text{crit}}$): already moot from weakness 1.
- **Weaknesses 5, 6, 7** (foundational): orthogonal to weaknesses 1-3; can still be tested.

The remaining derivations will determine whether intuitions I-1, I-2, I-3, I-4, I-5, I-10 survive *qualitatively*, even if the *quantitative* predictions don't.
