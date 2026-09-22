# Independent Audit of the Fable Heterotic Taub–NUT Chronology Result

**Status:** independent adversarial audit, 2026-09-22.

This note audits the Phase-IV result in:

- `notes/fable-heterotic-ctc-operational-traversal.md`
- `notes/heterotic-ctc-operational-traversal.md`
- `src/symbolic/heterotic_taubnut_twist_zero_modes.py`
- `src/symbolic/heterotic_taubnut_level_matching.py`

The narrow question is not whether the exact target geometry contains closed
timelike curves.  It does.

The question is:

\[
\boxed{
\text{Does the exact heterotic Taub--NUT theory actually permit a controlled
physical process that returns information or an excitation to its causal past?}
}
\]

The audit deliberately tries both directions:

1. kill the Fable sector-reclassification result using prior art or a global
   gauge-theory loophole;
2. if it survives, determine whether it materially strengthens the case for
   operational time travel.

---

# 0. Executive verdict

The Fable Phase-IV result survives this audit, but with narrower wording.

\[
\boxed{
\textbf{Fable Outcome A: CONFIRMED WITH WORDING CHANGE.}
}
\]

The strongest statement supported by the present evidence is:

\[
\boxed{
\text{There is no independent discrete }w\text{-labelled
chronology-winding superselection sector.}
}
\]

The shorter phrase

\[
w\text{ is gauge-trivial}
\]

is usable only if it is read as a statement about the **sector label**, not as
a statement that the associated physical configuration is absent.

Three parts of the Fable argument are strong:

1. the periodic chronology circle is the Hopf fibre inside an
   \(S^3\) constant-radial slice, so it does not define a conserved
   topological winding charge;
2. for the chronology model with \(\lambda\neq0\), the embedded
   \(B\)-gauge one-parameter subgroup contains a hyperbolic
   \(SL(2,\mathbb R)\) component and is globally noncompact, so the natural
   image of the gauge parameter is \(\mathbb R_B\), not a compact circle;
3. the explicit zero-mode/current-algebra calculation is internally
   consistent: after the auxiliary gauge sector is included, the full gauge
   constraints and \(L_0,\bar L_0\) are invariant on physical states.

