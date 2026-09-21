# Research Roadmap

The goal is to turn the spacetime-screening idea from a qualitative picture into a sequence of falsifiable mathematical models.

## Phase 0 — Definitions

- Define precisely what "screening" means.
- Separate the dimensionful \(G_{\rm eff}\) from dimensionless interaction strengths.
- Choose covariant diagnostics: curvature invariants, tidal eigenvalues, effective-action coefficients, and/or RG observables.
- Specify what is meant by a geometric versus non-geometric state.

**Exit condition:** every central claim can be stated without coordinate-dependent language.

## Phase 1 — Static spherical toy models

Study

\[
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2.
\]

Tasks:

- reproduce Schwarzschild and Hayward limits;
- classify small-\(r\) behavior required for finite curvature;
- derive conditions for de Sitter and Minkowski cores;
- map horizon structure as a function of model parameters;
- calculate surface gravities and Hawking temperatures.

**Exit condition:** a symbolic notebook verifies curvature invariants and horizon conditions.

## Phase 2 — Covariant action

**Current benchmark transition:** the auxiliary-vector model is retained as a
counterexample showing that background regularity is insufficient.  The active
v2 benchmark is pure-gravity quasitopological screening, followed by its
nonlocal completion.

Replace metric engineering with an action.

Candidate classes:

- extended mimetic / degenerate scalar-tensor models;
- auxiliary-vector / generalized Proca-type models;
- higher-curvature / quasitopological actions;
- nonlocal ghost-free form factors;
- RG-improved effective actions only where the scale identification is derived consistently.

Current status:

- a minimal static radial canonical (F(\chi)R) model has an ansatz-level no-go;
- a published two-vector action provides an exact Hayward-type benchmark;
- the next task is to analyze the propagating degrees of freedom and stability of an action-level realization rather than invent another metric ansatz.

Checks:

- Bianchi identities;
- stress-energy conservation;
- degrees of freedom;
- ghost/gradient stability;
- strong-coupling scale.

**Exit condition:** at least one action produces the target solution without ad hoc coordinate dependence.

## Phase 3 — Linear stability

Perturb the background,

\[
g_{\mu\nu}=\bar g_{\mu\nu}+h_{\mu\nu},
\qquad
\chi=\bar\chi+\delta\chi.
\]

Analyze:

- tensor/vector/scalar sectors;
- signs of kinetic terms;
- characteristic speeds;
- quasinormal modes;
- inner-horizon blueshift.

**Exit condition:** no immediately fatal linear instability in the intended regime.

## Phase 4 — Dynamical collapse

Static regular metrics are insufficient. Simulate spherical collapse from ordinary initial data and determine whether the theory dynamically generates:

- an event or trapping horizon;
- a screening transition;
- a finite-curvature core or non-geometric phase;
- a bounce or remnant;
- an inner horizon and its stability properties.

**Exit condition:** the proposed core emerges from evolution rather than being imposed as a boundary condition.

## Phase 5 — Semiclassical evaporation

Add quantum-field backreaction at a controlled approximation level.

Questions:

- Does \(T_H\) reach a maximum and then decrease?
- Is there a remnant, bounce, or complete evaporation?
- Does the information problem admit a consistent interpretation?
- Does the effective theory remain valid near the endpoint?

**Exit condition:** a causal diagram and energy budget exist for the complete life cycle.

## Phase 6 — Non-geometric completion

Only if the geometric model forces a branch pathology or inconsistent core:

- introduce a microscopic state space;
- define a geometric subspace or coarse-graining map;
- derive when metric variables become valid;
- recover Lorentzian causal structure and semiclassical QFT.

This is the most speculative phase.

## Phase 7 — Phenomenology

Search for robust signatures:

- ringdown deviations;
- echo-like structures only if produced by a well-posed model;
- modified near-extremal thermodynamics;
- constraints from horizon-scale observations;
- primordial-black-hole remnants;
- gravitational-wave consistency tests.

Prefer predictions that are insensitive to arbitrary core parametrization.

## Near-term issues

1. Derive curvature invariants for a one-parameter screening family.
2. Prove the regular-center scaling conditions.
3. Compare the vector-hair benchmark with extended mimetic reconstruction and identify the smaller healthy field content.
4. Complete the l>=2 odd-parity quadratic action and test whether the radial
   pure-TT Schwarzschild principal cone survives auxiliary-field elimination.
5. Perform a full ADM/Dirac constraint count for the two-vector action.
6. Determine whether the tensor characteristic horizon at r=2M is a genuine
   graviton horizon and whether the core principal operator is singular.
7. Derive even-parity non-spherical perturbations and test for hidden kinetic
   degeneracy.
8. Analyze coupled metric-vector Aretakis quantities on the extremal throat.
9. Test whether the extremal branch avoids classical mass inflation without
   introducing semiclassical or strong-coupling instabilities.
10. Determine whether universal limiting curvature can coexist with
    extremality across arbitrary black-hole masses.
11. Reproduce the pure-gravity QTG Hayward characteristic relation and
    curvature susceptibility (completed).
12. Extract or reconstruct the nonlocal-QTG quadratic operator and test it on
    the regular black-hole background, not only flat/maximally symmetric
    space.
