# Candidate Scorecard

This document tracks candidate realizations of Spacetime Screening against the
project's current acceptance criteria.

The purpose is not to rank theories by reputation.  It is to record exactly
which failure mode has been checked, which remains open, and what calculation
would change the status.

Legend:

- **PASS** — checked within the stated scope.
- **FAIL** — an explicit obstruction has been found.
- **PARTIAL** — succeeds in a restricted sector but not yet generally.
- **OPEN** — not established.
- **N/A** — criterion does not apply in the same form.

## Current scorecard

| Candidate | 4D covariant action | Regular BH background | Dynamical formation | Covariant-lift differentiability | Physical kinetic matrix | Principal-symbol regularity | Strong coupling | Inner-horizon status | Current role |
|---|---|---|---|---|---|---|---|---|---|
| Minimal static \(F(\chi)R\) scalar | PASS | FAIL for target one-function Hayward ansatz | OPEN | PASS | N/A | N/A | N/A | N/A | Rejected minimal toy |
| Two auxiliary vectors | PASS | PASS | OPEN | PASS | **FAIL candidate: negative odd-vector kinetic mode** | FAIL candidate in radial TT diagnostic | **strong ghost/degeneracy concern** | PARTIAL via extremality | Counterexample / diagnostic; direct 2-vector expansion pending |
| Nonpolynomial pure-gravity rational QTG lift | PASS as representative formula | PASS in spherical reduction | Related models: PARTIAL | **FAIL for displayed lift** | OPEN | not well-defined generically before lift repair | OPEN | OPEN | Spherical response benchmark |
| Regularized-Lovelock/Horndeski infinite tower | PASS | PASS for known planar branch | OPEN | PASS | **FAIL on known planar branch** | **FAIL on known planar branch** | **FAIL** | not main issue | Rejected known regular branch |
| Polynomial QTG, \(D\ge5\) | PASS | PASS | PASS in studied collapse models | PASS | OPEN on generic RBH | OPEN | OPEN | OPEN | Higher-D clean benchmark |
| 4D generalized quasi-topological gravity | PASS, polynomial order by order | no infinite-tower regular vacuum BH established here | OPEN | PASS | OPEN | OPEN | OPEN | OPEN | Candidate building blocks |
| First-order QTG-TNT (2026) | PASS as non-analytic metric action | PASS only above critical mass | OPEN | **FAIL/ill-defined on SF branch generically** | OPEN | OPEN | concern from non-differentiable action | extremal remnant; perturbative status OPEN | Symmetry-sector benchmark / rejected v3 |
| Nonlocal QTG completion | Reported PASS | Reported PASS | OPEN | expected to avoid projector lift; exact check pending | Reported ghost-free in source | OPEN on regular-BH background | Reported avoidance | OPEN | Leading v3 benchmark |

## 1. Minimal canonical scalar

Tested action:

\[
S
=
\int\sqrt{-g}
\left[
\frac{F(\chi)}{16\pi G}R
-\frac12(\partial\chi)^2
-V(\chi)
\right].
\]

For

\[
ds^2=-fdt^2+\frac{dr^2}{f}+r^2d\Omega^2,
\qquad
\chi=\chi(r),
\]

the field-equation difference gives

\[
F''=-8\pi G\chi'^2\le0.
\]

Regular-center and asymptotically constant boundary conditions force the
profile to be trivial.

**Status:** rejected as the minimal static one-function realization.

## 2. Two-vector benchmark

Strengths:

- explicit four-dimensional action;
- exact Hayward-type background;
- published radial linear stability;
- algebraic axial vector perturbations;
- extremal branch can remove the standard nonzero-surface-gravity
  mass-inflation setup.

Failures/concerns found in this repository:

- vector quadratic action vanishes around the asymptotic vacuum;
- a singular divergence-free null auxiliary combination behaves as \(r^{-2}\);
- radial pure-TT principal metric reduces exactly to Schwarzschild,
  \(f_T=1-2M/r\);
- test fields on the extremal throat possess an Aretakis instability.

**Status:** valuable counterexample showing that background regularity is
insufficient.

## 3. Nonpolynomial pure-gravity QTG

Strengths in spherical symmetry:

\[
\frac{\psi}{1-\ell^2\psi}=s,
\qquad
\psi=\frac{s}{1+\ell^2s},
\]

so

\[
\psi\to\ell^{-2},
\qquad
\partial_s\psi\to0.
\]

This is the cleanest current realization of the *background screening law*.

Problem found here:

the particular rational four-dimensional lift displayed in the 2026 paper
contains curvature-invariant ratios whose values are removable on the
single-function branch but whose generic invariant gradients diverge.

**Status:** keep the reduced response law; do not use that representative
rational lift as the full perturbative theory without a regular extension.

## 4. Regularized-Lovelock/Horndeski infinite tower

Advantages:

- local four-dimensional shift-symmetric Horndeski action;
- second-order field equations;
- no curvature-projector ratios needed;
- regular planar black-hole backgrounds exist.

Known exact regular branch:

\[
\phi'=\frac1r.
\]

Despite finite background curvature and finite

\[
X=-\frac12(\partial\phi)^2,
\]

published perturbation theory gives:

\[
c_{\Omega,\rm odd}^2\to-\infty
\]

at the core, together with odd ghost instability, while

\[
\det K=\det G=0
\]

