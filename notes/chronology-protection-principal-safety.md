# Chronology Protection as a Principal-Safety / Realizability Gate

**Status:** exploratory side branch.

Status discipline:

- **PUBLISHED RESULT**
- **REPRODUCED HERE**
- **SYNTHESIS / CRITERION**
- **CONJECTURE / OPEN**

This first pass deliberately stays narrow: **Misner space and compactly
generated Cauchy horizons**, centered on the Kay--Radzikowski--Wald (KRW)
result.

The question is not whether one can write a metric containing CTCs. It is

\[
\boxed{
\text{Can regular, physically admissible evolution reach a CTC region while
remaining well defined?}
}
\]

The first result of this side branch is already a useful negative test:

\[
\boxed{
\text{chronology horizon}
\not\Rightarrow
\text{local classical principal-symbol degeneration}.
}
\]

For Misner space the metric and Klein--Gordon principal symbol are locally
regular at the chronology horizon. The sharp known obstruction instead
appears in the **global/microlocal quantum-state structure**.

---

# 1. Literature map

## 1.1 Hawking chronology protection

**PUBLISHED RESULT.**

S. W. Hawking, *Chronology Protection Conjecture*,
Phys. Rev. D **46**, 603--611 (1992),
DOI 10.1103/PhysRevD.46.603.

Hawking studies the production of causality violation in a finite region
without a curvature singularity, focusing on compactly generated Cauchy
horizons.

For a noncompact initial surface, the classical argument requires violation of
an averaged weak/null energy condition in order to form such a horizon.

The quantum discussion gives strong evidence for large vacuum polarization and
backreaction near almost-closed null curves. It is not a theorem that

\[
\langle T_{\mu\nu}\rangle_{\rm ren}\to\infty
\]

for every state at every chronology horizon.

That distinction became important after explicit Misner examples with finite
limiting stress tensors were found.

## 1.2 Kay--Radzikowski--Wald

**PUBLISHED RESULT.**

B. S. Kay, M. J. Radzikowski, R. M. Wald,
*Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy
Horizon*, Commun. Math. Phys. **183**, 533--556 (1997),
arXiv:gr-qc/9603012,
DOI 10.1007/s002200050042.

KRW prove two precise statements for a linear Klein--Gordon field on a
spacetime with a compactly generated Cauchy horizon.

### Theorem 1: F-locality

There is no extension of the usual field algebra from the initial globally
hyperbolic region that satisfies **F-locality** at a horizon base point.

Base points are past terminal accumulation points of horizon generators.

Thus an attempted QFT extension cannot, at a base point, agree locally with
the ordinary field algebra that would be assigned to a globally hyperbolic
neighborhood.

### Theorem 2: Hadamard failure

Take a Hadamard state on the initial globally hyperbolic region and extend its
two-point distribution as a distributional bisolution of the Klein--Gordon
equation.

At every base point \(x\),

\[
\omega_2-H_{\rm loc}
\]

cannot be represented by a bounded function in any neighborhood of
\((x,x)\), where \(H_{\rm loc}\) is a local Hadamard distribution.

Therefore ordinary point-splitting definitions of

\[
\langle\phi^2\rangle_{\rm ren},
\qquad
\langle T_{\mu\nu}\rangle_{\rm ren}
\]

are ill-defined or singular at those points.

The proof uses propagation-of-singularities theorems for the Klein--Gordon
operator.

The crucial scope statement is

\[
\boxed{
\text{KRW is not a universal stress-tensor blow-up theorem.}
}
\]

## 1.3 Microlocal Hadamard condition

**PUBLISHED RESULT.**

M. J. Radzikowski,
*Micro-local approach to the Hadamard condition in quantum field theory on
curved space-time*,
Commun. Math. Phys. **179**, 529--553 (1996).

The Hadamard condition can be expressed as a condition on the wavefront set of
the two-point distribution.

This makes the KRW obstruction naturally interpretable as