The two new symbolic scripts have now passed repository CI under both
Python 3.11 and Python 3.12 (Symbolic CI run #82).  This verifies the algebra
implemented by the scripts; it does not by itself prove the global BRST
cohomology statement.

The main qualification is:

\[
\boxed{
\text{trivial bundle topology does not, by itself, prove that every continuous
gauge-field holonomy is gauge-trivial.}
}
\]

A continuous holonomy can remain an integration modulus even on a trivial
bundle.  Nothing found in this audit revives a **discrete** \(w\) sector, but
a fully explicit Taub--NUT heterotic partition-function/BRST treatment of the
continuous gauge zero modes would be needed to upgrade the global
field-identification statement to a theorem.

Most importantly:

\[
\boxed{
\textbf{The Fable result neither proves nor disproves time travel.}
}
\]

It removes one candidate mechanism -- a special Misner/BTZ-like winding sector
-- and moves the problem to the ordinary untwisted physical spectrum.

The current status of operational time travel is therefore:

\[
\boxed{
\text{OPEN: exact CTC geometry is established, physical past-return is not.}
}
\]

---

# 1. What the original exact-CFT papers really establish

## 1.1 Exact CTC geometry survives \(\alpha'\)

**PUBLISHED RESULT.**

Johnson and Svendsen constructed and analyzed the heterotic coset model whose
target contains a finite Taub cosmological region joined to NUT regions with
closed timelike curves.

Reference:

- C. V. Johnson and H. G. Svendsen,
  *Exact string theory model of closed timelike curves and cosmological
  singularities*, Phys. Rev. D **70**, 126011 (2004),
  arXiv:hep-th/0405141.

Their exact-in-\(\alpha'\) geometry retains the key Taub/NUT chronology
structure and Misner-type chronology horizons.

Therefore the strong claim

\[
\text{stringy }\alpha'\text{ corrections automatically erase the CTC region}
\]

is false in this model.

This is the strongest pro-time-machine fact in the entire chain.

## 1.2 Classical connectivity is real

**PUBLISHED RESULT.**

The original paper emphasizes that the Taub and NUT regions are connected and
that classical geodesics can pass between them.  Svendsen's later global study
analyzes analytic continuation, test-particle motion and T-duality in the exact
background.

Reference:

- H. G. Svendsen,
  *Global properties of an exact string theory solution in two and four
  dimensions*, Phys. Rev. D **73**, 064032 (2006),
  arXiv:hep-th/0511289.

Thus there is no purely geometric theorem in these papers that isolates the
chronal region from the CTC region.

However:

\[
\boxed{
\text{classical/test-particle accessibility}
\neq
\text{normalizable BRST physical-string accessibility}.
}
\]

The latter is not computed in these papers.

---

# 2. Audit of the Fable topology argument

## 2.1 The chronology circle is not a topological winding cycle

**CONFIRMED.**

Johnson--Svendsen explicitly describe constant radial slices in the NUT region
as \(S^3\), with periodic time as a circle fibred over \(S^2\).

Hence

\[
\pi_1(S^3)=0.
\]

A Hopf fibre is a geometrically distinguished circle, but as a loop in
\(S^3\) it is null-homotopic.

Therefore a string that follows that fibre does **not** acquire a conserved
topological winding charge merely from target-space topology.

This kills the most naive identification

\[
w
=
\text{ordinary conserved winding number around an }S^1\text{ factor}.
\]

This part of the Fable reclassification is strong.

## 2.2 Comparison with Misner and BTZ

This sharply differs from backgrounds where the relevant circle is created by
a discrete quotient and twisted sectors are genuine sectors of the orbifold
Hilbert space.

For Misner space, physical twisted states and timelike winding strings are
explicitly present:

- M. Berkooz, B. Pioline and M. Rozali,
  *Closed Strings in Misner Space: Cosmological Production of Winding
  Strings*, JCAP **08** (2004) 004,
  arXiv:hep-th/0405126.

For BTZ, hyperbolic spectral flow represents genuine quotient sectors:

- S. Hemming and E. Keski-Vakkuri,
  *The spectrum of strings on BTZ black holes and spectral flow in the
  SL(2,R) WZW model*, Nucl. Phys. B **626** (2002) 363,
  arXiv:hep-th/0110252.

Thus the Fable warning

\[
\boxed{
\text{do not import the BTZ winding-sector interpretation unchanged}
}
\]

is correct.

---

# 3. Audit of the global gauge-group claim

The source gauging acts schematically as

\[
g_1
\longrightarrow
e^{\epsilon_A\sigma_3/2}
g_1
e^{(\delta\epsilon_A+\lambda\epsilon_B)\sigma_3/2},
\]

\[
g_2
\longrightarrow
g_2e^{i\epsilon_B\sigma_3/2}.
\]

For \(\lambda\neq0\), the \(B\)-action includes

\[
e^{\lambda\epsilon_B\sigma_3/2}
\in SL(2,\mathbb R),
\]

which is hyperbolic and does not become the identity at
\(\epsilon_B=4\pi\).

Therefore the embedded one-parameter subgroup is injective in
\(\epsilon_B\) and is naturally isomorphic to \(\mathbb R\), even though
the source notation calls the gauging \(U(1)_B\).

The same logic applies to the relevant \(A\)-embedding.

Thus, in the chronology model,

\[
\boxed{
H\simeq\mathbb R_A\times\mathbb R_B
}
\]

is a defensible global reading of the embedded subgroup.

This also explains why

\[
\epsilon_B=4\pi
\]

acts trivially on the \(SU(2)\) factor while remaining nontrivial on the
parent \(SL(2,\mathbb R)\) factor.

---

# 4. What Hori's global gauged-WZW analysis does and does not prove here

Relevant prior art:

- K. Hori,
  *Global Aspects of Gauged Wess--Zumino--Witten Models*,
  Commun. Math. Phys. **182** (1996) 1,
  arXiv:hep-th/9411134.

Hori's analysis makes clear that global gauge-bundle topology and field
identification are not optional details in a gauged-WZW model.  Topological
sectors are tied to the global structure of the gauge group and, in the
standard setting, to nontrivial classes associated with the gauge group.

For a contractible group such as

\[
H\simeq\mathbb R^2,
\]

there is no \(\pi_1(H)\)-labelled family of discrete topological sectors.

This strongly supports Fable's conclusion that the integer \(w\) introduced
from the target coordinate period should not automatically be promoted to a
new discrete exact-CFT superselection sector.

But Hori does **not** supply a ready-made proof of the full Fable claim,
because:

1. the Taub--NUT construction is asymmetric and heterotic;
2. the relevant embedded gauge group is noncompact;
3. the exact Taub--NUT BRST spectrum and partition function were not computed
   in the cited chronology papers.

Therefore:

\[
\boxed{
\text{no discrete topological }w\text{ sector}
}
\]

is much better supported than

\[
\boxed{
\text{every possible gauge holonomy is physically trivial}.
}
\]

---

# 5. Holonomy loophole: the main qualification

A trivial principal bundle can still carry a connection with nonzero continuous
holonomy.

Schematically, on a spatial circle,

\[
A=a\,d\sigma
\]

can have

\[
\oint A=2\pi a
\]

even when the underlying bundle is trivial.

Therefore the implication

\[
\text{bundle trivial}
\Rightarrow
\text{all holonomy data absent}
\]

is not valid as a general mathematical statement.

For the present gauged WZW model the gauge field is auxiliary, so such zero
modes are expected to be constrained/integrated rather than to define an
ordinary propagating gauge degree of freedom.  But the exact way the
continuous holonomy enters the heterotic coset Hilbert space or torus
partition function has not been exhibited for this Taub--NUT model in the
literature located here.

### Audit consequence

This loophole **does not restore the discrete chronology integer** \(w\).

It only forces the wording:

\[
\boxed{
\text{No independent discrete }w\text{ sector is established;}
\quad
\text{continuous holonomy treatment remains to be written explicitly.}
}
\]

Thus Fable's central reclassification survives.

---

# 6. Audit of the symbolic BRST/zero-mode result

The repository scripts establish, within their stated conventions,

\[
\Delta G_B
=
4w(Q_B^2+P_B^2),
\]

\[
\Delta G_A
=
4w(Q_AQ_B+P_AP_B)
\]

for the matter-only combinations on the anomaly surface.

After including the auxiliary gauge-boson zero modes, the total constraints
are invariant.

The second script verifies

\[
\Delta L_0=2wC_B^L,
\qquad
\Delta\bar L_0=2wC_B^R,
\]

hence on physical states,

\[
C_B^L=C_B^R=0
\]

gives

\[
\boxed{
L_0^{(w)}=L_0^{(0)},
\qquad
\bar L_0^{(w)}=\bar L_0^{(0)}.
}
\]

Repository CI after the Phase-IV fixes passed in both Python 3.11 and 3.12.

### What this verifies

It verifies that the proposed shift is algebraically consistent with:

- the anomaly equations;
- the stated current levels;
- the auxiliary gauge-sector cancellation;
- level matching at the zero-mode level.

### What it does not verify

It is not a proof of:

- complete BRST cohomology;
- non-exactness of a particular physical vertex operator;
- modular equivalence of the full partition function;
- normalizability;
- target-space localization in the NUT region.

The scripts therefore support the sector reclassification but do not establish
a time-travelling physical state.

---

# 7. Audit of the SU(2) spectral-flow statement

Fable's periodic representative moves the apparent chronology winding into an
\(SU(2)_R\) affine excitation.

The general WZW literature supports the representation-theory statement that
spectral flow of \(\widehat{su}(2)_k\) does not generate an unlimited tower
of inequivalent modules in the same way as hyperbolic
\(\widehat{sl}(2,\mathbb R)\) flow.

For example, in the WZW analysis of

- A. Dei and A. Sfondrini,
  *Integrable spin chain for stringy Wess--Zumino--Witten models*,
  JHEP **07** (2018) 109,
  arXiv:1806.00422,

even spectral flow maps an integrable \(su(2)_k\) representation back to the
same representation class, while odd flow implements the familiar finite
representation identification.

This supports the Fable claim that an even flow \(2w\) need not define a new
independent \(SU(2)\) module.

Qualification:

\[
\boxed{
\text{module isomorphism in }\widehat{su}(2)
\neq
\text{full heterotic Taub--NUT BRST-state equivalence by itself}.
}
\]

The coupled asymmetric gauge constraints still matter.

---

# 8. A Fable overclaim that should be weakened

The Phase-IV note says, in effect, that strings which semiclassically wrap the
timelike \(t\)-circle in the NUT region “do exist as untwisted states.”

That is too strong if “states” means fully established normalizable
BRST-physical states of the exact heterotic model.

What is established is weaker:

\[
\boxed{
\text{the putative chronology configuration can be represented using ordinary
untwisted affine quantum numbers rather than a new }w\text{ sector.}
}
\]

Still missing:

1. explicit solution of both gauge constraints for the candidate class;
2. Virasoro mass shell and level matching in the full heterotic theory;
3. GSO/no-ghost conditions;
4. BRST closure and non-exactness;
5. normalizability;
6. target-space support or flux into \(x>1\).

Therefore this audit changes the wording to:

> chronology-relevant **untwisted candidate states**, not established
> chronology-traversing physical states.

---

# 9. Can prior art kill time travel here?

Not yet.

But related exact or controlled models show several mechanisms capable of
killing an operational time machine even after CTC geometry exists.

## 9.1 Exact heterotic Gödel: spectrum instability

D. Israël computed the physical spectrum and genus-one partition function in
an exact heterotic Gödel/AdS background:

- D. Israël,
  *Quantization of heterotic strings in a Gödel/Anti de Sitter spacetime and
  chronology protection*, JHEP **01** (2004) 042,
  arXiv:hep-th/0310158.

Chronology-related long strings destabilize the background, and a candidate
condensation endpoint avoids CTCs.

This is direct prior art for:

\[
\boxed{
\text{exact CTC background}
\not\Rightarrow
\text{stable usable CTC physics}.
}
\]

No analogous Taub--NUT spectrum/instability calculation has yet been located.

## 9.2 Misner strings: physical states exist but interactions become problematic

In Misner space, physical twisted states really do exist, including strings
associated with timelike winding, but the theory exhibits strong pair
production and singular behavior in loop or scattering observables.

Thus:

\[
\boxed{
\text{physical chronology-related string state}
\not\Rightarrow
\text{controlled operational time machine}.
}
\]

## 9.3 Holographic chronology protection

Emparan and Tomašević give controlled examples where interacting quantum
fields prevent operational passage through chronology horizons:

- R. Emparan and M. Tomašević,
  *Holography of time machines*, JHEP **03** (2022) 212,
  arXiv:2107.14200.
- R. Emparan and M. Tomašević,
  *Quantum backreaction on chronology horizons*, JHEP **02** (2022) 182,
  arXiv:2109.03611.

In their holographic constructions, chronal and nonchronal regions can become
physically disconnected, and with backreaction the chronology horizon can
turn into a strong spacelike singularity.

These are not the heterotic Taub--NUT model, so they do not prove chronology
protection here.

They do kill the inference:

\[
\text{regular exact background}
\Rightarrow
\text{operational crossing survives interactions}.
\]

---

# 10. Can prior art save time travel here?

Only partially.

The exact Taub--NUT literature establishes three unusually favorable facts:

1. an exact heterotic CFT background exists;
2. the CTC regions survive all target-space \(\alpha'\) corrections included
   in the exact geometry;
3. the Taub and NUT regions remain geometrically connected, with classical
   probe motion across the global extension studied in the literature.

The repository adds two more negative obstruction tests:

4. the first chronology horizon is not an automatic local Nambu--Goto area
   divergence for the simple wrapped probe;
5. the exact dilaton is finite at that horizon.

Therefore there is currently no known local geometric or
\(\alpha'\)-correction wall that obviously forbids entry.

This keeps the model alive as a counterexample candidate to strong chronology
protection.

But none of these results establishes the minimum quantum statement:

\[
\boxed{
\exists\,|\Psi\rangle_{\rm phys}
\text{ normalizable and BRST-nontrivial with nonzero flux from Taub into NUT}.
}
\]

That is now the decisive missing calculation.

---

# 11. Time-travel gate ladder

For clarity, separate the word “time travel” into progressively stronger
claims.

| Gate | Question | Status |
|---|---|---|
| T0 | Does an exact string background contain CTC geometry? | **ESTABLISHED** |
| T1 | Are Taub and NUT regions classically connected? | **ESTABLISHED / PUBLISHED** |
| T2 | Does a normalizable BRST-physical string state cross into NUT? | **OPEN** |
| T3 | Does that state remain controlled under interactions / finite \(g_s\) effects? | **OPEN** |
| T4 | Is there a gauge-invariant observable representing return to the preparation event's causal past? | **OPEN** |
| T5 | Can the time-machine configuration form predictively from regular chronal initial data? | **NOT ESTABLISHED** |

The Fable result resolves a side question between T0 and T2:

\[
\boxed{
\text{the route to T2 does not require a new discrete }w\text{ sector.}
}
\]

It does not pass T2.

---

# 12. Current verdict on “can we travel to the past?”

The scientifically defensible answer at this stage is:

\[
\boxed{
\textbf{Not demonstrated, not ruled out in this exact model.}
}
\]

More specifically:

- the exact CTC background is real within the model;
- the easy BTZ/Misner-like winding-sector route is removed;
- no published Taub--NUT-specific normalizable BRST crossing state was found;
- no published Taub--NUT-specific interacting chronology-protection
  instability was found either.

Thus the heterotic Taub--NUT model remains a serious **operational
time-machine counterexample candidate**, but not an operational time machine.

The Fable analysis slightly narrows the route rather than deciding the issue.

---

# 13. The next calculation that can actually change the answer

Do not return to the twisted-sector problem.

The next useful target is:

\[
\boxed{
\textbf{Untwisted BRST state + NUT transmission}
}
\]

in this order.

## 13.1 Untwisted physical-state existence

Construct a candidate affine primary

\[
(j;m,\bar m)
\otimes
(\ell;n,\bar n)
\otimes
\mathbf s
\]

and impose:

\[
\mathcal G_A=0,
\qquad
\mathcal G_B=0,
\]

together with:

- Virasoro mass shell;
- level matching;
- heterotic GSO conditions;
- allowed \(SL(2,\mathbb R)\) representation/no-ghost range;
- BRST closure/non-exactness;
- normalizability.

If no chronology-relevant state survives, the model acquires a genuine
state-space chronology-protection mechanism.

## 13.2 Minisuperspace localization / transmission

For a surviving physical quantum-number class, derive the exact
minisuperspace/Casimir radial equation and determine:

- near-\(x=1\) mode behavior;
- correct metric+dilaton inner-product measure;
- conserved radial flux;
- Taub-side and NUT-side normalizability;
- reflection/transmission coefficient.

The first result that would materially increase the case for time travel is:

\[
\boxed{
\mathcal F_{\rm Taub\to NUT}\neq0
}
\]

for a normalizable BRST-physical state.

## 13.3 Interaction gate

If transmission survives, test:

- finite tree-level amplitudes;
- factorization;
- chronology-sector instability;
- string-loop / \(g_s\) control;
- backreaction.

Only then should one formulate the final operational return observable.

---

# 14. What would count as a decisive result?

## A decisive negative result

Any one of the following would strongly damage the time-travel candidate:

\[
\boxed{
\text{no admissible BRST cohomology class}
}
\]

or

\[
\boxed{
\text{all NUT-supporting states are nonnormalizable / negative norm}
}
\]

or

\[
\boxed{
\text{zero transmission across }x=1
}
\]

or

\[
\boxed{
\text{unavoidable instability/backreaction forms before operational return}.
}
\]

## A decisive positive intermediate result

A controlled result of the form

\[
\boxed{
\exists\,|\Psi\rangle_{\rm phys}:
\quad
\mathcal F_{\rm Taub\to NUT}>0
}
\]

would be the first real quantum-string evidence that the chronology region is
physically accessible.

Even that would not yet prove return to the causal past.

The final positive target must be a BRST/gauge-invariant relational observable
that distinguishes “support in a CTC-containing region” from actual
closed-timelike return.

---

# 15. Audit classification

## Fable claim: no independent \(w\)-sector

**CONFIRMED WITH WORDING CHANGE.**

Preferred wording:

\[
\boxed{
\text{No independent discrete chronology-winding superselection sector exists.}
}
\]

## Fable claim: full global holonomy is trivial

**PARTIALLY CONFIRMED / TOO STRONG AS WRITTEN.**

Discrete \(w\) is not rescued, but continuous gauge holonomy should not be
declared absent solely from bundle triviality.  An explicit partition-function
or full BRST treatment would settle this cleanly.

## Fable claim: chronology-related configurations live in the untwisted spectrum

**SUPPORTED AS A RECLASSIFICATION.**

The relevant affine representatives can be sought in the ordinary spectrum.

## Fable claim: chronology-traversing physical strings exist

**NOT ESTABLISHED.**

This requires the untwisted physical-state and transmission calculation.

## Operational past-directed time travel

**OPEN.**

No no-go theorem has killed this Taub--NUT exact-CFT candidate, but no
controlled operational return has been exhibited.

---

# 16. References

1. C. V. Johnson and H. G. Svendsen,
   *Exact string theory model of closed timelike curves and cosmological
   singularities*, Phys. Rev. D **70**, 126011 (2004),
   arXiv:hep-th/0405141.

2. H. G. Svendsen,
   *Global properties of an exact string theory solution in two and four
   dimensions*, Phys. Rev. D **73**, 064032 (2006),
   arXiv:hep-th/0511289.

3. K. Hori,
   *Global Aspects of Gauged Wess--Zumino--Witten Models*,
   Commun. Math. Phys. **182** (1996) 1,
   arXiv:hep-th/9411134.

4. D. Karabali and H. J. Schnitzer,
   *BRST Quantization of the Gauged WZW Action and Coset Conformal Field
   Theories*, Nucl. Phys. B **329** (1990) 649.

5. D. Gepner,
   *Field Identification in Coset Conformal Field Theories*,
   Phys. Lett. B **222** (1989) 207.

6. S. Hemming and E. Keski-Vakkuri,
   *The spectrum of strings on BTZ black holes and spectral flow in the
   SL(2,R) WZW model*, Nucl. Phys. B **626** (2002) 363,
   arXiv:hep-th/0110252.

7. A. Dei and A. Sfondrini,
   *Integrable spin chain for stringy Wess--Zumino--Witten models*,
   JHEP **07** (2018) 109,
   arXiv:1806.00422.

8. D. Israël,
   *Quantization of heterotic strings in a Gödel/Anti de Sitter spacetime and
   chronology protection*, JHEP **01** (2004) 042,
   arXiv:hep-th/0310158.

9. M. Berkooz, B. Pioline and M. Rozali,
   *Closed Strings in Misner Space: Cosmological Production of Winding
   Strings*, JCAP **08** (2004) 004,
   arXiv:hep-th/0405126.

10. M. Berkooz, B. Durin, B. Pioline and D. Reichmann,
    *Closed Strings in Misner Space: Stringy Fuzziness with a Twist*,
    arXiv:hep-th/0407216.

11. R. Emparan and M. Tomašević,
    *Holography of time machines*, JHEP **03** (2022) 212,
    arXiv:2107.14200.

12. R. Emparan and M. Tomašević,
    *Quantum backreaction on chronology horizons*, JHEP **02** (2022) 182,
    arXiv:2109.03611.

---

# 17. Restart point

The next chronology task should begin with:

\[
\boxed{
\text{untwisted physical-state gate}
}
\]

not with another winding-sector analysis.

First determine whether a normalizable BRST-physical state with the required
ordinary Cartan/gauge quantum numbers exists.

Then test:

\[
\boxed{
\text{Taub}\to\text{NUT radial flux}.
}
\]

That calculation, not the discrete \(w\) label, is now the shortest route to
changing the answer to the actual question:

\[
\boxed{
\text{Can this exact quantum-gravity model realize physical travel to the past?}
}
\]
