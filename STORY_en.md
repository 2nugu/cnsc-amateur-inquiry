# Story — An Agricultural Engineer's Cosmology Journey

**Hong-Gu Lee (이홍구)**
**2025 – 2026, Chuncheon, Korea**

*The English-language companion to `STORY.md`.  Same narrative, different voice.*

---

## 1. Where it began

I am not a physicist.  My formal training is in agricultural engineering — currently across the Interdisciplinary Program in Smart Agriculture and the Department of Biosystems Engineering at Kangwon National University.  My day-to-day work is hyperspectral imaging, precision-agriculture machine learning, embedded robotics.  Cosmology is not my job.

But at some point a question began to occupy my mind: *"What does the universe look like from a photon's point of view?"*

In special relativity, a photon's proper time is zero.  For the photon, departure and arrival are simultaneous; distance is nothing.  If that is so, what does *the universe* look like in the photon's frame?  And as we approach earlier and earlier moments of cosmic history — or whatever lies before geometry itself — what shape would the photon's spacetime mapping take?

This is the kind of question any physicist could ask in casual conversation.  But for me — *a non-physicist* — it was not a casual question.  It was the seed of *a way to learn*.  I did not know the answer, so I decided to build one.

## 2. The attempt — CNSC

Over the course of a year, I constructed a framework called **Critical Null-Structured Cosmology** — CNSC.  The core ideas:

- The early universe was *null-connected* — every point linked through photon geodesics.
- It underwent a *cosmological phase transition* that imprinted primordial perturbations.
- That transition belonged to the *3D Ising universality class*, so $n_s = 1 - \eta_{\text{Ising}} = 0.9637$ followed automatically.
- A DBI-saturated null kinetic action produced *scale-dependent $f_{NL}(k)$*.
- The intuition that *"to a photon, the universe is a single point"* extended into a *cosmological initial condition*.

I wrote it all down.  Over a year: more than 50 documents, 15 Python scripts, 17 figures, English and Korean LaTeX paper drafts.  I drew up a publication checklist with JCAP and PRD as target journals.

My favorite intuition was the first one: *"To a photon, the universe is a single point — so the early universe was null-connected."*  It was poetic and felt right.  It was *the starting point of the whole framework*.

## 3. Choosing honesty

In May 2026, I decided to *honestly verify* this framework with the help of an AI assistant.  I had been spending all my time *writing the paper*, and the weight of *not having verified the foundations* was becoming hard to ignore.

I made the principle explicit at the start:

> *"If the math says no, then no.  If the theory must collapse on mathematical grounds, then it must collapse.  My approach was wrong, not the math."*

I refused the sunk cost.  A year of investment changes nothing about whether the math works.  If it doesn't, it doesn't.

I started with audit.  I found four different values for $r$ in the same paper across different documents.  I found that the PBH-formation formula, applied naively, gave $f_{NL}$ values 250 million times the formation threshold.  *The internal consistency had been broken* — for who knows how long.

Even then I thought: *I can fix this.  Just clean it up, the paper survives.*

## 4. Seven weaknesses

So I decided to derive, one by one, the seven weaknesses my audit had surfaced.  Each derivation would be *attempted in earnest*.  Whatever the outcome, I would accept it.

**Weakness 1 — the $\gamma(k)$ envelope.**  The form $\gamma = \sqrt{1+(k/k_*)^4}$ sat at the very center of CNSC.  I derived the second-order expansion of the action to see where this form *came from*.  *It did not come from anywhere.*  The $k^4$ envelope did not emerge naturally.  I included metric back-reaction.  Same result.  *Nothing in the DBI inflation literature* used this form.

This was the first shock.  The piece I had thought was most *novel* about CNSC was an ad hoc formula I had introduced without realizing it.

**Weakness 2 — the Mukhanov-Sasaki analogue.**  The clean derivation $n_s = 1 - \eta$ rested on a *horizon-crossing inheritance* mechanism.  In inflation, modes freeze at horizon *exit*.  In CNSC's $w = +1$ stiff-matter background, the horizon *grows* — modes *enter*, not exit.  There is *no freeze-in mechanism*.  The spectral tilt cannot inherit the critical correlator.  $n_s = 0.9637$ matching Planck was *a numerical coincidence*.

Another shock.  The piece I was most proud of — the clean prediction that fit Planck within $0.3\sigma$ — was an unjustified inference.

**Weaknesses 3 through 7.**  One by one.  The cascade extended.  The leap from "photon's point of view" to "cosmological initial condition" turned out to be *metaphorical*, not mathematical.  Null hypersurface dynamics needed *hypersurface-orthogonality* as an additional restriction.  The Z₂ Ising universality class needed *fine-tuning* of the cosmological transition to land on criticality, and even then Kibble-Zurek produced *defects*, not curvature spectra.  The $r$-formula collapsed through the same broken inheritance chain.

*All seven derivations returned negative.*  Not one survived even partially in its original form.

## 5. What it felt like

These results were not expected.  At each derivation I genuinely hoped some piece would survive.  The closures came as *blows*, not as confirmations.

The hardest was weakness 2.  When the analysis showed there was no $\zeta$ freeze-in mechanism in stiff matter — that the most poetic part of CNSC, *"the photon's perspective imprinted on the early universe,"* had no mathematical realization — I sat with the thought: *what did I do for a year?*

