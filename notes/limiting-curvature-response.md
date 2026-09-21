# Limiting Curvature as a Response Exponent

A 2026 analysis of quasitopological gravity formulates sufficient asymptotic
conditions on the inverse characteristic response that guarantee bounded
vacuum curvature invariants and relates them to Markov's limiting-curvature
hypothesis.

For the Hayward response used by this repository, those conditions can be
checked explicitly.

Reference:

P. Bueno, R. A. Hennigar, Á. J. Murcia, A. Vicente-Cano,
*Regular Geometries from Singular Matter in Quasi-Topological Gravity*,
Phys. Rev. D **114**, 024070 (2026).

## 1. Curvature response

Use the source variable

\[
s=\frac{2M}{r^3}
\]

and the Hayward curvature response

\[
\boxed{
\psi(s)
=
\frac{s}{1+\ell^2s}.
}
\]

The saturation value is

\[
\psi_*=\frac1{\ell^2}.
\]

## 2. First derivative

The response susceptibility is

\[
\psi'(s)
=
\frac1{(1+\ell^2s)^2}.
\]

For

\[
s\to\infty,
\]

\[
\boxed{
\psi'(s)
\sim
\frac1{\ell^4s^2}.
}
\]

Thus the effective asymptotic exponent is

\[
\boxed{
\beta=2.
}
\]

## 3. Second derivative

Similarly,

\[
\psi''(s)
=
-\frac{2\ell^2}
{(1+\ell^2s)^3},
\]

so

\[
\boxed{
\psi''(s)
\sim
-\frac{2}{\ell^4s^3}.
}
\]

This has the expected one-extra-power falloff relative to \(\psi'\).

## 4. Saturation gap

The distance to the limiting curvature is

\[
\frac1{\ell^2}-\psi
=
\frac1{
\ell^2(1+\ell^2s)
}.
\]

Therefore

\[
\boxed{
\frac1{\ell^2}-\psi
\sim
\frac1{\ell^4s}.
}
\]

The curvature approaches the limiting value algebraically even while the
source diverges.

## 5. Running response exponent

Define a scale-dependent response exponent

\[
\beta_{\rm eff}(s)
=
-
\frac{d\ln\psi'}{d\ln s}.
\]

For the Hayward response,

\[
\boxed{
\beta_{\rm eff}
=
\frac{
2\ell^2s
}{
1+\ell^2s
}.
}
\]

Hence

\[
\beta_{\rm eff}\to0
\qquad(s\to0),
\]

and

\[
\boxed{
\beta_{\rm eff}\to2
\qquad(s\to\infty).
}
\]

This gives a useful continuous diagnostic of when the screening regime has
been entered.

## 6. Interpretation

The 2026 quasitopological analysis states that vacuum theories in the relevant
infinite-tower class can satisfy Markov's limiting-curvature hypothesis:
curvature invariants are bounded by solution-independent scales.

The Hayward response supplies an explicit simple example of the underlying
mechanism:

\[
\boxed{
\text{source divergence}
\quad+\quad
\beta>1
\quad\Rightarrow\quad
\text{rapidly vanishing curvature susceptibility}.
}
\]

For this specific response,

\[
\beta=2.
\]

This is stronger and more invariantly meaningful than saying that a radial
effective Newton constant happens to vanish.

## 7. Matter caveat

The same 2026 work emphasizes that minimally coupled matter can spoil the
vacuum scaling responsible for a universal solution-independent curvature
bound, even when the resulting geometry remains regular.

Therefore a complete screening theory must test two separate statements:

\[
\boxed{
\text{regular geometry}
}
\]

and

\[
\boxed{
\text{universal limiting curvature independent of matter/source parameters}.
}
\]

They are not equivalent.

This matters directly for collapse, evaporation, and mass inflation, where
matter or semiclassical stress tensors cannot be ignored.

## 8. Selection criterion for the repo

The project will track

\[
\beta_{\rm eff}
=
-\frac{d\ln|\partial\psi/\partial s|}
{d\ln|s|}
\]

for candidate spherical response functions.

A useful high-source target is

\[
\boxed{
\lim_{|s|\to\infty}
\beta_{\rm eff}>1,
}
\]

combined with the stronger principal-safe conditions from
\`docs/principal-safe-screening.md\`.

This is a background-screening diagnostic, not by itself a perturbative
stability theorem.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/limiting_curvature_response.py
\`\`\`

to reproduce the large-source derivative coefficients and
\(\beta_{\rm eff}\to2\).
