# Vector-Hair Benchmark: Exact Hayward-Type Solutions from an Action

This note uses the two-vector construction of Eichhorn & Fernandes as a
benchmark for the spacetime-screening program.

Reference:

A. Eichhorn and P. G. S. Fernandes,
*Regular black holes without mass-inflation instability and gravastars from
modified gravity*, Phys. Rev. D **113**, L081501 (2026),
arXiv:2508.00686, https://doi.org/10.1103/nqz2-88zf

The significance for this repository is that a Hayward-type metric is not
merely postulated: it appears as an exact solution of a four-dimensional
generally covariant action with auxiliary vector fields.

We use geometric units \(G=c=1\) in this note, matching the reference.

## 1. Action

The theory contains two vector fields \(A_\mu\) and \(B_\mu\),

\[
S
=
\frac1{16\pi}
\int d^4x\sqrt{-g}
\left[
R+\ell^2\left(\mathcal L[A]-\mathcal L[B]\right)
\right],
\]

with

\[
\mathcal L[W]
=
4G^{\mu\nu}W_\mu W_\nu
+
8W_\nu W^\nu\nabla_\mu W^\mu
+
6(W_\nu W^\nu)^2.
\]

The vectors have no ordinary kinetic term in this construction and act as
nonlinear auxiliary constraints.

For the black-hole solution they are null.

## 2. General static spherical solution

In ingoing null coordinates,

\[
ds^2
=
-f(r)dv^2
+
2\,dv\,dr
+
r^2d\Omega^2.
\]

Take

\[
A_\mu dx^\mu=a(r)dv,
\qquad
B_\mu dx^\mu=b(r)dv.
\]

The solution family contains two primary-hair integration constants
\(q_a,q_b\),

\[
a(r)
=
\frac{r-rf(r)-q_a/2}{2r^2},
\]

\[
b(r)
=
\frac{r-rf(r)-q_b/2}{2r^2},
\]

and

\[
f(r)
=
1-
\frac{
8Mr^3+\ell^2(q_a^2-q_b^2)
}{
4r\left[r^3+(q_a-q_b)\ell^2\right]
}.
\]

## 3. Regularity fixes a relation between the hairs

Expanding at small \(r\),

\[
f(r)
=
-\frac{q_a+q_b}{4r}
+
1
+
O(r^2).
\]

Therefore regularity requires

\[
\boxed{
q_b=-q_a
}.
\]

On this branch,

\[
\boxed{
f(r)
=
1-
\frac{2Mr^2}
{r^3+2q_a\ell^2}
}.
\]

This is a Hayward-type geometry.

The original Hayward form is recovered for

\[
\boxed{
q_a=M
}.
\]

## 4. Screening interpretation

Write

\[
f(r)
=
1-\frac{2M}{r}S(r).
\]

Then

\[
\boxed{
S(r)
=
\frac{r^3}
{r^3+2q_a\ell^2}
}.
\]

Thus

\[
S(r)\to1
\qquad(r\to\infty),
\]

while

\[
S(r)\to0
\qquad(r\to0).
\]

So the exact solution realizes the same *diagnostic* screening profile used in
this repository, but now it arises from a covariant action rather than an
ad-hoc \(G(r)\).

This does **not** mean that Newton's constant literally becomes zero. The
screening factor is a convenient characterization of the resulting geometry.

## 5. Core curvature

Near the center,

\[
f(r)
=
1-
\frac{M}{q_a\ell^2}r^2
+
O(r^5).
\]

Define

\[
L_{\rm core}^2
=
\frac{q_a\ell^2}{M}.
\]

Then

\[
f(r)
=
1-\frac{r^2}{L_{\rm core}^2}+O(r^5).
\]

Therefore

\[
R(0)
=
\frac{12}{L_{\rm core}^2}
=
\frac{12M}{q_a\ell^2},
\]

\[
R_{\mu\nu}R^{\mu\nu}(0)
=
\frac{36M^2}{q_a^2\ell^4},
\]

and

\[
\boxed{
K(0)
=
\frac{24M^2}{q_a^2\ell^4}
=
\frac{24}{L_{\rm core}^4}
}.
\]

The primary hair therefore controls the maximum core curvature.

## 6. Effective stress response

If the geometry is moved to the right-hand side of the ordinary Einstein
equation as an effective source,

\[
\rho
=
\frac{
3Mq_a\ell^2
}{
2\pi(r^3+2q_a\ell^2)^2
},
\]

