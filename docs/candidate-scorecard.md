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
| Two auxiliary vectors | PASS | PASS | OPEN | PASS | **FAIL: direct odd ghost in asymptotic exterior** | FAIL candidate in radial TT diagnostic | **FAIL / asymptotic degeneracy** | PARTIAL via extremality | Rejected as healthy benchmark; retained as counterexample |
| Nonpolynomial pure-gravity rational QTG lift | PASS as representative formula | PASS in spherical reduction | Related models: PARTIAL | **FAIL for displayed lift** | OPEN | not well-defined generically before lift repair | OPEN | OPEN | Spherical response benchmark |
| Regularized-Lovelock/Horndeski infinite tower | PASS | PASS for known planar branch | OPEN | PASS | **FAIL on known planar branch** | **FAIL on known planar branch** | **FAIL** | not main issue | Rejected known regular branch |
| Polynomial QTG, \(D\ge5\) | PASS | PASS | PASS in studied collapse models | PASS | OPEN on generic RBH | OPEN | OPEN | OPEN | Higher-D clean benchmark |
| 4D analytic Class-II / GQTG | PASS, polynomial order by order | no principal-safe infinite-tower regular vacuum BH established here | OPEN | PASS order by order | **FAIL/strong-coupling concern as complete local theory** | **FAIL/degenerate principal structure concern** | concern from reduced spectrum | OPEN | EFT/building block only |
| First-order QTG-TNT (2026) | PASS as non-analytic metric action | PASS only above critical mass | OPEN | **FAIL/ill-defined on SF branch generically** | OPEN | OPEN | concern from non-differentiable action | extremal remnant; perturbative status OPEN | Symmetry-sector benchmark / rejected v3 |
| Nonlocal QTG completion | PASS as pure-metric nonlocal construction | PASS in inherited SS sector | OPEN | **OPEN in 4D: depends on nonpolynomial QT base** | PASS on maximally-symmetric/SS proven subspaces | **OPEN for generic nonspherical RBH modes** | PASS for order-reduction mechanism in source | OPEN | Leading surviving candidate |

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

Direct source-action follow-up now shows that, in a sufficiently large but
finite asymptotic exterior region, the reduced odd (l=2) physical kinetic
matrix has negative determinant after the nondynamical directions are
eliminated:

\[
\lim_{r\to\infty}
r^5\det K_{\rm red}
=
-\frac{1152\pi^2}{25}
M\ell^4(16M^2+q^2)<0.
\]

Hence one reduced odd kinetic eigenvalue is negative in that open region.
The derivative-null vector combination has positive algebraic stiffness and
no velocity mixing, so it does not remove the negative mode.

**Status:** rejected as a globally healthy perturbative benchmark; retained as
a counterexample showing that background regularity is insufficient.

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


## Direct odd-sector ghost update

The original two-vector action has now been expanded directly in four-
dimensional axial harmonics.

The direct calculation reproduces:

\[
\text{no intrinsic }\dot u^2
\quad+\quad
\text{metric-vector derivative mixing}
\quad+\quad
\text{one derivative-null vector combination}.
\]

After transforming to active/null vector variables, the null combination is
purely auxiliary in the asymptotic exterior:

- no quadratic velocity;
- no linear velocity mixing;
- positive algebraic stiffness.

After eliminating \(Q\), the remaining \((W,U)\) kinetic determinant is
strictly negative for sufficiently large finite \(r\).

Therefore the benchmark contains a linear odd-sector ghost in that asymptotic
open region.

This is a technical result of the direct quadratic calculation.  Novelty
priority remains unclaimed pending a broader literature review.

See:

- \`notes/direct-two-vector-odd-expansion.md\`
- \`notes/direct-asymptotic-odd-ghost.md\`


## Class-II / NLQT gate update

The auxiliary derivative-mixing failure found in the two-vector model is not
present in pure-metric Class-II/GQTG or NLQT theories.  However, a stronger
gate is needed.

### Local analytic Class-II / GQTG

The \(n=0\) even Class-II family reduces to four-dimensional generalized
quasi-topological gravity, including Einsteinian cubic gravity at cubic
order.

These theories have the known reduced-spectrum / strong-coupling problem:
their linearized equations degenerate on maximally symmetric and highly
symmetric backgrounds relative to generic backgrounds.

For use as a complete nonperturbative singularity-resolution theory, this
violates the repository's principal-rank criterion.

In addition, the repository's all-order spherical scaling shows that every
finite analytic curvature order vanishes as \(r^3\) at a regular de
Sitter-type core.  A nonzero mass therefore requires a nonuniform infinite
resummation.

**Status:** reject as the full completion; retain as EFT/polynomial building
blocks.

### Nonlocal QTG

The nonlocal completion adds a quadratic \(\hat{\mathcal E}\mathcal F
\hat{\mathcal E}\) term chosen so the linearized derivative order does not
drop on symmetric backgrounds.

For zero-free entire form factors, the source proves no additional poles on
maximally symmetric backgrounds and on the spherically symmetric perturbation
subspace of spherically symmetric vacuum backgrounds.

Two project-specific gates remain:

1. the target four-dimensional QT base action is nonpolynomial and must itself
   pass the covariant-action differentiability test;
2. generic nonspherical odd/even perturbations of the regular black hole are
   not covered by the clean self-adjoint factorization used in the source.

**Status:** leading candidate, but not yet principal-safe verified in 4D.

See \`notes/principal-gate-classII-nlqt.md\`.


## NLQT zero-kernel / kinetic / core status

Current verdict:

- **regular background core:** PASS;
- **zero-kernel:** PASS only on the source-proven maximally symmetric and
  spherical-perturbation subspaces;
- **healthy flat/maximally-symmetric spectrum:** PASS;
- **generic nonspherical RBH zero-kernel:** OPEN;
- **generic nonspherical RBH kinetic sign:** OPEN;
- **fluctuation-operator regularity at the core:** OPEN for a generic 4D
  completion.

A four-dimensional completion ambiguity prevents inference of the odd
quadratic operator from the spherical response \(h(\psi)\) alone.  Terms such
as \(({}^\star RR)^2\) leave the static spherical background unchanged while
modifying the odd quadratic action.

In addition, the NLQT operator \(\hat{\mathcal D}\) inherits the curvature
Hessian of the local QT base action.  Therefore the previously studied
nondifferentiable rational 4D base lift is not rescued automatically by the
nonlocal form factor.

**Next prerequisite:** specify a differentiable off-spherical 4D QT base
action before computing the full NLQT odd operator.


## 4D base-action search update

The latest search narrows the 4D NLQT base options further.

### Normalized Cotton/Weyl NPG representatives

Recent 4D non-polynomial gravities admit exact regular black holes and even
non-conformally-flat vacuum geometries.  This helps away from conformally-flat
regions.

However, a smooth spherical center has

\[
C_{\mu\nu\rho\sigma}=O(r^2),
\qquad
C_{\alpha\beta\gamma}^{\rm Cotton}=O(r),
\]

so normalized direction tensors schematically of the form

\[
u\sim\frac{CC}{C^2}
\]

have generic first/second variations scaling like

\[
\delta u\sim r^{-1},
\qquad
\delta^2u\sim r^{-2}.
\]

Thus the non-conformally-flat-vacuum construction does not automatically pass
the regular-core Hessian gate.

### Analytic 4D GQTG base

Polynomial GQTG densities avoid the normalized-projector problem order by
order.  However, the genuine 4D family starts at cubic curvature order.

Its Schwarzschild asymptotic corrections begin at

\[
\delta f_3=O(r^{-6}),
\]

whereas exact Hayward begins at

\[
\delta f_H=O(r^{-4}).
\]

Therefore exact Hayward cannot be inherited from a normally convergent
analytic 4D GQTG tower.

**Design decision:** a principal-safe 4D NLQT program should stop requiring
the exact Hayward metric and instead search for a regular screening solution
with GQTG-compatible asymptotics.


## Explicit 2025 NPQT representative pole

The displayed cubic NPQT density has the rational term

\[
\frac92
\frac{W_3Z_3W_2}
{(WZZ)W_2-2W_3Z_2}.
\]

A direct Lorentzian algebraic-curvature construction gives a point with
denominator zero and numerator nonzero.  The same result is reproduced by
direct tensor index contraction.

Therefore the **displayed representative** fails the open-neighborhood
covariant-action gate.

This is narrower than rejecting the entire NPQT spherical theory:
alternative covariant representatives remain logically possible and are now
an explicit design target.


## Dynamical-formation benchmark update

The project now has an external astrophysical benchmark chain for the
dynamical-formation criterion:

\[
\text{cosmological inflow}
\to
\text{accreting SMS}
\to
\text{GRI}
\to
\text{post-GRI fate}
\to
\text{strong-field endpoint}.
\]

Published inputs include:

- Chon et al. (2026): realistic heavy-seed cosmological environment;
- Saio et al. (2024): GR radial-instability threshold and compactness;
- Nagele & Umeda (2024): nonlinear collapse/pulsation/explosion fate for
  accreting Pop III SMS models;
- Shibata & Shapiro (2002) and Fujibayashi et al. (2025): rotating
  strong-field GR endpoint benchmarks.

This does **not** turn any current candidate's dynamical-formation entry into
PASS.  It defines the calculation required to change that entry.

For nonlocal QTG in particular, the remaining task is still to produce a
well-defined four-dimensional principal-safe evolution system before it can be
inserted into this collapse benchmark.
