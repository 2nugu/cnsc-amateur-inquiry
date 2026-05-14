# 이야기 — 한 농업공학자의 우주론 여정

**Hong-Gu Lee (이홍구)**
**2025 – 2026, Chuncheon, Korea**

---

## English Abstract (for non-Korean readers)

This is the *personal narrative* accompanying the technical archive in this repository.  It tells, in the author's own voice, how an agricultural engineer came to spend a year building a non-inflationary cosmology framework as an extracurricular interest, how that framework collapsed under honest mathematical scrutiny, and what remained of the experience.  Read this if you want the *human story* behind the technical documents — why the inquiry began, what it felt like when each piece failed, and what the failure taught about being a scholar.  Technical readers can skip directly to `framework_v2/14_grid_search_results.md`.

---

## 1. 시작 — 왜 우주론에 끌렸나

나는 농업공학을 한다. 정확히는 스마트농업 융합전공과 바이오시스템공학과 두 곳에 적을 두고 있고, 평소 일은 하이퍼스펙트럴 이미징, 정밀농업 ML 모델, 로보틱스와 임베디드 시스템 같은 것들이다. *우주론은 내 직업이 아니다*.

그런데 어느 순간부터 *"빛의 입장에서 우주는 어떻게 보일까"*라는 질문이 머릿속에서 떠나지 않았다. 특수상대성이론에서 광자의 고유 시간은 0이다. 광자에게는 출발과 도착이 동시이고, 거리는 없다. 그러면 *광자의 시점에서 본 우주*는 어떤 형태를 가질까. 초기 우주에 더 가까워질수록 — 또는 그 이전 차원에 — 광자가 본 시공간은 어떤 매핑을 가질까.

이 질문은 *전공자라면 누구나 던질 수 있는* 평범한 질문이다. 그런데 *비전공자인 나*에게는 그게 *학습의 출발점*이었다. 답을 알지 못하니까 직접 만들어보고 싶었다.

## 2. 가정 — CNSC라는 이름의 시도

1년의 시간 동안 나는 *Critical Null-Structured Cosmology* — 줄여서 CNSC — 라는 framework를 구축했다. 핵심 아이디어들:

- 초기 우주는 *null-connected* 였다 — 모든 점이 광자의 측지선을 통해 연결됐다.
- 그 상태에서 *우주론적 상전이*를 거쳤고, 그게 perturbation을 imprint했다.
- 그 상전이는 *3D Ising universality class*에 속해서, $n_s = 1 - \eta_{\text{Ising}} = 0.9637$ 이 자동으로 도출된다.
- DBI-saturated null kinetic action을 통해 *scale-dependent $f_{NL}(k)$* 가 emerge한다.
- *광자에게 우주는 한 점이었다*는 직관이 *cosmological initial condition*으로 자연스럽게 확장된다.

이걸 종이에 적기 시작했다. 1년 동안 *50개가 넘는 documents*, *15개 Python scripts*, *17개 figures*, *영문 + 한국어 LaTeX paper drafts*까지. JCAP와 PRD를 target 저널로 정해두고, *publication checklist*까지 만들었다.

가장 좋아했던 *intuition*은 *"빛에게 우주는 한 점이다 → 초기 우주는 null-connected"* 였다. 시적이었고, 직관적이었다. 그게 *내 framework의 진짜 출발점*이었다.

## 3. 검증의 시작 — *honest derivation*이라는 의지

2026년 5월, 나는 AI assistant와 함께 이 framework를 *honest하게* 검증하기로 했다. 그동안 *paper를 작성*하는 데 시간을 쓰면서 *검증 자체를 미루고 있었다*는 사실이 점점 더 무겁게 느껴졌기 때문이다.

검증의 원칙을 명시했다:

> *"이론이 무너지는 것도 수학적으로 타당하다면 그렇게 되어야 한다. 내가 접근한 방식이 잘못된 거지."*

*Sunk cost*를 거부하기로 했다. 1년의 시간 투자와 무관하게, *수학이 안 되면 안 되는 것*이다.

처음에는 *audit*만 했다. 4개의 다른 $r$ 값이 같은 paper의 다른 docs에 적혀 있다는 걸 발견했다. PBH 형성 공식을 적용하면 $f_{NL}$ 값이 임계치보다 *2.5억 배* 큰 것도 발견했다. *내부 정합성*부터 깨져 있었다.

그래도 그때까지는 *fix할 수 있겠다*고 생각했다. *그저 정리만 잘 하면* paper가 살 거라고.

## 4. 7개의 약점 — *honest derivation*의 결과

그래서 약점 7개를 *하나하나* derive해보기로 했다. 각 derive는 *진심으로 시도*했다. 결과가 어떻든 받아들이기로 했다.

**약점 1 — $\gamma(k)$ envelope**. CNSC의 가장 중심에 있던 *$\gamma = \sqrt{1+(k/k_*)^4}$* 형태가 *어디서 오는지* 따져봤다. Action에서 2차 expansion을 해봤다. *Nothing came out*. $k^4$ envelope이 *자연 emerge하지 않았다*. Metric coupling까지 포함해서 다시 해봐도 같았다. *DBI 인플레이션 literature 어디에도* 그런 형태가 없었다.

