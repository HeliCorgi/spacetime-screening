# NPQT Petrov-Regulator Continuity Gate

**Status:** NEW CALCULATION CANDIDATE. Priority is not claimed.

This note continues the representative-design problem in
`notes/npqt-petrov-regulator-toy.md`.

The displayed cubic 4D NPQT density contains

\[
\mathcal R_{\rm old}=\frac{N}{D},
\qquad
D=(WZZ)W_2-2W_3Z_2,
\qquad
N=W_3Z_3W_2.
\]

The earlier proof-of-concept replacement was

\[
\mathcal R_\mu=
\frac{ND}{D^2+\mu\Delta_WZ_2^2},
\qquad
\Delta_W=W_2^3-12W_3^2.
\]

It removes the explicit type-I pole found previously.  The stronger question
is whether it is even continuous on the intended spherical simultaneous-zero
set.  It is not.

## 1. Exact spherical target

Work at one point in an orthonormal Lorentzian frame.  For a spherical type-D
purely electric Weyl tensor take

\[
E=\operatorname{diag}(-2q,q,q),
\]

so that

\[
W_2=48q^2,
\qquad
W_3=96q^3.
\]

Allow a general symmetric time-radial traceless-Ricci block,

\[
Z_{ab}=
\begin{pmatrix}
a&b&0&0\\
b&a-2\Theta&0&0\\
0&0&\Theta&0\\
0&0&0&\Theta
\end{pmatrix}_{ab}.
\]

Direct Lorentzian index contraction gives

\[
D=-576q^3(a-b-\Theta)(a+b-\Theta),
\]

\[
N=-27648q^5\Theta(a-b-\Theta)(a+b-\Theta).
\]

Therefore, wherever \(D\neq0\),

\[
\boxed{
\frac ND=W_2\Theta.
}
\]

This includes an off-diagonal time-radial Ricci block.  Thus the rational
piece is, on spherical symmetry, a covariant lift of the repeated angular
traceless-Ricci eigenvalue \(\Theta\).

The representative-design problem is therefore better stated as

\[
\boxed{
\text{construct a smooth 4D covariant extension of }\Theta
}
\]

rather than merely lifting the old denominator.

## 2. Type-D diagonal reduction

Set

\[
(e_1,e_2,e_3)=(-2q,q,q),
\]

and define

\[
A=z_0+z_2,
\qquad
B=z_1+z_2,
\qquad
\theta=z_2.
\]

Then

\[
z_3=\theta-A-B,
\]

and exactly

\[
\boxed{
D=-288q^3(A^2+B^2),
}
\]

\[
\boxed{
N=-13824q^5AB(A+B-2\theta).
}
\]

Spherical Ricci alignment is \(z_2=z_3\), hence \(A+B=0\).  Away from the
simultaneous zero,

\[
\left.\frac ND\right|_{\rm sph}=48q^2\theta.
\]

At \(A=B=0\),

\[
(z_0,z_1,z_2,z_3)=(-\theta,-\theta,\theta,\theta),
\]

while

\[
D=N=\Delta_W=0.
\]

The restricted spherical value nevertheless remains \(48q^2\theta\).

## 3. The old Petrov regulator fails at C0

Along the spherical path

\[
A=\epsilon,
\qquad
B=-\epsilon,
\]

one has

\[
D=-576\epsilon^2q^3,
\qquad
N=-27648\epsilon^2q^5\theta,
\]

so

\[
\lim_{\epsilon\to0}\mathcal R_\mu=48q^2\theta.
\]

Now hold the Ricci tensor fixed at the simultaneous-zero value and split the
repeated Weyl eigenvalues,

\[
e_1=-2q+\epsilon,
\qquad
e_2=q,
\qquad
e_3=q-\epsilon.
\]

Then \(Z_3=0\), so \(N=0\) identically, while

\[
D=128\epsilon^2\theta^2(2q-\epsilon),
\]

\[
\Delta_W=
1024\epsilon^2(3q-2\epsilon)^2(3q-\epsilon)^2.
\]

Hence the punctured path has

\[
\mathcal R_\mu=0.
\]

Therefore

\[
\boxed{
\lim_{\rm sph}\mathcal R_\mu=48q^2\theta,
\qquad
\lim_{\rm Weyl\ split}\mathcal R_\mu=0.
}
\]

For \(q\theta\neq0\), no continuous extension exists.

So the earlier Petrov toy remains only a pointwise demonstration that one
specific type-I pole can be removed.  It is not a regular representative.

## 4. Petrov speciality alone cannot solve the problem

Stay on exact type D and approach \(A=B=0\) along

\[
A=\epsilon,
\qquad
B=k\epsilon.
\]

Then

\[
\boxed{
\lim_{\epsilon\to0}\frac ND
=
-\frac{96k}{1+k^2}q^2\theta.
}
\]

