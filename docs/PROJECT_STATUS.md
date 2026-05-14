# PROJECT STATUS

## Overview
Critical Null-Structured Cosmology (CNSC): a non-inflationary phase-transition cosmology grounded in null hypersurface geometry, with falsifiable observational predictions ($n_s$, $r$, $f_{NL}$).

## Current Phase
Phase: **Inquiry complete — final substantive deliverable produced (2026-05-14).**  Status: **No novel quantitative content surviving. Methodology, intuition catalog, case studies remain as intellectual artifacts. Ready for release.**

**Final verdict (2026-05-14 grid search)**:
- CNSC retrospective: would have survived observationally within natural priors of 5 derivable parameters, at the cost of 3 ad-hoc fine-tunings ($\lambda$, $\beta/\alpha$, $S_{\text{crit}}$). Mechanism-level failures remain independent. Doc 11 Scenario 2 confirmed retrospectively.
- Framework v2 H1 (path-integral coherence VSL, curvature-gradient ansatz): grid search shows $\Delta\mathcal{C} \sim 10^{-250}$ at natural EFT scales; cosmologically unobservable at any parameter value. Doc 11 Scenario 5 (newly identified): "too weak even with tuning". Framework v2 H1 in its present ansatz form joins CNSC as archived/failed.
- Total: **8 novel-quantitative-content failures, 0 surviving** (7 CNSC weaknesses + 1 framework v2 H1).
- Final intellectual artifacts: methodology M1-M8, intuition catalog (`docs/derivations/00`), failure-mode case studies (`docs/derivations/01-08`, `framework_v2/06-14`), AI-collaborative honest-derivation record.

Progress: 26 of 27 actionable tasks closed. Tasks #7-#26 closed axiomatic-reframing program; tasks #27-#33 closed weakness-derivation inquiry. Only task #13 (future-work items) remains, now moot.

**Final outcome (2026-05-13 weakness derivation program)**: 7개 약점 모두 derive 시도; 결과는 **모든 quantitative claims가 mathematically not derivable**:
- 약점 1 ($\gamma(k)$ envelope) — negative (Derivations 01, 02)
- 약점 2 (Mukhanov-Sasaki analogue) — negative (Derivation 03)
- 약점 3 ($r$ formula) — cascade negative (Derivation 07)
- 약점 4 ($S_{\text{crit}}$) — moot from 약점 1
- 약점 5 (photon → cosmology) — metaphorical leap (Derivation 04)
- 약점 6 (null dynamics) — partial defensible under hypersurface-orthogonality (Derivation 05)
- 약점 7 (Z₂ LG origin) — fine-tuned ansatz (Derivation 06)

**Intuition catalog (`docs/derivations/00_intuition_catalog.md`)**:
- ✅ Defensible: 2 (I-1 SR-level, I-10 stiff matter cosmology) — both standard
- 🟡 Partial: 2 (I-3, I-4) — qualitative only
- ❌ Not defensible: 7 — all CNSC novelty claims

**Next-step recommendation** (`docs/derivations/08_what_remains_and_what_next.md`):
- 1주일 휴식 후 CNSC paper 운명 결정 (폐기 vs negative-result paper)
- 별도 framework redirect 검토 (path-integral coherence VSL 통찰)

**Post-2026-05-13 redirect status**: framework_v2 outline complete with 6 documents.  Recommended path is *phenomenological-first* (P-α + P-γ of `framework_v2/05_phenomenological_path.md`), bypassing OQ-1 derive-first heavy lifting.  Estimated 2 months to first publishable claim.  Alternative: negative-result paper from inquiry artifacts (no new derivation needed).

## Framework v2 Registry (post-pivot, 2026-05-13)

