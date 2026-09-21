# Petrov-Discriminant Regulator: A Possible Alternative NPQT Representative

The explicit pole of the displayed 2025 NPQT representative does **not** prove
that every covariant representative with the same spherical reduction is
singular.

This note tests one concrete repair mechanism.

> **Update — 2026-09-22:** the follow-up continuity calculation shows that
> this toy is **not C0** at an intended spherical simultaneous zero
> \(D=\Delta_W=0\).  A spherical path tends to \(48q^2\theta\), while a
> Weyl-splitting path tends to zero.  See
> `notes/npqt-petrov-regulator-continuity-gate.md` and
> `src/symbolic/npqt_petrov_regulator_continuity_gate.py`.
>
> Accordingly, this file is retained only as the pointwise type-I-pole
> proof of concept; it is no longer the mainline representative candidate.

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
3. Weyl tensors with nonzero magnetic part, for which the full com## 5. Updated mainline problem

The denominator-only design problem has now been sharpened.

The follow-up calculation finds that, on a general spherical algebraic
curvature configuration,

\[
\boxed{
\frac ND=W_2\Theta,
}
\]

where \(\Theta\) is the repeated angular eigenvalue of the traceless Ricci
tensor in the spherical decomposition.

Therefore the next construction should seek a smooth 4D covariant extension

\[
\Theta_{\rm ext}
\]

and test

\[
\boxed{
T_{\rm ext}=W_2\Theta_{\rm ext}
}
\]

directly for a genuine \(C^2\) curvature extension.  A simple
Petrov-discriminant denominator lift cannot solve the type-D directional
problem because \(\Delta_W\) vanishes identically on that whole locus.

See:

- `notes/npqt-petrov-regulator-continuity-gate.md`;
- `src/symbolic/npqt_petrov_regulator_continuity_gate.py`.

hat a modified
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
