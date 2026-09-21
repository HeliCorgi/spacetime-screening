# Normalized Cotton Projectors: Smooth-Core Differentiability Warning

The August-2026 non-polynomial-gravity construction suggests a possible way
to avoid globally conformally-flat vacua: use exact non-conformally-flat
vacuum geometries.

This helps away from symmetry-enhanced points, but it does not by itself solve
the regular-core problem.

## 1. NPG normalized Cotton tensor

The NPG action uses a non-analytic tensor of the schematic form

\[
u^\mu{}_\nu
\sim
\frac{
C C
}{
C_{\alpha\beta\gamma}C^{\alpha\beta\gamma}
},
\]

where \(C_{\alpha\beta\gamma}\) is the Cotton tensor.

This tensor extracts a curvature-defined directional splitting.

The August-2026 source explicitly notes that the field equations become
ill-defined on conformally flat geometries and motivates non-conformally-flat
vacua as a way around that issue.

## 2. Smooth spherical centers are symmetry-enhanced

For a smooth single-function spherical center, Cartesian smoothness gives

\[
f(r)
=
1-c r^2+d r^4+O(r^6).
\]

The spherical Weyl scalar used in the NPG decomposition is

\[
\psi_W
=
\frac12 f''
-\frac{f'}{r}
-\frac{1-f}{r^2}.
\]

Substitution gives

\[
\boxed{
\psi_W
=
3d r^2+O(r^4).
}
\]

Hence the Weyl tensor vanishes at the center.

The Cotton tensor contains one derivative of this quantity and terms of order
\(\psi_W/r\), so

\[
\boxed{
C_{\alpha\beta\gamma}
=
O(r).
}
\]

Thus

\[
C^2=O(r^2).
\]

This is true even if the spacetime is non-conformally-flat at every finite
\(r>0\).

A smooth spherical center approaches a conformally-flat point.

## 3. Value regularity is not differentiability

Consider the finite-dimensional analogue

\[
U(v)
=
\frac{v v^{\rm T}}{v\cdot v}.
\]

Along

\[
v=\epsilon w,
\]

the value is finite and independent of \(\epsilon\):

\[
U(\epsilon w)
=
\frac{w w^{\rm T}}{w\cdot w}.
\]

However generic derivatives obey

\[
\boxed{
\frac{\partial U}{\partial v}
\sim
\epsilon^{-1},
}
\]

and

\[
\boxed{
\frac{\partial^2U}{\partial v^2}
\sim
\epsilon^{-2}.
}
\]

Replacing

\[
\epsilon\sim |C|\sim r
\]

gives the core scaling

\[
\boxed{
\delta u
\sim
r^{-1},
\qquad
\delta^2u
\sim
r^{-2}
}
\]

in generic off-background directions.

## 4. Consequence for a 4D NLQT base

A non-conformally-flat vacuum can make the NPG action well defined throughout
an open region with \(r>0\).

But if the regular black hole has a smooth spherical center, the Cotton and
Weyl tensors vanish in the \(r\to0\) limit.

Therefore a bare normalized Cotton/Weyl projector does not itself possess a
regular generic variation at the center.  However, the full NPQT densities
multiply such non-analytic structures by higher-order curvature numerators,
so a cancellation at the level of the complete action is possible in
principle.  The correct requirement is therefore to test whether the **full
rational density** admits a C² extension for which

\[
\mathcal L,\quad
\frac{\partial\mathcal L}{\partial R},\quad
\frac{\partial^2\mathcal L}{\partial R^2}
\]

have a regular extension to the center, unless the complete action exhibits a
nontrivial cancellation.

This means the non-conformally-flat-vacuum branch does **not automatically**
provide the differentiable 4D QT base needed by NLQT, but this note alone does
not prove that the complete NPQT action fails.

## 5. Stronger design rule

For a principal-safe regular spherical center, normalized curvature
projectors should trigger an explicit full-density extension test rather than
being accepted from their symmetry-reduced value alone.

Schematically, avoid

\[
\boxed{
\frac{T\otimes T}{T^2}
}
\]

whenever

\[
T\to0
\]

on the target solution.

This extends the earlier curvature-spectral-projector obstruction.

## 6. Literature status

The August-2026 NPG paper explicitly states that its theories are generically
non-analytic in Weyl/Cotton curvature data, that conformally-flat geometries
are only limiting solutions for these representatives, and that finding NPG
representatives whose black-hole perturbations are well-defined and
second-order remains an open direction.

Thus this repository is not treating the smooth-core differentiability issue
as solved by the existence of non-conformally-flat vacua.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/npg_cotton_projector_core.py
\`\`\`.


## 7. Important refinement: homogeneous full densities

The explicit 2025 NPQT representatives are not simply normalized projectors.
Their rational terms contain higher-degree curvature numerators.

Consequently a complete rational term can be homogeneous of positive degree
\(m\ge3\).  Along a fixed curvature-space ray whose denominator coefficient is
nonzero, such a term can scale as

\[
\mathcal Z_{\rm rat}=O(\epsilon^m),
\]

so its first and second derivatives may vanish as the maximally symmetric
point is approached.

This means the projector derivative estimate above is a **warning about the
building block**, not a completed Hessian calculation for the full NPQT
density.

However fixed-ray power counting is still insufficient.  A homogeneous
denominator can have nontrivial zero directions, and a path approaching such
a direction can invalidate continuity unless the full numerator cancels the
zero set strongly enough.

The remaining precise question is therefore:

\[
\boxed{
\text{Does each full NPQT rational density admit a C² covariant extension
across its denominator-zero set near the regular core?}
}
\]

See \`src/symbolic/npqt_homogeneous_c2_gate.py\` for a toy demonstration that
positive homogeneous degree alone does not guarantee such an extension.
