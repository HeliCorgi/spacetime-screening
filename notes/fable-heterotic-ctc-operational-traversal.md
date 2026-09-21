# Exact Heterotic Taub–NUT CFT: Twisted-Sector Existence and Quantization Gate

**Status:** Phase IV chronology side branch (continues Phase III).

Status labels used below:

- **PUBLISHED RESULT**
- **REPRODUCED HERE**
- **NEW CALCULATION CANDIDATE**
- **SYNTHESIS / CRITERION**
- **COUNTEREXAMPLE CANDIDATE**
- **OPEN**

This note continues:

- notes/heterotic-ctc-operational-traversal.md (Phase III, state-map gate)

and does **not** revisit the exact metric, the wrapped Nambu–Goto
determinant, the Misner/KRW analysis, the general realizability audit, the
origin of \(t\sim t+4\pi\lambda\), the parent monodromy
\(g_1(\sigma+2\pi)=g_1(\sigma)e^{2\pi\lambda w\sigma_3}\), the heterotic
boson shifts \(\Delta\Phi_{1,2}\), or the local neutrality combinations
\(\mathcal G_A,\mathcal G_B\).  All of these are taken as input.

Executable checks (SymPy, run in CI):

- src/symbolic/heterotic_taubnut_twist_zero_modes.py
- src/symbolic/heterotic_taubnut_level_matching.py

The adversarial question of this phase is

\[
\boxed{
\text{Does the large-}U(1)_B\text{ chronology monodromy }\epsilon_B=4\pi w
\text{ survive exact heterotic coset quantization as a healthy physical
state sector?}
}
\]

---

# 0. Executive result

\[
\boxed{
\textbf{Outcome A: } w \text{ is gauge-trivial.}
}
\]

The integer \(w\) does **not** label an independent sector of the exact
gauged heterotic Taub–NUT CFT.  Three independent formulations give the same
answer:

1. **Target-space topology (PUBLISHED RESULT, Misner 1963; Johnson–Svendsen
   2004).**  Constant-\(x\) slices of the exact background are
   \(S^3\) with the periodic coordinate \(t\) as the circle fibred over
   \(S^2\).  The chronology circle is a Hopf fibre and is homotopically
   trivial.  A closed string cannot carry a conserved winding number around
   it.

2. **Gauged-WZW global structure (REPRODUCED HERE / SYNTHESIS).**  The
   subgroup of \(SL(2,\mathbb R)\times SU(2)\) actually gauged is
   \(H=\mathbb R_A\times\mathbb R_B\): the \(U(1)_B\) generator is hyperbolic
   on \(SL(2,\mathbb R)\), so its one-parameter group never closes.  \(H\) is
   connected and contractible.  Every principal \(H\)-bundle on the
   closed-string circle is trivial, all parent fields are periodic, and the
   "twisted" boundary condition
   \(g_1(\sigma+2\pi)=g_1(\sigma)e^{2\pi\lambda w\sigma_3}\) is a
   clutching description of the *same* configuration space.  Explicitly, the
   \(\sigma\)-dependent gauge parameter \(\epsilon_B(\sigma)=-2w\sigma\)
   maps the twisted lift to a periodic lift with \(g_1\) constant and \(g_2\)
   winding \(w\) times along the Hopf fibre (checked by
   \(2\times2\) matrix algebra in the first script).

3. **Coset field identification (SYNTHESIS).**  In the equivalent "unfolded"
   description in which \(U(1)_B\) is compact and the parent
   \(SL(2,\mathbb R)\) carries the extremal-BTZ-like hyperbolic
   identification \(g_1\sim g_1e^{2\pi\lambda\sigma_3}\), the \(w\)-twisted
   sectors exist as orbifold sectors but are mapped onto the untwisted
   sector by the winding \(U(1)_B\) gauge transformation.  This is the
   standard field-identification / spectral-flow orbit of coset models: the
   physical Hilbert space contains each orbit once.  The identification
   preserves the full BRST constraints and \(L_0,\bar L_0\) exactly
   (second script).

The stop condition "\(w\neq0\) is globally gauge-trivial" of the phase task
therefore fires.

What this does and does not mean:

- It **removes** the "twisted-sector / winding-string" route to an
  operational CTC observable: there is no Misner- or BTZ-type winding
  superselection sector in this model, hence no Berkooz–Pioline-type
  winding-string pair-production channel and no BTZ-type hyperbolic
  spectral-flow spectrum to compute.
- It does **not** establish chronology protection.  Strings that
  semiclassically wrap the timelike \(t\)-circle in the NUT region do exist
  as *untwisted* states: they are \(SU(2)_R\) spectral-flow images (even
  flow \(2w\)) of ordinary states, with large right Cartan charge
  \(\bar N\simeq k_2w\), balanced in \(\mathcal G_B=0\) by
  \(\lambda\bar M\) and the heterotic left charges.  They are not
  topologically protected and can unwind.
