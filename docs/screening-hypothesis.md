# Screening Hypothesis

## 1. Diagnostic definition

For a static spherical metric,

\[
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2,
\]

one may write

\[
f(r)=1-\frac{2M G_{\rm diag}(r)}{r}.
\]

\(G_{\rm diag}(r)\) is a **diagnostic** extracted from the geometry. It is not assumed to be a fundamental coordinate-dependent coupling.

For a regular center,

\[
1-f(r)=O(r^2),
\]

so

\[
G_{\rm diag}(r)=O(r^3)
\]

or faster.

This provides a simple operational meaning for "screening" in spherical solutions.

## 2. Covariant formulation

A fundamental model should instead use a generally covariant scalar such as

\[
\mathcal I
=
\ell_*^4
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}.
\]

One possible response function is

\[
G_{\rm eff}(\mathcal I)
=
G_N\,S(\mathcal I),
\]

with

\[
S(0)=1,
\qquad
S'(\mathcal I)<0
\]

over the screening regime.

Examples worth testing include rational, exponential, and fixed-point-inspired forms.

A purely phenomenological example is

\[
S(\mathcal I)
=
\frac{1}{1+(\mathcal I/\mathcal I_*)^\alpha}.
\]

This is not yet a theory because inserting this function directly into Einstein's equations can violate consistency relations. It must arise from an action, effective action, or controlled nonlocal equation.

## 3. Order parameter

Introduce a field \(\chi\) with

\[
F(\chi)R
\]

as the effective gravitational prefactor. For example,

\[
F(\chi)=e^{\chi^2},
\qquad
G_{\rm eff}=\frac{G_N}{F(\chi)}.
\]

Let curvature modify the effective potential,

\[
V(\chi,\mathcal I)
=
\frac{\mu^2}{2}
\left(1-\frac{\mathcal I}{\mathcal I_*}\right)\chi^2
+
\frac{\lambda}{4}\chi^4.
\]

This produces a toy transition from \(\chi=0\) to a screened phase with \(\chi\neq0\).

The immediate tasks are to determine:

- whether the scalar introduces ghosts or tachyons;
- whether the Einstein-frame description is regular;
- whether the transition is continuous or first order;
- whether matter couples universally;
- whether collapse dynamically reaches the screened branch.

## 4. RG interpretation

If a covariant scale \(k\) can be identified,

\[
G(k)\sim \frac{g_*}{k^2}
\]

near a UV fixed point provides another screening mechanism for the dimensionful Newton coupling.

The hard part is the scale identification. A prescription \(k\sim1/r\) is generally coordinate- and model-dependent. A useful theory must define \(k\) through invariant physics or directly compute observables without relying on a heuristic substitution.

## 5. What screening must not mean

The project does not assume:

- that gravity literally turns off;
- that the dimensionless interaction strength vanishes;
- that Hawking temperature itself is the fundamental trigger;
- that a regular metric automatically gives a stable quantum theory;
- that a chosen \(G_{\rm eff}(r)\) is enough to define dynamics.

The target is a covariant mechanism whose spherical solutions *look* screened when expressed in an appropriate diagnostic.