\[
\boxed{
\text{principal null bicharacteristics}
+
\text{global null recurrence}
\rightarrow
\text{forbidden two-point wavefront singularities}.
}
\]

That is the cleanest bridge to the repository's principal-safety language.

## 1.4 Finite-stress Misner examples

**PUBLISHED RESULT.**

S. V. Krasnikov,
*Quantum stability of the time machine*,
Phys. Rev. D **54**, 7322 (1996),
arXiv:gr-qc/9508038.

S. V. Sushkov,
*Chronology Protection and Quantized Fields: Complex Automorphic Scalar Field
in Misner Space*,
Class. Quantum Grav. **14**, 523 (1997),
arXiv:gr-qc/9509056.

These works contain examples in which a renormalized stress tensor remains
bounded, or can vanish, in the initial globally hyperbolic region as the
horizon is approached.

Thus

\[
\boxed{
\langle T_{\mu\nu}\rangle\to\infty
}
\]

is not the right universal chronology-protection criterion.

## 1.5 Cramer--Kay resolution of the finite-stress issue

**PUBLISHED RESULT.**

C. R. Cramer, B. S. Kay,
*Stress-Energy Must be Singular on the Misner Space Horizon even for
Automorphic Fields*,
Class. Quantum Grav. **13**, L143 (1996),
arXiv:gr-qc/9606027.

C. R. Cramer, B. S. Kay,
*The thermal and two-particle stress-energy must be ill-defined on the
two-dimensional Misner space chronology horizon*,
Phys. Rev. D **57**, 1052 (1998),
arXiv:gr-qc/9708028.

They analyze states whose stress tensor can vanish throughout the initial
globally hyperbolic region. Nevertheless, in every neighborhood of a horizon
point there are non-null-related point pairs for which the suitably
differentiated two-point function is singular.

Therefore a finite limit from the chronal side does not imply that the
renormalized stress tensor is well defined **on** the horizon.

---

# 2. Misner space as the clean testbed

Use the two-dimensional Misner metric

\[
\boxed{
ds^2=-2\,dT\,d\psi-T\,d\psi^2,
}
\]

with periodic identification

\[
\psi\sim\psi+\Delta.
\]

The periodic generator is

\[
k=\partial_\psi.
\]

Its norm is

\[
\boxed{
k^2=g_{\psi\psi}=-T.
}
\]

Hence

\[
T<0
\Rightarrow
k^2>0
\Rightarrow
\text{periodic orbit spacelike},
\]

\[
T=0
\Rightarrow
k^2=0
\Rightarrow
\text{closed null orbit / chronology horizon},
\]

\[
T>0
\Rightarrow
k^2<0
\Rightarrow
\text{closed timelike curves}.
\]

Misner space is a boost quotient of flat Minkowski space. The essential
pathology is global rather than a curvature blow-up.

---

# 3. Local principal-safety check

## 3.1 Metric rank

**REPRODUCED HERE.**

In coordinates \((T,\psi)\),

\[
g_{ab}
=
\begin{pmatrix}
0&-1\\
-1&-T
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\det g=-1
}
\]

everywhere, including \(T=0\).

The inverse metric is

\[
g^{ab}
=
\begin{pmatrix}
T&-1\\
-1&0
\end{pmatrix},
\]

and

\[
\boxed{
\det g^{ab}=-1.
}
\]

Direct symbolic contraction gives

\[
R_{ab}=0,
\qquad
R=0.
\]

So the chronology horizon is locally smooth and flat.

## 3.2 Klein--Gordon principal polynomial

For a scalar field,

\[
P(\xi)=g^{ab}\xi_a\xi_b.
\]

Thus

\[
\boxed{
P(\xi)
=
T\xi_T^2-2\xi_T\xi_\psi.
}
\]

There is no rank loss of the principal metric at the horizon.

The full massless wave equation is

\[
\Box\phi
=
T\,\partial_T^2\phi
+
\partial_T\phi
-
2\,\partial_T\partial_\psi\phi.
\]

## 3.3 The horizon is characteristic, not singular

