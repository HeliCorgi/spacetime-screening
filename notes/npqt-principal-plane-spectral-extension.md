# NPQT Principal-Plane Spectral Extension Toy

**Status:** NEW CALCULATION CANDIDATE. Priority is not claimed.

The continuity gate in
`notes/npqt-petrov-regulator-continuity-gate.md` identifies the exact
spherical value of the displayed cubic rational term as

\[
\left.\frac ND\right|_{\rm sph}=W_2\Theta,
\]

where \(\Theta\) is the repeated angular eigenvalue of the traceless Ricci
tensor.

This note asks the next local question:

\[
\boxed{
\text{can the spherical angular Weyl two-plane be continued smoothly through
a type-D}\to\text{type-I splitting?}
}
\]

In the real purely-electric sector, away from the conformally-flat core, the
answer is locally **yes**.

## 1. Spectral projector

Let \(E\) be a real symmetric tracefree \(3\times3\) electric Weyl matrix and
let \(\lambda_s\) be an isolated simple eigenvalue.

Define

\[
I_2=\operatorname{tr}(E^2).
\]

For a tracefree cubic characteristic polynomial, the rank-one spectral
projector onto the simple eigendirection can be written as

\[
\boxed{
P_s
=
\frac{
E^2+\lambda_s E+
\left(\lambda_s^2-\frac12I_2\right)I
}{
3\lambda_s^2-\frac12I_2
}.
}
\]

The denominator is the derivative of the characteristic polynomial evaluated
at the simple root,

\[
p'(\lambda_s)
=
3\lambda_s^2-\frac12I_2.
\]

Hence \(P_s\) is smooth wherever the simple root remains separated from the
other two eigenvalues.

The complementary projector

\[
\boxed{
h=I-P_s
}
\]

is a rank-two projector onto the spectral cluster which becomes the repeated
type-D spatial plane.

## 2. Explicit type-D to type-I split

Take eigenvalues

\[
(-2q,\ q+\delta,\ q-\delta)
\]

and allow an arbitrary spatial rotation \(R(\phi)\).

Then

\[
E
=
R
\operatorname{diag}(-2q,q+\delta,q-\delta)
R^{\rm T}.
\]

The isolated branch is

\[
\lambda_s=-2q.
\]

One finds

\[
I_2=6q^2+2\delta^2,
\]

and therefore

\[
\boxed{
p'(\lambda_s)=9q^2-\delta^2.
}
\]

At the type-D point \(\delta=0\),

\[
p'(\lambda_s)=9q^2.
\]

Thus for \(q\neq0\), the spectral projector is nonsingular through the
type-D/type-I splitting.

The symbolic script verifies exactly that

\[
P_s
=
R\operatorname{diag}(1,0,0)R^{\rm T},
\]

and

\[
h
=
R\operatorname{diag}(0,1,1)R^{\rm T}.
\]

## 3. Smooth extension of the angular Ricci mode

Let the spatial traceless-Ricci block in the same rotated frame be

\[
Z_{\rm sp}
=
R
\operatorname{diag}
(z_r,\Theta+\delta_Z,\Theta-\delta_Z)
R^{\rm T}.
\]

Define

\[
\boxed{
\Theta_{\rm ext}
=
\frac12\operatorname{tr}(h Z_{\rm sp}).
}
\]

The projector calculation gives identically

\[
\boxed{
\Theta_{\rm ext}=\Theta,
}
\]

independent of

- the rotation angle;
- the Weyl eigenvalue splitting \(\delta\);
- the traceless Ricci anisotropy \(\delta_Z\) inside the two-plane.

In the repository's purely-electric normalization,

\[
W_2
=
8\operatorname{tr}(E^2)
=
48q^2+16\delta^2.
\]

Hence

\[
\boxed{
T_{\rm ext}
=
W_2\Theta_{\rm ext}
=
(48q^2+16\delta^2)\Theta.
}
\]

At the type-D point,

\[
\boxed{
T_{\rm ext}\to48q^2\Theta,
}
\]

which is precisely the spherical target obtained in the continuity gate.

Unlike the old Petrov regulator, a small type-I Weyl splitting does not force
the continuation to zero.

## 4. Interpretation

This result removes one possible concern:

\[
\boxed{
\text{the type-D eigenvalue splitting is not itself a local obstruction}
}
\]

at a non-conformally-flat spherical point.

The reason is simple. The repeated eigenvalue may split, but the
**two-dimensional spectral cluster** remains separated from the isolated
simple eigenvalue. The cluster projector is therefore smooth in a
sufficiently small neighborhood.

This is the correct local object to continue, not either one of the two
individual eigenvectors inside the cluster.

## 5. Relation to intrinsic type-D geometry

The differential-geometry literature gives an intrinsic Weyl principal
\(2+2\) structure for type-D spacetimes, and explicit Riemann/Weyl
concomitants can recover the corresponding projectors on non-conformally-flat
warped and spherically symmetric geometries.

Useful references are:

- J. J. Ferrando and J. A. Sáez,
  *An intrinsic characterization of 2+2 warped spacetimes*,
  Class. Quantum Grav. **27**, 205023 (2010), arXiv:1005.1491.
- J. J. Ferrando and J. A. Sáez,
  *An intrinsic characterization of spherically symmetric spacetimes*,
  Class. Quantum Grav. **27**, 205024 (2010), arXiv:1005.1780.

Those results support the use of a Weyl-principal-plane concomitant on the
exact type-D/spherical stratum.

The unresolved issue here is different: constructing one expression suitable
for the **action on an open generic 4D curvature neighborhood**.

## 6. Remaining gates

This toy is not yet a 4D NPQT representative.

It does not solve:

1. magnetic Weyl curvature and the full self-dual Weyl operator;
2. global branch selection when no fixed isolated eigenvalue cluster exists;
3. Petrov II/III/N directions;
4. degenerate/null Weyl directions for which scalar polynomial invariants may
   fail to separate nonzero curvature;
5. a single-valued \(C^2\) extension on an open neighborhood of the
   maximally symmetric core \(W=0\);
6. insertion into the complete cubic NPQT density;
7. the resulting full curvature Hessian and NLQT operator.

In particular, the spectral gap closes at the core. Multiplication by
\(W_2\) makes the target cubic in the common curvature scaling, which is
promising for second differentiability at the exact origin, but it does not by
itself prove continuity across branch-switching surfaces arbitrarily near the
origin.

That is now the main mathematical gate.

## Reproducibility

Run

    python src/symbolic/npqt_principal_plane_spectral_toy.py

The script verifies:

- the closed-form spectral projector;
- the exact rank-one/rank-two projector identities;
- the gap factor \(9q^2-\delta^2\);
- \(\Theta_{\rm ext}=\Theta\);
- recovery of the spherical target \(48q^2\Theta\).
