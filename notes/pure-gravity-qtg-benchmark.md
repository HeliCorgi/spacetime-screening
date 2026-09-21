# Pure-Gravity Quasitopological Benchmark: Intrinsic Curvature Screening

This note introduces the next action-level benchmark for the project:
four-dimensional nonpolynomial quasitopological gravity.

Primary reference:

Johanna Borissova and Raúl Carballo-Rubio,
*Regular black holes from pure gravity in four dimensions*,
Phys. Rev. D **113**, 124004 (2026),
https://doi.org/10.1103/6x2z-qbkh

The key difference from the auxiliary-vector benchmark is conceptual:

\[
\boxed{
\text{regularization is encoded directly in the gravitational curvature response}
}
\]

rather than in a cancellation between singular extra fields.

## 1. Spherical curvature variable

For

\[
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2,
\]

define

\[
\boxed{
\psi(r)=\frac{1-f(r)}{r^2}.
}
\]

In Schwarzschild,

\[
\psi_{\rm GR}=\frac{2M}{r^3}.
\]

It is useful to regard

\[
s(r)=\frac{2M}{r^3}
\]

as the source/GR curvature scale that would diverge at the center.

## 2. Hayward characteristic function

For the exact Hayward realization in the 2026 pure-gravity construction, the
nonpolynomial quasitopological characteristic function is

\[
\boxed{
H(\psi)
=
\frac{6\psi}{1-\ell^2\psi}.
}
\]

The spherical vacuum equation is

\[
H(\psi)=\frac{12M}{r^3}.
\]

Dividing by six gives the especially transparent relation

\[
\boxed{
\frac{\psi}{1-\ell^2\psi}
=
s.
}
\]

Solving for the curvature response,

\[
\boxed{
\psi(s)
=
\frac{s}{1+\ell^2s}.
}
\]

## 3. Screening as vanishing curvature susceptibility

At weak curvature,

\[
\ell^2s\ll1,
\]

so

\[
\psi=s-\ell^2s^2+\cdots,
\]

and GR is recovered.

At strong source,

\[
s\to\infty,
\]

we get

\[
\boxed{
\psi\to\frac1{\ell^2}.
}
\]

More importantly,

\[
\boxed{
\frac{d\psi}{ds}
=
\frac1{(1+\ell^2s)^2}
\to0.
}
\]

This gives a sharper definition of **spacetime screening** than an ad-hoc
running Newton constant:

\[
\boxed{
\text{screening}
\equiv
\text{vanishing response of curvature to further source growth}.
}
\]

The source \(s\) may continue to diverge as \(r^{-3}\), while the geometric
curvature variable saturates.

## 4. Intrinsic screening factor

Define

\[
\Sigma
=
1-\ell^2\psi.
\]

On the solution,

\[
\boxed{
\Sigma(r)
=
\frac{r^3}{r^3+2M\ell^2}.
}
\]

This is exactly the same radial function that was previously interpreted
diagnostically as

\[
G_{\rm eff}/G.
\]

But here it has a more intrinsic meaning:

\[
\boxed{
\Sigma
=
\text{distance from the curvature-response pole}.
}
\]

Furthermore,

\[
\boxed{
\frac{d\psi}{ds}=\Sigma^2.
}
\]

Thus the earlier screening intuition can be recast without saying that
Newton's constant literally depends on radius.

## 5. Exact Hayward metric

Using

\[
f=1-r^2\psi,
\]

we obtain

\[
\boxed{
f(r)
=
1-
\frac{2Mr^2}{r^3+2M\ell^2}.
}
\]

At the center,

\[
\psi\to\frac1{\ell^2},
\]

so

\[
f(r)
=
1-\frac{r^2}{\ell^2}+O(r^5).
\]

The curvature invariants approach

\[
\boxed{
R(0)=\frac{12}{\ell^2},
}
\]

\[
\boxed{
R_{\mu\nu}R^{\mu\nu}(0)=\frac{36}{\ell^4},
}
\]

and

\[
\boxed{
K(0)=\frac{24}{\ell^4}.
}
\]

The limiting scale is independent of the black-hole mass.

## 6. Why this is a better screening benchmark

The auxiliary-vector benchmark taught us that

\[
\text{finite background metric curvature}
\]

is not sufficient.

Its background regularity depended on a cancellation involving a singular
null auxiliary field, and the radial pure-TT principal symbol retained a
hidden Schwarzschild structure.

The pure-gravity quasitopological benchmark avoids that particular mechanism:

- there is no singular auxiliary vector profile;
- the regularity is encoded in a constitutive relation for curvature itself;
- the Hayward metric is a vacuum solution of a generally covariant
  four-dimensional gravitational action;
- the spherical field equation is second order and algebraic in the
  single-function static sector.

This makes it a cleaner realization of the original Spacetime Screening idea.

## 7. But local quasitopological gravity is not automatically the endpoint

The 2026 pure-gravity paper guarantees special second-order behavior on
spherically symmetric backgrounds. That does not by itself prove that the full
four-dimensional nonspherical perturbation spectrum is ghost-free or free
from strong coupling.

This distinction is essential.

The project should not repeat the mistake

\[
\text{regular background}
\Rightarrow
\text{healthy theory}.
\]

Instead, the local nonpolynomial theory is the **background benchmark**, while
its infinite-derivative completion is the more ambitious perturbative
benchmark.

## 8. Nonlocal quasitopological completion

A July 2026 preprint by Bueno, Cano, Hennigar, and Murcia,

*Regular Black Holes in Nonlocal Quasitopological Gravity*,
arXiv:2607.07790,

states that an infinite-derivative completion can simultaneously provide:

- ghost freedom;
- avoidance of strong-coupling instabilities;
- exact spherically symmetric vacuum regular black holes;
- a perturbative Birkhoff theorem.

This is currently a particularly direct match to the failure criteria found
in the vector benchmark.

Because that work is a recent preprint, the project will treat these properties
as claims to reproduce/check, not as assumptions.

## 9. Dynamical formation

Related four-dimensional nonpolynomial gravity constructions have already
been used to model nonsingular collapse of pressureless stars and thin shells,
with second-order spherical equations and a Birkhoff theorem.

This means the pure-gravity route is not limited to reverse-engineering a
static metric.

A successful Spacetime Screening model should ultimately reproduce that
dynamical advantage while also passing nonspherical principal-symbol tests.

## 10. New working definition

Based on the calculations so far, the repository adopts the following stronger
working definition:

\[
\boxed{
\text{Spacetime Screening}
=
\frac{\partial(\text{physical curvature response})}
{\partial(\text{source scale})}
\longrightarrow0
}
\]

in the high-curvature regime,

**provided that** the physical perturbation principal symbols remain finite,
hyperbolic, and nondegenerate.

The second clause is necessary because the vector benchmark demonstrated that
background screening can coexist with a singular characteristic structure.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/pure_gravity_qtg_benchmark.py
\`\`\`

to verify the characteristic function, exact Hayward solution, screening
susceptibility, and center curvature limits.
