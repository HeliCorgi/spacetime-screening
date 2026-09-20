# Regular Black Holes

## 1. Regular center

For

\[
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2,
\]

a sufficient small-\(r\) form for finite curvature is

\[
f(r)=1-a r^2+O(r^3)
\]

with finite \(a\).

The special case \(a>0\) is de Sitter-like.

A stronger Minkowski-core condition requires the \(r^2\) term itself to vanish so that curvature invariants tend to zero.

## 2. Hayward benchmark

A useful benchmark is

\[
f(r)
=
1-
\frac{2G_NMr^2}
{r^3+2G_NM\ell^2}.
\]

At large radius,

\[
f(r)
=
1-\frac{2G_NM}{r}+O(r^{-4}),
\]

so the Schwarzschild limit is recovered.

At small radius,

\[
f(r)
=
1-\frac{r^2}{\ell^2}+O(r^5),
\]

so the core is de Sitter-like and curvature remains finite.

Hayward's original model is a benchmark geometry, not evidence by itself for a unique quantum-gravity mechanism.

Reference:
Sean A. Hayward, *Formation and Evaporation of Nonsingular Black Holes*, Phys. Rev. Lett. 96, 031103 (2006), https://doi.org/10.1103/PhysRevLett.96.031103

## 3. Horizon structure

If a static asymptotically flat geometry satisfies

\[
f(\infty)>0,
\qquad
f(0)>0,
\]

but contains a non-extremal outer horizon \(r_+\), then \(f\) changes sign at \(r_+\). To return to positive \(f(0)\), continuity generically requires an inner zero \(r_-\).

Thus a regular center often trades a central singularity for an inner-horizon problem.

## 4. Mass inflation

Cauchy horizons can exhibit large blueshift of perturbations. In many black-hole models this drives mass inflation and may recreate a singular structure even when the background metric is regular.

Therefore "finite background curvature" is not sufficient. The stability of the background under ingoing and outgoing perturbations must be tested.

Recent work has explored inner-extremal regular black holes with vanishing inner-horizon surface gravity as a way to soften classical mass-inflation behavior:

F. Di Filippo, I. Kolář, D. Kubizňák, *Inner-extremal regular black holes from pure gravity*, Phys. Rev. D 111, L041505 (2025), https://doi.org/10.1103/PhysRevD.111.L041505

This does not remove all semiclassical or quantum stability questions.

## 5. Project criteria

A regular-black-hole solution is useful here only if we can answer:

1. What covariant dynamics generates it?
2. Does it form from ordinary collapse?
3. Are its perturbations well behaved?
4. What happens at the inner horizon?
5. How does Hawking evaporation modify the geometry?
6. Does the endpoint preserve information?
7. Is the effective description valid in the core?

The repo will treat a regular metric as a starting point, not as singularity resolution by itself.
