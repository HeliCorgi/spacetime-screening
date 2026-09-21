# Nonlocal Zero-Free Form Factor: Minimal Ghost-Free Toy Test

The active v2 research direction is a nonlocal completion of
quasitopological gravity. The July 2026 preprint
arXiv:2607.07790 reports a completion that is ghost-free, avoids strong
coupling instabilities, retains exact spherical vacuum regular black holes,
and satisfies a perturbative Birkhoff theorem.

The full paper formulas were not imported into this repository at this stage.
This note instead records an independent, generic diagnostic that any
ghost-free infinite-derivative quadratic sector can be tested against.

## 1. Quadratic operator

Consider a schematic physical graviton operator

\[
\mathcal O(k^2)
=
k^2
\mathcal F\!\left(\frac{k^2}{M_*^2}\right).
\]

The propagator is

\[
\Pi(k^2)
\sim
\frac{1}
{k^2\mathcal F(k^2/M_*^2)}.
\]

If

\[
\mathcal F(z)
\]

has finite zeros, every zero generically introduces an additional propagator
pole.

Those additional poles can correspond to extra degrees of freedom and, in
higher-derivative gravity, often include ghosts.

## 2. Zero-free entire choice

A standard design class is

\[
\boxed{
\mathcal F(z)=e^{\gamma(z)}
}
\]

with \(\gamma(z)\) entire.

Because an exponential is never zero at finite complex argument,

\[
\boxed{
\mathcal F(z)\neq0
}
\]

everywhere in the finite complex plane.

A representative toy choice is

\[
\gamma(z)=z^2.
\]

Then

\[
\mathcal O(k^2)
=
k^2
e^{(k^2/M_*^2)^2},
\]

and, for positive Euclidean momentum magnitude,

\[
\boxed{
\Pi(k^2)
\sim
\frac{
e^{-(k^2/M_*^2)^2}
}{
k^2
}.
}
\]

The only finite pole is the GR massless pole,

\[
k^2=0.
\]

## 3. Infrared limit

As

\[
k^2\to0,
\]

\[
\mathcal F\to1,
\]

so

\[
\mathcal O(k^2)\sim k^2.
\]

Therefore the low-energy propagator reduces to the standard massless form.

This is a minimal consistency requirement for recovering GR.

## 4. UV behavior

For positive Euclidean \(k^2\),

\[
\Pi(k^2)
\sim
\frac{
e^{-(k^2/M_*^2)^2}
}{
k^2
}
\to0.
\]

Thus high-momentum propagation is exponentially suppressed in this toy
quadratic sector.

This does not by itself prove ultraviolet finiteness of a full interacting
gravity theory.

## 5. Contrast with a finite higher-derivative polynomial

Take

\[
\mathcal O_{\rm bad}(k^2)
=
k^2
\left(
1-\frac{k^2}{m_g^2}
\right).
\]

Then

\[
\mathcal O_{\rm bad}=0
\]

at both

\[
k^2=0
\]

and

\[
k^2=m_g^2.
\]

The propagator therefore contains an extra finite pole.

This is exactly the type of pole proliferation that zero-free entire form
factors are designed to avoid.

## 6. Relation to the vector-benchmark failure

The vector benchmark had the opposite pathology:

\[
\boxed{
S_{\rm vector}^{(2)}=0
}
\]

around its asymptotic vacuum.

That means the quadratic kinetic operator vanished rather than remaining
nonzero.

A principal-safe nonlocal completion should instead have a kinetic multiplier
that is:

1. nonzero for every finite physical momentum except the intended massless
   zero from \(k^2\);
2. finite or controllably defined on the background of interest;
3. free from sign changes that generate ghost kinetic eigenvalues;
4. compatible with a hyperbolic Lorentzian initial-value problem.

The zero-free entire toy passes only the first, simplest pole-counting test.

## 7. What remains to be checked on a regular black hole

Flat-space pole counting is not enough.

The vector benchmark already demonstrated why:

\[
\text{healthy/regular asymptotics}
\not\Rightarrow
\text{healthy core principal symbol}.
\]

For the nonlocal-QTG candidate the important calculation is therefore not
merely

\[
\Pi_{\rm Minkowski}(k),
\]

but the covariant fluctuation operator

\[
\delta^2S
\big|_{g=\bar g_{\rm RBH}}
\]

on the regular-black-hole background.

The project should extract:

- physical tensor/scalar sectors;
- nonlocal form factors evaluated on the curved background;
- characteristic or pseudodifferential principal structure;
- whether any effective kinetic coefficient vanishes at the center or
  horizons;
- whether the regular core remains regular for the fluctuation Green
  functions.

## 8. Status

This note is **not** a derivation of the specific July 2026
nonlocal-quasitopological theory.

It is a reproducible design benchmark implementing the generic mechanism

\[
\boxed{
\text{zero-free entire kinetic multiplier}
\Rightarrow
\text{no additional finite propagator zeros}
}
\]

at quadratic flat-space level.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/nonlocal_zero_free_form_factor.py
\`\`\`

to verify the IR limit, Euclidean UV suppression, and the difference between
the zero-free entire toy operator and a polynomial operator with an extra
finite pole.