- The chronology question for this model is thereby **reclassified**: it is
  a question about the untwisted spectrum and its localization across
  \(x=\pm1\), not about a new sector.

---

# 1. Prior-art check

A narrow search was run (web search, arXiv abstracts, one full-text check)
for the global quantization of asymmetrically gauged WZW / heterotic cosets
with nontrivial gauge holonomies and for any quantization of the Taub–NUT
coset itself.  "Verified" below means the abstract or text was checked in
this pass; "partially verified" means the citation was checked but the
specific claim rests on standard secondary literature.

| Question | Prior art | Applicable directly? | What remains Taub–NUT-specific? |
|---|---|---|---|
| Non-compact \(\mathbb R^2\) gauging of \(SL(2,\mathbb R)\times SU(2)\) and its global space | Bars–Sfetsos, PLB 301 (1993) 183 [hep-th/9208001]; PRD 46 (1992) 4495 [hep-th/9205037] (verified: gauged group is the non-compact \(\mathbb R^2\); global coordinates found) | Yes, as the bosonic template | Asymmetric heterotic \(U(1)_A\times U(1)_B\) embedding; periodic-\(t\) sector |
| Sum over gauge-bundle sectors and large gauge transformations in gauged WZW | Hori, CMP 182 (1996) 1 [hep-th/9411134] (verified: topological sectors of the gauge field; actions of \(\pi_1\) of the gauge group relating sectors) | Yes, general machinery | Whether the \(t\)-circle is a gauge-trivial orbit; here shown yes |
| Field identification = spectral-flow / simple-current orbit in cosets | Gepner, PLB 222 (1989) 207; Moore–Seiberg, PLB 220 (1989) 422; Schellekens–Yankielowicz, NPB 334 (1990) 67 (partially verified) | Yes as a principle | Application to the asymmetric two-\(U(1)\) heterotic coset |
| Asymmetric heterotic cosets, partition functions with gauge holonomies | Israël–Kounnas–Orlando–Petropoulos, Fortsch. Phys. 53 (2005) 1030 [hep-th/0412220]; Fortsch. Phys. 53 (2005) 73 [hep-th/0405213] (verified: left/right asymmetric embeddings \(\epsilon_L,\epsilon_R\), compact examples) | Yes, same technology as Johnson–Svendsen | Taub–NUT combination not treated; winding spectrum not treated |
| BTZ winding sectors as hyperbolic spectral flow | Hemming–Keski-Vakkuri [hep-th/0110252]; Natsuume–Satoh [hep-th/9611041]; Martinec–McElgin [hep-th/0106171] (verified: sectors exist because BTZ is a *discrete orbifold*) | Methodology only | The Taub–NUT twist sits inside a *connected gauged* group; see §9 |
| Worldsheet quantization of the Johnson–Svendsen Taub–NUT coset (spectrum, twisted sectors, \(t\)-winding) | **NOT FOUND**; Svendsen [hep-th/0410011], [hep-th/0511289] are classical-geometry papers | — | Entire spectral analysis open; the present note settles only the sector question |
| Taub–NUT topology \(\mathbb R\times S^3\), time circle = Hopf fibre, CTCs contractible | Misner, J. Math. Phys. 4 (1963) 924 (verified: \(r=\)const slices are \(S^3\), time orbits are circles); Hawking–Ellis ch. 5 | Yes | Survival at the exact-CFT level: shown here |
| Does Johnson–Svendsen exhibit the fibration? | Johnson–Svendsen [hep-th/0405141] (verified: "constant radial slices have the topology of an \(S^3\) where the time is a circle fibred over the \(S^2\)"; metric term \((dt+2\lambda A^M_\phi d\phi)^2\) with a Dirac-monopole \(A^M_\phi\)) | Yes, directly | They do not ask whether \(t\)-winding is a twisted sector |

No paper was found that derives the exact Taub–NUT \(U(1)_B\) sector
quantization.  The sector question is settled below from standard
ingredients; the spectral questions remain open.

---

# 2. Global \(U(1)_B\) sector and holonomy

## 2.1 What group is gauged

**REPRODUCED HERE.**

In the hyperbolic chart
\(g_1=e^{t_L\sigma_3/2}h(x)e^{t_R\sigma_3/2}\),
\(g_2=e^{i\phi\sigma_3/2}e^{i\theta\sigma_2/2}e^{i\psi\sigma_3/2}\),
the gauge action of the previous phase reads

