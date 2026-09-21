# Test-Field Aretakis Instability on the Extremal Regular Branch

The fully extremal regular branch removes the usual nonzero-surface-gravity
inner-horizon setup that drives mass inflation. However, extremality introduces
a separate question: the Aretakis horizon instability.

This note derives the spherically symmetric massless-scalar version directly
for the extremal regular geometry.

The result is a **test-field statement**. It does not yet establish instability
of the full coupled metric-vector theory.

## 1. Geometry

Use ingoing Eddington-Finkelstein coordinates,

\[
ds^2
=
-f(r)dv^2
+
2\,dv\,dr
+
r^2d\Omega^2.
\]

For the fully extremal branch,

\[
f(r)
=
1-
\frac{2Mr^2}
{r^3+\frac{32}{27}M^3},
\]

and

\[
r_h=\frac{4M}{3}.
\]

At the horizon,

\[
f(r_h)=0,
\qquad
f'(r_h)=0,
\]

and

\[
\boxed{
f''(r_h)=\frac{2}{r_h^2}
}.
\]

## 2. S-wave massless scalar equation

Let

\[
\Phi=\Phi(v,r)
\]

be a minimally coupled massless scalar,

\[
\Box\Phi=0.
\]

For the metric above, the spherical wave equation is

\[
\boxed{
2\Phi_{vr}
+
\frac{2}{r}\Phi_v
+
f\Phi_{rr}
+
\left(
f'
+
\frac{2f}{r}
\right)\Phi_r
=
0
}.
\]

## 3. Horizon conservation law

Evaluate the equation at the extremal horizon.

Because

\[
f(r_h)=f'(r_h)=0,
\]

we obtain

\[
2\Phi_{vr}
+
\frac{2}{r_h}\Phi_v
=
0.
\]

Equivalently,

\[
\boxed{
\partial_v
\left(
\Phi_r+\frac{\Phi}{r_h}
\right)_{r=r_h}
=
0
}.
\]

Define

\[
\boxed{
H_0
=
\left[
\Phi_r+\frac{\Phi}{r_h}
\right]_{r=r_h}
}.
\]

Then

\[
\partial_vH_0=0.
\]

This is the \(l=0\) Aretakis conserved quantity for this extremal horizon.

## 4. Growth of the next transverse derivative

Differentiate the wave equation once with respect to \(r\), then evaluate at
the horizon.

Using

\[
f=f'=0,
\qquad
f''=\frac{2}{r_h^2},
\]

gives

\[
2\Phi_{vrr}
+
\frac{2}{r_h}\Phi_{vr}
-
\frac{2}{r_h^2}\Phi_v
+
\frac{2}{r_h^2}\Phi_r
=
0.
\]

From the horizon conservation equation,

\[
\Phi_{vr}
=
-\frac{\Phi_v}{r_h}.
\]

Therefore

\[
\boxed{
\Phi_{vrr}
=
\frac{2}{r_h^2}\Phi_v
-
\frac{1}{r_h^2}\Phi_r
}.
\]

If the scalar itself and its tangential derivative decay at late advanced
time,

\[
\Phi\to0,
\qquad
\Phi_v\to0,
\]

while the generic Aretakis constant is nonzero,

\[
H_0\ne0,
\]

then

\[
\Phi_r\to H_0.
\]

Hence asymptotically,

\[
\partial_v\Phi_{rr}
\to
-\frac{H_0}{r_h^2},
\]

so

\[
\boxed{
\Phi_{rr}
\sim
-\frac{H_0}{r_h^2}v
}
\]

up to subleading terms.

Thus the second transverse derivative grows linearly along the horizon.

## 5. Interpretation

The extremal regular geometry therefore supports the standard Aretakis
mechanism for a minimally coupled test scalar:

\[
\boxed{
\text{field decays}
\quad\text{while}\quad
\text{transverse derivatives fail to decay / grow}.
}
\]

This is not a curvature singularity of the background itself.

It is a horizon instability in perturbative derivatives.

The result is consistent with general analyses showing Aretakis constants and
transverse-derivative growth in broad classes of static spherically symmetric
extremal black holes.

## 6. Why this matters for Spacetime Screening

The fully extremal route was introduced to eliminate ordinary mass inflation.

The stability picture is therefore not

\[
\text{mass inflation removed}
\Rightarrow
\text{stable}.
\]

Instead it is

\[
\boxed{
\text{mass-inflation channel removed}
\quad\longrightarrow\quad
\text{extremal-horizon channel must be tested}.
}
\]

For the benchmark geometry, a test scalar already detects the latter channel.

The decisive question is whether the **coupled metric-vector physical modes**
have analogous conserved horizon quantities.

The published radial metric-vector calculation finds no nontrivial radial
linear modes, so the test scalar result does not contradict it. Aretakis
behavior may appear in non-radial gravitational/vector sectors or in external
matter fields even when the constrained radial vector sector is trivial.

## 7. Next calculation

The natural next target is odd-parity perturbations.

Reasons:

- they often have fewer constraint variables than the even-parity sector;
- they can expose tensor/vector kinetic signs and characteristic speeds;
- near an extremal horizon they provide a direct test of whether a physical
  metric-vector master variable has an Aretakis conserved quantity.

## References

- S. Aretakis, *Horizon Instability of Extremal Black Holes*,
  arXiv:1206.6598.

- J. Lucietti, K. Murata, H. S. Reall, N. Tanahashi,
  *On the horizon instability of an extreme Reissner-Nordström black hole*,
  JHEP **03** (2013) 035, arXiv:1212.2557.

- T. Katagiri and M. Kimura,
  *Aretakis constants and instability in general spherically symmetric
  extremal black hole spacetimes*,
  Phys. Rev. D **105**, 064062 (2022),
  https://doi.org/10.1103/PhysRevD.105.064062

- A. Eichhorn and P. G. S. Fernandes,
  *Regular black holes without mass-inflation instability and gravastars from
  modified gravity*,
  Phys. Rev. D **113**, L081501 (2026),
  https://doi.org/10.1103/nqz2-88zf

## Reproducibility

Run

\`\`\`bash
python src/symbolic/aretakis_test_scalar.py
\`\`\`

to verify the extremal horizon identities, the conserved \(l=0\) horizon
quantity, and the late-time linear growth coefficient for the second
transverse derivative under the stated decay assumption.
