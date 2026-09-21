# Spherical Background Does Not Fix the Nonspherical Operator

This note records an important limitation on what can be inferred from a
regular spherical black-hole solution.

## 1. Completion ambiguity

Let a four-dimensional action \(S_0[g]\) possess a static spherically
symmetric parity-even regular black hole.

The gravitational Pontryagin pseudoscalar is

\[
\mathcal P
=
{}^\star R_{\mu\nu\rho\sigma}
R^{\mu\nu\rho\sigma}.
\]

For a static spherically symmetric parity-even background,

\[
\bar{\mathcal P}=0.
\]

Now define a one-parameter family of covariant actions

\[
\boxed{
S_\lambda
=
S_0
+
\lambda
\int d^4x\sqrt{-g}\,
\mathcal P^2.
}
\]

Because \(\bar{\mathcal P}=0\),

\[
\Delta S[\bar g]=0
\]

and the first variation also vanishes:

\[
\boxed{
\delta\Delta S[\bar g]=0.
}
\]

Therefore the same spherical background remains an exact solution for every
\(\lambda\).

Its spherical response law, mass function, horizons, and regular core are
unchanged.

## 2. The quadratic action is changed

Write

\[
\mathcal P
=
\epsilon\,\delta\mathcal P
+
O(\epsilon^2).
\]

Then

\[
\boxed{
\Delta S^{(2)}
\propto
\lambda
\int\sqrt{-\bar g}\,
(\delta\mathcal P)^2.
}
\]

Thus the linear perturbation operator depends on \(\lambda\), even though the
background does not.

The ambiguity is physical at the level relevant to principal safety.

## 3. Why odd perturbations see it

On a parity-even spherical background the magnetic Weyl tensor vanishes,

\[
\bar B_{ij}=0,
\]

while the electric Weyl tensor is generally nonzero.

The Pontryagin density is proportional, up to conventions, to

\[
E_{ij}B^{ij}.
\]

Odd/axial gravitational perturbations generate the magnetic Weyl sector, so
generically

\[
\delta\mathcal P
\propto
\bar E_{ij}\,\delta B^{ij}
\neq0.
\]

This is consistent with the black-hole perturbation literature in
Chern-Simons gravity, where the Pontryagin condition acts directly on the
axial gravitational master sector.

Therefore \(\mathcal P^2\) provides an explicit covariant deformation that:

- leaves the static spherical background unchanged;
- leaves the spherical background equations unchanged at first order in the
  action variation;
- changes the odd nonspherical quadratic/principal operator.

## 4. Consequence for the NLQT test

The regular-black-hole response

\[
h(\psi)
\]

does **not** uniquely determine the generic nonspherical operator

\[
\mathcal D_{\rm odd},
\qquad
\hat{\mathcal D}_{\rm odd},
\qquad
\Delta\mathcal D_{\rm odd}.
\]

Hence one cannot decide

\[
\text{zero-kernel},
\quad
\text{healthy kinetic},
\quad
\text{regular core}
\]

from the Hayward/QT spherical equations alone.

A specific full four-dimensional covariant completion must be chosen.

This is particularly important in \(D=4\), where the source paper notes that
the QT densities reproducing the regular spherical equations are
nonpolynomial and the repository has already found explicit lift
differentiability problems for one representative construction.

## 5. What is nevertheless established for NLQT

For the specific NLQT construction of Bueno, Cano, Hennigar and Murcia:

- finite-derivative truncations restore the derivative order on symmetric
  backgrounds;
- for maximally symmetric perturbations and SS perturbations of SS vacuum
  backgrounds, the relevant operators coincide and become self-adjoint;
- with the zero-free entire form factor, the source proves zero kernel of the
  exponential multiplier on those subspaces;
- the flat-space propagator contains only the massless graviton pole.

These are genuine restricted PASS results.

They do not uniquely fix generic nonspherical black-hole perturbations until
the full 4D base action is specified.

## 6. Updated gate

Before claiming a regular black-hole model is principal-safe in 4D, require:

\[
\boxed{
\text{a fully specified off-spherical covariant completion}.
}
\]

Then compute its actual

\[
\delta^2 S_{\rm odd/even}
\]

rather than reconstructing it from the spherical response function.

For NLQT, the research problem therefore separates into two stages:

1. choose a differentiable 4D QT base action realizing the desired regular
   spherical response;
2. only then evaluate
   \[
   \mathcal Q
   =
   \mathcal D
   +
   \hat{\mathcal D}^{\dagger}
   \mathcal F(\hat{\mathcal D})
   \hat{\mathcal D}
   \]
   in generic odd/even sectors.

## References

- N. Yunes, C. F. Sopuerta,
  *Perturbations of Schwarzschild Black Holes in Chern-Simons Modified
  Gravity*, arXiv:0712.1028.
- V. Cardoso, L. Gualtieri,
  *Perturbations of Schwarzschild black holes in Dynamical Chern-Simons
  modified gravity*, arXiv:0907.5008.
- P. Bueno, P. A. Cano, R. A. Hennigar, Á. J. Murcia,
  *Regular Black Holes in Nonlocal Quasitopological Gravity*,
  arXiv:2607.07790.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/ss_completion_ambiguity.py
\`\`\`