The normal to \(T=\) constant is \(dT\), and

\[
P(dT)=g^{TT}=T.
\]

Therefore

\[
\boxed{
P(dT)|_{T=0}=0.
}
\]

So the chronology horizon is a null characteristic hypersurface.

But

\[
\det g^{ab}|_{T=0}=-1,
\]

so this is not a principal-rank singularity.

The distinction is

\[
\boxed{
\text{characteristic horizon}
\neq
\text{degenerate principal symbol}.
}
\]

Reproducibility:

    python src/symbolic/chronology_misner_principal_gate.py

---

# 4. Answer to the six first-task questions

## 4.1 What exactly does KRW establish?

**PUBLISHED RESULT.**

Under its hypotheses,

\[
\boxed{
\text{compactly generated Cauchy horizon}
+
\text{Hadamard state in the initial GH region}
}
\]

implies a breakdown of ordinary local QFT structure at horizon base points.

Specifically:

1. F-locality cannot be maintained there.
2. A Hadamard two-point distribution cannot retain the standard local
   Hadamard singularity structure there.
3. Standard point-split composite observables such as
   \(\langle\phi^2\rangle_{\rm ren}\) and
   \(\langle T_{\mu\nu}\rangle_{\rm ren}\) are consequently ill-defined or
   singular there.

KRW does **not** prove:

- that every chronology horizon is compactly generated;
- a universal divergence rate;
- that the metric or curvature diverges;
- that the local wave operator loses hyperbolicity;
- that semiclassical backreaction necessarily destroys the horizon;
- that no alternative non-globally-hyperbolic QFT can exist;
- that full quantum gravity forbids every CTC background.

## 4.2 Which object ceases to be well defined?

The most precise answer is

\[
\boxed{
\text{the two-point distribution fails the Hadamard/microlocal admissibility
condition at KRW base points.}
}
\]

It is too crude to say that the two-point distribution simply "does not
exist." KRW considers a distributional bisolution extension.

The problem is that its singularity structure cannot be reduced to the local
Hadamard singularity plus a sufficiently regular remainder.

Point splitting requires

\[
\omega_2-H_{\rm loc}
\]

to be regular enough near coincidence. When that fails, standard definitions
of local Wick observables fail.

Thus the logical chain is

\[
\boxed{
\text{Hadamard failure}
\rightarrow
\text{point-splitting failure}
\rightarrow
\langle T_{\mu\nu}\rangle_{\rm ren}
\text{ not defined in the standard way}.
}
\]

This is stronger and more precise than demanding a numerical divergence of
the stress tensor along every approach to the horizon.

## 4.3 Can this be phrased as a principal-safety gate?

### Local classical principal gate: NO

The Misner calculation directly gives

\[
\det g^{ab}=-1
\]

at the horizon.

Therefore

\[
\boxed{
\text{CTC onset}
\Rightarrow
\text{local principal-symbol degeneration}
}
\]

is false for this testbed.

### Microlocal principal-realizability gate: YES as a synthesis

**SYNTHESIS / CRITERION.**

The KRW proof is driven by propagation of singularities. Singular directions
are transported by the null bicharacteristic flow determined by the principal
symbol.

Compact generation makes null characteristics recur and accumulate in a way
that is incompatible with the Hadamard wavefront-set condition.

So the more useful formulation is

\[
\boxed{
\text{regular local principal operator}
+
\text{globally recurrent characteristics}
\rightarrow
\text{microlocally inadmissible standard QFT state}.
}
\]

This suggests adding a gate to the repository:

\[
\boxed{
\textbf{Microlocal state gate:}
\quad
WF(\omega_2)
\text{ must preserve the Hadamard spectrum structure.}
}
\]

This is a repository synthesis, not a new theorem.

## 4.4 Can regular initial data approach the horizon?

Three notions must be separated.

### Fixed-background field evolution

Yes.

The region

\[
T<0
\]

is a smooth globally hyperbolic chronal region. Classical field data and
Hadamard quantum states can be specified there and evolved arbitrarily close
to

