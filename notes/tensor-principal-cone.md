# Radial Tensor Principal Cone: a Hidden Schwarzschild Geometry

This note studies the highest-derivative propagation of a local
transverse-traceless metric perturbation on the regular two-vector background.

The result is unexpectedly sharp:

\[
\boxed{
f_{\rm tensor}(r)=1-\frac{2M}{r}
}
\]

for the radial pure-TT principal characteristic.

Thus the background metric is regular, but this tensor characteristic retains
the Schwarzschild radial cone.

This is a **principal-symbol result**, not yet the complete
\(l\ge2\) Regge-Wheeler quadratic action.

## 1. Why a local TT calculation is useful

At wavelengths much shorter than the background curvature scale, propagation
is controlled by the highest-derivative terms in the quadratic action.

Choose a local inertial frame with radial direction \(x\). The two background
vectors are parallel and null:

\[
A_\mu=a\,k_\mu,
\qquad
B_\mu=b\,k_\mu,
\qquad
k_\mu k^\mu=0.
\]

For a radial TT graviton, e.g.

\[
h_{yz}=\psi(t,x)
\]

or the orthogonal plus polarization, the angular vector perturbations are not
sourced at principal order.

Also,

\[
\delta(W^2)=0
\]

for this polarization, so the \(W^2\nabla\cdot W\) and \((W^2)^2\) pieces do
not contribute to the pure-TT principal kinetic operator.

The relevant modification comes from

\[
4\ell^2
G^{\mu\nu}
\left(
A_\mu A_\nu-B_\mu B_\nu
\right).
\]

## 2. Explicit local quadratic expansion

Define

\[
D_{\mu\nu}
=
A_\mu A_\nu-B_\mu B_\nu
=
d\,k_\mu k_\nu.
\]

Expanding

\[
\sqrt{-g}
\left[
R+4\ell^2G^{\mu\nu}D_{\mu\nu}
\right]
\]

to second order in either TT polarization and integrating by parts gives

\[
\boxed{
\mathcal L_{\rm TT}^{(2)}
\doteq
\frac12
\left[
\dot\psi^2
-\psi_x^2
-\zeta
(\dot\psi-\psi_x)^2
\right]
}
\]

where

\[
\zeta\,k^\mu k^\nu
=
4\ell^2D^{\mu\nu}.
\]

The symbol \(\doteq\) means equality up to total derivatives and an overall
positive normalization.

This can be written as propagation on a null Kerr-Schild deformation of the
inverse metric,

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

Because the deformation vector is null, the determinant is unchanged by the
rank-one update. Therefore this isolated principal metric remains Lorentzian
for every finite deformation coefficient.

This is important: the result is not simply a conventional ghost sign flip.

## 3. Exact background vector difference

On the regular branch,

\[
D(r)=r^3+2q\ell^2,
\]

\[
f(r)
=
1-
\frac{2Mr^2}{D(r)}.
\]

The exact ingoing profiles obey

\[
\boxed{
a^2-b^2
=
-\frac{Mq}{rD(r)}
}.
\]

Since

\[
A^\mu\partial_\mu=a\,\partial_r,
\qquad
B^\mu\partial_\mu=b\,\partial_r
\]

in ingoing coordinates, the inverse metric changes only in its \(rr\)
component:

\[
g_{\rm T}^{rr}
=
f(r)
+
4\ell^2(a^2-b^2).
\]

Substituting,

\[
g_{\rm T}^{rr}
=
1-
\frac{2Mr^2}{D}
-
\frac{4Mq\ell^2}{rD}.
\]

The numerator combines exactly:

\[
2Mr^2
+
\frac{4Mq\ell^2}{r}
=
\frac{2M}{r}
\left(
r^3+2q\ell^2
\right).
\]

Therefore

\[
\boxed{
g_{\rm T}^{rr}
=
1-\frac{2M}{r}
}.
\]

## 4. Ingoing characteristic metric

The background inverse \((v,r)\) block is

\[
g^{ab}
=
\begin{pmatrix}
0 & 1\\
1 & f
\end{pmatrix}.
\]

The radial TT principal block becomes

\[
g_{\rm T}^{ab}
=
\begin{pmatrix}
0 & 1\\
1 & 1-2M/r
\end{pmatrix}.
\]

Its inverse is

\[
g^{\rm T}_{ab}
=
\begin{pmatrix}
-(1-2M/r) & 1\\
1 & 0
\end{pmatrix}.
\]

