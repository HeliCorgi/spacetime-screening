# Exact Heterotic Taub–NUT: Time-Travel Decision Audit

**Status:** adversarial decision analysis, 2026-09-22.

This note asks the binary question as directly as possible:

\[
\boxed{
\text{Can the exact heterotic Taub--NUT model support physical travel to the past?}
}
\]

The answer after the present calculation is:

\[
\boxed{
\textbf{Operational past-directed time travel is not proved, but it is not ruled out.}
}
\]

More sharply,

\[
\boxed{
\textbf{at exact-background/minisuperspace level, the first chronology horizon is transmissive, not a hard wall.}
}
\]

So a simple chronology-protection mechanism based on universal reflection at
\(x=1\) is not available. Any remaining obstruction must enter through the
full heterotic BRST spectrum, norm/normalizability, interactions,
finite-\(g_s\) backreaction, or the operational return observable.

This note continues the Fable audit and the main chronology note. Executable
algebra is in

    src/symbolic/heterotic_taubnut_minisuperspace_horizon.py

---

# 1. Decision ladder

| Gate | Question | Present status |
|---|---|---|
| D0 | Exact string background contains CTC geometry? | **YES / PUBLISHED** |
| D1 | Taub and NUT regions are geometrically connected? | **YES / PUBLISHED** |
| D2 | Exact metric+dilaton force zero wave flux at \(x=1\)? | **NO / CALCULATED HERE** |
| D3 | Chronology-relevant untwisted BRST-physical string state exists? | **OPEN** |
| D4 | Such a state has nonzero Taub-to-NUT transmission? | **OPEN, but no local minisuperspace wall** |
| D5 | Interactions and finite-\(g_s\) effects remain controlled? | **OPEN** |
| D6 | Gauge-invariant observable realizes return to the causal past? | **OPEN** |
| D7 | Time-machine configuration forms predictively from regular chronal data? | **NOT ESTABLISHED** |

Thus:

- exact time-machine kinematics: **yes**;
- local exact wave-horizon obstruction: **no**;
- fully physical string time travel: **not established**;
- exact-model impossibility theorem: **not found**.

---

# 2. Exact background used

For the nonrotating exact heterotic Taub--NUT model,

\[
ds^2=(k-2)\left[
\frac{dx^2}{x^2-1}
-\frac{x^2-1}{D(x)}
\left(dt-\lambda\cos\theta\,d\phi\right)^2
+d\theta^2+\sin^2\theta\,d\phi^2
\right],
\]

with

\[
D(x)
=
(x+\delta)^2-\frac{4}{k+2}(x^2-1),
\]

and exact dilaton

\[
\Phi-\Phi_0=-\frac14\ln D(x).
\]

The chronology horizons remain at \(x=\pm1\). For the first NUT region,
\(x>1\) and \(D>0\), the periodic \(t\)-direction is timelike.

---

# 3. Exact cancellation in the string-frame zero-mode measure

The exact determinant is

\[
\boxed{
\det g
=
-\frac{(k-2)^4\sin^2\theta}{D(x)}.
}
\]

Hence

\[
\sqrt{|g|}
=
\frac{(k-2)^2\sin\theta}{\sqrt{D(x)}}.
\]

Since

\[
e^{-2\Phi}\propto \sqrt{D(x)},
\]

we get

\[
\boxed{
e^{-2\Phi}\sqrt{|g|}
\propto
(k-2)^2\sin\theta,
}
\]

with no \(x\)-dependence.

Therefore the exact dilaton does not create a divergent radial measure at the
chronology horizon.

---

# 4. Exact minisuperspace radial equation

Use the dilaton-weighted scalar operator

\[
\mathcal O\Psi
=
\frac{1}{e^{-2\Phi}\sqrt{|g|}}
\partial_\mu
\left(
e^{-2\Phi}\sqrt{|g|}
g^{\mu\nu}\partial_\nu\Psi
\right).
\]

This is an obstruction diagnostic, not yet the full heterotic BRST problem.

For

\[
\Psi=e^{-i\omega t}e^{im\phi}\Theta(\theta)R(x),
\]

