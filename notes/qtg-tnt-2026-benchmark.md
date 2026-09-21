# 2026 QTG-TNT Benchmark: Regular Metric from a Singular Curvature Coupling

Primary reference:

A. Colléaux, I. Kolář, T. Málek,
*Quasi-topological gravity for 4-dimensional Taub-NUT, near-horizon extreme
Kerr, and swirling symmetries*,
arXiv:2606.17784 (2026).

This paper constructs four-dimensional metric theories with
quasi-topological integrability not only for static spherical metrics but for
the larger Taub-NUT-type (TNT) symmetry class.

It contains a particularly simple infinite-tower model with a closed-form
regular static black hole.

The result is highly relevant to Spacetime Screening, but it also exposes a
new failure mode:

\[
\boxed{
\text{finite metric curvature is produced by a coupling that becomes singular
at the limiting curvature}.
}
\]

## 1. First-order QTG-TNT action

The simplest first-order QTG-TNT family is

\[
I_1
=
\int d^4x\sqrt{-g}
\left[
-2\Lambda
+
R
+
A(\ell^2 R_3)R_4
\right],
\]

with

\[
A(x)
=
\sum_{p=1}^\infty \alpha_p x^p.
\]

The quantities \(R_3,R_4\) are non-analytic scalar functions of polynomial
curvature invariants chosen to reduce to independent Riemann components on
TNT geometries.

The paper explicitly notes that these invariant representatives are
non-unique away from the TNT sector and that broader metric configurations and
perturbations are outside the scope of the construction.

## 2. Static single-function reduction

For

\[
ds^2=-a(r)dt^2+\frac{dr^2}{a(r)}+r^2d\Omega^2
\]

with \(\Lambda=0\), spherical topology \(k=1\),

\[
R_3
=
\frac{2(1-a)}{r^2}.
\]

The once-integrated field equation is

\[
-\left[
1+\frac12A(\ell^2R_3)
\right]a
+
1
=
\frac{2m}{r}.
\]

This has essentially GR-level algebraic integrability.

## 3. Why an infinite nonpolynomial tower is required

Assume a regular core

\[
a(r)
=
1+a_2r^2+a_3r^3+\cdots.
\]

For nonzero mass, the right-hand side behaves as

\[
\frac{2m}{r}.
\]

The left-hand side can reproduce this singular source while keeping \(a\)
finite only if the function \(A(x)\) becomes singular at the finite limiting
curvature

\[
x_*=-2\ell^2a_2.
\]

The paper derives, for the standard regularity class with \(a_3\neq0\),

\[
A(x)
\sim
\frac{\text{const.}}{x-x_*}.
\]

Thus finite polynomial order cannot produce the regular core in this
first-order family.

The regular metric is generated precisely because the **theory function**
becomes non-analytic at the limiting curvature.

## 4. Simple exact model

The paper's simplest example is

\[
\boxed{
A(x)=\frac{2x}{1-x}
}
\]

which corresponds to the infinite series

\[
A(x)
=
2\sum_{p=1}^\infty x^p
\]

inside its radius of convergence.

The unique static spherical solution is

\[
\boxed{
a(r)
=
\frac{
(r-2m)(r^2-2\ell^2)
}{
r^3-2r\ell^2+4m\ell^2
}.
}
\]

It is asymptotically Schwarzschild.

## 5. Curvature variable

For this solution,

\[
x(r)
\equiv
\ell^2R_3
=
\boxed{
\frac{
4m\ell^2
}{
r^3-2r\ell^2+4m\ell^2
}
}.
\]

The field equation can be rewritten as

\[
a
=
\left(1-\frac{2m}{r}\right)(1-x).
\]

Thus

\[
\Sigma_{\rm TNT}
\equiv
1-x
\]

multiples the Schwarzschild metric function.

However, unlike the Hayward QTG response, this is not a monotonic
susceptibility function of \(2m/r^3\) alone.

## 6. The action pole is reached by the physical solution

At the center,

\[
\boxed{
x(r)\to1.
}
\]

Also, at

\[
\boxed{
r=\sqrt2\,\ell,
}
\]

we have

\[
x=1.
\]

But

\[
A(x)=\frac{2x}{1-x}
\]

has its pole precisely at

\[
x=1.
\]

Therefore the physical solution touches the singularity of the theory function
both:

- at the regular center;
- at the theory-fixed horizon.

The reduced field equation remains meaningful through correlated limiting
products.

For a generic four-dimensional fluctuation this is a major warning.

## 7. Center expansion

The exact metric expands as

\[
\boxed{
a(r)
=
1
-\frac{r^2}{2\ell^2}
-\frac{r^3}{4m\ell^2}
-\frac{r^4}{8m^2\ell^2}
+O(r^5).
}
\]

The leading core is de Sitter-like with effective radius

\[
L_{\rm core}^2=2\ell^2.
\]

Polynomial curvature invariants are finite:

\[
\boxed{
R(0)=\frac{6}{\ell^2},
}
\]

\[
\boxed{
R_{\mu\nu}R^{\mu\nu}(0)
=
\frac{9}{\ell^4},
}
\]

and

\[
\boxed{
K(0)=\frac{6}{\ell^4}.
}
\]

These limiting values are independent of the mass.

## 8. The geometry is not smoothly regular in curvature derivatives

The unavoidable odd term

\[
-\frac{r^3}{4m\ell^2}
\]

makes curvature invariants non-even at the center.

For example,

\[
R(r)
=
\frac{6}{\ell^2}
+
\frac{5}{m\ell^2}r
+
O(r^2).
\]

The covariant d'Alembertian therefore behaves as

\[
\boxed{
\Box R
\sim
\frac{10}{m\ell^2\,r}
}
\]

near the center.

