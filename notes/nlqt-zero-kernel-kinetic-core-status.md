# NLQT Status: Zero Kernel, Kinetic Health, and Regular Core

This note separates what is established by the 2026 NLQT source from what is
established in this repository and what remains open in four dimensions.

Primary source:

P. Bueno, P. A. Cano, R. A. Hennigar, Á. J. Murcia,
*Regular Black Holes in Nonlocal Quasitopological Gravity*,
arXiv:2607.07790 (2026).

## 1. Regular background core

The NLQT action is constructed so that every QT solution satisfying

\[
\hat{\mathcal E}_{ab}=0
\]

remains an exact solution, because the nonlocal correction is quadratic in
\(\hat{\mathcal E}_{ab}\).

Therefore the regular spherically symmetric QT black holes, including the
Hayward-type example, remain exact NLQT solutions.

For the Hayward-type branch,

\[
f(r)
=
1-
\frac{\mathsf M r^2}
{r^{D-1}+\alpha\mathsf M},
\]

and

\[
f(r)
=
1-\frac{r^2}{\alpha}+\cdots
\]

near the center.

Thus the **background geometry** has a regular de Sitter core.

\[
\boxed{
\text{background regular core: PASS}
}
\]

This is a background statement only.

## 2. Zero-kernel result

For perturbations satisfying the restricted operator identity

\[
\mathcal D
=
\hat{\mathcal D}
=
\hat{\mathcal D}^{\dagger},
\]

the NLQT source reduces the auxiliary equation to

\[
e^{\Omega(\hat{\mathcal D})}e=0.
\]

Because the exponential of an entire function has no finite zeros,

\[
\ker e^{\Omega(\hat{\mathcal D})}=0,
\]

so

\[
e=0.
\]

The source establishes the required operator identity for:

1. perturbations around maximally symmetric backgrounds;
2. spherically symmetric perturbations of spherically symmetric vacuum
   backgrounds.

Therefore

\[
\boxed{
\text{zero-kernel: PASS on the proven symmetric subspaces}
}
\]

but **not yet** for generic nonspherical regular-black-hole perturbations.

## 3. Healthy kinetic / propagator result

On flat space, the source derives tensor/scalar propagator factors of the form

\[
\frac{1}
{k^2 E_{\rm t}(-k^2)},
\qquad
\frac{1}
{k^2 E_{\rm s}(-k^2)},
\]

with zero-free entire functions \(E_{\rm t},E_{\rm s}\).

Hence the only propagator pole is

\[
k^2=0,
\]

the usual massless graviton pole.

Thus

\[
\boxed{
\text{healthy linear spectrum: PASS on flat/maximally symmetric backgrounds}
}
\]

within the source's assumptions.

The source also shows that finite-derivative truncations do not reduce the
linearized derivative order on symmetric backgrounds relative to generic
backgrounds, removing the specific QT strong-coupling mechanism caused by
principal-order reduction.

## 4. Generic nonspherical regular-BH sector

For a generic perturbation,

\[
\mathcal D
\neq
\hat{\mathcal D}
\]

in general, and \(\hat{\mathcal D}\) is not generally self-adjoint.

The clean zero-free factorization therefore does not follow.

The repository records this explicitly through the operator-mismatch gate:

\[
\boxed{
\Delta\mathcal D
=
\mathcal D-\hat{\mathcal D}.
}
\]

A zero-free entire function does not by itself imply that

\[
\mathcal D
+
\hat{\mathcal D}^{\dagger}
\mathcal F(\hat{\mathcal D})
\hat{\mathcal D}
\]

has zero kernel.

Therefore

\[
\boxed{
\text{generic nonspherical zero-kernel: OPEN}
}
\]

and

\[
\boxed{
\text{generic nonspherical healthy kinetic: OPEN}
}
\]

unless a specific full covariant completion is supplied and its quadratic
operator is analyzed.

## 5. Four-dimensional completion ambiguity

