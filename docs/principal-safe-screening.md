# Principal-Safe Spacetime Screening

The vector benchmark exposed a failure mode that is easy to miss:

\[
\text{regular background metric}
\not\Rightarrow
\text{regular physical propagation}.
\]

This document upgrades the project's acceptance criteria.

## 1. Background screening criterion

A candidate should possess a high-curvature response that suppresses further
growth of physical curvature.

For the pure-gravity Hayward benchmark,

\[
s=\frac{2M}{r^3},
\qquad
\psi=\frac{s}{1+\ell^2s},
\]

so

\[
\frac{d\psi}{ds}
=
\frac1{(1+\ell^2s)^2}
\to0.
\]

This motivates defining background screening by

\[
\boxed{
\chi_{\rm curv}
\equiv
\frac{\partial\psi_{\rm physical}}
{\partial s_{\rm source}}
\to0
}
\]

in the ultraviolet/high-curvature regime.

## 2. Background regularity criterion

All independent curvature invariants of the physical background must remain
bounded, or the metric description must be demonstrably replaced by a
well-defined non-geometric phase before they diverge.

For a geometric regular core this includes, at minimum,

\[
R,
\qquad
R_{\mu\nu}R^{\mu\nu},
\qquad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}.
\]

## 3. Auxiliary/background-field regularity

Every background field or tensor entering the physical fluctuation operator
must be regular in a regular frame.

This criterion was violated by the vector benchmark in a subtle way:
one null auxiliary combination behaved as \(r^{-2}\) while all its simple
polynomial scalar invariants vanished.

Therefore scalar-invariant regularity alone is insufficient.

## 4. Principal-symbol regularity

For every physical propagating sector \(I\), let

\[
P_I(x,k)
\]

be the principal symbol after all nondynamical fields and constraints have
been consistently eliminated.

Require:

\[
\boxed{
P_I
\text{ finite on the entire physical solution}
}
\]

and that its characteristic polynomial define a well-posed causal problem.

In a second-order single-mode sector this reduces to an effective inverse
metric

\[
\mathcal G_I^{\mu\nu}k_\mu k_\nu=0.
\]

A regular background is not acceptable if \(\mathcal G_I^{\mu\nu}\) becomes
singular or develops a hidden curvature singularity.

## 5. No-ghost criterion

After constraint reduction, the physical kinetic matrix must have positive
eigenvalues with respect to the chosen physical time orientation.

Schematically,

\[
S^{(2)}
=
\frac12
\int
\left[
\dot q^T K \dot q
-
(\nabla q)^T G(\nabla q)
+\cdots
\right],
\]

with

\[
\boxed{
K>0
}
\]

on all physical modes.

A vanishing quadratic kinetic eigenvalue is not automatically safe: it can
signal either a true auxiliary constraint or strong coupling.

## 6. Hyperbolicity / gradient criterion

Physical characteristic speeds must be real and the reduced equations must
admit a well-posed initial-value problem.

At the simplest level,

\[
\boxed{
c_I^2>0
}
\]

for all physical modes.

More generally, the principal polynomial must possess the appropriate
hyperbolicity cone.

## 7. Strong-coupling criterion

A candidate fails as a perturbative effective theory if a physical mode loses
its quadratic operator while nonlinear interactions remain at the same
background.

The vector benchmark illustrated the diagnostic:

\[
S_{\rm vector}^{(2)}=0,
\]

while cubic self-interactions are nonzero.

This can still be consistent if the vector is fully constrained, but only
after an explicit constraint count proves that no physical vector mode
survives.

## 8. Constraint regularity

The algebraic or differential constraint matrix used to eliminate
nondynamical fields should not become singular on relevant regions of the
solution unless a separate gauge symmetry or phase transition accounts for
the rank change.

For an auxiliary system

\[
C_{ab}(r)u_b=J_a,
\]

the limit

\[
\det C\to0
\]

must be treated before solving by \(C^{-1}\).

This matters both at horizons and at regular cores.

## 9. Dynamical formation

A static regular solution is not enough.

The theory should admit evolution from regular initial data in which the
screened region forms dynamically.

The four-dimensional nonpolynomial-gravity program provides an important
benchmark here: related theories have explicitly produced regular black holes
from pressureless-star and thin-shell collapse.

## 10. Inner-horizon criterion

If the solution contains an inner horizon, ordinary mass inflation,
generalized blueshift instabilities, and semiclassical backreaction must be
tested using equations valid for the candidate theory itself.

GR thin-shell arguments cannot automatically be transplanted to
quasitopological gravity: 2026 work shows that standard distributional null
thin shells need not exist in the pure-gravity theories under study.

Thus the status should remain "open" until a direct perturbative or nonlinear
analysis is available.

## 11. Quantum / UV criterion

For a putative UV completion or quantum-gravity-effective theory, background
regularity should not be purchased by extra ghost poles.

A particularly useful target is a propagator schematically of the form

\[
\Pi(k)
\sim
\frac{1}
{k^2\,\mathcal F(k^2/M_*^2)}
\]

where the form factor has no zeros that generate additional physical poles.

The July 2026 nonlocal-quasitopological preprint claims a construction that is
ghost-free and avoids strong-coupling instabilities while retaining exact
regular spherical black holes. This is now a benchmark to reproduce rather
than an assumption.

## 12. Current comparison

### Minimal static canonical scalar \(F(\chi)R\)

- fails the one-function static-radial reconstruction under the assumptions
  tested;
- useful as order-parameter intuition, not as the present action candidate.

### Two-vector auxiliary benchmark

- exact covariant Hayward-type solution;
- regular metric;
- radial linear sector is constrained;
- can make the horizon extremal;
- but contains a singular null auxiliary combination;
- vector quadratic operator degenerates asymptotically;
- radial pure-TT principal cone is Schwarzschild-like.