\[
p_r=-\rho,
\]

and

\[
p_t
=
\frac{
3Mq_a\ell^2(r^3-q_a\ell^2)
}{
\pi(r^3+2q_a\ell^2)^3
}.
\]

Thus

\[
\rho+p_r+2p_t
=
\frac{
6Mq_a\ell^2(r^3-q_a\ell^2)
}{
\pi(r^3+2q_a\ell^2)^3
}.
\]

The strong energy condition is violated for

\[
\boxed{
r<(q_a\ell^2)^{1/3}
}.
\]

This matches the region identified in the exact vector-field construction.

The reference emphasizes that the two individual vector contributions can be
singular at the origin while canceling on the regular branch. The finite core
is therefore produced by the full constrained system, not by interpreting one
vector as ordinary matter.

## 7. Extremal regular black holes for arbitrary mass

The horizon equation is

\[
r_h^3-2Mr_h^2+2q_a\ell^2=0.
\]

A degenerate horizon satisfies additionally

\[
f'(r_h)=0.
\]

Solving both gives

\[
q_a
=
\frac{r_h^3}{4\ell^2},
\]

and

\[
M=\frac{3r_h}{4}.
\]

Hence

\[
\boxed{
r_{\rm ext}=\frac{4M}{3}
}
\]

and

\[
\boxed{
q_{a,\rm ext}
=
\frac{16M^3}{27\ell^2}
}.
\]

The metric becomes

\[
\boxed{
f_{\rm ext}(r)
=
1-
\frac{2Mr^2}
{r^3+\frac{32}{27}M^3}
}.
\]

The horizon is degenerate, so its surface gravity vanishes.

This construction removes the standard two-distinct-horizon mass-inflation
setup at the classical level.

## 8. New tradeoff for the screening program

There are two particularly informative choices for \(q_a\).

### Original Hayward choice

Set

\[
q_a=M.
\]

Then

\[
L_{\rm core}^2=\ell^2
\]

and

\[
\boxed{
K_{\rm core}
=
\frac{24}{\ell^4}
}.
\]

Thus \(\ell\) sets a mass-independent limiting curvature.

This is attractive if \(\ell\) is interpreted as a universal microscopic
quantum-gravity scale.

However, only the special mass

\[
M=\frac{3\sqrt3}{4}\ell
\]

is extremal.

### Fully extremal choice

Instead choose

\[
q_a
=
\frac{16M^3}{27\ell^2}.
\]

Then all masses can lie on the extremal regular branch, but

\[
L_{\rm core}^2
=
\frac{16}{27}M^2,
\]

so

\[
\boxed{
K_{\rm core}
=
\frac{2187}{32M^4}
}.
\]

The coupling scale \(\ell\) drops out of the metric and the limiting curvature
is no longer universal: it depends strongly on the black-hole mass.

This gives a concrete tradeoff:

\[
\boxed{
\text{universal limiting curvature}
\quad\leftrightarrow\quad
\text{extremality for arbitrary mass}
}
\]

within this benchmark family.

The tradeoff is not a theorem for all regular-black-hole theories, but it is a
useful target for the spacetime-screening program: a stronger model should ask
whether it can retain both.

## 9. Screening strength at the extremal horizon

For the fully extremal branch,

\[
S(r)
=
\frac{r^3}
{r^3+\frac{32}{27}M^3}.
\]

At

\[
r_h=\frac{4M}{3},
\]

the exact value is

\[
\boxed{
S(r_h)=\frac23
}.
\]

Thus the degenerate horizon forms while the diagnostic gravitational response
has already been reduced by one third relative to the asymptotic value.

## 10. Interpretation

This benchmark changes the status of the project in an important way.

The qualitative sequence

\[
\text{GR exterior}
\rightarrow
\text{screened region}
\rightarrow
\text{finite-curvature core}
\]

can already be realized by an explicit covariant action.

What remains open is whether the mechanism is a plausible quantum-gravity
completion. In particular we still need:

- perturbative degree-of-freedom analysis;
- nonlinear stability;
- semiclassical stability of the degenerate horizon;
- rotating solutions;
- dynamical formation from ordinary collapse;
- a microscopic reason for the required vector-hair branch;
- a universal scale if limiting curvature is to be fundamental.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/vector_hair_benchmark.py
\`\`\`

to verify the regularity condition, core invariants, effective stress tensor,
SEC boundary, extremal hair relation, and the limiting-curvature tradeoff.