the angular part is monopole-harmonic type. Collect all finite angular,
mass and other zero-mode contributions into \(\Lambda\). Then the exact radial
equation is

\[
\boxed{
\frac{d}{dx}
\left[
(x^2-1)\frac{dR}{dx}
\right]
+
\left[
\omega^2\frac{D(x)}{x^2-1}
-\Lambda
\right]R
=
0.
}
\]

This equation is enough to decide whether the first chronology horizon is a
local hard wall.

---

# 5. Horizon Frobenius analysis

At \(x=1\),

\[
D(1)=(1+\delta)^2.
\]

Set \(y=x-1\). Since \(x^2-1=2y+O(y^2)\), the leading equation is

\[
2\frac{d}{dy}
\left(y\frac{dR}{dy}\right)
+
\frac{\omega^2(1+\delta)^2}{2y}R
\simeq0.
\]

For \(R\sim y^\alpha\),

\[
\boxed{
\alpha^2+\frac{\omega^2(1+\delta)^2}{4}=0.
}
\]

Therefore

\[
\boxed{
\alpha_\pm
=
\pm i\frac{\omega(1+\delta)}{2}.
}
\]

The horizon solutions are oscillatory logarithmic waves,

\[
R_\pm
\sim
(x-1)^{\pm i\omega(1+\delta)/2},
\]

not modes forced to vanish at the horizon.

The same structure occurs at \(x=-1\), with \(1+\delta\) replaced by
\(\delta-1\).

---

# 6. Exact conserved horizon flux

The Sturm--Liouville current is

\[
\mathcal J_x
=
\frac{x^2-1}{2i}
\left(
R^*\partial_xR-R\partial_xR^*
\right).
\]

For

\[
R\sim(x-1)^{ia},
\qquad
a=\frac{\omega(1+\delta)}{2},
\]

the exact leading flux is

\[
\boxed{
\lim_{x\to1^+}\mathcal J_x
=
2a
=
\omega(1+\delta).
}
\]

The opposite branch carries the opposite flux.

Thus

\[
\boxed{
\text{the exact first chronology horizon admits finite nonzero minisuperspace flux.}
}
\]

A universal perfect-reflection mechanism at \(x=1\) is therefore excluded at
this level.

---

# 7. Tortoise coordinate and Schrödinger potential

Define

\[
\frac{dr_*}{dx}
=
\frac{\sqrt{D(x)}}{x^2-1}.
\]

Near \(x=1\),

\[
r_*
\sim
\frac{1+\delta}{2}\ln|x-1|.
\]

Hence the two horizon branches are

\[
R_\pm\sim e^{\pm i\omega r_*}.
\]

After setting

\[
R=D^{-1/4}\psi,
\]

the equation has Schrödinger form

\[
\frac{d^2\psi}{dr_*^2}
+
\left[
\omega^2-V(x)
\right]\psi
=
0.
\]

The symbolic calculation gives the exact horizon limit

\[
\boxed{
V(x\to1^+)=0.
}
\]

So the first chronology horizon is an asymptotically free wave region.

This result is insensitive to finite \(\Lambda\). Ordinary finite angular,
mass, or regular gauge-coupling terms do not create an infinite local barrier.

---

# 8. Exact radial equation is hypergeometric type

An exact identity is

\[
\frac{D(x)}{x^2-1}
=
\frac{k-2}{k+2}
+
\frac{(1+\delta)^2}{2(x-1)}
-
\frac{(\delta-1)^2}{2(x+1)}.
\]

With

\[
z=\frac{1-x}{2},
\]

the radial equation becomes

\[
z(1-z)R_{zz}
+
(1-2z)R_z
+
\left[
C
+
\frac{\omega^2(1+\delta)^2}{4z}
+
\frac{\omega^2(\delta-1)^2}{4(1-z)}
\right]R
=
0,
\]

where

\[
C
=
\Lambda
-
\omega^2\frac{k-2}{k+2}.
\]

It has three regular singular points \(z=0,1,\infty\), so it is of
hypergeometric/Riemann-\(P\) type.

