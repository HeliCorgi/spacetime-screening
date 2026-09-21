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


## 11. Perturbative status of the vector benchmark

The vector benchmark has a published linear radial-stability result. In the
spherically symmetric time-dependent sector, the vector equations constrain
the vector perturbations in terms of the metric perturbations, and the
remaining equations reduce to a pure time-reparametrization mode. Thus there
is no nontrivial radial linear mode.

However, the asymptotic quadratic spectrum is highly degenerate.

For one vector,

\[
\mathcal L[W]
=
4G^{\mu\nu}W_\mu W_\nu
+
8W^2\nabla_\mu W^\mu
+
6(W^2)^2.
\]

Around

\[
g_{\mu\nu}=\eta_{\mu\nu},
\qquad
W_\mu=0,
\]

the interaction orders are

\[
G^{\mu\nu}W_\mu W_\nu=O(hw^2),
\]

\[
W^2\partial\cdot W=O(w^3),
\]

\[
(W^2)^2=O(w^4).
\]

Therefore

\[
\boxed{
S^{(2)}_{\rm vector}=0
}
\]

on the asymptotic Minkowski vacuum.

This is compatible with the authors' interpretation of the vectors as
nonlinear constraints. It also means that, if a vector degree of freedom
survives the complete constraint analysis, it has no conventional quadratic
propagator and would be strongly coupled around the vacuum.

On a constant null vector background, the quadratic fixed-metric vector
Lagrangian is only first order in derivatives,

\[
\mathcal L_2
=
16(\bar W\cdot w)\partial\cdot w
+
24(\bar W\cdot w)^2,
\]

and its velocity Hessian vanishes.

The corresponding principal symbol is

\[
P^\mu{}_\nu(k)
=
2(\bar W^\mu k_\nu-k^\mu\bar W_\nu),
\]

which obeys

\[
\det P=0,
\qquad
{\rm rank}\,P\le2.
\]

Thus the vector sector is a degenerate constrained system, not an ordinary
hyperbolic Proca wave operator.

The decisive next step is a full metric-vector ADM/Dirac constraint count and
non-spherical perturbation analysis.

See
[notes/vector-constraint-analysis.md](notes/vector-constraint-analysis.md).

## 12. Extremal near-horizon structure

For the fully extremal regular branch,

\[
f(r)
=
1-
\frac{2Mr^2}{r^3+32M^3/27},
\qquad
r_h=\frac{4M}{3}.
\]

The horizon is a double zero and

\[
f''(r_h)=\frac{9}{8M^2}.
\]

Consequently the near-horizon geometry is

\[
\boxed{
AdS_2\times S^2
}
\]

with equal radii

\[
L_{AdS_2}=R_{S^2}=r_h=\frac{4M}{3}.
\]

At the horizon,

\[
R=0,
\]

and the effective stress tensor satisfies

\[
p_r=-\rho,
\qquad
p_t=+\rho,
\]

so it is traceless and Maxwell-like.

This extremal throat explains why the Aretakis instability is a natural next
stability question even though ordinary mass inflation has been removed.

A direct test-field calculation confirms that a minimally coupled massless
s-wave has the horizon conserved quantity

\[
H_0
=
\left[
\partial_r\Phi+\frac{\Phi}{r_h}
\right]_{r_h},
\qquad
\partial_vH_0=0.
\]

If \(\Phi\) decays along the horizon while \(H_0\neq0\), then

\[
\partial_r^2\Phi
\sim
-\frac{H_0}{r_h^2}v,
\]

so the second transverse derivative grows linearly. Thus the benchmark has a
genuine Aretakis channel for external test fields even though the published
coupled radial metric-vector sector has no nontrivial linear mode.

See
[notes/extremal-near-horizon.md](notes/extremal-near-horizon.md) and
[notes/aretakis-test-scalar.md](notes/aretakis-test-scalar.md).

## 13. Radial tensor principal cone

The strongest current obstruction to the two-vector benchmark comes from the
high-frequency radial tensor principal symbol.

For a local transverse-traceless graviton propagating radially, the two
background vectors are parallel and null. Their difference enters through

\[
D_{\mu\nu}
=
A_\mu A_\nu-B_\mu B_\nu.
\]

The pure-TT quadratic principal action is a null Kerr-Schild deformation with

\[
\boxed{
g_{\rm T}^{\mu\nu}
=
g^{\mu\nu}
+
4\ell^2
\left(
A^\mu A^\nu-B^\mu B^\nu
\right)
}.
\]

