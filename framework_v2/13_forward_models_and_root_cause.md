# 13 — Forward Models, Constraint Application, and Root-Cause Tracking

**Date**: 2026-05-14
**Purpose**: Make explicit, for each framework whose parameters enter the grid search of `12_physical_origins.md`, *how* observational constraints are computed from the parameters.  Without this, grid search constraints like *"$A_s$ match Planck"* are ambiguous in non-inflationary frameworks.

This document also defines the **root-cause tracking** methodology — when the grid search returns a fine-tuned region (most likely outcome per `11_naturalness_meta_observation.md`), *which* parameter is *responsible* for the fine-tuning, and *why*.

**Scope** (per user direction Q2, 2026-05-14): CNSC and framework v2 only.  Inflation / ekpyrotic / cyclic / pre-Big Bang appear only as *reference context* in `12_physical_origins.md §4` and are *not* included in the active grid search.

**Framing reminder** (O2 follow-up): CNSC parameters appear here for *retrospective* analysis.  The framework is archived; grid search asks *where could it have lived* not *should we revive it*.

---

## 1. The forward-model question, sharply stated

The standard cosmological observable set is:

- $A_s$ — scalar perturbation amplitude
- $n_s$ — scalar spectral tilt
- $r$ — tensor-to-scalar ratio
- $\alpha_s = dn_s/d\ln k$ — running of the tilt
- $f_{NL}$ — primordial non-Gaussianity amplitude (various shapes)
- $r_s$ — sound horizon at recombination
- $d_L(z), d_A(z)$ — luminosity / angular-diameter distances
- $H_0$ — present-day Hubble parameter

These are *defined* operationally (CMB power spectrum, SN Ia magnitudes, BAO scale, etc.).  But their *theoretical prediction* depends on a *model-specific forward map* from parameters to predictions.  Different frameworks compute the same $A_s$ via *different mechanisms*.

For the grid search to apply *"$A_s$ matches Planck"* consistently, each framework needs an explicit forward map.

## 2. Forward model — Inflation (reference; for orientation)

This is the *baseline* that other frameworks deviate from.  Inflation's forward map:

$$A_s = \frac{1}{8\pi^2 \epsilon_V c_s}\frac{H_*^2}{M_P^2}, \qquad n_s = 1 - 6\epsilon_V + 2\eta_V, \qquad r = 16 \epsilon_V c_s$$

Inputs: $H_*$, $\epsilon_V$, $\eta_V$, $c_s$.  Outputs: all of $A_s, n_s, r$ at the pivot scale $k_*$.

This is the *standard reference* — the relation between *physical parameters* and *cosmological observables* is *derived* from the Mukhanov-Sasaki equation applied to inflaton fluctuations at horizon exit during de Sitter expansion.

## 3. Forward model — CNSC (archived)

CNSC is non-inflationary.  $w = +1$ stiff matter background.  Horizon *enters* rather than exits.  Therefore:

### 3.1 $A_s$ in CNSC — *broken*

The inflationary formula above assumes Mukhanov-Sasaki freeze-out at horizon exit.  CNSC has *no horizon exit* and *no Mukhanov-Sasaki analogue* (per `docs/derivations/03_stiff_matter_mukhanov_sasaki.md`).  

Therefore $A_s$ in CNSC is **not derivable from the framework's parameters**.  CNSC's strategy was to *match* $A_s$ to the Planck value by adjusting $\Phi_0$ (see `12_physical_origins.md §2.3`): $\Phi_0 \approx \sqrt{A_s}$.  This is *not derivation*; it is *parameter-fitting*.

**Grid-search implication**: the constraint *"$A_s$ matches Planck"* in CNSC translates to *"$\Phi_0^2 \approx A_s$"* — i.e., it *fixes* $\Phi_0$ uniquely.  $\Phi_0$ has *no independent freedom* in the grid search; its value is dictated by $A_s$ alone.

### 3.2 $n_s$ in CNSC — *also broken*

The CNSC claim $n_s = 1 - \eta_{\text{Ising}}$ was found mathematically non-derivable (`docs/derivations/03`).  It survives only as a *numerical match*.

**Grid-search implication**: the constraint *"$n_s$ matches Planck"* in CNSC translates to *"$\eta_{\text{Ising}} = 1 - n_s^{\text{Planck}} \approx 0.0351 \pm 0.0042$"*.  This is consistent with 3D Ising $\eta_{\text{Ising}} = 0.0363$ at $\sim 0.3\sigma$.  *Not new information*.

### 3.3 $r$ in CNSC — *ansatz with adjustable suppression*

The CNSC formula $r = 16\,\epsilon_{\text{eff}}\,c_s\,(\beta/\alpha)\cdot S_{\text{crit}}$ was found non-derivable.  As a *fit ansatz*:

$$r^{\text{CNSC,ansatz}}(M_{\text{GUT}}, \lambda, H_*, \beta/\alpha, S_{\text{crit}}, \Phi_0) = 16 \cdot \frac{|\dot H_*|}{H_*^2} \cdot \frac{1}{\bar\gamma} \cdot \frac{\beta}{\alpha} \cdot S_{\text{crit}}$$

with $\bar\gamma = \sqrt{1 + 9\alpha\lambda H_*^2/M_{\text{GUT}}^4}$ and $\epsilon_{\text{eff}} \approx 3$ in stiff matter.

**Grid-search implication**: the constraint *"$r < 0.06$"* in CNSC translates to a *combined* upper bound on $\beta/\alpha \cdot S_{\text{crit}} / \bar\gamma$.  Since $S_{\text{crit}}$ has *no natural prior* (it was introduced ad hoc), this constraint can *always be satisfied* by making $S_{\text{crit}}$ small enough.  *r-constraint provides no grid-search information* until $S_{\text{crit}}$'s prior is fixed.

### 3.4 BBN compatibility in CNSC

CNSC's null energy dilutes as $\rho_{\text{null}} \propto a^{-6}$.  At BBN ($T \sim 1$ MeV):

$$\rho_{\text{null}}(T_{\text{BBN}}) / \rho_r(T_{\text{BBN}}) \approx (T_{\text{BBN}}/T_c)^2 \cdot (\rho_{\text{null}}/\rho_r)(T_c)$$

Constraint: $\Delta N_{\text{eff}} < 0.3$ ⇒ $\rho_{\text{null}}/\rho_r < 0.1$ at BBN.

**Grid-search implication**: this gives *one genuine constraint* on $T_c$ and $H_*$ that does *not* reduce to parameter-fitting.  Specifically, $T_c \gtrsim 10$ MeV with reasonable margin.

### 3.5 Sound horizon $r_s$, $H_0$, $d_L(z)$ in CNSC

CNSC late-time cosmology *matches* $\Lambda$CDM (the framework was designed to recover standard cosmology post-transition).  Therefore $r_s, H_0, d_L(z)$ are *not* differentially constrained by CNSC parameters (assuming the framework recovers $\Lambda$CDM by $a \gtrsim 10^{-10}$).

**Grid-search implication**: these constraints are *trivially satisfied* in CNSC and provide *no grid-search information*.

### 3.6 Summary table — CNSC grid-search information content

| Constraint | Information for CNSC grid? | Reason |
|---|---|---|
| $A_s$ match | ❌ Trivially fixes $\Phi_0$ | No mechanism |
| $n_s$ match | ❌ Tautological with $\eta_{\text{Ising}}$ | Inheritance broken |
| $r < 0.06$ | ❌ Trivially satisfied via $S_{\text{crit}}$ | No prior on $S_{\text{crit}}$ |
| BBN | ✅ Bounds $T_c$ | Genuine constraint |
| Sound horizon | ❌ Trivial | $\Lambda$CDM recovered |
| $H_0$ tension | ❌ Trivial | $\Lambda$CDM recovered |
| $d_L(z)$ | ❌ Trivial | $\Lambda$CDM recovered |
| GRB LIV | ❌ Inapplicable | CNSC has no propagation modification |

**Honest result**: CNSC's *retrospective* grid search has *only one genuine observational constraint* (BBN).  All others reduce to parameter-fitting or are inapplicable.  The grid search will *primarily reveal the fine-tuning structure* (`11_naturalness_meta_observation.md`), not the *viable observational region*.  This is itself the finding.

## 4. Forward model — Framework v2

Framework v2's H1 is *not* a perturbation-generation framework.  It is a *light-propagation modification*: $c_{\text{eff}} = c_0 \cdot \mathcal{C}$.

Therefore $A_s, n_s, r$ are *not* directly produced by framework v2 — they must come from *whatever* sources cosmological perturbations (in framework v2's minimal form, possibly inflation or a separate non-inflationary mechanism such as CNSC's surviving F2-F4 substrate).

Framework v2 *modifies* the *propagation* of perturbations from emitter to observer.  The relevant observables are:

### 4.1 $c_{\text{eff}}(z)$ — sky-averaged

$$\frac{c_{\text{eff}}(z)}{c_0} = 1 - \frac{\xi_3}{M_*^6}\int_0^z \frac{\langle |\nabla_\perp R|^2\rangle(z')}{H(z')}dz'$$

This *modifies* the $d_L$-$z$ relation:

$$d_L^{\text{framework v2}}(z) = (1+z)\int_0^z \frac{c_{\text{eff}}(z')}{H(z')}dz'$$