\[
T=0.
\]

No local curvature or principal-rank obstruction appears before the horizon.

### Classical evolution on some CTC backgrounds

J. L. Friedman and M. S. Morris proved existence, and restricted uniqueness,
of smooth massless-field solutions on certain nonglobally-hyperbolic wormhole
spacetimes with CTCs:

*Existence and uniqueness theorems for massless fields on a class of
spacetimes with closed timelike curves*,
Commun. Math. Phys. **186**, 495--529 (1997),
arXiv:gr-qc/9411033.

Hence

\[
\boxed{
\text{CTC background}
\not\Rightarrow
\text{automatic classical PDE inconsistency}.
}
\]

### Dynamical creation of the Misner quotient

This is not established by the fixed-background construction.

The boost identification is part of the definition of Misner spacetime. The
test does not show that ordinary Einstein--matter data on a regular,
simply-connected Cauchy surface dynamically generate that global
identification.

Therefore

\[
\boxed{
\text{Misner is a clean chronology-horizon test,
not a complete formation model.}
}
\]

### Semiclassical approach

Finite or vanishing stress-tensor behavior can occur on the initial globally
hyperbolic side.

But at the horizon KRW/Cramer--Kay imply failure of the ordinary Hadamard
point-splitting construction.

Thus the semiclassical Einstein equation

\[
G_{\mu\nu}
=
8\pi G
\langle T_{\mu\nu}\rangle_{\rm ren}
\]

cannot simply be assumed to remain defined through the KRW obstruction.

The failure can be

\[
\boxed{
\text{the right-hand side ceases to be a standard local observable},
}
\]

not merely that it becomes a very large number.

## 4.5 What would full quantum gravity have to repair?

A theory that genuinely allows passage through the chronology horizon must
replace at least one component of the semiclassical framework.

Possible mechanisms are:

1. **Geometry changes before the horizon.**
   Backreaction, a singularity, a domain wall, topology change, or new light
   degrees of freedom remove the naive continuation.

2. **The state space changes.**
   Standard Hadamard/microlocal admissibility is replaced by another
   formulation that still gives finite observables, unitarity, and an
   acceptable locality principle.

3. **The CTC region is formally present but inaccessible.**
   A UV theory may decouple it from physical excitations.

4. **A new global evolution law replaces ordinary Cauchy evolution.**
   If global hyperbolicity is lost, the full theory must explain how
   observables remain predictive without inconsistent multiple evolution.

Krasnikov's criticism of F-locality is relevant here: the KRW theorem proves
an obstruction to a very well-motivated standard framework. It is not a
logical contradiction in every conceivable quantum theory.

A proposed full theory should therefore answer

\[
\boxed{
\text{What replaces the ordinary Cauchy/Hadamard construction?}
}
\]

rather than merely exhibit a finite metric.

## 4.6 Is there a UV-complete counterexample with genuinely physical CTCs?

The targeted search gives a mixed answer.

### Exact heterotic CFT: serious counterexample candidate

**PUBLISHED RESULT / COUNTEREXAMPLE CANDIDATE.**

C. V. Johnson, H. G. Svendsen,
*Exact string theory model of closed timelike curves and cosmological
singularities*,
Phys. Rev. D **70**, 126011 (2004),
arXiv:hep-th/0405141.