On the regular branch,

\[
a^2-b^2
=
-\frac{Mq}{r(r^3+2q\ell^2)}.
\]

Since the null vectors point along the ingoing radial direction, the effective
radial characteristic function is

\[
f_{\rm T}
=
f+4\ell^2(a^2-b^2).
\]

Using

\[
f
=
1-\frac{2Mr^2}{r^3+2q\ell^2},
\]

the screening terms cancel exactly:

\[
\boxed{
f_{\rm T}(r)
=
1-\frac{2M}{r}.
}
\]

Thus the radial pure-TT characteristic cone is Schwarzschild-like even though
the background metric is regular.

Its characteristic horizon is

\[
\boxed{
r_{\rm T}=2M,
}
\]

while every regular-background horizon obeys

\[
r_h<2M
\]

for \(q>0\).

If this principal metric survives the complete spherical constraint
reduction, its characteristic curvature is

\[
K_{\rm T}
=
\frac{48M^2}{r^6},
\]

so the perturbation operator retains a Schwarzschild-like singular core.

This is not yet a proof that the full theory is ill posed. The complete
\(l\ge2\) odd quadratic action must still be reduced. It is, however, a sharp
warning that

\[
\boxed{
\text{background regularity}
\not\Rightarrow
\text{regular characteristic geometry}.
}
\]

See
[notes/tensor-principal-cone.md](notes/tensor-principal-cone.md).


## 14. Pure-gravity quasitopological benchmark

The current replacement benchmark is four-dimensional nonpolynomial
quasitopological gravity, where the screening mechanism is encoded directly
in the curvature response rather than in auxiliary-field cancellation.

For the Hayward realization define

\[
\psi=\frac{1-f}{r^2},
\qquad
s=\frac{2M}{r^3}.
\]

The characteristic relation is

\[
\boxed{
\frac{\psi}{1-\ell^2\psi}=s
}
\]

or

\[
\boxed{
\psi(s)=\frac{s}{1+\ell^2s}.
}
\]

Therefore

\[
\psi\to\frac1{\ell^2},
\qquad
\frac{d\psi}{ds}
=
\frac1{(1+\ell^2s)^2}
\to0
\]

in the strong-source limit.

This motivates a more intrinsic definition of screening:

\[
\boxed{
\text{screening}
=
\text{suppression of curvature susceptibility}
}
\]

rather than a literal coordinate-dependent Newton constant.

Defining

\[
\Sigma=1-\ell^2\psi,
\]

one finds

\[
\Sigma(r)
=
\frac{r^3}{r^3+2M\ell^2}
\]

and

\[
\frac{d\psi}{ds}=\Sigma^2.
\]

Thus the old diagnostic screening factor has a direct interpretation as the
distance from the saturation pole in curvature-response space.

The local nonpolynomial theory gives the exact regular vacuum background and
second-order spherical dynamics, but full nonspherical perturbative health
still has to be established.

A July 2026 nonlocal-quasitopological preprint reports an infinite-derivative
completion that is ghost-free, avoids strong-coupling instabilities, preserves
exact spherical regular black holes, and satisfies a perturbative Birkhoff
theorem. These claims now define the next benchmark to reproduce on the
black-hole background.

See
[notes/pure-gravity-qtg-benchmark.md](notes/pure-gravity-qtg-benchmark.md)
and
[docs/principal-safe-screening.md](docs/principal-safe-screening.md).


## 15. Covariant-lift differentiability

The explicit representative four-dimensional lift used to realize the
nonpolynomial spherical theory has an additional obstruction that appears
before a nonspherical tensor principal symbol can be defined.

The densities \(\mathcal P\) and \(\mathcal K\) contain the denominator

\[
D
=
I_{C^2}I_{R^2C}
+
2I_{\hat R^2}I_{C^3}.
\]

On a generic warped-product background,

\[
\boxed{
D
=
-\frac13
(\eta^2-2\tau)\Omega^3.
}
\]

For a static single-function metric,

\[
\tau=\frac{\eta^2}{2},
\]

so

\[
D=0
\]

identically along the entire Hayward branch.  The corresponding numerators
also vanish and the spherical ratios possess the removable limits
\(\mathcal P\to\psi\) and \(\mathcal K\to\mathcal R\).

However, generic four-dimensional invariant gradients behave as

