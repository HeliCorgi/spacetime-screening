# Spacetime Screening

**Spacetime Screening** is a research repository about a narrower question than
"can a regular black-hole metric be written down?":

> **Can quantum-gravity-motivated screening make black-hole curvature regular
> without hiding the singular behavior in physical propagation modes,
> constraints, or the four-dimensional action itself?**

The project began from the intuition

\[
\text{high curvature}
\rightarrow
\text{weaker effective response}
\rightarrow
\text{singularity avoidance},
\]

but the main research direction is now **principal safety**:

\[
\boxed{
\text{regular background}
\not\Rightarrow
\text{regular dynamics}.
}
\]

This repository does **not** claim a completed quantum-gravity theory.

## Current working definition of screening

For a symmetry-reduced curvature response

\[
\psi=\psi(s),
\]

define the dimensionless logarithmic response

\[
\boxed{
\mathscr S
=
\frac{d\ln\psi}{d\ln s}.
}
\]

For the Hayward/QTG response

\[
\psi(s)=\frac{s}{1+\ell^2s},
\]

one finds

\[
\mathscr S
=
\frac1{1+\ell^2s}
=
1-\ell^2\psi
\rightarrow0
\]

at high source scale.

The spherical response itself is mostly known physics. The repo's focus is
whether a theory realizing such screening also has a healthy **physical
quadratic/principal structure**.

## Main research criterion

A candidate is not considered to have resolved the singularity unless it
passes, at minimum,

\[
\boxed{
\begin{aligned}
&\text{bounded background curvature},\\
&\text{differentiable 4D action},\\
&\text{controlled constraint rank},\\
&\text{positive physical kinetic matrix},\\
&\text{finite, hyperbolic principal symbol},\\
&\text{nonzero strong-coupling scale},\\
&\text{dynamical formation from regular data}.
\end{aligned}
}
\]

See [docs/principal-safe-screening.md](docs/principal-safe-screening.md).

## Current strongest calculation candidates

These are **not priority claims**. See [NOVELTY.md](NOVELTY.md) for status and
scope.

### 1. Direct odd-sector ghost in the two-vector benchmark

The original Eichhorn-Fernandes \(A-B\) action has now been expanded directly
in four-dimensional odd harmonics.  No one-vector perturbation formalism is
needed for the core result.

For \(l=2\), after eliminating the nondynamical directions in a sufficiently
large finite asymptotic exterior region,

\[
\boxed{
\lim_{r\to\infty}
r^5\det K_{\rm red}
=
-
\frac{1152\pi^2}{25}
M\ell^4(16M^2+q^2)
<0.
}
\]

Therefore the reduced physical odd kinetic matrix has one positive and one
negative eigenvalue in that open region.

The derivative-null vector combination is separately shown to have

- no quadratic velocity;
- no linear velocity mixing;
- positive algebraic stiffness.

So that auxiliary direction does not remove the negative active mode.

Independent checks include:

- brute-force \(l=2\) four-dimensional curvature expansion;
- full-\((t,r)\) principal expansion;
- local linearized-Einstein derivation;
- \(l=1\) canonical constraint analysis;
- published generalized-Proca coefficients used only afterward as a
  cross-check.

**Technical status:** the asymptotic odd ghost is directly established within
the quadratic theory.  **Novelty priority is not claimed.**

See:

- [notes/direct-two-vector-odd-expansion.md](notes/direct-two-vector-odd-expansion.md)
- [notes/direct-asymptotic-odd-ghost.md](notes/direct-asymptotic-odd-ghost.md)
- [src/symbolic/direct_two_vector_odd_l2.py](src/symbolic/direct_two_vector_odd_l2.py)
- [src/symbolic/direct_odd_asymptotic_ghost.py](src/symbolic/direct_odd_asymptotic_ghost.py)

### 2. Hidden Schwarzschild tensor characteristic

The same odd quadratic-action coefficient block gives

\[
q_T=\frac{f-\Delta}{2f^2},
\]

with radial characteristic roots

