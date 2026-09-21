# Exact Heterotic Taub–NUT CFT: Operational CTC Traversal Audit

**Status:** Phase III chronology side branch; Phase IV (twisted-sector gate)
resolved in notes/fable-heterotic-ctc-operational-traversal.md.

Status labels used below:

- **PUBLISHED RESULT**
- **REPRODUCED HERE**
- **NEW CALCULATION CANDIDATE**
- **SYNTHESIS / CRITERION**
- **COUNTEREXAMPLE CANDIDATE**
- **OPEN**

This note continues:

- notes/chronology-protection-principal-safety.md
- notes/chronology-realizability-counterexample-audit.md

It does not revisit the Phase-I Misner/KRW analysis or the Phase-II general
realizability survey.

The adversarial target is narrower:

\[
\boxed{
\begin{aligned}
&\text{Does the exact heterotic Taub--NUT coset CFT contain a controlled}\\
&\text{physical string process that crosses from the chronal Taub region}\\
&\text{into the NUT/CTC sector and realizes an operational closed-timelike}\\
&\text{history?}
\end{aligned}}
\]

The result of this pass is:

\[
\boxed{
\text{Level A (exact CTC background): ESTABLISHED}
}
\]

but

\[
\boxed{
\text{Level B/C (BRST-physical traversal and operational CTC observable):
OPEN in the targeted literature search.}
}
\]

The first new diagnostic is negative for a simple chronology-protection
mechanism:

\[
\boxed{
\text{the }x=1\text{ chronology horizon is not an automatic local
Nambu--Goto area singularity for the simplest wrapped probe.}
}
\]

The exact dilaton is also finite there. Thus, if string theory blocks
operational traversal in this model, it must do more than produce a trivial
local divergence of the wrapped-string area density or a divergent string
coupling at the first horizon.

---

# 1. Executive result

The exact heterotic Taub--NUT model remains a serious
**COUNTEREXAMPLE CANDIDATE** to the overly strong statement

\[
\text{UV completion} \Rightarrow \text{no CTC geometry}.
\]

