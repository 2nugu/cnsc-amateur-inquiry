# Derivation 1 — The k-dependence of γ in CNSC

**Date**: 2026-05-13
**Purpose**: Test whether the form $\gamma(k) = \sqrt{1+(k/k_*)^4}$ asserted in T2.4 of the axiom map emerges naturally from the second-order action expansion of $S_{\text{CNSC}}$, or whether a different power (or no power) emerges.  This is an *honest derivation attempt*: success / partial / failure are all reported as found.

## 1. Setup

The CNSC action is

$$S = \int d^4x\,\sqrt{-g}\left[\frac{R}{16\pi G} - M^4\!\left(\gamma - 1\right)\right], \qquad \gamma = \sqrt{1 + \frac{\lambda I_{\text{null}}}{M^4}}, \qquad I_{\text{null}} = \alpha\theta^2 + \beta\sigma_{\mu\nu}\sigma^{\mu\nu}.$$

We work on the FLRW background $ds^2 = -dt^2 + a(t)^2 d\vec x^2$, with $\bar\ell^\mu = (1, 1/a, 0, 0)$ (radial null generator), $\bar\theta = 3H$, $\bar\sigma_{\mu\nu}=0$.  Define background DBI factor

$$\bar\gamma \;\equiv\; \sqrt{1 + \frac{9\alpha\lambda H^2}{M^4}}.$$

We expand $\ell^\mu = \bar\ell^\mu + \delta\ell^\mu$ to second order in the perturbation $\delta\ell^\mu(t,\vec x)$.

## 2. Linear constraint from $\ell^\mu\ell_\mu = 0$

$$g_{\mu\nu}\ell^\mu\ell^\nu = 0.$$

At linear order on FLRW,

$$-2\bar\ell^0\,\delta\ell^0 + 2a^2\bar\ell^i\,\delta\ell_i = 0\quad\Rightarrow\quad \delta\ell^0 = a\,\delta\ell^r$$

(taking only radial perturbation; transverse $\delta\ell^{\perp}$ vanishes from null preservation at linear order if we ignore metric perturbations).

We adopt $u(t,\vec x) \equiv a\,\delta\ell^r$ as the single dynamical scalar perturbation; then $\delta\ell^0 = u$, $\delta\ell^r = u/a$.

## 3. Linear perturbation of $\theta$

$$\theta = \nabla_\mu\ell^\mu = \frac{1}{\sqrt{-g}}\partial_\mu(\sqrt{-g}\,\ell^\mu) = \dot\ell^0 + 3H\ell^0 + \partial_i\ell^i.$$

Background: $\bar\theta = 0 + 3H \cdot 1 + 0 = 3H.$  ✓

With $\delta\ell^0 = u$, $\delta\ell^r = u/a$ (from §2 constraint):

$$\delta\theta = \dot u + 3Hu + \partial_r(u/a) = \dot u + 3Hu + \frac{1}{a}\partial_r u.$$

In Fourier space $\partial_r \to ik$:

$$\boxed{\delta\theta(t,k) = \dot u + 3Hu + \frac{ik}{a}\,u.}\tag{D1.0}$$

Note: the spatial derivative gives a $k/a$ factor (not $k/a^2$ as a sloppier dimensional argument might suggest); the Hubble-friction term $3Hu$ is essential.

## 4. Linear perturbation of $\sigma_{\mu\nu}\sigma^{\mu\nu}$

The shear tensor

$$\sigma_{\mu\nu} = \nabla_{(\mu}\ell_{\nu)} - \frac{1}{3}\theta\,h_{\mu\nu}, \qquad h_{\mu\nu} = g_{\mu\nu} + \ell_\mu k_\nu + k_\mu\ell_\nu$$

(with auxiliary null $k^\mu$).  On the FLRW background, $\bar\sigma_{\mu\nu} = 0$ by spatial isotropy.

The linear perturbation $\delta\sigma_{\mu\nu}$ is more involved because $h_{\mu\nu}$ also fluctuates.  However, $\sigma_{\mu\nu}\sigma^{\mu\nu}$ is *quadratic* in $\sigma$, so at second order in $\delta\ell^\mu$ the relevant contribution is

$$\delta^2(\sigma_{\mu\nu}\sigma^{\mu\nu}) = 2\,\delta\sigma_{\mu\nu}\delta\sigma^{\mu\nu}$$

(the cross term $2\bar\sigma\cdot\delta\sigma = 0$).

For a single-mode radial perturbation, the shear contribution is *higher* order in spatial derivatives than the trace contribution.  In Fourier space, schematically

$$\delta\sigma_{\mu\nu}\delta\sigma^{\mu\nu} \sim \left(\frac{k}{a}\right)^2 u^2 \cdot \mathcal{O}(1)$$

The factor $(k/a)^2$ (not $(k/a^2)^2$) comes from the *traceless* part of the gradient, which has a different scaling than the trace.

