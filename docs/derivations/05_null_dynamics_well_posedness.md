# Derivation 5 — Well-Posedness of Null Hypersurface Dynamics

**Date**: 2026-05-13
**Purpose**: Test whether the CNSC dynamics on null hypersurfaces (or null-vector-field dynamics) constitute a *well-posed initial value problem*.

## 1. The general null problem

A *characteristic surface* of a PDE is one along which the principal symbol is degenerate.  For Einstein's equations and most matter field equations, **null hypersurfaces are characteristic**.

Consequence: an initial value problem with data only on a null hypersurface is generically *ill-posed* — additional data on a second null hypersurface (a *double-null* foliation) or on a timelike "corner" is needed to determine the future evolution.

This is the *Penrose-Sachs double-null formalism*: well-posed null initial value problems require *two* intersecting null hypersurfaces, not one.

## 2. CNSC's claim

The paper asserts that $\ell^\mu = \partial^\mu S$ is an *effective hydrodynamic field* whose dynamics are governed by the equation of motion derived from $S_{\text{CNSC}}$:

$$\nabla_\mu\!\left(\frac{\alpha\theta}{\gamma}\right) + \Lambda\,\ell_\mu = 0,$$

with the constraint $\ell^\mu\ell_\mu = 0$ enforced by Lagrange multiplier $\Lambda$.

The question: is this a well-posed PDE system?

## 3. Counting of dofs and constraints

$\ell^\mu$ has 4 components. The null constraint $\ell^2 = 0$ removes 1.  So 3 propagating dofs.

The equation of motion (one vector equation, 4 components) plus the constraint give a *constrained Hamiltonian system*.  Standard analysis (Dirac):

(i) Compute the primary constraint $\phi_1 = \ell^2 = 0$.
(ii) Compute the secondary constraint by demanding $\dot\phi_1 = \{\phi_1, H\} = 0$ on the constraint surface.
(iii) Continue until no new constraints emerge.

For a *gradient* field $\ell_\mu = \partial_\mu S$, the constraint $(\partial S)^2 = 0$ is the **eikonal equation**.  The eikonal equation is a *first-order, fully non-linear PDE* for $S$, and it is *well-posed as a Cauchy problem* on a spacelike hypersurface (standard PDE theory).

So *if* CNSC's $\ell^\mu$ is genuinely a gradient $\partial^\mu S$ with $S$ a scalar, then the dynamics reduce to the eikonal equation, which is well-posed.

## 4. The hidden assumption

But: *not every null vector field is a gradient*.  For a generic null $\ell^\mu$:

$$\nabla_{[\mu}\ell_{\nu]} \neq 0 \quad\text{(twist)}.$$

The paper assumes $\omega_{\mu\nu} = \nabla_{[\mu}\ell_{\nu]} = 0$ (zero twist, T2.1 implicitly).  Zero twist is equivalent to $\ell_\mu = f(x)\,\partial_\mu S$ for some scalar functions $f, S$ — i.e., *hypersurface-orthogonal* null vector.

This is **a substantive geometric restriction**, not a generic property.  Most cosmological null vector fields *do* have nonzero twist (e.g., the light from rotating black holes, or null geodesics in Bianchi cosmologies).

The CNSC paper's assumption that $\omega_{\mu\nu} = 0$ is *not derived* from any deeper principle — it is assumed for tractability.

## 5. Verdict on well-posedness

| Aspect | Status |
|---|---|
| Eikonal equation for $S$ | ✅ Well-posed (PDE theory) |
| $\ell^\mu = \partial^\mu S$ is hypersurface-orthogonal | 🟡 Restriction, assumed not derived |
| Zero twist $\omega_{\mu\nu} = 0$ | 🟡 Restriction, assumed not derived |
| General null $\ell^\mu$ dynamics in CNSC | ⏸ Not addressed |

So well-posedness *holds* under the restriction to hypersurface-orthogonal null vectors, but the restriction itself is an extra assumption beyond the action.

## 6. Why this matters for I-3

Intuition I-3 — *"$\ell^\mu = \partial^\mu S$ is an effective hydrodynamic field"* — is **partially defensible**:
- The form $\ell^\mu = \partial^\mu S$ *is* well-posed as eikonal dynamics.
- But it *excludes* the more generic non-gradient null vector fields, which the original null-connected cosmological intuition might more naturally describe.

The paper's specific choice $\ell^\mu = \partial^\mu S$ is a *simplification* that makes the problem tractable but restricts the physical content.

## 7. Verdict

| Intuition | Status |
|---|---|
| I-3 ($\ell^\mu = \partial^\mu S$ effective hydrodynamic field) | 🟡 **Partial** — well-posed within the assumed hypersurface-orthogonality, but the assumption itself is not derived |
| I-10 ($w=+1$ horizon problem resolution) | ✅ **Defensible** — standard stiff-matter cosmology supports this; CNSC adds nothing controversial here |
| I-2 (null-connected initial geometry) | ❌ **Cascade not defensible** — the well-posedness restriction (hypersurface-orthogonal) is *additional structure* beyond "null-connected", and the original cosmological intuition is not realized without it |

## 8. Closure

The null hypersurface dynamics in CNSC are well-posed *only after* assuming hypersurface-orthogonality.  This is a *restrictive* assumption that:
- Was not explicitly stated as an axiom T2.x in the paper (it is implicit in $\ell_\mu = \partial_\mu S$).
- Excludes generic cosmological null vector fields.
- Reduces the dynamical content to the eikonal equation, which is well-known and not specific to "null cosmology".

The deeper intuition I-2 (*"null-connected initial geometry"* as a cosmological state) does not survive without ad hoc additional structure.
