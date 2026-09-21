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


## NLQT prerequisite: fix the 4D off-spherical completion

The source-proven zero-kernel result does not determine generic nonspherical
regular-black-hole perturbations in four dimensions.

Reason:

- the spherical response \(h(\psi)\) does not uniquely determine the odd
  quadratic action;
- a covariant deformation such as \(({}^\star RR)^2\) can leave the entire
  spherical background unchanged while modifying odd perturbations;
- \(\hat{\mathcal D}\) inherits the curvature Hessian of the chosen QT base
  action.

Therefore the next NLQT calculation must proceed in this order:

1. select a differentiable full 4D QT base action;
2. verify its curvature Hessian on the regular core;
3. derive \(\hat{\mathcal D}_{\rm odd}\);
4. derive \(\mathcal D_{\rm odd}\);
5. compute \(\Delta\mathcal D_{\rm odd}\);
6. test the complete nonlocal odd operator for zero kernel, kinetic sign,
   hyperbolicity and core regularity.

Until step 1 is resolved, the generic odd problem is underdetermined rather
than merely technically incomplete.


## GQTG-compatible regular target

The 4D NLQT branch should no longer require exact Hayward asymptotics.

Reason:

- bare normalized Cotton/Weyl projectors are nondifferentiable at a smooth core, while the full NPQT rational densities still require an explicit C²-extension test;
- analytic 4D GQTG bases are differentiable order by order but their first
  genuine correction is cubic;
- cubic GQTG changes Schwarzschild at \(O(r^{-6})\), while Hayward changes it
  already at \(O(r^{-4})\).

### New construction target

Find a static spherical regular metric satisfying

\[
f(r)
=
1-\frac{2M}{r}
+O(r^{-6})
\]

at large \(r\), together with a smooth finite-curvature core and a screened
curvature response.

Then:

1. inverse-match an analytic 4D GQTG infinite tower to that solution;
2. test convergence and the resummed curvature Hessian;
3. use the resulting differentiable base in the NLQT completion;
4. perform the generic odd/even zero-kernel and kinetic tests.

The screening mechanism, not the exact Hayward metric, is now the invariant
design target.


## NPQT full-density differentiability refinement

The normalized-projector warning has been narrowed.

The 2025 four-dimensional NPQT densities contain high-degree curvature
numerators multiplying their common rational denominator.  Therefore the
complete density can have harmless \(O(\delta R^3)\) fixed-ray scaling even
though the normalized directional building blocks themselves are singular.

The unresolved gate is now:

1. factor the full rational numerator/denominator near a maximally symmetric
   core;
2. determine the full denominator-zero set in algebraic curvature space;
3. test whether each numerator vanishes with sufficient multiplicity on that
   set;
4. construct, or rule out, a C² covariant extension;
5. only then use that NPQT density as the 4D base of NLQT.

This is a more precise target than declaring all non-polynomial/projector
bases unsuitable.


## Chon et al. heavy-seed formation benchmark

The 2026 Nature simulation by Chon et al. provides a realistic external
formation/accretion environment for \(10^6M_\odot\)-class heavy seeds.

This is useful for Phase 4, but only with a clean scale separation.

The AREPO calculation follows cosmological collapse, protostellar growth,
Bondi-scale gas capture, radiation feedback and host-galaxy assembly, while
the actual strong-field interior is represented by sink/BH particles.

Published subgrid interfaces include:

- stellar-sink \(\rightarrow\) BH-particle conversion;
- unresolved accretion inside a sink/Bondi radius;
- a fixed \(\epsilon_r=0.1\) slim-disk luminosity prescription;
- no kinetic jet/wind feedback;
- BH particle mergers below 10 physical pc.

The high-resolution accretion follow-up reaches about 500 au.  For a
\(10^6M_\odot\) BH this is roughly \(2.5\times10^4\) Schwarzschild radii.

### Project use

Treat the cosmological simulation as an **outer-boundary generator**, not as a
direct test of singularity resolution.

The minimum handoff is

\[
\{M,\dot M,\rho,T,j\}_{r_{\rm sink}}
\longrightarrow
\text{screened strong-field model}
\longrightarrow
\{M_{\rm grav},L_{\rm bol},{\rm SED},\epsilon_{\rm rad},
\dot M_{\rm wind},\dot E_{\rm kin}\}.
\]

The first practical experiment does not require modifying AREPO:

1. obtain a heavy-seed \(M(t),\dot M(t)\) history from the published run;
2. feed it into the screened-BH inner model;
3. replace the fixed slim-disk luminosity closure;
4. compare growth and ionizing feedback.

See \`notes/cosmological-heavy-seed-interface.md\`.


## SMS GRI / post-GRI formation gate

The Chon et al. heavy-seed benchmark exposes an earlier interface than
post-BH accretion: the fate of the accreting supermassive star itself.

Published GR work now supplies two distinct gates.

### Gate 1 — onset of relativistic radial instability

Use the Saio et al. GR benchmark

\[
\omega_0^2(M,\dot M_*)=0
\]

to define

\[
M_{\rm crit,GR}(\dot M_*).
\]

The source models encounter the instability at very low compactness,

\[
2GM/(Rc^2)\sim10^{-5}-10^{-4}.
\]

Therefore a genuinely high-curvature screening theory is expected to leave
this onset approximately GR-like.

Primary observable:

\[
\Delta M_{\rm crit}
=
M_{\rm crit,screened}
-
M_{\rm crit,GR}.
\]

A large shift would imply that the theory modifies weak/post-Newtonian stellar
gravity and would require a separate low-curvature consistency analysis.

### Gate 2 — nonlinear fate after GRI

GRI does not imply immediate BH formation.

Nagele & Umeda (2024) find, for Pop III constant-accretion models:

- \(0.1M_\odot/{\rm yr}\): collapse;
- \(1,10,50M_\odot/{\rm yr}\): pulsation;
- \(90,100M_\odot/{\rm yr}\): collapse;
- \(200M_\odot/{\rm yr}\): pulsation.

Thus the formation closure must be

\[
\text{SMS}
\rightarrow
\text{GRI}
\rightarrow
\{\text{collapse},\text{pulsation},\text{explosion}\},
\]

not simply

\[
\text{SMS}\rightarrow\text{BH particle}.
\]

### Spacetime-Screening target

The clean high-curvature test is to start from a GR branch that genuinely
collapses and ask whether, before a trapped/singular region forms, the
candidate theory produces:

- a screened finite-curvature core;
- a bounce;
- a delayed collapse that changes nuclear burning;
- or an instability/pathology of the physical principal operator.

Track

\[
\Delta t_{\rm collapse},
\qquad
\Delta E_{\rm nuc},
\qquad
\Delta M_{\rm eject},
\qquad
M_{\rm remnant}.
\]

See:

- \`notes/sms-gr-instability-formation-gate.md\`;
- \`notes/sms-post-gri-fate-gate.md\`;
- \`data/sms_gri_gr_benchmark.csv\`;
- \`data/sms_post_gri_fates.csv\`.
