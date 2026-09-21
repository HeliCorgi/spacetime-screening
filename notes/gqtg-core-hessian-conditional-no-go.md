# Conditional No-Go: Analytic 4D GQTG Base vs a Nonzero-Mass Limiting-Curvature Core

This note combines the all-order 4D GQTG core scaling with the NLQT
base-Hessian gate.

## 1. Core scaling

For the genuine four-dimensional GQTG density at curvature order \(n\),

\[
F_n
=
-\frac12
\lambda_n c^n r^3
\]

on an exact de Sitter-type core

\[
f(r)=1-c r^2.
\]

Define

\[
G(c)
=
\sum_{n\ge3}\lambda_n c^n.
\]

The integrated higher-curvature contribution is therefore

\[
-\frac12r^3G(c).
\]

## 2. Nonzero mass requires a singular resummation

Suppose

\[
c(r)\to c_*
\]

with \(c_*\) finite and the integrated equation must approach a nonzero mass
constant.

Then necessarily

\[
\boxed{
r^3G(c(r))
\to
\text{nonzero}.
}
\]

Therefore

\[
\boxed{
G(c(r))
\sim
r^{-3}.
}
\]

In particular, \(G(c)\) cannot remain finite at \(c_*\).

## 3. Normal convergence is incompatible

If the infinite local-curvature series converges normally in a neighborhood
of \(c_*\),

\[
\sum|\lambda_n c^n|
<\infty,
\]

then \(G(c_*)\) is finite.

Consequently,

\[
r^3G(c(r))
\to0,
\]

contradicting a nonzero mass constant.

Hence:

\[
\boxed{
\text{nonzero-mass finite-curvature core}
\Longrightarrow
\text{nonuniform / singular resummation at }c_*.
}
\]

This is the same conclusion reached previously from the spherical response,
now stated as a gate on the analytic GQTG base.

## 4. Relation to the curvature Hessian

Termwise differentiability of the local action requires control over series
with additional powers of \(n\), schematically

\[
\sum
n(n-1)
\lambda_n c^{n-2},
\]

which is the structure entering curvature Hessians on constant-curvature
backgrounds.

A representative geometric tower,

\[
\lambda_n
\propto
c_*^{1-n},
\]

gives

\[
G(c)
\sim
\frac{1}{1-c/c_*},
\]

while

\[
G''(c)
\sim
(1-c/c_*)^{-3}.
\]

Thus the simplest resummation that supplies the required core mass also makes
the curvature-response Hessian divergent.

## 5. Conditional no-go

Under the assumptions that:

1. the 4D base is a local analytic GQTG infinite tower;
2. the action and its curvature Hessian are defined by normally convergent,
   termwise differentiable series in an open neighborhood of the limiting
   curvature;
3. the core has finite curvature \(c_*\) and nonzero mass;

the three conditions are incompatible.

Schematically,

\[
\boxed{
\begin{array}{c}
\text{local analytic GQTG}\\
+\text{finite Hessian at }c_*\\
+\text{nonzero-mass limiting-curvature core}
\end{array}
\quad\text{cannot all hold.}
}
\]

This is a **conditional** no-go.  It does not exclude exotic resummation
prescriptions for which the full action is defined nonperturbatively despite
the failure of termwise convergence.

## 6. Consequence for 4D NLQT

NLQT needs a well-defined base operator

\[
\hat{\mathcal D}
=
\delta\hat{\mathcal E},
\]

which in turn uses the curvature Hessian of the base action.

Therefore simply taking an analytic local GQTG tower to the boundary of its
convergence radius does not automatically provide a principal-safe 4D NLQT
base.

The remaining escape routes are:

1. a genuinely nonlocal base action defined nonperturbatively from the start;
2. additional regular fundamental fields;
3. a regular geometry without a symmetry-enhanced \(r=0\) center, such as a
   bounce/minimal-radius geometry;
4. an explicit resummation whose full curvature Hessian is finite despite the
   singular spherical response.

Option 4 would require an explicit construction.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/gqtg_core_hessian_conditional_no_go.py
\`\`\`.
