# Chronology Realizability / Counterexample Audit

**Status:** second-phase chronology side branch.

This note continues, but does not replace:

- notes/chronology-protection-principal-safety.md
- src/symbolic/chronology_misner_principal_gate.py

Status labels:

- **PUBLISHED RESULT**
- **REPRODUCED HERE**
- **SYNTHESIS / CRITERION**
- **COUNTEREXAMPLE CANDIDATE**
- **OPEN**

The target is not whether a metric can contain CTCs. The target is the stronger
**chronology realizability chain**:

\[
\boxed{
\begin{aligned}
&\text{regular admissible initial data}\\
&\to \text{predictively determined evolution}\\
&\to \text{quantum-admissible chronology horizon}\\
&\to \text{operationally traversable CTC region}.
\end{aligned}}
\]

A model counts as an operational time machine here only if a physical
excitation beginning in a regular chronal region is carried by the theory's
predictive dynamics into a CTC region and can complete a closed timelike
history, without the result depending on an arbitrary post-Cauchy-horizon
extension, a singular barrier, an uncontrolled strong-coupling regime, or an
undefined quantum state.

---

# 1. Executive result

The targeted literature audit did **not** identify a demonstrated operational
time machine satisfying the full realizability chain.

This is a literature result, not a no-go theorem.

The main pruning is:

\[
\boxed{
\text{chronology-horizon formation}
\neq
\text{predictive formation of a CTC phase}.
}
\]

That distinction is not new. It is explicit in Ori 2007 and is the standard
mathematical role of a Cauchy horizon: the unique maximal globally hyperbolic
development (MGHD) is determined by the initial data, while an extension
beyond a Cauchy horizon is outside ordinary Cauchy predictivity.

Ori 2007 strongly narrows the gap by constructing regular initial data for
which the Cauchy horizon contains closed null generators and by imposing the
additional condition that **any smooth extension across a suitable horizon
portion contains nearby CTCs**. But the extension itself is not uniquely
selected by the initial data; the pseudo-Schwarzschild core explicitly admits
two non-equivalent analytic extensions.

Xavier 2026 is even more explicit: the initial data determine the **onset of
causality violation**, not the CTC region beyond the horizon. Moreover, the
traveling wave must be supported by an external source that the preprint does
not specify, and the matching/evolution of that support to an asymptotically
flat exterior is outside its scope.

The best quantum counterexample candidate remains the exact heterotic
Taub--NUT CFT family. It has:

- a full worldsheet CFT definition;
- geometry exact to all orders in \(\alpha'\);
- surviving CTC regions;
- a later analysis of global extensions and test-particle motion;
- no simple \(\alpha'\)-driven excision of the chronology-violating sectors.

However, the audit did not identify a calculation demonstrating the stronger
operational chain with normalizable interacting physical string states
propagated from a chronal region through the chronology horizon and back along
a CTC, with target-space observables and string-loop effects under control.

Thus the present outcome is closest to:

\[
\boxed{
\textbf{Outcome C:}
\quad
\text{the exact heterotic CFT is a serious remaining candidate,}
}
\]

but the exact missing calculation is **physical string-state traversal and
interacting target-space consistency**, not another computation of the
\(\alpha'\)-corrected metric.

---

# 2. Three meanings of "time machine"

## 2.1 Geometry-level

\[
\boxed{
\exists\ \text{CTC in the mathematical spacetime}.
}
\]

This is common and not a realizability result.

## 2.2 Extension-level

\[
\boxed{
\text{a regular chronal region admits an extension containing CTCs}.
}
\]

This is stronger, but the extension may not be selected by initial data.

## 2.3 Operational-level

\[
\boxed{
\text{a physical excitation, under predictive dynamics, crosses into a CTC
region and returns to its causal past}.
}
\]

This is the target of the second-phase audit.

---

# 3. Prior-art kill matrix

The following universal claims should not be revived.

| Claim | Status | Reason |
|---|---|---|
| CTC onset requires local metric/principal-symbol singularity | KILLED | Misner gives a smooth flat chronology horizon |
| CTC formation universally requires WEC violation | KILLED | Ori-type non-compactly generated constructions evade this |
| Classical PDEs on CTC backgrounds are automatically inconsistent | KILLED | restricted free-field existence/uniqueness results exist |
| Renormalized stress tensor must numerically diverge on every approach | KILLED | finite/vanishing chronal-side examples exist; KRW is sharper |
| Quantum theory is logically impossible with CTCs | KILLED | Deutsch/Hartle-type generalized frameworks exist |
| Free quantum fields on CTC backgrounds are always nonunitary | KILLED | free-field unitary scattering exists on restricted classes |
| UV completion removes every CTC geometry | KILLED | exact heterotic CFT examples retain CTC regions |
| Surviving string-theory CTC geometry implies traversability | NOT ESTABLISHED | protecting/inaccessible examples exist |

The surviving question is therefore not geometric existence. It is predictive,
quantum-admissible, interacting, operational realization.

---

# 4. Ori 2007 audit

Primary source:

A. Ori,
*Formation of closed timelike curves in a composite vacuum/dust
asymptotically-flat spacetime*,
Phys. Rev. D **76**, 044002 (2007),
arXiv:gr-qc/0701024.

## 4.1 What the initial data determine

**PUBLISHED RESULT.**

Ori constructs a regular, asymptotically flat, topologically trivial spacelike
initial hypersurface with:

- a compact vacuum core;
- a positive-density dust envelope;
- an exterior vacuum region;
- weak, dominant, and strong energy conditions satisfied;
- a well-posed Einstein--dust initial-value system.

The predictable part is explicitly organized using domains of dependence.

Ori also states the central logical difficulty directly:

\[
\boxed{
\text{if CTCs form, they lie outside }D^+(S).
}
\]

He therefore does **not** identify post-horizon CTCs with ordinary Cauchy
evolution.

## 4.2 Ori's replacement criterion

Ori proposes three causal criteria:

1. \(H^+(S)\) contains closed null geodesics;
2. an analytic extension beyond a suitable horizon portion contains CTCs
   immediately beyond it;
3. **any smooth extension** beyond that portion contains nearby CTCs.

The model is constructed to satisfy all three.

This is much stronger than merely displaying one convenient CTC extension.

It still does not make the extension part of the MGHD.

## 4.3 Nonuniqueness is explicit

The pseudo-Schwarzschild core is Misner-like. Ori states that it admits
**two non-equivalent analytic extensions** beyond the Cauchy horizon.

Therefore the implication

\[
\text{horizon onset}
\Rightarrow
\text{unique post-horizon spacetime}
\]

is false in this construction.

What is robust is a weaker statement: smooth extensions of the relevant
horizon neighborhood inherit chronology violation.

## 4.4 Traversability

The construction improves on an earlier Ori model by identifying a horizon
portion \(H_1\) whose chronal-side neighborhood is explicitly regular, thereby
removing a specific concern that a singularity elsewhere on the future
boundary might approach the closed null generator.

This makes classical crossing more plausible.

However, the paper does not establish:

- nonlinear stability of the chronology horizon;
- a quantum-admissible state across it;
- interacting QFT consistency;
- a UV completion;
- a predictive law selecting a unique post-horizon continuation.

## 4.5 Implication diagram

\[
\boxed{
\text{regular initial data}
\overset{\text{PROVED}}{\Longrightarrow}
\text{chronology-horizon onset}
}
\]

within the constructed Einstein--dust model.

\[
\boxed{
\text{chronology-horizon onset}
\overset{\text{FALSE}}{\Longrightarrow}
\text{unique CTC extension}.
}
\]

There are non-equivalent extensions.

A weaker arrow is:

\[
\boxed{
\text{chronology-horizon onset}
\overset{\text{CONSTRUCTED BUT NONUNIQUE}}{\Longrightarrow}
\text{nearby CTCs in every smooth extension}
}
\]

for the relevant horizon portion.

Finally,

\[
\boxed{
\text{CTC extension}
\overset{\text{OPEN}}{\Longrightarrow}
\text{operational quantum time machine}.
}
\]

## 4.6 Audit verdict

Ori 2007 is a strong **extension-level** time-machine construction.

It is not an operational counterexample to the predictive-realizability gate.

---

# 5. Xavier 2026 vacuum traveling-wave audit

Primary source:

S. Xavier,
*Closed Timelike Curves from a Vacuum Traveling Wave*,
arXiv:2607.00788 (2026).

**Status:** recent preprint; treat independently and cautiously.

## 5.1 Exact core result

The vacuum core metric is

\[
ds^2
=
-2h(z,t)\,dt\,dz
+
[h(z,t)-f(x,y,z)]\,dz^2
+
dx^2+dy^2,
\]

with periodic \(z\).

The \(z\)-circles change causal character when

\[
g_{zz}=h-f
\]

changes sign.

The metric determinant is

\[
\det g=-h^2,
\]

so the chronology transition need not coincide with local metric
degeneracy.

## 5.2 What is and is not supplied dynamically

The preprint states that the traveling wave that drives the transition must
be supported by a source outside the vacuum core.

It then explicitly says:

- that source is not fixed;
- it is not identified with an established fundamental field;
- its evolution is outside the scope of the work;
- matching to an external asymptotically flat region is outside the scope.

Therefore the exact vacuum core solution is not, by itself, a complete
globally specified dynamical construction from a known matter theory.

## 5.3 The determinism statement is explicit

The paper states that CTCs cannot lie inside

\[
D^+(S_0).
\]

At most a closed null geodesic appears on

\[
H^+(S_0).
\]

Most importantly, it explicitly says:

\[
\boxed{
\text{the initial data determine the onset of causality violation,
not the CTC region beyond the horizon}.
}
\]

Thus the second-phase distinction is already acknowledged by the preprint.

## 5.4 Completeness and stability

For the generic parameter choice, the closed null generator is future
incomplete.

A special degenerate tuning removes the boost and makes the on-axis closed
null generator complete.

But even there:

- the full horizon remains non-compactly generated;
- finite \(\langle T_{ab}\rangle\) requires additional quantum-state
  assumptions;
- the stated stability condition is only marginally satisfied;
- classical/quantum stability remains open.

## 5.5 Implication diagram

For the **vacuum core alone**,

\[
\boxed{
\text{specified core data}
\overset{\text{PROVED}}{\Longrightarrow}
\text{chronology-horizon onset}.
}
\]

For the claimed **full asymptotically flat supported system**,

\[
\boxed{
\text{regular global physical data}
\overset{\text{MODEL ASSUMPTION}}{\Longrightarrow}
\text{the required traveling-wave evolution},
}
\]

because the source and matching are not supplied.

Beyond the horizon,

\[
\boxed{
\text{horizon onset}
\overset{\text{CONSTRUCTED BUT NONUNIQUE}}{\Longrightarrow}
\text{a regular CTC extension}.
}
\]

But

\[
\boxed{
\text{horizon onset}
\overset{\text{FALSE}}{\Longrightarrow}
\text{CTC region determined by the initial Cauchy data}.
}
\]

And

\[
\boxed{
\text{CTC extension}
\overset{\text{OPEN}}{\Longrightarrow}
\text{operational quantum time machine}.
}
\]

## 5.6 Audit verdict

Xavier 2026 is a useful exact **chronology-onset core model**.

It does not close the predictive-extension or quantum-realizability gaps.

---

# 6. The MGHD / Cauchy-horizon distinction is established prior art

**PUBLISHED RESULT.**

For Einstein initial data, the Choquet-Bruhat--Geroch theorem gives a unique
maximal globally hyperbolic Cauchy development.

Modern formulations, e.g. Sbierski, make this uniqueness explicit.

A Cauchy horizon is precisely the boundary beyond which the ordinary globally
hyperbolic Cauchy development no longer determines the spacetime.

Strong cosmic censorship is motivated by this loss of predictivity: it asks,
roughly and formulation-dependently, whether generic MGHDs are inextendible
with an appropriate regularity.

Therefore:

\[
\boxed{
\text{MGHD determined by initial data}
\neq
\text{arbitrary extension beyond a Cauchy horizon}.
}
\]

This is standard mathematical relativity and must not be presented as a new
chronology-protection insight.

It also means that a classical paper showing

\[
\text{regular data}\to H^+(S)
\]

has not, by that fact alone, shown

\[
\text{regular data}\to\text{unique CTC phase}.
\]

Ori's "any smooth extension contains CTCs" condition is best understood as a
strong attempt to make chronology violation robust despite this standard
nonuniqueness.

Strong cosmic censorship does not currently supply a universal chronology
no-go theorem. Its validity depends on matter model, asymptotics, and
regularity class, and extendible Cauchy horizons occur in important solution
families.

---

# 7. Exact heterotic Taub--NUT CFT audit

Primary sources:

C. V. Johnson, H. G. Svendsen,
*Exact string theory model of closed timelike curves and cosmological
singularities*,
Phys. Rev. D **70**, 126011 (2004),
arXiv:hep-th/0405141.

H. G. Svendsen,
*Exact geometry of a Kerr--Taub--NUT solution of string theory*,
Phys. Rev. D **71**, 044027 (2005),
arXiv:hep-th/0410011.

H. G. Svendsen,
*Global properties of an exact string theory solution in two and four
dimensions*,
Phys. Rev. D **73**, 064032 (2006),
arXiv:hep-th/0511289.

## 7.1 What is exact?

The Taub--NUT construction has a heterotic coset worldsheet CFT description.

The target-space fields analyzed in the 2004 work include the complete
\(\alpha'\) corrections obtainable from that exact CFT description.

The rotating Kerr--Taub--NUT extension likewise has an exact CFT
description and exact metric/dilaton analysis.

This does **not** mean that every target-space observable has been computed
nonperturbatively in the string coupling \(g_s\).

Thus:

\[
\boxed{
\text{exact in }\alpha'
\neq
\text{all-genus / all-}g_s\text{ solution of every observable}.
}
\]

## 7.2 Do CTC regions survive?

Yes at the geometry level.

The all-order \(\alpha'\) geometry retains the main Taub--NUT causal
structure, including NUT regions with CTCs.

Therefore:

\[
\boxed{
\text{UV/stringy }\alpha'\text{ completion}
\not\Rightarrow
\text{automatic removal of all CTC geometry}.
}
\]

## 7.3 Are the regions geometrically connected?

The follow-up global analysis studies analytic continuations and test-particle
motion and uses T-duality to reinterpret/resolve curvature-singular regions
of the exact solution.

This makes the example substantially stronger than a formal metric with an
obvious \(\alpha'\) barrier at the first chronology horizon.

However, point-particle geodesic accessibility is not the operational
criterion required here.

## 7.4 What has not been demonstrated

The targeted search did not identify a later calculation establishing all of:

1. a normalizable BRST-physical string wave packet initially localized in a
   chronal Taub region;
2. controlled propagation through the chronology horizon into the NUT/CTC
   region;
3. interacting string amplitudes or another target-space observable defining
   the traversal;
4. control of the relevant \(g_s\) / genus corrections;
5. completion of a closed timelike history and return to the causal past;
6. dynamical formation from regular chronal initial data rather than selection
   of an exact non-globally-hyperbolic background.

The original papers themselves present the physical interpretation of the CTC
regions cautiously.

## 7.5 Counterexample status

| Realizability link | Status |
|---|---|
| Exact fundamental background description | ESTABLISHED, in worldsheet-CFT / \(\alpha'\) sense |
| CTC geometry survives \(\alpha'\) corrections | ESTABLISHED |
| No immediate first-horizon \(\alpha'\) excision | ESTABLISHED |
| Classical/test-particle global analysis | PARTIAL |
| Normalizable physical string-state traversal | OPEN |
| Interacting target-space unitarity across chronology horizon | OPEN |
| Full \(g_s\) control | OPEN |
| Dynamical formation from regular chronal initial data | FAILS / NOT PROVIDED |
| Operational return to causal past | OPEN |

## 7.6 Audit verdict

This remains the most serious **COUNTEREXAMPLE CANDIDATE** found in the
second-phase search.

The open question is no longer whether the CTC geometry survives
\(\alpha'\).

It is:

\[
\boxed{
\text{Does the exact CFT contain a controlled physical string process that
operationally traverses the chronology-violating sector?}
}
\]

---

# 8. Misner string-orbifold audit

Primary sources:

M. Berkooz, B. Pioline, M. Rozali,
*Closed Strings in Misner Space: Cosmological Production of Winding Strings*,
arXiv:hep-th/0405126.

M. Berkooz, B. Durin, B. Pioline, D. Reichmann,
*Closed Strings in Misner Space: Stringy Fuzziness with a Twist*,
arXiv:hep-th/0407216.

## 8.1 Positive evidence

The fixed Misner orbifold has genuine string states in twisted sectors.

The spectrum includes:

- short strings winding the spacelike compact direction in Milne regions;
- long strings winding the timelike compact direction in the Rindler
  "whisker" regions.

So the existence of physical string sectors associated with timelike
compact directions is not merely a classical metric statement.

## 8.2 Obstructions

The same analyses exhibit:

- strong winding-string pair production;
- rates approaching unity at large winding;
- singularities in one-loop amplitudes;
- divergent tree amplitudes in some multi-string channels.

Therefore the model does not provide a uniformly weakly coupled,
interaction-controlled traversal experiment.

## 8.3 Realizability failure

More fundamentally, the Misner orbifold is selected as a fixed global
background. It is not obtained by predictive evolution from regular
asymptotically controlled chronal data.

Hence it fails the R1/R3 part of the operational chain before the string
scattering difficulties are even considered.

---

# 9. Interacting-QFT consistency audit

The literature distinguishes free fields sharply from interacting fields.

Friedman--Morris type results show that, on restricted CTC geometries, free
classical fields and free quantum scattering can be well behaved.

Friedman--Papastamatiou--Simon then show perturbative unitarity failure for
interacting fields in the class they analyze: the CTC-modified Feynman
propagator fails the identities required for an ordinary unitary perturbative
S-matrix.

This does not imply a logical contradiction in every possible quantum
framework. Hartle replaces ordinary state-vector evolution by a generalized
sum-over-histories quantum mechanics with consistent probability rules, but
the ordinary state on a spacelike slice is lost and causal structure is
modified.

Deutsch-type CTC quantum mechanics is another modified framework and likewise
does not preserve ordinary quantum-mechanical structure unchanged.

## 9.1 Framework comparison

| Framework | Ordinary unitarity | Locality / causal factorization | Predictive state evolution | CTC allowed | Dynamical gravity? |
|---|---|---|---|---|---|
| Restricted free QFT on fixed CTC spacetime | can hold asymptotically | modified by global geometry | restricted existence/uniqueness | yes | no |
| Perturbative interacting QFT of Friedman--Papastamatiou--Simon class | fails | causal propagator relations fail | ordinary S-matrix framework inconsistent | yes as background | no |
| Hartle generalized histories | ordinary unitary state evolution replaced | causality notion modified | histories probabilities replace state evolution | yes | background fixed |
| Deutsch CTC quantum mechanics | ordinary unitarity/correspondence modified | nonstandard | fixed-point prescription | yes | no |
| Exact heterotic CFT | worldsheet consistency established | target-space chronology nonstandard | operational target-space evolution not demonstrated | yes geometrically | background exact, not dynamically formed |
| Holographic time-machine model | boundary QFT controlled | bulk CTC sector dynamically inaccessible | chronal observables controlled | CTC sector exists | dual gravity included |

The pattern supports a useful but non-theorem statement:

\[
\boxed{
\text{known CTC-compatible quantum frameworks either modify ordinary
dynamics or fail to demonstrate gravitational realizability.}
}
\]

---

# 10. Holographic protection comparison

Primary sources:

R. Emparan, M. Tomašević,
*Holography of time machines*,
JHEP **03** (2022) 212,
arXiv:2107.14200.

R. Emparan, M. Tomašević,
*Quantum backreaction on chronology horizons*,
JHEP **02** (2022) 182,
arXiv:2109.03611.

This is a controlled negative result for operational traversability.

In the holographic construction:

- the boundary geometry develops a time-machine region;
- the dual bulk can remain regular;
- the bulk splits into disconnected CTC and non-CTC components;
- physical excitations cannot cross the chronology horizon.

With backreaction in the related analysis, the chronology horizon can instead
be replaced by a strong spacelike curvature singularity.

Thus:

\[
\boxed{
\text{CTC geometry in the description}
\neq
\text{physical access to the CTC sector}.
}
\]

The construction is model-specific, but it is an explicit realization of the
predictive-realizability gate by **decoupling/inaccessibility**, rather than by
a local principal-symbol singularity.

---

# 11. Adversarial R1--R9 audit

Statuses are descriptive only.

| Model | R1 regular chronal data | R2 asymptotic control | R3 CTC selected by dynamics | R4 perturbative control | R5 quantum states | R6 interacting consistency | R7 physical entry | R8 operational return | R9 UV/fundamental control |
|---|---|---|---|---|---|---|---|---|---|
| Ori 2007 | established | established classically | partial: horizon selected, extension not unique | open | open | open | partial classically | open | fails / classical GR+dust |
| Xavier 2026 | partial for full system | partial; external matching omitted | onset selected, CTC beyond horizon not Cauchy-determined | open | open | open | open | open | fails / classical GR core |
| Exact heterotic Taub--NUT | not supplied as IVP | exact background, \(g_s\) caveat | fails as dynamical-formation example | partial | partial / worldsheet CFT | open in target-space sense | open for physical string packet | open | established in \(\alpha'\) CFT sense |
| Misner string orbifold | fails / fixed orbifold | partial | fails | problematic | twisted states established | some amplitudes singular | partial fixed-background evidence | not demonstrated | perturbative string background |
| Holographic time machine | model background controlled | controlled in holographic regime | not an operational CTC evolution | controlled in model | established | interacting CFT controlled | **fails: disconnected** | fails | strong holographic control |

No row currently satisfies all R1--R9.

This is not evidence for a universal no-go by itself. It identifies where the
known examples fail.

---

# 12. Surviving candidate and exact remaining calculation

The exact heterotic Taub--NUT CFT is the surviving candidate that most directly
challenges a realizability-based chronology-protection criterion.

The next useful calculation is **not** another curvature or metric analysis.

The exact question is:

\[
\boxed{
\begin{aligned}
&\text{Can one construct a normalizable BRST-physical string state in the}\\
&\text{chronal Taub region, propagate it through the exact CFT across the}\\
&\text{Misner-type chronology horizon, and compute a controlled observable}\\
&\text{showing entry into and operational use of the NUT/CTC region?}
\end{aligned}}
\]

A convincing positive answer should specify:

1. the physical vertex operators / Hilbert-space states;
2. normalizability and BRST conditions;
3. the horizon-crossing observable or amplitude;
4. whether genus/\(g_s\) corrections are controlled;
5. whether the state can complete a closed timelike history;
6. whether the construction is merely a fixed background or can be embedded
   in predictive formation from regular data.

If no such calculation exists, the exact CFT remains a geometry/background
counterexample but not an operational time-machine counterexample.

---

# 13. Predictive realizability gate

**SYNTHESIS / CRITERION — not a theorem.**

A chronology-violating phase should be called physically realizable only if:

\[
\boxed{
\begin{aligned}
1.\;&\text{the physical evolution law selects it, rather than an arbitrary
post-Cauchy-horizon extension;}\\
2.\;&\text{physical states remain admissible;}\\
3.\;&\text{interacting observables remain consistently defined;}\\
4.\;&\text{the CTC region is operationally reachable;}\\
5.\;&\text{the relevant evolution remains UV controlled.}
\end{aligned}}
\]

The present audit has attempted to falsify this gate.

No located example falsifies all five conditions simultaneously.

That statement is a documented literature-search outcome, not a universal
chronology-protection theorem.

---

# 14. Novelty/status map

### MGHD / extension distinction

**PUBLISHED RESULT / PRIOR ART.**

Not novel. Ori explicitly discusses the logical difficulty, and the
Choquet-Bruhat--Geroch MGHD framework already formalizes the deterministic
boundary.

### Ori "any smooth extension contains nearby CTCs" response

**PUBLISHED RESULT.**

Important because it strengthens extension-level chronology violation despite
nonunique post-horizon extensions.

### Xavier "onset, not CTC region" statement

**PUBLISHED CLAIM in a 2026 preprint.**

The paper explicitly limits what its initial data determine and leaves the
supporting source/matching outside scope.

### Predictive realizability gate

**SYNTHESIS / CRITERION.**

Useful organizing principle, not a theorem.

### No operational counterexample identified

**LITERATURE SEARCH RESULT / OPEN.**

Do not rewrite this as "operational time travel is impossible."

### Exact heterotic CFT

**COUNTEREXAMPLE CANDIDATE.**

Strong against the claim that UV completion removes every CTC geometry.
Operational target-space traversal remains open in this audit.

---

# 15. References

1. A. Ori, *Formation of closed timelike curves in a composite vacuum/dust
   asymptotically-flat spacetime*, Phys. Rev. D **76**, 044002 (2007),
   arXiv:gr-qc/0701024.
2. S. Xavier, *Closed Timelike Curves from a Vacuum Traveling Wave*,
   arXiv:2607.00788 (2026).
3. Y. Choquet-Bruhat, R. Geroch, *Global aspects of the Cauchy problem in
   general relativity*, Commun. Math. Phys. **14**, 329 (1969).
4. J. Sbierski, *On the Existence of a Maximal Cauchy Development for the
   Einstein Equations -- a Dezornification*, Ann. Henri Poincaré **17**, 301
   (2016), arXiv:1309.7591.
5. J. Isenberg, *On Strong Cosmic Censorship*, Surveys in Differential
   Geometry **20** (2015), arXiv:1505.06390.
6. C. V. Johnson, H. G. Svendsen, *Exact string theory model of closed
   timelike curves and cosmological singularities*, Phys. Rev. D **70**,
   126011 (2004), arXiv:hep-th/0405141.
7. H. G. Svendsen, *Exact geometry of a Kerr--Taub--NUT solution of string
   theory*, Phys. Rev. D **71**, 044027 (2005), arXiv:hep-th/0410011.
8. H. G. Svendsen, *Global properties of an exact string theory solution in
   two and four dimensions*, Phys. Rev. D **73**, 064032 (2006),
   arXiv:hep-th/0511289.
9. M. Berkooz, B. Pioline, M. Rozali, *Closed Strings in Misner Space:
   Cosmological Production of Winding Strings*, arXiv:hep-th/0405126.
10. M. Berkooz, B. Durin, B. Pioline, D. Reichmann, *Closed Strings in Misner
    Space: Stringy Fuzziness with a Twist*, arXiv:hep-th/0407216.
11. J. L. Friedman, N. J. Papastamatiou, J. Z. Simon, *Failure of unitarity for
    interacting fields on spacetimes with closed timelike curves*,
    Phys. Rev. D **46**, 4456 (1992).
12. J. B. Hartle, *Unitarity and causality in generalized quantum mechanics for
    nonchronal spacetimes*, Phys. Rev. D **49**, 6543 (1994),
    arXiv:gr-qc/9309012.
13. D. Deutsch, *Quantum mechanics near closed timelike lines*,
    Phys. Rev. D **44**, 3197 (1991).
14. R. Emparan, M. Tomašević, *Holography of time machines*,
    JHEP **03** (2022) 212, arXiv:2107.14200.
15. R. Emparan, M. Tomašević, *Quantum backreaction on chronology horizons*,
    JHEP **02** (2022) 182, arXiv:2109.03611.