\[
v_-=-f,
\qquad
v_+
=
f\frac{f+\Delta}{f-\Delta}.
\]

On the exact regular branch,

\[
\boxed{
f+\Delta
=
1-\frac{2M}{r}.
}
\]

Thus

\[
\boxed{
r_T=2M
}
\]

appears as a tensor characteristic horizon even though the regular background
metric is not on a horizon there.

At \(r=2M\),

\[
q_T>0,
\]

so this is not merely a kinetic-sign crossing.

See:

- [notes/tensor-principal-cone.md](notes/tensor-principal-cone.md)
- [notes/vector-odd-kinetic-analysis.md](notes/vector-odd-kinetic-analysis.md)
- [src/symbolic/vector_odd_tensor_reduction.py](src/symbolic/vector_odd_tensor_reduction.py)

### 3. Restricted scalar-tensor no-go

For a canonical static radial scalar with

\[
F(\chi)R,
\]

the one-function metric ansatz gives

\[
F''(r)
=
-8\pi G\,\chi'(r)^2\le0.
\]

Regular-center and asymptotically constant boundary conditions force the
localized scalar profile to be trivial.

This is a restricted ansatz-level result, not a general scalar-tensor no-hair
theorem.

See [notes/scalar-tensor-no-go.md](notes/scalar-tensor-no-go.md).

## Candidate models already stress-tested

### Two auxiliary vectors

**Background:** regular Hayward-type geometry.

**Problems found:** directly established asymptotic odd ghost, degenerate
vector/null sector, hidden Schwarzschild tensor characteristic candidate, and
an extremal test-field Aretakis channel.

### Nonpolynomial pure-gravity QTG

**Background:** excellent curvature-response saturation,

\[
\psi=\frac{s}{1+\ell^2s}.
\]

**Problem found:** the explicit rational four-dimensional lift used as a
representative construction is nondifferentiable on the single-function
branch in generic curvature directions.

### 2026 first-order QTG-TNT

**Background:** exact regular black-hole solutions and GR-like first-order
integrability.

**Problem found:** the covariant

\[
R_4
=
\sqrt{
\frac{2I_6}{3}
-
\frac{2I_{11}}{I_1}
}
\]

has a square-root cusp on the single-function branch and divergent curvature
derivatives. The source classification also implies that nontrivial
first-order Class-I QTG-TNT is structurally non-analytic.

### Regularized-Lovelock / Horndeski infinite tower

**Background:** regular known planar branch.

**Problem already known in the literature:** odd ghost/gradient instability
and an infinitely strongly-coupled even scalar mode on that branch.

See [docs/candidate-scorecard.md](docs/candidate-scorecard.md).

## Research priority

The present priority order is:

1. **P0 — archive the two-vector odd result as a completed failure test and
   finish the independent physical tensor-master reduction only if useful for
   the hidden-cone claim.**
2. **P1 — turn recurring failure mechanisms into model-independent
   principal-safety / no-go statements where possible.**
3. **P2 — local analytic Class-II/GQTG is retained only as an EFT/control
   family; the main surviving completion candidate is nonlocal QTG.**

See [ROADMAP.md](ROADMAP.md).

## Novelty policy

The repository explicitly separates:

- **KNOWN**
- **REPRODUCED HERE**
- **NEW CALCULATION CANDIDATE**
- **SYNTHESIS / CRITERION**
- **CONJECTURE**

in [NOVELTY.md](NOVELTY.md).

No "first", "new theorem", or similar priority claim should be made until the
derivation is complete and a targeted literature search has been documented.

## Repository map

Core documents:

- [NOVELTY.md](NOVELTY.md) — novelty/status map and priority-claim policy.
- [THEORY.md](THEORY.md) — current mathematical skeleton.
- [ROADMAP.md](ROADMAP.md) — research priorities and open calculations.
- [docs/principal-safe-screening.md](docs/principal-safe-screening.md) —
  acceptance criteria.
- [docs/candidate-scorecard.md](docs/candidate-scorecard.md) — candidate
  comparison.
