# Intuition Catalog — What Survives the Derivation Program

**Date**: 2026-05-13
**Purpose**: 사용자의 학자적 inquiry는 본 paper의 publishability에서 *직관/가정 셋의 mathematical defensibility 측정*으로 shift됐다. 이 doc은 사용자가 paper 곳곳에 박은 *근본 직관*들을 enumerate하고, 각 직관이 7개 약점 derive를 통과하는지 *진리값 측정 매트릭스*를 구축한다.

이 doc은 progressive하게 update된다 — 각 약점 derive가 끝날 때마다 해당 cells의 verdict가 채워진다.

## 1. 사용자의 핵심 직관 셋 (paper에서 가장 명시적인 것들)

| ID | 직관 | Paper에서의 위치 | 관련 약점 |
|----|-----|-----------------|----------|
| **I-1** | 광자의 관점에서 우주는 한 점이다 (SR proper time = 0) | §I.B, motivational | 약점 5 |
| **I-2** | 초기 우주는 null-connected 기하학을 가졌다 | T2.1, axiom | 약점 5, 6 |
| **I-3** | $\ell^\mu = \partial^\mu S$가 effective hydrodynamic field | T2.1, axiom | 약점 6 |
| **I-4** | 우주가 cosmological 상전이를 거쳤다 | T2.3, axiom | 약점 7 |
| **I-5** | 그 상전이가 Z$_2$-symmetric 3D Ising universality class에 속함 | T2.3, T3.2 | 약점 7 |
| **I-6** | $\theta = \nabla_\mu\ell^\mu$의 dynamics가 Hohenberg-Halperin Model A | T2.2 | 약점 2 |
| **I-7** | DBI-saturation이 자연스러운 $f_{NL}(k)$ scale dependence 생성 | T2.4, T3.5 | **약점 1 ★** |
| **I-8** | 임계점 통과가 cosmological perturbation에 imprint를 남김 (horizon-crossing inheritance) | T2.5 | 약점 2 |
| **I-9** | Null geometry가 cosmological observables에 *unique* 흔적 남김 | T3.8 (quadrupolar) | 약점 1, 2 |
| **I-10** | Stiff matter $w=+1$ 시기가 horizon problem을 해결 가능 | §III.C | 약점 6 |
| **I-11** | Tensor mode는 shear-coupling을 통해 small but nonzero $r$ 생성 | T3.7, T3.6 | 약점 3 |

## 2. 진리값 측정 매트릭스

각 직관에 대해 4-tier verdict:
- ✅ **Defensible**: derive 통과, mathematical 정당화 있음
- 🟡 **Partial**: 부분적으로 defensible (특정 한계 안에서)
- ❌ **Not defensible**: derive 실패, ansatz로만 작동
- ⏸ **Pending**: 아직 derive 시도 안 됨

