# Spacetime Screening

**Spacetime Screening** is an exploratory research repository about whether black-hole singularities can be replaced by a high-curvature regime in which the effective gravitational response is screened, saturates, or changes phase.

The project starts from a simple question:

> What if increasing curvature does not make gravity arbitrarily stronger, but instead drives the effective gravitational description toward a screened or non-geometric regime?

A schematic target behavior is

\[
\mathcal{K} \uparrow
\quad\Longrightarrow\quad
G_{\mathrm{eff}} \downarrow
\quad\Longrightarrow\quad
\text{curvature growth is self-limited},
\]

where \(\mathcal{K}=R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}\) is a curvature invariant.

This repository does **not** claim a completed theory of quantum gravity. It is a workspace for turning the idea into precise models, deriving consistency conditions, comparing them with existing approaches, and identifying falsifiable consequences.

## Core hypothesis

The working hypothesis is that sufficiently high curvature may trigger one or both of the following:

1. **Gravitational screening:** the dimensionful effective Newton coupling decreases with the relevant invariant/RG scale.
2. **Spacetime phase change:** the metric description itself ceases to be the most useful set of variables and is replaced by another quantum phase, from which a semiclassical spacetime can later re-emerge.

A minimal effective picture is

\[
\text{GR regime}
\rightarrow
\text{screening regime}
\rightarrow
\text{finite-curvature or non-geometric core}.
\]

The distinction between these possibilities matters. A de Sitter-like regular core can remain geometrical. A genuinely Minkowski-like or non-geometric core may require a branch change or additional order parameter rather than a single smooth GR branch.

## What is established vs. what is speculative

### Established context

- Regular black-hole geometries can replace a curvature singularity with a finite-curvature core.
- Hayward's nonsingular black-hole model has a cosmological-constant-like small-radius core.
- In asymptotic-safety scenarios, the dimensionful Newton coupling can scale as \(G(k)\sim g_*/k^2\) near a non-Gaussian UV fixed point.
- Static regular black holes often introduce an inner/Cauchy horizon, whose stability is a serious constraint.
- Spacetime emergence from more fundamental quantum structure is an active research direction, especially in holography and quantum-information-inspired approaches.

### Working conjectures in this repository

- Screening may be best formulated as a covariant response to curvature invariants or a dynamically selected RG scale, not as an ad hoc \(G(r)\).
- A strictly regular center plus asymptotic GR can force qualitative changes in the effective gravitational response.
- A Minkowski-like core may require a phase/branch transition rather than a single-valued smooth curvature response.
- The physically relevant end state of collapse may be dynamical and non-geometric rather than a permanently static regular core.

These conjectures are research targets, not results.

## Current model target

The original minimal static-radial scalar screening ansatz has an ansatz-level
no-go under healthy canonical boundary conditions. The current target is
therefore a covariant constrained/degenerate scalar, auxiliary-vector, or
higher-curvature realization.

A schematic order-parameter action remains useful as intuition:

\[
S[g,\chi,\ldots]
=
\int d^4x\sqrt{-g}
\left[
\frac{F(\chi)}{16\pi G_N}R
-\frac12(\nabla\chi)^2
-V(\chi,\mathcal I)
+\mathcal L_{\rm higher\ curvature}
+\cdots
\right],
\]

with a covariant invariant \(\mathcal I\), such that

\[
F(\chi)\to 1
\quad\text{at low curvature},
\]

while at high curvature a new branch or condensate can drive

\[
G_{\rm eff}\sim \frac{G_N}{F(\chi)}
\]

downward without introducing ghosts, violating unitarity, or destroying the GR limit.

## Consistency requirements

A viable model should satisfy, at minimum:

- general covariance;
- a controlled GR + QFT low-energy limit;
- finite curvature invariants or a well-defined replacement of geometry;
- no propagating negative-norm degrees of freedom;
- well-posed dynamics;
- stress-energy consistency / Bianchi identities;
- acceptable black-hole thermodynamics;
- control of inner-horizon or mass-inflation instabilities;
- a path to dynamical collapse and evaporation, not only static metrics;
- observable consequences that distinguish the model from GR and other quantum-gravity scenarios.

## Repository map