\[
\frac{\partial\mathcal P}
{\partial I_{\hat R^3}}
\sim
\frac{1}{6(\eta^2-2\tau)},
\]

\[
\frac{\partial\mathcal K}
{\partial I_{\hat R^3}}
\sim
-\frac{1}{3(\eta^2-2\tau)}.
\]

For the complete representative QTG action, cancellation of this divergence
would require the additional background condition

\[
(\mathcal R-2\psi)H_4'
+
(\eta+2\psi)^2H_4''
=
0.
\]

The explicit Hayward functions do not satisfy this identically.

Alternative algebraic lifts do not trivially cure the problem. A
square-root extraction from \(I_{\hat R^2}\) reconstructs the correct
single-function branch, but its derivative diverges when the traceless Ricci
tensor vanishes.  The Weyl-ratio density \(\mathcal H\) likewise has divergent
invariant gradients on Weyl-zero surfaces.

Therefore the representative rational lift is suitable as a spherical
proof-of-principle construction but is not presently a regular starting point
for a generic nonspherical perturbation calculation.

This does not invalidate the reduced QTG response law.  It strengthens the
requirement that a full screening theory possess a four-dimensional action
that is differentiable on the background in the physical perturbation
directions.

See
[notes/covariant-lift-degeneracy.md](notes/covariant-lift-degeneracy.md).


## 16. QTG-TNT regularity by singular constitutive law

A separate June 2026 four-dimensional construction extends
quasi-topological integrability to the full Taub-NUT-type symmetry class.

Its first-order family has action

\[
I_1
=
\int\sqrt{-g}
\left[
-2\Lambda+R+A(\ell^2R_3)R_4
\right].
\]

For the static spherical SF branch,

\[
R_4=0,
\qquad
R_3=\frac{2(1-a)}{r^2}.
\]

The simple infinite-tower choice

\[
A(x)=\frac{2x}{1-x}
\]

gives the exact metric

\[
a(r)
=
\frac{
(r-2m)(r^2-2\ell^2)
}{
r^3-2r\ell^2+4m\ell^2
}.
\]

The center has finite polynomial curvature,

\[
R(0)=\frac6{\ell^2},
\qquad
K(0)=\frac6{\ell^4},
\]

but

\[
\Box R\sim\frac{10}{m\ell^2r}.
\]

More importantly, the reduced field equation requires

\[
x=\ell^2R_3\to1
\]

at the regular center, exactly where

\[
A(x)\to\infty.
\]

Thus this model regularizes the metric through a **singular constitutive
function** rather than a smoothly vanishing curvature susceptibility.

The theory's representative invariants are non-analytic and the SF branch is
defined by \(R_4=0\). Generic off-symmetry perturbative differentiability is
not established and is outside the source paper's scope.

This provides another design constraint:

\[
\boxed{
\text{finite curvature produced by a singular action derivative is not
principal-safe screening}.
}
\]

See
[notes/qtg-tnt-2026-benchmark.md](notes/qtg-tnt-2026-benchmark.md).

## 17. Phase-transition hypothesis

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

## 18. What would count as success

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


## 19. 4D analytic GQTG core-scaling constraint

For the known four-dimensional genuine GQTG family, the all-order integrated
single-function equation gives a sharp regular-core scaling law.

For an exact de Sitter-type core

\[
f(r)=1-cr^2,
\]

the order-\(n\) genuine GQTG contribution behaves as

\[
\boxed{
F_n=-\frac12 c^n r^3
}
\]

up to the normalization of the order-\(n\) coupling.

For a generic regular series

\[
f(r)=1-cr^2+dr^3+O(r^4),
\]

one still finds

\[
\boxed{
\frac{F_n}{r^3}
\to
-\frac12c^n
+\frac{3}{16}n(n-1)c^{n-3}d^2.
}
\]

Thus every finite curvature order is \(O(r^3)\) at the center.

A finite truncation therefore cannot balance a nonzero vacuum mass integration
constant at a regular center.  If an infinite tower converges normally at the
limiting curvature, its sum also remains \(O(r^3)\).

Hence a nonzero-mass regular vacuum core requires a non-uniform resummation at
the limiting curvature.

If a finite curvature variable approaches

\[
c(r)-c_*=a r^p+\cdots,
\]

and the integrated equation has the schematic form

\[
M_0=r^3\mathcal G(c(r))+\cdots,
\qquad M_0\ne0,
\]

then necessarily

\[
\boxed{
\mathcal G(c)
\sim
|c-c_*|^{-3/p}.
}
\]

