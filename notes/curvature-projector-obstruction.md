# Curvature-Projector Obstruction at Symmetry-Enhanced Cores

The explicit nonpolynomial four-dimensional lifts reconstruct the variables of a
\(2+2\) warped-product geometry from scalar curvature invariants.  The
degeneracies found in \(\mathcal P,\mathcal K,\mathcal H\) are manifestations
of a more general kinematical problem.

At a de Sitter or maximally symmetric core, curvature no longer contains a
preferred radial-versus-angular splitting.

## 1. Spectral-projector model

Suppose a curvature endomorphism has two doubly-degenerate eigenvalues,

\[
\lambda_B
\]

on the two-dimensional base and

\[
\lambda_S
\]

on the two-sphere.

The spectral projectors are formally

\[
P_B
=
\frac{
\mathsf A-\lambda_S\mathbb 1
}{
\lambda_B-\lambda_S
},
\]

and

\[
P_S
=
\frac{
\mathsf A-\lambda_B\mathbb 1
}{
\lambda_S-\lambda_B
}.
\]

As long as

\[
\lambda_B\neq\lambda_S,
\]

these reconstruct the geometric splitting.

## 2. Enhanced symmetry closes the eigenvalue gap

At a maximally symmetric point,

\[
\lambda_B=\lambda_S.
\]

Then the denominators vanish.

Along a specially correlated path the *value* of a projector may have a finite
limit, but a generic perturbation of the curvature operator is amplified by

\[
\boxed{
\delta P
\sim
\frac{
\delta\mathsf A
}{
\lambda_B-\lambda_S
}.
}
\]

Hence

\[
\left\|\delta P\right\|
\to\infty
\]

as the eigenvalue gap closes.

This is the spectral-projector version of the removable-value / divergent-
gradient behavior observed explicitly in the rational QTG lift.

## 3. Why de Sitter cores are especially problematic for projector lifts

A de Sitter core satisfies

\[
R_{\mu\nu}
=
\Lambda g_{\mu\nu}
\]

and

\[
C_{\mu\nu\rho\sigma}=0.
\]

Therefore:

- the traceless Ricci tensor vanishes;
- the Weyl tensor vanishes;
- curvature eigenvalues become degenerate;
- local curvature tensors do not distinguish a preferred \(2+2\) splitting.

But the spherical reduced variable

\[
\psi=\frac{1-f}{r^2}
\]

implicitly knows which directions are the sphere and which are the base.

A local covariant formula that tries to reconstruct \(\psi\) by first
reconstructing that directional split must therefore become ambiguous or
nondifferentiable when the symmetry is enhanced.

## 4. This is not a no-go theorem for covariant regular gravity

A smooth covariant action does not need to reconstruct the spherical projector
at all.

For example, an action built from analytic symmetric contractions such as an
infinite tower

\[
R,
\quad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma},
\quad
R^3,
\quad
\ldots
\]

can remain well-defined when curvature eigenvalues coincide.

The obstruction applies specifically to constructions that recover reduced
directional variables by dividing by curvature eigenvalue gaps or by using
equivalent invariant ratios.

## 5. Design rule

The v2/v3 action should therefore satisfy

\[
\boxed{
\text{no explicit curvature spectral projector is required to define the action}.
}
\]

In particular, avoid fundamental densities whose regularity depends on ratios
such as

\[
\frac{I_{C^3}}{I_{C^2}}
\]

or

\[
\frac{
\text{invariant vanishing with an eigenvalue gap}
}{
\text{another invariant vanishing with the same gap}
}
\]

unless differentiability through the degeneracy is proven at the level of the
complete action.

## 6. Consequence for candidate selection

This favors, as full four-dimensional candidates:

1. polynomial or convergent infinite towers of curvature invariants;
2. nonlocal entire-function operators acting on covariant tensors;
3. other formulations whose fundamental variables remain regular when the
   metric approaches de Sitter.

It disfavors using a rational curvature-projector lift as the fundamental
definition of the theory, even if its spherical reduction is exact.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/curvature_projector_obstruction.py
\`\`\`

to verify the spectral-projector divergence when the curvature eigenvalue gap
closes.