This reproduces the paper's observation that polynomial curvature invariants
can remain finite while curvature-derivative invariants diverge.

Thus this model is "regular" only in the polynomial-curvature sense.

## 9. Horizons

The numerator factorizes, so two horizon radii are exact:

\[
\boxed{
r_{h,1}=2m,
}
\]

and

\[
\boxed{
r_{h,2}=\sqrt2\,\ell.
}
\]

The second horizon is fixed by the theory rather than by the mass.

They coincide at

\[
\boxed{
m_{\rm ext}
=
\frac{\ell}{\sqrt2}.
}
\]

The model therefore has an extremal remnant scale of order \(\ell\).

## 10. Low-mass singularity

The denominator is

\[
D(r)
=
r^3-2r\ell^2+4m\ell^2.
\]

Its positive minimum occurs at

\[
r_{\rm min}
=
\sqrt{\frac23}\,\ell.
\]

The double-root condition gives

\[
\boxed{
m_{\rm crit}
=
\frac{2\ell}{3\sqrt6}.
}
\]

For

\[
m>m_{\rm crit}
\]

the static solution is regular.

At

\[
m=m_{\rm crit}
\]

the denominator develops a positive double root and curvature becomes
unbounded.

For

\[
0<m<m_{\rm crit},
\]

two positive denominator roots split the geometry into singular branches.

The extremal mass satisfies

\[
m_{\rm ext}>m_{\rm crit},
\]

so semiclassical Hawking evolution can in principle stop at extremality before
entering the low-mass singular parameter region.

## 11. Surface gravities

At the mass-dependent horizon,

\[
a'(2m)
=
\frac{
2m^2-\ell^2
}{
4m^3
}.
\]

For the outer horizon in the large-mass branch,

\[
T_H
=
\frac{
2m^2-\ell^2
}{
16\pi m^3
}.
\]

It approaches the Schwarzschild value at large mass and vanishes at

\[
m=\ell/\sqrt2.
\]

At the theory-fixed horizon,

\[
a'(\sqrt2\ell)
=
\frac{
\sqrt2(\sqrt2\ell-2m)
}{
2\ell m
}.
\]

The two expressions vanish simultaneously when the horizons merge.

## 12. Covariant-action differentiability problem

The non-analytic invariant \(R_4\) is constructed as a square-root-type
discriminant of polynomial curvature invariants, and the SF branch is
covariantly characterized by

\[
\boxed{
R_4=0.
}
\]

The action correction is *linear* in this quantity:

\[
A(\ell^2R_3)R_4.
\]

Writing schematically

\[
R_4=\sqrt{\Delta},
\]

a generic invariant-space variation contains

\[
\frac{\partial R_4}{\partial\Delta}
=
\frac{1}{2\sqrt{\Delta}},
\]

which is non-differentiable at

\[
R_4=0.
\]

Thus the exact black-hole branch lies on a nondifferentiable surface of this
representative action.

In addition, at the regular core and fixed horizon,

\[
A\to\infty.
\]

So the generic variation of

\[
A\,R_4
\]

is more singular, not less, unless the allowed variation is restricted to the
TNT/SF submanifold or an additional extension prescription is supplied.

## 13. This concern is consistent with the paper's own scope

The authors explicitly state that the choice of invariant representatives is
highly non-unique away from the TNT geometries and that investigation of
broader metric configurations or perturbations lies beyond the scope of the
work.

They also note that their non-analytic representatives can be ill-defined on
other important backgrounds, including conformally flat/maximally symmetric
limits.

Therefore the regular black-hole construction should be interpreted as a
strong symmetry-sector result, not yet as a principal-safe four-dimensional
perturbative theory.

## 14. Comparison with the earlier 2026 pure-gravity Hayward lift

Both constructions share a pattern:

1. the symmetry-reduced field equations are unusually simple;
2. a regular static black hole is obtained exactly;
3. the explicit four-dimensional realization uses non-analytic curvature
   invariants;
4. generic off-symmetry perturbative differentiability is not established.

They differ in the background response:

### Borissova-Carballo-Rubio Hayward response

\[
\psi(s)=\frac{s}{1+\ell^2s},
\]

with smooth saturation and vanishing curvature susceptibility.

### QTG-TNT first-order response

regularity requires

\[
A(x)
\]

itself to develop a finite-curvature singularity.

For the simple model,

\[
A(x)=2x/(1-x).
\]

Thus the QTG-TNT mechanism is less naturally interpreted as smooth
screening.

## 15. Candidate status

### Strengths

- four-dimensional metric-only construction;
- very broad symmetry integrability;
- exact static, Taub-NUT, NHEK, swirling, and Eguchi-Hanson-type solutions;
- exact regular static black hole for a finite mass range;
- solution-independent polynomial-curvature bounds over the physically
  relevant mass range;
- extremal remnant before the low-mass singular regime.

### Failures / unresolved issues for this project

- the required coupling is singular at the limiting curvature;
- curvature-derivative invariants diverge at the center;
- the representative action is non-analytic and nondifferentiable on the SF
  branch in generic invariant directions;
- perturbations outside the TNT symmetry class are not established;
- low-mass metric singularities exist below a theory-dependent critical mass.

## 16. Verdict for Spacetime Screening

This candidate is highly informative but does not pass the current
principal-safe action-selection gate.

It should be retained as a benchmark for the statement:

\[
\boxed{
\text{a regular background can be generated by a singular constitutive law}.
}
\]

For the Spacetime Screening program, the preferred mechanism remains one in
which the *response softens smoothly* while the underlying action and physical
principal operator remain differentiable.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/qtg_tnt_2026_benchmark.py
\`\`\`

to verify the exact solution, center curvature, derivative-curvature
singularity, horizon structure, critical masses, and the action-pole
locations.