The spherical direction \(k=-1\) gives \(+48q^2\theta\), whereas
\(k=+1\) gives \(-48q^2\theta\).

Because \(\Delta_W\equiv0\) on the entire type-D family, a regulator whose
only detector is Weyl non-speciality leaves this directional obstruction
untouched.

The missing information is Ricci anisotropy inside the repeated Weyl
two-plane.

## 5. Principal-plane decomposition

Let \(h^a{}_b\) be the projector onto the repeated spacelike Weyl two-plane
on this local type-D branch.  Define

\[
\Theta_h=\frac12h^a{}_bZ_a{}^b,
\]

and

\[
J_h=
\left(
h^a{}_cZ^c{}_dh^d{}_b-\Theta_hh^a{}_b
\right)
\left(
h^b{}_eZ^e{}_fh^f{}_a-\Theta_hh^b{}_a
\right).
\]

In the diagonal family,

\[
\Theta_h=-\frac{A+B-2\theta}{2},
\qquad
J_h=\frac12(A+B)^2.
\]

With

\[
T=W_2\Theta_h=-24q^2(A+B-2\theta),
\]

one has \(T=N/D\) on the spherical locus and the exact factorization

\[
\boxed{
N-TD
=
-6912q^5(A+B-2\theta)(A+B)^2.
}
\]

This identifies the correct kind of off-spherical datum that the Petrov
discriminant misses.

## 6. A continuity repair still fails the C2 gate

As a local experiment define

\[
A_{\rm align}=\mu W_2^4J_h,
\]

\[
\mathcal R_{\rm blend}
=
\frac{ND+T A_{\rm align}}{D^2+A_{\rm align}}.
\]

It preserves \(N/D\) on the spherical locus.  In the diagonal type-D family,

\[
\mathcal R_{\rm blend}-T
=
\frac{
24q^2(A+B)^2(A^2+B^2)(A+B-2\theta)
}{
(A^2+B^2)^2+32\mu q^2(A+B)^2
}.
\]

This is continuous at \(A=B=0\).  However, for a straight non-tangent
direction

\[
A=\alpha t,
\qquad
B=\beta t,
\qquad
\alpha+\beta\neq0,
\]

the second directional correction is

\[
\boxed{
\lim_{t\to0}
\frac{2(\mathcal R_{\rm blend}-T)}{t^2}
=
-\frac{3\theta}{\mu}(\alpha^2+\beta^2).
}
\]

On the exact spherical tangent \((\alpha,\beta)=(1,-1)\), the correction
vanishes identically.  Nearby directions approach \(-6\theta/\mu\), while
the tangent value is zero.

A Hessian is a continuous quadratic form of the direction.  Therefore this
simplest alignment blend is not \(C^2\) at the simultaneous zero.

## 7. Revised constructive target

The exact spherical quantity is

\[
\boxed{
T_{\rm sph}=W_2\Theta.
}
\]

The next useful construction is therefore a smooth covariant extension

\[
\Theta_{\rm ext}
=
\frac12 h[W]^a{}_b Z_a{}^b,
\qquad
T_{\rm ext}=W_2\Theta_{\rm ext},
\]

where \(h[W]\) should extend the spherical Weyl principal two-plane.

The hard gates are now explicit:

1. construct \(h[W]\) covariantly, including magnetic Weyl curvature;
2. control branch changes when the type-D eigenvalue cluster splits;
3. handle type II/III/N directions;
4. prove that the \(W_2\) weighting makes the full scalar genuinely \(C^2\)
   at the maximally symmetric core;
5. restore the complete cubic density and verify exact spherical reduction;
6. only then compute the curvature Hessian required by NLQT.

The relevant question is not whether a normalized projector is finite, but
whether the weighted scalar \(W_2\Theta_{\rm ext}\) has a regular second
curvature derivative.

## Status update

The previous toy regulator now has the sharper status

\[
\boxed{
\text{explicit type-I pole removal: PASS}
}
\]

but

\[
\boxed{
C^0\text{ extension on the spherical simultaneous-zero set: FAIL}.
}
\]

## Reproducibility

Run:

    python src/symbolic/npqt_petrov_regulator_continuity_gate.py

The script checks the general-spherical identity, both incompatible path
limits, the exact type-D directional dependence, the principal-plane
factorization, and the C2 failure of the simplest alignment blend.

## Source relation

P. Bueno, P. A. Cano, R. A. Hennigar, Á. J. Murcia,
*Regular black hole formation in four-dimensional non-polynomial gravities*,
Phys. Rev. D **113**, 024019 (2026), arXiv:2509.19016.

That source proves the rational densities are well defined after spherical
reduction and explicitly leaves their behavior on other backgrounds open.
Its spherical decomposition contains precisely the repeated angular
traceless-Ricci coefficient \(\Theta\) isolated above.
