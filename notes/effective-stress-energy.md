# Effective Stress-Energy of the Hayward Geometry

This note interprets the Hayward metric through the ordinary Einstein equation

\[
G^\mu{}_\nu=8\pi G\,T^\mu{}_\nu
\]

and asks what effective anisotropic stress-energy tensor would be required.

This is an **effective GR reconstruction**. If the metric instead arises from higher-curvature or quantum gravity, part or all of this effective stress tensor may represent gravitational corrections rather than fundamental matter.

## 1. Metric

Use

\[
ds^2
=
-f(r)dt^2
+
\frac{dr^2}{f(r)}
+
r^2d\Omega^2
\]

with

\[
f(r)
=
1-
\frac{2GMr^2}
{r^3+2GM\ell^2}.
\]

Write

\[
T^\mu{}_\nu
=
\operatorname{diag}
(-\rho,p_r,p_t,p_t).
\]

For this metric ansatz,

\[
G^t{}_t
=
G^r{}_r
=
\frac{rf'(r)+f(r)-1}{r^2},
\]

and

\[
G^\theta{}_\theta
=
G^\phi{}_\phi
=
\frac{f''(r)}2+\frac{f'(r)}r.
\]

## 2. Effective density and pressures

Define

\[
D(r)=r^3+2GM\ell^2.
\]

The symbolic calculation gives

\[
\boxed{
\rho(r)
=
\frac{
3GM^2\ell^2
}{
2\pi D(r)^2
}
}
\]

and

\[
\boxed{
p_r(r)=-\rho(r)
}.
\]

The tangential pressure is

\[
\boxed{
p_t(r)
=
\frac{
3GM^2\ell^2
\left(r^3-GM\ell^2\right)
}{
\pi D(r)^3
}
}.
\]

Thus the radial equation of state is exactly vacuum-like at all radii,

\[
w_r\equiv\frac{p_r}{\rho}=-1.
\]

The tangential equation of state varies with radius.

Introduce

\[
x
=
\frac{r^3}{GM\ell^2}.
\]

Then

\[
\boxed{
\frac{p_t}{\rho}
=
\frac{2(x-1)}{x+2}
}.
\]

Therefore:

\[
x=0:
\qquad
\frac{p_t}{\rho}=-1,
\]

\[
x=1:
\qquad
p_t=0,
\]

\[
x=4:
\qquad
p_t=\rho,
\]

and

\[
x\to\infty:
\qquad
\frac{p_t}{\rho}\to2.
\]

## 3. Center: exact de Sitter equation of state

At \(r=0\),

\[
\boxed{
\rho(0)
=
\frac{3}{8\pi G\ell^2}
}
\]

and

\[
\boxed{
p_r(0)=p_t(0)=-\rho(0)
}.
\]

Thus the core is exactly vacuum-energy-like.

Since de Sitter space satisfies

\[
f(r)=1-\frac{\Lambda r^2}{3},
\]

comparison with the Hayward center,

\[
f(r)=1-\frac{r^2}{\ell^2}+O(r^5),
\]

gives

\[
\boxed{
\Lambda_{\rm eff}=\frac{3}{\ell^2}
}.
\]

Then

\[
\rho_\Lambda
=
\frac{\Lambda_{\rm eff}}{8\pi G}
=
\frac{3}{8\pi G\ell^2},
\]

exactly matching the reconstructed center density.

## 4. Effective mass profile

Define \(m(r)\) by

\[
f(r)=1-\frac{2Gm(r)}r.
\]

For Hayward,

\[
\boxed{
m(r)
=
M\frac{r^3}{r^3+2GM\ell^2}
}.
\]

The symbolic calculation verifies

\[
\boxed{
m'(r)=4\pi r^2\rho(r)
}.
\]

Also,

\[
m(0)=0,
\qquad
m(\infty)=M.
\]

Thus the effective density integrates to the ADM mass:

\[
4\pi\int_0^\infty \rho(r)r^2dr=M.
\]

The density is positive and monotonically decreasing:

\[
\rho(r)>0,
\]

\[
\frac{d\rho}{dr}<0
\qquad(r>0).
\]

## 5. Stress anisotropy

The anisotropy is

\[
\boxed{
p_t-p_r
=
\rho+p_t
=
\frac{
9GM^2\ell^2r^3
}{
2\pi D(r)^3
}
\ge0
}.
\]

It vanishes at the exact center, where the effective fluid is isotropic, and becomes positive away from the core.

## 6. Conservation

The anisotropic-fluid conservation equation is

\[
p_r'
+
(\rho+p_r)\frac{f'}{2f}
+
\frac{2}{r}(p_r-p_t)
=
0.
\]

Since

\[
\rho+p_r=0,
\]

it reduces to

\[
p_r'
+
\frac{2}{r}(p_r-p_t)
=
0.
\]

The symbolic calculation verifies this identity exactly.

Thus the reconstructed source is consistent with

\[
\nabla_\mu T^{\mu\nu}=0.
\]

## 7. Null energy condition

For a Type-I anisotropic source, NEC requires

\[
\rho+p_r\ge0,
\]

\[
\rho+p_t\ge0.
\]

Here,

\[
\boxed{
\rho+p_r=0
}
\]

and

\[
\boxed{
\rho+p_t
=
\frac{
9GM^2\ell^2r^3
}{
2\pi D(r)^3
}
\ge0
}.
\]

Therefore:

\[
\boxed{\text{NEC is satisfied everywhere}}
\]

with the radial NEC saturated.

## 8. Weak energy condition

WEC requires

\[
\rho\ge0
\]

plus NEC.

Since

\[
\rho>0
\]

for finite \(r\), and NEC holds,

\[
\boxed{\text{WEC is satisfied everywhere}}.
\]

This is important: singularity avoidance in the static Hayward geometry does **not** require negative effective energy density.

## 9. Strong energy condition

SEC additionally requires

\[
\rho+p_r+2p_t\ge0.
\]

For Hayward,

\[
\boxed{
\rho+p_r+2p_t
=
\frac{
6GM^2\ell^2
\left(r^3-GM\ell^2\right)
}{
\pi D(r)^3
}
}.
\]

Thus the sign changes at

\[
\boxed{
r_{\rm SEC}
=
(GM\ell^2)^{1/3}
}.
\]

Therefore,

\[
\boxed{
r<r_{\rm SEC}
\quad\Rightarrow\quad
\text{SEC violated}
}
\]

and

\[
r>r_{\rm SEC}
\quad\Rightarrow\quad
\text{SEC satisfied}.
\]

This is exactly the expected behavior of a de Sitter-like repulsive core.

## 10. Dominant energy condition

DEC requires

\[
\rho\ge |p_r|,
\qquad
\rho\ge |p_t|.
\]

The radial condition is saturated because

\[
|p_r|=\rho.
\]

Since \(\rho+p_t\ge0\), the nontrivial tangential bound is

\[
\rho-p_t\ge0.
\]

Symbolically,

\[
\boxed{
\rho-p_t
=
\frac{
3GM^2\ell^2
\left(4GM\ell^2-r^3\right)
}{
2\pi D(r)^3
}
}.
\]

Hence

\[
\boxed{
r_{\rm DEC}
=
(4GM\ell^2)^{1/3}
}
\]

and

\[
\boxed{
0\le r\le r_{\rm DEC}
\quad\Rightarrow\quad
\text{DEC satisfied},
}
\]

while

\[
\boxed{
r>r_{\rm DEC}
\quad\Rightarrow\quad
\text{DEC violated}.
}
\]

The violation occurs because

\[
p_t>\rho
\]

in the outer tail, even though both quantities decay rapidly as \(r^{-6}\).

As \(r\to\infty\),

\[
\rho
\sim
\frac{3GM^2\ell^2}{2\pi r^6},
\]

\[
p_t
\sim
\frac{3GM^2\ell^2}{\pi r^6}
=
2\rho.
\]

## 11. Relation to the outer horizon

For a Hayward horizon \(r_h\),

\[
M(r_h)
=
\frac{r_h^3}
{2G(r_h^2-\ell^2)}.
\]

At the horizon,

\[
\frac{r_h^3}{GM\ell^2}
=
2\left(\frac{r_h^2}{\ell^2}-1\right).
\]

For the outer horizon,

\[
r_h\ge\sqrt3\,\ell.
\]

Therefore,

\[
\frac{r_h^3}{GM\ell^2}\ge4.
\]

So the extremal outer horizon lies exactly at the DEC boundary:

\[
r_{\rm ext}
=
r_{\rm DEC}
=
\sqrt3\,\ell
\]

when

\[
M=M_{\rm ext}.
\]

For every non-extremal Hayward black hole,

\[
r_+>r_{\rm DEC},
\]

so the reconstructed effective source violates DEC at and outside the outer horizon, although its magnitude falls as \(r^{-6}\).

This is a warning against interpreting the effective source as ordinary classical matter.

## 12. Summary

| Condition | Result |
|---|---|
| \(\rho\ge0\) | satisfied everywhere |
| radial NEC \(\rho+p_r\ge0\) | saturated everywhere |
| tangential NEC \(\rho+p_t\ge0\) | satisfied everywhere |
| WEC | satisfied everywhere |
| SEC | violated for \(r<(GM\ell^2)^{1/3}\) |
| DEC | violated for \(r>(4GM\ell^2)^{1/3}\) |

The core mechanism is therefore more specific than "negative energy prevents collapse."

Instead:

\[
\boxed{
\text{positive density}
+
\text{vacuum-like radial tension}
+
\text{negative core tangential pressure}
}
\]

produce a de Sitter-like region that violates the strong energy condition while preserving NEC and WEC.

For the spacetime-screening program, this suggests that the first property to reproduce dynamically is not necessarily \(\rho<0\), but a high-curvature stress response capable of driving

\[
\rho+p_r+2p_t<0
\]

without creating fatal instabilities.

## Reproducibility

Run:

\`\`\`bash
python src/symbolic/effective_stress_energy.py
\`\`\`

The script checks the stress tensor, mass profile, conservation equation, center limits, trace relation, and energy-condition boundaries symbolically.
