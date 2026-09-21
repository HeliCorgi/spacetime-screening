# \(R_4\) Differentiability in the 2026 4D QTG-TNT Class-I Theory

This note evaluates the non-analytic curvature invariant \(R_4\) used in

A. Colléaux, I. Kolář, T. Málek,
*Quasi-topological gravity for 4-dimensional Taub-NUT, near-horizon extreme Kerr, and swirling symmetries*,
arXiv:2606.17784 (2026).

The class of interest contains the action

\[
I_1
=
\int d^4x\sqrt{-g}
\left[
-2\Lambda+R+A(\ell^2R_3)R_4
\right].
\]

The single-function (SF) black-hole branch satisfies

\[
R_4=0.
\]

The question is whether the displayed covariant \(R_4\) is differentiable there, as required for a generic four-dimensional perturbation theory.

## 1. Exact covariant definition

The paper uses the Zakhary-McIntosh invariants

\[
I_1=C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma},
\]

\[
I_6=S_{\mu\nu}S^{\mu\nu},
\]

and

\[
I_{11}
=
S_{\mu\nu}S_{\rho\sigma}
\left(
C^{\mu\alpha\beta\nu}C^\rho{}_{\alpha\beta}{}^\sigma
-
\widetilde C^{\mu\alpha\beta\nu}
\widetilde C^\rho{}_{\alpha\beta}{}^\sigma
\right).
\]

The non-analytic invariant is

\[
\boxed{
R_4
=
\sqrt{
\frac{2I_6}{3}
-
\frac{2I_{11}}{I_1}
}.
}
\]

Define

\[
Q
=
\frac{2I_6}{3}
-
\frac{2I_{11}}{I_1}.
\]

Then simply

\[
R_4=\sqrt Q.
\]

## 2. The SF branch is exactly the square-root cusp

Appendix A of the paper gives, on the TNT geometries,

\[
\boxed{
R_4^2
=
4\Phi_{00}\Phi_{22}.
}
\]

For the Lorentzian single-function branch,

\[
\Phi_{00}=\Phi_{22}=0,
\]

so

\[
R_4=0.
\]

Thus the desired black-hole backgrounds lie exactly on the zero of the square root.

## 3. Generic invariant derivatives diverge

Treat \(I_1,I_6,I_{11}\) as independent invariant coordinates in a generic four-dimensional neighborhood.

Then

\[
\boxed{
\frac{\partial R_4}{\partial I_6}
=
\frac{1}{3R_4},
}
\]

and

\[
\boxed{
\frac{\partial R_4}{\partial I_{11}}
=
-\frac{1}{I_1R_4}.
}
\]

The second derivative is even more singular:

\[
\boxed{
\frac{\partial^2R_4}{\partial I_6^2}
=
-\frac{1}{9R_4^3}.
}
\]

Therefore,

\[
R_4\to0
\]

implies that the first curvature derivative diverges as \(R_4^{-1}\) and the Hessian needed for a quadratic action diverges as \(R_4^{-3}\), unless the relevant perturbation directions are specially constrained.

This immediately fails the repository's covariant-action differentiability test for a generic four-dimensional neighborhood.

## 4. The problem remains even inside the TNT family

The failure is not merely an artifact of choosing arbitrary invariant coordinates.

For \(n=0\), the reduced TNT expression is