13. Check whether all tensor/scalar principal symbols remain bounded at the
    regular core and whether their characteristic horizons coincide with or
    differ from the metric horizon.
14. Revisit inner-horizon stability using the actual quasitopological
    equations rather than importing GR thin-shell arguments.
15. Use the vector benchmark failure as a permanent design constraint:
    background regularity without principal-symbol regularity is insufficient.


## Immediate v2 action-selection gate

Before computing any nonspherical principal symbol for a nonpolynomial
four-dimensional lift, require:

1. the action density is finite on the exact black-hole background;
2. its first curvature derivatives are finite there;
3. the Hessian needed for the quadratic action is finite;
4. no extraction of spherical directions relies on a \(0/0\), singular
   projector, or nondifferentiable square-root branch.

The representative 2026 rational lift currently fails this gate on the
single-function Hayward branch, despite having a perfectly finite spherical
reduction.

**Next target:** identify or construct a regular four-dimensional lift /
polynomial-infinite-tower / nonlocal completion before resuming the tensor
principal-symbol calculation.


## R4 differentiability gate: completed

The June-2026 first-order QTG-TNT candidate fails the full four-dimensional
action-selection gate:

\[
R_4
=
\sqrt{
\frac{2I_6}{3}
-
\frac{2I_{11}}{I_1}
}
\]

is not differentiable on the single-function branch \(R_4=0\), with generic
curvature derivatives scaling as

\[
\partial R_4\sim R_4^{-1},
\qquad
\partial^2R_4\sim R_4^{-3}.
\]

Even within TNT, the covariant square root reconstructs a signed linear
reduced perturbation as an absolute-value cusp.

The classification result shows that this is structurally tied to the
first-order/algebraic Class-I mechanism: analytic Riemann-only scalar actions
contain only even powers of \(R_4\).

### Next branch

Move to one of:

1. analytic Class-II QTG-TNT / generalized-QTG infinite towers, accepting a
   higher-order reduced equation;
2. a nonlocal entire-function completion with a regular curved-background
   quadratic operator;
3. a formulation with additional regular fundamental fields in which the
   signed reduced degree of freedom is not reconstructed through a curvature
   square root.

Immediate task:

\[
\boxed{
\text{Can analytic Class II reproduce limiting-curvature screening in 4D?}
}
\]

If not, prioritize extraction of the exact nonlocal-QTG black-hole quadratic
operator.


## P0 vector odd-sector status: direct failure established

Completed:

- direct \(l=2\) four-dimensional expansion of the original \(A-B\) action;
- direct full-\((t,r)\) principal metric-vector mixing;
- direct active/null vector basis;
- proof that the null vector combination has no velocity mixing and positive
  algebraic stiffness;
- local/canonical \(l=1\) reduction;
- algorithmic linearized-Einstein cross-check;
- asymptotic elimination of nondynamical \(Q\) and null \(V\);
- proof that
  \[
  \lim_{r\to\infty}
  r^5\det K_{\rm red}<0.
  \]

Thus the vector benchmark fails the physical-kinetic criterion in an
asymptotic exterior open region.

Remaining vector-model work is no longer required to decide viability.

Optional follow-up only:

1. complete the global-in-\(r\) Dirac rank map to identify every
   rank-changing surface;
2. finish the direct physical \(l\ge2\) tensor master equation to decide the
   separate hidden-Schwarzschild-cone claim;
3. convert the direct odd calculation into a concise publication-style
   derivation and broaden the literature search.

### Main research branch now

Return effort to candidate theories that may survive the principal-safe gate:

1. analytic Class-II / generalized-QTG infinite towers;
2. the exact nonlocal-QTG completion and its regular-BH fluctuation operator;
3. model-independent no-go / necessary-condition statements extracted from
   the failure catalogue.


## Post-vector gate decision

Applying the auxiliary-mixing and principal-rank gates gives:

### Local analytic Class-II / GQTG

- passes the "no auxiliary derivative mixing" test;
- remains useful as a polynomial/EFT control family;
- fails the full-completion gate because of the known reduced-spectrum /
  strong-coupling structure of local ECG/GQTG-like theories;
- any regular finite-curvature vacuum core requires a nonuniform infinite
  resummation beyond finite analytic truncations.

**Decision:** no longer the primary completion candidate.

### Nonlocal QTG

The source construction explicitly restores principal derivative order and
uses a zero-free entire form factor.

**Passes so far:**

- no two-vector-style auxiliary-hair failure;
- no derivative-order reduction on the symmetric backgrounds analyzed in the
  source;
- no extra propagator poles on maximally symmetric backgrounds for the
  zero-free entire choice;
- healthy SS perturbative/Birkhoff subspace.

**Next gates:**

1. specify a differentiable four-dimensional QT base action;
2. derive the generic odd-parity nonspherical regular-BH quadratic operator;
3. test whether the curved-background nonlocal operator remains zero-kernel
   and whether its physical kinetic/principal structure is finite at the
   horizon and core.

### Immediate next research target

\[
\boxed{
\text{NLQT odd-parity perturbations on the regular black-hole background}
}
\]

with the 4D base-action differentiability issue tracked separately.
