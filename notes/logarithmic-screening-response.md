# Dimensionless Screening Response

The original working definition used the curvature susceptibility

\[
\frac{d\psi}{ds},
\]

where for the spherical Hayward response

\[
s=\frac{2M}{r^3},
\qquad
\psi=\frac{1-f}{r^2}.
\]

This is useful but there is a cleaner dimensionless measure.

## 1. Logarithmic response

Define

\[
\boxed{
\mathscr S
\equiv
\frac{d\ln\psi}{d\ln s}
=
\frac{s}{\psi}\frac{d\psi}{ds}.
}
\]

This measures the fractional change in physical curvature produced by a
fractional change in the source curvature scale.

Interpretation:

- \(\mathscr S=1\): GR-like unscreened linear response;
- \(0<\mathscr S<1\): partial screening;
- \(\mathscr S\to0\): additional source growth produces negligible fractional
  curvature growth.

## 2. Hayward response

For

\[
\psi(s)
=
\frac{s}{1+\ell^2s},
\]

we have

\[
\frac{d\psi}{ds}
=
\frac{1}{(1+\ell^2s)^2}.
\]

Hence

\[
\boxed{
\mathscr S(s)
=
\frac{1}{1+\ell^2s}.
}
\]

But

\[
1-\ell^2\psi
=
\frac{1}{1+\ell^2s},
\]

so

\[
\boxed{
\mathscr S
=
1-\ell^2\psi.
}
\]

On the black-hole solution,

\[
\boxed{
\mathscr S(r)
=
\frac{r^3}{r^3+2M\ell^2}.
}
\]

Thus the same radial factor previously compared to \(G_{\rm eff}/G\) is
exactly the logarithmic curvature response.

This interpretation is stronger because it does not require saying that
Newton's constant literally runs with radius.

## 3. Incremental versus average response

The average curvature response from the origin of response space is

\[
\frac{\psi}{s}.
\]

The incremental response is

\[
\frac{d\psi}{ds}.
\]

Their ratio is

\[
\boxed{
\frac{
d\psi/ds
}{
\psi/s
}
=
\mathscr S.
}
\]

So screening can be read as the incremental gravitational response becoming
small compared with the response accumulated at lower curvature.

## 4. Flow equation

The Hayward screening factor obeys a closed logarithmic flow,

\[
\boxed{
\frac{d\mathscr S}{d\ln s}
=
-\mathscr S(1-\mathscr S).
}
\]

The two fixed points are

\[
\mathscr S=1
\]

and

\[
\mathscr S=0.
\]

The first is the weak-curvature GR limit and the second is the saturated
high-curvature limit.

In this limited response-space sense the Hayward relation resembles a simple
RG flow from an unscreened to a screened fixed point.

This analogy should not be confused with an actual renormalization-group
derivation.

## 5. Relation to the limiting-curvature exponent

Previously we defined

\[
\beta_{\rm eff}
=
-
\frac{d\ln(d\psi/ds)}
{d\ln s}.
\]

For Hayward,

\[
\boxed{
\beta_{\rm eff}
=
2(1-\mathscr S).
}
\]

Therefore

\[
\mathscr S\to0
\]

corresponds to

\[
\beta_{\rm eff}\to2.
\]

The limiting-curvature and screening diagnostics are therefore two views of
the same response law.

## 6. Covariance status

This quantity is **not yet a general four-dimensional local scalar
definition**.

It is invariant under coordinate changes that preserve the physical
identification of the spherical solution because:

- \(r\) is the areal radius;
- \(M\) is the asymptotic mass parameter;
- \(\psi=(1-f)/r^2\) is the spherical curvature-response variable.

It should therefore be described as a **symmetry-covariant response
diagnostic**, not a fully background-independent definition of quantum
gravity.

A full theory needs a four-dimensional generalization.

## 7. Candidate full-theory generalization

For a local curvature theory with Lagrangian

\[
\mathcal L(g,R_{\mu\nu\rho\sigma}),
\]

define the generalized curvature momentum

\[
P^{\mu\nu\rho\sigma}
=
\frac{\partial\mathcal L}
{\partial R_{\mu\nu\rho\sigma}}.
\]

The curvature Hessian

\[
\mathcal C^{\mu\nu\rho\sigma}{}_{\alpha\beta\gamma\delta}
=
\frac{\partial P^{\mu\nu\rho\sigma}}
{\partial R^{\alpha\beta\gamma\delta}}
\]

is the natural covariant response tensor.

It also enters the highest-derivative part of the fluctuation equations in
generic higher-curvature theories.

This suggests that the ultimate definition of Spacetime Screening should be
formulated in terms of **physical eigenvalues of a reduced curvature-response
operator**, after constraints and gauge redundancies are removed.

The spherical quantity \(\mathscr S\) should then emerge as one eigenvalue or
one symmetry-reduced projection of that operator.

## 8. Updated working definition

At the spherical-response level:

\[
\boxed{
\text{Spacetime Screening}
\Longleftrightarrow
\mathscr S
=
\frac{d\ln\psi}{d\ln s}
\longrightarrow0.
}
\]

At the full-theory level, the desired generalization is:

\[
\boxed{
\text{physical curvature-response eigenvalues soften at high curvature}
}
\]

while the physical kinetic/principal operator remains finite, nondegenerate,
and hyperbolic.

This explicitly prevents the vector-model pathology in which the background
response was screened but the graviton characteristic remained singular.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/logarithmic_screening_response.py
\`\`\`

to verify the exact Hayward logarithmic response and its flow equation.
