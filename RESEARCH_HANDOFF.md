# Research Handoff — Spacetime Screening

Last consolidated: 2026-09-22 (JST)

Repository:

\[
\texttt{https://github.com/HeliCorgi/spacetime-screening}
\]

Main branch: \`main\`

This file is the restart point for the next research session.

---

# 0. Central research question

The project is no longer primarily asking

> Can one write down a regular black-hole metric?

The current question is

\[
\boxed{
\text{Can quantum-gravity-motivated screening regularize black-hole curvature}
}
\]

without moving the pathology into

\[
\boxed{
\text{physical kinetic modes, constraints, principal symbols, or the 4D action?}
}
\]

The key working lesson is

\[
\boxed{
\text{regular background}
\not\Rightarrow
\text{regular/healthy physical dynamics}.
}
\]

---

# 1. Working rules for future sessions

When continuing this repository:

1. distinguish explicitly between:
   - **PUBLISHED RESULT**;
   - **REPRODUCED HERE**;
   - **NEW CALCULATION CANDIDATE**;
   - **CONJECTURE / OPEN**;

2. do not claim priority merely because a relation has not yet been found in
   a quick search;

3. commit substantive calculations directly to \`main\`; direct commits have
   already been authorized;

4. run symbolic/numerical assertions through GitHub Actions;

5. persistent CI reports are posted to:

   \[
   \boxed{
   \text{GitHub Issue \#1: CI monitor: symbolic calculations}
   }
   \]

6. do not revive already-rejected candidate models merely because their
   background metric is attractive;

7. for long derivations, prefer:
   - explicit symbolic script;
   - short technical note;
   - CI assertion;
   - only then README/scorecard promotion.


## 1.1 Computation-budget / timeout policy

Long symbolic calculations have repeatedly exceeded interactive-session limits.
Treat this as a design constraint for future research.

Rules:

1. **Do not start with the full 4D tensor/Hessian calculation.**
   First test every candidate on the smallest algebraic-curvature family that
   can falsify it.

2. Keep each new symbolic claim in a **small independent script**. Prefer

   \[
   \text{one question}
   \longleftrightarrow
   \text{one script}
   \longleftrightarrow
   \text{one short note section}.
   \]

3. Commit after each substantive checkpoint. A later timeout should lose at
   most one small calculation, not an entire research branch.

4. Reuse closed-form expressions already established in earlier scripts.
   Do not recompute large tensor contractions merely to recover invariants
   whose formulas are already checked.

5. Test in this order whenever possible:

   \[
   \boxed{
   \text{reduced algebraic family}
   \rightarrow
   \text{explicit counterexample paths}
   \rightarrow
   C^0/C^1/C^2\text{ directional gates}
   \rightarrow
   \text{full covariant tensor calculation}
   }
   \]

6. If a candidate fails an early gate, stop expanding it. Record the failure
   and move to the next representative.

7. Let GitHub Actions run the repository-wide suite. The interactive session
   should focus on the new small script and use Issue #1 as the persistent CI
   handoff.

8. For a calculation that is still too large, split it into committed stages:

   - invariant construction;
   - spherical reduction;
   - off-spherical pole test;
   - core differentiability;
   - only then the full Hessian.

This policy is part of the research workflow, not merely a convenience.


---

# 2. Current research priority

## Primary theoretical branch

\[
\boxed{
\text{construct/find a viable 4D QT/NPQT base}
\rightarrow
\text{NLQT completion}
\rightarrow
\text{generic nonspherical principal-safety test}
}
\]

The immediate unsolved problem is **not** the nonlocal form factor itself.

The bottleneck is the full four-dimensional off-spherical base action.

## Secondary dynamical-formation branch

Use the 2026 heavy-seed / supermassive-star literature as realistic external
formation data for a future principal-safe screened-collapse theory.

Do **not** attempt an AREPO rerun before a healthy strong-field model exists.

---

# 3. Completed failure test: two-vector regular black hole

Published benchmark:

A. Eichhorn, P. G. S. Fernandes,
*Regular black holes without mass-inflation instability and gravastars from
modified gravity*, Phys. Rev. D **113**, L081501 (2026),
arXiv:2508.00686.

Action:

\[
S
=
\frac1{16\pi G}
\int\sqrt{-g}
\left[
R+\ell^2(\mathcal L[A]-\mathcal L[B])
\right],
\]

\[
\mathcal L[W]
=
4G^{\mu\nu}W_\mu W_\nu
+
8W^2\nabla_\mu W^\mu
+
6(W^2)^2.
\]

Regular branch:

\[
f(r)
=
1-
\frac{2Mr^2}{r^3+2q\ell^2}.
\]

## 3.1 Direct odd ghost result

The repository now contains a **direct 4D harmonic expansion of the original
\(A-B\) action**.  The published generalized-Proca formalism is only a later
cross-check.

For \(l=2\), after eliminating the nondynamical directions in a sufficiently
large finite asymptotic exterior region,

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

Therefore the reduced physical odd kinetic matrix has one positive and one
negative eigenvalue in that open region.

Technical status:

\[
\boxed{
\text{direct asymptotic odd ghost established within quadratic theory}
}
\]

Novelty priority: **not claimed**.

Key files:

- \`notes/direct-two-vector-odd-expansion.md\`
- \`notes/direct-asymptotic-odd-ghost.md\`
- \`src/symbolic/direct_two_vector_odd_l2.py\`
- \`src/symbolic/direct_two_vector_odd_principal_tr.py\`
- \`src/symbolic/direct_odd_active_null_constraints.py\`
- \`src/symbolic/direct_odd_asymptotic_ghost.py\`
- \`src/symbolic/direct_ab_odd_fourier.py\`
- \`src/symbolic/direct_ab_odd_constraints.py\`

## 3.2 Reusable Schur-complement gate

For a healthy sector \(x\) and an additional sector \(y\),

\[
\mathcal L_{\rm kin}
=
\frac12\dot x^{\rm T}A\dot x
+
\dot x^{\rm T}B\dot y
+
\frac12\dot y^{\rm T}C\dot y,
\]

the reduced kinetic matrix is

\[
\boxed{
K_{\rm red}
=
C-B^{\rm T}A^{-1}B.
}
\]

If

\[
C=0
\]

and an active \(B\)-direction survives constraints,

\[
K_{\rm red}\le0.
\]

Key files:

- \`notes/auxiliary-derivative-mixing-lemma.md\`
- \`src/symbolic/auxiliary_mixing_schur_lemma.py\`

## 3.3 Hidden Schwarzschild tensor characteristic

Separate calculation candidate:

\[
\boxed{
f_T(r)=1-\frac{2M}{r}.
}
\]

This factor has been recovered both from a local TT principal metric and from
the standard odd quadratic coefficient block.

It remains interesting, but it is no longer required to reject the model:
the odd ghost already does that.

Optional future work only:

- full physical tensor master reduction;
- global-in-\(r\) constraint-rank map.

---

# 4. Principal-safety framework

A candidate must pass more than background regularity.

Current minimum gates:

\[
\boxed{
\begin{aligned}
&\text{bounded background curvature},\\
&\text{regular auxiliary/background fields},\\
&\text{differentiable 4D action},\\
&\text{controlled constraint rank},\\
&\text{positive physical kinetic matrix},\\
&\text{finite/hyperbolic principal symbol},\\
&\text{nonzero strong-coupling scale},\\
&\text{dynamical formation},\\
&\text{inner-horizon / semiclassical stability}.
\end{aligned}
}
\]

For a local curvature action require, at minimum,

\[
\boxed{
\mathcal L,\qquad
\frac{\partial\mathcal L}{\partial R_{\mu\nu\rho\sigma}},
\qquad
\frac{\partial^2\mathcal L}
{\partial R_{\mu\nu\rho\sigma}\partial R_{\alpha\beta\gamma\delta}}
}
\]

to exist and be finite on the target background in all perturbatively relevant
directions.

Key document:

- \`docs/principal-safe-screening.md\`

---

# 5. Local analytic Class-II / GQTG branch

## 5.1 Status

Pure-metric Class-II/GQTG avoids the two-vector auxiliary-mixing gate, but as
a complete local nonperturbative theory it retains the known
reduced-spectrum / strong-coupling problem.

Keep it as:

\[
\boxed{
\text{EFT / polynomial building block}
}
\]

not as the final screening completion.

## 5.2 Exact Hayward asymptotic mismatch

The genuine 4D GQTG family starts at cubic order.

For order \(n\),

\[
\delta f_n
=
O(r^{-(3n-3)}).
\]

The cubic correction starts at

\[
\boxed{
\delta f_3=O(r^{-6}).
}
\]

Hayward instead has

\[
f_H
=
1-\frac{2M}{r}
+
\frac{4M^2\ell^2}{r^4}
+
O(r^{-7}).
\]

Therefore exact Hayward cannot arise from a normally convergent analytic 4D
GQTG tower.

Key files:

- \`src/symbolic/gqtg_hayward_asymptotic_obstruction.py\`
- \`notes/gqtg-hayward-asymptotic-obstruction.md\`

## 5.3 Conditional core/Hessian no-go

On a de Sitter-type core,

\[
f=1-cr^2,
\]

each finite genuine GQTG order contributes

\[
F_n
=
-\frac12\lambda_n c^n r^3.
\]

A nonzero mass constant at finite limiting curvature \(c_*\) requires a
nonuniform/singular resummation

\[
G(c)=\sum\lambda_n c^n\to\infty
\]

as \(c\to c_*\).

Thus, under normal-convergence and termwise-differentiability assumptions,

\[
\boxed{
\text{local analytic GQTG}
+
\text{finite curvature Hessian at }c_*
+
\text{nonzero-mass limiting-curvature core}
}
\]

cannot all hold.

This is **conditional**, not a theorem for arbitrary nonperturbative
resummations.

Key files:

- \`src/symbolic/gqtg_core_hessian_conditional_no_go.py\`
- \`notes/gqtg-core-hessian-conditional-no-go.md\`

---

# 6. Nonlocal QTG (NLQT): current leading framework

Primary source:

P. Bueno, P. A. Cano, R. A. Hennigar, Á. J. Murcia,
*Regular Black Holes in Nonlocal Quasitopological Gravity*,
arXiv:2607.07790 (2026).

Schematic construction:

\[
S_{\rm NLQT}
=
S_{\rm QT}
-
\frac12
\hat{\mathcal E}^{ab}
\mathcal F_{ab}{}^{cd}
\hat{\mathcal E}_{cd},
\]

\[
\mathcal F
=
\frac{
e^{\Omega(\hat{\mathcal D})}-I
}{
\hat{\mathcal D}
}.
\]

## 6.1 Restricted PASS results

On subspaces where

\[
\mathcal D
=
\hat{\mathcal D}
=
\hat{\mathcal D}^{\dagger},
\]

the quadratic operator factorizes with a zero-free entire multiplier.

Published restricted passes:

- maximally symmetric perturbations;
- SS perturbations of SS vacuum backgrounds;
- flat-space ordinary massless-graviton pole structure;
- no local-QT derivative-order reduction on the analyzed symmetric sectors.

Thus:

\[
\boxed{
\text{zero-kernel: PASS on proven symmetric subspaces}
}
\]

and

\[
\boxed{
\text{healthy linear spectrum: PASS on flat/max-sym backgrounds}
}
\]

but **not yet for generic nonspherical RBH perturbations**.

## 6.2 Operator mismatch gate

For generic perturbations,

\[
\mathcal D\ne\hat{\mathcal D}
\]

in general.

Define

\[
\boxed{
\Delta\mathcal D
=
\mathcal D-\hat{\mathcal D}.
}
\]

A zero-free entire function alone does not imply a zero-free/full healthy
curved-background operator.

Key files:

- \`src/symbolic/nonlocal_qtg_gate.py\`
- \`src/symbolic/nonlocal_qtg_nonspherical_gate.py\`
- \`notes/principal-gate-classII-nlqt.md\`
- \`notes/nlqt-zero-kernel-kinetic-core-status.md\`

---

# 7. Main current bottleneck: the 4D QT/NPQT base action

This is the most important theoretical status for restart.

## 7.1 Spherical response does not determine nonspherical perturbations

A deformation such as

\[
\Delta S
=
\lambda
\int\sqrt{-g}
({}^{\star}RR)^2
\]

vanishes on a static parity-even spherical background at value and first
variation, while changing the odd quadratic action through

\[
\Delta S^{(2)}
\propto
\lambda
[\delta({}^{\star}RR)]^2.
\]

Therefore

\[
\boxed{
\text{spherical }h(\psi)
\text{ does not uniquely determine generic odd stability}.
}
\]

Key files:

- \`src/symbolic/ss_completion_ambiguity.py\`
- \`notes/ss-completion-ambiguity.md\`

## 7.2 NLQT inherits base-action differentiability

The NLQT operator uses

\[
\hat{\mathcal D}
=
\delta\hat{\mathcal E},
\]

and therefore the curvature Hessian of the local QT base action.

If the base Hessian is divergent/undefined, the entire form factor does not
repair an operator that is undefined before the form factor is applied.

Key files:

- \`src/symbolic/nlqt_base_hessian_inheritance.py\`
- \`notes/nlqt-base-hessian-inheritance.md\`

## 7.3 Displayed 2025 4D NPQT representative has an explicit pole

The displayed rational common denominator is

\[
\boxed{
D_{\rm NPQT}
=
(WZZ)W_2-2W_3Z_2.
}
\]

The repository found a real Lorentzian algebraic curvature direction

\[
(e_1,e_2,e_3)=(1,5,-6),
\]

\[
z_1=z_2=1,
\qquad
z_0=-1+\frac{8}{\sqrt{61}},
\]

for which

\[
\boxed{
D_{\rm NPQT}=0
}
\]

while

\[
\boxed{
W_3Z_3W_2
=
-\frac{274268160}{61}
\ne0.
}
\]

So the displayed cubic rational term has a genuine off-spherical pole.

This was independently checked by direct Lorentzian tensor contraction.

Key files:

- \`notes/npqt-explicit-singular-direction.md\`
- \`src/symbolic/npqt_explicit_singular_direction.py\`
- \`src/symbolic/npqt_explicit_pole_tensor_check.py\`

Important scope:

\[
\boxed{
\text{this rejects the displayed representative, not every possible 4D NPQT representative.}
}
\]

## 7.4 NLQT cannot perturbatively hide a bad base

In the source-proven SS zero-kernel sector, the NLQT perturbation stays on the
original QT branch.

Therefore

\[
\boxed{
\text{bad/missing QT SS branch}
\not\xrightarrow{\text{small NLQT deformation}}
\text{new healthy SS branch}.
}
\]

Key note:

- \`notes/nlqt-no-perturbative-base-rescue.md\`

---

# 8. Current constructive idea: extend the spherical target, not the old denominator

The Petrov-discriminant regulator remains useful only as a proof that the
explicit type-I pole can be removed pointwise.

For the displayed cubic rational term,

\[
D=(WZZ)W_2-2W_3Z_2,
\qquad
N=W_3Z_3W_2,
\]

the previous toy was

\[
\mathcal R_\mu
=
\frac{ND}{D^2+\mu\Delta_WZ_2^2},
\qquad
\Delta_W=W_2^3-12W_3^2.
\]

## 8.1 New continuity failure of the Petrov toy

A direct general-spherical Lorentzian contraction now gives

\[
\boxed{
\left.\frac ND\right|_{\rm spherical}=W_2\Theta,
}
\]

where \(\Theta\) is the repeated angular eigenvalue in

\[
Z_{ab}
=
\delta_a^\mu\delta_b^\nu\mathcal S_{\mu\nu}
+
\Theta\sigma_{ab}.
\]

On the type-D diagonal branch

\[
(e_1,e_2,e_3)=(-2q,q,q),
\]

define

\[
A=z_0+z_2,
\qquad
B=z_1+z_2,
\qquad
\theta=z_2.
\]

Then

\[
D=-288q^3(A^2+B^2),
\]

\[
N=-13824q^5AB(A+B-2\theta).
\]

The spherical locus is \(A+B=0\), and its restricted ratio is

\[
\frac ND=48q^2\theta.
\]

At the simultaneous spherical zero \(A=B=0\), the old Petrov toy has
incompatible path limits:

\[
\boxed{
\lim_{\rm spherical}\mathcal R_\mu=48q^2\theta,
\qquad
\lim_{\rm Weyl\ split}\mathcal R_\mu=0.
}
\]

Therefore

\[
\boxed{
\text{Petrov toy: FAIL already at }C^0
\text{ on the intended simultaneous-zero set.}
}
\]

Moreover, entirely within exact type D,

\[
A=\epsilon,
\qquad
B=k\epsilon
\]

gives

\[
\boxed{
\lim_{\epsilon\to0}\frac ND
=
-\frac{96k}{1+k^2}q^2\theta.
}
\]

Thus a Weyl-speciality invariant alone cannot resolve the type-D directional
problem.

Key files:

- `notes/npqt-petrov-regulator-continuity-gate.md`;
- `src/symbolic/npqt_petrov_regulator_continuity_gate.py`;
- `notes/npqt-petrov-regulator-toy.md` — retained only as the earlier
  pointwise type-I-pole proof of concept.

## 8.2 Principal-plane target

Let \(h^a{}_b\) denote the repeated spacelike Weyl two-plane projector on a
local type-D branch.  Define

\[
\Theta_h=\frac12h^a{}_bZ_a{}^b.
\]

In the diagonal family,

\[
T=W_2\Theta_h
=-24q^2(A+B-2\theta)
\]

reproduces the spherical ratio exactly.

The Ricci anisotropy in the repeated Weyl plane is

\[
J_h=\frac12(A+B)^2,
\]

and the old numerator mismatch factorizes as

\[
\boxed{
N-TD
=
-6912q^5(A+B-2\theta)(A+B)^2.
}
\]

A first alignment blend can be made continuous, but its second directional
curvature derivatives disagree at the simultaneous zero; it therefore fails
the required \(C^2\) gate.

## 8.3 Revised representative-design problem

The immediate constructive target is now

\[
\boxed{
\Theta_{\rm ext}
=\text{smooth 4D covariant extension of the spherical angular Ricci mode}
}
\]

followed by

\[
\boxed{
T_{\rm ext}=W_2\Theta_{\rm ext}.
}
\]

The next calculation must determine whether a Weyl-principal-plane
concomitant can be made:

1. single-valued under generic type-D \(\rightarrow\) type-I splitting;
2. covariant with magnetic Weyl curvature included;
3. controlled on type-II/III/N directions;
4. genuinely \(C^2\) at the maximally symmetric core after the \(W_2\)
   weighting;
5. exactly spherical-equivalent when inserted into the full cubic density.

Only after those checks should its curvature Hessian be fed into NLQT.

This replaces the earlier mainline idea of solving the problem primarily by
adding spherical-vanishing squares to the old denominator.


## 8.4 Local spectral-cluster PASS away from the core

The first constructive continuation test passes locally in the
purely-electric sector.

For a real symmetric tracefree electric-Weyl operator \(E\) with an isolated
simple eigenvalue \(\lambda_s\), define

\[
I_2=\operatorname{tr}(E^2),
\]

\[
\boxed{
P_s
=
\frac{
E^2+\lambda_s E+
\left(\lambda_s^2-\frac12 I_2\right)I
}{
3\lambda_s^2-\frac12 I_2
}.
}
\]

Then

\[
h=I-P_s
\]

projects onto the two-dimensional eigenvalue cluster that becomes the
repeated spherical/type-D plane.

For

\[
\operatorname{spec}(E)=(-2q,q+\delta,q-\delta),
\]

the gap denominator is

\[
\boxed{
3\lambda_s^2-\frac12I_2
=
9q^2-\delta^2.
}
\]

Thus at the type-D point \(\delta=0\), the cluster projector is smooth whenever

\[
q\neq0.
\]

With

\[
\Theta_{\rm ext}
=
\frac12\operatorname{tr}(hZ_{\rm sp}),
\]

the explicit rotated split family gives

\[
\boxed{
\Theta_{\rm ext}=\Theta,
}
\]

independent of the Weyl splitting, the rotation inside the cluster, and
Ricci anisotropy inside that plane. Hence

\[
\boxed{
T_{\rm ext}
=
W_2\Theta_{\rm ext}
=
(48q^2+16\delta^2)\Theta
\rightarrow
48q^2\Theta.
}
\]

Therefore

\[
\boxed{
\text{type-D}\rightarrow\text{type-I splitting is not itself a local
obstruction away from }W=0.
}
\]

Key files:

- notes/npqt-principal-plane-spectral-extension.md
- src/symbolic/npqt_principal_plane_spectral_toy.py

## 8.5 Self-dual local PASS with magnetic Weyl

The same local spectral construction extends to the complex self-dual Weyl
operator \(\mathcal W\).

For

\[
\operatorname{spec}(\mathcal W)
=
(-2\rho,\rho+\delta,\rho-\delta),
\]

with

\[
a=\operatorname{tr}(\mathcal W^2),
\qquad
\lambda_s=-2\rho,
\]

the simple-eigenline projector has gap

\[
\boxed{
3\lambda_s^2-\frac12a
=
9\rho^2-\delta^2.
}
\]

At exact non-conformally-flat type D,

\[
\delta=0,
\qquad
\rho\neq0,
\]

the self-dual simple eigenline is therefore locally analytic even when
electric and magnetic Weyl curvature are both present.

At exact type D,

\[
a=6\rho^2,
\qquad
b=\operatorname{tr}(\mathcal W^3)=-6\rho^3,
\]

so

\[
\boxed{
\rho=-\frac ba,
}
\]

and

\[
\boxed{
P_D
=
\frac13
\left(
\mathcal G-\frac{\mathcal W}{\rho}
\right)
=
\frac13
\left(
\mathcal G+\frac ab\mathcal W
\right).
}
\]

Thus magnetic Weyl curvature is not, by itself, a local obstruction near a
nonzero type-D point.

Key files:

- notes/npqt-selfdual-principal-plane-extension.md
- src/symbolic/npqt_selfdual_principal_plane_toy.py

## 8.6 Global Weyl-only branch selection FAIL

The local self-dual projector cannot be promoted to a globally single-valued
Weyl-only eigenline label.

An explicit self-dual Weyl loop satisfies

\[
\boxed{
\mathcal W(s)=\mathcal W(-s),
}
\]

while its nonzero eigenprojectors exchange,

\[
\boxed{
P_+(-s)=P_-(s).
}
\]

A generic Ricci contraction distinguishes the two sheets. The loop can be
scaled arbitrarily close to \(W=0\), so the obstruction accumulates at the
maximally symmetric core.

Therefore

\[
\boxed{
\text{global branch-specific Weyl projector: FAIL}.
}
\]

This does not rule out a regular NPQT representative. It changes the
constructive target to

\[
\boxed{
\text{permutation-symmetric or mixed Weyl--Ricci extension of }W_2\Theta.
}
\]

Key files:

- notes/npqt-selfdual-branch-monodromy.md
- src/symbolic/npqt_selfdual_branch_monodromy.py

## 8.7 Immediate next algebraic problem

Do **not** proceed directly to a full curvature Hessian.

The next mainline problem is to find a branch-free invariant representation
of the exact spherical target

\[
\boxed{
T_{\rm sph}=W_2\Theta.
}
\]

The preferred route is to work in the ring of permutation-symmetric mixed
Weyl--Ricci scalar contractions.

First search for alternative covariant rational representations

\[
\boxed{
T_i=\frac{N_i(W,Z)}{D_i(W,Z)}
}
\]

that all reduce to \(W_2\Theta\) on the spherical locus but use inequivalent
denominators.

The purpose of this "invariant atlas" is diagnostic:

- determine whether the old denominator pole is specific to one invariant
  chart;
- identify mixed invariants that distinguish the spherical angular Ricci mode
  without globally labeling a Weyl eigenline;
- locate unavoidable common-zero strata before attempting a full action.

A piecewise atlas is **not** itself an acceptable final action. The final
representative must still be one covariant, single-valued \(C^2\) density.


---

# 9. Normalized-projector warning

Recent NPG constructions use normalized Weyl/Cotton directional tensors.

For a smooth spherical core

\[
f(r)
=
1-cr^2+dr^4+\cdots,
\]

the repository finds

\[
\text{Weyl}=O(r^2),
\qquad
\text{Cotton}=O(r).
\]

Thus a normalized object

\[
U[T]
=
\frac{T\otimes T}{T^2}
\]

may have a finite directional value but generic derivatives

\[
\delta U\sim r^{-1},
\qquad
\delta^2U\sim r^{-2}.
\]

This is a structural warning, though full rational-density cancellations must
be checked before rejecting an entire equivalence class.

Key files:

- \`src/symbolic/npg_cotton_projector_core.py\`
- \`notes/npg-cotton-projector-core.md\`

---

# 10. Dynamical-formation benchmark: Chon et al. heavy seeds

Primary source:

S. Chon, S. Hirano, T. Ishiyama, S.-J. Chang, V. Springel,

*Overmassive black holes and little red dots naturally form in simulations*,

Nature **657**, 621–625 (2026),

DOI \`10.1038/s41586-026-10985-8\`,

arXiv:2601.04955.

The simulation is useful as an **outer-boundary generator**, not as a direct
test of the screened core.

## 10.1 Spatial separation

For a \(10^6M_\odot\) BH,

\[
r_s\simeq0.02\ {\rm au}.
\]

The dedicated accretion zoom reaches roughly

\[
500\ {\rm au},
\]

or

\[
\sim2.5\times10^4r_s.
\]

The cosmological sink scale is much larger.

Thus the resolved cosmological gas flow is naturally separable from a
horizon-scale screened interior.

## 10.2 Temporal separation

\[
t_g=\frac{GM}{c^3}.
\]

For \(10^6M_\odot\),

\[
t_g\simeq4.93\ {\rm s}.
\]

The early super-Eddington episode is \(<1\) Myr.

Therefore a first coupling can treat the strong-field region as a sequence of
quasi-stationary inner solutions labelled by slowly varying outer data.

## 10.3 Subgrid interfaces

The Nature calculation does not dynamically resolve:

- SMS \(\rightarrow\) compact-object collapse;
- horizon/ISCO/core accretion;
- detailed inner radiative efficiency;
- jets/winds;
- strong-field BH merger.

The first coupling interface is

\[
\{M,\dot M,\rho,T,j\}_{r_{\rm sink}}
\rightarrow
\text{strong-field inner model}
\rightarrow
\{L_{\rm bol},{\rm SED},\epsilon_{\rm rad},
\dot M_{\rm wind},\dot E_{\rm kin}\}.
\]

## 10.4 Repository harnesses

- \`data/heavy_seed_source_envelope.csv\`
- \`src/numerical/heavy_seed_boundary_harness.py\`
- \`src/numerical/heavy_seed_sed_adapter.py\`
- \`src/numerical/heavy_seed_feedback_sensitivity.py\`
- \`src/numerical/heavy_seed_timescale_separation.py\`
- \`src/symbolic/heavy_seed_scale_separation.py\`
- \`notes/cosmological-heavy-seed-interface.md\`

Important data policy:

The Nature release publishes code/configuration/initial conditions, but not
the full simulation outputs.

Do not present hand-read Fig. 1 values as exact source data.

Use either:

1. author-supplied \(M(t),\dot M(t)\);
2. explicitly documented digitization;
3. a rerun of the archived setup.

---

# 11. More direct formation gate: supermassive-star GR instability

The heavy-seed literature revealed a better strong-gravity interface than
post-BH luminosity alone.

The chain is

\[
\boxed{
\text{cosmological inflow}
\to
\text{accreting SMS}
\to
\text{GR instability}
\to
\text{nonlinear fate}
\to
\text{compact object / explosion / pulsation}.
}
\]

## 11.1 GRI onset benchmark

Saio et al. (2024) give the radial-mode condition

\[
\boxed{
\omega_0^2(M_{\rm crit},\dot M_*)=0.
}
\]

Repository table:

\[
\dot M_*
=
0.05,0.1,1,10,100,1000
\ M_\odot{\rm yr}^{-1}
\]

with corresponding published critical masses stored in

- \`data/sms_gri_gr_benchmark.csv\`.

Key files:

- \`notes/sms-gr-instability-formation-gate.md\`
- \`src/numerical/sms_gri_benchmark.py\`
- \`src/symbolic/sms_gri_critical_mass_shift.py\`

For a candidate screening theory define

\[
\boxed{
\Delta M_{\rm crit}
=
M_{\rm crit,screened}
-
M_{\rm crit,GR}.
}
\]

Near the GR root,

\[
\boxed{
\Delta M_{\rm crit}
=
-
\frac{
\Delta\omega_0^2
}{
\partial_M\omega_{0,\rm GR}^2
}.
}
\]

No nonzero screening shift is currently claimed.

## 11.2 GRI occurs at very low compactness

Published GRI compactness values are approximately

\[
1.1\times10^{-5}
\lesssim
\mathcal C_*
\lesssim
1.7\times10^{-4}.
\]

For the \(1M_\odot/{\rm yr}\) model,

\[
\mathcal C_*=2.9\times10^{-5}.
\]

Using horizon curvature only as a scale diagnostic,

\[
\frac{K(R_*)}{K(2M)}
=
\mathcal C_*^6.
\]

At \(2.9\times10^{-5}\),

\[
\mathcal C_*^6
\simeq5.9\times10^{-28}.
\]

Therefore a genuinely high-curvature-only screening mechanism should leave
GRI onset almost GR-like.

The more sensitive test is **post-GRI nonlinear collapse**.

Key files:

- \`src/numerical/sms_gri_curvature_separation.py\`
- \`notes/sms-screening-activation-scale.md\`

## 11.3 GRI does not imply BH formation

Nagele & Umeda (2024) show that unstable accreting SMS models can undergo:

- direct collapse;
- thermonuclear pulsation;
- explosion.

The fate is not monotonic in \(\dot M_*\).

Thus never encode

\[
\boxed{
\text{GRI}\Rightarrow\text{BH particle}
}
\]

as an exact physical rule.

Key files:

- \`data/sms_post_gri_fates.csv\`
- \`src/numerical/sms_post_gri_fate_benchmark.py\`
- \`notes/sms-post-gri-fate-gate.md\`

## 11.4 Variable accretion history matters

Woods et al. (2021) show that cosmological time-dependent accretion histories
produce structural diversity that cannot in general be replaced by one
time-averaged \(\dot M_*\).

Repository policy:

- constant \(\dot M_*\): interpolation/fate lookup permitted only within
  source scope;
- variable \(\dot M_*(t)\): do **not** infer a fate without a stellar
  evolution solver.

Key files:

- \`src/numerical/sms_formation_interface.py\`
- \`notes/sms-formation-systematics.md\`

---

# 12. GR nonlinear collapse endpoint benchmarks

If an SMS actually reaches a strong-field collapse branch, compare a future
screened theory against GR endpoint observables.

## 12.1 Uniformly rotating mass-shedding SMS

Shibata & Shapiro (2002):

\[
\frac{M_{\rm BH}}M\simeq0.9,
\]

\[
\frac{J_{\rm BH}}{M_{\rm BH}^2}\simeq0.75,
\]

\[
\frac{M_{\rm disk}}M\simeq0.1.
\]

## 12.2 Modern rotating SMS-core calculations

Fujibayashi et al. (2025), in the studied models:

\[
\frac{M_{\rm eject}}M\sim10^{-2},
\]

\[
v_{\rm eject}\sim0.2c,
\]

\[
E_{\rm exp}\sim10^{-4}Mc^2.
\]

Use a comparison vector such as

\[
\boxed{
\left\{
t_{\rm AH},
\frac{M_{\rm AH}}M,
a_{\rm rem},
\frac{M_{\rm disk}}M,
\frac{M_{\rm eject}}M,
\frac{E_{\rm eject}}{Mc^2}
\right\}.
}
\]

If no apparent horizon forms, replace horizon quantities with

\[
\boxed{
\left\{
R_{\rm min},
K_{\rm max},
\frac{M_{\rm core}}M,
\frac{M_{\rm eject}}M,
\frac{E_{\rm eject}}{Mc^2}
\right\}.
}
\]

Key note:

- \`notes/sms-gr-collapse-endpoints.md\`

---

# 13. GR-to-screened matching parameter

Define

\[
\eta_{\rm act}
=
\frac{K_{\rm act}}{K_h}.
\]

Using the Schwarzschild curvature scale diagnostically,

\[
\boxed{
\frac{r_{\rm act}}{r_s}
=
\eta_{\rm act}^{-1/6}.
}
\]

Examples:

\[
\eta_{\rm act}=10^{-6}
\Rightarrow r_{\rm act}=10r_s,
\]

\[
\eta_{\rm act}=10^{-12}
\Rightarrow r_{\rm act}=100r_s.
\]

The future nonlinear strategy should be:

1. evolve early SMS collapse with GR while
   \[
   K/K_h\ll\eta_{\rm act};
   \]
2. enter an overlap region;
3. switch/couple to the principal-safe screened theory;
4. test convergence as the matching surface moves.

Key files:

- \`notes/sms-screening-activation-scale.md\`
- \`src/numerical/sms_screening_activation_scale.py\`

---

# 14. Recommended restart order

## Task A — theory first

Continue the **4D NPQT representative-design problem**.

Read first:

- notes/npqt-petrov-regulator-continuity-gate.md
- notes/npqt-principal-plane-spectral-extension.md
- notes/npqt-selfdual-principal-plane-extension.md
- notes/npqt-selfdual-branch-monodromy.md
- notes/npqt-explicit-singular-direction.md

The exact spherical target is

\[
\boxed{
T_{\rm sph}=W_2\Theta.
}
\]

The Weyl-only branch-projector route is locally useful but globally rejected
by monodromy. The immediate target is therefore

\[
\boxed{
\text{a permutation-symmetric or mixed Weyl--Ricci covariant extension of }
W_2\Theta.
}
\]

### A1 — next concrete calculation: mixed-invariant atlas

This is the **next task to do**.

Build a small library of independent low-degree mixed Weyl--Ricci scalar
contractions and reduce them on the spherical/type-D algebraic family.

Then solve, algebraically, for alternative rational expressions

\[
T_i=\frac{N_i}{D_i}
\]

satisfying

\[
\left.T_i\right|_{\rm spherical}=W_2\Theta.
\]

Requirements for this stage:

1. use permutation-symmetric scalar invariants;
2. do not choose or label a Weyl eigenvalue branch;
3. keep each invariant/relation in a small script;
4. test the known simultaneous-zero and explicit type-I pole points
   immediately;
5. if no low-degree alternative exists, record that negative result instead of
   increasing algebraic complexity without a reason.

Suggested output:

- src/symbolic/npqt_mixed_invariant_atlas_*.py
- notes/npqt-mixed-invariant-atlas.md

### A2 — branch-free stress tests

Only after A1 produces a candidate, test it separately on:

1. the explicit old type-I pole direction;
2. the spherical simultaneous zero \(D=\Delta_W=0\);
3. the self-dual branch-monodromy loop;
4. common scaling
   \[
   (W,Z)\rightarrow\epsilon(W,Z)
   \]
   toward the maximally symmetric core.

Use one short script per logically distinct failure mechanism.

### A3 — \(C^0/C^1/C^2\) core gate

Only a candidate that passes A2 should be tested for differentiability.

Start with finite-dimensional algebraic curvature paths and directional
derivatives. Require path-independent value, gradient, and Hessian limits
before attempting the full Riemann-tensor Hessian.

A failure here ends that candidate.

### A4 — full covariant density

Only after A3 passes:

1. restore the complete cubic NPQT density;
2. verify exact spherical reduced equations;
3. check that no new denominator-zero strata appear in the full expression.

### A5 — curvature Hessian and NLQT

Only after A4:

\[
\frac{\partial^2\mathcal L}
{\partial R_{\mu\nu\rho\sigma}\partial R_{\alpha\beta\gamma\delta}}
\]

should be computed on the regular-black-hole/core backgrounds.

Only then feed the base action into the generic nonspherical NLQT operator.

This ordering is deliberate: **do not spend a long symbolic run on A4/A5
before the cheap algebraic gates A1--A3 have passed.**


## Task B — once a viable theory exists

Use the SMS collapse benchmarks as the dynamical-formation test.

The first nonlinear simulation should **not** reproduce the whole cosmological
box.

It should start from a GR SMS collapse configuration near the strong-field
matching region and ask:

1. does an apparent horizon form?
2. is curvature bounded?
3. is the physical principal operator hyperbolic?
4. what are remnant/disk/ejecta fractions?
5. is the result stable as the matching radius changes?

## Task C — cosmological closure later

Once Task B gives a healthy inner model, connect its

\[
L_{\rm bol},\ {\rm SED},\ \dot M_{\rm wind},\ \dot E_{\rm kin}
\]

to the heavy-seed outer-boundary harness and eventually AREPO.

---

# 15. Do not restart from these superseded tasks

Do **not** spend mainline effort on:

- proving the two-vector model healthy;
- reconstructing Hayward with a minimal canonical scalar;
- using the displayed rational 4D NPQT representative unchanged;
- assuming zero-free NLQT form factors automatically prove generic
  nonspherical stability;
- demanding exact Hayward asymptotics from analytic 4D GQTG;
- treating GRI onset as automatic BH formation;
- rerunning AREPO before the strong-field theory is principal-safe.

These are already resolved or demoted.

---

# 16. Key repository entry points

Read in this order:

1. \`README.md\`
2. \`NOVELTY.md\`
3. \`ROADMAP.md\`
4. \`docs/principal-safe-screening.md\`
5. \`docs/candidate-scorecard.md\`
6. this file

Then, for the current main theoretical task:

7. `notes/npqt-explicit-singular-direction.md`
8. `notes/npqt-petrov-regulator-toy.md`
9. `notes/npqt-petrov-regulator-continuity-gate.md`
10. `notes/npqt-principal-plane-spectral-extension.md`
11. `notes/npqt-selfdual-principal-plane-extension.md`
12. `notes/npqt-selfdual-branch-monodromy.md`
13. `notes/nlqt-no-perturbative-base-rescue.md`
14. `notes/principal-gate-classII-nlqt.md`

For dynamical formation:

15. `notes/cosmological-heavy-seed-interface.md`
16. `notes/sms-gr-instability-formation-gate.md`
17. `notes/sms-post-gri-fate-gate.md`
18. `notes/sms-screening-activation-scale.md`
19. `notes/sms-gr-collapse-endpoints.md`
20. `notes/sms-formation-systematics.md`

---

# 17. CI / reproducibility

GitHub Actions runs the symbolic suite and numerical harnesses.

Persistent report:

\[
\boxed{
\text{Issue \#1 — CI monitor: symbolic calculations}
}
\]

At the time this handoff was prepared, the latest recorded monitor runs for
the current head history were successful.

If a future run fails:

1. inspect the first actual calculation failure, not the monitor workflow;
2. distinguish physics assertion failure from test-code/sign/shape error;
3. fix the minimal issue;
4. do not weaken a physics assertion merely to obtain a green build.

---

# 18. Suggested exact restart prompt

A future session can resume with:

> Read RESEARCH_HANDOFF.md, NOVELTY.md, and the current NPQT notes listed
> under Task A. Continue from the mainline, not the chronology side branch.
>
> The next concrete task is **A1: mixed-invariant atlas**. Start from the exact
> spherical target \(T_{\rm sph}=W_2\Theta\). Search for low-degree,
> permutation-symmetric mixed Weyl--Ricci covariant scalar ratios
> \(T_i=N_i/D_i\) that reproduce \(W_2\Theta\) on the spherical locus without
> globally labeling a Weyl eigenline.
>
> Keep the calculation timeout-safe: one invariant/relation per small script,
> commit each substantive checkpoint, and test the known type-I pole,
> spherical simultaneous zero, monodromy loop, and core scaling before doing
> any full 4D Hessian calculation. Use Issue #1 as the persistent CI handoff.

That is the intended restart point.