| File | Purpose |
|---|---|
| `framework_v2/README.md` | Reading order and navigation |
| `framework_v2/00_foundations.md` | F1-F4 surviving intuitions (all standard, used as substrate) |
| `framework_v2/01_coherence_VSL_seed.md` | H1 hypothesis with mainstream connections |
| `framework_v2/02_open_questions.md` | OQ1-OQ5 with realistic time estimates and bypass strategies |
| `framework_v2/03_methodology.md` | M1-M8 axiomatic + honest-derive rules |
| `framework_v2/04_user_specific_core.md` | What is uniquely the user's contribution (cores A, B, C, D) |
| `framework_v2/05_phenomenological_path.md` | Concrete P-α + P-γ starting plan, ~2 months to first claim |

## Phase Checklist
- [x] Reproduce paper-claimed numerical predictions end-to-end
- [x] Cross-document consistency audit
- [x] Assess Ising universality justification
- [x] Address stiff-matter reduction critique
- [x] Derive a new falsifiable signature (anisotropic $f_{NL}$)
- [x] Compile audit & defense documents
- [x] **Reconcile the $r$ formula across abstract, code, and Appendix** (T3.7 single formula across all 5 files)
- [x] **Fix PBH over-production by domain restriction** (T2.6 in code + paper; Figure 6 removed; §VIII.I speculative-only paragraph)
- [x] **Add $n_s = 1 - \eta$ derivation block to Appendix L** (full 7-step derivation + D1–D5 data programs)
- [x] **Rewrite abstract's $r$ claim as a window** ([10⁻⁷, 10⁻⁵], T3.7 formula)
- [x] **Promote $f_{NL}^{(2)}$ to fourth headline prediction** (T3.8 in §II.A + abstract + §IV.B + falsification table)
- [x] **Adopt axiomatic paper structure** (Axiom Map in §II.A of all 3 paper files + Appendices L, Mb expanded)
- [x] **Honest Disclosure block §VIII.J** with assumption-to-data map (T2.1–T2.6 → D1–D12)
- [x] **Single-paper strategy adopted** — no paper I/II/III split; Class III items as future-work program
- [x] **T-id annotations** on key numbered equations in PRD + JCAP English + Korean LaTeX
- [ ] **(Future-work, post-paper-I)** Second-order shear bispectrum derivation (Class III)
- [ ] **(Future-work, post-paper-I)** Stiff-matter Mukhanov-Sasaki analogue (T2.5 closure)
- [ ] **(Future-work, post-paper-I)** $\gamma(k)$ second-order action expansion (T2.4 closure)

## Completed Milestones

| Milestone | Output | Date |
|---|---|---|
| Numerical reproduction of $n_s$, $f_{NL}$, $k_*$ | `outputs/verification/audit.json` | 2026-05-13 |
| Cross-document audit (caught 4-way $r$ inconsistency, PBH catastrophe) | `docs/CNSC_Verification_Audit_2026.md` | 2026-05-13 |
| Null-geometry distinctiveness derivation | `docs/CNSC_Null_Geometry_Unique_Signature.md` | 2026-05-13 |
| Anisotropic $f_{NL}^{(2)}$ template (new falsifier) | `outputs/figures/anisotropic_fNL_template.*` | 2026-05-13 |

## Critical Findings (2026-05-13 weakness derivation program)

**Weakness 1 — γ(k) envelope derivation**: **NEGATIVE result confirmed**.

Both Path 1 (bare second-order expansion, `docs/derivations/01_gamma_k_second_order.md`) and Path 2 (with full metric back-reaction, `docs/derivations/02_gamma_k_with_metric_coupling.md`) yield a *k-independent* sound speed $c_s^2 = 1 + (2\bar\gamma^2/(1+\bar\gamma^2))(\beta/\alpha)$, **not** the $\gamma = \sqrt{1+(k/k_*)^4}$ envelope asserted in T2.4 of the paper.

