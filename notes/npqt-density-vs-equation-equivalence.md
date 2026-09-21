# NPQT Density Equivalence vs Equation Equivalence

**Status:** SYNTHESIS / OPEN GATE.

The aligned scalar-invariant sign obstruction now rules out an important class
of four-dimensional lifts of the exact spherical cubic density.

It does **not** yet rule out every four-dimensional theory with the same
spherical equations of motion.

This distinction is essential.

---

# 1. Pointwise density result already established

For the displayed cubic NPQT density,

\[
\mathcal Z_{(3)}
=
P_{(3)}(R_{abcd})
+
\frac92\frac ND,
\]

the general spherical reduction gives

\[
\left.\frac ND\right|_{\rm sph}=W_2\Theta.
\]

On the aligned pair

\[
(q,+\Theta),
\qquad
(q,-\Theta),
\]

the algebraic scalar Riemann invariants agree, while

\[
W_2\Theta\rightarrow-W_2\Theta.
\]

Therefore the full pointwise spherical cubic density differs by

\[
\boxed{
\Delta\mathcal Z_{(3)}
=
9W_2\Theta.
}
\]

This has also been reproduced directly from the published two-dimensional
spherical density, where

\[
\Delta\mathcal Z_{(3)}^{2d}
=
27\Omega^2\Theta
=
9W_2\Theta.
\]

Thus the sign distinction is not an artifact of one displayed four-dimensional
rational chart.

Key files:

- src/symbolic/npqt_full_cubic_sign_pair_gate.py
- src/symbolic/npqt_reduced_cubic_sign_pair.py
- src/symbolic/npqt_locally_symmetric_product_pair.py

---

# 2. What this excludes

A new four-dimensional density of the form

\[
\mathcal L_{\rm new}
=
\mathcal L_{\rm source}
+
\Delta\mathcal L,
\]

with

\[
\left.\Delta\mathcal L\right|_{\rm spherical}=0
\]

pointwise on every spherical configuration cannot remove the aligned sign
distinction.

Likewise, a single-valued function only of the algebraic scalar Riemann
invariants cannot reproduce the signed target on both aligned branches.

This is the scope of the current conditional no-go.

---

# 3. What this does not exclude

Two Lagrangian densities can generate the same reduced equations without being
pointwise identical.

Locally, a variationally trivial difference is represented by a null
Lagrangian / total divergence.

Therefore the logically weaker target is

\[
\boxed{
\text{same spherical Euler--Lagrange equations}
}
\]

rather than

\[
\boxed{
\text{same spherical Lagrangian density pointwise}.
}
\]

The present sign-pair calculation by itself does not exclude this weaker
equivalence class.

---

# 4. Relation to published inverse-lift constructions

Borissova and Carballo-Rubio construct four-dimensional non-polynomial
gravities by starting from two-dimensional Horndeski theories and lifting
warped-product curvature variables back to covariant curvature invariants.

Their construction makes two facts especially relevant here:

1. a given reduced Horndeski theory admits many inequivalent four-dimensional
   lifts;
2. solving for the warped-product curvature variables in terms of scalar
   invariants generically introduces non-polynomial expressions and
   noninteger powers / algebraic branches.

This is precisely the branch structure isolated by the present
\(\Theta\)-sign calculation.

The existence of a formal inverse lift therefore does not yet establish the
principal-safety requirement

\[
\mathcal L,\quad
\frac{\partial\mathcal L}{\partial R},\quad
\frac{\partial^2\mathcal L}{\partial R\,\partial R}
\]

on an open generic four-dimensional curvature neighborhood.

The current project question is narrower:

\[
\boxed{
\text{Does there exist an inverse lift that is single-valued and }C^2
\text{ on the required open neighborhood?}
}
\]

---

# 5. Curvature-derivative lifts are a separate escape route

Borissova's 2026 classification shows that allowing curvature-derivative
invariants enlarges the lift space further: generic two-dimensional Horndeski
theories can arise from higher-dimensional pure gravities once such invariants
are admitted.

This is an important existence result.

It does not automatically solve the present NLQT-base problem because generic
curvature-derivative actions reopen:

- higher-order principal symbols;
- additional characteristic surfaces;
- strong-coupling / degeneracy questions;
- a more complicated base Hessian/operator entering NLQT.

Moreover, on the locally symmetric aligned product pair used in the sign gate,

\[
\nabla R_{abcd}=0,
\]

so scalar curvature-derivative invariants vanish on both sign branches and do
not themselves recover the missing sign on that test family.

Thus curvature derivatives remain a possible **equation-level lift**, not an
automatic differentiable replacement for the current local base.

---

# 6. Total-derivative loophole: current status

The aligned pair can be realized as

\[
M_2(k_L)\times S^2(k_S),
\]

with constant curvatures

\[
k_L=3q-\Theta,
\qquad
k_S=3q+\Theta.
\]

The spherical radius/dilaton and all local curvature scalars are covariantly
constant on this family.

Consequently any ordinary covariant boundary current built locally from these
fields and their covariant derivatives vanishes on the pair.

This makes a simple integration-by-parts removal of the cubic sign difference
implausible.

However, this observation is **not yet promoted to a theorem** because
variationally trivial generally covariant densities can have global/topological
representatives, and the exact local cohomology class of the reduced
metric--dilaton theory has not been classified here.

Therefore:

\[
\boxed{
\text{pointwise-density escape: strongly constrained}
}
\]

