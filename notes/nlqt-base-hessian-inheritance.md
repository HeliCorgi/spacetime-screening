# NLQT Inherits the Differentiability of Its QT Base Action

The nonlocal completion does not remove a pathology already present in the
curvature Hessian of the local QT base action.

## 1. Base tensors

For

\[
\mathcal L_{\rm QT}(g,R_{\mu\nu\rho\sigma}),
\]

define

\[
P^{abcd}
=
\frac{\partial\mathcal L_{\rm QT}}
{\partial R_{abcd}},
\]

and

\[
\hat{\mathcal E}_{ab}
=
P_{acde}R_b{}^{cde}
-\frac12
\mathcal L_{\rm QT}g_{ab}.
\]

The NLQT form factor is constructed from the linearized operator

\[
\delta\hat{\mathcal E}_{ab}
=
\hat{\mathcal D}_{ab}{}^{cd}h_{cd}.
\]

## 2. The base curvature Hessian enters \(\hat{\mathcal D}\)

Define

\[
\mathcal H^{abcd|efgh}
=
\frac{\partial^2\mathcal L_{\rm QT}}
{\partial R_{abcd}\partial R_{efgh}}.
\]

Then

\[
\delta P^{abcd}
=
\mathcal H^{abcd|efgh}
\delta R_{efgh}
+\cdots.
\]

Therefore the principal two-derivative part of
\(\delta\hat{\mathcal E}_{ab}\) contains schematically

\[
\boxed{
\left(
P
+
\bar R\cdot\mathcal H
\right)
\delta R[h].
}
\]

Thus \(\hat{\mathcal D}\) is only as well defined as the first and second
curvature derivatives of the QT base action.

## 3. Consequence for the 4D rational lift

The repository previously found that the displayed rational 4D lift of the
Hayward/QT spherical theory has removable values on the single-function
branch but divergent generic invariant gradients, and its representative
action fails an additional first-variation cancellation condition.

Alternative square-root/Weyl-ratio lifts also become nondifferentiable on
symmetry-enhanced surfaces.

Therefore one cannot simply insert that representative base action into

\[
\mathcal F
=
\frac{e^{\Omega(\hat{\mathcal D})}-I}
{\hat{\mathcal D}}
\]

and expect the entire function to cure the problem.

If \(\hat{\mathcal D}\) is undefined/divergent before \(\mathcal F\) is
applied, the nonlocal completion is not a well-defined perturbative theory on
that background.

## 4. Logical order of the NLQT gates

The correct order is:

1. **base differentiability**
   \[
   \mathcal L_{\rm QT},\quad
   P,\quad
   \mathcal H
   \text{ finite/well defined};
   \]

2. **operator definition**
   \[
   \hat{\mathcal D}
   \text{ finite/well defined};
   \]

3. **operator mismatch**
   \[
   \mathcal D-\hat{\mathcal D};
   \]

4. **nonlocal zero-kernel / kinetic / characteristic test**.

The zero-free entire form factor is a powerful result only after the first two
steps have passed.

## 5. Current 4D verdict

For the particular rational 4D QT lift already analyzed in this repository:

\[
\boxed{
\text{NLQT based on that lift fails before the zero-kernel gate}
}
\]

unless a nontrivial full-tensor cancellation not visible in the invariant
analysis is explicitly demonstrated.

This does not rule out a different, differentiable four-dimensional QT base
completion.

It means such a base action is now the prerequisite for a genuine 4D NLQT
principal-safety test.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/nlqt_base_hessian_inheritance.py
\`\`\`.