\[
(t_L,t_R,\psi)
\longrightarrow
(t_L+\epsilon_A,\;
t_R+\delta\epsilon_A+\lambda\epsilon_B,\;
\psi+\epsilon_B).
\]

The one-parameter subgroup generated by the \(U(1)_B\) generator is

\[
\{(e^{\lambda\epsilon\sigma_3/2},\,e^{i\epsilon\sigma_3/2}):\epsilon\in\mathbb R\}
\subset SL(2,\mathbb R)\times SU(2).
\]

Its \(SL(2,\mathbb R)\) component is hyperbolic and injective in
\(\epsilon\); the subgroup is a closed line, isomorphic to \(\mathbb R\),
not to \(U(1)\).  The same holds for \(U(1)_A\).  Hence

\[
\boxed{
H=\mathbb R_A\times\mathbb R_B,
\qquad
\pi_0(H)=\pi_1(H)=0 .
}
\]

The element \(\epsilon_B=4\pi\) that generates \(t\sim t+4\pi\lambda\) is a
*constant* gauge transformation connected to the identity inside \(H\); it
is "large" only in the sense that it acts trivially on the \(SU(2)\)
factor.  This corrects the terminology of the previous phase.

## 2.2 The quotient at fixed \(x\) is \(S^3\)

**REPRODUCED HERE** (first script, Part 1(iv)).

The generators \(v_A=(1,\delta,0)\), \(v_B=(0,\lambda,1)\) on
\((t_L,t_R,\psi)\) are linearly independent, so the orbits are
two-dimensional wherever the chart is nondegenerate.  Their common
annihilator is one-dimensional and spanned by

\[
\boxed{t=t_R-\delta t_L-\lambda\psi,}
\]

which reduces to \(t=t_R\) in the gauge \(t_L=\psi=0\) and inherits the
period \(4\pi\lambda\) from \(\psi\sim\psi+4\pi\).  The
\((t_L,t_R)\)-block of \((v_A,v_B)\) has determinant \(\lambda\neq0\), so
the slice \(t_L=t_R=0\) meets every orbit exactly once.  Therefore, at
fixed \(x\neq\pm1\),

\[
\boxed{
\frac{\mathbb R_{t_L}\times\mathbb R_{t_R}\times SU(2)}
{\mathbb R_A\times\mathbb R_B}
\;\cong\;
SU(2)=S^3,
}
\]

and the \(t\)-circle at fixed \((\theta,\phi)\) is the orbit of
\(g_2\to g_2e^{i\psi\sigma_3/2}\), i.e. the Hopf fibre.  This is exactly
the \(S^3\) fibration stated by Johnson–Svendsen and the classic Misner
topology.

Chart degenerations occur only at \(x=\pm1\) (with \(x=\cos2\theta\) in
the Taub region), where \(h(x)\) commutes or anticommutes with
\(\sigma_3\) and the gauge action acquires discrete \(\mathbb Z\)
stabilizers generated by
\((\epsilon_A,\epsilon_B)=(\mp4\pi\lambda n/(1\pm\delta),\,4\pi n)\).
These loci are the horizons.  Locally the \((x,t)\) block there is a
quotient of a Rindler wedge by a discrete boost, i.e. Misner space, which
is the standard structure of Taub–NUT horizons.  This is a side
observation (**SYNTHESIS**, bosonic chart level) and is not used below.

## 2.3 Bundles and holonomy on the closed-string circle

**SYNTHESIS / CRITERION.**

On the spatial circle a gauged sigma model with connected structure group
\(H\) has only the trivial principal bundle, and sections of the associated
\(G\)-bundle are periodic maps \(S^1\to G\).  A loop in the quotient lifts
to a path \(\gamma:[0,2\pi]\to G\) with \(\gamma(2\pi)=\gamma(0)\cdot h_0\),
\(h_0\in H\).  Because \(H\) is connected, a path \(h(\sigma)\) from \(1\)
to \(h_0\) exists and \(\tilde\gamma=\gamma\,h(\sigma)^{-1}\) is a periodic
lift of the same loop.  Two periodic lifts of the same loop differ by a
periodic gauge transformation.  Hence:

\[
\boxed{
\{\text{closed-string configurations}\}
=
\{\text{periodic parent fields}\}/\{\text{periodic gauge transformations}\},
}
\]

with no twisted sectors and no independent holonomy label.  The
non-periodic parameter \(\epsilon_B(\sigma)=2w\sigma\) is not a gauge
transformation on the circle in the \(\mathbb R_B\) description; it is the
bundle isomorphism that converts the clutched (twisted) description into the
periodic one.  The holonomy \(\oint A^B\) it shifts by \(4\pi w\) is a
change of description, not a quantum number: \(A^B\) is auxiliary (no kinetic
term) and is determined by the matter fields.

