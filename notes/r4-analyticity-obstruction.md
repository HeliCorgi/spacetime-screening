# Structural Analyticity Obstruction for First-Order 4D QTG-TNT

This note records a structural result from

A. Colléaux, I. Kolář, T. Málek,
*Quasi-topological gravity for 4-dimensional Taub-NUT, near-horizon extreme Kerr, and swirling symmetries*,
arXiv:2606.17784 (2026).

It explains why the \(R_4\) cusp found in
\`notes/r4-differentiability.md\` is not merely an unfortunate choice of one
covariant representative.

## 1. The first-order Class-I mechanism

The unique new QTG-TNT sector with GR-like algebraic integrability is

\[
I_1^{(I)}
=
\int d^4x\sqrt{-g}\,
A_1(R_3)R_4.
\]

Its reduced static spherical equation is algebraic after the trivial
integration, which is exactly the attractive feature of the model.

## 2. Analytic curvature scalars are even in \(R_4\)

The 2026 classification proves that, when restricted to TNT geometries, any
scalar Lagrangian analytic in the Riemann tensor and its dual contains \(R_4\)
only through even powers:

\[
\boxed{
\mathcal L_{\rm analytic}
=
F(R_4^2,\ldots).
}
\]

Therefore,

\[
\boxed{
\left.
\frac{\partial\mathcal L_{\rm analytic}}
{\partial R_4}
\right|_{R_4=0}
=
0.
}
\]

A nonzero linear term

\[
c\,R_4
\]

cannot arise from an analytic curvature scalar in a neighborhood of the
single-function branch.

## 3. Consequence

The first-order Class-I integrability mechanism requires

\[
\boxed{
\text{linear dependence on }R_4.
}
\]

But analytic curvature actions permit only even powers of \(R_4\).

Hence:

\[
\boxed{
\text{first-order nontrivial QTG-TNT}
\Longrightarrow
\text{non-analytic curvature dependence}.
}
\]

This is not a conjecture of this repository; it is a classification result of
the 2026 paper.

## 4. Relation to the explicit square-root representative

The displayed covariant scalar is

\[
R_4
=
\sqrt{
\frac{2I_6}{3}
-
\frac{2I_{11}}{I_1}
}.
\]

On the single-function branch \(R_4=0\), and the repository finds

\[
\frac{\partial R_4}{\partial I_6}
=
\frac{1}{3R_4},
\]

\[
\frac{\partial^2R_4}{\partial I_6^2}
=
-\frac{1}{9R_4^3}.
\]

The structural classification therefore explains why one should not expect
the linear-\(R_4\) first-order theory to admit a completely smooth analytic
Riemann-only representative.

## 5. What must be sacrificed to regain analyticity

The same classification shows that analytic non-topological QTG-TNT theories
belong to Class II and have third-order reduced field equations, i.e. second
order after one trivial integration.

Thus a smooth analytic four-dimensional theory must give up the exact
GR-like first-order/algebraic integrability of Class I.

The design tradeoff is:

\[
\boxed{
\begin{array}{c}
\text{GR-like first-order integrability}\\
\Updownarrow\\
\text{non-analytic linear }R_4
\end{array}
}
\]

versus

\[
\boxed{
\begin{array}{c}
\text{analytic/polynomial 4D action}\\
\Updownarrow\\
\text{higher-order reduced equation}
\end{array}
}
\]

within this QTG-TNT classification.

## 6. Project implication

For Spacetime Screening, this candidate is therefore best treated as:

- a valuable symmetry-reduced integrability construction;
- a source of exact regular backgrounds;
- evidence that non-polynomial response functions can enforce limiting
  curvature;

but **not** as the preferred full 4D perturbative completion.

The next serious 4D candidates should prioritize:

1. analytic/polynomial Class-II or generalized-QTG building blocks;
2. nonlocal entire-function completions with regular quadratic operators;
3. formulations with additional regular fields where the signed reduced
   degree of freedom is fundamental rather than reconstructed through a
   square root of curvature invariants.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/r4_analyticity_obstruction.py
\`\`\`

to verify the elementary even-function consequence that analytic TNT
dependence has vanishing linear slope at \(R_4=0\).
