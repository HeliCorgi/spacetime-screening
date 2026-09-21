# Theory Skeleton

This document records the current mathematical skeleton of the **Spacetime Screening** program.

It deliberately separates kinematic requirements, dynamical hypotheses, and quantum-gravity requirements. Nothing in this file is a claim of a completed theory.

## 1. Classical failure mode

For a Schwarzschild black hole,

\[
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2,
\qquad
f(r)=1-\frac{2G_N M}{r}.
\]

The Kretschmann scalar is

\[
\mathcal K
=
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=
\frac{48G_N^2M^2}{r^6},
\]

which diverges as \(r\to0\).

The project asks whether this divergence is an artifact of extrapolating low-energy gravitational variables beyond their regime of validity.

## 2. Effective screening diagnostic

A useful rewriting is

\[
f(r)=1-\frac{2M G_{\rm eff}(r)}{r}.
\]

This is a diagnostic representation, not permission to insert an arbitrary coordinate-dependent Newton constant into Einstein's equations. A viable model must derive the behavior from a generally covariant action or a well-defined nonlocal/nonperturbative theory.

A regular center requires

\[
1-f(r)=O(r^2).
\]

Therefore, in this diagnostic representation,

\[
G_{\rm eff}(r)=O(r^3)
\]

or faster as \(r\to0\).

## 3. Two geometric endpoints

### Finite-curvature / de Sitter-like core

If

\[
f(r)=1-\frac{r^2}{\ell^2}+O(r^n),
\]

then curvature invariants remain finite. In the exact de Sitter limit,

\[
R=\frac{12}{\ell^2},
\qquad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=
\frac{24}{\ell^4}.
\]

A representative regular-black-hole form is

\[
f(r)
=
1-\frac{2G_NMr^2}{r^3+2G_NM\ell^2}.
\]

It can be rewritten diagnostically as

\[
G_{\rm eff}(r)
=
G_N\frac{r^3}{r^3+2G_NM\ell^2}.
\]

Thus the dimensionful effective coupling tends to zero at the center while the geometry approaches a finite-curvature de Sitter core.

### Minkowski-like core

A stronger condition would be

\[
R_{\mu\nu\rho\sigma}\to0
\qquad(r\to0),
\]

with \(f(r)\to1\) faster than in the de Sitter case.

Such a core is more demanding. Both spatial infinity and the center can correspond to small curvature while requiring different dynamical behavior. This motivates an additional order parameter or branch label.

## 4. Why force language is insufficient

Inside a black hole, "gravitational force" is not a generally covariant observable. The invariant local statement concerns geodesic deviation,

\[
\frac{D^2\xi^\mu}{D\tau^2}
=
-R^\mu{}_{\nu\rho\sigma}
u^\nu\xi^\rho u^\sigma.
\]

Therefore the physically meaningful screening question is whether tidal curvature remains finite, saturates, decreases again, or ceases to be described by a classical metric.

## 5. Covariant screening variable

The fundamental screening variable should be covariant. Candidate inputs include

\[
R,\qquad
R_{\mu\nu}R^{\mu\nu},\qquad
\mathcal K=R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma},
\]

or a dynamically determined RG scale \(k[g,\Phi]\).

A toy invariant is

\[
\mathcal I=\ell_*^4\mathcal K.
\]

The project will avoid treating \(r\) itself as a fundamental screening variable.

## 6. Order-parameter model

To model a change of gravitational phase, introduce a scalar order parameter \(\chi\):

\[
S=
\int d^4x\sqrt{-g}
\left[
\frac{F(\chi)}{16\pi G_N}R
-\frac12(\nabla\chi)^2
-V(\chi,\mathcal I)
+\mathcal L_{\rm HC}
\right].
\]

A toy coupling is

\[
F(\chi)=e^{\chi^2},
\]

so that at the level of the effective Einstein coupling,

\[
G_{\rm eff}(\chi)=G_Ne^{-\chi^2}.
\]

A curvature-triggered potential can be written schematically as

\[
V(\chi,\mathcal I)
=
\frac{\mu^2}{2}
\left(1-\frac{\mathcal I}{\mathcal I_*}\right)\chi^2
+
\frac{\lambda}{4}\chi^4.
\]

For \(\mathcal I<\mathcal I_*\), the symmetric phase \(\chi=0\) is preferred. For sufficiently large \(\mathcal I\), a nonzero \(\chi\) can become preferred and the effective dimensionful gravitational response can decrease.

This remains useful as an order-parameter intuition, but the simplest static radial realization is now known to be insufficient.

For the restricted action

\[
S=\int\sqrt{-g}\left[
\frac{F(\chi)}{16\pi G}R
-\frac12(\partial\chi)^2
-V(\chi)
\right]
\]

with

\[
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2,
\qquad
\chi=\chi(r),
\]