For the chronology loop itself the first script verifies:

\[
\gamma=(g_1^0e^{\lambda w\sigma\sigma_3},\,g_2^0)
\xrightarrow{\;\epsilon_B=-2w\sigma\;}
\tilde\gamma=(g_1^0,\,g_2^0e^{-iw\sigma\sigma_3}),
\qquad
t(\sigma)=2\lambda w\sigma
\text{ for both.}
\]

## 2.4 Equivalent compact description (unfolding)

**SYNTHESIS.**

One may instead declare \(U(1)_B\) compact, \(\epsilon_B\sim\epsilon_B+4\pi\).
This is consistent only after first quotienting the parent by the discrete
hyperbolic group \(\mathbb Z_B=\langle g_1\to g_1e^{2\pi\lambda\sigma_3}\rangle\),
an extremal-BTZ-like one-sided identification.  Then

\[
\frac{(SL(2,\mathbb R)/\mathbb Z_B)\times SU(2)}{\mathbb R_A\times U(1)_B}
=
\frac{SL(2,\mathbb R)\times SU(2)}{\mathbb R_A\times\mathbb R_B}
\]

as targets.  In this description the \(\mathbb Z_B\)-orbifold has twisted
sectors labelled by \(w\) (hyperbolic spectral flow of \(SL(2,\mathbb R)_R\),
§4), and the compact \(U(1)_B\) admits winding gauge transformations
\(\epsilon_B(\sigma)=2w\sigma\) which map sector \(w\) onto sector \(0\).
The gauge-invariant Hilbert space contains one copy of each orbit.  The
sum over \(w\) of the orbifold is the unfolding of the non-compact holonomy
integral of the \(\mathbb R_B\) description; both give the same physical
spectrum.  In the Karabali–Schnitzer BRST formulation the label \(w\) is
the winding number of the auxiliary gauge boson for \(U(1)_B\), which is
pure gauge.

---

# 3. Is \(w\) gauge-trivial or physical?

\[
\boxed{
w\text{ is gauge-trivial.}
}
\]

The classification of §1 of the task resolves as: interpretation 1 (pure
gauge redundancy) in the \(\mathbb R_B\) description, equivalently
interpretation 6 (removed by gauge equivalence / field identification) in
the compact description.  Interpretations 2–5 (independent holonomy sector,
genuine twisted sector, BTZ-type spectral-flow sector, projected sector) do
not apply.

The physical content that survives is the *state*, not the *label*:

- the chronology loop's periodic representative has \(g_1\) constant and
  \(g_2\) Hopf-wound; in the \(SU(2)_{k_2}\) affine algebra this is the
  spectral flow by the **even** amount \(2w\), which maps every integrable
  module to itself (second script, Part 3):
  \[
  \bar K^3_0\to\bar K^3_0+k_2w,\qquad
  \bar L_0\to\bar L_0+2w\bar K^3_0+k_2w^2 ;
  \]
  the flowed vacuum is the extremal descendant
  \((\bar K^+_{-1})^{k_2w}|0\rangle\) of weight \(k_2w^2\);
- the conserved charge along the chronology direction is the
  \(t\)-momentum, carried by the hyperbolic right Cartan charge
  \(\bar M\), which \(\mathcal G_B=0\) quantizes in units set by
  \(\bar N\) and the heterotic lattice charges (energy quantization on a
  periodic time direction, as expected in a CTC region);
- \(w\) itself is absorbed into \(\bar N\) and is not separately conserved.

Contrast with the cigar \(SL(2,\mathbb R)/U(1)\): there the asymptotic
winding is a (non-conserved) label because the parent elliptic spectral-flow
sectors are genuinely new modules.  Here the only twist that survives
untwisting of \(SL(2,\mathbb R)_R\) sits in \(SU(2)_R\), whose even flows
are inner.

---

# 4. Twisted current algebra (the gauge-image formulas)

**REPRODUCED HERE** (second script, Part 1).  These formulas describe the
same physical states in the clutched description; they are derived, not
imported from BTZ.

For \(\bar J=g_1^{-1}\partial_-g_1\) and the twist
\(g_1\to g_1h(x^-)\), \(h=e^{-\lambda wx^-\sigma_3}\) (which realizes the
stated monodromy since \(x^-=\tau-\sigma\)),

\[
\bar J\to h^{-1}\bar Jh+h^{-1}\partial_-h
\]

gives, in the basis \(\bar J=\bar J^3\sigma_3/2+\bar J^+\sigma_++\bar J^-\sigma_-\),

\[
\boxed{
\bar J^3\to\bar J^3-2\lambda w,
\qquad
\bar J^\pm(x^-)\to e^{\pm2\lambda wx^-}\bar J^\pm(x^-).
}
\]