### 4.2 $H_0$ tension

If $c_{\text{eff}}(z=0) < c_0$ in a frame where it accumulated over local LSS but $c_{\text{eff}}(z\sim 1100)$ is closer to $c_0$ (less integrated inhomogeneity at high z), the *inferred* $H_0$ from local distance ladder differs from the *inferred* $H_0$ from CMB sound horizon.  This is a *candidate explanation* for the SH0ES vs Planck $H_0$ tension.

Forward map:

$$\frac{H_0^{\text{local}} - H_0^{\text{CMB}}}{H_0^{\text{CMB}}} \approx \frac{c_{\text{eff,local}} - c_{\text{eff,CMB-LOS}}}{c_0}$$

Required: $\sim 5$ to $6\%$ to explain the observed tension.

### 4.3 GRB Lorentz invariance

For energy-independent $\mathcal{C}$ (framework v2 ansatz is so by construction — $\nabla_\perp R$ depends on geometry, not photon energy), Fermi-LAT GRB 090510 bound does not directly apply.  *Indirect* bound: $1 - \mathcal{C} < $ few % over GRB LOS, else GRB photons would be observationally smeared in time.

### 4.4 Sound horizon $r_s$

$r_s$ depends on integrated $c(z)$ from BBN to recombination.  If $c_{\text{eff}}$ differs from $c_0$ in that period, $r_s$ shifts.  Forward map:

$$\frac{\Delta r_s}{r_s} \approx \langle \mathcal{C} - 1 \rangle_{\text{BBN to recomb}}$$

### 4.5 Summary table — framework v2 grid-search information content

| Constraint | Information for framework v2 grid? | Forward map |
|---|---|---|
| $A_s$ match | ❌ Not produced by framework v2 | — (needs separate source) |
| $n_s$ match | ❌ Same | — |
| $r < 0.06$ | ❌ Same | — |
| BBN | △ Indirect via $c_{\text{eff}}$ at BBN epoch | $\mathcal{C}$ at $z \sim 10^{10}$ |
| Sound horizon $r_s$ | ✅ Direct | §4.4 |
| $H_0$ tension | ✅ Direct (potentially explanatory) | §4.2 |
| $d_L(z)$ | ✅ Direct | §4.1 |
| GRB LIV | △ Indirect | §4.3 |

**Honest result**: framework v2's grid search has *more genuine constraints* than CNSC's *because framework v2 modifies propagation*, which directly enters distance-redshift observables.  This is a structural advantage of framework v2 over CNSC for grid-search informativeness.

## 5. Predetermined fine-tuning verdict — from `12_physical_origins.md §5`

Three CNSC parameters have *no natural prior* (Doc 12 §5):

| Parameter | Natural prior | Predetermined verdict |
|---|---|---|
| $\lambda$ (DBI coupling) | absent | will be fine-tuned in any allowed grid region |
| $\beta/\alpha$ | absent | will be fine-tuned in any allowed grid region |
| $S_{\text{crit}}$ | absent | will be fine-tuned in any allowed grid region |

For these three, the grid search *outcome is predetermined* — they will be *fine-tuned regardless of search depth*.  The grid search's *real question* for CNSC is:

> **Within natural priors of the remaining 5 CNSC parameters ($M_{\text{GUT}}$, $\Phi_0$, $H_*$, $\eta_{\text{Ising}}$, $T_c$), is there a region consistent with the *one* genuine constraint (BBN)?**

Spoiler from §3.6: this is *trivially answerable* — BBN bound on $T_c \gtrsim 10$ MeV is easily satisfied within $T_c$'s natural prior $[10^{14}, 10^{16}]$ GeV.  So the CNSC retrospective grid search concludes:

- Within natural priors, *all 5 derivable parameters fit easily*.
- 3 non-natural parameters (λ, β/α, S_crit) are *predetermined fine-tuned*.
- The framework would have *survived observationally* (at the level of these constraints) but only by *accepting the 3 fine-tunings*.

This matches the *standard cosmological alternative* fate (Doc 11 §5 scenario 2).

## 6. Framework v2's predetermined verdict

Framework v2 has *no parameters without natural prior* (§3 of `12_physical_origins.md`).  $\xi_3, M_*$ both have natural EFT priors.  So:

> **The grid search's question for framework v2 is: do the natural priors $(\xi_3, M_*) = (1, M_P)$ produce a $c_{\text{eff}}(z)$ that *partially or fully explains* the $H_0$ tension while satisfying GRB and SNe bounds?**

This is *substantive* — unlike CNSC, the answer is *not predetermined*.  It depends on the actual numerical magnitudes.

