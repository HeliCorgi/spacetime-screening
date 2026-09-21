# Analytic 4D GQTG Core Scaling and the Resummation Constraint

This note records a general structural result for four-dimensional
**analytic/polynomial generalized quasi-topological gravity (GQTG)**.

The result uses the all-order integrated single-function spherical equation
derived in:

P. Bueno, P. A. Cano, R. A. Hennigar, M. Lu, J. Moreno,
*Generalized quasi-topological gravities: the whole shebang*,
Class. Quantum Grav. **40** (2023) 015004,
arXiv:2203.05589.

That work finds that in \(D=4\) there is evidence for one genuine GQTG family
per curvature order \(n\ge3\), while the algebraic quasi-topological family
available in \(D\ge5\) is absent. The single-function black-hole equation is
therefore generically differential rather than algebraic.

## 1. Setup

Take the standard spherical ansatz

\[
ds^2
=
-f(r)dt^2
+
\frac{dr^2}{f(r)}
+
r^2d\Omega^2.
\]

For the \(D=4\) genuine GQTG family at curvature order \(n\), the relevant
integrated equation is a fixed combination of the general basis functions
\(F(n,j)\).

Up to normalization, the \(D=4\) coefficients satisfy

\[
\alpha_{n,n-1}
=
-\frac{n}{n-2}\alpha_{n,n}.
\]

## 2. Exact de Sitter-type core

First take

\[
f(r)=1-cr^2
\]

with finite positive \(c\).

Direct substitution into the all-order integrated equation gives

\[
F(n,j)
=
\frac12
c^{n-1}r
\left[
2j-n-cr^2(j-n+1)
\right].
\]

The genuine \(D=4\) combination therefore reduces exactly to

\[
\boxed{
F_n
=
-\frac12 c^n r^3
}
\]

up to the overall order-\(n\) coupling normalization.

The Einstein-Hilbert contribution likewise behaves as

\[
\boxed{
F_{\rm EH}=2cr^3.
}
\]

Hence every finite curvature order vanishes at least as

\[
r^3
\]

at a regular de Sitter-type center.

## 3. Generic regular core

The result is not an artifact of imposing an exactly even de Sitter series.

Take instead

\[
f(r)
=
1-cr^2+dr^3+O(r^4).
\]

For arbitrary curvature order \(n\),

\[
\boxed{
\frac{F_n}{r^3}
\longrightarrow
-\frac12c^n
+
\frac{3}{16}
n(n-1)c^{n-3}d^2
}
\]

as

\[
r\to0.
\]

Thus

\[
\boxed{
F_n=O(r^3)
}
\]

for every finite \(n\), even when the first odd regular-core correction is
included.

## 4. Finite truncations cannot support a nonzero vacuum mass at the center

The integrated black-hole equation contains the ADM-mass integration
constant.

Schematically,

\[
\mathcal F_{\rm EH}
+
\sum_{n=3}^{N}
\lambda_n\mathcal F_n
=
\text{constant proportional to }M.
\]

But every term on the left behaves as

\[
O(r^3)
\]

for finite \(N\).

Therefore

\[
\boxed{
\text{a finite analytic GQTG truncation cannot balance a nonzero mass
constant at a regular vacuum center.}
}
\]

This is consistent with the general expectation that finite higher-curvature
truncations can soften but do not generically remove the black-hole
singularity.

## 5. Normally convergent infinite towers have the same problem

Now consider an infinite tower,

\[
\sum_{n=3}^\infty
\lambda_nF_n(r).
\]

If this series converges normally/uniformly in a neighborhood of the limiting
core curvature, the \(r^3\) factor can be taken outside the convergent sum:

\[
\sum_n\lambda_nF_n
=
r^3
\mathcal G(c,d,\ldots)
+
o(r^3),
\]

with finite \(\mathcal G\).

Hence the sum still vanishes as

\[
r^3.
\]

It cannot equal a nonzero mass integration constant.

Therefore a nonzero-mass regular vacuum core requires at least one assumption
to fail.

Within the pure-metric local GQTG setup, the natural failure is:

\[
\boxed{
\text{the infinite tower must resum non-uniformly at the limiting curvature.}
}
\]

Equivalently, the resummed spherical response must become singular while the
physical curvature remains finite.

## 6. How singular must the resummation be?

Suppose a finite curvature variable \(c(r)\) approaches its limiting value as

\[
c(r)-c_*
=
a r^p+\cdots,
\qquad
p>0.
\]

Suppose the integrated equation near the core has the schematic form

\[
M_0
=
r^3\mathcal G(c(r))
+\cdots
\]

with

\[
M_0\neq0.
\]

Then

\[
\mathcal G(c(r))
\sim
\frac{M_0}{r^3}.
\]

Since

\[
r
\sim
\left|
\frac{c-c_*}{a}
\right|^{1/p},
\]

the required resummed behavior is

\[
\boxed{
\mathcal G(c)
\sim
|c-c_*|^{-3/p}.
}
\]

Examples:

### Hayward-type approach

For

\[
c-c_*\sim r^3,
\]

we have

\[
p=3,
\]

so the required inverse response has a **simple pole**,