With the level restored (\(\bar J^3\bar J^3\sim(k_1/2)/\bar z^2\)),

\[
\boxed{
\Delta_w\bar J^3_0=-k_1\lambda w,
\qquad
\bar J^\pm_n\to\bar J^\pm_{n\pm\alpha_w},
\qquad
\alpha_w=2i\lambda w .
}
\]

The shift \(\alpha_w\) is **imaginary** because the twist is hyperbolic;
the twisted \(SL(2,\mathbb R)_R\) modules are not isomorphic to untwisted
ones on their own.  The same \(U(1)_B\) transformation acts on
\(SU(2)_R\) with \(h_2=e^{-iwx^-\sigma_3}\):

\[
\boxed{
\bar K^3_0\to\bar K^3_0+k_2w,
\qquad
\bar K^\pm_n\to\bar K^\pm_{n\mp2w},
}
\]

an **integer** (inner) flow, and on the bosonized fermion sectors as the
zero-mode shifts of §5.  The combined map is the gauge transformation of
§2.3, which is why the imaginary \(SL(2,\mathbb R)_R\) shift never appears
alone in a physical state.

For comparison, BTZ has \(\alpha_w\propto i(r_+\pm r_-)w/\ell\) acting
symmetrically on both chiralities with no compensating compact factor.

---

# 5. Twisted gauge constraints

**REPRODUCED HERE** (first script, Part 2).

Write each gauged current as a sum of chiral \(U(1)\) currents with levels
\(\kappa_i\) (\(k_1/2\), \(k_2/2\) for the WZW Cartans, \(1\) per bosonized
complex fermion) and charges \((q_i^A,q_i^B)\) read off from the exact
embedding.  Left movers: \(SL(2,\mathbb R)_L\) Cartan \((1,0)\), heterotic
fermions \((Q_A,Q_B)\), \((P_A,P_B)\).  Right movers:
\(SL(2,\mathbb R)_R\) Cartan \((\delta,\lambda)\), \(SU(2)_R\) Cartan
\((0,1)\), supersymmetric fermions \((\delta,\lambda)\), \((0,1)\).

**Anomaly equations are the level-matrix equality.**  With
\(K_{L,R}^{XY}=\sum_{i\in L,R}\kappa_iq_i^Xq_i^Y\), the three anomaly
equations of the previous phase are exactly

\[
\boxed{K_L=K_R\equiv K}
\]

entrywise (up to the overall factor 2).

**Zero-mode shifts.**  The transformation \(\epsilon_B(\sigma)=2w\sigma\)
is a spectral flow by \(\eta_i=2wq_i^B\) in every charged sector:

\[
\boxed{p_i\to p_i+2\kappa_iq_i^Bw}
\]

in the sign convention of the previous phase, where all right-moving charges
enter \(\mathcal G_{A,B}\) with a plus sign.  This reproduces
\(\Delta\Phi_1:\Delta\Phi_2=(Q_B+\lambda):(P_B+1)\).

**The local combinations are not invariant.**  The previous phase's
\(\mathcal G_X=J^L_X+J^R_X\) (sum of left and right matter charges, the
winding-like combination) shifts by

\[
\boxed{
\mathcal G_A^{(w)}-\mathcal G_A^{(0)}=4w\,(Q_AQ_B+P_AP_B),
\qquad
\mathcal G_B^{(w)}-\mathcal G_B^{(0)}=4w\,(Q_B^2+P_B^2),
}
\]

on the anomaly surface (equivalently \(2w(K_L+K_R)^{XB}=4wK^{XB}\)).

**The full constraints are invariant.**  Including the Karabali–Schnitzer
auxiliary bosons \(a^{L,R}_X\) (level matrices \(-K_L\), \(-K_R\)), the
BRST zero-mode constraints are \(C^L_X=J^L_X+a^L_X=0\),
\(C^R_X=J^R_X+a^R_X=0\).  Under the flow the auxiliary zero modes shift by
\(-2K^{XB}w\) per chirality, and

\[
\boxed{
\Delta C^L_X=\Delta C^R_X=0
\quad\text{identically on }K_L=K_R .
}
\]

Interpretation of Step C:

- the shifts of the *matter* constraints do **not** cancel by themselves;
  they are compensated by the auxiliary gauge boson's winding
  \(-2K^{XB}w\), i.e. by the holonomy/bundle datum of \(A^B\);
- in the \(\mathbb R_B\) description the auxiliary boson is non-compact and
  has no winding, so \(\mathcal G_{A,B}=0\) holds exactly and the
  twisted matter states are simply not physical — the physical
  representative is the periodic (Hopf-wound) state with
  \(\mathcal G_{A,B}=0\);