So the corresponding radial line element is formally

\[
\boxed{
ds_{\rm T}^2
=
-\left(1-\frac{2M}{r}\right)dv^2
+
2\,dv\,dr
+
r^2d\Omega^2
}
\]

if the local principal metric extends to the complete radial tensor
characteristic.

This is precisely Schwarzschild in ingoing coordinates.

## 5. Characteristic horizon versus background horizon

The tensor characteristic zero is

\[
\boxed{
r_{\rm T}=2M
}.
\]

By contrast, any regular-background horizon satisfies

\[
r_h^3+2q\ell^2
=
2Mr_h^2.
\]

Hence

\[
2M
=
r_h
+
\frac{2q\ell^2}{r_h^2}.
\]

For

\[
q>0,
\]

this implies

\[
\boxed{
r_h<2M.
}
\]

Therefore the candidate tensor characteristic horizon lies outside every
regular metric horizon in this branch.

For the fully extremal background,

\[
r_h=\frac{4M}{3},
\]

so

\[
\boxed{
r_{\rm T}-r_h
=
\frac{2M}{3}.
}
\]

At \(r=2M\), the regular background itself is not on a horizon:

\[
\boxed{
f(2M)
=
\frac{q\ell^2}{4M^3+q\ell^2}
>0.
}
\]

For the fully extremal value

\[
q\ell^2=\frac{16M^3}{27},
\]

this becomes

\[
f(2M)=\frac{4}{31}.
\]

Thus matter/light coupled to the background metric and the radial TT
principal mode can have distinct characteristic horizons.

## 6. The singularity reappears in the characteristic geometry

If the principal metric above is taken as the radial tensor effective metric,
its Kretschmann scalar is Schwarzschild:

\[
\boxed{
K_{\rm T}
=
\frac{48M^2}{r^6}
}.
\]

So although the physical background has

\[
K_{\rm background}(0)<\infty,
\]

the tensor characteristic geometry retains

\[
K_{\rm T}\to\infty.
\]

This does **not** mean that the background spacetime itself becomes singular.

It means that the coefficients governing the high-frequency tensor
propagation may become singular at the core.

For a screening theory this distinction is crucial:

\[
\boxed{
\text{regular background}
\not\Rightarrow
\text{regular perturbation characteristics}.
}
\]

## 7. Relation to the diverging auxiliary backgrounds

The background vector difference is

\[
a^2-b^2
=
-\frac{Mq}{r(r^3+2q\ell^2)}.
\]

Near the center,

\[
a^2-b^2
\sim
-\frac{M}{2\ell^2r}.
\]

Thus the combination entering the tensor principal metric diverges even though
the background metric curvature remains finite.

This makes precise the concern raised by the original paper's observation
that the individual vector-sector stress tensors diverge at the origin and
cancel only in the background sum.

The cancellation that regularizes the background does not automatically
regularize every fluctuation operator.

## 8. What is and is not established

### Established by this calculation

For a local radial pure-TT polarization:

- the two vectors are not sourced at principal order;
- the quadratic principal action is a null Kerr-Schild deformation;
- the radial characteristic function simplifies exactly to
  \(1-2M/r\);
- its characteristic zero is at \(2M\), outside the regular metric horizon.

### Not yet established

We have not yet proven that:

- the complete spherical \(l\ge2\) odd master equation uses exactly this
  effective metric at all frequencies;
- integrating all auxiliary metric/vector variables leaves no additional
  principal branch;
- the even-parity physical tensor mode has the identical global effective
  metric;
- the full coupled initial-value problem is ill posed at the core.

Those require the complete reduced quadratic action.

## 9. Consequence for the research program

This is currently the strongest obstruction found for the vector benchmark.

The theory may resolve the background curvature singularity while leaving a
Schwarzschild-like singularity in the tensor principal structure.

Therefore the benchmark should not be promoted as a successful
"spacetime-screening completion" unless the full perturbation reduction shows
that this apparent hidden characteristic singularity is either:

1. removed by the constraints;
2. physically inaccessible;
3. replaced by a regular principal variable;
4. or otherwise shown not to correspond to a breakdown of evolution.

If none of these occur, the model would be useful mainly as a demonstration
that **background regularity alone is insufficient**.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/tensor_principal_cone.py
\`\`\`

to verify the exact vector-background difference, the null Kerr-Schild radial
principal metric, the Schwarzschild simplification, and the separation between
the background and tensor characteristic horizons.