This clarifies an important point: a pole in the **inverse/reduced response**
is not automatically pathological.  Curvature saturation with an unbounded
source necessarily makes the inverse response diverge.

The actual acceptance test is whether the full four-dimensional action and
the reduced physical perturbation operator remain differentiable,
nondegenerate, and hyperbolic at the limiting curvature.

See
[notes/analytic-gqtg-core-scaling.md](notes/analytic-gqtg-core-scaling.md).


## 18. 2026 QTG-TNT square-root obstruction

The first-order QTG-TNT construction of Colléaux, Kolář, and Málek uses

\[
R_4
=
\sqrt{
\frac{2I_6}{3}
-
\frac{2I_{11}}{I_1}
}
\]

and a correction

\[
A(\ell^2R_3)R_4.
\]

The single-function black-hole branch is exactly \(R_4=0\).

Generic curvature derivatives satisfy

\[
\frac{\partial R_4}{\partial I_6}
=
\frac{1}{3R_4},
\qquad
\frac{\partial^2R_4}{\partial I_6^2}
=
-\frac{1}{9R_4^3}.
\]

Within TNT, a smooth signed perturbation
\(R_4^{\rm signed}\propto\epsilon\) is reconstructed covariantly as
\(\sqrt{(R_4^{\rm signed})^2}\propto|\epsilon|\), so the first variation has a
cusp even before considering generic nonsymmetric directions.

For the explicit regular-black-hole example

\[
A(x)=\frac{2x}{1-x},
\]

one finds

\[
A(x(r))
=
\frac{8m\ell^2}{r(r^2-2\ell^2)}
\sim-\frac{4m}{r}
\]

at the regular center, and \(A\) also diverges at
\(r=\sqrt2\,\ell\).

The source classification proves that this tension is structural:
analytic Riemann-only scalar actions restricted to TNT contain \(R_4\) only
through even powers. Therefore a nonzero linear \(R_4\) term, which is what
gives the nontrivial first-order/algebraic Class-I equations, necessarily
requires non-analytic curvature dependence.

The project therefore keeps this construction as a symmetry-sector
integrability benchmark, not as the current principal-safe 4D completion.

See
[notes/r4-differentiability.md](notes/r4-differentiability.md) and
[notes/r4-analyticity-obstruction.md](notes/r4-analyticity-obstruction.md).


## 19. Odd-vector kinetic obstruction in the two-vector benchmark

Using the published generalized-Proca odd-parity quadratic-action structure,
the additive two-vector model has no direct Maxwell-type transverse-vector
kinetic block.  The metric-vector derivative mixing therefore induces

\[
\boxed{
K_{\rm vec}
=
-\frac{cc^{\rm T}}{C_1}.
}
\]

For the static exterior,

\[
C_1>0,
\]

so the derivative-active vector combination has a negative kinetic
eigenvalue.  The vector combination orthogonal to \(c\) has zero principal
quadratic kinetic term.

On the regular branch,

\[
\lambda_{\rm vec}
=
-\frac{
8\ell^4(a^2+b^2)
}{
f^2r^2
},
\]

and near the regular center,

\[
\lambda_{\rm vec}
\sim
-\frac{\ell^4q^2}{r^6}.
\]

The corresponding radial principal matrices satisfy

\[
R=-2fK,
\qquad
G=f^2K,
\]

so the derivative-active vector mode has

\[
\boxed{
P_{\rm vec}(\omega,k)
\propto
(\omega+fk)^2.
}
\]

The \(l=1\) sector makes the sign especially transparent.  Since there is no
local odd gravitational-wave degree of freedom for the dipole, the principal
derivative action reduces to

\[
\boxed{
\mathcal L_{l=1}^{\rm pr}
=
-\frac1{C_1}
\left[
c^{\rm T}(\dot u-fu')
\right]^2.
}
\]

Its canonical Hamiltonian contains a negative quadratic momentum term.

This is currently a **new-calculation candidate**, not yet a publication-level
ghost theorem.  The final check is to reproduce the entire two-vector
spherical-harmonic quadratic action directly from the original action and
verify that no additional degeneracy removes the active negative-kinetic
combination.

This result is independent of, and more immediately damaging than, the
separate question of whether the \(l\ge2\) physical tensor master mode retains
the hidden Schwarzschild characteristic.

See
[notes/vector-odd-kinetic-analysis.md](notes/vector-odd-kinetic-analysis.md).