- in the compact description the twisted states are physical but are the
  gauge images of untwisted ones.  Either way no additional projection, no
  restriction to special \(w\), and no new sector.

---

# 6. \(L_0,\bar L_0\)

**REPRODUCED HERE** (second script, Part 2).

In the abelian zero-mode sector, \(L_0\supset\sum p_i^2/2\kappa_i\) for
matter and \(-\tfrac12a^TK_{L,R}^{-1}a\) for the auxiliary bosons, the flow
gives the exact identities

\[
\boxed{
\Delta L_0=2w\,C^L_B,
\qquad
\Delta\bar L_0=2w\,C^R_B ,
}
\]

with the \(w^2\) terms \(2w^2K_L^{BB}\), \(2w^2K_R^{BB}\) of the matter
cancelled sector by sector by the auxiliary bosons.  Hence on physical
states

\[
\boxed{
L_0^{(w)}=L_0^{(0)},
\qquad
\bar L_0^{(w)}=\bar L_0^{(0)} .
}
\]

There is no \(w\)-dependent conformal weight to tabulate: the \(w\)-twisted
description and its untwisted gauge image are the same state with the same
weights.  The \(w\)-dependence one sees in a single sector, e.g.
\(\bar L_0^{SU(2)}\to\bar L_0^{SU(2)}+2w\bar N+k_2w^2\), is exactly
compensated by \(\bar L_0^{SL(2,\mathbb R)}\to\bar L_0^{SL(2,\mathbb R)}+2\lambda w\bar M+k_1\lambda^2w^2\)
and the fermion and auxiliary contributions.

The non-abelian parts of the Sugawara operators are untouched by the
argument: the flow is an automorphism of the full affine algebras, and the
equality of total weights follows from the invariance of the total gauge
currents, not from the abelian truncation.  What the abelian truncation
demonstrates is that the anomaly equations are precisely what makes the
cancellation work.

---

# 7. Level matching

Immediate from §6:

\[
\boxed{
L_0^{(w)}-\bar L_0^{(w)}=L_0^{(0)}-\bar L_0^{(0)} .
}
\]

Level matching is inherited from the untwisted representative, not
re-imposed.  No admissible-\(w\) condition arises.

---

# 8. BRST, norm, normalizability

Because the \(w\)-sector coincides with the untwisted sector, the
physical-state gates of the task's Step E reduce to those of the untwisted
heterotic coset:

1. BRST closure / non-exactness: those of the untwisted
   \(U(1)_A\times U(1)_B\) heterotic coset cohomology (technology exists,
   Phase III §7.1; not computed here);
2. level matching: inherited (§7);
3. norm and \(SL(2,\mathbb R)\) unitarity range: untwisted question;
4. normalizability in \(x\): untwisted question;
5. GSO: untwisted question;
6. tachyonic / massless thresholds: untwisted question.

None of these is specific to \(w\).  The Hopf-wound representatives are
heavy (\(\bar L_0\gtrsim k_2w^2\)) descendants of ordinary affine primaries
and are not candidates for a tachyonic chronology instability of the
Gödel long-string type.

**OPEN:** the untwisted spectral questions above.

---

# 9. Comparison with BTZ

The six differences listed in the task remain true, but the decisive one is
structural:

| | BTZ | Heterotic Taub–NUT |
|---|---|---|
| origin of periodicity | discrete orbifold \(\mathbb Z\subset SL(2,\mathbb R)_L\times SL(2,\mathbb R)_R\) | element \(\epsilon_B=4\pi\) of a *connected gauged* \(\mathbb R_B\) |
| cycle topology | non-contractible circle of the quotient | Hopf fibre of \(S^3\), contractible |
| twisted sectors | genuine orbifold sectors, hyperbolic flow \(\alpha_w\propto i(r_+\pm r_-)w/\ell\) on both chiralities | clutching descriptions of untwisted states; \(\alpha_w=2i\lambda w\) on \(SL(2,\mathbb R)_R\) only, cancelled by \(SU(2)_R\) and heterotic flows |
| compensating compact factor | none | \(SU(2)_R\) with \(e^{2\pi i w\sigma_3}=1\) |
| local charge constraints | none | \(\mathcal G_{A,B}\) shift by \(4wK^{XB}\), absorbed by the gauge sector |
| winding as quantum number | yes (conserved) | no |

The hyperbolic-flow formulas of §4 are the correct Taub–NUT analogue of the
BTZ formulas, but their role is opposite: in BTZ they build new sectors, here
they are half of a gauge transformation.

---

# 10. Outcome

\[
\boxed{\textbf{Outcome A}}
\]