Preliminary expectation from `xi_grid_search.py` (first attempt): the natural EFT region produces *effects too small to be observable*.  But that calculation used schematic $|\nabla_\perp R|^2$ estimates.  A more careful calculation (using actual LSS power spectrum integrated along light-of-sight) might shift this.

## 7. Root-cause tracking methodology

For the next-turn grid search script, **each accepted parameter region** must be annotated with which parameters are *driving the fit*.

Specifically:

### 7.1 Sensitivity diagnostic

For each accepted point $\mathbf{\pi}^*$ in parameter space, compute the *log-Jacobian* of each constraint with respect to each parameter:

$$J_{ij} = \frac{\partial \ln (\text{constraint}_i)}{\partial \ln \pi_j}\bigg|_{\mathbf{\pi}^*}$$

Rows: 9 observational constraints.  Columns: 10 parameters.

### 7.2 Identification of root-cause parameters

A parameter is the *root cause* of fine-tuning if:

1. Its $|J_{ij}|$ for at least one constraint is $> 1$ (constraint is *sensitive* to it),
2. Its accepted-region width is $\Delta \ln \pi_j < 1$ dex (the constraint *forces* a narrow range),
3. Its natural prior is broader than the accepted range.

Conditions 1-3 together signal that the parameter is *forced fine-tuned* by the constraint set.

### 7.3 Naturalness gap quantification

For each fine-tuned parameter $\pi_j$, the *naturalness gap* is:

$$g_j = \log_{10}\frac{\text{natural prior width}}{\text{accepted region width}}$$

$g_j > 1$ means at least 1 order of magnitude of fine-tuning.  $g_j > 5$ means severe fine-tuning (e.g., cosmological constant level).

### 7.4 Outputs from root-cause tracking

The next-turn grid-search script will produce:

| Output | Purpose |
|---|---|
| `multi_framework_result.json::sensitivity_matrix` | $J_{ij}$ for each accepted region |
| `multi_framework_result.json::root_cause_parameters` | list of parameters with $g_j > 1$ |
| `multi_framework_result.json::naturalness_gap_summary` | $\{(\pi_j, g_j)\}$ for all parameters |
| `outputs/figures/sensitivity_heatmap.png` | $J_{ij}$ visualized |
| `outputs/figures/naturalness_gap_bar.png` | $g_j$ for each parameter as bar chart |

The user's intuition — *"이전 기각된 연구에서도 그렇고"* — translates operationally to: *"identify which parameters' fine-tuning was the cause of past framework failures"*.  Root-cause tracking gives this directly.

## 8. Next-turn deliverables

`outputs/verification/multi_framework_grid.py`:
- Implement forward models §3 (CNSC) and §4 (framework v2).
- Apply the 9 observational constraints with framework-specific tolerances.
- Use natural priors for first-pass grid (Doc 12 §5).
- Use stretched priors for second-pass extended grid.
- Output:
  - Viable region maps for $(M_{\text{GUT}}, H_*)$, $(\beta/\alpha, S_{\text{crit}})$, $(\xi_3, M_*)$ 2D slices.
  - Sensitivity matrix and root-cause annotations.
  - JSON summary.

Expected time: 2-3 hours of Python implementation + ~30 minutes runtime + ~30 minutes interpretation.

## 9. What this document achieves

Three things, mapping to the user's directives:

1. **Forward maps explicit** (O1) — each constraint is now operationally defined per framework.  The grid search will *not* apply inflationary formulas to CNSC by accident.

2. **Retrofit risk neutralized** (O2) — Doc 12 §0 framing + this doc's §3 are explicit: CNSC parameters are *retrospective targets*, not *revival inputs*.

3. **Root-cause methodology defined** (Q3) — the grid search will not just identify viable regions but *will annotate which parameters force the fine-tuning*.  This converts the standard "yes/no viability" output into *"yes/no + which root causes"*, giving the user's intuition operational form.

## 10. Final honest expectation

Under the analyses of §3.6, §4.5, §5, §6:

- **CNSC retrospective grid search**: will show *5 derivable parameters fit easily within natural priors* + *3 ad-hoc parameters fine-tuned regardless*.  Net conclusion: *CNSC would have observationally survived, at the cost of 3 fine-tunings*.  Not a revival — a *retrospective confirmation* of `docs/derivations/`'s naturalness verdict.

- **Framework v2 grid search**: will likely show natural $(\xi_3, M_*)$ produce *unobservably small* effects.  Either *stretched priors must be invoked* (fine-tuning required) or *the ansatz is too weak* (framework v2 inadequate).  Decisive either way.

The grid search will not *resolve* the naturalness problem.  It will *quantify* it precisely.  That quantification is itself the inquiry's next data point.