for the even scalar-containing sector at all radii.

**Status:** known regular planar branch fails principal-safe criteria.

The stability of hypothetical regular spherical branches is not settled by
that result.

## 5. Polynomial QTG in higher dimensions

In \(D\ge5\), polynomial quasitopological gravities provide a particularly
clean conceptual benchmark:

- no rational projector lift;
- infinite higher-curvature tower;
- regular black-hole solutions;
- explicit dynamical collapse results.

The drawback for this project is obvious:

\[
D\neq4.
\]

**Status:** use as a structural benchmark for what a successful 4D theory
should imitate.

## 6. Four-dimensional generalized quasi-topological gravity

Polynomial generalized quasi-topological densities exist in \(D=4\) and
propagate only the massless transverse graviton on maximally symmetric
backgrounds, order by order.

However, the static spherical equation is generally differential rather than
the algebraic QTG relation responsible for the simplest limiting-curvature
mechanism.

No four-dimensional infinite-tower vacuum regular black-hole construction is
being assumed here unless explicitly demonstrated.

**Status:** candidate set of polynomial building blocks, not yet a completed
screening model.

## 7. Nonlocal QTG

The July 2026 preprint reports an infinite-derivative quasitopological
completion with:

- ghost freedom;
- avoidance of strong-coupling instabilities;
- exact spherical vacuum regular black holes;
- perturbative Birkhoff behavior.

Those are precisely the properties the previous candidates failed to combine.

The repository has not yet reproduced the exact curved-background quadratic
operator from the preprint, so these entries remain **reported**, not
independently verified.

**Status:** highest-priority v3 benchmark.

## Decision tree

The next candidate should be rejected immediately if any of the following
occur:

\[
\boxed{
\begin{array}{ll}
1.&\text{action/first variation undefined on the background},\\
2.&\text{physical kinetic eigenvalue vanishes or becomes negative},\\
3.&\text{physical gradient eigenvalue becomes negative},\\
4.&\text{principal characteristic becomes singular at a regular core},\\
5.&\text{regularity relies on cancellation of singular hidden fields}.
\end{array}
}
\]

Only after passing these tests should effort be spent on evaporation,
information recovery, or a non-geometric completion.

## Immediate next step

Obtain the exact nonlocal-QTG quadratic operator or an equivalent authoritative
expression, then test it directly on the regular black-hole background.

If that is not possible, the fallback route is to construct a polynomial
four-dimensional GQTG infinite tower whose action is manifestly smooth and
ask whether the desired curvature-susceptibility saturation can be reproduced
without introducing an extra physical mode.


## 8. First-order QTG-TNT (2026)

The June 2026 QTG-TNT construction enlarges quasi-topological integrability to
static spherical, Taub-NUT, NHEK, swirling, and related symmetry classes.

The simplest regular static model has

\[
A(x)=\frac{2x}{1-x},
\]

and

\[
a(r)
=
\frac{(r-2m)(r^2-2\ell^2)}
{r^3-2r\ell^2+4m\ell^2}.
\]

For

\[
m>\frac{2\ell}{3\sqrt6},
\]

the metric has finite polynomial curvature invariants at the center.  It
reaches extremality at

\[
m=\frac{\ell}{\sqrt2}.
\]

However:

- regularity requires \(A(x)\) to have a pole at the limiting curvature;
- the physical solution reaches that pole at \(r=0\) and at
  \(r=\sqrt2\,\ell\);
- \(\Box R\sim1/r\) at the center;
- the covariant SF selector is
  \[
  R_4=\sqrt{\frac{2I_6}{3}-\frac{2I_{11}}{I_1}},
  \]
  so on the SF branch
  \[
  \partial R_4/\partial I_6\sim1/R_4,
  \qquad
  \partial^2R_4/\partial I_6^2\sim1/R_4^3;
  \]
- even within TNT, the covariant square root gives an \(|\epsilon|\) cusp
  when the signed reduced \(R_4\) crosses zero;
- the full correction \(A(R_3)R_4\) therefore has no ordinary generic 4D
  first variation on the SF branch unless \(A=0\);
- the source classification proves this is structural: analytic curvature
  scalars contain only even powers of \(R_4\), so the nontrivial first-order
  Class-I mechanism necessarily requires non-analyticity.

**Status:** strong symmetry-sector construction and useful integrability
benchmark, but **FAIL** as the present full four-dimensional perturbative
candidate under the covariant-action differentiability criterion.


## Odd-vector kinetic update

Applying the standard generalized-Proca odd quadratic-action reduction to the
additive two-vector benchmark gives

\[
K_{\rm vec}
=
-\frac{cc^{\rm T}}{C_1}.
\]

In the static exterior \(C_1>0\), so the derivative-active vector combination
has a negative kinetic eigenvalue.  The orthogonal vector combination has zero
principal kinetic coefficient.

The \(l=1\) sector is especially diagnostic because there is no local odd
gravitational-wave degree of freedom.  At principal derivative order,

\[
\mathcal L_{l=1}^{\rm pr}
=
-\frac1{C_1}
[c^{\rm T}(\dot u-fu')]^2.
\]

This is now the leading viability obstruction for the vector benchmark.

The score remains labeled **candidate** rather than a completed theorem until
the full two-vector harmonic action is rederived directly from the original
action and its constraint algebra is explicitly checked.