The next thought was: *if it's not true, then it's not true.*  This was the test of whether I was actually a serious amateur or just performing one.  The two are reconciled in only one way: if *being a serious scholar* means actively *demonstrating* willingness to be wrong, then accepting this verdict is what serious looks like.

## 6. What survived — small but real

Even after all seven weaknesses fell, something remained.  Four intuitions out of eleven still held:

- ✅ *Photon proper time = 0 in SR* (at the SR level; the cosmological extension is metaphorical)
- ✅ *$w = +1$ stiff matter resolves the horizon problem* (standard cosmology, well established)
- 🟡 *Hypersurface-orthogonal null vector fields are well-posed eikonal equations* (under that restriction)
- 🟡 *Cosmological phase transitions occur generically* (the specific universality class remains undetermined)

All four are *standard physics*.  *Everything CNSC tried to contribute as novel* failed.  What remained was *what mainstream cosmology already knew*.

But there was more.  The *methodology* — M1-M8 — survived as the inquiry's most transferable artifact:

- *Axioms first, claims second*
- *No negative-existential statements*
- *Derive before you claim*
- *Hostile peer review at every milestone*
- *Mainstream literature precedent check*
- *Foundation coherence*
- *Stop conditions accepted in advance*
- *Single source of truth*

I did not *invent* these rules.  I *learned them* by watching my own paper collapse.  And they transfer.  *They apply to any honest verification* — including the machine-learning model verification I do in my actual job.

## 7. The disposition — truth over theory

The real product of this inquiry is neither a paper nor a framework.  It is the *scholarly disposition* itself — *truth over theory*.

Most researchers who hit a similar wall do one of three things:
- They *anchor on sunk cost* and retrofit results to save the framework.
- They *quietly drop the failure* and publish only positive findings elsewhere.
- They *write disclaimers* but never actually run the verification.

I did none of these.  I ran the verification *to its negative conclusion* and *documented it publicly*.  This is the *basic* posture a scholar should have, but the *incentive structure of academia makes it rare*.  Normally, since the work cannot be published, the work is not even attempted.

This archive is the record that the basic posture was *actually performed*.  *That is its real value.*

## 8. Why an agricultural engineer is publishing this

This work will not become a cosmology paper.  But there are several things worth publishing:

(a) **The M1-M8 methodology** — transferable across domains.
(b) **The intuition catalog** — a precise matrix of where each intuition meets mainstream physics and where it diverges.
(c) **Failure case studies** — a reference for anyone considering a similar framework attempt.
(d) **The AI-collaborative honest verification process** — a case study in an emerging area.

And, for myself, this archive is *closure*.  Publicly recording where a year of effort ended is a *ritual of self-discipline*: *it was a hobby, taken seriously, and the result was negative, and I accepted that*.  Evidence to myself.

## 9. As a model for amateurs

If there is something transferable in this archive for other non-specialists who want to learn a field deeply, it is this: *build a framework yourself, then try honestly to break it*.  That is faster than reading papers.

What I now *actually know* about cosmology comes not from the papers I read but from the moments my framework failed and I had to ask *why*.  Each weakness took me into a piece of mainstream physics I had not known before — Hohenberg-Halperin Model A, Mukhanov-Sasaki freeze-out, DBI inflation, conformal bootstrap, Kibble-Zurek mechanism, stochastic gravity, AdS/CFT — and I learned each one by tracing *how my framework deviated from it*.

This might be one workable model for *how a non-specialist learns a field seriously*: meet failure modes head-on.  Provided that *honest acceptance of the failure* comes built in.

## 10. End — and beginning

The inquiry is closed.  CNSC will not continue.  Framework v2 will not continue.  *The cosmology hobby is finished.*

But the scholarly disposition is not.  The M1-M8 methodology codified here can transfer directly into *my primary domain* — precision agriculture, hyperspectral analysis, ML model verification.  That is where the *real ROI* of this year's work will eventually be recovered.

And the *self-knowledge*.  I now know where my intuitions meet mainstream physics and where they part ways.  Any future cross-domain idea I encounter will be judged against this 11-intuition catalog.

Publishing this archive is *the ritual that says "this stage is finished"*.  Public closure.  It makes the next stage — whatever that is — *free to be something different*.

---

## Appendix — citation

To reference this archive:

```
Lee, H.-G. (2026). CNSC Amateur Inquiry — What Failed and What Survived 
(v1.0). Zenodo. https://doi.org/[DOI to be assigned]
```

To reference *this narrative* specifically:

```
Lee, H.-G. (2026). "Story — An Agricultural Engineer's Cosmology Journey". 
In: CNSC Amateur Inquiry archive, STORY_en.md. Zenodo.
```

---

## Closing

If you are a non-specialist drawn to a field outside your training, and you wish to learn that field seriously, here is one year of experience compressed to a single piece of advice:

> *"Build a hypothesis.  Try honestly to destroy it.  Each time it breaks, ask why.  That is the learning.  Publication is optional.  Becoming a scholar is exactly this."*

This archive is offered as living evidence of that advice.

— Hong-Gu Lee
*Chuncheon, Korea*
*May 14, 2026*