Thus both chronology horizons are regular singular wave surfaces, not hard
reflecting boundaries. A global continuation prescription is still required,
but local analytic continuation exists.


## 8.1 Exact horizon-to-NUT connection coefficient

The hypergeometric form allows a stronger statement than local Frobenius
regularity.

Write

\[
a_+
=
\frac{\omega(1+\delta)}{2},
\qquad
a_-
=
\frac{\omega(\delta-1)}{2},
\]

and choose one horizon branch

\[
\alpha=-ia_+.
\]

Let \(\beta=\pm ia_-\), and define \(h\) by

\[
h(h+1)=C.
\]

With

\[
R=z^\alpha(1-z)^\beta\,{}_2F_1(a,b;c;z),
\]

the hypergeometric parameters may be chosen as

\[
a=\alpha+\beta-h,
\qquad
b=\alpha+\beta+h+1,
\qquad
c=1+2\alpha.
\]

For the first NUT region, \(x>1\) corresponds to \(z<0\), and
\(x\to+\infty\) means \(z\to-\infty\).

The standard hypergeometric connection formula gives two asymptotic powers,

\[
R
\sim
A_h(-z)^h
+
B_h(-z)^{-h-1},
\]

with

\[
A_h
=
\frac{\Gamma(c)\Gamma(b-a)}
{\Gamma(b)\Gamma(c-a)},
\]

\[
B_h
=
\frac{\Gamma(c)\Gamma(a-b)}
{\Gamma(a)\Gamma(c-b)}.
\]

The Gamma function has no zeros. Therefore these coefficients are generically
nonzero; they vanish only on special discrete parameter loci where a
denominator Gamma function has a pole.

Hence:

\[
\boxed{
\text{a horizon wave branch generically has nonzero continuation into the
NUT asymptotic basis.}
}
\]

This is stronger than saying that the local horizon potential is finite. It
shows that the exact minisuperspace connection problem does not generically
decouple the NUT region from the horizon.

It still does not prove that the corresponding mode belongs to the full
heterotic BRST cohomology.

---

# 9. NUT infinity has a genuine continuum regime

Let

\[
A=\frac{k-2}{k+2}.
\]

At \(x\to+\infty\),

\[
D(x)\sim Ax^2,
\]

and

\[
x^2R''+2xR'+(\omega^2A-\Lambda)R\simeq0.
\]

Therefore

\[
R\sim x^s,
\qquad
s=
-\frac12
\pm
\sqrt{
\frac14+\Lambda-\omega^2A
}.
\]

Equivalently, the Schrödinger potential tends to

\[
\boxed{
V(+\infty)
=
\frac{\Lambda+1/4}{A}.
}
\]

Hence continuum propagation in the NUT region occurs whenever

\[
\boxed{
\omega^2
>
\frac{\Lambda+1/4}{A}.
}
\]

So the first NUT region is not kinematically empty of propagating
minisuperspace modes.

For globally single-valued scalar modes, periodic \(t\) and the Hopf fibration
quantize the usual monopole-harmonic charge combination
\(q=\lambda\omega\). This changes the allowed spectrum but does not create a
horizon wall.

---

# 10. The closed timelike orbit has finite proper duration

In the first NUT region, take \(x,\theta,\phi\) constant and increase \(t\)
through one period

\[
\Delta t=4\pi\lambda.
\]

The orbit is timelike and its proper duration is

\[
\boxed{
\Delta\tau_{\rm CTC}
=
4\pi\lambda
\sqrt{
(k-2)\frac{x^2-1}{D(x)}
}.
}
\]

For finite \(x>1\) away from a curvature singularity this is finite.

These constant-position CTCs need not be geodesics, so maintaining them can
require acceleration. But once a physical controllable probe reaches the NUT
region, the background does contain finite-proper-time closed timelike
worldlines.

---

# 11. No-go mechanisms now excluded

The following simple chronology-protection mechanisms have been eliminated for
this model:

1. **All \(\alpha'\) corrections remove the CTC region:** false by the exact
   CFT geometry.
2. **Curvature blows up at the first chronology horizon:** false; generic
   curvature is finite at \(x=1\).
3. **The exact string coupling blows up at \(x=1\):** false; \(D(1)\) is
   finite and nonzero.
4. **The simplest wrapped-string area necessarily diverges:** false by the
   earlier repository calculation.
5. **Every minisuperspace wave is perfectly reflected:** false by the finite
   flux and \(V\to0\) calculation above.
6. **A separate BTZ/Misner winding sector is required:** false/reclassified
   by the Fable analysis; chronology-relevant candidates belong to the
   untwisted spectrum.

These results materially narrow where chronology protection can still occur.

---

# 12. What can still kill physical time travel

The remaining negative mechanisms are higher-level and genuinely quantum.

## 12.1 Full heterotic BRST cohomology

A scalar minisuperspace mode is not automatically a physical string state.
The chronology-relevant candidate must satisfy

\[
Q_{\rm BRST}|\Psi\rangle=0
\]

modulo exact states, together with both gauge constraints, Virasoro
conditions, GSO conditions and level matching.

It remains possible that all chronology-relevant untwisted candidates are
removed here.

## 12.2 Norm and representation range

The required hyperbolic \(SL(2,\mathbb R)\) representation could be
nonunitary, negative norm, or nonnormalizable.

No Taub--NUT-specific theorem establishing this exclusion has been found.

## 12.3 Interaction instability

This remains a serious candidate for chronology protection.

Exact heterotic Gödel models exhibit chronology-related string
instabilities. Misner string theory has physical chronology-related states but
strong pair production and problematic loop/scattering behavior.

Thus free transmission does not imply a usable time machine.

## 12.4 Finite-\(g_s\) backreaction

The target geometry is exact in \(\alpha'\), not automatically exact in
string loops. Backreaction could turn the chronology horizon into a barrier or
destroy the useful CTC region.

No Taub--NUT-specific all-\(g_s\) result is known here.

## 12.5 Operational return observable

Support in a region containing CTCs is not yet the same as a demonstrated
information-return protocol.

A positive final result needs a BRST/gauge-invariant relational observable
that distinguishes an actual closed-timelike return from mere wave support in
the NUT region.

---

# 13. Pressure from prior art

The original Johnson--Svendsen exact CFT already shows that string theory can
define a background whose CTC structure survives \(\alpha'\) corrections.
Svendsen's global analysis studies classical propagation and analytic
continuation across the regions.

Nearby gauged-WZW models strengthen the conclusion that CTC-containing exact
CFTs need not be meaningless. The Nappi--Witten cosmology has static regions
with CTCs; D-brane analyses found well-behaved probe wavefunctions in those
regions. The Elitzur--Giveon--Kutasov--Rabinovici quotient CFT connects
cosmological regions to static CTC-containing regions.

There is also direct classical-gravity evidence that ordinary Lorentzian
Taub--NUT is perturbatively fragile. Holzegel (gr-qc/0602045) found that
finite time-dependent \(SU(2)\)-invariant tensor perturbations cannot be made
regular both at the horizon and infinity, and interpreted this as linear
instability of Lorentzian Taub--NUT. This is a serious negative prior, but it
is not a theorem about the exact heterotic background: the latter contains a
nontrivial dilaton, \(B\)-field and gauge fields and includes all
\(\alpha'\) corrections in its target geometry. Thus the vacuum Einstein
instability cannot simply be imported as the missing stringy no-go.

But related models also supply warning signs: heterotic Gödel strings can
destabilize chronology-violating backgrounds; Misner-space interactions can
be singular; holographic time-machine constructions can generate
disconnection or singular barriers after backreaction; standard QFT at
compactly generated chronology horizons faces the Kay--Radzikowski--Wald
microlocal obstruction.

So prior art does not settle this Taub--NUT model either way. It moves the
burden from geometry to physical-state and interaction consistency.

---

# 14. Binary verdict

If forced to choose only between “possible” and “impossible,” the current
evidence does **not** justify “impossible.”

The strongest defensible conclusion is

\[
\boxed{
\textbf{Kinematically possible in the exact background; operational full-string time travel remains unproved.}
}
\]

In repository gate language:

\[
\boxed{
\textbf{the candidate passes the geometry gate and the minisuperspace
horizon-transmission gate, but has not passed BRST, interaction, and
operational-return gates.}
}
\]

Therefore:

### Impossible

**NOT SUPPORTED.**

### Fully demonstrated operational time travel

**NOT ESTABLISHED.**

### Live exact-string time-machine candidate

\[
\boxed{\textbf{YES.}}
\]

---

# 15. Shortest next calculation

Do not return to metric or winding-sector calculations.

The next decisive target is

\[
\boxed{
\textbf{untwisted BRST physical-state existence}
}
\]

for chronology-relevant hyperbolic \(SL(2,\mathbb R)\) charge.

Use the already identified constraints

\[
\mathcal G_A=0,
\qquad
\mathcal G_B=0,
\]

together with exact heterotic Virasoro conditions.

If a state survives, insert its actual \(\omega,\Lambda\) and charge data into
the exact radial problem derived here and compute a physical
Taub-to-NUT flux/two-point/reflection observable.

A decisive positive intermediate result is

\[
\boxed{
\exists\,|\Psi\rangle_{\rm BRST}:
\qquad
\mathcal F_{\rm Taub\to NUT}\neq0.
}
\]

A decisive negative result is

\[
\boxed{
\text{all chronology-relevant candidates are absent, BRST-exact,
nonunitary, or nonnormalizable.}
}
\]

Until one of those is obtained, the exact heterotic Taub--NUT model remains a
live but unproven candidate for physical travel to the past.

---

# 16. References

1. C. V. Johnson and H. G. Svendsen, *An Exact String Theory Model of Closed
   Time-Like Curves and Cosmological Singularities*, Phys. Rev. D 70, 126011
   (2004), arXiv:hep-th/0405141.

2. H. G. Svendsen, *Aspects of plane waves and Taub--NUT as exact string
   theory solutions*, PhD thesis, Durham University (2004).

3. H. G. Svendsen, *Global properties of an exact string theory solution in
   two and four dimensions*, Phys. Rev. D 73, 064032 (2006),
   arXiv:hep-th/0511289.

4. I. Bars and K. Sfetsos, *SL(2,R)xSU(2)/R^2 string model in curved
   spacetime and exact conformal results*, Phys. Lett. B 301 (1993) 183,
   arXiv:hep-th/9208001.

5. S. Elitzur, A. Giveon, D. Kutasov and E. Rabinovici,
   *From Big Bang to Big Crunch and Beyond*, JHEP 06 (2002) 017,
   arXiv:hep-th/0204189.

6. Y. Hikida, R. R. Nayak and K. L. Panigrahi,
   *D-branes in a Big Bang/Big Crunch Universe: Nappi-Witten Gauged WZW
   Model*, JHEP 09 (2005) 023, arXiv:hep-th/0503148.

7. D. Israël, *Quantization of heterotic strings in a Gödel/Anti de Sitter
   spacetime and chronology protection*, JHEP 01 (2004) 042,
   arXiv:hep-th/0310158.

8. M. Berkooz, B. Pioline and M. Rozali,
   *Closed Strings in Misner Space: Cosmological Production of Winding
   Strings*, JCAP 08 (2004) 004, arXiv:hep-th/0405126.

9. B. S. Kay, M. J. Radzikowski and R. M. Wald,
   *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy
   Horizon*, Commun. Math. Phys. 183 (1997) 533.

10. R. Emparan and M. Tomašević, *Holography of time machines*,
    JHEP 03 (2022) 212, arXiv:2107.14200.

---

# 17. Restart point

The exact horizon/minisuperspace obstruction test is now done.

Restart from

\[
\boxed{
\text{full untwisted heterotic BRST state with chronology-relevant charge}
}
\]

and determine whether such a state can be inserted into the exact
transmission problem.

That is the shortest route to changing the answer from “live candidate” to
either “physically impossible in this model” or “physical string transmission
into the CTC region exists.”