\[
R_4^{\rm signed}
=
\frac{a}{2r}\frac{b'}{b}.
\]

The SF branch is

\[
b=1.
\]

Perturb it smoothly,

\[
b(r)=1+\epsilon h(r)+O(\epsilon^2).
\]

Then

\[
R_4^{\rm signed}
=
\epsilon
\frac{a h'}{2r}
+
O(\epsilon^2).
\]

So the signed reduced curvature component crosses zero linearly.

But the covariant scalar representative reconstructs it from the square,

\[
R_4^{\rm cov}
=
\sqrt{
\left(
R_4^{\rm signed}
\right)^2
}
=
|\epsilon|
\left|
\frac{a h'}{2r}
\right|
+
O(\epsilon^2).
\]

Hence the one-sided derivatives are

\[
\left.
\frac{dR_4^{\rm cov}}{d\epsilon}
\right|_{0^+}
=
\left|
\frac{a h'}{2r}
\right|,
\]

and

\[
\left.
\frac{dR_4^{\rm cov}}{d\epsilon}
\right|_{0^-}
=
-
\left|
\frac{a h'}{2r}
\right|.
\]

They disagree.

Therefore

\[
\boxed{
R_4^{\rm cov}
\text{ has a cusp on the SF branch.}
}
\]

The symmetry-reduced **signed** variable is differentiable; the displayed covariant square-root representative is not.

## 5. Consequence for the action \(A(R_3)R_4\)

The modification is

\[
\mathcal L_{\rm corr}
=
A(\ell^2R_3)R_4.
\]

Along the TNT perturbation above, its one-sided first variations differ by

\[
\boxed{
\Delta
\left(
\frac{d\mathcal L_{\rm corr}}{d\epsilon}
\right)
=
2A(\ell^2R_3)
\left|
\frac{ah'}{2r}
\right|.
}
\]

Thus the action is differentiable at \(R_4=0\) only if, at that spacetime point,

\[
A(\ell^2R_3)=0
\]

or the perturbation direction is trivial.

A nontrivial Class-I modification does not satisfy \(A=0\) along the entire black-hole branch.

So the issue is structural, not limited to one special point.

## 6. Generic perturbations are even worse

For a generic invariant-space perturbation,

\[
Q(\epsilon)
=
q_1\epsilon+O(\epsilon^2),
\]

one obtains

\[
R_4
\sim
\sqrt{q_1\epsilon}.
\]

For \(q_1>0\),

\[
\frac{dR_4}{d\epsilon}
\sim
\epsilon^{-1/2},
\]

while for the opposite sign the principal real square root leaves its real domain.

Thus the displayed real non-analytic action does not possess an ordinary open real neighborhood around \(R_4=0\) in generic curvature-invariant directions.

## 7. Explicit regular-black-hole example

The paper's simplest regular-black-hole model chooses

\[
\boxed{
A(x)=\frac{2x}{1-x}.
}
\]

Its static solution is

\[
a(r)
=
\frac{
(r-2m)(r^2-2\ell^2)
}{
r^3-2r\ell^2+4m\ell^2
}.
\]

For \(n=0,k=1\),

\[
R_3
=
\frac{2(1-a)}{r^2}.
\]

Direct simplification gives

\[
\boxed{
R_3(r)
=
\frac{
4m
}{
4m\ell^2-2r\ell^2+r^3
}.
}
\]

Therefore

\[
x(r)=\ell^2R_3(r),
\]

and

\[
\boxed{
A(x(r))
=
\frac{
8m\ell^2
}{
r(r^2-2\ell^2)
}.
}
\]

At the regular center,

\[
x\to1,
\]

and

\[
\boxed{
A(x(r))
\sim
-\frac{4m}{r}.
}
\]

So the coefficient multiplying the nondifferentiable \(R_4\) itself diverges at the center.

It also has a pole at

\[
\boxed{
r=\sqrt2\,\ell,
}
\]

which is one of the horizons of this explicit solution.

The paper explicitly treats such divergent-\(A\) horizons in a limiting sense.

## 8. The center has a second, independent covariant issue

The paper already notes that its non-analytic invariant representatives are ill-defined when

\[
I_1=0,
\]

including conformally flat geometries.

The regular static solutions have an (A)dS-type center, where the Weyl tensor tends to zero.

Thus at the exact center the \(R_3,R_4\) representative system also approaches the known \(I_1=0\) degeneracy of the Zakhary-McIntosh reconstruction.

This is independent of the \(R_4=0\) square-root cusp.

## 9. Verdict

For the **symmetry-reduced TNT equations**, \(R_4\) can be treated as a signed reduced curvature component and the construction produces exact regular black-hole solutions.

For the **displayed generic four-dimensional covariant action**, however,

\[
\boxed{
R_4=\sqrt{
\frac{2I_6}{3}-\frac{2I_{11}}{I_1}
}
}
\]

is not differentiable on the SF branch.

Therefore the action

\[
A(\ell^2R_3)R_4
\]

does not provide a regular starting point for generic nonspherical linear perturbations or a tensor-principal-symbol calculation around the regular SF black hole.

Current score:

\[
\boxed{
\text{background SF solution: PASS/PARTIAL}
}
\]

but

\[
\boxed{
\text{4D covariant-action differentiability: FAIL}.
}
\]

## 10. What would rescue the idea

The reduced QTG-TNT mechanism could still be useful if one finds a different four-dimensional completion that:

1. reproduces the signed \(R_4\) dynamics on TNT geometries;
2. does not reconstruct \(R_4\) through a square-root cusp;
3. remains real and differentiable in an open neighborhood of the black-hole background;
4. has a finite curvature Hessian for physical perturbations.

The paper itself emphasizes that curvature-invariant representatives are highly non-unique and that broader perturbations are beyond its scope.

So this result rejects the **displayed non-analytic representative as a full perturbative completion**, not the symmetry-reduced integrability idea itself.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/r4_differentiability.py
\`\`\`

to reproduce the \(1/R_4\) and \(1/R_4^3\) derivative singularities, the TNT cusp, and the explicit \(A(x)=2x/(1-x)\) behavior.