- [docs/open-problems.md](docs/open-problems.md) — unresolved failure modes.

Selected calculations:

- [notes/vector-odd-kinetic-analysis.md](notes/vector-odd-kinetic-analysis.md)
- [notes/tensor-principal-cone.md](notes/tensor-principal-cone.md)
- [notes/scalar-tensor-no-go.md](notes/scalar-tensor-no-go.md)
- [notes/covariant-lift-degeneracy.md](notes/covariant-lift-degeneracy.md)
- [notes/r4-differentiability.md](notes/r4-differentiability.md)
- [notes/principal-gate-classII-nlqt.md](notes/principal-gate-classII-nlqt.md) — new-gate comparison of analytic Class-II/GQTG and nonlocal QTG

Reproducible symbolic checks live under [src/symbolic/](src/symbolic/).

## Reproducibility

Install dependencies:

\`\`\`bash
python -m pip install -r requirements.txt
\`\`\`

Run all symbolic checks:

\`\`\`bash
for f in src/symbolic/*.py; do
  echo "==> $f"
  python "$f" || exit 1
done
\`\`\`

GitHub Actions also runs the symbolic suite on pushes and pull requests once
the workflow is enabled in this repository.

## Starting references

1. S. A. Hayward, *Formation and Evaporation of Nonsingular Black Holes*,
   Phys. Rev. Lett. **96**, 031103 (2006).
2. R. Kase, M. Minamitsuji, S. Tsujikawa, Y.-L. Zhang,
   *Black hole perturbations in vector-tensor theories: The odd-mode
   analysis*, JCAP **02** (2018) 048, arXiv:1801.01787.
3. F. Di Filippo, I. Kolář, D. Kubizňák,
   *Inner-extremal regular black holes from pure gravity*,
   Phys. Rev. D **111**, L041505 (2025).
4. A. Eichhorn, P. G. S. Fernandes,
   *Regular black holes without mass-inflation instability and gravastars
   from modified gravity*, Phys. Rev. D **113**, L081501 (2026).
5. J. Borissova, R. Carballo-Rubio,
   *Regular black holes from pure gravity in four dimensions*,
   Phys. Rev. D **113**, 124004 (2026).
6. A. Colléaux, I. Kolář, T. Málek,
   *Quasi-topological gravity for 4-dimensional Taub-NUT, near-horizon
   extreme Kerr, and swirling symmetries*, arXiv:2606.17784.

## License

- **Code:** Apache License 2.0 — see [LICENSE](LICENSE).
- **Research text, documentation, equations, and original figures:** CC BY
  4.0 — see [LICENSE-DOCS](LICENSE-DOCS).

## Status

Early-stage research repository. The project is deliberately adversarial:
candidate models are expected to fail tests, and those failures are treated as
useful results.


## NLQT status: restricted PASS, generic 4D sector still open

The current leading candidate, nonlocal QTG, passes several important gates:

- exact regular spherical background;
- restored derivative order relative to local QT;
- zero-free form-factor proof on maximally symmetric backgrounds;
- zero-kernel proof on the spherical perturbation subspace;
- ordinary massless-graviton pole structure on flat space.

But the repository does **not** presently claim generic four-dimensional
principal safety.

Two obstructions remain:

1. the spherical response does not uniquely determine the off-spherical
   quadratic action;
2. the nonlocal operator inherits the differentiability of the chosen local
   QT base action.

Therefore the next NLQT task starts by choosing a differentiable full 4D QT
base action, not merely by specifying the Hayward response \(h(\psi)\).

See:

- [notes/principal-gate-classII-nlqt.md](notes/principal-gate-classII-nlqt.md)
- [notes/ss-completion-ambiguity.md](notes/ss-completion-ambiguity.md)
- [notes/nlqt-base-hessian-inheritance.md](notes/nlqt-base-hessian-inheritance.md)
- [notes/nlqt-zero-kernel-kinetic-core-status.md](notes/nlqt-zero-kernel-kinetic-core-status.md)
