# Chronology / Hadamard / semiclassical gravity: phase-one audit

2026-10-08 JST. Audited main snapshot: `1ff10c4453f52f9f8f8c2c835a52812ce7faac90`.

## 1. Scope and classification

The user's target is the existence or non-existence of a chronology-violating spacetime with a positive Hadamard quantum state, finite renormalized stress-energy, specified finite energy, and a self-consistent semiclassical Einstein equation. This is not the same as the repository's stronger operational past-signalling target.

**User labels:** A = existence proof; B = no-go theorem; C = not determined by the current formulation. These are NOT the existing repository A/B/C candidate labels.

**Overall: user-C.** There is no supplied global state–geometry pair satisfying all requested conditions, and no theorem covering every remaining geometry and matter theory. This is not a logical undecidability theorem. The fixed v10 product quotient and the existing ordinary scalar NUT model admit narrower Hadamard obstructions, described below. Their rejection must not be generalized to all CTC spacetimes.

All 314 tracked files were archived and indexed: 168 Python, 107 Markdown, one Lean file, and other evidence/infrastructure. All major research families were inventoried. Chronology geometry, v10/v11, state definitions, and the NUT obstruction received focused independent checks. This is not a claim that every equation in every historical branch has an independent proof or peer review.

## 2. The required logical chain

A complete candidate must specify a smooth time-oriented Lorentzian manifold, global identifications and boundary conditions, field equations, field algebra, positive state, and fixed renormalization prescription.

For an ordinary real scalar, a global distribution W must satisfy the Klein–Gordon equation in both arguments, positivity, Hermiticity, and the usual CCR in sufficiently small globally hyperbolic neighbourhoods. In each such convex normal neighbourhood U, W minus the local Hadamard parametrix must be smooth. Do not assume a globally defined unique advanced-minus-retarded propagator on a CTC spacetime.

The same metric that defines W must satisfy the renormalized semiclassical equation, including fixed cosmological, Newton, and curvature-squared counterterms. Defining a required source by G/(8 pi G_N), or importing an RSET from a different background, is not such a solution.

Local finite density, finite classical wave-packet energy, finite Killing energy, and finite apparatus-inclusive total energy are different. A constant density on a noncompact product core does not establish finite total energy. Formation from a chronal initial region and stability under perturbations are additional questions, not silently imposed definitions of bare existence.

## 3. What reproduces in v10

The four-dimensional curvature of

```math
ds^2=-dt^2+dx^2+r_0^2d\Omega_2^2
```

and the nonlinear root for the printed Popov stress model reproduce. The code correctly names TWO support fields: a conformal massless scalar and a very massive nonconformal scalar, plus classical electromagnetism. The parameters are xi=-10000 and m^2=1000 in Planck units. The root is r0=101.4933616691... and Q^2=20601.82206196....

However, the implemented stress combines rounded coefficients 0.00310 and -0.00171 with a truncated inverse-mass expansion. Popov's integral formulas on the constant product and the printed approximations are not interchangeable. A roughly 10^-66 numerical residual is a residual of the supplied truncated equations, not a 60-digit error bound for the exact RSET. The r approximately 101.49 example already appears in Popov's paper.

The nonzero two-variable Jacobian concerns (r,Q^2) in this local model. A functional implicit-function theorem for the full state-dependent semiclassical problem also needs a defined differentiable stress functional, admissible states, quantitative error bounds, and control of flux/time-dependent/nonspherical components. Retuning Q^2 changes the fixed-charge problem if charge was part of the CBSSL input data.

The classical constant configurations chi=+v and chi=-v have zero signal stress in the stated double-well potential. Local reset gradients, preparation work, detector stress, and quantum corrections do not thereby vanish. The quoted D_past=erf(3/sqrt(2)) comes from the stipulated Gaussian receiver noise, not a constructed global QFT detector model.