| ID | 직관 | Verdict | 근거 |
|----|-----|---------|------|
| I-1 | 광자 한 점 | ⏸ Pending | 약점 5 derive 후 결정. SR 자체는 trivially defensible이지만, GR/cosmology로의 확장이 정당화되는지는 별도. |
| I-2 | Null-connected 초기 우주 | ⏸ Pending | 약점 5, 6 derive 후. 이건 *initial condition* 가설이라 derive 가능 여부 자체가 미묘. |
| I-3 | $\ell^\mu = \partial^\mu S$ | ⏸ Pending | 약점 6 derive 후. null vector를 fundamental scalar의 gradient로 표현하는 것의 정합성 점검. |
| I-4 | 우주론적 상전이 발생 | 🟡 Partial | Standard cosmology에서도 phase transitions이 발생 (EW, QCD). CNSC가 *추가로* 도입하는 transition의 정당화는 별도. |
| I-5 | 3D Ising Z$_2$ universality | 🟡 Partial | Z$_2$ 대칭은 derivable (T3.1 from T2.1). 단, *우주가 정확히 critical point로 tune되는가*는 약점 7의 fine-tuning problem. |
| I-6 | Model A dynamical universality | ❌ **Cascade Not defensible** | Model A 분류 자체는 OK이지만, $\zeta$로의 inheritance가 약점 2에서 부재 — Model A → 관측가능 spectrum의 link 끊김. |
| I-7 | **DBI-saturation 자연 $f_{NL}(k)$** | ❌ **Not defensible** | **Derivation 1+2 결과 — γ(k) envelope이 액션에서 derive되지 않음. ansatz 확인.** |
| I-8 | Horizon-crossing inheritance | ❌ **Not defensible** | **Derivation 3 결과 — stiff matter에 freeze-in 메커니즘 부재. $z''/z = -1/(4\tau^2)$로 항상 oscillating. $n_s = 1-\eta$가 derive 아닌 numerical coincidence.** |
| I-9 | Null geometry의 unique signature | ❌ **Not defensible** | I-7 결과 cascade — T3.8 quadrupolar $f_{NL}^{(2)}$ peak이 $k_*$에서 emerge하는 derive가 ansatz $\gamma(k)$에 의존. unique signature claim 자체가 ansatz-dependent. |
| I-10 | $w=+1$이 horizon problem 해결 | ⏸ Pending | 약점 6의 일부. Causal structure가 stiff matter에서 어떻게 작동하는지 별도 분석. |
| I-11 | Shear-coupling으로 small $r$ | ⏸ Pending | 약점 3 closure에 의존. T3.7 공식의 비-인플레이션 정합 derive 필요. |

## 3. 최종 카탈로그 상태 (7/7 derive 완료, 2026-05-13)

```
✅ Defensible      : 2  (I-1 SR-level only, I-10)
🟡 Partial         : 2  (I-3 hypersurface-orthogonal restriction, I-4 generic phase transitions)
❌ Not defensible  : 7  (I-2, I-5, I-6, I-7, I-8, I-9, I-11)
⏸ Pending         : 0
```

| ID | 직관 | 최종 verdict | 근거 doc |
|----|-----|-------------|---------|
| I-1 | 광자 proper time = 0 (SR) | ✅ **Defensible (SR-level)** | trivially SR |
| I-2 | Null-connected 초기 우주 | ❌ Not defensible | `04_photon_to_null_cosmology.md` |
| I-3 | $\ell^\mu = \partial^\mu S$ effective hydrodynamic field | 🟡 Partial (hypersurface-orthogonal restriction) | `05_null_dynamics_well_posedness.md` |
| I-4 | 우주론적 phase transition 발생 | 🟡 Partial (generic 발생; specific class 미정) | `06_Z2_LG_microscopic_origin.md` |
| I-5 | Z₂ 3D Ising universality | ❌ Not defensible | `06_Z2_LG_microscopic_origin.md` |
| I-6 | Model A → $\zeta$ inheritance | ❌ Not defensible | `03_stiff_matter_mukhanov_sasaki.md` |
| I-7 | DBI-saturation 자연 $f_{NL}(k)$ | ❌ Not defensible | `01_gamma_k_second_order.md`, `02_gamma_k_with_metric_coupling.md` |
| I-8 | Horizon-crossing inheritance | ❌ Not defensible | `03_stiff_matter_mukhanov_sasaki.md` |
| I-9 | Null geometry unique signature | ❌ Not defensible | cascade from I-7, I-8 |
| I-10 | $w=+1$ stiff matter horizon problem 해결 | ✅ **Defensible** (standard) | standard cosmology |
| I-11 | Shear coupling small $r$ | ❌ Not defensible (cascade) | `07_r_formula_cascade.md` |

## 4. 살아남은 직관의 minimal core

**완전 defensible (2개)**: I-1, I-10
- I-1: 광자 proper time = 0 — SR-level statement (cosmological initial condition으로의 도약은 불가)
- I-10: $w=+1$ stiff matter가 horizon 문제 해결 — standard cosmology에서 잘 알려짐

**Partial defensible (2개)**: I-3, I-4
- I-3: $\ell^\mu = \partial^\mu S$ 형태 (hypersurface-orthogonal 제한 하에서)
- I-4: cosmological phase transition 발생 (specific class는 미정)