This is a heterotic coset model with a full CFT definition. Important
Taub--NUT features, including CTC regions, persist after the complete
\(\alpha'\) correction considered in the exact geometry.

Therefore an overly strong statement such as

\[
\boxed{
\text{a UV-complete theory can contain no CTC geometry at all}
}
\]

is not tenable on the basis of present string examples.

However, the same model contains an emergent Euclidean-signature region
bounded by timelike curvature singularities, and the authors explicitly
describe the physical interpretation of the surviving CTCs as premature.

It does not establish

\[
\boxed{
\text{regular admissible initial data}
\to
\text{unitary controlled evolution}
\to
\text{physically traversable CTC region}.
}
\]

So it is not a clean counterexample to the **dynamical-realizability**
formulation of chronology protection.

### Misner string orbifold

M. Berkooz, B. Pioline, M. Rozali,
*Closed Strings in Misner Space: Cosmological Production of Winding Strings*,
arXiv:hep-th/0405126.

String propagation can be studied on the Misner boost orbifold, but the model
shows strong winding-string production and singularities in loop amplitudes
associated with periodic trajectories.

Again, this is not a clean stable physical time machine.

### Stringy chronology-protection example

N. Drukker, B. Fiol, J. Simón,
*Gödel's Universe in a Supertube Shroud*,
Phys. Rev. Lett. **91**, 231601 (2003),
arXiv:hep-th/0306057.

In these Gödel-like backgrounds, supertube modes can acquire negative kinetic
terms when wrapping CTCs, and domain-wall physics can eliminate the CTC
region.

This is unusually close to the repository's original principal-safety
language:

\[
\boxed{
\text{chronology pathology}
\leftrightarrow
\text{negative physical kinetic mode}
}
\]

in a model-specific UV completion.

### Holographic interacting-QFT example

R. Emparan, M. Tomašević,
*Holography of time machines*,
JHEP **03** (2022) 212,
arXiv:2107.14200.

Their holographic CFT construction has a regular dual bulk that separates into
CTC and non-CTC components, with no physical passage across the chronology
horizon.

In related work, quantum backreaction can turn the chronology horizon into a
strong spacelike curvature singularity.

These examples support **physical inaccessibility / realizability failure**
rather than a universal perturbative stress-tensor blow-up mechanism.

The current conclusion is therefore

\[
\boxed{
\text{exact quantum backgrounds with CTC regions exist as candidates,
but no clean UV-complete dynamically formed traversable CTC counterexample
has been established in this pass.}
}
\]

---

# 5. Gate matrix

| Gate | Misner / compact-horizon status | Interpretation |
|---|---|---|
| Background curvature | PASS | Misner is locally flat |
| Local metric rank | PASS | \(\det g=-1\) |
| Local KG principal metric | PASS | \(\det g^{ab}=-1\) |
| Chronology horizon characteristic | YES | \(P(dT)=0\) |
| Local cone degeneracy | NO | principal metric remains Lorentzian |
| Global hyperbolicity across horizon | FAIL | ordinary global Cauchy problem ends |
| F-locality at KRW base points | FAIL | theorem-level |
| Hadamard extension at KRW base points | FAIL | theorem-level |
| Finite stress tensor on approach | STATE DEPENDENT | finite examples exist |
| Standard renormalized stress tensor on horizon | FAIL at KRW points | point splitting fails |
| Backreaction destroys horizon | NOT UNIVERSAL | model dependent |
| Full-QG ban on all CTC geometries | NOT ESTABLISHED | exact-CFT candidates exist |
| Dynamically formed, physically traversable CTC in UV theory | OPEN | no clean example found here |

---

# 6. Mechanism classification

Using the chronology-task taxonomy:

## Type I — energy-condition obstruction

**PUBLISHED / conditional.**

Important for manufactured compactly generated horizons, but quantum matter
can violate the relevant classical energy conditions.

## Type II — stress-energy / Hadamard failure

**PUBLISHED / strongest theorem-level mechanism in this phase.**

The robust statement is KRW's Hadamard/microlocal obstruction under its
hypotheses, not universal numerical stress-energy blow-up.

## Type III — principal-symbol / strong-coupling failure

**NEGATIVE RESULT for fixed-background Misner scalar QFT.**

No local principal-rank failure occurs at \(T=0\).

However, stringy Gödel examples show model-specific negative kinetic modes, so
this mechanism can operate in a UV theory without being universal.

## Type IV — unitarity / UV-consistency exclusion

**MODEL DEPENDENT / OPEN.**

Some string and holographic models protect chronology; other exact CFT models
retain CTC regions.

## Type V — dynamical non-realizability

**PROMISING SYNTHESIS / OPEN.**

The mixed evidence is consistent with

\[
\boxed{
\text{formal CTC solution}
\not\Rightarrow
\text{physically reachable CTC history}.
}
\]

## Type VI — causality imposed fundamentally

Not tested in this first phase.

It must remain logically distinct from deriving causality from physical
consistency.

---

# 7. What is actually proved

## PUBLISHED RESULT

1. Under KRW hypotheses, ordinary F-locality and Hadamard extension fail at
   compactly generated Cauchy-horizon base points.
2. Standard point-split local observables therefore fail there.
3. A finite stress-tensor limit while approaching a Misner horizon does not
   remove the singular horizon two-point structure.
4. Some CTC spacetimes nevertheless admit regular classical free-field
   solutions.
5. String theory contains both chronology-protecting mechanisms and exact-CFT
   backgrounds in which CTC regions persist.

## REPRODUCED HERE

For the standard two-dimensional Misner metric,

\[
\det g=-1,
\qquad
R_{ab}=0,
\]

\[
k^2=-T,
\]

\[
P(\xi)=T\xi_T^2-2\xi_T\xi_\psi,
\]

\[
\det g^{ab}=-1,
\]

and

\[
P(dT)|_{T=0}=0.
\]

Thus the chronology horizon is a regular characteristic horizon, not a local
principal-metric singularity.

---

# 8. Main synthesis

The Misner/KRW test rejects the simple identification

\[
\boxed{
\text{chronology violation}
=
\text{local principal-safety failure}.
}
\]

A more defensible statement is

\[
\boxed{
\text{chronology violation may require failure of a global
physical-realizability gate}.
}
\]

For compactly generated Cauchy horizons in ordinary linear QFT, the precise
known failure is

\[
\boxed{
\text{Hadamard / microlocal state admissibility at KRW base points}.
}
\]

So the useful chronology-protection analogue of principal safety is not merely

\[
\det P(\xi)\neq0.
\]

It should include

\[
\boxed{
\text{local principal regularity}
+
\text{global Cauchy structure}
+
\text{microlocal spectrum admissibility}.
}
\]

The strongest present synthesis is

\[
\boxed{
\text{chronology protection may be a global/microlocal consistency
condition rather than a local principal-symbol condition.}
}
\]

This is a **SYNTHESIS / CRITERION**, not a theorem.

---

# 9. Remaining gap

The unresolved question is

\[
\boxed{
\text{Does every dynamically reachable CTC phase fail some physical
consistency gate in a complete quantum theory?}
}
\]

KRW alone does not establish this.

The most important gaps are:

1. extension beyond compactly generated Cauchy horizons;
2. interacting-QFT analogues of KRW;
3. whether a non-Hadamard UV state concept can remain unitary and locally
   predictive;
4. full-QG behavior when the Weyl/metric description itself changes;
5. a genuinely dynamical exact-string example starting from regular initial
   data and reaching a physically traversable CTC region.

---

# 10. Candidate calculations

## Candidate A — Misner image/wavefront toy

Construct the image-sum two-point function for the boost quotient and track
null-related image pairs accumulating near the horizon.

Goal:

\[
\boxed{
\text{reproduce geometrically why the extra singular pairs accumulate}.
}
\]

This would be **REPRODUCED HERE**, not a new theorem.

## Candidate B — principal versus microlocal gate

For a self-interacting or UV-completed Misner-like model, compare

\[
\text{principal determinant},
\qquad
\text{physical kinetic matrix},
\qquad
WF(\omega_2).
\]

Question:

\[
\boxed{
\text{Does the microlocal gate fail before any local kinetic pathology?}
}
\]

## Candidate C — exact-CFT counterexample audit

For the Johnson--Svendsen heterotic Taub--NUT model, explicitly audit:

\[
\begin{aligned}
&\text{worldsheet unitarity},\\
&\text{normalizable physical states in the CTC region},\\
&\text{transition amplitudes across the chronology horizon},\\
&\text{dynamical formation from a regular state}.
\end{aligned}
\]

This is the cleanest route to deciding whether that exact background is a
genuine counterexample to realizability-based chronology protection.

---

# 11. Novelty / status map

### Misner local principal-symbol regularity

**Status:** REPRODUCED HERE.

No novelty claim.

### Microlocal state gate

**Status:** SYNTHESIS / CRITERION.

The mathematical ingredients are published: propagation of singularities,
microlocal Hadamard structure, and KRW. The repository contribution is only
their organization into the principal-safety gate language.

### Universal chronology-protection theorem

**Status:** NOT ESTABLISHED.

Do not claim that all CTCs are forbidden by quantum gravity.

### Exact-string CTC counterexample

**Status:** OPEN / COUNTEREXAMPLE CANDIDATE.

Exact CFT examples are enough to reject an overly strong "UV theories cannot
contain CTC geometries" slogan, but they do not yet establish the stronger
dynamical-realizability chain required here.

---

# 12. References

1. S. W. Hawking, *Chronology Protection Conjecture*, Phys. Rev. D **46**,
   603--611 (1992), DOI 10.1103/PhysRevD.46.603.
2. B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on
   Spacetimes with a Compactly Generated Cauchy Horizon*, Commun. Math. Phys.
   **183**, 533--556 (1997), arXiv:gr-qc/9603012,
   DOI 10.1007/s002200050042.
3. M. J. Radzikowski, *Micro-local approach to the Hadamard condition in
   quantum field theory on curved space-time*, Commun. Math. Phys. **179**,
   529--553 (1996).
4. C. R. Cramer, B. S. Kay, *Stress-Energy Must be Singular on the Misner
   Space Horizon even for Automorphic Fields*, Class. Quantum Grav. **13**,
   L143 (1996), arXiv:gr-qc/9606027.
5. C. R. Cramer, B. S. Kay, *The thermal and two-particle stress-energy must
   be ill-defined on the two-dimensional Misner space chronology horizon*,
   Phys. Rev. D **57**, 1052 (1998), arXiv:gr-qc/9708028,
   DOI 10.1103/PhysRevD.57.1052.
6. S. V. Krasnikov, *Quantum stability of the time machine*, Phys. Rev. D
   **54**, 7322 (1996), arXiv:gr-qc/9508038.
7. S. V. Sushkov, *Chronology Protection and Quantized Fields: Complex
   Automorphic Scalar Field in Misner Space*, Class. Quantum Grav. **14**,
   523 (1997), arXiv:gr-qc/9509056.
8. J. L. Friedman, M. S. Morris, *Existence and uniqueness theorems for
   massless fields on a class of spacetimes with closed timelike curves*,
   Commun. Math. Phys. **186**, 495--529 (1997), arXiv:gr-qc/9411033,
   DOI 10.1007/s002200050118.
9. C. V. Johnson, H. G. Svendsen, *Exact string theory model of closed
   timelike curves and cosmological singularities*, Phys. Rev. D **70**,
   126011 (2004), arXiv:hep-th/0405141,
   DOI 10.1103/PhysRevD.70.126011.
10. M. Berkooz, B. Pioline, M. Rozali, *Closed Strings in Misner Space:
    Cosmological Production of Winding Strings*, arXiv:hep-th/0405126.
11. N. Drukker, B. Fiol, J. Simón, *Gödel's Universe in a Supertube Shroud*,
    Phys. Rev. Lett. **91**, 231601 (2003), arXiv:hep-th/0306057,
    DOI 10.1103/PhysRevLett.91.231601.
12. R. Emparan, M. Tomašević, *Holography of time machines*, JHEP **03**
    (2022) 212, arXiv:2107.14200, DOI 10.1007/JHEP03(2022)212.
13. R. Emparan, M. Tomašević, *Quantum backreaction on chronology horizons*,
    JHEP **02** (2022) 182, arXiv:2109.03611.


---

## Second-phase follow-up

See `notes/chronology-realizability-counterexample-audit.md` for the second-phase predictive-realizability / operational-counterexample audit.