In four dimensions the spherical regular-BH equations do not uniquely
determine the off-spherical covariant action.

An explicit example is

\[
\Delta S
=
\lambda
\int\sqrt{-g}
\,
({}^{\star}RR)^2.
\]

On a static parity-even spherical background,

\[
\overline{{}^{\star}RR}=0.
\]

Hence

\[
\Delta S[\bar g]=0,
\qquad
\delta\Delta S[\bar g]=0,
\]

so the same spherical background remains a solution.

But at quadratic order,

\[
\boxed{
\Delta S^{(2)}
\propto
\lambda
\left[
\delta({}^{\star}RR)
\right]^2,
}
\]

and odd perturbations generically have

\[
\delta({}^{\star}RR)\neq0.
\]

Therefore two full four-dimensional actions can share the same regular
spherical black hole and the same spherical response law while possessing
different odd quadratic/principal operators.

Consequently:

\[
\boxed{
h(\psi)\ \text{alone does not determine generic odd stability}.
}
\]

## 6. Inheritance of base-action differentiability

The NLQT form factor is constructed from

\[
\hat{\mathcal D}
=
\delta\hat{\mathcal E}.
\]

For a base action

\[
\mathcal L_{\rm QT}(g,R_{\mu\nu\rho\sigma}),
\]

its curvature Hessian

\[
\mathcal H
=
\frac{\partial^2\mathcal L_{\rm QT}}
{\partial R\,\partial R}
\]

enters the principal coefficients of \(\hat{\mathcal D}\) through

\[
\delta P
=
\mathcal H\,\delta R.
\]

Thus a divergent or undefined base curvature Hessian is generically inherited
by the operator on which the nonlocal entire function acts.

The repository's previously analyzed rational 4D Hayward lift fails the
covariant differentiability gate.

Therefore an NLQT theory built directly on that representative lift is **not**
a principal-safe four-dimensional completion unless a further tensorial
cancellation is explicitly demonstrated.

## 7. Current three-part verdict

### Zero kernel

\[
\boxed{
\text{PASS: maximally symmetric + SS perturbation subspace}
}
\]

\[
\boxed{
\text{OPEN: generic nonspherical RBH perturbations}
}
\]

### Healthy kinetic / spectrum

\[
\boxed{
\text{PASS: flat/maximally symmetric linear spectrum}
}
\]

\[
\boxed{
\text{PASS: avoids the local-QT order-reduction mechanism}
}
\]

\[
\boxed{
\text{OPEN: physical odd/even kinetic operator on generic RBH}
}
\]

### Regular core

\[
\boxed{
\text{PASS: background geometry}
}
\]

\[
\boxed{
\text{OPEN: fluctuation/principal operator at the core}
}
\]

for a general four-dimensional completion.

For the specific rational 4D base lift previously tested in this repository,
the fluctuation-operator regularity gate fails before the nonlocal
zero-kernel test can be meaningfully applied.

## 8. Research consequence

The immediate problem is no longer simply

\[
\text{compute }\Delta\mathcal D_{\rm odd}
\]

from the spherical response.

Instead the logical order is:

1. choose a **specific differentiable four-dimensional QT base action**;
2. verify its background and curvature Hessian on the regular core;
3. construct \(\hat{\mathcal D}_{\rm odd}\) and
   \(\mathcal D_{\rm odd}\);
4. evaluate
   \[
   \Delta\mathcal D_{\rm odd};
   \]
5. test the full NLQT odd operator for kernel, kinetic signature,
   hyperbolicity, and core regularity.

Until step 1 is fixed, generic nonspherical stability is underdetermined.

## Reproducibility

Relevant scripts:

\`\`\`bash
python src/symbolic/nonlocal_qtg_gate.py
python src/symbolic/nonlocal_qtg_nonspherical_gate.py
python src/symbolic/ss_completion_ambiguity.py
python src/symbolic/nlqt_base_hessian_inheritance.py
\`\`\`