Source: [Popov](https://arxiv.org/abs/1809.06202); [v10 note](cbssl-rset-core-v10.md).

## 4. What v11 does and does not establish

For a flat helical quotient with deck vector k=(-Delta,L), a^2=L^2-Delta^2>0, the periodic massless scalar image calculation reproduces

```math
\Delta\langle\phi^2\rangle=\frac1{12a^2},\qquad
\Delta T_{\mu\nu}=\frac{\pi^2}{90a^4}(\eta_{\mu\nu}-4e_\mu e_\nu),\quad e=k/a.
```

Its trace, invariant contraction, and p-series controls reproduce. Its divergence as a approaches zero from the spacelike side is valid for this construction.

This is NOT a proof that no state exists on every timelike quotient. Several v11 failure/domain classifications are asserted descriptions of the tested image prescription. The verifier does not construct or reject every possible global state. A parameter boundary in a family is not automatically a chronology horizon inside each fixed timelike member. An eternal timelike quotient need not have the initial development assumed by the compact-horizon KRW theorem. Fewster–Higuchi construct F-local algebras on some timelike translation quotients; algebra existence alone is not a positive Hadamard state or a semiclassical solution.

The v11 flat control is not the global two-field RSET on the curved v10 product.

For the axial MP test, K=-Delta partial_T+alpha partial_phi has the correctly calculated norm

```math
K^2=U^2\rho^2\alpha^2-\Delta^2/U^2.
```

But its zero is not proved to be a chronology horizon or a null image geodesic. With the ordinary angular coordinate modulo 2 pi and alpha=2 pi, the finite map is just a time translation. Delta nonzero then produces CTCs even where this helical K has positive norm. Unwrapping the angle changes the manifold and requires its own specification. A null Killing orbit is not automatically geodesic: nabla_K K=-grad(K^2)/2. Actual image singularities require actual null geodesics and transport amplitudes, not substituting a local Killing norm into the flat Casimir formula.

The actual Schein–Aichelburg RN sewing, the v3 direct MP handle, and this axial quotient are three different constructions.

Sources: [v11](cbssl-global-rset-v11.md), [Fewster–Higuchi](https://arxiv.org/abs/gr-qc/9508051), [SA](https://arxiv.org/abs/gr-qc/9606069).

## 5. A separate Hadamard obstruction for the actual fixed v10 quotient

The following is an explicit audit application of the established propagation-of-singularities theorem. It is not an existing v11 assertion, a new fundamental theorem, a Lean certificate, or an independently peer-reviewed result.

Assume the global product and identification stated in v10:

```math
\widetilde M=\mathbb R^{1,1}\times S^2_r,\quad
\gamma(t,x,\Omega)=(t-\Delta,x+L,\Omega),\quad L=100r,\quad\Delta=2L.
```

**Claim:** no global distributional bisolution of an ordinary normally hyperbolic Klein–Gordon equation can be locally Hadamard everywhere on this exact quotient.

**Proof.** Set T=sqrt(Delta^2-L^2)=100 sqrt(3) r and boost to

```math
\tau=(\Delta t+Lx)/T,\qquad y=(Lt+\Delta x)/T.
```

The metric is -d tau^2+d y^2+r^2 d Omega_2^2 and the identification is tau modulo T. Thus M=S^1_time(T) times R_y times S^2_r.

At fixed y, follow a null geodesic around a great circle: tau=s, theta=pi/2, phi=s/r. Each spatial revolution takes P=2 pi r. Since P/T=pi/(50 sqrt(3)) is irrational, there are integers m_j,n_j with nonzero epsilon_j=m_j P-n_j T tending to zero. The endpoint q_j after m_j revolutions is distinct from the starting point p, has the same spatial coordinates, and approaches p in the quotient. Within a sufficiently small convex normal neighbourhood it is timelike, not null, separated from p. Globally it is joined to p by the long null geodesic just constructed.

Local Hadamard form forces (p,k;p,-k) into WF(W) for the appropriate nonzero future null covector k along this ray. Propagating in the first argument along the null bicharacteristic gives (q_j,k_j;p,-k) in WF(W). Global hyperbolicity is not needed for this microlocal propagation in the region with nonzero first covector. But for large j both points lie in one fixed small normal neighbourhood, where local Hadamard form is smooth at this timelike separated pair. Contradiction. QED.

Smooth mass and curvature-coupling terms do not change the principal null characteristics. Positivity, stationarity, Gaussianity, finite energy, and CBSSL are not needed for the obstruction. Keeping the exact ratios while retuning r or Q does not remove it.

**Scope:** this rejects the exact global product quotient with ordinary local KG/Hadamard requirements (user-B). It does NOT reject an arbitrary finite core embedded in another spacetime, an arbitrary backreacted non-product geometry, all other time quotients, or a theory with different local equations. No stability theorem for this obstruction under arbitrary metric perturbations is claimed.

Sources for the method: [KRW, especially section 6](https://arxiv.org/abs/gr-qc/9603012); [Khavkine–Moretti](https://arxiv.org/abs/1412.5945).

## 6. Existing restricted no-go results and genuine open conditions

The existing [NUT null-return note](nut-null-return-obstruction.md) has a separate, stronger-than-finite-mode obstruction for its specified scalar model. Both the integer interval certificate and the independent four-dimensional Hamiltonian calculation were rerun. The return path remains in x>12; endpoint radial covectors have opposite nonzero signs. Propagation produces an off-diagonal cotangent pair at the spacetime diagonal, contradicting local Hadamard form. This is not a universal full-string result.

The [smooth RN trace obstruction](charged-source-handle-v3.md) is valid for the fixed profile, finite neutral free massless conformal matter, finite local counterterms, and no extra boundary/source contributions: the required r^-4 trace cannot be supplied by the r^-6 anomaly. Changing lapse, mass, coupling, charged interactions, or sources changes the problem. One KMS temperature failing at two nonextremal RN horizons is not a theorem against all non-equilibrium states.

KRW excludes a Hadamard extension across base points of a compactly generated Cauchy horizon from its initially globally hyperbolic region. It does not require every RSET component to diverge on every approach curve. Finite components or special cancellations do not restore Hadamard form. For actual SA, the partial Cauchy surface, full generators, compact generation, and smooth treatment of shells remain to be established before asserting the compact-horizon theorem. Thin-shell distributional Einstein equations are not automatically a smooth curvature-squared renormalized QFT.

Noncompact generation, an eternal CTC region, or changed boundary conditions removes a theorem's hypothesis, not the need for a positive local-Hadamard global state. Conversely KRW itself identifies exceptional refocusing spacetimes: closed null geodesics alone are not an unconditional no-go.

CBSSL's lexicographic selection additionally needs a nonempty admissible state set, an attained minimum, continuum/type-III-compatible entropy/fidelity definitions, fixed renormalization, cut independence, and covariant conservation. A vanishing weighted residual constrains only the region where its weight is positive. A finite-dimensional fixed-point construction cannot fill these gaps.

The [B1 VCDM candidate](auxiliary-volume-b1.md) is a separate bounce model. Its specified potential, homogeneous/Bianchi I solutions, and substitutions into published perturbation coefficients are useful classical checks. The displayed complete spacetimes have a global time t, not CTCs. They do not supply a Hadamard state or RSET for the chronology programme. Curvature-screening, vector stability, SMS/GRI controls, architecture validation, and the standalone Lean causal-order lemma likewise do not replace the missing global state–geometry pair.

## 7. Reproduction and implementation issues

Pinned Actions run [37701712376](https://github.com/HeliCorgi/spacetime-screening/actions/runs/37701712376) completed successfully: all 150 root Python targets on both Python 3.11 and 3.12 in four shards each; selector tests; Lean 4.19.0 conditional causal-order lemmas; and source archive. B1's two entry points are included among the 150. This is not a claim that every one of the 168 Python files was separately executed as a standalone script.

Local Python 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0 also reproduced v10 forward, v11 forward plus evidence verifier, NUT geometry/certificate, B1 entries, and all three architecture test suites.

Two bugs were reproduced:

1. `cbssl_rset_core_v10.py` line 238 writes a literal backslash-n after JSON. Its documented forward-to-`--evidence` command fails with JSONDecodeError even though the standalone root-CI target passes.
2. `cbssl_global_rset_v11.py` constructs V10_R0 and V10_Q2 with mp.mpf at module import, before workdps(80). Lost digits cannot be recovered inside the later high-precision context.

A local software-only patch and regression test were executed successfully: real newline output, string constants parsed inside workdps, JSON round trips and source-hash evidence verification for v10/v11, plus an import-at-15-digits precision regression. No physical assertion, threshold, or scientific classification was weakened. The patch is supplied separately; these research scripts are not changed by this documentation PR.

The audit branch does not modify main or enable auto-merge. Original full-CI results apply to the pinned original snapshot, not automatically to arbitrary later code revisions.

## 8. Minimal remaining problem and one next target

To obtain user-A, one model must simultaneously provide: (1) specified global geometry, field theory, boundary conditions, fixed renormalization and energy definition; (2) positive CCR-compatible locally Hadamard W; (3) finite conserved RSET and the required finite total energy; (4) the same metric solving the full semiclassical equation. To obtain user-B for a larger class, at least one of these must be proved impossible for every member of that class. Current calculations do not cover all survivors.

**One next physical problem:** determine whether a refocusing time-periodic Einstein universe supports a positive finite-energy Hadamard state that closes its own semiclassical Einstein equation.

Fix

```math
M_a=(\mathbb R_\tau/2\pi a\mathbb Z)\times S^3,\qquad
 g_a=-d\tau^2+a^2d\Omega_3^2,\qquad P=\Box-R/6,
```

with a finite number of ordinary free massless conformal scalars, no ghosts, no CBSSL, and fixed renormalized gravitational couplings. Test the spatially invariant quasifree vacuum/KMS family on the Einstein cover, with mode frequencies (n+1)/a. The real identification period 2 pi a and the inverse temperature beta are different parameters.

Prove that the full, untruncated W descends in each argument, is positive, obeys local CCR and Hadamard form, and yields finite conserved RSET. With a fixed prescription in which the higher-curvature couplings are set to zero at a specified scale, solve both

```math
3/a^2-\Lambda=8\pi G\rho_{ren}(a,\beta),\qquad
-1/a^2+\Lambda=8\pi Gp_{ren}(a,\beta).
```

Otherwise retain the specified counterterms explicitly. Require finite E=2 pi^2 a^3 rho on the spatial cut, identifying that cut as spacelike but not Cauchy. A physically controlled semiclassical claim additionally needs an appropriate curvature scale and smeared stress-fluctuation control.

Success must establish all these conditions for the SAME pair (g,W), not infer stress from the Einstein tensor. Failure of one temperature, one cutoff, or a root finder is not a no-go for the specified family, much less all states. This is an eternal compact CTC testbed, not asymptotically flat finite-mouth formation. It is excluded if those extra conditions are explicitly required.

KRW's refocusing exception motivates this test; [Altaie's cover-space finite-temperature backreaction calculation](https://doi.org/10.1103/PhysRevD.65.044028) is a comparison source, not a proof of all time-quotient state conditions. No existence conclusion for this next problem is asserted in phase one.

## 9. openai/math

Targeted inspection of openai/math at search snapshot `adc7f1241b42e322a6451854ab7e4b4c146bf78a` found Riemannian Einstein rigidity/classification, Hadamard matrix results, Fourier/Sobolev estimates, and Liouville quantum gravity/planar-map material, not a directly usable theorem closing this Lorentzian four-dimensional state–geometry problem. This is not an exhaustive independent audit of every manuscript. No new claim in that repository is used as an unverified premise here.
