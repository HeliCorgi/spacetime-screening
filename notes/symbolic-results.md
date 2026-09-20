# Symbolic Results: Schwarzschild vs. Hayward

Generated and checked with \`src/symbolic/black_holes.py\`.

Metric ansatz:

\[
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2.
\]

For any \(f(r)\) in this ansatz,

\[
R=
-f''-\frac{4f'}r+\frac{2(1-f)}{r^2},
\]

\[
R_{\mu\nu}R^{\mu\nu}
=
2\left(\frac{f''}{2}+\frac{f'}r\right)^2
+
2\left(\frac{f'}r+\frac{f-1}{r^2}\right)^2,
\]

and

\[
K\equiv
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
=
(f'')^2
+
4\left(\frac{f'}r\right)^2
+
4\left(\frac{1-f}{r^2}\right)^2.
\]

## Schwarzschild

With

\[
f_S(r)=1-\frac{2GM}{r},
\]

the symbolic calculation gives

\[
R=0,
\qquad
R_{\mu\nu}R^{\mu\nu}=0,
\]

\[
\boxed{
K_S=\frac{48G^2M^2}{r^6}
}.
\]

Hence the classical curvature diverges at \(r=0\).

## Hayward

Use

\[
f_H(r)
=
1-
\frac{2GMr^2}{r^3+2GM\ell^2}.
\]

The Ricci scalar is

\[
\boxed{
R_H
=
\frac{
24G^2M^2\ell^2
\left(4GM\ell^2-r^3\right)
}{
\left(r^3+2GM\ell^2\right)^3
}
}.
\]

The Ricci-tensor square is

\[
\boxed{
R_{\mu\nu}R^{\mu\nu}
=
\frac{
288G^4M^4\ell^4
\left(
8G^2M^2\ell^4
-4GM\ell^2r^3
+5r^6
\right)
}{
\left(r^3+2GM\ell^2\right)^6
}
}.
\]

The Kretschmann scalar is

\[
\boxed{
K_H
=
\frac{
48G^2M^2
\left(
32G^4M^4\ell^8
-16G^3M^3\ell^6r^3
+72G^2M^2\ell^4r^6
-8GM\ell^2r^9
+r^{12}
\right)
}{
\left(r^3+2GM\ell^2\right)^6
}
}.
\]

## Center limits

As \(r\to0\),

\[
f_H(r)
=
1-\frac{r^2}{\ell^2}
+\frac{r^5}{2GM\ell^4}
+O(r^8).
\]

Therefore

\[
\boxed{
R_H(0)=\frac{12}{\ell^2}
},
\]

\[
\boxed{
\left.R_{\mu\nu}R^{\mu\nu}\right|_{r=0}
=
\frac{36}{\ell^4}
},
\]

\[
\boxed{
K_H(0)=\frac{24}{\ell^4}
}.
\]

The center is therefore finite-curvature and de Sitter-like rather than singular.

## Asymptotic limit

For \(r\to\infty\),

\[
R_H\to0,
\qquad
R_{\mu\nu}R^{\mu\nu}\to0,
\]

and

\[
K_H
\sim
\frac{48G^2M^2}{r^6},
\]

so the Schwarzschild curvature is recovered asymptotically.

## Horizons

The horizon equation \(f_H(r_h)=0\) is

\[
\boxed{
r_h^3-2GM r_h^2+2GM\ell^2=0
}.
\]

Solving instead for the mass,

\[
\boxed{
M(r_h)
=
\frac{r_h^3}
{2G(r_h^2-\ell^2)}
}.
\]

The extremal configuration follows from the minimum of \(M(r_h)\):

\[
\boxed{
r_{\rm ext}=\sqrt3\,\ell
},
\]

\[
\boxed{
M_{\rm ext}
=
\frac{3\sqrt3}{4}\frac{\ell}{G}
}.
\]

Thus:

- \(M>M_{\rm ext}\): two positive horizons;
- \(M=M_{\rm ext}\): degenerate horizon;
- \(M<M_{\rm ext}\): no black-hole horizon in this static model.

## Surface gravity and Hawking temperature

After eliminating \(M\) using the horizon condition,

\[
f'_H(r_h)
=
\frac{r_h^2-3\ell^2}{r_h^3}.
\]

For the outer horizon,

\[
\boxed{
\kappa_+
=
\frac{r_h^2-3\ell^2}{2r_h^3}
},
\]

and in units \(\hbar=c=k_B=1\),

\[
\boxed{
T_H
=
\frac{r_h^2-3\ell^2}{4\pi r_h^3}
}.
\]

At extremality,

\[
T_H(\sqrt3\,\ell)=0.
\]

Differentiating with respect to \(r_h\),

\[
\frac{dT_H}{dr_h}
=
\frac{(3\ell-r_h)(3\ell+r_h)}
{4\pi r_h^4},
\]

so the temperature reaches its maximum at

\[
\boxed{
r_h=3\ell
}
\]

with

\[
\boxed{
T_{\max}
=
\frac{1}{18\pi\ell}
}.
\]

Therefore, along the outer-horizon branch as the black hole shrinks from large mass, the temperature first rises, reaches a finite maximum, and then falls to zero at the extremal configuration.

## Interpretation

This benchmark realizes the qualitative screening picture in a precise geometric sense:

\[
K_{\rm Schwarzschild}\to\infty
\]

is replaced by

\[
K_{\rm Hayward}\to\frac{24}{\ell^4}.
\]

However, this calculation proves only regularity and thermodynamic identities for the chosen metric. It does **not** prove dynamical formation, inner-horizon stability, ghost freedom, or a fundamental quantum-gravity completion.