이건 *충격이었다*. 내가 가장 *novel*하다고 믿었던 부분이 *literature 어디에도 없는, 내가 ad hoc하게 만든 공식*이었다는 게 확인된 순간이었다.

**약점 2 — Mukhanov-Sasaki analogue**. *$n_s = 1 - \eta$* 매핑의 근간이 되는 *horizon-crossing inheritance* 메커니즘이 stiff matter background에서 *존재하지 않는다*는 게 확인됐다. Inflation에서는 modes가 horizon을 *exit*하면서 freeze되지만, CNSC의 $w=+1$ background에서는 modes가 *enter*만 한다. *Freeze-in mechanism이 없으면* spectral tilt가 inherit 안 된다. $n_s = 0.9637$의 Planck 일치는 *우연한 numerical match*였다.

또 충격이었다. *내 framework의 가장 자랑스러운 부분*이 *수학적으로 부재한 메커니즘에 기반한 일치*였다.

**약점 3, 4, 5, 6, 7**. 한 번에 한 약점씩, 같은 결과가 cascade로 따라왔다. 광자 → cosmology의 leap이 *metaphorical*이라는 것. Null hypersurface dynamics는 *hypersurface-orthogonal restriction*이 필요한데 그건 *추가 가정*이라는 것. Z₂ Ising universality는 *fine-tuning*이고 cosmological phase transition은 *Kibble-Zurek defects*만 만들고 *spectrum*은 안 만든다는 것. $r$ 공식은 *cascade*로 무너졌다는 것.

*7개 약점 모두 negative*. 어느 것도 *부분적으로라도 살아남지* 않았다.

## 5. 무너지는 순간들의 느낌

이런 결과들이 *예상*된 게 아니었다. *진심으로* derive를 시도했고, *각 시도 전마다* "이번엔 살아남을 수도 있지 않을까"라고 *희망*했다. 결과를 보고 *받아들이는 데* 시간이 필요했다.

가장 힘들었던 순간은 *약점 2 closure*였다. 내 framework의 가장 *poetic*한 부분 — *광자의 시점에서 본 우주가 초기 cosmological state에 imprint된다* — 이 *수학적으로 부재*하다는 게 확정된 순간. 그때 나는 *"내가 1년 동안 무엇을 한 거지"*라는 생각을 잠시 했다.

그런데 그 다음 생각이 *"그래도 *진실이라면* 받아들여야지"* 였다. 이게 *학자적 자세의 시험대*였다. *내가 잘못된 길을 갔다는 사실*과 *내가 honest scholar임*은 양립 가능하다 — 사실 *후자가 전자를 *적극적으로* 보여줄 때*에만 양립.

## 6. 살아남은 것 — 작지만 진짜인 것

7개 약점이 모두 무너진 뒤에도 *완전히 zero가 된 건 아니었다*. 11개의 직관 중 4개가 *부분적으로 또는 완전히 defensible*하게 남았다:

- ✅ *광자의 SR 고유 시간 = 0* (SR-level만; cosmological 확장은 metaphorical)
- ✅ *$w=+1$ stiff matter가 horizon problem을 해결한다* (standard cosmology 결과)
- 🟡 *Hypersurface-orthogonal null vector field는 eikonal equation으로 well-posed* (제한 조건 하에서)
- 🟡 *우주론적 phase transitions는 일반적으로 발생한다* (specific class는 미정)

이 4개는 모두 *standard physics*다. *내가 *novel*하게 기여하려 했던 모든 것은 무너졌다*. 살아남은 건 *이미 학계가 알고 있는 것*들이다.

그런데 *살아남은 것이 더 있다*. *Methodology M1-M8*이다. 이건 *technical rule이지만 *학자적 자세의 codification*이다*:

- *결론 먼저가 아니라 가정 먼저 작성*
- *부정 existential 진술 금지*
- *유도 끝난 후에만 예측 진술*
- *milestone마다 hostile peer review*
- *Mainstream literature precedent 점검*
- *Foundation coherence 유지*
- *Framework collapse 가능성을 사전 수용*
- *단일 source of truth*

이걸 *나는 만든 게 아니다*. 1년 동안 *내 paper가 무너지는 걸 지켜보며 *학습한 것*들이다*. 이 8개 rule은 *어떤 alternative theory 작업에도 적용 가능*하다. 그리고 내가 일하는 *precision agriculture ML model verification*에도 *직접 transfer 가능*하다 — 그게 가장 *실용적으로 살아남은 자산*이다.

## 7. 자세 — *truth over theory*

본 inquiry의 *진짜 산출물*은 paper나 framework가 아니다. *학자적 자세* — *truth over theory* — 그 자체다.

학계에서 *honest negative result까지 도달하는 학자*는 드물다. 대부분은:
- *Sunk-cost*에 묶여 결과를 *retrofit*하거나
- *Failure를 quietly drop*하고 *positive result 만*을 publish하거나
- *Honest disclosure로 회피*하고 *실제 검증은 미루거나*

