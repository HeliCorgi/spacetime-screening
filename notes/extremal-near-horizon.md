# Extremal Near-Horizon Geometry

This note studies the fully extremal regular branch of the current two-vector
benchmark.

In geometric units \(G=c=1\),

\[
f(r)
=
1-
\frac{2Mr^2}
{r^3+\frac{32}{27}M^3},
\]

with degenerate horizon

\[
\boxed{
r_h=\frac{4M}{3}
}.
\]

## 1. Double zero

At the horizon,

\[
f(r_h)=0,
\qquad
f'(r_h)=0.
\]

The second derivative is

\[
\boxed{
f''(r_h)=\frac{9}{8M^2}
}.
\]

Thus

\[
f(r)
=
\frac12f''(r_h)(r-r_h)^2+\cdots
=
\frac{9}{16M^2}(r-r_h)^2+\cdots.
\]

Writing

\[
f(r)
\simeq
\frac{(r-r_h)^2}{L_2^2},
\]

gives

\[
\boxed{
L_2=\frac{4M}{3}=r_h
}.
\]

## 2. Near-horizon product geometry

The near-horizon metric therefore becomes

\[
ds^2
\simeq
-\frac{\rho^2}{L_2^2}dt^2
+
\frac{L_2^2}{\rho^2}d\rho^2
+
r_h^2d\Omega^2,
\]

with

\[
L_2=r_h.
\]

This is

\[
\boxed{
AdS_2(L_2)\times S^2(r_h)
}
\]

with equal radii.

The structure is the same local product geometry that appears in the
near-horizon limit of extremal Reissner-Nordström, even though the global
black hole and underlying field content here are different.

## 3. Horizon curvature

The exact curvature invariants at the degenerate horizon are

\[
\boxed{
R_h=0
},
\]

\[
\boxed{
R_{\mu\nu}R^{\mu\nu}\big|_h
=
\frac{81}{64M^4}
},
\]

and

\[
\boxed{
K_h
=
\frac{81}{32M^4}
}.
\]

For a product \(AdS_2\times S^2\) with equal radius \(L=r_h\),

\[
R_{AdS_2}
=
-\frac{2}{L^2},
\qquad
R_{S^2}
=
+\frac{2}{L^2},
\]

so the total Ricci scalar cancels:

\[
R=0.
\]

The other invariants reproduce the exact black-hole values.

## 4. Maxwell-like effective stress tensor on the horizon

The effective Einstein-source reconstruction gives at \(r=r_h\),

\[
\boxed{
\rho_h
=
\frac{9}{128\pi M^2}
},
\]

\[
\boxed{
p_{r,h}=-\rho_h
},
\]

\[
\boxed{
p_{t,h}=+\rho_h
}.
\]

Therefore

\[
T^\mu{}_\mu
=
-\rho+p_r+2p_t
=
0
\]

on the horizon.

This is precisely the anisotropic equation-of-state pattern of a radial
Maxwell field:

\[
\boxed{
(-\rho,-\rho,+\rho,+\rho)
}.
\]

Indeed,

\[
\rho_h
=
\frac{1}{8\pi r_h^2},
\]

since \(r_h=4M/3\).

Thus the extremal horizon locally reproduces both the geometry and effective
stress structure associated with a Bertotti-Robinson-like extremal throat.

## 5. Relation to Aretakis instability

The published vector-black-hole paper explicitly flags the Aretakis
instability as an unresolved issue for its fully extremal solutions.

The present calculation explains why that concern is structurally natural:

- the surface gravity vanishes;
- the horizon is degenerate;
- the near-horizon throat is \(AdS_2\times S^2\);
- the throat has the same equal-radius geometry as extremal
  Reissner-Nordström.

This does **not** prove that the full coupled metric-vector system possesses
the same Aretakis instability. The conserved horizon quantities depend on the
actual perturbation equations.

It does show that eliminating mass inflation by making the black hole fully
extremal trades one instability question for another:

\[
\boxed{
\text{nonzero inner-horizon surface gravity}
\;\longrightarrow\;
\text{degenerate extremal throat}
}.
\]

The next non-radial perturbation calculation should therefore pay special
attention to zero-frequency / near-horizon modes.

## 6. Curvature hierarchy

For the fully extremal branch, the core Kretschmann scalar found previously is

\[
K_{\rm core}
=
\frac{2187}{32M^4}.
\]

At the horizon,

\[
K_h
=
\frac{81}{32M^4}.
\]

Therefore

\[
\boxed{
\frac{K_{\rm core}}{K_h}=27
}.
\]

The geometry remains finite everywhere, but the core still probes a curvature
scale 27 times larger than the extremal horizon in this invariant.

## 7. Proper throat distance

Because

\[
f(r)\sim\frac{(r-r_h)^2}{L_2^2},
\]

the proper radial distance on a static slice behaves as

\[
s
\sim
\int
\frac{dr}{\sqrt{f}}
\sim
L_2
\int
\frac{dr}{|r-r_h|}.
\]

Hence

\[
\boxed{
s\sim L_2\log|r-r_h|
}
\]

diverges as the horizon is approached.

This is another standard extremal-throat feature and is relevant to the
long-time behavior of perturbations.

## 8. Implication for Spacetime Screening

The fully extremal route successfully removes the ordinary mass-inflation
setup, but it produces a highly structured throat rather than a featureless
screened transition.

A viable completion must therefore answer both:

1. why the high-curvature core is regular;
2. why the extremal throat is dynamically acceptable.

The two questions cannot be collapsed into a single "singularity resolved"
criterion.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/extremal_near_horizon.py
\`\`\`

to verify the double zero, near-horizon radius, product-space curvature
invariants, Maxwell-like horizon stress tensor, and core/horizon curvature
ratio.
