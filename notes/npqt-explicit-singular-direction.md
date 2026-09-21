# Explicit Lorentzian Singular Direction of the 4D NPQT Rational Representative

The 2025 four-dimensional non-polynomial QT construction uses a common
rational denominator

\[
\boxed{
D_{\rm NPQT}
=
(WZZ)\,W_2
-
2W_3 Z_2
}
\]

where

\[
W_2
=
W_{ab}{}^{cd}W_{cd}{}^{ab},
\]

\[
W_3
=
W_{ab}{}^{cd}
W_{cd}{}^{ef}
W_{ef}{}^{ab},
\]

\[
Z_2
=
Z_a{}^bZ_b{}^a,
\qquad
Z_3
=
Z_a{}^bZ_b{}^cZ_c{}^a,
\]

and

\[
WZZ
=
W_{ab}{}^{cd}
Z_c{}^a Z_d{}^b.
\]

The displayed cubic representative contains a rational term proportional to

\[
\frac{W_3 Z_3 W_2}{D_{\rm NPQT}}.
\]

The source proves that the representative is well-defined after imposing
spherical symmetry, but explicitly leaves potential singular behavior on
other backgrounds open.

## 1. Actual Lorentzian algebraic curvature family

Take an orthonormal Lorentzian frame and a purely electric Weyl tensor with
electric eigenvalues

\[
(e_1,e_2,e_3),
\qquad
e_3=-e_1-e_2.
\]

Take the mixed traceless Ricci tensor to be diagonal with eigenvalues

\[
(z_0,z_1,z_2,z_3),
\qquad
z_3=-z_0-z_1-z_2.
\]

This defines a legitimate real algebraic Weyl tensor and a legitimate
traceless Ricci tensor at a spacetime point.

For this family,

\[
W_2
=
16(e_1^2+e_1e_2+e_2^2),
\]

\[
W_3
=
48e_1e_2(e_1+e_2),
\]

and the remaining invariants are given explicitly in the reproducibility
script.

## 2. Exact denominator-zero direction

Choose

\[
e_1=1,
\qquad
e_2=5,
\qquad
e_3=-6,
\]

and

\[
z_1=z_2=1,
\]

\[
\boxed{
z_0
=
-1+\frac{8}{\sqrt{61}}.
}
\]

Then

\[
\boxed{
D_{\rm NPQT}=0
}
\]

exactly, while

\[
W_2=496,
\]

\[
W_3=1440,
\]

\[
Z_3=-\frac{384}{61}.
\]

Therefore

\[
\boxed{
W_3Z_3W_2
=
-\frac{274268160}{61}
\neq0.
}
\]

So the displayed cubic rational term is genuinely singular on this real
Lorentzian algebraic curvature configuration.

This is not merely a bad choice of spherical coordinates or a removable
\(0/0\) on the symmetric branch.

## 3. The singular set reaches the maximally symmetric point

Scale the Weyl and traceless-Ricci tensors as

\[
W\rightarrow\epsilon W,
\qquad
Z\rightarrow\epsilon Z.
\]

Then

\[
D_{\rm NPQT}
\rightarrow
\epsilon^5D_{\rm NPQT}
=0,
\]

while

\[
W_3Z_3W_2
\rightarrow
\epsilon^8
W_3Z_3W_2
\neq0
\]

for every \(\epsilon\neq0\).

Hence the denominator-zero set contains a ray that approaches arbitrarily
close to a maximally symmetric curvature point.

The displayed rational formula therefore does not define an open
neighborhood of that point.

Moreover a nearby path whose leading denominator coefficient tends to zero
as

\[
\delta\sim\epsilon^4
\]

has the scaling

\[
\frac{
\epsilon^8
}{
\epsilon^5\delta
}
\sim
\epsilon^{-1}.
\]

So fixed-direction degree counting,

\[
\mathcal Z_{\rm rat}\sim O(\epsilon^3),
\]

is insufficient to establish continuity or a C² extension.

## 4. Consequence for 4D NLQT

The NLQT operator uses the first and second variations of its QT base action.

Therefore the **displayed 2025 NPQT representative** cannot be used as an
immediately well-defined generic 4D NLQT base on the strength of its spherical
regularity alone.

At minimum one needs a different representative in the same spherical
equivalence class for which the rational singular set is removed.

This result does **not** prove that every four-dimensional NPQT completion is
singular.  The source itself emphasizes the large degeneracy of covariant
actions sharing the same spherical reduction.

The result is narrower:

\[
\boxed{
\text{the displayed common-denominator representative has a genuine
off-spherical singular curvature direction.}
}
\]

## 5. Literature relation

Bueno, Cano, Hennigar and Murcia explicitly state that their representative
actions contain denominators that may vanish and that their possible
singular behavior away from spherical symmetry is an open problem.  They also
stress that many covariant theories can share the same spherical reduced
action.

The calculation here provides an explicit Lorentzian algebraic-curvature
realization of that concern for the displayed denominator.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/npqt_explicit_singular_direction.py
\`\`\`.


## 6. Full cubic-density source check

The source equation for the displayed cubic NPQT density is

\[
\mathcal Z_{(3)}
=
\text{polynomial cubic curvature contractions}
+
\frac92
\frac{
W_3 Z_3 W_2
}{
(WZZ)W_2-2W_3Z_2
}.
\]

There is no second rational term in \(\mathcal Z_{(3)}\) with which this pole
could cancel.  All other cubic terms are ordinary polynomial contractions and
remain finite on a finite algebraic curvature tensor.

The repository has now also reconstructed the Weyl tensor explicitly in a
Lorentzian orthonormal frame and recomputed

\[
W_2,\quad W_3,\quad Z_2,\quad Z_3,\quad WZZ
\]

by direct index contraction.

This independent tensor-level check gives the same values,

\[
W_2=496,\qquad
W_3=1440,
\]

\[
Z_3=-\frac{384}{61},
\]

\[
D_{\rm NPQT}=0,
\]

and

\[
W_3Z_3W_2
=
-\frac{274268160}{61}.
\]

Thus the pole is a property of the full displayed cubic density, not an
artifact of the shorthand invariant formulas.

See

\`src/symbolic/npqt_explicit_pole_tensor_check.py\`.