while

\[
\boxed{
\text{equation-equivalent / variationally trivial escape: OPEN}.
}
\]

---

# 7. Tensorial causal data provides a genuine local escape

The scalar-invariant obstruction does not mean the geometry itself lacks the
required sign information.

Ferrando and Sáez show that the Ricci tensor of a spherical spacetime admits a
spacelike two-eigenplane and provide explicit tensor concomitants for its
projector.

On the aligned NPQT stratum,

\[
N^a{}_b
=
\operatorname{diag}(-\Theta,-\Theta,\Theta,\Theta),
\]

the two algebraic branches

\[
\nu=\pm\frac{\sqrt b}{2}
\]

correspond to the two double eigenspaces.

The condition that the selected rank-two projector is spacelike chooses the
signed angular branch.

The repository reproduces

\[
\boxed{
\Theta
=
\frac12\operatorname{tr}(hN)
}
\]

and hence

\[
\boxed{
W_2\Theta
=
\frac{W_2}{2}\operatorname{tr}(hN).
}
\]

This is the cleanest surviving local pure-metric route.

Key file:

- src/symbolic/npqt_spacelike_ricci_projector_gate.py

---

# 8. Generic splitting does not immediately kill the Ricci route

The exact spherical angular double eigenvalue need not remain degenerate
off spherical symmetry.

Let the two Ricci spectral clusters split as

\[
-\Theta\pm a,
\qquad
+\Theta\pm d.
\]

A cubic interpolation polynomial in the traceless-Ricci endomorphism defines
the rank-two projector onto the \(+\Theta\) cluster whenever the two clusters
remain separated.

Its denominator is exactly the product of the four cross-cluster gaps,

\[
\boxed{
\Delta_{\rm gap}
=
(a-d-2\Theta)
(a-d+2\Theta)
(a+d-2\Theta)
(a+d+2\Theta).
}
\]

The projector remains analytic for

\[
\Delta_{\rm gap}\neq0,
\]

and satisfies

\[
\boxed{
\frac12\operatorname{tr}(hN)=\Theta
}
\]

for the split family, including after an explicit Lorentz-frame mixing.

Thus:

\[
\boxed{
\text{generic eigenvalue splitting is not itself a local obstruction.}
}
\]

The obstruction moves to cluster-collision strata, especially the
Ricci-isotropic region.

Key file:

- src/symbolic/npqt_ricci_cluster_local_extension.py

---

# 9. Current decision tree

The pure-curvature NPQT-base problem now has three logically distinct routes.

## Route A — scalar-invariant root lift

Current status: strongly disfavored.

- SPI-only single-valued algebraic lift: conditional FAIL.
- principal absolute-root prescription: FAIL at \(C^1\).
- other multivalued/root branches: locally possible, but require explicit
  branch data and a \(C^2\) gate.

## Route B — tensorial causal-projector lift

Current status: **leading local constructive route**.

Known passes:

- exact spherical sign recovered;
- causal spacelike plane chooses the correct branch;
- generic local cluster splitting is analytic while the spectral gap remains
  open.

Open:

- one globally single-valued four-dimensional formula;
- Ricci cluster collisions;
- matching to the Weyl principal-plane chart;
- the maximally symmetric core;
- \(C^2\) curvature Hessian.

## Route C — equation-equivalent / curvature-derivative lift

Current status: existence plausible/published at the reduced-theory level,
principal safety OPEN.

This route should be used only if Route B cannot be made \(C^2\), because
curvature derivatives enlarge the generic principal operator substantially.

---

# 10. Next exact calculation

Do not compute the full 4D Hessian yet.

The next useful gate is:

\[
\boxed{
\text{Can the Ricci causal-projector chart and Weyl principal-plane chart be
patched over the full non-core spherical locus?}
}
\]

The spherical locus naturally has two complementary regions:

\[
\Theta\neq0
\quad\Rightarrow\quad
\text{Ricci spectral-cluster chart},
\]

\[
W\neq0
\quad\Rightarrow\quad
\text{Weyl principal-plane chart}.
\]

They overlap when both are nonzero and both select the same angular
two-plane.

The only unavoidable common degeneracy on the exact spherical locus is

\[
W=0,\qquad Z=0,
\]

the maximally symmetric core.

The next task is therefore to construct a **weighted overlap scalar** rather
than a normalized global projector, and test whether the \(W_2\) prefactor is
sufficient to give a \(C^2\) extension at that common core.

This should be done first in a finite-dimensional algebraic-curvature toy.

---

# 11. References

1. J. Borissova, R. Carballo-Rubio,
   *Regular black holes from pure gravity in four dimensions*,
   Phys. Rev. D **113**, 124004 (2026).

2. J. Borissova,
   *All 2D generalised dilaton theories from d>=4 gravities*,
   Phys. Rev. D **113**, 124088 (2026),
   arXiv:2603.06786.

3. J. J. Ferrando, J. A. Sáez,
   *Labeling spherically symmetric spacetimes with the Ricci tensor*,
   Class. Quantum Grav. **34**, 045002 (2017),
   arXiv:1701.05023.

4. P. Bueno, P. A. Cano, R. A. Hennigar, Á. J. Murcia,
   *Regular black hole formation in four-dimensional non-polynomial
   gravities*,
   Phys. Rev. D **113**, 024019 (2026),
   arXiv:2509.19016.