the identity \(G^t{}_t=G^r{}_r\) implies

\[
\boxed{
F''(r)=-8\pi G\,\chi'(r)^2\le0
}.
\]

Smooth-center and asymptotically constant boundary conditions give
\(F'(0)=F'(\infty)=0\). Concavity then forces \(F'\equiv0\) and
\(\chi'\equiv0\). Therefore a nontrivial localized canonical radial scalar
cannot support the one-function Hayward geometry in this minimal model.

The same obstruction persists for healthy radial k-essence with \(P_X\ge0\).

See [notes/scalar-tensor-no-go.md](notes/scalar-tensor-no-go.md).

## 7. Covariant action benchmark: auxiliary vector hair

A 2026 vector-tensor construction provides an explicit action benchmark. In
geometric units, the regular branch has

\[
f(r)
=
1-
\frac{2Mr^2}{r^3+2q_a\ell^2}.
\]

It follows from a generally covariant two-vector action rather than from an
ad-hoc replacement \(G\to G(r)\).

The associated diagnostic screening factor is

\[
S(r)
=
\frac{r^3}{r^3+2q_a\ell^2},
\]

with \(S(0)=0\) and \(S(\infty)=1\).

The core scale is

\[
L_{\rm core}^2
=
\frac{q_a\ell^2}{M},
\]

so

\[
K(0)=\frac{24}{L_{\rm core}^4}.
\]

Two choices expose an important tradeoff:

- \(q_a=M\): the original Hayward form has universal
  \(K(0)=24/\ell^4\), but only one special mass is extremal.
- \(q_a=16M^3/(27\ell^2)\): every mass can lie on a fully extremal regular
  branch, but \(K(0)=2187/(32M^4)\), so the limiting curvature is no longer
  universal.

This benchmark therefore demonstrates that covariant screening-like geometry
is possible, while sharpening the next question: can one retain both a
universal microscopic curvature scale and robust inner-horizon stability?

See [notes/vector-hair-benchmark.md](notes/vector-hair-benchmark.md).

## 8. Connection with asymptotic safety

At a non-Gaussian UV fixed point, a dimensionless Newton coupling

\[
g(k)=k^2G(k)
\]

can approach a finite fixed-point value \(g_*\). Then

\[
G(k)\sim\frac{g_*}{k^2}
\qquad(k\to\infty).
\]

This is conceptually compatible with high-energy weakening of the dimensionful Newton coupling. It does not imply that quantum gravity becomes trivial, and it does not justify an arbitrary substitution \(G_N\to G(k(r))\).

## 9. Regularity can require more than screening

Suppose diagnostically

\[
G_{\rm eff}(r)\sim C r^p,
\qquad p\ge3.
\]

A Newtonianized potential behaves as

\[
\Phi(r)\sim -MC r^{p-1},
\]

so

\[
a_r=-\frac{d\Phi}{dr}
\sim +MC(p-1)r^{p-2}.
\]

Within this simplified interpretation, the innermost region is effectively repulsive even though the acceleration vanishes at the exact center.

This is not a theorem for all covariant gravity theories. It is a warning that screening alone may not stop already collapsing matter. A bounce, pressure, effective repulsion, branch transition, or non-geometric regime may be required.

## 10. Horizon-structure constraint

For a static asymptotically flat metric with \(f(\infty)>0\) and a regular center with \(f(0)>0\), a non-extremal outer horizon makes \(f\) negative immediately inside. Continuity then generically requires another zero before reaching the positive central region.

Static regular black holes therefore naturally tend to develop an inner horizon. Inner-horizon stability is a central constraint.

## 11. Phase-transition hypothesis

The stronger version of the project is

\[
\text{GR phase}
\rightarrow
\text{screened geometric phase}
\rightarrow
\text{non-geometric phase}
\rightarrow
\text{emergent geometry}.
\]

"Non-geometric" means that a single classical Lorentzian metric may no longer be an adequate state variable. It does not mean that the underlying quantum state disappears.

A conceptual state-space picture is

\[
\mathcal H_{\rm fundamental}
\supset
\mathcal H_{\rm geometric},
\]

where states in \(\mathcal H_{\rm geometric}\) admit an approximate description by \((M,g_{\mu\nu},\Phi)\), while sufficiently quantum states need not.

## 12. What would count as success

A serious model must derive, rather than assume:

1. a covariant action or nonperturbative definition;
2. the GR limit;
3. a regular or replaced high-curvature regime;
4. the correct propagating degrees of freedom;
5. absence of ghosts and fatal gradient instabilities;
6. a sensible initial-value problem;
7. dynamically formed black holes;
8. controlled inner-horizon behavior;
9. evaporation and backreaction;
10. observables that can distinguish the theory.

Until these are obtained, spacetime screening is a research program and organizing hypothesis.