Consequences (cascade through paper's quantitative skeleton):
- T2.4 is **not derivable** from $S_{\text{CNSC}}$ → ansatz status confirmed.
- T3.5 ($f_{NL}(k)$ shape), T3.8 (quadrupolar peak at $k_*$), $n_{f_{NL}} \approx 4$ running all inherit T2.4's ansatz status.
- The only path to recover the $k^4$ envelope is adding a higher-derivative operator to the action (Path 1), which changes the DBI-saturation interpretation and reintroduces fine-tuning.
- Hidden parameter $S_{\text{crit}}$ becomes unnecessary (no critical-point sound-speed suppression to derive an origin for).

**Only T3.3 ($n_s = 1 - \eta$) remains potentially derivable**, contingent on weakness 2 (stiff-matter Mukhanov-Sasaki analogue) closure.

## Active Decisions & Rationale

- **Epistemological reframing (2026-05-13)**: paper is to be restructured from "we predict X" (conclusion-first) to "under assumptions {A_i}, X follows" (axiom→derivation→bounded claim).  Negative existentials such as "no mechanism" are forbidden.  See `docs/CNSC_Axiom_Derivation_Map.md` for the full T1/T2/T3 classification of every numerical claim.  Rationale: user observed that "unproved claims are numerical assertions about something that cannot be numerically verified" — the constructive forward direction converts each weakness into either an explicit assumption (honest) or a derivation (defensible).
- **$r$ formula choice**: adopt `CNSC_Coupled_Perturbations.md` §6 expression $r = 16\epsilon_{\text{eff}}c_s\cdot(\beta_{\text{eff}}/\alpha_{\text{eff}})$ as the single authoritative formula (T3.7).  Reason: only this expression has a derivation; the other three values are scatter-plot annotations or post-hoc estimates.  Implication: must rewrite the abstract using a *window* prediction.
- **PBH catastrophe handling**: domain restriction — the EFT is valid only for $k \le k_*$ (T2.6).  Predictions at $k\sim 10^{12}$ Mpc$^{-1}$ are *not* given by this paper.  Reason: more honest than ad hoc UV cutoffs, and directly inherited from the axiom map.
- **Anisotropic $f_{NL}^{(2)}$ status**: T3.8, declared as *parametric estimate*.  Reason: the prefactor is from dimensional analysis, not from a second-order action expansion.  Promotion to a fully derived T3 result is a Class III open task (~1-3 months).
- **Single-paper strategy (2026-05-13)**: paper I/II/III 분할 거부됨. 모든 prediction과 future work이 단일 paper 안에 explicit하게 박힘. Class III 항목은 본 paper §IX.E의 future-work program으로 분류되며, 본 paper의 결론을 위협하지 않음. 광속-coherence VSL 재해석(사용자 별도 통찰)은 memory에만 보관, paper 본문 통합 안 함.

## Open Questions

- [x] ~~Paper structural quirk: §VIII.G, §VIII.H misplaced after Appendix N~~ — **resolved** 2026-05-13 (Task #19); §G, §H now correctly inside §VIII Discussion between §F and §I.
- [ ] Does the conformal-bootstrap value $\eta_{3D\text{Ising}} = 0.036298$ apply when the order parameter is the *composite* operator $\theta = \Box S$ rather than a fundamental field?  (Dynamical universality class assignment under Hubble friction is the right framework — Model A vs B vs C is not yet pinned down.)
- [ ] Is the post-transition FLRW background's spatial isotropy compatible with a residual preferred direction $\hat\ell$ that would source $f_{NL}^{(2)}$ at observable scales today?  (If $\hat\ell$ is averaged out by post-transition equilibration, the anisotropic signature is suppressed.)
- [ ] What is the actual reheating temperature implied by the stiff-matter → radiation transition?  (Flagged W4 in `cnsc_internal_review.py` but never quantified.)

## Key Outputs Registry

| Type | File | Description |
|---|---|---|
| Figure | `outputs/figures/fNL_spectrum_reproduction.png` | DBI $f_{NL}(k)$ reproduced with Planck/Euclid overlays |
| Figure | `outputs/figures/ns_eta_band.png` | CNSC $n_s$ on Planck 2018 $1\sigma$ band |
| Figure | `outputs/figures/r_prediction_inconsistency.png` | Visualizes the four-value $r$ disagreement |
| Figure | `outputs/figures/anisotropic_fNL_template.png` | New falsifier: $f_{NL}^{(2)}$ quadrupolar shape |
| Data   | `outputs/verification/audit.json` | Machine-readable audit results |
| Code   | `outputs/verification/verify_cnsc_predictions.py` | Reproduction driver |
| Code   | `outputs/verification/anisotropic_fNL_template.py` | New-signature generator |

## Docs Registry

| File | Purpose | Created | Last Updated |
|---|---|---|---|
| `docs/PROJECT_STATUS.md` | Project overview | 2026-05-13 | 2026-05-13 |
| `docs/CNSC_Verification_Audit_2026.md` | Full audit results + 6 prioritized actions | 2026-05-13 | 2026-05-13 |
| `docs/CNSC_Null_Geometry_Unique_Signature.md` | Defense against stiff-matter reduction critique, anisotropic $f_{NL}^{(2)}$ derivation | 2026-05-13 | 2026-05-13 |
| `docs/CNSC_Axiom_Derivation_Map.md` | T1/T2/T3 classification of every numerical claim; backbone of the axiomatic paper rewrite | 2026-05-13 | 2026-05-13 |
| `docs/CNSC_eta_to_ns_mapping.md` | Class II — $n_s = 1 - \eta$ derivation from Ising fixed point; lists 5 confirmation datasets (D1-D5) | 2026-05-13 | 2026-05-13 |
| `docs/CNSC_Dynamical_Universality_Model_A.md` | Class II — Model A justification + Q3 hedge for Model B; lists 4 data programs (D6-D9) | 2026-05-13 | 2026-05-13 |
| `docs/CNSC_Honest_Disclosure_Block.md` | Class II — 6 T2.x assumption-to-data map + Planck anomaly connection; paper §IX.E source | 2026-05-13 | 2026-05-13 |

## Pivot Record

### Pivot 1 — 2026-05-13: CNSC paper-form abandoned; framework v2 started

- **Reason**: 7-weakness derivation program (`docs/derivations/01-08`) found *all* of CNSC's novel quantitative content is *not mathematically derivable* from the stated assumptions.  $\gamma(k)$ envelope (weakness 1), Mukhanov-Sasaki analogue (weakness 2), $r$ formula (weakness 3), $S_{\text{crit}}$ origin (weakness 4), photon → cosmology leap (weakness 5), null dynamics well-posedness (weakness 6, partial only under restriction), Z₂ LG microscopic origin (weakness 7) — all returned negative or cascade-negative.
- **User decision**: the user explicitly accepted the mathematical verdict — *"이론이 무너지는 것도 수학적으로 타당하다면 그렇게 되어야 하는거야"* — and chose to redirect rather than retrofit.
- **What changed**:
  - CNSC paper drafts (PRD + JCAP English/Korean LaTeX + PDFs) → `archive_cnsc_paper_2026-05-13/paper_drafts/`
  - 47 supporting markdown docs + 6 docs/CNSC_*.md → `archive_cnsc_paper_2026-05-13/supporting_docs/`
  - 15 paper-specific Python scripts → `archive_cnsc_paper_2026-05-13/python_code/`
  - 17 paper figures → `archive_cnsc_paper_2026-05-13/figures/`
  - 15 LaTeX build artifacts → `archive_cnsc_paper_2026-05-13/latex_build/`
  - New direction outline started: `framework_v2/` (4 docs: foundations, coherence-VSL seed, open questions, methodology)
- **Carry-forward**:
  - 4 surviving intuitions (F1-F4) from CNSC are foundations of framework v2.
  - The user's path-integral coherence VSL insight, developed during the inquiry, is the novel seed of framework v2.
  - The *axiomatic + honest-derive methodology* developed during the CNSC inquiry is codified as framework v2's working method (`framework_v2/03_methodology.md`).
- **Archive status**: all CNSC paper-form files are *read-only reference*.  Not to be modified.  The new framework v2 starts fresh from the surviving foundations.