Johnson--Svendsen and Svendsen establish a full heterotic coset-CFT
description and an exact-in-\(\alpha'\) target geometry whose Taub/NUT
chronology structure survives. The later global analysis studies analytic
continuations, test-particle motion, and T-duality.

However, the targeted search performed for this phase did **not** identify a
Taub--NUT-specific paper that performs the decisive string-state calculation:

\[
\boxed{
\text{normalizable BRST state in Taub}
\to
\text{horizon crossing}
\to
\text{controlled state in NUT/CTC}
\to
\text{BRST/gauge-invariant operational return}.
}
\]

This statement is a documented search result, not proof that no such work
exists.

The exact missing link is already visible in the coset construction. The
periodic target coordinate is not introduced as an ordinary spectator
compact boson. In the gauged WZNW description, after gauge fixing

\[
t_R=t,\qquad t_L=0,\qquad \psi=0,
\]

a large \(U(1)_B\) gauge transformation with parameter \(4\pi\) acts
trivially on the \(SU(2)\) factor while shifting

\[
t_R\to t_R+4\pi\lambda.
\]

Hence

\[
\boxed{
t\sim t+4\pi\lambda
}
\]

is induced by the coset gauging.

Therefore the chronology-direction quantum number cannot safely be treated as
the winding number of a free compact boson without first mapping it into the
gauged-WZW/BRST quantum numbers.

This mapping is the first unresolved full-CFT gate.

---

# 2. Taub–NUT-specific prior-art audit

The search was restricted to descendants and closely related work around:

1. Johnson--Svendsen 2004;
2. Svendsen 2005;
3. Svendsen 2006;
4. the original heterotic-coset Taub--NUT constructions.

Search terms included:

- heterotic Taub--NUT spectrum;
- physical vertex operators;
- BRST cohomology;
- gauged-WZW representations;
- minisuperspace;
- wavefunctions;
- reflection/transmission;
- two-point functions;
- correlation functions;
- scattering;
- winding around the periodic Taub--NUT fiber;
- Taub/NUT horizon crossing.

## 2.1 Audit table

| Proposed calculation | Prior art found? | Exact scope found | Remaining gap |
|---|---|---|---|
| all-\(\alpha'\) Taub--NUT metric/dilaton | YES | exact coset-derived target fields | no need to redo |
| all-\(\alpha'\) Kerr--Taub--NUT geometry | YES | rotating exact metric/dilaton, singularity analysis | no need to redo |
| global analytic extension | YES | analytic regions, T-duality, classical test particles | string-state traversal not supplied |
| CTC survival after \(\alpha'\) corrections | YES | CTC/NUT structure persists | operational meaning unresolved |
| Taub--NUT-specific BRST physical spectrum | NOT IDENTIFIED | generic heterotic-coset machinery exists | explicit chronology-sector cohomology |
| target-fiber winding state map | NOT IDENTIFIED | periodicity traced to large \(U(1)_B\) gauging | map winding/holonomy to exact coset labels |
| minisuperspace Taub\(\to\)NUT transmission | NOT IDENTIFIED | classical test particles studied | wave equation/flux for string states |
| exact Taub\(\to\)NUT two-point/reflection amplitude | NOT IDENTIFIED | no such result located | first useful crossing observable |
| interacting chronology-sector correlator | NOT IDENTIFIED | comparison models exist | OPE/factorization/instability |
| operational closed-timelike-return observable | NOT IDENTIFIED | none found | decisive Level-C test |

The closest relevant calculations are in **other** CTC string backgrounds:

- heterotic Gödel/AdS: physical spectrum and genus-one partition function are
  computed; long strings destabilize the CTC background;
- Misner orbifold: physical twisted states include strings winding a timelike
  compact direction; pair production and loop/amplitude singularities occur;
- Gödel M-theory: M2 probes can cross the CTC horizon and their wavefunctions
  can be quantized.

These comparison models kill any claim that the novelty target is merely
"extended objects can enter a CTC region."

The Taub--NUT-specific target remains the exact-CFT operational process.

---

# 3. Exact source conventions

## 3.1 Coset structure

**PUBLISHED RESULT.**

The exact model is based on the heterotic coset

\[
\boxed{
\frac{SL(2,\mathbb R)\times SU(2)}
{U(1)_A\times U(1)_B}.
}
\]

The asymmetric gauging is anomaly free only after including right-moving
supersymmetric fermions and suitably charged left-moving fermions. In the
bosonized description the left charges are fixed by algebraic anomaly
cancellation conditions.

For the nonrotating Taub--NUT model, the relevant features are inherited from
the \(\tau=0\) specialization of the Kerr--Taub--NUT coset.

The periodic target coordinate arises from the \(U(1)_B\) gauging:

\[
\boxed{
\epsilon_B=4\pi:
\quad
t_R\to t_R+4\pi\lambda
}
\]

while acting as the identity on the \(SU(2)\) group coordinate. After gauge
fixing \(t_R=t\), this becomes

\[
\boxed{
t\sim t+4\pi\lambda.
}
\]

This is central for the physical-state problem.

## 3.2 Exact metric

For the nonrotating solution, at fixed angular coordinates the exact
\((x,t)\) fiber block is

\[
\boxed{
ds_{\rm fib}^2
=
(k-2)
\left[
\frac{dx^2}{x^2-1}
-
\frac{x^2-1}{D(x)}dt^2
\right],
}
\]

with

\[
\boxed{
D(x)
=
(x+\delta)^2
-
\frac4{k+2}(x^2-1).
}
\]

The exact dilaton is

\[
\boxed{
\Phi-\Phi_0
=
-\frac14\ln D(x).
}
\]

The chronology/Killing horizons remain at

\[
\boxed{x=\pm1}.
\]

In the Taub region

\[
-1<x<1,
\]

the periodic \(t\) direction is spacelike.

In the adjacent NUT region \(x>1\), while \(D>0\),

\[
g_{tt}<0
\]

and the same periodic direction is timelike, producing CTCs.

At the first horizon,

\[
D(1)=(1+\delta)^2.
\]

For the physical parameter range used in the source this is nonzero.

The exact geometry therefore does not insert an \(\alpha'\) curvature
singularity precisely at the first chronology horizon.

---

# 4. Preliminary wrapped-worldsheet diagnostic

**REPRODUCED HERE / diagnostic.**

At fixed angular coordinates take

\[
x=x(\tau),
\qquad
t=2\lambda w\,\sigma,
\qquad
0\le\sigma<2\pi,
\]

with integer \(w\).

The embedding closes because

\[
\Delta t
=
(2\lambda w)(2\pi)
=
w(4\pi\lambda),
\]

an integer multiple of the exact target period.

The induced metric is

\[
h_{\tau\tau}
=
(k-2)\frac{\dot x^2}{x^2-1},
\]

\[
h_{\sigma\sigma}
=
-(k-2)
\frac{x^2-1}{D(x)}
(2\lambda w)^2,
\]

\[
h_{\tau\sigma}=0.
\]

Hence

\[
\boxed{
\det h
=
-\frac{
(k-2)^2(2\lambda w)^2\dot x^2
}{
D(x)
}.
}
\]

The \(x^2-1\) factors cancel exactly.

At \(x=1\),

\[
\boxed{
\det h
\to
-\frac{
4\lambda^2w^2(k-2)^2\dot x^2
}{
(1+\delta)^2
},
}
\]

which is finite for finite \(\dot x\).

The exact dilaton gives

\[
e^{\Phi-\Phi_0}
=
D^{-1/4},
\]

so at \(x=1\),

\[
\boxed{
e^{\Phi-\Phi_0}
=
(1+\delta)^{-1/2},
}
\]

also finite.

Reproducibility:

    python src/symbolic/heterotic_taubnut_wrapped_probe.py

## 4.1 Interpretation

This rules out one very simple protection mechanism:

\[
\boxed{
\text{the first chronology horizon is not automatically a local divergence
of the Nambu--Goto area density for this wrapped ansatz.}
}
\]

It also rules out the claim that the first horizon is automatically excluded
by divergent \(g_s\).

## 4.2 Caveats

This calculation does **not** show that a physical heterotic string crosses.

It has not imposed:

- Polyakov conformal constraints;
- left/right Virasoro conditions;
- coset gauge constraints;
- BRST closure;
- BRST non-exactness;
- level matching;
- physical norm;
- normalizability;
- mutual locality of vertex operators;
- interacting factorization;
- a crossing amplitude.

The worldsheet interpretation of a static winding gauge also changes when the
target fiber changes from spacelike to timelike.

Therefore the result is only a local obstruction test.

---

# 5. Effective compact-circle intuition

On the Taub side,

\[
R_t^2(x)
\propto
(2\lambda)^2(k-2)
\frac{1-x^2}{D(x)}
\]

tends to zero as

\[
x\to1^-.
\]

So a naive **spacelike** compact-circle estimate would make winding modes
light near the horizon.

However:

\[
\boxed{
\text{do not continue }m_w^2\sim w^2R_t^2/\alpha'^2
\text{ into the timelike region and call it a tachyon proof.}
}
\]

The periodic direction is generated by a coset gauge identification, and
beyond the horizon it is timelike. The physical question belongs to the exact
gauged-CFT state conditions.

Possible outcomes remain:

- a perfectly physical chronology-sector state;
- a massless threshold;
- a tachyonic instability;
- a negative-norm state;
- nonnormalizability;
- disappearance from BRST cohomology;
- transition outside the unitary representation range.

No Taub--NUT-specific calculation resolving this was located in the targeted
search.

---

# 6. Exact CFT data needed for the physical-state gate

The minimum data are now quite specific.

## 6.1 Numerator and gauging

The parent current algebra is

\[
SL(2,\mathbb R)_k\times SU(2)_{k-4}
\]

plus the heterotic fermion/current sector.

The quotient gauges

\[
U(1)_A\times U(1)_B
\]

asymmetrically.

The right \(SL(2,\mathbb R)\) \(U(1)_B\) generator is proportional to

\[
-\lambda \sigma_3/2,
\]

and the right \(SU(2)\) \(U(1)_B\) generator to

\[
-i\sigma_3/2.
\]

Left-moving fermionic charges participate in anomaly cancellation.

Therefore a physical vertex operator must obey coupled gauge-neutrality/BRST
conditions involving several sectors, not simply a free-boson
momentum-winding mass shell.

## 6.2 The chronology-direction state-map problem

The critical target-space fact is

\[
t\sim t+4\pi\lambda.
\]

But this identification is generated by a **large gauge transformation**.

Consequently the precise relation

\[
\boxed{
w_t
\longleftrightarrow
\text{affine }SL(2,\mathbb R)\text{ labels}
+
SU(2)\text{ labels}
+
U(1)_B\text{ gauge/holonomy sector}
+
\text{heterotic charges}
}
\]

must be established before one can call \(w_t\) a physical winding quantum
number in the exact coset Hilbert space.

The audited geometry papers do not supply this map at the level required for
the operational-traversal question.

This is the current **first full-CFT bottleneck**.

---

# 7. BRST / physical-state sector

**OPEN.**

To establish Level B one needs explicit physical operators/states satisfying:

\[
Q_{\rm BRST}|\Psi\rangle=0,
\]

modulo BRST-exact states, together with:

- gauged \(U(1)_A,U(1)_B\) constraints;
- left/right Virasoro mass-shell conditions;
- level matching;
- heterotic GSO/unitarity conditions as appropriate;
- normalizability in the relevant noncompact \(SL(2,\mathbb R)\) direction;
- positive physical norm.

The chronology-related state should have a semiclassical target interpretation
that approaches the periodic \(t\) fiber from the Taub patch and continues to
the NUT patch.

The present search did not locate a paper that constructs this sector
explicitly for the exact Lorentzian heterotic Taub--NUT model.

Generic heterotic-coset formalism is not enough to mark this gate as passed.

---

## 7.1 Nearby BRST technology already exists

**PUBLISHED RESULT / methodological prior art.**

The absence of a Taub--NUT-specific chronology-state calculation should not be
confused with absence of BRST technology for asymmetric heterotic cosets.

For related \(SL(2,\mathbb R)\times U(1)\) asymmetric gauged-WZW models,
physical vertex operators have been constructed by:

1. introducing the coset gauge ghosts and auxiliary boson;
2. constructing a nilpotent \(U(1)\) BRST current;
3. requiring affine primaries dressed by the gauge boson to be BRST closed;
4. imposing Virasoro/mass-shell conditions;
5. quotienting BRST-exact polarizations.

The ordinary \(SL(2,\mathbb R)/U(1)\) black-hole coset also has a substantial
literature on explicit vertex operators, spectrum, and BRST cohomology.

Therefore the next Taub--NUT step is technically well posed:

\[
\boxed{
\text{generalize the known one-}U(1)\text{ BRST construction to the actual }
U(1)_A\times U(1)_B\text{ heterotic gauging.}
}
\]

What remains special to Taub--NUT is that the chronology fiber is tied to the
large \(U(1)_B\) identification.  The physical state must therefore combine
affine Cartan charges, heterotic left charges, and the gauge topological
sector consistently.

This sharply reduces the novelty target: the new content, if any, would be
the **Taub--NUT chronology-sector application**, not BRST quantization of
gauged WZW models itself.

# 7.2 State-map gate — partial resolution

**Status: REPRODUCED FROM SOURCE CONVENTIONS + NEW SYNTHESIS.**

The state-map problem can now be sharpened beyond the statement
"the fiber periodicity comes from gauging."

## 7.2.1 Exact nonzero gauge embeddings

For the nonrotating model the nonzero bosonic gauge generators may be written,
in the source conventions, as

\[
t^{(1)}_{A,L}=+\frac{\sigma_3}{2},
\qquad
t^{(1)}_{A,R}=-\delta\,\frac{\sigma_3}{2},
\]

\[
t^{(1)}_{B,R}=-\lambda\,\frac{\sigma_3}{2},
\qquad
t^{(2)}_{B,R}=-i\,\frac{\sigma_3}{2},
\]

with the omitted \(A/B\) actions zero.

Equivalently, the group action is

\[
g_1
\longrightarrow
e^{\epsilon_A\sigma_3/2}\,
g_1\,
e^{(\delta\epsilon_A+\lambda\epsilon_B)\sigma_3/2},
\]

\[
g_2
\longrightarrow
g_2\,e^{i\epsilon_B\sigma_3/2}.
\]

The left heterotic fermions have charge vectors

\[
(Q_A,P_A),
\qquad
(Q_B,P_B)
\]

under \(U(1)_A,U(1)_B\), while the right supersymmetric fermion embedding is
fixed by

\[
(\delta,0)
\quad\text{and}\quad
(\lambda,1).
\]

The anomaly-cancellation equations are

\[
\boxed{
-k_1(1-\delta^2)
=
2\left(Q_A^2+P_A^2-\delta^2\right),
}
\]

\[
\boxed{
k_1\delta\lambda
=
2\left(
Q_AQ_B+P_AP_B-\delta\lambda
\right),
}
\]

\[
\boxed{
k_2+k_1\lambda^2
=
2\left(
Q_B^2+P_B^2-(1+\lambda^2)
\right),
}
\]

with

\[
\boxed{
k_1=k_2+4.
}
\]

These are not optional charge decorations: the left-moving gauge sector is of
order \(\sqrt{k}\) and is part of the exact heterotic construction.

## 7.2.2 Zero-mode gauge constraints on a candidate affine primary

Let a parent-state candidate carry:

- \(SL(2,\mathbb R)\) affine labels
  \[
  (j;m,\bar m);
  \]
- \(SU(2)\) affine labels
  \[
  (\ell;n,\bar n);
  \]
- a left heterotic charge vector
  \[
  \mathbf s=(s_1,s_2).
  \]

It is convenient to absorb the right-moving supersymmetric-fermion Cartan
charges into total right charges

\[
\bar M,\qquad \bar N,
\]

for the \(SL(2,\mathbb R)\) and \(SU(2)\) Cartans respectively.

The necessary gauge-neutrality conditions then take the zero-mode form

\[
\boxed{
\mathcal G_A
=
m+\delta\,\bar M
+
Q_A s_1+P_A s_2
=
0,
}
\]

\[
\boxed{
\mathcal G_B
=
\lambda\,\bar M+\bar N
+
Q_B s_1+P_B s_2
=
0.
}
\]

The precise normalization of \(m,\bar M,\bar N,s_i\) depends on the affine and
fermion bosonization conventions, but the **linear combinations are fixed by
the exact gauge embedding above**.

These equations are necessary BRST/gauge constraints, not the full physical
state conditions.  Full BRST cohomology also requires the auxiliary
\(H=U(1)_A\times U(1)_B\) coset sector and ghosts, together with the Virasoro
conditions.

A useful consequence is immediate:

\[
\boxed{
\text{a local gauge-invariant primary with }\mathcal G_B=0
\text{ does not carry }w
\text{ simply as a nonzero }U(1)_B\text{ charge}.
}
\]

So the chronology winding integer is not encoded by violating the local gauge
constraint.

## 7.2.3 Lift of the target-space winding to the parent gauged model

Take the target-space winding condition

\[
\Delta t=4\pi\lambda w,
\qquad
w\in\mathbb Z.
\]

The exact source shows that this is generated by the finite transformation

\[
\epsilon_B=4\pi w.
\]

Before gauge fixing, the corresponding parent-field boundary condition is

\[
\boxed{
g_1(\sigma+2\pi)
=
g_1(\sigma)\,
e^{2\pi\lambda w\sigma_3},
}
\]

while

\[
\boxed{
g_2(\sigma+2\pi)
=
g_2(\sigma)\,
e^{2\pi i w\sigma_3}
=
g_2(\sigma).
}
\]

Thus the same integer \(w\) that becomes target-space \(t\)-winding is a
**right-Cartan twist of the parent \(SL(2,\mathbb R)\) WZW field**.

It is not ordinary free-boson winding.

## 7.2.4 The heterotic fermion sector twists at the same time

The bosonized fermion action contains the covariant combinations

\[
D\Phi_1
=
d\Phi_1
-
(Q_A+\delta)A^A
-
(Q_B+\lambda)A^B,
\]

\[
D\Phi_2
=
d\Phi_2
-
P_A A^A
-
(P_B+1)A^B.
\]

Hence

\[
\delta\Phi_1
=
(Q_A+\delta)\epsilon_A
+
(Q_B+\lambda)\epsilon_B,
\]

\[
\delta\Phi_2
=
P_A\epsilon_A
+
(P_B+1)\epsilon_B.
\]

For the chronology transformation,

\[
\epsilon_A=0,
\qquad
\epsilon_B=4\pi w,
\]

one gets

\[
\boxed{
\Delta\Phi_1
=
4\pi w(Q_B+\lambda),
}
\]

\[
\boxed{
\Delta\Phi_2
=
4\pi w(P_B+1).
}
\]

Therefore an exact-CFT lift of a string that winds the target \(t\) circle is
not a configuration in which only \(t\) winds.

It is a **combined monodromy sector**

\[
\boxed{
\text{target }t\text{ winding}
\;\Longleftrightarrow\;
SL(2,\mathbb R)_R\text{ Cartan twist}
+
\text{heterotic fermion-sector twist},
}
\]

with the \(SU(2)_R\) endpoint returning to itself after an integer \(4\pi\)
rotation.

This is the main state-map result of the present pass.

It also sharpens the interpretation of the earlier Nambu--Goto calculation:
the fixed-angle \(t\)-only winding ansatz is a useful target-space probe, but
it is **not yet a lift of a complete exact-CFT state** because it omits the
correlated gauge/fermion monodromy.

## 7.2.5 What is \(w\) in the Hilbert space?

The safest present statement is:

\[
\boxed{
w
\text{ labels a boundary-condition / gauge-transition sector, not a local
gauge charge.}
}
\]

A loop in the quotient lifts to a path in the parent theory whose endpoints
are related by the finite \(U(1)_B\) gauge transformation
\(\epsilon_B=4\pi w\).

In affine language the \(SL(2,\mathbb R)\) factor therefore lies in a
Cartan-twisted sector.

This resembles the hyperbolic spectral-flow construction used for strings on
BTZ quotients, where twisted sectors are generated by spectral flow in the
hyperbolic basis.  That literature is useful methodology, but it does **not**
by itself provide the Taub--NUT heterotic spectrum because here:

1. the twist coefficient is the embedded parameter \(\lambda w\);
2. the quotient is asymmetrically gauged;
3. \(SU(2)_R\) participates in the same \(U(1)_B\) action;
4. the left heterotic charge lattice is required by anomaly cancellation.

Accordingly, do **not** import the standard integer
\(SL(2,\mathbb R)\) spectral-flow formulas without deriving the shifts in the
actual embedded gauge current.

## 7.2.6 State-map gate status

The original state-map question is now partly resolved.

### Established

\[
\boxed{
\Delta t=4\pi\lambda w
}
\]

corresponds to a definite combined parent-field monodromy generated by
\(\epsilon_B=4\pi w\).

The required local gauge-neutrality combinations are also identified.

### Not established

It remains to quantize that twisted sector and determine:

- the exact shifted affine zero modes;
- the conformal weights \(L_0,\bar L_0\);
- level matching;
- BRST closure and non-exactness in the twisted sector;
- the allowed \(SL(2,\mathbb R)\) representation \(j\);
- normalizability;
- positive physical norm / no-ghost range.

Therefore no stop condition has fired yet:

\[
\boxed{
\text{the chronology sector has not been shown absent,
but it has not been shown physical.}
}
\]

## 7.2.7 Smallest next calculation

The next task is no longer to guess a winding mass.

It is to derive the current-algebra twist produced by

\[
g_1(\sigma+2\pi)
=
g_1(\sigma)e^{2\pi\lambda w\sigma_3}
\]

and the simultaneous fermion-boson shifts above.

The desired output is a set of twisted-sector formulas of the form

\[
\bar J^3_0
\to
\bar J^3_0+\Delta_w\bar J^3_0,
\]

\[
\bar K^3_0
\to
\bar K^3_0+\Delta_w\bar K^3_0,
\]

together with the compensating heterotic charge-sector contribution such that

\[
\mathcal G_A=\mathcal G_B=0
\]

remains satisfied.

Only after obtaining the corresponding

\[
L_0,\qquad \bar L_0
\]

should the analysis ask whether a normalizable unitary chronology-sector state
exists.



## 7.3 Twisted-sector existence and quantization gate

**Status (Phase IV): RESOLVED — Outcome A, \(w\) is gauge-trivial.**

Full derivation, prior-art table, and executable checks:

- notes/fable-heterotic-ctc-operational-traversal.md
- src/symbolic/heterotic_taubnut_twist_zero_modes.py
- src/symbolic/heterotic_taubnut_level_matching.py

Summary:

1. The subgroup actually gauged is \(H=\mathbb R_A\times\mathbb R_B\)
   (the \(U(1)_B\) generator is hyperbolic on \(SL(2,\mathbb R)\), so its
   one-parameter group never closes).  \(H\) is connected and contractible;
   \(\epsilon_B=4\pi\) is a constant gauge element, not a topologically
   large transformation.
2. At fixed \(x\neq\pm1\) the quotient of
   \((t_L,t_R,g_2)\) by \(H\) is \(SU(2)=S^3\) and the \(t\)-circle is the
   Hopf fibre (as Johnson–Svendsen state).  The chronology loop is
   contractible.
3. The twisted lift
   \(g_1(\sigma+2\pi)=g_1(\sigma)e^{2\pi\lambda w\sigma_3}\) is the gauge
   image, under \(\epsilon_B(\sigma)=-2w\sigma\), of a periodic lift with
   \(g_1\) constant and \(g_2\) wound \(w\) times along the Hopf fibre.  In
   the compact/unfolded description the \(w\)-sectors are field-identification
   images of the untwisted sector.
4. The local combinations shift as
   \(\mathcal G_B^{(w)}-\mathcal G_B^{(0)}=4w(Q_B^2+P_B^2)\),
   \(\mathcal G_A^{(w)}-\mathcal G_A^{(0)}=4w(Q_AQ_B+P_AP_B)\); the full
   BRST constraints including the auxiliary gauge bosons are invariant, and
   \(L_0^{(w)}=L_0^{(0)}\), \(\bar L_0^{(w)}=\bar L_0^{(0)}\) on physical
   states.  Level matching is inherited.
5. The hyperbolic twisted currents have
   \(\bar J^\pm_n\to\bar J^\pm_{n\pm2i\lambda w}\),
   \(\Delta\bar J^3_0=-k_1\lambda w\); the same transformation is the
   integer flow \(\bar K^\pm_n\to\bar K^\pm_{n\mp2w}\) on \(SU(2)_R\).

Consequence: there is no winding superselection sector, hence no Misner- or
BTZ-type winding-string chronology mechanism in this model.  This is not
chronology protection.  The Level B/C question moves to the untwisted
spectrum (Hopf-wound states with \(\bar N\simeq k_2w\)).

---

# 8. Minisuperspace crossing diagnostic

**NOT YET PERFORMED in this note.**

Svendsen 2006 analyzes classical test particles and global continuation.
That is useful geometric evidence but is weaker than a string-state
calculation.

The next controlled intermediate calculation, if the full BRST construction
is not immediately tractable, is:

1. derive the scalar/minisuperspace wave operator from the exact metric,
   dilaton, gauge field, and \(B\)-field;
2. separate modes carrying the \(t\)-fiber quantum number;
3. compute the conserved radial flux;
4. solve the near-\(x=1\) connection problem;
5. determine a reflection/transmission coefficient or wave-packet transfer.

A nonzero transmission coefficient would still establish only

\[
\boxed{
\text{minisuperspace crossing}
\neq
\text{full BRST string traversal}.
}
\]

It would nevertheless test whether there is a second local obstruction beyond
the wrapped-area gate.

---

# 9. Exact-CFT crossing observable

**OPEN.**

An ordinary target-space S-matrix should not be assumed because the geometry
does not provide the usual globally asymptotically flat scattering setup.

The first meaningful exact-CFT Level-B/C observable could instead be:

- a two-point/reflection amplitude for identified physical coset states;
- overlap of physical wave packets with semiclassical support in Taub and NUT;
- a transfer/reflection matrix;
- a BRST-invariant correlator whose saddle/localization has a clear
  Taub-to-NUT interpretation.

The minimum desired statement is

\[
\boxed{
\mathcal A_{\rm Taub\to NUT}\neq0
}
\]

for well-defined physical states.

But it must answer:

- what state is prepared;
- what state is detected;
- how target-space localization is defined;
- why the observable is gauge/BRST invariant;
- whether it is finite;
- what precisely "crossing" means in the quotient CFT.

No such Taub--NUT-specific observable was identified in this search.

---

# 10. Operational closed-timelike return

Even successful horizon crossing is not yet operational time travel.

The Level-C criterion requires a physical observable corresponding to a
complete closed timelike history.

Possible definitions include:

- a controlled state carrying the chronology-direction winding through a full
  NUT cycle;
- a correlator connecting a chronal preparation to a relationally defined
  event in its target-space causal past after the CTC winding;
- a gauge-invariant return amplitude that cannot be reinterpreted merely as
  support in a region containing CTCs.

No such observable was identified for the heterotic Taub--NUT coset.

Therefore:

\[
\boxed{
\text{CTC geometry}
+
\text{even possible probe crossing}
\not\Rightarrow
\text{operational closed-timelike return}.
}
\]

---

# 11. Interaction / instability gate

A one-string result would be insufficient.

The first controlled interacting test should ask whether chronology-sector
vertex operators have:

- finite OPE coefficients;
- mutual locality;
- sensible factorization;
- finite tree-level correlators;
- a consistent optical/factorization interpretation;
- no tachyonic or condensate instability that appears before operational use.

The comparison models show that this is not optional.

## 11.1 Heterotic Gödel/AdS

**PUBLISHED RESULT.**

The exact heterotic Gödel/AdS model has a computed physical spectrum and
modular-invariant genus-one partition function.

Long strings associated with the chronology-violating regime destabilize the
background; a new exact background describing a condensation endpoint avoids
CTCs.

This is direct evidence that exact-CFT control can turn chronology protection
into a **spectrum/instability** phenomenon rather than geometric excision.

## 11.2 Misner orbifold

**PUBLISHED RESULT.**

Physical twisted states include:

- short strings winding a spacelike circle in Milne regions;
- long strings winding a timelike compact direction in whisker regions.

But:

- winding-string pair production becomes strong;
- the one-loop amplitude has singularities;
- some tree-level amplitudes involving twisted states diverge.

Thus physical support in a CTC region does not imply interaction-controlled
operational use.

## 11.3 Taub--NUT status

For the exact heterotic Taub--NUT chronology sector, an analogous spectrum /
interaction calculation was not identified.

So the model has not yet passed this gate.

---

# 12. \(g_s\) / genus-control gate

The coset geometry is exact in \(\alpha'\).

It is not automatically exact in the string-loop expansion:

\[
\boxed{
\alpha'\text{-exact}
\neq
g_s\text{-exact}.
}
\]

At the first chronology horizon \(x=1\),

\[
D(1)=(1+\delta)^2
\]

and

\[
e^{\Phi-\Phi_0}=D^{-1/4}
\]

is finite.

Therefore the first horizon is not trivially a strong-coupling wall.

The source papers do identify strong-coupling behavior near some curvature
singularities deeper in the global extension; the later global analysis uses
T-duality to relate problematic regions to better-behaved descriptions.

For operational traversal, the unresolved tasks are:

1. fix the overall asymptotic/string-coupling normalization;
2. follow \(g_s\) along the proposed string process;
3. determine whether the relevant NUT segment remains perturbative;
4. compute at least the first interacting/worldsheet-loop observable;
5. test whether winding backreaction invalidates the fixed background.

Thus the wrapped-probe negative result is meaningful but not sufficient.

---

# 13. Comparison table

| Model | Exact/fundamental control | Probe enters CTC region? | Interactions controlled? | Instability? | Dynamical formation? |
|---|---|---|---|---|---|
| Heterotic Taub--NUT | exact heterotic coset, \(\alpha'\)-exact target fields | **OPEN at full BRST level**; local wrapped-area barrier absent | OPEN | OPEN | no |
| Heterotic Gödel/AdS | exact marginal CFT | long-string sector studied | spectrum + genus one studied | strong long-string instability | no |
| M-theory Gödel | supergravity/M-theory probe regime | M2 probes cross CTC horizon | limited | model dependent | no |
| Misner orbifold | exact orbifold background perturbatively | yes, fixed-background twisted sectors | problematic | pair production / loop and amplitude singularities | no |
| Holographic time machine | controlled holographic regime | no operational crossing in studied construction | interacting boundary CFT controlled | disconnection/backreaction | not a formation example |

The only potentially new calculation target here is therefore:

\[
\boxed{
\text{Taub--NUT-specific exact-CFT physical traversal}.
}
\]

---

# 14. What is actually established

## PUBLISHED RESULT

1. The heterotic Taub--NUT background has a full coset-CFT definition.
2. Its target geometry can be computed exactly in \(\alpha'\).
3. The Taub/NUT chronology structure and CTC regions survive those
   corrections.
4. The target fiber is periodic because of a large \(U(1)_B\) gauge
   identification.
5. The first chronology horizon is not removed by the exact target geometry.
6. Later work studies analytic continuation, test-particle motion, and
   T-duality globally.
7. Other exact CTC string models admit physical chronology-related states,
   probe crossing, and/or stringy chronology-protection instabilities.

## REPRODUCED HERE

For the exact nonrotating Taub--NUT fiber conventions:

\[
D(x)
=
(x+\delta)^2-\frac4{k+2}(x^2-1),
\]

\[
t\sim t+4\pi\lambda,
\]

and the fixed-angle winding ansatz gives

\[
\boxed{
\det h
=
-\frac{
(k-2)^2(2\lambda w)^2\dot x^2
}{
D(x)
}.
}
\]

Therefore there is no \(x^2-1\) divergence at \(x=1\).

Also,

\[
e^{\Phi-\Phi_0}
=
D^{-1/4}
\]

is finite at that horizon.

## NOT ESTABLISHED

1. the precise BRST cohomology of the chronology-direction sector;
2. ~~the quantization of the combined \(U(1)_B\) monodromy sector~~
   (resolved in Phase IV: the sector is gauge-trivial; see §7.3) — replaced
   by: the untwisted spectrum with \(\mathcal G_A=\mathcal G_B=0\)
   resolved and the normalizability of the Hopf-wound states;
3. normalizable physical string transmission Taub\(\to\)NUT;
4. a finite exact-CFT crossing amplitude;
5. interaction-controlled propagation in the CTC sector;
6. a BRST-invariant operational closed-timelike-return observable;
7. dynamical formation of this exact background from chronal data.

---

# 15. Exact remaining gap

**Updated in Phase IV.**  The twisted-sector quantization gate is closed:
\(w\) is gauge-trivial (§7.3).  The next calculation should therefore
**not** be a twisted-state observable.

The first unresolved problem is now:

\[
\boxed{
\textbf{Untwisted chronology-state gate:}
\quad
\text{resolve }\mathcal G_A=\mathcal G_B=0\text{ with the Virasoro
conditions in the hyperbolic }SL(2,\mathbb R)\text{ basis and test
normalizability/localization of the }\bar N\simeq k_2 w\text{ states across }x=1.
}
\]

Concretely:

1. classify affine primaries
   \((j;m,\bar m)\otimes(\ell;n,\bar n)\otimes\mathbf s\) satisfying both
   gauge constraints, with \(\bar M\) quantized by \(\mathcal G_B=0\)
   (energy quantization on the periodic time direction);
2. derive the minisuperspace wave equation for a \(t\)-momentum eigenstate
   in the exact \((x,t)\) fiber block;
3. determine whether any normalizable state is supported in the NUT region
   and whether the Hopf-wound representatives are among them;
4. only then formulate a gauge-invariant Taub\(\to\)NUT two-point /
   reflection observable.

If no such state exists, record a model-specific obstruction; if it does,
proceed to the smallest crossing observable.

---

# 16. Novelty / status map

### Exact CTC geometry survives all \(\alpha'\) corrections considered

**PUBLISHED RESULT.**

No novelty claim.

### Local wrapped-string area density is finite at \(x=1\)

**REPRODUCED HERE / diagnostic.**

This is a small direct calculation in the exact source conventions. It is not
a physical-state traversal result.

### Exact dilaton is finite at the first chronology horizon

**PUBLISHED RESULT / REPRODUCED algebraically here.**

No strong-\(g_s\) wall is forced at \(x=1\) by the exact dilaton formula.

### Taub--NUT chronology-fiber winding as a simple free compact-boson quantum number

**NOT ESTABLISHED / likely oversimplified.**

The target periodicity is generated by a large gauged \(U(1)_B\)
transformation.

### Taub--NUT chronology winding as a twisted / spectral-flow sector

**RESOLVED NEGATIVE (Phase IV).**  The gauged group is connected; the
\(w\)-monodromy is a trivializable clutching datum and the chronology circle
is a Hopf fibre.  No twisted sector exists.  See §7.3.

### Taub--NUT-specific BRST physical traversal

**OPEN in the targeted search.**

No novelty claim should be made until a deeper citation/representation search
is completed.

### Exact heterotic Taub--NUT as an operational time-machine counterexample

**COUNTEREXAMPLE CANDIDATE, NOT ESTABLISHED.**

Level A is strong; Levels B/C remain open; Level D is absent.

---

# 17. References

1. C. V. Johnson, H. G. Svendsen,
   *Exact string theory model of closed timelike curves and cosmological
   singularities*, Phys. Rev. D **70**, 126011 (2004),
   arXiv:hep-th/0405141.

2. H. G. Svendsen,
   *The Exact Geometry of a Kerr--Taub--NUT Solution of String Theory*,
   Phys. Rev. D **71**, 044027 (2005),
   arXiv:hep-th/0410011.

3. H. G. Svendsen,
   *Global properties of an exact string theory solution in two and four
   dimensions*, Phys. Rev. D **73**, 064032 (2006),
   arXiv:hep-th/0511289.

4. C. V. Johnson,
   *Heterotic Cosets*,
   arXiv:hep-th/9409061.

5. D. Israël,
   *Quantization of heterotic strings in a Gödel/Anti de Sitter spacetime and
   chronology protection*,
   JHEP **01** (2004) 042,
   arXiv:hep-th/0310158.

6. Y. Hikida, S.-J. Rey,
   *Can branes travel beyond CTC horizon in Gödel Universe?*,
   Nucl. Phys. B **669** (2003) 57--77,
   arXiv:hep-th/0306148.

7. M. Berkooz, B. Pioline, M. Rozali,
   *Closed Strings in Misner Space: Cosmological Production of Winding
   Strings*,
   JCAP **08** (2004) 004,
   arXiv:hep-th/0405126.

8. M. Berkooz, B. Durin, B. Pioline, D. Reichmann,
   *Closed Strings in Misner Space: Stringy Fuzziness with a Twist*,
   arXiv:hep-th/0407216.

9. K. Itoh, H. Kunitomo, N. Ohta, M. Sakaguchi,
   *BRST Analysis of Physical States in Two-Dimensional Black Hole*,
   Phys. Rev. D **48**, 3793 (1993),
   arXiv:hep-th/9305179.

10. D. P. Jatkar,
    *The Spectrum of \(SL(2,R)/U(1)\) Black Hole Conformal Field Theory*,
    Nucl. Phys. B **395**, 167 (1993),
    arXiv:hep-th/9203063.

11. H. G. Svendsen,
    *Aspects of plane waves and Taub--NUT as exact string theory solutions*,
    PhD thesis, Durham University (2004).

12. S. Hemming, E. Keski-Vakkuri,
    *The spectrum of strings on BTZ black holes and spectral flow in the
    SL(2,R) WZW model*,
    Nucl. Phys. B **626**, 363 (2002),
    arXiv:hep-th/0110252.


---

# 18. Restart point

Do not recompute the metric, wrapped determinant, large-gauge
identification, or the twisted-sector analysis.

Phase IV result: \(w\) is gauge-trivial; the chronology circle is a gauged
Hopf fibre; the twisted lift is the gauge image of an untwisted Hopf-wound
state (notes/fable-heterotic-ctc-operational-traversal.md).

Continue from:

\[
\boxed{
\text{Untwisted chronology-state gate (§15).}
}
\]

Next:

1. resolve \(\mathcal G_A=\mathcal G_B=0\) together with the Virasoro
   conditions in the hyperbolic basis;
2. minisuperspace wave equation for \(t\)-momentum eigenstates in the exact
   fiber block;
3. normalizability and NUT-region localization of the
   \(\bar N\simeq k_2w\) states;
4. stop if none survives; otherwise formulate the smallest Taub\(\to\)NUT
   crossing observable.

The BTZ hyperbolic-spectral-flow formulas are the gauge-image description of
untwisted states here, not a source of new sectors.
