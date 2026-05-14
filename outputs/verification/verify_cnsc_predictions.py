"""
CNSC Prediction Reproduction & Internal Consistency Audit
=========================================================
Runs the core CNSC quantitative claims end-to-end, compares against the
values stated in CNSC_Paper_Draft_PRD.md / CNSC_Complete_Framework.md /
CNSC_Document_Structure_Guide.md, and surfaces any inconsistencies.

Outputs three triples (PNG + CSV + *_desc.md) under outputs/figures/ and a
machine-readable JSON audit under outputs/verification/.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
FIG_DIR = ROOT / "outputs" / "figures"
VER_DIR = ROOT / "outputs" / "verification"
FIG_DIR.mkdir(parents=True, exist_ok=True)
VER_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# Baseline parameters (from CNSC_Paper_Draft_PRD.md §II.B & cnsc_internal_review.py)
# -----------------------------------------------------------------------------
M_GUT      = 1.0e16   # GeV (GUT scale)
LAMBDA_C   = 1.0e20   # GeV^2 (DBI coupling)
PHI_0      = 1.0e-5   # dimensionless amplitude
H_STAR     = 1.0e-10  # H*/M_Pl at transition
BETA_ALPHA = 0.01     # hierarchy
ETA_ISING  = 0.0363   # 3D Ising anomalous dimension

# Stated predictions in the documents
NS_STATED         = 0.9637
R_STATED_PAPER    = "≈ 0  (< 1e-4 falsifier threshold)"
R_STATED_RANALYS  = 1.0e-16        # cnsc_r_analysis.py
R_STATED_INTREVW  = (BETA_ALPHA**2) * 1.0e-6   # cnsc_internal_review.py → 1e-10
FNL_PLANCK_OBS    = (-0.9, 5.1)    # Planck 2018 local fNL ± 1σ
FNL_PBH_THRESHOLD = 1.3e5

# -----------------------------------------------------------------------------
# Core analytic predictions
# -----------------------------------------------------------------------------
def k_star(M=M_GUT, lam=LAMBDA_C, phi=PHI_0, H=H_STAR) -> float:
    """DBI saturation scale.  k* = (M^4 H^2 / (lambda phi^2))^(1/4)."""
    return (M**4 * H**2 / (lam * phi**2)) ** 0.25

def fNL(k, M=M_GUT, lam=LAMBDA_C, phi=PHI_0, H=H_STAR) -> np.ndarray:
    ks = k_star(M, lam, phi, H)
    gamma = np.sqrt(1.0 + (np.asarray(k) / ks)**4)
    return (35.0 / 108.0) * (gamma**2 - 1.0)

def ns_from_eta(eta=ETA_ISING) -> float:
    return 1.0 - eta

# -----------------------------------------------------------------------------
# Audit dataclass
# -----------------------------------------------------------------------------
@dataclass
class Check:
    name: str
    claimed: str
    computed: str
    delta: str
    status: str   # "pass" | "warn" | "fail"
    note: str = ""

checks: list[Check] = []

# (a) n_s ----------------------------------------------------------------------
ns_calc = ns_from_eta()
checks.append(Check(
    name="n_s from 3D Ising η",
    claimed=f"{NS_STATED:.4f}",
    computed=f"{ns_calc:.4f}",
    delta=f"{abs(ns_calc - NS_STATED):.2e}",
    status="pass" if abs(ns_calc - NS_STATED) < 1e-4 else "fail",
    note="Planck 2018: 0.9649 ± 0.0042 → CNSC at 0.29σ"
))

# (b) k_star -------------------------------------------------------------------
ks = k_star()
checks.append(Check(
    name="DBI saturation k_*",
    claimed="(M^4 H^2 / (λ φ^2))^{1/4}",
    computed=f"{ks:.3e} (natural units)",
    delta="-",
    status="pass",
    note="Sensitivity: k* ∝ M, ∝ H^{1/2}, ∝ λ^{-1/4}, ∝ φ^{-1/2}"
))

# (c) f_NL at Planck pivot -----------------------------------------------------
fNL_pivot = float(fNL(0.05))
fNL_compat_sigma = abs(fNL_pivot - FNL_PLANCK_OBS[0]) / FNL_PLANCK_OBS[1]
checks.append(Check(
    name="f_NL at k_CMB = 0.05 Mpc^{-1}",
    claimed="≪ 5  (Planck-compatible)",
    computed=f"{fNL_pivot:.3e}",
    delta=f"{fNL_compat_sigma:.3f}σ from Planck central",
    status="pass" if fNL_compat_sigma < 1.0 else "warn",
    note="Planck local: -0.9 ± 5.1"
))

# (d) f_NL saturation at PBH scale --------------------------------------------
fNL_pbh = float(fNL(1e12))
checks.append(Check(
    name="f_NL at PBH scale k ~ 10^12",
    claimed="≳ 1.3e5  (PBH formation threshold)",
    computed=f"{fNL_pbh:.3e}",
    delta=f"factor {fNL_pbh/FNL_PBH_THRESHOLD:.2f}× threshold",
    status="pass" if fNL_pbh > FNL_PBH_THRESHOLD else "warn",
    note="If well above threshold → potential PBH OVER-production risk"
))

# (e) r prediction --- THIS IS THE FLAGGED INCONSISTENCY -----------------------
checks.append(Check(
    name="Tensor-to-scalar ratio r — CROSS-DOC AUDIT",
    claimed="Paper Draft says r≈0; r_analysis.py says 1e-16; internal_review.py says 1e-10",
    computed=f"r_analysis={R_STATED_RANALYS:.0e}, internal_review={R_STATED_INTREVW:.0e}",
    delta="6 orders of magnitude discrepancy across own documents",
    status="fail",
    note="Internal inconsistency — must reconcile before submission. Both formulas are post-hoc estimates; neither is derived from a tensor mode equation."
))

# -----------------------------------------------------------------------------
# Figure 1: f_NL(k) spectrum with annotation
# -----------------------------------------------------------------------------
k_grid = np.logspace(-3, 15, 1000)
fNL_grid = fNL(k_grid)

fig1, ax = plt.subplots(figsize=(10, 6))
ax.loglog(k_grid, fNL_grid, color="tab:blue", lw=2.2, label=r"CNSC: $f_{NL}(k)$")
ax.errorbar(0.05, abs(FNL_PLANCK_OBS[0]), yerr=FNL_PLANCK_OBS[1],
            fmt="o", color="crimson", capsize=5, label=r"Planck 2018 ($1\sigma$)")
ax.errorbar(1.0, 1.0, yerr=1.0, fmt="s", color="forestgreen", capsize=5,
            label=r"Euclid/DESI projected ($1\sigma$)")
ax.axhline(FNL_PBH_THRESHOLD, ls="--", color="purple", alpha=0.7,
           label=r"PBH formation threshold ($f_{NL}\sim 10^5$)")
ax.axvline(ks, ls=":", color="black", alpha=0.6, label=fr"$k_* = {ks:.2e}$")
ax.set_xlabel(r"Wavenumber $k$  [Mpc$^{-1}$]")
ax.set_ylabel(r"$|f_{NL}(k)|$")
ax.set_title("Reproduced CNSC scale-dependent $f_{NL}$ spectrum")
ax.set_xlim(1e-3, 1e15)
ax.set_ylim(1e-10, 1e8)
ax.grid(True, which="both", alpha=0.3)
ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0))
fig1.tight_layout()
fig1_path = FIG_DIR / "fNL_spectrum_reproduction.png"
fig1.savefig(fig1_path, dpi=160, bbox_inches="tight")
plt.close(fig1)

np.savetxt(
    FIG_DIR / "fNL_spectrum_reproduction.csv",
    np.column_stack([k_grid, fNL_grid]),
    delimiter=",", header="k_Mpc_inv,fNL", comments=""
)

# -----------------------------------------------------------------------------
# Figure 2: n_s parameter band
# -----------------------------------------------------------------------------
eta_grid = np.linspace(0.020, 0.060, 200)
ns_grid = 1.0 - eta_grid
fig2, ax = plt.subplots(figsize=(8, 5))
ax.plot(eta_grid, ns_grid, color="tab:blue", lw=2.0, label=r"$n_s = 1 - \eta$")
ax.fill_between(eta_grid, 0.9649 - 0.0042, 0.9649 + 0.0042,
                color="crimson", alpha=0.15, label=r"Planck 2018 $1\sigma$")
ax.axhline(0.9649, color="crimson", lw=1.2)
ax.axvline(ETA_ISING, color="forestgreen", ls="--",
           label=fr"3D Ising $\eta = {ETA_ISING}$")
ax.scatter([ETA_ISING], [ns_calc], color="black", s=70, zorder=10,
           label=fr"CNSC: $n_s = {ns_calc:.4f}$")
ax.set_xlabel(r"Critical exponent $\eta$")
ax.set_ylabel(r"Spectral index $n_s$")
ax.set_title("CNSC $n_s$ prediction vs Planck 2018")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0))
fig2.tight_layout()
fig2_path = FIG_DIR / "ns_eta_band.png"
fig2.savefig(fig2_path, dpi=160, bbox_inches="tight")
plt.close(fig2)

np.savetxt(
    FIG_DIR / "ns_eta_band.csv",
    np.column_stack([eta_grid, ns_grid]),
    delimiter=",", header="eta,ns", comments=""
)

# -----------------------------------------------------------------------------
# Figure 3: r prediction — visualize the cross-doc inconsistency
# -----------------------------------------------------------------------------
ba_grid = np.logspace(-3, 0, 200)
r_internal_grid = (ba_grid**2) * 1.0e-6  # internal_review.py formula
fig3, ax = plt.subplots(figsize=(8, 5))
ax.loglog(ba_grid, r_internal_grid, color="tab:orange", lw=2.0,
          label=r"$r = (\beta/\alpha)^2 \cdot 10^{-6}$  (internal_review.py)")
ax.axhline(R_STATED_RANALYS, color="tab:red", ls="--",
           label=r"$r = 10^{-16}$  (cnsc_r_analysis.py)")
ax.axhline(1e-30, color="black", ls=":",
           label=r"Paper Draft: $r \approx 0$  (placeholder)")
ax.axhline(0.036, color="gray", ls="-.", alpha=0.7,
           label="BICEP/Keck upper bound (2024)")
ax.axhline(1e-3, color="forestgreen", ls=":", alpha=0.7,
           label=r"CMB-S4 target sensitivity")
ax.axhline(1e-4, color="crimson", ls=":", alpha=0.7,
           label=r"CNSC falsification threshold (claim)")
ax.axvline(BETA_ALPHA, color="black", alpha=0.5,
           label=fr"baseline $\beta/\alpha={BETA_ALPHA}$")
ax.set_xlabel(r"Hierarchy $\beta/\alpha$")
ax.set_ylabel(r"Tensor-to-scalar ratio $r$")
ax.set_title("Three different $r$ values appear across CNSC documents")
ax.set_ylim(1e-35, 1)
ax.grid(True, which="both", alpha=0.3)
ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=8)
fig3.tight_layout()
fig3_path = FIG_DIR / "r_prediction_inconsistency.png"
fig3.savefig(fig3_path, dpi=160, bbox_inches="tight")
plt.close(fig3)

np.savetxt(
    FIG_DIR / "r_prediction_inconsistency.csv",
    np.column_stack([ba_grid, r_internal_grid]),
    delimiter=",", header="beta_over_alpha,r_internal_review_formula", comments=""
)

# -----------------------------------------------------------------------------
# Description files
# -----------------------------------------------------------------------------
descs = {
    "fNL_spectrum_reproduction": dict(
        name="fNL_spectrum_reproduction",
        purpose="Reproduce CNSC scale-dependent f_NL prediction from DBI saturation.",
        source_script="outputs/verification/verify_cnsc_predictions.py",
        x_axis=("Wavenumber k", "Mpc^-1", f"{k_grid[0]:.1e} to {k_grid[-1]:.1e}", "log-spaced"),
        y_axis=("|f_NL(k)|", "dimensionless"),
        observations=[
            f"k_* = {ks:.3e}",
            f"f_NL at k=0.05 Mpc^-1 = {fNL_pivot:.3e}  (Planck: -0.9 ± 5.1)",
            f"f_NL at k=1.0 Mpc^-1  = {float(fNL(1.0)):.3e}  (Euclid target)",
            f"f_NL at k=1e12        = {fNL_pbh:.3e}  (PBH threshold 1.3e5)",
        ],
    ),
    "ns_eta_band": dict(
        name="ns_eta_band",
        purpose="CNSC n_s = 1 - η prediction overlaid on Planck 2018 1σ band.",
        source_script="outputs/verification/verify_cnsc_predictions.py",
        x_axis=("Critical exponent η", "dimensionless", "0.020 to 0.060", "linear"),
        y_axis=("Spectral index n_s", "dimensionless"),
        observations=[
            f"η_Ising = {ETA_ISING}",
            f"n_s,CNSC = {ns_calc:.4f}",
            "Planck central 0.9649, σ = 0.0042 → CNSC at 0.29σ",
        ],
    ),
    "r_prediction_inconsistency": dict(
        name="r_prediction_inconsistency",
        purpose=("Visualize the discrepancy between three different r predictions "
                 "(r≈0 paper, 1e-16 r_analysis.py, 1e-10 internal_review.py)."),
        source_script="outputs/verification/verify_cnsc_predictions.py",
        x_axis=("Hierarchy β/α", "dimensionless", "1e-3 to 1", "log-spaced"),
        y_axis=("Tensor-to-scalar ratio r", "dimensionless"),
        observations=[
            "internal_review.py formula → r=1e-10 at baseline β/α=0.01",
            "r_analysis.py asserts r=1e-16 with no formula",
            "Paper Draft asserts r≈0 with no derivation",
            "CMB-S4 sensitivity 1e-3; CNSC's own falsifier 1e-4",
            "All three CNSC values lie BELOW all detection thresholds — so internal numerical disagreement does NOT change observational status, but it WILL be flagged by referees.",
        ],
    ),
}

def write_desc(d: dict, path: Path) -> None:
    x_var, x_unit, x_range, x_step = d["x_axis"]
    y_var, y_unit = d["y_axis"]
    obs = "\n".join(f"- {o}" for o in d["observations"])
    text = (
        f"# Figure: {d['name']}\n\n"
        f"## Purpose\n{d['purpose']}\n\n"
        f"## Data Source\n- File: {d['name']}.csv\n"
        f"- Generated by: {d['source_script']}\n- Date: 2026-05-13\n\n"
        f"## Axes\n- X: {x_var} ({x_unit}) — range: {x_range}, interval: {x_step}\n"
        f"- Y: {y_var} ({y_unit})\n\n"
        f"## Key Observations\n{obs}\n\n"
        f"## Reproduction\npython outputs/verification/verify_cnsc_predictions.py\n"
    )
    path.write_text(text, encoding="utf-8")

for stem, d in descs.items():
    write_desc(d, FIG_DIR / f"{stem}_desc.md")

# -----------------------------------------------------------------------------
# JSON audit
# -----------------------------------------------------------------------------
audit = {
    "parameters": dict(M_GUT=M_GUT, LAMBDA_C=LAMBDA_C, PHI_0=PHI_0,
                       H_STAR=H_STAR, BETA_ALPHA=BETA_ALPHA, ETA_ISING=ETA_ISING),
    "checks": [asdict(c) for c in checks],
}
(VER_DIR / "audit.json").write_text(
    json.dumps(audit, indent=2, ensure_ascii=False), encoding="utf-8"
)

# -----------------------------------------------------------------------------
# Console summary
# -----------------------------------------------------------------------------
print("=" * 72)
print("CNSC PREDICTION REPRODUCTION — AUDIT REPORT")
print("=" * 72)
for c in checks:
    mark = {"pass": "[ OK ]", "warn": "[WARN]", "fail": "[FAIL]"}[c.status]
    print(f"{mark} {c.name}")
    print(f"       claimed : {c.claimed}")
    print(f"       computed: {c.computed}")
    print(f"       delta   : {c.delta}")
    print(f"       note    : {c.note}")
print("-" * 72)
print(f"Figures : {FIG_DIR}")
print(f"Audit   : {VER_DIR / 'audit.json'}")