in the specific sense "\(w\) is gauge-trivial".  Not in the senses "all
\(w\neq0\) states are projected out", "empty cohomology", "negative norm" or
"non-normalizable": those statements presuppose a sector that does not
exist.

The model-specific mechanism is **topological**, not dynamical:

\[
\boxed{
\text{the chronology circle of exact heterotic Taub–NUT is a gauged Hopf
fibre; no winding sector exists to be protected or to become unstable.}
}
\]

This should not be confused with chronology protection.  It means that the
Misner-type and BTZ-type stringy chronology mechanisms (winding-string
production, twisted-sector tachyons) are unavailable here, and that any
Taub–NUT-specific statement about operational CTC traversal must be made in
the untwisted spectrum.

---

# 11. Exact remaining gap

The Level B/C question of Phase III survives in reformulated form.  The
smallest next calculation is **not** a transmission observable for a
twisted state.  It is:

1. **Untwisted physical spectrum with the constraints resolved.**  Solve
   \(\mathcal G_A=\mathcal G_B=0\) together with the Virasoro conditions
   for affine primaries \((j;m,\bar m)\otimes(\ell;n,\bar n)\otimes\mathbf s\)
   of the heterotic coset, in the hyperbolic basis for
   \(SL(2,\mathbb R)\).  Identify which representations (continuous,
   discrete) are normalizable in \(x\).
2. **Localization.**  For the Hopf-wound representatives
   (\(\bar N=k_2w+\dots\)), determine the minisuperspace wavefunction in
   \(x\) and whether it is supported in the NUT region \(x>1\).  Only then
   is a Taub\(\to\)NUT reflection/transmission coefficient meaningful.
3. **Meaning of "return".**  Since the CTC is contractible, a closed
   timelike history is a statement about the semiclassical trajectory of an
   untwisted state, not about a sector.  An operational observable must be
   a gauge-invariant correlator that distinguishes a state following the
   Hopf fibre from one that has unwound; candidates are two-point functions
   of \(t\)-momentum eigenstates across \(x=1\).
4. **Horizon structure.**  The \(\mathbb Z\) stabilizers at \(x=\pm1\)
   (§2.2) suggest that the Misner-space structure of the horizons is visible
   in the coset as fixed points of a discrete subgroup of the gauge group.
   Whether this induces horizon-localized physical states in the untwisted
   spectrum is open and is the closest surviving analogue of a "twisted
   sector".

Stop conditions for the next phase: non-normalizability of every
\(\bar N\simeq k_2w\) state in the NUT region, or absence of any such state
from the untwisted BRST cohomology, would end the operational-traversal
program for this model.

---

# 12. Novelty / status map

### The Taub–NUT chronology circle is a Hopf fibre and is contractible

**PUBLISHED RESULT** (Misner 1963; stated by Johnson–Svendsen for the exact
model).  No novelty.

### The gauged group is \(\mathbb R_A\times\mathbb R_B\) and \(w\) is a trivializable clutching datum

**REPRODUCED HERE / SYNTHESIS.**  Standard gauged-WZW global reasoning
(Bars–Sfetsos non-compact gauging; Hori) applied to the exact embedding.
The explicit statement for this model was not found in the literature.

### Explicit gauge map twisted lift \(\to\) Hopf-wound periodic lift

**NEW CALCULATION CANDIDATE** (small).  Checked in the first script.

### Anomaly equations \(=\) equality of left/right level matrices; shifts of \(\mathcal G_{A,B}\) under the twist

**REPRODUCED HERE.**  Convention-fixing algebra; the \(4wK^{XB}\) shifts and
their absorption by the auxiliary sector are checked in the first script.

### Twisted current algebra with \(\alpha_w=2i\lambda w\) and the compensating \(SU(2)_R\) integer flow

**REPRODUCED HERE.**  Derived from the current transformation law; second
script.

### \(L_0^{(w)}=L_0^{(0)}\), \(\bar L_0^{(w)}=\bar L_0^{(0)}\) on physical states

**REPRODUCED HERE** in the abelian zero-mode sector; the non-abelian
extension follows from the automorphism property but was not computed.

### Reclassification of the Taub–NUT operational-CTC question

**SYNTHESIS / CRITERION.**  The counterexample-candidate status of the model
is unchanged at Level A; Levels B/C move to the untwisted spectrum.

### Horizons as \(\mathbb Z\)-stabilizer loci of the gauge action

**SYNTHESIS**, bosonic chart level, side observation; not used in the main
argument.

---

# 13. References

1. C. V. Johnson, H. G. Svendsen, *An exact string theory model of closed
   timelike curves and cosmological singularities*, Phys. Rev. D **70**
   (2004) 126011, arXiv:hep-th/0405141.
