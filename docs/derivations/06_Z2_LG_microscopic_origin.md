# Derivation 6 — Microscopic Origin of Z₂ Landau-Ginzburg Criticality

**Date**: 2026-05-13
**Purpose**: Test whether the cosmological phase transition assumed in T2.3 (Z₂-symmetric Landau-Ginzburg, *tuned* to criticality) has a microscopic origin, or whether it reintroduces the fine-tuning problem of inflation.

## 1. The fine-tuning question

Critical phenomena arise *only* when the system sits at the critical point of a phase transition — i.e., when the *reduced temperature* $r = (T - T_c)/T_c$ is exactly zero (or within a small window scaled by correlation length).

In condensed matter, this tuning is achieved by *external manipulation* (lab experimenter adjusts $T$).  In cosmology, $T$ decreases monotonically with expansion, so $T = T_c$ is crossed *briefly* (at most for one Hubble time $\Delta t \sim 1/H$).

The question: does the universe spend *enough time near criticality* for critical universality to be realized?  And if not, what does the imprint look like?

## 2. Time at criticality

The correlation length at criticality diverges as $\xi \sim |r|^{-\nu}$ with $\nu \approx 0.63$ for 3D Ising.  For the spectrum to inherit the critical 2-point function, $\xi$ must exceed the Hubble length $1/H$:

$$\xi > 1/H \;\Leftrightarrow\; |r| < H^{1/\nu} \cdot \xi_0^{1/\nu}$$

For typical cosmological scales $H \sim 10^{-10}\,M_P$ and microphysical $\xi_0 \sim 1/M_{\text{GUT}}$, this gives $|r| < 10^{-15}$.

The universe crosses $T = T_c$ in time $\Delta t \sim 1/H$, and during that time $r$ ranges over $\sim 1$ (from $+\infty$ to $-\infty$ schematically — actually from $r_+ > 0$ to $r_- < 0$ over $\Delta t$, with $|r| \sim 1$ at the boundary).  The fraction of time during which $|r| < 10^{-15}$ is essentially zero.

**Verdict on naive scaling**: the universe is at criticality for an *infinitesimal* fraction of its evolution, far too short for critical universality to be realized.

## 3. Kibble-Zurek mechanism — actually relevant

The standard analysis of "phase transitions in cosmology" is the **Kibble-Zurek mechanism**:

(i) At $T \gg T_c$, $\theta$ is in the symmetric phase ($\langle\theta\rangle = 0$).
(ii) At $T \to T_c$, the relaxation time $\tau_\theta \sim |r|^{-\nu z}$ diverges (critical slowing).
(iii) At some point $r_f$ before reaching $T_c$, the relaxation time exceeds the available time ($\tau_\theta = $ Hubble time), and $\theta$ "freezes out" of equilibrium.
(iv) The *frozen-in* correlation length is $\xi_{\text{frozen}} \sim (\tau_{\text{Hubble}})^{\nu/(\nu z)} \sim H^{-1/z}$.
(v) Below $T_c$, the field rapidly relaxes to the broken-symmetry vacuum, with *topological defects* (cosmic strings/domain walls) at scale $\xi_{\text{frozen}}$.

The output of Kibble-Zurek is **defects**, with a characteristic *density* determined by $\xi_{\text{frozen}}$.  These are observationally well-studied:
- Domain walls (Z$_2$ symmetry): catastrophic for cosmology unless symmetry-broken by another mechanism.
- Cosmic strings (U(1) symmetry): tightly constrained but not excluded.
- Monopoles, textures (higher symmetry): various constraints.

**A Z$_2$ Landau-Ginzburg cosmological transition produces domain walls.**  If they survive to the present, their energy density grows as $\rho_{\text{wall}} \propto a^{-1}$, dominating the universe at late times — already excluded by observation.

CNSC must therefore include a mechanism to *erase* the domain walls (e.g., explicit symmetry breaking that biases one vacuum, or a subsequent inflation), which the paper does not address.

## 4. The deeper problem: who tunes $T_c$?

In Landau theory, $r = (T - T_c)/T_c$ is *defined* — there is no derivation of $T_c$ from first principles.  In condensed matter, $T_c$ is *measured*.  In cosmology, $T_c$ must come from *microphysics*: a coupling of $\theta$ to other fields whose vacuum energy or thermal state sets $T_c$.

The CNSC paper sets $T_c \sim 10^{15}\,\text{GeV}$, close to GUT scale.  This is *plausible* but not *derived* — it is matched to obtain the right observational scales.

**The fine-tuning question reduces to**: why is $T_c \sim T_{\text{GUT}}$ rather than, say, $T_c \sim T_{\text{EW}}$ or $T_c \sim M_{\text{Planck}}$?  No microscopic answer in the paper.

## 5. Is there *any* phase transition in standard cosmology with Ising critical scaling?

Empirically:
- Electroweak transition: weakly first-order in the Standard Model, possibly second-order in extensions — *no* Ising criticality.
- QCD transition: smooth crossover at the physical quark masses (lattice QCD result) — *no* Ising criticality.
- GUT-scale transition (hypothetical): depends on the specific GUT; no observational evidence and no theoretical prediction of Ising universality.

**No known cosmological phase transition is Ising-universal.**  The CNSC assumption is *constructed* to obtain $\eta_{3D\text{Ising}} \to n_s$, not derived from a microphysical model.

## 6. Verdict

| Intuition | Status |
|---|---|
| I-4 (cosmological phase transition occurred) | 🟡 **Partial** — generic phase transitions are well-established, but their *specific properties* (order, universality class) require microphysical input |
| I-5 (specifically Z$_2$ 3D Ising universality) | ❌ **Not defensible** — no microphysical model in the paper produces this universality; Kibble-Zurek produces *defects*, not the $n_s = 1-\eta$ spectrum; $T_c$ is fine-tuned without justification |

## 7. Cascade

This negative result strengthens the cascade from weakness 2:
- Even if the Mukhanov-Sasaki analogue had worked, the *origin* of the Ising universality class would still be unmotivated.
- Combined with weakness 2, this means: **no derivable path from cosmological microphysics to $n_s = 1-\eta$**.

The numerical match $\eta_{\text{Ising}} = 0.036298 \to n_s = 0.9637$ remains striking, but it is *coincidence* (or — more politely — *suggestive without derivation*).

## 8. Closure

The Z$_2$ Landau-Ginzburg coarse-graining assumed in T2.3 is **not derived** from any microphysical model.  Combined with the *absence* of a freeze-in mechanism (weakness 2), it cannot produce the asserted $n_s = 1-\eta$ as a cosmological prediction.

Intuitions I-4 and I-5 of the catalog: I-4 stays partial (phase transitions occur), I-5 collapses (specific universality class is unjustified).