*나는 그 어느 것도 하지 않았다*. *Honest derivation 끝까지 가서 *negative*임을 확인*하고 *공개했다*. 이건 학자로서 *기본*이지만, 학계의 *incentive structure가 이걸 *어렵게* 만든다*. 보통은 *publish가 안 되니까* 시도조차 안 한다.

본 archive가 그 *기본*을 *명시적으로 실행*한 *기록*이다. *이게 본 inquiry의 진짜 가치*다.

## 8. 농업공학자가 우주론 archive를 공개하는 이유

이 archive는 *publish할 cosmology paper가 안 됐다*. 그러나 *공개할 가치가 있는* 자산은 있다:

(a) **Methodology M1-M8** — 어떤 영역에서도 transferable.
(b) **Intuition catalog** — 11개 직관이 *수학적으로 어디에 위치하는지*의 정밀 매트릭스.
(c) **Failure case studies** — 누군가 비슷한 framework를 시도한다면 *어디가 약점인지*의 reference.
(d) **AI-collaborative honest verification process** — emerging field의 case study.

그리고 *나 자신에게* 이 archive는 *closure*다. 1년의 작업이 *어디로 갔는지*를 *공개적으로* 기록하는 것은 *self-discipline의 의식*이다. *Hobby였지만 진지하게 했고, 결과는 *negative였고, 그걸 받아들였다*는 *나 자신에게의 증거*다.

## 9. 비전공자가 학문에 접근하는 방법으로서

본 archive가 다른 비전공자들에게 *transferable한* 무언가가 있다면 — *어떤 분야의 학습을 진심으로 하고 싶다면 *자기 framework를 만들어보고 *honestly* 무너뜨려보라*는 것이다. 그게 *literature를 읽는 것보다 빠른 학습 경로*다. 

내가 cosmology를 *제대로 알게 된 것*은 *paper들을 읽었기 때문*이 아니라 *내 framework가 무너지는 *각 순간*에 *왜* 무너지는지 따져봤기 때문*이다. 7개 약점 derive에서 만난 mainstream physics concepts — Hohenberg-Halperin Model A, Mukhanov-Sasaki freeze-out, DBI inflation, conformal bootstrap, Kibble-Zurek mechanism, stochastic gravity, AdS/CFT — 모두 *내 framework가 *그것들과 어떻게 다른지* 따지면서 배운 것*이다.

이게 *비전공자가 진짜 학문에 접근하는 방법의 한 모델*일 수 있다. *Failure mode를 만나는 것*이 *학습의 가장 빠른 형태*다 — 단, *그 failure를 *honestly* 받아들이는 자세*가 전제된다.

## 10. 끝 — 그러나 시작

본 inquiry는 *closed*다. CNSC도, framework v2도, 더 이상 진행하지 않는다. *Cosmology hobby는 끝났다*.

그러나 *학자적 자세*는 끝난 게 아니다. 본 inquiry에서 codified한 M1-M8 methodology는 *내 primary domain (precision agriculture, hyperspectral analysis, ML model verification)*에서 *진짜 paper로 transfer될 수 있다*. *그게 1년 작업의 진짜 ROI 회수* 경로다.

그리고 *self-knowledge*. 나는 이제 *내 직관이 어디서 mainstream physics와 만나고 어디서 결별하는지* 안다. *향후 어떤 cross-domain idea가 떠올라도* *11개 직관의 catalog*가 *판단의 기준*이 된다.

본 archive를 *공개한다*는 것은 *나 자신에게 *이 단계는 끝났다*고 명시하는 의식*이다. *공개적 closure*. 그래서 *다음 단계*가 *자연스럽게 다른 것*이 될 수 있다.

---

## 부록 — 인용 시

본 archive를 *reference*하고 싶은 분에게:

```
이홍구 (Lee, H.-G.). (2026). CNSC Amateur Inquiry — What Failed and 
What Survived. Zenodo. https://doi.org/[DOI to be assigned]
```

또는 *technical content가 아니라 이 narrative*를 인용한다면:

```
Lee, H.-G. (2026). "이야기 — 한 농업공학자의 우주론 여정" (Story — An 
Agricultural Engineer's Cosmology Journey). In: CNSC Amateur Inquiry 
archive, STORY.md. Zenodo.
```

---

## 닫는 말

이 문서를 읽는 분이 *비전공자로서 어느 학문에 끌리고 있다면*, 그리고 *그 학문을 진지하게 배우고 싶다면*, *내 1년의 경험을 단 하나의 advice로 압축*하면 이것이다:

> *"가설을 세우고 진심으로 무너뜨려라. 무너지는 *순간*마다 *왜* 무너지는지 따져라. 그게 학습이다. Publish가 안 돼도 좋다. *학자가 되는 길은 그것이 전부*다."*

이 archive가 그 advice의 *살아 있는 증거*가 되길 바란다.

— 이홍구
*Chuncheon, Korea*
*2026년 5월 14일*