2. H. G. Svendsen, *The exact geometry of a Kerr–Taub–NUT solution of
   string theory*, Phys. Rev. D **71** (2005) 044027,
   arXiv:hep-th/0410011.
3. H. G. Svendsen, *Global properties of an exact string theory solution
   in two and four dimensions*, Phys. Rev. D **73** (2006) 064032,
   arXiv:hep-th/0511289.
4. C. V. Johnson, *Heterotic cosets*, arXiv:hep-th/9409061.
5. I. Bars, K. Sfetsos, *\(SL(2,\mathbb R)\times SU(2)/\mathbb R^2\)
   string model in curved spacetime and exact conformal results*, Phys.
   Lett. B **301** (1993) 183, arXiv:hep-th/9208001.
6. I. Bars, K. Sfetsos, *Global analysis of new gravitational
   singularities in string and particle theories*, Phys. Rev. D **46**
   (1992) 4495, arXiv:hep-th/9205037.
7. K. Hori, *Global aspects of gauged Wess–Zumino–Witten models*,
   Commun. Math. Phys. **182** (1996) 1, arXiv:hep-th/9411134.
8. D. Karabali, H. J. Schnitzer, *BRST quantization of the gauged WZW
   action and coset conformal field theories*, Nucl. Phys. B **329**
   (1990) 649.
9. K. Gawędzki, A. Kupiainen, *G/H conformal field theory from gauged WZW
   model*, Phys. Lett. B **215** (1988) 119; *Coset construction from
   functional integrals*, Nucl. Phys. B **320** (1989) 625.
10. D. Gepner, *Field identification in coset conformal field theories*,
    Phys. Lett. B **222** (1989) 207.
11. G. Moore, N. Seiberg, *Taming the conformal zoo*, Phys. Lett. B
    **220** (1989) 422.
12. A. N. Schellekens, S. Yankielowicz, *Field identification fixed points
    in the coset construction*, Nucl. Phys. B **334** (1990) 67 (citation
    from memory; verify).
13. D. Israël, C. Kounnas, D. Orlando, P. M. Petropoulos, *Heterotic
    strings on homogeneous spaces*, Fortsch. Phys. **53** (2005) 1030,
    arXiv:hep-th/0412220.
14. D. Israël, C. Kounnas, D. Orlando, P. M. Petropoulos,
    *Electric/magnetic deformations of \(S^3\) and \(AdS_3\), and
    geometric cosets*, Fortsch. Phys. **53** (2005) 73,
    arXiv:hep-th/0405213.
15. S. Hemming, E. Keski-Vakkuri, *The spectrum of strings on BTZ black
    holes and spectral flow in the SL(2,R) WZW model*, Nucl. Phys. B
    **626** (2002) 363, arXiv:hep-th/0110252.
16. M. Natsuume, Y. Satoh, *String theory on three-dimensional black
    holes*, Int. J. Mod. Phys. A **13** (1998) 1229,
    arXiv:hep-th/9611041.
17. E. J. Martinec, W. McElgin, *String theory on AdS orbifolds*, JHEP
    **04** (2002) 029, arXiv:hep-th/0106171.
18. J. Maldacena, H. Ooguri, *Strings in AdS\(_3\) and the SL(2,R) WZW
    model. I*, J. Math. Phys. **42** (2001) 2929, arXiv:hep-th/0001053.
19. E. Witten, *On string theory and black holes*, Phys. Rev. D **44**
    (1991) 314.
20. C. W. Misner, *The flatter regions of Newman, Unti, and Tamburino's
    generalized Schwarzschild space*, J. Math. Phys. **4** (1963) 924.
21. S. W. Hawking, G. F. R. Ellis, *The Large Scale Structure of
    Space-Time*, Cambridge (1973), ch. 5 (Taub–NUT space).
22. D. Israël, *Quantization of heterotic strings in a Gödel/anti de
    Sitter spacetime and chronology protection*, JHEP **01** (2004) 042,
    arXiv:hep-th/0310158.
23. M. Berkooz, B. Pioline, M. Rozali, *Closed strings in Misner space:
    cosmological production of winding strings*, JCAP **08** (2004) 004,
    arXiv:hep-th/0405126.

---

# 14. Restart point

Do not recompute the sector analysis.  \(w\) is gauge-trivial.

Continue from §11: the untwisted heterotic-coset spectrum in the hyperbolic
\(SL(2,\mathbb R)\) basis with \(\mathcal G_A=\mathcal G_B=0\) resolved,
the normalizability of the \(\bar N\simeq k_2w\) Hopf-wound states in
\(x\), and their localization relative to \(x=1\).  The first executable
target is a minisuperspace wave equation for a \(t\)-momentum eigenstate in
the exact \((x,t)\) fiber block, with the constraint-determined
\(\bar M\).