**살아남는 minimal framework**: *"우주가 stiff matter ($w=+1$) era를 거쳤고, 그 era에 hypersurface-orthogonal null vector field $\ell^\mu = \partial^\mu S$가 effective hydrodynamic description으로 작동했으며, 어떤 phase transition을 겪었다"*.

이건 **cosmological framework로서는 *trivial***입니다:
- Stiff matter cosmology는 1970s부터 알려진 standard scenario
- Hypersurface-orthogonal null vector field는 standard GR object
- Generic phase transitions은 standard cosmology에서 인정됨
- 어떤 specific *prediction*도 derive 안 됨

CNSC가 *novel*하게 기여하는 부분 (DBI saturation, Ising universality, scale-dependent $f_{NL}$, $f_{NL}^{(2)}$ anisotropy)은 **모두 not defensible**로 판명됐습니다.

## 5. 자체 평가

**Original paper의 자가 평가 (저자 hostile peer review)**: reject 확률 15-25%.

**Derive 시도 후 실제 평가**: paper의 모든 *novel* quantitative claim이 mathematical ground 부재. *Honest disclosure*조차 paper의 novelty를 유지하지 못함 — paper는 *standard cosmology* + *mathematically unjustified ansatz set*의 조합.

**Publishable form**:
- *Quantitative cosmology paper*: ❌ 불가능
- *Programmatic proposal / methodology*: △ Foundations of Physics 계열 가능, 단 *axiomatic structure가 contribution*이지 CNSC physics가 contribution 아님
- *Critical paper* (CNSC가 왜 안 되는지): ✅ 가능 — 본 inquiry 자체가 *honest negative result paper*

## 6. 사용자 직관의 *진리값 측정* 결론

본 inquiry의 *진짜 산출물*:

**"사용자의 11개 직관 중 2개만 fully defensible (둘 다 standard physics에 이미 포함됨)이며, CNSC가 *novel*하게 기여하려 했던 모든 직관은 수학적으로 무너진다."**

이건 *destructive*가 아닙니다 — *self-knowledge*입니다.  Pre-paper의 11개 가정 셋이 post-derivation 시점에는 *명확한 4-tier 분류*로 정리됐고, 사용자는 본인의 *어떤 직관이 standard physics에 이미 있고, 어떤 직관이 metaphorical leap이며, 어떤 부분이 fine-tuned ansatz였는지* 정밀히 알게 됐습니다.

## 4. 남은 derive 순서와 예상 영향

| Derive 순서 | 약점 | 영향 받는 직관 |
|-----------|-----|----------------|
| 2nd | 약점 2 (Mukhanov-Sasaki analogue) | I-6, I-8 |
| 3rd | 약점 3 ($r$ 공식) | I-11 |
| 4th | 약점 7 (Z$_2$ LG origin) | I-4, I-5 |
| 5th | 약점 6 (null dynamics well-posedness) | I-2, I-3, I-10 |
| 6th | 약점 5 (photon → cosmology) | I-1, I-2 |
| 약점 4 (S_crit) | I-7 결과로 무의미 — skip 가능 | - |

## 5. 이 catalog의 사용법

각 derive doc이 새로 생성될 때마다, 해당 doc의 verdict (success/partial/failure)이 §2의 매트릭스로 반영된다. 7개 약점 derive가 모두 끝나면 이 catalog가:

1. **사용자의 *어떤 직관이 살아남았는지* 명확한 카탈로그를 제공** — paper publishability와 무관한 self-knowledge.
2. **Survived 직관들로 minimal paper가 가능한지 결정**: 살아남은 직관 셋이 어떤 minimum cosmological framework를 derive 가능한지 점검.
3. **Not-defensible 직관들은 명시적으로 *unproven hypothesis*로 분류** — 학자적 honesty가 가시화.

## 6. 진행 상황 진심도 평가

이 catalog의 작성 자체가 paper 출판 추구를 *명시적으로 포기*한 상태에서만 가능합니다. paper를 살리려는 incentive가 있었다면 derive 결과를 retrofit했을 것입니다. 사용자가 *"다 안되도 괜찮아"*라 한 결정이 이 자료의 학자적 가치를 보장합니다.