\[
\mathcal G\sim|c-c_*|^{-1}.
\]

This is exactly the qualitative behavior of the Hayward inverse response.

### Smooth even correction

If

\[
c-c_*\sim r^2,
\]

then

\[
p=2
\]

and

\[
\mathcal G
\sim
|c-c_*|^{-3/2}.
\]

### Linear approach

If

\[
c-c_*\sim r,
\]

then

\[
p=1
\]

and

\[
\mathcal G
\sim
|c-c_*|^{-3}.
\]

## 7. Important conceptual correction: a response pole is not automatically a pathology

This point is essential.

If the physical curvature saturates,

\[
\psi(s)\to\psi_*
\]

while the source variable satisfies

\[
s\to\infty,
\]

then the inverse function

\[
s(\psi)
\]

**must** diverge at

\[
\psi=\psi_*.
\]

For example, Hayward screening gives

\[
\psi(s)
=
\frac{s}{1+\ell^2s},
\]

so

\[
s(\psi)
=
\frac{\psi}{1-\ell^2\psi},
\]

which has a pole at

\[
\psi_*=\ell^{-2}.
\]

That pole is simply the inverse mathematical statement of saturation.

Therefore the project should **not** reject a candidate merely because its
symmetry-reduced inverse response diverges at the limiting curvature.

The physically meaningful question is:

\[
\boxed{
\text{Does the full 4D action and the reduced physical perturbation operator
remain finite and differentiable?}
}
\]

## 8. Distinguishing three kinds of singularity

The calculations so far motivate a strict distinction.

### A. Necessary inverse-response singularity

Example:

\[
s(\psi)
\to\infty
\]

as

\[
\psi\to\psi_*.
\]

This can be a healthy representation of curvature saturation.

### B. Non-uniform resummation

An infinite analytic tower has a finite radius/boundary of convergence or
develops a singular resummed generating function at the limiting curvature.

This may be necessary to evade the \(r^3\) suppression theorem.

It is not automatically fatal, but it requires a nonperturbative definition.

### C. Fundamental-action / principal-operator singularity

Examples include:

- a four-dimensional action whose first variation does not exist on the
  background;
- a kinetic matrix that vanishes or flips sign;
- a physical characteristic metric whose curvature diverges.

These are genuine failures under the current principal-safe criteria unless a
more fundamental description resolves them.

## 9. Four-dimensional structural tension

Combining the current results gives the following picture for local
pure-metric theories depending algebraically on the Riemann tensor.

### If one demands algebraic GR-like spherical equations in \(D=4\)

The recent QTG-TNT classification finds that first-order/algebraic
integrability requires non-analytic curvature dependence. citeturn418771academia37

### If one demands analytic/polynomial four-dimensional curvature actions

The known \(D=4\) GQTG family has differential single-function equations rather
than the algebraic quasi-topological equation present in \(D\ge5\).
The 2023 GQTG classification specifically notes that no ordinary
quasi-topological family exists in \(D=4\), while a genuine GQTG density
appears at each order. citeturn418771academia38turn418771search39

### If one also demands a nonzero-mass regular vacuum core

The present calculation shows that every finite analytic order contributes
only

\[
O(r^3)
\]

at the center.

Therefore the infinite tower must become non-uniform at the limiting
curvature.

This is the current **4D screening structural constraint**:

\[
\boxed{
\begin{array}{c}
\text{local pure metric}\\
+\text{analytic finite-order building blocks}\\
+\text{nonzero-mass regular vacuum core}
\end{array}
\Rightarrow
\text{non-uniform infinite resummation is required}.
}
\]

This is not a formal no-go theorem for every conceivable local theory, but it
is a concrete all-order constraint within the known \(D=4\) GQTG spherical
family.

## 10. Relation to the 2026 nonpolynomial Hayward construction

The Borissova–Carballo-Rubio theory realizes a regular four-dimensional
Hayward vacuum solution using explicitly nonpolynomial gravity and an
algebraic spherical equation. citeturn418771search0turn418771academia36

Its reduced Hayward inverse response contains exactly the kind of limiting
pole expected from the argument above.

The difficulty found by this repository was not the existence of that pole,
but the differentiability of one explicit four-dimensional rational
representative used to lift the reduced theory.

That distinction should remain explicit in all future candidate evaluations.

## 11. Consequence for v3 design

The most promising directions are now:

1. **Nonlocal QTG:** allow a genuinely nonlocal resummation whose fundamental
   operator can remain entire/ghost-free even though the spherical inverse
   response is non-uniform.

2. **A manifestly smooth infinite-tower 4D GQTG definition:** find a
   nonperturbative resummation in which the full action is well defined at the
   limiting curvature despite the required non-uniformity.

3. **Extra microscopic variables / phase change:** let the metric-only local
   description cease to be fundamental before the resummation singularity is
   reached.

The first option currently remains the cleanest match to the project's
principal-safe criteria.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/analytic_gqtg_core_scaling.py
python src/symbolic/resummation_singularity_scaling.py
\`\`\`

to reproduce the all-order \(r^3\) core scaling and the required
\(|c-c_*|^{-3/p}\) resummation behavior.
