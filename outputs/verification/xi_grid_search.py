"""
Grid Search — Coherence VSL Parameter Window Identification
============================================================
Tests whether any region of the (xi_3, M_*) parameter space simultaneously
satisfies the dominant cosmological / GRB constraints under the working
ansatz of framework_v2/06:

    C(gamma) = exp[ - xi_3 / M_*^6 * Integral( |grad_perp R|^2 ) d lambda ]
    c_eff = c_0 * C(gamma)

This script implements ORDER-OF-MAGNITUDE analytical bounds, not full
CAMB/MCMC likelihoods. The goal is to identify whether an allowed window
EXISTS, not to fit it precisely.

Outputs:
  outputs/figures/xi_M_allowed_region.png  (+ CSV + _desc.md)
  outputs/verification/xi_grid_result.json (machine-readable bound summary)
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
FIG_DIR = ROOT / "outputs" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------------------
# Physical constants and reference scales (natural units, GeV)
# ----------------------------------------------------------------------------
M_PLANCK = 1.22e19          # Planck mass in GeV
M_GUT    = 1.0e16           # GUT-scale reference
M_EW     = 246.0            # Electroweak scale
H0_GeV   = 1.44e-42         # H0 ~ 67 km/s/Mpc in GeV (natural units)
R_typical_LSS = 1.0e-122    # typical Ricci scalar squared in current universe ~ (H_0)^4 in GeV^4

# Inhomogeneity scale: typical curvature gradient in LSS
# |grad_perp R|^2 ~ (delta_R / L)^2 where delta_R ~ R * delta_rho/rho ~ R * 1e-5 (CMB-level)
# L ~ 100 Mpc ~ 1e-29 GeV^-1 for spatial gradient
delta_rho_over_rho = 1e-5
L_LSS_inv_GeV = 1.0 / (100 * 3.086e22 * 1e9 / 6.582e-25)   # 100 Mpc in GeV^-1 ... compute numerically
# Simpler: use cosmological scale H0^-1 as characteristic length
L_cos_GeV_inv = 1.0 / H0_GeV
# grad_perp R ~ R * delta_rho_over_rho / L_LSS  with L_LSS ~ Hubble scale / 100
L_LSS_GeV_inv = L_cos_GeV_inv / 100.0
grad_perp_R_squared_typical = (np.sqrt(abs(R_typical_LSS)) * delta_rho_over_rho / L_LSS_GeV_inv)**2
# (this is order-of-magnitude only; we use it as a calibration scale)

# Hubble-time light path: ~ 1/H0
lambda_path_GeV_inv = L_cos_GeV_inv

# ----------------------------------------------------------------------------
# Constraint functions
# ----------------------------------------------------------------------------
def DeltaC_estimate(log10_xi, log10_M_GeV):
    """
    Order-of-magnitude estimate of 1 - C(gamma) accumulated over a Hubble-scale path
    through typical LSS inhomogeneity.

        1 - C ~ xi/M^6 * |grad_perp R|^2 * lambda_path
    """
    xi = 10**log10_xi
    M  = 10**log10_M_GeV
    return xi / (M**6) * grad_perp_R_squared_typical * lambda_path_GeV_inv

def constraint_GRB(log10_xi, log10_M_GeV):
    """
    GRB Lorentz invariance: ANY energy-independent VSL effect along the GRB
    line of sight must satisfy 1 - C < 1e-3 (else GRB photons wouldn't reach us
    coherently at observed levels).
    Returns True if PASSES (allowed).
    """
    return DeltaC_estimate(log10_xi, log10_M_GeV) < 1e-3

def constraint_dL_residual(log10_xi, log10_M_GeV):
    """
    Pantheon+ supernova d_L(z) residual: c_eff variation along line of sight
    contributes to distance modulus; must be < 1% (current SNe systematic).
    Same as 1-C < 1e-2.
    """
    return DeltaC_estimate(log10_xi, log10_M_GeV) < 1e-2

def constraint_observable_lower(log10_xi, log10_M_GeV):
    """
    Lower bound for observability: 1 - C must be > 1e-5 to be plausibly
    distinguishable from cosmological systematics by next-decade surveys.
    Returns True if effect IS observable (allowed region's interesting subset).
    """
    return DeltaC_estimate(log10_xi, log10_M_GeV) > 1e-5

def constraint_H0_tension(log10_xi, log10_M_GeV):
    """
    H0 tension is ~5%; if framework explains it, 1-C ~ 5e-2 at z ~ 0.1.
    Loose constraint: pass if 1-C in [1e-3, 1e-1] (could partially explain).
    """
    dc = DeltaC_estimate(log10_xi, log10_M_GeV)
    return (dc > 1e-3) & (dc < 1e-1)

# ----------------------------------------------------------------------------
# Grid setup
# ----------------------------------------------------------------------------
log_xi_arr = np.linspace(-30, 30, 121)   # xi_3 from 1e-30 to 1e30
log_M_arr  = np.linspace(10, 20, 101)    # M_* from 1e10 to 1e20 GeV

XI, MM = np.meshgrid(log_xi_arr, log_M_arr, indexing="ij")
DC_grid = DeltaC_estimate(XI, MM)

# Region masks
mask_GRB     = constraint_GRB(XI, MM)
mask_dL      = constraint_dL_residual(XI, MM)
mask_observ  = constraint_observable_lower(XI, MM)
mask_H0      = constraint_H0_tension(XI, MM)

# Combined allowed region (passes both upper bounds AND is observable)
mask_allowed_obs = mask_GRB & mask_dL & mask_observ
mask_allowed_any = mask_GRB & mask_dL
mask_H0_window   = mask_H0 & mask_GRB & mask_dL

# ----------------------------------------------------------------------------
# Naturalness analysis
# ----------------------------------------------------------------------------
# Natural EFT value: xi ~ O(1) at M_* ~ M_Planck
log_xi_natural = 0.0
log_M_natural  = np.log10(M_PLANCK)
DC_natural = DeltaC_estimate(log_xi_natural, log_M_natural)

# Allowed region width
allowed_indices = np.argwhere(mask_allowed_any)
if len(allowed_indices):
    log_xi_allowed = log_xi_arr[allowed_indices[:, 0]]
    log_M_allowed  = log_M_arr[allowed_indices[:, 1]]
    log_xi_range = (float(log_xi_allowed.min()), float(log_xi_allowed.max()))
    log_M_range  = (float(log_M_allowed.min()),  float(log_M_allowed.max()))
else:
    log_xi_range = log_M_range = None

# Naturalness gap: how far from xi=1, M=M_Planck is the allowed region?
def dist_from_natural(log_xi, log_M):
    return np.sqrt((log_xi - log_xi_natural)**2 + (log_M - log_M_natural)**2)

if len(allowed_indices):
    distances = dist_from_natural(log_xi_allowed, log_M_allowed)
    min_dist  = float(distances.min())
    closest_idx = int(distances.argmin())
    closest_log_xi = float(log_xi_allowed[closest_idx])
    closest_log_M  = float(log_M_allowed[closest_idx])
else:
    min_dist = closest_log_xi = closest_log_M = None

# ----------------------------------------------------------------------------
# Plot
# ----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 7))

# Background: color-code by Delta C order of magnitude (log10)
log_DC = np.log10(np.clip(DC_grid, 1e-40, 1e40))
im = ax.pcolormesh(log_xi_arr, log_M_arr, log_DC.T, cmap="viridis",
                   shading="auto", vmin=-30, vmax=10)
cbar = fig.colorbar(im, ax=ax)
cbar.set_label(r"$\log_{10}(1 - \mathcal{C})$ over Hubble path")

# Overlay constraint boundaries
ax.contour(log_xi_arr, log_M_arr, DC_grid.T, levels=[1e-3], colors=["red"],
           linewidths=2, linestyles="-")
ax.contour(log_xi_arr, log_M_arr, DC_grid.T, levels=[1e-2], colors=["orange"],
           linewidths=2, linestyles="--")
ax.contour(log_xi_arr, log_M_arr, DC_grid.T, levels=[1e-5], colors=["cyan"],
           linewidths=2, linestyles=":")

# Mark natural point
if DC_natural > 0:
    log_DC_natural = float(np.log10(DC_natural))
    nat_label = fr"natural EFT: $\xi=1$, $M_*=M_P$ ($\log_{{10}}\Delta C \approx {log_DC_natural:.1f}$)"
else:
    nat_label = r"natural EFT: $\xi=1$, $M_*=M_P$ ($\Delta C$ underflows)"
ax.plot(log_xi_natural, log_M_natural, marker="*", color="white",
        markersize=18, markeredgecolor="black", label=nat_label)

# Mark closest allowed point (if any)
if closest_log_xi is not None:
    ax.plot(closest_log_xi, closest_log_M, marker="o", color="red",
            markersize=12, markeredgecolor="black",
            label=fr"closest allowed: $\xi=10^{{{closest_log_xi:.1f}}}$, $M_*=10^{{{closest_log_M:.1f}}}$ GeV")

# Mark H0-tension window
if mask_H0_window.any():
    h0_indices = np.argwhere(mask_H0_window)
    h0_log_xi = log_xi_arr[h0_indices[:, 0]]
    h0_log_M  = log_M_arr[h0_indices[:, 1]]
    ax.scatter(h0_log_xi, h0_log_M, marker="x", color="magenta",
               s=12, label=r"$H_0$ tension explanation window")

ax.set_xlabel(r"$\log_{10}\,\xi_3$ (dimensionless coupling)")
ax.set_ylabel(r"$\log_{10}(M_* / \mathrm{GeV})$")
ax.set_title(r"Parameter window for $\mathcal{C} = \exp[-\xi_3 |\nabla_\perp R|^2 / M_*^6]$")

# Custom legend handles for contours
from matplotlib.lines import Line2D
contour_handles = [
    Line2D([], [], color="red",    linewidth=2, linestyle="-",  label=r"GRB bound ($\Delta C = 10^{-3}$)"),
    Line2D([], [], color="orange", linewidth=2, linestyle="--", label=r"SNe $d_L$ bound ($\Delta C = 10^{-2}$)"),
    Line2D([], [], color="cyan",   linewidth=2, linestyle=":",  label=r"observability ($\Delta C = 10^{-5}$)"),
]
legend1 = ax.legend(handles=contour_handles, loc="upper left", fontsize=9)
ax.add_artist(legend1)
ax.legend(loc="lower right", fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig_path = FIG_DIR / "xi_M_allowed_region.png"
fig.savefig(fig_path, dpi=160, bbox_inches="tight")
plt.close(fig)

# ----------------------------------------------------------------------------
# CSV
# ----------------------------------------------------------------------------
csv = np.column_stack([XI.ravel(), MM.ravel(), DC_grid.ravel(),
                       mask_allowed_any.astype(int).ravel(),
                       mask_observ.astype(int).ravel(),
                       mask_H0_window.astype(int).ravel()])
np.savetxt(FIG_DIR / "xi_M_allowed_region.csv", csv, delimiter=",",
           header="log10_xi,log10_M_GeV,delta_C,allowed_GRB_dL,observable,H0_window",
           comments="")

# ----------------------------------------------------------------------------
# Description file
# ----------------------------------------------------------------------------
desc_path = FIG_DIR / "xi_M_allowed_region_desc.md"
desc = f"""# Figure: xi_M_allowed_region

## Purpose
Grid search over the (xi_3, M_*) parameter space of framework v2's coherence
functional ansatz, identifying regions that simultaneously satisfy GRB and
supernova bounds while remaining observable.

## Data Source
- File: xi_M_allowed_region.csv
- Generated by: outputs/verification/xi_grid_search.py
- Date: 2026-05-14

## Axes
- X: log10(xi_3), range -30 to 30 (60 dex span)
- Y: log10(M_* / GeV), range 10 to 20 (GUT to super-Planck)
- Z: log10(1 - C) accumulated over Hubble-scale photon path

## Constraints overlaid
- Red solid: GRB Lorentz invariance (Delta C = 1e-3)
- Orange dashed: Pantheon+ d_L residual (Delta C = 1e-2)
- Cyan dotted: Observability threshold (Delta C = 1e-5)

## Key Observations
- Natural EFT point (xi=1, M=M_P): Delta C ~ {DC_natural:.2e}
  (off the chart — far below observability)
- Allowed-and-observable region: {"exists" if mask_allowed_obs.any() else "does NOT exist within grid"}
- H0 tension window (Delta C in [1e-3, 1e-1]): {"exists" if mask_H0_window.any() else "does not exist"}
- Closest allowed-region point to "natural EFT" baseline:
  xi = 10^{closest_log_xi}, M = 10^{closest_log_M} GeV (if applicable)
- Naturalness gap (log10 distance from natural baseline to closest allowed):
  {min_dist:.1f} dex (if applicable)

## Reproduction
python outputs/verification/xi_grid_search.py
"""
desc_path.write_text(desc, encoding="utf-8")

# ----------------------------------------------------------------------------
# JSON summary
# ----------------------------------------------------------------------------
summary = {
    "natural_baseline": {
        "log10_xi": log_xi_natural,
        "log10_M_GeV": log_M_natural,
        "delta_C_at_natural": float(DC_natural),
    },
    "allowed_region_exists": bool(mask_allowed_any.any()),
    "allowed_and_observable_exists": bool(mask_allowed_obs.any()),
    "H0_window_exists": bool(mask_H0_window.any()),
    "allowed_log_xi_range": log_xi_range,
    "allowed_log_M_range": log_M_range,
    "naturalness_gap_dex": min_dist,
    "closest_allowed": {
        "log10_xi": closest_log_xi,
        "log10_M_GeV": closest_log_M,
    } if min_dist is not None else None,
    "interpretation": (
        "If allowed_region_exists is True but naturalness_gap_dex >> 0, "
        "the framework is phenomenologically alive but theoretically fine-tuned. "
        "This is the typical fate predicted by docs/derivations/00 + framework_v2/11."
    ),
}
(HERE / "xi_grid_result.json").write_text(
    json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
)

# ----------------------------------------------------------------------------
# Console output
# ----------------------------------------------------------------------------
print("="*72)
print("xi-M GRID SEARCH — RESULTS")
print("="*72)
print(f"Grid: log10_xi in [{log_xi_arr[0]}, {log_xi_arr[-1]}] ({len(log_xi_arr)} points)")
print(f"      log10_M  in [{log_M_arr[0]}, {log_M_arr[-1]}] ({len(log_M_arr)} points)")
print()
print(f"Natural EFT baseline: xi=1, M=M_P -> Delta C = {DC_natural:.3e}")
print()
print(f"GRB allowed region:        {'YES' if mask_GRB.any() else 'NO'}")
print(f"SNe d_L allowed region:    {'YES' if mask_dL.any() else 'NO'}")
print(f"Observable AND GRB+dL OK:  {'YES' if mask_allowed_obs.any() else 'NO'}")
print(f"H0 tension explainable:    {'YES' if mask_H0_window.any() else 'NO'}")
print()
if min_dist is not None:
    print(f"Closest allowed point to natural baseline:")
    print(f"  xi = 10^{closest_log_xi:.1f},  M_* = 10^{closest_log_M:.1f} GeV")
    print(f"  Naturalness gap = {min_dist:.1f} dex (log-distance from xi=1,M=M_P)")
print()
print(f"Figure: {fig_path}")
print(f"Summary JSON: {HERE / 'xi_grid_result.json'}")
