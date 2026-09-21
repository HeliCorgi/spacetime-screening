# Exact Hayward Is Not an Analytic 4D GQTG Asymptotic

If the 4D NLQT program is to use a differentiable, polynomial
order-by-order GQTG base rather than a normalized curvature-projector NPG, the
target regular black hole must also be changed.

## 1. Genuine 4D GQTG begins at cubic order

At quadratic curvature order, the four-dimensional Lovelock/Gauss-Bonnet
combination is topological. The genuine four-dimensional GQTG family starts
at cubic order.

Using the all-order integrated spherical equation, the order-\(n\) genuine
4D GQTG term evaluated on Schwarzschild obeys

\[
F_n
=
(-1)^n
\left[
\frac94n(n-1)
\frac{M^{n-1}}{r^{3n-4}}
+
O(r^{-(3n-3)})
\right].
\]

Since the Einstein integrated equation varies as

\[
\delta F_{\rm EH}
=
-2r\,\delta f,
\]

the induced metric correction scales as

\[
\boxed{
\delta f_n
=
O(r^{-(3n-3)}).
}
\]

For the first genuine term,

\[
n=3,
\]

this gives

\[
\boxed{
\delta f_3
=
O(r^{-6}).
}
\]

## 2. Hayward starts too early

The Hayward metric expands as

\[
f_H
=
1-\frac{2M}{r}
+
\frac{4M^2\ell^2}{r^4}
+O(r^{-7}).
\]

Thus the first correction is

\[
\boxed{
\delta f_H
=
O(r^{-4}).
}
\]

There is no integer \(n\ge3\) for which

\[
3n-3=4.
\]

Therefore a finite analytic 4D GQTG truncation cannot reproduce exact
Hayward asymptotics.

The same remains true for a normally/uniformly convergent tower whose
large-radius expansion can be exchanged with the infinite sum.

## 3. Consequence for 4D NLQT design

The nonlocal correction preserves the chosen QT/GQTG base solutions.

Therefore choosing an analytic GQTG base means the exact inherited regular
black hole should **not** be expected to be Hayward.

The project should instead search for a regular target with:

\[
\boxed{
f(r)
=
1-\frac{2M}{r}
+
O(r^{-6})
}
\]

at infinity, while retaining a smooth finite-curvature core.

This is not a loss of the screening idea. The physically relevant target is

\[
\mathscr S\to0
\]

at high curvature, not one specific phenomenological metric.

## 4. Design implication

A principal-safe 4D NLQT candidate based on analytic GQTG should satisfy:

1. no normalized Weyl/Cotton/spectral projectors;
2. polynomial curvature densities order by order;
3. an infinite-tower regular solution with GQTG-compatible asymptotics;
4. a finite resummed curvature Hessian on the core;
5. the NLQT zero-kernel and kinetic gates on nonspherical perturbations.

This replaces "reproduce Hayward exactly" with "reproduce the screening
mechanism in an analytically compatible 4D theory."

## Reproducibility

Run

\`\`\`bash
python src/symbolic/gqtg_hayward_asymptotic_obstruction.py
\`\`\`.