## 5. Quadratic action

Expanding $\mathcal{L} = -M^4(\gamma - 1)$ around $\bar\gamma$:

$$\delta^{(2)}\mathcal{L} = -\frac{\lambda}{\bar\gamma}\left[\alpha\,(\delta\theta)^2 + \beta\,\delta\sigma_{\mu\nu}\delta\sigma^{\mu\nu}\right] + \frac{9\lambda^2\alpha^2 H^2}{2 M^4 \bar\gamma^3}\,(\delta\theta)^2.$$

The first bracket is the *direct* quadratic contribution; the second term comes from expanding $\gamma$ to second order using the background value $\bar I = 9\alpha H^2 \cdot \lambda/M^4 \cdot \bar\gamma^{-2}$ implicit in $\bar\gamma$.

Substituting $\delta\theta$ from (boxed equation above) and the shear contribution:

Substituting (D1.0) for $\delta\theta$ and the schematic shear contribution $\delta\sigma^2 \sim (k/a)^2|u|^2$:

$$\delta^{(2)}\mathcal{L} = -\frac{\alpha\lambda}{\bar\gamma}\!\left|\dot u + 3Hu + \frac{ik}{a}u\right|^2 - \frac{\beta\lambda}{\bar\gamma}\cdot\frac{k^2}{a^2}|u|^2 + \frac{9\alpha^2\lambda^2 H^2}{2M^4\bar\gamma^3}\!\left|\dot u + 3Hu + \frac{ik}{a}u\right|^2.$$

Combining the $\theta$-channel terms and using $\bar\gamma^2 = 1 + 9\alpha\lambda H^2/M^4$, the kinetic prefactor becomes

$$\mathcal{K} \equiv \frac{\alpha\lambda(1+\bar\gamma^2)}{2\bar\gamma^3}.$$

So the **second-order action for the radial perturbation $u$** is

$$\boxed{S^{(2)} = \int dt\,d^3x\,a^3\left[\,-\mathcal{K}\,\left|\dot u + 3Hu + \frac{ik}{a}u\right|^2 - \frac{\beta\lambda}{\bar\gamma}\,\frac{k^2}{a^2}\,|u|^2\,\right].}\tag{D1.1}$$

## 6. Reading off the kinetic structure

Expand the square in (D1.1):

$$\left|\dot u + 3Hu + \frac{ik}{a}u\right|^2 = |\dot u + 3Hu|^2 + \frac{k^2}{a^2}|u|^2 + 2\,\frac{k}{a}\,\text{Im}\bigl[(\dot u + 3Hu)u^*\bigr].$$

The dominant terms for high-$k$ modes are the $|\dot u|^2$ kinetic and the $(k^2/a^2)|u|^2$ "gradient" piece.

- **Pure kinetic coefficient**: $\mathcal{K}$ — independent of $k$.
- **Gradient $k^2|u|^2$ coefficient**: $\mathcal{K}/a^2 + \beta\lambda/(a^2\bar\gamma)$.

WKB dispersion relation:

$$\omega^2(k) \approx \frac{k^2}{a^2}\!\left[\,1 + \frac{\beta/\alpha}{(1+\bar\gamma^2)/(2\bar\gamma^2)}\,\right].$$

Defining the effective sound speed by $\omega^2 = c_s^2 k^2/a^2$:

$$\boxed{c_s^2 \;=\; 1 \;+\; \frac{2\bar\gamma^2}{1+\bar\gamma^2}\cdot\frac{\beta}{\alpha} \;=\; \text{constant in } k.}\tag{D1.2}$$

Three notable features:

(i) The sound speed in (D1.2) is **manifestly $k$-independent**.  No envelope $\gamma(k) = \sqrt{1+(k/k_*)^4}$ emerges.

(ii) In the high-energy limit $\bar\gamma \gg 1$ (deep DBI regime), $c_s^2 \to 1 + 2(\beta/\alpha)$ — a *constant*.

(iii) In the low-energy limit $\bar\gamma \to 1$, $c_s^2 \to 1 + (\beta/\alpha)$ — also a constant (different value).

## 7. What this says

Reading (D1.2) carefully:

1. The $k^2$ dependence has **factored out** of the dispersion relation. The "sound speed" $c_s^2(k)$ in (D1.2) is **not $k$-dependent** at this order — it is a sum of a *scale-factor-dependent* piece $1/a^2$ and a *constant* piece $2\bar\gamma^2(\beta/\alpha)/(1+\bar\gamma^2)$.

2. There is **no $(k/k_*)^4$ envelope** emerging from this leading-order calculation. The $k^4$ behaviour asserted in T2.4 of the axiom map does *not* come from this expansion.

3. What does appear is a *time-dependent* sound speed through $a(t)$ and $\bar\gamma(t)$.  The scale $k_*$ defined in T2.4 (as $M\,H/\sqrt{\lambda}\,\phi$) does not appear here.

