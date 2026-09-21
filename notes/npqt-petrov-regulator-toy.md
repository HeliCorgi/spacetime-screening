# Petrov-Discriminant Regulator: A Possible Alternative NPQT Representative

The explicit pole of the displayed 2025 NPQT representative does **not** prove
that every covariant representative with the same spherical reduction is
singular.

This note tests one concrete repair mechanism.

## 1. Freedom away from spherical symmetry

The source literature emphasizes that many inequivalent four-dimensional
covariant actions can possess the same two-dimensional spherical reduction.

Therefore one may modify a rational density by terms which vanish identically
on the spherical sector.

The goal is to remove off-spherical denominator zeros without changing the
spherical field equations.

## 2. Petrov speciality as a spherical-vanishing invariant

A static spherically symmetric four-dimensional metric has algebraically
special Weyl curvature of Petrov type D (or type O at conformally-flat
points).

The standard speciality condition is

\[
I^3-27J^2=0.
\]

In the purely-electric Weyl normalization used by the repository's explicit
algebraic-curvature calculation, a real polynomial representative is

\[
\boxed{
\Delta_W
=
W_2^3-12W_3^2.
}
\]

For electric Weyl eigenvalues

\[
(e_1,e_2,e_3),
\qquad
e_1+e_2+e_3=0,
\]

one obtains

\[
\boxed{
\Delta_W
=
1024
(e_1-e_2)^2
(e_2-e_3)^2
(e_3-e_1)^2.
}
\]

Thus \(\Delta_W=0\) whenever the Weyl eigenvalues have the type-D
degeneracy.

The explicit singular direction previously found,

\[
(e_1,e_2,e_3)=(1,5,-6),
\]

is type I and has

\[
\Delta_W=97140736\neq0.
\]

## 3. Toy regulated representative

Let

\[
D=(WZZ)W_2-2W_3Z_2,
\]

and

\[
N=W_3Z_3W_2.
\]

The displayed cubic representative contains \(N/D\).

Consider instead

\[
\boxed{
\mathcal R_\mu
=
\frac{
ND
}{
D^2+\mu\,\Delta_W Z_2^2
},
\qquad
\mu>0.
}
\]

All terms in the denominator have curvature degree ten, while \(ND\) has
degree thirteen, so the modified density remains homogeneous of degree three.

On the type-D spherical locus,

\[
\Delta_W=0,
\]

and wherever \(D\neq0\),

\[
\boxed{
\mathcal R_\mu=\frac ND.
}
\]

Hence the spherical reduction is unchanged there.

At the explicit off-spherical singular direction,

\[
D=0,\qquad
N\neq0,\qquad
\Delta_W\neq0,\qquad
Z_2\neq0,
\]

the modified density instead gives

\[
\boxed{
\mathcal R_\mu=0.
}
\]

So that specific pole is removed.

## 4. Why this is not yet a solution

This construction is only an algebraic proof of concept.

It does **not** establish a globally regular covariant representative.

Remaining problems include:

1. simultaneous zeros
   \[
   D=\Delta_W=0;
   \]
2. type-II/D algebraically special but nonspherical configurations;
3. Weyl tensors with nonzero magnetic part, for which the full complex
   speciality discriminant must be used;
4. points with \(Z_2=0\);
5. C² extendibility at the maximally symmetric core;
6. whether the modified full density still has the required second-order
   spherical equations after all terms and normalization conventions are
   restored.

The important result is narrower:

\[
\boxed{
\text{off-spherical representative freedom can remove at least the explicit
type-I pole without changing the spherical ratio.}
}
\]

This keeps the search for a better 4D NPQT base alive.

## 5. Next algebraic problem

The representative-design problem can be formulated as follows.

Find spherical-vanishing polynomial invariants \(S_i\) such that a modified
denominator

\[
D_{\rm reg}
=
D^{2m}
+
\sum_i S_i^2
\]

has no real Lorentzian zero away from the intended spherical limiting set,
while the corresponding numerator is chosen so that the ratio agrees with
\(N/D\) on every spherical configuration.

This is an algebraic-geometric separation problem between:

- the spherical curvature variety;
- the unwanted denominator-zero variety.

The Petrov discriminant provides the first separating invariant for the
explicit type-I pole found in this repository.

## References

The Weyl speciality condition \(I^3=27J^2\) characterizes algebraically
special Weyl tensors; spherical black-hole geometries are Petrov type D.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/npqt_petrov_regulator_toy.py
\`\`\`.
