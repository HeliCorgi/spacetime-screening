# Novelty Map

This file separates **known literature**, **results reproduced in this
repository**, **new calculation candidates**, and **conjectures**.

The purpose is to prevent accidental priority claims and to keep the research
program focused on results that are both technically defensible and genuinely
useful.

Status labels:

- **KNOWN** — established in prior literature.
- **REPRODUCED HERE** — known result independently rederived or checked here.
- **NEW CALCULATION CANDIDATE** — a calculation produced in this repository
  for which no matching prior result has yet been identified; priority is
  **not** claimed until a dedicated literature search and full derivation are
  complete.
- **SYNTHESIS / CRITERION** — known ingredients assembled here into a common
  diagnostic framework.
- **CONJECTURE** — speculative research direction.

## 1. Background screening and regular black holes

### High-curvature weakening / screening

\[
\text{high curvature}
\rightarrow
\text{weaker effective gravitational response}
\rightarrow
\text{singularity avoidance}
\]

**Status:** KNOWN.

Related ideas occur in asymptotic safety, limiting-curvature models, mimetic
gravity, nonlocal gravity, regular black holes, and quasitopological gravity.

This repository does **not** claim novelty for the broad screening idea.

### Hayward / de Sitter core

\[
f(r)
=
1-
\frac{2GMr^2}{r^3+2GM\ell^2}
\]

with

\[
R(0)=\frac{12}{\ell^2},
\qquad
K(0)=\frac{24}{\ell^4}
\]

**Status:** KNOWN; REPRODUCED HERE.

See:

- \`src/symbolic/black_holes.py\`
- \`notes/symbolic-results.md\`

### Effective Hayward stress tensor and energy conditions

The repository reconstructs

\[
\rho,\quad p_r,\quad p_t
\]

for Hayward interpreted through ordinary Einstein gravity, including exact
NEC/WEC/SEC/DEC boundaries.

**Status:** REPRODUCED / DERIVED HERE, but not presently treated as a novelty
claim because related effective-source analyses exist throughout the regular
black-hole literature.

See:

- \`src/symbolic/effective_stress_energy.py\`
- \`notes/effective-stress-energy.md\`

## 2. Screening-response formulation

For the QTG Hayward response,

\[
\psi(s)
=
\frac{s}{1+\ell^2s},
\]

the repository defines

\[
\mathscr S
=
\frac{d\ln\psi}{d\ln s}
=
\frac1{1+\ell^2s}
=
1-\ell^2\psi.
\]

**Status:** SYNTHESIS / REPARAMETERIZATION.

The underlying curvature-response saturation is known QTG physics.  The
dimensionless logarithmic response \(\mathscr S\) is used here as a convenient
screening diagnostic, not as a claimed new physical effect.

See:

- \`src/symbolic/logarithmic_screening_response.py\`
- \`notes/logarithmic-screening-response.md\`

## 3. Restricted scalar-tensor obstruction

For

\[
S
=
\int\sqrt{-g}
\left[
\frac{F(\chi)}{16\pi G}R
-\frac12(\partial\chi)^2
-V(\chi)
\right],
\]

with

\[
ds^2
=
-f(r)dt^2
+
\frac{dr^2}{f(r)}
+
r^2d\Omega^2,
\qquad
\chi=\chi(r),
\]

the repository derives

\[
F''(r)
=
-8\pi G\,\chi'(r)^2
\le0.
\]

Under regular-center and asymptotically constant boundary conditions,

\[
F'(0)=F'(\infty)=0
\]

forces

\[
F'\equiv0,
\qquad
\chi'\equiv0.
\]

**Status:** NEW CALCULATION CANDIDATE.

This is only an **ansatz-level restricted no-go**.  It is not a no-hair theorem
for general scalar-tensor / Horndeski / DHOST gravity.

A substantial dedicated literature search is required before any priority
claim.

See:

- \`src/symbolic/scalar_tensor_no_go.py\`
- \`notes/scalar-tensor-no-go.md\`

## 4. Two-vector Hayward benchmark

The exact two-vector regular-black-hole action and its Hayward-type solution
are from prior literature.

**Status:** KNOWN.

The following repository calculations are additional diagnostics of that
model.

### Vector asymptotic quadratic degeneracy

Around

\[
g_{\mu\nu}=\eta_{\mu\nu},
\qquad
A_\mu=B_\mu=0,
\]

the vector sector has no independent quadratic action:

\[
S_{\rm vector}^{(2)}=0.
\]

**Status:** NEW CALCULATION CANDIDATE / INTERPRETIVE DIAGNOSTIC.

This may represent a genuinely auxiliary constrained sector or a strong-
coupling issue.  A full Dirac/ADM constraint analysis is required.

See:

- \`src/symbolic/vector_constraint_diagnostics.py\`
- \`notes/vector-constraint-analysis.md\`

### Axial vector modes are algebraic auxiliaries

For odd-parity angular perturbations, the repository finds an algebraic
constraint coefficient

\[
C(r)
=
G^\theta{}_\theta
+
2\nabla\cdot W
=
8\pi(\rho+p_t).
\]

**Status:** NEW CALCULATION CANDIDATE.

See:

- \`src/symbolic/axial_vector_auxiliary.py\`
- \`notes/odd-parity-vector-auxiliary.md\`

### Direct odd-sector ghost in the asymptotic exterior

The repository now contains a **direct four-dimensional harmonic expansion of
the original two-vector action**, without importing the published one-vector
generalized-Proca odd coefficients.

For \(l=2\), after passing to the active/null vector basis and eliminating the
nondynamical metric variable \(Q\), the direct reduced kinetic determinant
satisfies

\[
\boxed{
\lim_{r\to\infty}
r^5\det K_{\rm red}
=
-
\frac{1152\pi^2}{25}
M\ell^4
(16M^2+q^2)
<0.
}
\]

Therefore, for sufficiently large but finite \(r\), the direct physical
odd-sector kinetic matrix has one positive and one negative eigenvalue.

The derivative-null vector combination is independently shown to have

- no quadratic velocity;
- no linear velocity mixing with the remaining kinetic variables;
- positive algebraic stiffness on the regular branch.

Thus it is an auxiliary direction and does not remove the negative active
mode.

A separate local/canonical \(l=1\) derivation obtains the same sign structure,
and a full \(l=1\) four-dimensional harmonic expansion is included as an
additional CI cross-check.

**Technical status:** DIRECT RESULT in the stated asymptotic exterior region.

**Novelty status:** NEW CALCULATION CANDIDATE.  A targeted September-2026
search did not identify a published odd-parity ghost analysis of this exact
Eichhorn-Fernandes two-vector branch, but priority is **not** claimed.

This result is sufficient to reject the benchmark as a globally healthy
principal-safe theory even if special radii have different constraint rank.

See:

- \`src/symbolic/direct_two_vector_odd_l2.py\`
- \`src/symbolic/direct_two_vector_odd_principal_tr.py\`
- \`src/symbolic/direct_l2_velocity_linear_audit.py\`
- \`src/symbolic/direct_odd_active_null_constraints.py\`
- \`src/symbolic/direct_odd_asymptotic_ghost.py\`
- \`src/symbolic/direct_asymptotic_ghost_robustness.py\`
- \`src/symbolic/direct_ab_odd_fourier.py\`
- \`src/symbolic/direct_ab_odd_constraints.py\`
- \`notes/direct-two-vector-odd-expansion.md\`
- \`notes/direct-asymptotic-odd-ghost.md\`

### Hidden radial TT Schwarzschild characteristic

For a local radial pure-TT perturbation, the repository obtains the principal
metric ansatz

\[
g_{\rm T}^{\mu\nu}
=
g^{\mu\nu}
+
4\ell^2
\left(
A^\mu A^\nu-B^\mu B^\nu
\right),
\]

which simplifies on the regular branch to

\[
\boxed{
f_{\rm T}(r)
=
1-\frac{2M}{r}.
}
\]

The background metric is regular Hayward-like while the candidate radial TT
characteristic is Schwarzschild-like.

**Status:** NEW CALCULATION CANDIDATE — HIGHEST PRIORITY.

**Updated support:** the same factor has now been recovered from the standard
Regge-Wheeler odd quadratic-action coefficient block.  The reduced tensor
kinetic coefficient and radial characteristics are

\[
q_T=\frac{f-\Delta}{2f^2},
\qquad
v_-=-f,
\qquad
v_+=f\frac{f+\Delta}{f-\Delta},
\]

with

\[
f+\Delta=1-\frac{2M}{r}.
\]

At (r=2M), (q_T>0) and the background metric is regular, so this behaves as
a tensor characteristic horizon rather than a kinetic ghost surface.

The remaining limitation is an **independent direct harmonic expansion of the
original two-vector action**, including its complete constraint algebra.
Therefore this is still not labeled a publication-ready priority claim.

The immediate research goal is to determine whether the same characteristic
survives the full \(l\ge2\) odd-parity Regge-Wheeler reduction.

See:

- \`src/symbolic/tensor_principal_cone.py\`
- \`notes/tensor-principal-cone.md\`

## 5. Extremal benchmark diagnostics

### Extremal near-horizon \(AdS_2\times S^2\)

For the fully extremal vector branch, the repository derives the equal-radius
near-horizon product geometry.

**Status:** REPRODUCED / DERIVED HERE from the known exact solution.

### Test-scalar Aretakis quantity

The repository explicitly derives the \(l=0\) test-scalar horizon conserved
quantity and transverse-derivative growth.

**Status:** REPRODUCED INSTANCE of a known general extremal-horizon mechanism,
not a novelty claim.

See:

- \`src/symbolic/aretakis_test_scalar.py\`
- \`notes/aretakis-test-scalar.md\`

## 6. Principal-safe screening framework

The repository requires more than finite background curvature:

\[
\begin{aligned}
&\text{background regularity},\\
&\text{covariant-action differentiability},\\
&\text{constraint regularity},\\
&\text{positive physical kinetic matrix},\\
&\text{regular / hyperbolic principal symbol},\\
&\text{nonzero strong-coupling scale},\\
&\text{dynamical formation}.
\end{aligned}
\]

**Status:** SYNTHESIS / CRITERION.

Each ingredient is standard in modified-gravity / PDE / EFT analysis.  The
potential contribution of this repository is to apply the same destructive
test consistently across regular-black-hole models.

See:

- \`docs/principal-safe-screening.md\`
- \`docs/candidate-scorecard.md\`

## 7. Rational QTG lift degeneracy

For the explicit four-dimensional rational lift of the spherical
nonpolynomial QTG model, the repository finds:

- the displayed \(\mathcal P,\mathcal K\) densities are \(0/0\) on the
  single-function branch;
- their spherical limits are removable;
- generic four-dimensional invariant gradients diverge;
- the complete representative action requires an additional cancellation
  condition not obeyed identically by the explicit Hayward functions;
- square-root and Weyl-ratio alternative lifts remain nondifferentiable at
  symmetry-enhanced points.

**Status:** NEW CALCULATION CANDIDATE.

The source literature already warns that the four-dimensional lift is
nonunique and may be pathological away from the spherical sector.  The
specific factorization and gradient-divergence results here should therefore
be presented as a concrete realization of that caveat, not as a claim that
the reduced QTG theory is invalid.

See:

- \`src/symbolic/covariant_lift_degeneracy.py\`
- \`src/symbolic/covariant_lift_action_gradient.py\`
- \`notes/covariant-lift-degeneracy.md\`

## 8. 2026 first-order QTG-TNT \(R_4\) obstruction

For

\[
R_4
=
\sqrt{
\frac{2I_6}{3}
-
\frac{2I_{11}}{I_1}
},
\]

the repository derives

\[
\frac{\partial R_4}{\partial I_6}
=
\frac1{3R_4},
\qquad
\frac{\partial^2R_4}{\partial I_6^2}
=
-\frac1{9R_4^3},
\]

and shows the covariant square root produces an absolute-value cusp across the
single-function branch.

**Status:** NEW CALCULATION CANDIDATE, strongly supported by the source
classification.

The associated **structural analyticity obstruction** is mostly a reformulation
of the paper's classification result:

- analytic Riemann-only scalars contain \(R_4\) only through even powers;
- nontrivial first-order Class-I QTG-TNT requires linear \(R_4\);
- therefore the first-order mechanism is structurally non-analytic.

The classification itself is KNOWN; the explicit differentiability/cusp
diagnostics are calculations performed here.

See:

- \`src/symbolic/r4_differentiability.py\`
- \`src/symbolic/r4_analyticity_obstruction.py\`
- \`notes/r4-differentiability.md\`
- \`notes/r4-analyticity-obstruction.md\`

## 9. Regularized-Lovelock planar benchmark

The existence of the regular planar solution and its instability are known
from 2025 literature.

**Status:** KNOWN; REPRODUCED HERE as a benchmark.

It is retained because it provides an independent example of

\[
\boxed{
\text{regular background}
\not\Rightarrow
\text{regular physical perturbations}.
}
\]


### Smooth-core normalized-projector obstruction

For a smooth single-function spherical center,

\[
f(r)=1-cr^2+dr^4+\cdots,
\]

the Weyl tensor vanishes as \(O(r^2)\) and the Cotton tensor as \(O(r)\).

Therefore covariant action variables of the normalized-projector form

\[
U[T]
=
\frac{T\otimes T}{T^2}
\]

can possess a finite directional value while generic variations scale as

\[
\delta U\sim r^{-1},
\qquad
\delta^2U\sim r^{-2}.
\]

**Status:** NEW CALCULATION CANDIDATE / STRUCTURAL DIAGNOSTIC.

This applies directly to NPG representatives built from normalized
Cotton/Weyl direction tensors.  It does not rule out every possible
non-polynomial representation; a full-action cancellation could evade it.

See:

- \`src/symbolic/npg_cotton_projector_core.py\`
- \`notes/npg-cotton-projector-core.md\`

### Analytic GQTG / regular-core conditional no-go

For the genuine 4D GQTG tower, each curvature order contributes

\[
F_n
=
-\frac12\lambda_n c^n r^3
\]

on an exact de Sitter-type core.

A nonzero mass constant at finite limiting curvature therefore requires a
nonuniform resummation

\[
G(c)=\sum\lambda_n c^n
\to\infty
\]

as \(c\to c_*\).

If the local curvature expansion and its curvature Hessian converge normally
and are termwise differentiable in an open neighborhood of \(c_*\), then
\(G(c_*)\) is finite and the nonzero-mass core cannot be supported.

**Status:** NEW CONDITIONAL NO-GO CANDIDATE.

The assumptions are essential.  This is not claimed for arbitrary
nonperturbative summation prescriptions.

See:

- \`src/symbolic/gqtg_core_hessian_conditional_no_go.py\`
- \`notes/gqtg-core-hessian-conditional-no-go.md\`


### Explicit pole in the displayed 2025 NPQT representative

The displayed cubic 4D NPQT density contains

\[
\frac92
\frac{
W_3 Z_3 W_2
}{
(WZZ)W_2-2W_3Z_2
}.
\]

The repository constructs a real Lorentzian algebraic curvature tensor for
which

\[
(WZZ)W_2-2W_3Z_2=0
\]

while

\[
W_3 Z_3 W_2
=
-\frac{274268160}{61}
\neq0.
\]

The result has been independently checked by explicit tensor index
contractions in an orthonormal Lorentzian frame.

**Status:** NEW CALCULATION CANDIDATE / EXPLICIT OBSTRUCTION TO THE DISPLAYED
REPRESENTATIVE.

This does **not** establish that every covariant representative with the same
spherical reduction is singular.  The source literature explicitly stresses
the degeneracy of off-spherical completions.

See:

- \`src/symbolic/npqt_explicit_singular_direction.py\`
- \`src/symbolic/npqt_explicit_pole_tensor_check.py\`
- \`notes/npqt-explicit-singular-direction.md\`

### NPQT spherical-target identity and Petrov-regulator continuity failure

For the displayed cubic rational piece

[
rac ND,
qquad
D=(WZZ)W_2-2W_3Z_2,
qquad
N=W_3Z_3W_2,
]

a direct Lorentzian contraction on a general local spherical algebraic
curvature configuration gives

[
oxed{
left.rac NDight|_{m spherical}=W_2Theta,
}
]

where (Theta) is the repeated angular traceless-Ricci eigenvalue.

The earlier Petrov-discriminant toy

[
mathcal R_mu
=
rac{ND}{D^2+muDelta_WZ_2^2}
]

removes the previously identified explicit type-I pole pointwise, but the
follow-up calculation finds incompatible limits at a spherical simultaneous
zero:

[
oxed{
lim_{m spherical}mathcal R_mu=48q^2	heta,
qquad
lim_{m Weyl split}mathcal R_mu=0.
}
]

Thus that toy has no (C^0) extension there.

**Status:** NEW CALCULATION CANDIDATE / OBSTRUCTION TO THE TOY REGULATOR.

See:

- `src/symbolic/npqt_petrov_regulator_continuity_gate.py`
- `notes/npqt-petrov-regulator-continuity-gate.md`
- `notes/npqt-petrov-regulator-toy.md`

### Local principal-plane spectral extension

In the purely-electric sector, let (E) be the spatial electric-Weyl operator
and let (lambda_s) be an isolated simple eigenvalue.  The complementary
rank-two spectral-cluster projector can be constructed from

[
P_s
=
rac{
E^2+lambda_sE+
left(lambda_s^2-rac12I_2ight)I
}{
3lambda_s^2-rac12I_2
},
qquad
h=I-P_s.
]

For the local split family

[
operatorname{spec}(E)=(-2q,q+delta,q-delta),
]

the spectral gap factor is

[
9q^2-delta^2,
]

which is nonzero at the type-D point (delta=0) whenever (q
eq0).

The candidate extension

[
Theta_{m ext}
=
rac12operatorname{tr}(hZ_{m sp})
]

then remains exactly equal to the cluster-average Ricci eigenvalue and
recovers

[
W_2Theta_{m ext}
	o
48q^2Theta.
]

So local type-D to type-I splitting is not by itself an obstruction away from
the conformally-flat core.

**Status:** NEW CALCULATION CANDIDATE / LOCAL CONSTRUCTIVE PASS ONLY.

The magnetic-Weyl, type-II/III/N, global branch-selection, and (C^2)
(W=0) core problems remain open.

See:

- `src/symbolic/npqt_principal_plane_spectral_toy.py`
- `notes/npqt-principal-plane-spectral-extension.md`

### Self-dual local principal-plane extension

The local spectral-cluster construction also extends to the complex self-dual
Weyl operator, so magnetic Weyl curvature is included at the algebraic level.

For

[
operatorname{spec}(mathcal W)
=
(-2ho,ho+delta,ho-delta),
]

the isolated simple-root projector has gap factor

[
oxed{
9ho^2-delta^2.
}
]

At exact non-conformally-flat type D,

[
delta=0,
qquad
ho
eq0,
]

the gap is nonzero.  The exact type-D invariants satisfy

[
ho=-rac{
operatorname{tr}(mathcal W^3)
}{
operatorname{tr}(mathcal W^2)
},
]

and the simple-line projector can be written intrinsically as

[
P_D
=
rac13
left(
mathcal G-rac{mathcal W}{ho}
ight).
]

Thus magnetic Weyl curvature does not create a separate local obstruction to
continuing the type-D principal plane.  The remaining obstruction is global
branch selection / algebraically special non-D directions / the
gap-closing conformally-flat core.

**Status:** NEW CALCULATION CANDIDATE / LOCAL CONSTRUCTIVE PASS ONLY.

See:

- `src/symbolic/npqt_selfdual_principal_plane_toy.py`
- `notes/npqt-selfdual-principal-plane-extension.md`

### Self-dual Weyl branch-monodromy obstruction

The local self-dual spectral continuation does not provide a global Weyl-only
eigenline label.

For the explicit complex symmetric tracefree family

[
mathcal W(t)
=
egin{pmatrix}
a&b&0\\
b&-a&0\\
0&0&0
end{pmatrix},
qquad
a=rac{1+t}{2},
qquad
b=rac{1-t}{2i},
]

with (t=s^2),

[
chi(lambda)
=
lambda(lambda^2-t).
]

Although

[
mathcal W(s)=mathcal W(-s),
]

the nonzero eigenprojectors are exchanged:

[
P_+(-s)=P_-(s).
]

A generic Ricci contraction distinguishes the two sheets, and the whole loop
can be scaled arbitrarily close to (W=0).

**Status:** NEW CALCULATION CANDIDATE / OBSTRUCTION TO GLOBAL WEYL-ONLY
EIGENLINE SELECTION.

This does not rule out permutation-symmetric or mixed Weyl-Ricci
representatives.

See:

- `src/symbolic/npqt_selfdual_branch_monodromy.py`
- `notes/npqt-selfdual-branch-monodromy.md`

## 10. Nonlocal zero-free form factor

The use of zero-free entire functions to avoid additional propagator poles is
standard in nonlocal gravity.

**Status:** KNOWN; toy implementation REPRODUCED HERE.

The current script is only a design diagnostic and is **not** the exact
nonlocal-QTG action.

## 11. Non-geometric / spacetime-phase interpretation

The possibility that the metric ceases to be a useful fundamental variable at
high curvature is not established by the current calculations.

**Status:** CONJECTURE.

It should remain downstream of the more immediate question:

\[
\boxed{
\text{Can a geometric screening theory be principal-safe?}
}
\]

Only if geometric candidates systematically fail should the non-geometric
extension become the main line.

## 12. Current project question

The recommended central question is:

> **Can quantum-gravity-motivated screening regularize black-hole curvature
> without hiding the singular behavior in physical propagation modes,
> constraints, or the covariant action itself?**

Equivalent technical version:

\[
\boxed{
\text{regular background}
+
\text{regular physical principal structure}
+
\text{healthy spectrum}
\;?
}
\]

## 13. Immediate priority

### P0 — construct a differentiable 4D NPQT base representative

The direct two-vector odd-parity failure test is complete and no longer the
mainline task.

The current target is the displayed NPQT spherical rational response rewritten
as

[
oxed{
T_{m sph}=W_2Theta.
}
]

Continue from the local principal-plane spectral construction and determine
whether there exists one generic 4D covariant extension that is

1. single-valued for generic off-spherical curvature;
2. valid with magnetic Weyl curvature;
3. controlled on Petrov II/III/N directions;
4. genuinely (C^2) through the maximally symmetric (W=0) core;
5. exactly equivalent to the required spherical reduced density.

Only after those gates pass should the curvature Hessian be inserted into the
NLQT operator.

### P1 — generic nonspherical NLQT principal operator

Once a differentiable 4D QT/NPQT base exists, compute the odd/even mismatch

[
Deltamathcal D
=
mathcal D-hat{mathcal D}
]

and test the physical kinetic/principal structure on the regular-black-hole
background.

### P2 — dynamical formation

Use the SMS GR-instability and nonlinear-collapse benchmarks only after a
principal-safe strong-field theory exists.

## 14. Priority-claim policy

Do **not** use phrases such as:

- "first discovery";
- "new theorem";
- "previously unknown";
- "we prove";

for any NEW CALCULATION CANDIDATE until:

1. the derivation is complete;
2. a targeted literature search is documented;
3. assumptions and scope are stated;
4. independent reproduction is possible from repository code.

Until then use:

- "we find";
- "our calculation suggests";
- "candidate result";
- "we have not identified a prior derivation of this exact relation."