- [THEORY.md](THEORY.md) — current mathematical skeleton and assumptions.
- [ROADMAP.md](ROADMAP.md) — concrete research program and milestones.
- [docs/motivation.md](docs/motivation.md) — physical motivation.
- [docs/screening-hypothesis.md](docs/screening-hypothesis.md) — screening mechanisms and covariant formulations.
- [docs/regular-black-holes.md](docs/regular-black-holes.md) — regular-core geometry and inner-horizon issues.
- [docs/spacetime-phase-transition.md](docs/spacetime-phase-transition.md) — branch changes and non-geometric phases.
- [docs/open-problems.md](docs/open-problems.md) — failure modes and unresolved questions.
- [docs/principal-safe-screening.md](docs/principal-safe-screening.md) — upgraded acceptance criteria for background, constraints, and physical characteristics.
- [notes/derivations.md](notes/derivations.md) — derivations and toy calculations.
- [notes/effective-stress-energy.md](notes/effective-stress-energy.md) — Hayward effective density, pressures, conservation, and energy conditions.
- [notes/scalar-tensor-no-go.md](notes/scalar-tensor-no-go.md) — why the simplest static radial scalar realization fails.
- [notes/vector-hair-benchmark.md](notes/vector-hair-benchmark.md) — exact action-level Hayward-type benchmark and extremality/curvature tradeoff.
- [notes/vector-constraint-analysis.md](notes/vector-constraint-analysis.md) — radial stability, absent asymptotic vector quadratic action, principal-symbol degeneracy, and regularity sensitivity.
- [notes/extremal-near-horizon.md](notes/extremal-near-horizon.md) — AdS2 x S2 extremal throat and Maxwell-like horizon stress.
- [notes/aretakis-test-scalar.md](notes/aretakis-test-scalar.md) — explicit s-wave test-field Aretakis conserved quantity and derivative growth.
- [notes/odd-parity-vector-auxiliary.md](notes/odd-parity-vector-auxiliary.md) — axial vector perturbations are algebraic auxiliaries and become degenerate at the endpoints.
- [notes/generalized-proca-mapping.md](notes/generalized-proca-mapping.md) — mapping to quartic generalized Proca and the known odd-mode instability warning.
- [notes/tensor-principal-cone.md](notes/tensor-principal-cone.md) — radial pure-TT characteristic cone and the hidden Schwarzschild geometry.
- [notes/pure-gravity-qtg-benchmark.md](notes/pure-gravity-qtg-benchmark.md) — intrinsic curvature screening in four-dimensional nonpolynomial quasitopological gravity.
- [src/](src/) — reproducible symbolic/numerical code.

## Starting references

1. S. A. Hayward, *Formation and Evaporation of Nonsingular Black Holes*, Phys. Rev. Lett. **96**, 031103 (2006). DOI: https://doi.org/10.1103/PhysRevLett.96.031103
2. M. Reuter and F. Saueressig, *The Asymptotic Safety Scenario in Quantum Gravity*, Living Rev. Relativity. https://link.springer.com/article/10.12942/lrr-2006-5
3. F. Di Filippo, I. Kolář, and D. Kubizňák, *Inner-extremal regular black holes from pure gravity*, Phys. Rev. D **111**, L041505 (2025). DOI: https://doi.org/10.1103/PhysRevD.111.L041505
4. M. Van Raamsdonk, *Building up spacetime with quantum entanglement*, Gen. Rel. Grav. **42**, 2323–2329 (2010). arXiv:1005.3035
5. K. Giesel, H. Liu, P. Singh, S. Weigl, *Regular black holes and their relationship to polymerized models and mimetic gravity*, Phys. Rev. D **111**, 064064 (2025). DOI: https://doi.org/10.1103/PhysRevD.111.064064
6. A. Eichhorn, P. G. S. Fernandes, *Regular black holes without mass-inflation instability and gravastars from modified gravity*, Phys. Rev. D **113**, L081501 (2026). DOI: https://doi.org/10.1103/nqz2-88zf

## License

- **Code**: Apache License 2.0 — see [LICENSE](LICENSE).
- **Research text, documentation, equations, and original figures**: Creative Commons Attribution 4.0 International — see [LICENSE-DOCS](LICENSE-DOCS).

Unless a file states otherwise, this scope applies by file type.

## Status

Early-stage research notebook. Expect assumptions to change as consistency checks become stricter.