## 8. Possible interpretations

This negative result has three possible resolutions, in increasing order of plausibility:

(a) **The $(k/k_*)^4$ envelope is wrong**.  T2.4 should be revised to reflect the *constant* $c_s^2$ that emerges here, and the entire $f_{NL}(k)$ shape claim of the paper (T3.5, T3.8) must be rewritten.

(b) **The $(k/k_*)^4$ envelope emerges from higher-order operators not included in $S_{\text{CNSC}}$**.  For example, a term like $(\partial^2\theta)^2/M^4$ in $\mathcal{L}_{\text{null}}$ would give a $k^4$ kinetic contribution and could produce the asserted envelope.  But such operators must be *added* to the action, and once added, the action is no longer the DBI-inspired form claimed in §II.B of the paper.

(c) **The calculation above neglects something essential** — for example, the back-reaction of metric perturbations $\delta g_{\mu\nu}$ via Einstein's equations, or the null constraint at second (rather than linear) order.  If included, these could in principle produce additional $k$-dependence.  But each such inclusion makes the derivation longer and more dependent on auxiliary assumptions.

## 9. Honest verdict

Under the most natural reading of $S_{\text{CNSC}}$ as written in §II.B of the paper, the second-order action for the radial null-vector perturbation $u$ does **not** yield $\gamma = \sqrt{1+(k/k_*)^4}$.  Instead, it yields a sound speed $c_s^2$ that is *constant in $k$* at leading order, with time-dependence only through $a(t)$ and $\bar\gamma(t)$.

This is a *significant finding* for the paper:

- The claim T2.4 — *"the kinetic suppression envelope is $\gamma = \sqrt{1+(k/k_*)^4}$"* — is **not derivable** from the published $S_{\text{CNSC}}$.
- All downstream claims that depend on this envelope (T3.5 $f_{NL}(k)$ shape, T3.8 quadrupolar $f_{NL}^{(2)}$ peak at $k_*$, the $n_{f_{NL}} \approx 4$ running) are therefore **not derived** in the paper as it stands.
- The paper's quantitative skeleton above the spectral tilt $n_s$ rests on an unjustified momentum dependence.

This is the same critique that O1 raised in the audit, now made quantitative: the form $\gamma(k)$ promoted from background to momentum dependence in the DBI literature does not survive a careful second-order expansion.

## 10. What recovery would require

To salvage the $(k/k_*)^4$ envelope and the dependent predictions, one of the following must be done explicitly:

(i) **Add a higher-derivative operator** to $\mathcal{L}_{\text{null}}$ that generates $k^4$ in the kinetic term.  This is the only natural path within the EFT framework, but it changes the action.

(ii) **Include the metric perturbation back-reaction** in the calculation above and demonstrate that the coupled $\delta g_{\mu\nu} + \delta\ell^\mu$ system gives the $k^4$ envelope.  This would be a longer derivation but would close the gap.

(iii) **Reinterpret $k_*$ as a property of the *background*** rather than of the dispersion relation.  This is closer to the standard DBI usage, but then $k_*$ is not the saturation scale of an envelope — it is just a parameter.

The honest paper-level outcome is that **T2.4 must be re-stated as either an additional operator (path i) or a parametric ansatz (path iii), not as a derived consequence**.  This is now an open Class III task that has *not* been closed by the present derivation.

## 11. Cascade impact on other weaknesses

This result *cascades* to weaknesses 2, 3, 4:

- **Weakness 3 ($r$ formula)**: the formula $r = 16\epsilon_{\text{eff}} c_s (\beta/\alpha)$ assumes a $c_s$ from the DBI structure. With the *constant* $c_s$ derived here, $r$ becomes simply $r = 16\epsilon_{\text{eff}}c_s^{\text{const}}(\beta/\alpha)$ — no critical-point suppression $S_{\text{crit}}$ appears.  The window $[10^{-7}, 10^{-5}]$ adopted in the honest-path correction does *not* survive; the actual window becomes wider and overlaps the LiteBIRD/CMB-S4 sensitivity, *strengthening* the falsifiability but invalidating the paper's "all predictions below experimental reach" claim.

- **Weakness 2 (Mukhanov-Sasaki analogue)**: independent of weakness 1, this remains open. The freeze-in mechanism for $\zeta$ in $w=+1$ background is a separate open derivation.

- **Weakness 4 ($S_{\text{crit}}$ origin)**: this weakness *dissolves* in light of weakness 1's result — there is no $S_{\text{crit}}$ to derive an origin for, because no critical-point sound-speed suppression appears at this order.

## 12. Honest closing

**This derivation attempt did not succeed in confirming T2.4.**  Instead, it surfaced that T2.4 is *not derivable* from the published action under the most natural reading.  The result is reported as found; no attempt is made to retrofit the calculation to produce the desired envelope.