It is now primarily a **counterexample showing that background regularity is
not enough**.

### Local nonpolynomial pure-gravity QTG

- exact four-dimensional vacuum Hayward solution;
- intrinsic curvature-response saturation;
- no extra background matter/auxiliary field needed for the spherical
  solution;
- second-order spherical equations.

Open issue:

- full nonspherical perturbative health is not guaranteed merely by spherical
  second-order behavior.

### Nonlocal QTG completion

Published status as of September 2026: recent preprint.

Reported properties:

- ghost-free completion;
- avoidance of strong-coupling instabilities;
- exact spherical vacuum regular black holes;
- perturbative Birkhoff theorem.

Primary project task:

\[
\boxed{
\text{independently test the physical principal symbols on the regular BH}
}
\]

rather than accepting flat-space or maximally symmetric stability as
sufficient.

## 13. Updated acceptance condition

A candidate will be considered "principal-safe" only if it satisfies

\[
\boxed{
\begin{aligned}
&\text{background curvature bounded},\\
&\text{physical kinetic matrix healthy},\\
&\text{principal symbols finite and hyperbolic},\\
&\text{constraint rank controlled},\\
&\text{strong-coupling scale nonzero},\\
&\text{regular solution dynamically formable}.
\end{aligned}
}
\]

This is now the project's minimum standard before discussing a
non-geometric completion.


## 14. Covariant-action differentiability

A symmetry-reduced action may remain finite even when the four-dimensional
representative used to generate it is not differentiable on the exact
background.

For any proposed fundamental four-dimensional action require that:

\[
\boxed{
\mathcal L,\qquad
\frac{\partial\mathcal L}{\partial R_{\mu\nu\rho\sigma}},
\qquad
\frac{\partial^2\mathcal L}
{\partial R_{\mu\nu\rho\sigma}\partial R_{\alpha\beta\gamma\delta}}
}
\]

exist and are finite in the directions needed for the physical quadratic
problem, modulo controlled gauge/constraint degeneracies.

A removable \(0/0\) after imposing spherical symmetry is not sufficient,
because nonspherical perturbations probe directions that leave the reduced
submanifold.

The explicit rational lift analyzed in
\`notes/covariant-lift-degeneracy.md\` demonstrates this distinction.


## 15. Curvature-derivative regularity

Finite polynomial curvature invariants are weaker than smooth geometric
regularity.

A candidate with

\[
R,\quad
R_{\mu\nu}R^{\mu\nu},\quad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
\]

finite can still have divergent invariants containing covariant derivatives,
for example

\[
\Box R
\]

or

\[
\nabla_\alpha R_{\mu\nu\rho\sigma}
\nabla^\alpha R^{\mu\nu\rho\sigma}.
\]

The 2026 first-order QTG-TNT black hole gives an explicit example:

\[
a(r)
=
1-\frac{r^2}{2\ell^2}
-\frac{r^3}{4m\ell^2}
+\cdots
\]

has finite polynomial curvature at \(r=0\), but

\[
\Box R\sim\frac{1}{r}.
\]

A candidate intended as a smooth effective spacetime should therefore either:

1. keep the required curvature-derivative invariants finite; or
2. explicitly declare the derivative expansion invalid and replace it by a
   better-defined microscopic/nonlocal description before that point.


## 15. Auxiliary derivative-mixing gate

For a quadratic principal kinetic sector

\[
\mathcal L_{\rm kin}
=
\frac12\dot x^{\rm T}A\dot x
+
\dot x^{\rm T}B\dot y
+
\frac12\dot y^{\rm T}C\dot y,
\]

with a healthy block

\[
A>0,
\]

the reduced kinetic matrix after completing the healthy square is

\[
\boxed{
K_{\rm red}
=
C-B^{\rm T}A^{-1}B.
}
\]

Therefore, if an extra field sector has no direct kinetic term,

\[
C=0,
\]

then

\[
\boxed{
K_{\rm red}
=
-B^{\rm T}A^{-1}B
\le0.
}
\]

Any derivative-active direction that survives the constraint/gauge reduction
inherits negative kinetic sign.

This gives a fast action-selection gate:

1. identify fields with vanishing bare kinetic matrix;
2. compute their derivative mixing \(B\) with healthy physical modes;
3. if \(B\neq0\), require an explicit constraint/gauge proof that every
   active direction is removed;
4. otherwise reject the candidate before relying on background regularity.

The two-vector Hayward benchmark is an explicit example: the null vector
combination is auxiliary, while the derivative-active combination survives
and becomes a direct asymptotic odd ghost.

See
[notes/auxiliary-derivative-mixing-lemma.md](../notes/auxiliary-derivative-mixing-lemma.md).


## 16. Nonlocal operator-mismatch gate

For nonlocal candidates, a zero-free entire form factor is necessary but is
not by itself sufficient on a curved background.

If the physical quadratic operator has the schematic form

\[
\mathcal Q
=
\mathcal D
+
\hat{\mathcal D}^{\dagger}
\mathcal F(\hat{\mathcal D})
\hat{\mathcal D},
\]

then a proof based on

\[
\mathcal Q
=
\mathcal D e^{\Omega(\mathcal D)}
\]

requires the operator identities used in that factorization to hold on the
actual perturbation subspace.

Therefore require:

1. identify \(\mathcal D-\hat{\mathcal D}\);
2. determine whether \(\hat{\mathcal D}\) is self-adjoint on the physical
   subspace;
3. verify zero kernel / acceptable pole structure of the **full** curved-
   background operator, not only the entire form factor;
4. check the horizon/core limits of the resulting pseudodifferential
   principal operator.

This is the next gate for nonlocal QTG.
