# Auxiliary Derivative Mixing as a Principal-Safety Failure Mode

The direct two-vector black-hole calculation exposes a reusable linear-algebra
mechanism.

Suppose a quadratic principal kinetic sector can be written as

\[
\mathcal L_{\rm kin}
=
\frac12\dot x^{\rm T}A\dot x
+
\dot x^{\rm T}B\dot y
+
\frac12\dot y^{\rm T}C\dot y,
\]

where:

- \(x\) denotes an already-healthy sector;
- \(A>0\) is its kinetic matrix;
- \(y\) denotes another set of perturbations;
- \(C\) is their direct kinetic matrix;
- \(B\) is derivative mixing.

This note records the resulting necessary condition for principal safety.

## 1. Schur complement

Because \(A\) is invertible,

\[
\mathcal L_{\rm kin}
=
\frac12
\left(
\dot x+A^{-1}B\dot y
\right)^{\rm T}
A
\left(
\dot x+A^{-1}B\dot y
\right)
+
\frac12
\dot y^{\rm T}
K_{\rm red}
\dot y,
\]

with

\[
\boxed{
K_{\rm red}
=
C-B^{\rm T}A^{-1}B.
}
\]

This is the kinetic Schur complement.

## 2. Auxiliary sector with no direct kinetic term

If

\[
C=0,
\]

then

\[
\boxed{
K_{\rm red}
=
-B^{\rm T}A^{-1}B.
}
\]

For any perturbation vector \(y\),

\[
y^{\rm T}K_{\rm red}y
=
-(By)^{\rm T}A^{-1}(By)
\le0.
\]

Thus every direction for which

\[
By\ne0
\]

has negative reduced kinetic sign.

The only zero directions satisfy

\[
By=0.
\]

## 3. Interpretation

This does **not** by itself prove a physical ghost in every constrained field
theory.

A zero/negative direction can still be absent from the physical phase space if
an independent gauge symmetry or constraint removes it.

The useful necessary condition is instead:

\[
\boxed{
\text{no direct kinetic}
+
\text{nonzero derivative mixing}
+
\text{surviving active mode}
\;\Rightarrow\;
\text{negative reduced kinetic sign}.
}
\]

Therefore any candidate regular-black-hole theory relying on auxiliary fields
with derivative curvature mixing must explicitly demonstrate which constraints
remove the active directions.

## 4. Application to the two-vector benchmark

The direct \(A-B\) expansion has one healthy odd metric kinetic direction and
two vector perturbations.

The vector sector has

\[
C=0
\]

at principal derivative order, while the metric-vector mixing vector is
nonzero.

Hence

\[
K_{\rm vec}
=
-\frac{cc^{\rm T}}{C_1}.
\]

The derivative-null vector combination lies in

\[
\ker c^{\rm T}.
\]

The direct full quadratic calculation then shows that this null combination is
an ordinary algebraic auxiliary field, while the active combination survives
the local constraint reduction.

That is why the general Schur-complement warning becomes an actual asymptotic
ghost in this benchmark.

## 5. How to evade the failure

A new candidate has several possible escape routes.

### A. Give the extra sector sufficient healthy direct kinetic energy

Require

\[
\boxed{
C-B^{\rm T}A^{-1}B>0.
}
\]

The direct kinetic matrix must dominate the negative mixing-induced Schur
term.

### B. Make the derivative mixing vanish on the physical branch

\[
B=0.
\]

Then the auxiliary sector does not inherit a kinetic term through the healthy
sector.

### C. Supply a genuine constraint/gauge degeneracy

The image of \(B\) must lie entirely in directions removed from the physical
phase space.

This must be established by a complete constraint analysis, not inferred from
the absence of a bare kinetic term.

## 6. Research use

This is not claimed as new mathematics.  It is elementary Schur-complement
linear algebra.

Its role in this repository is as a fast **principal-safety gate**:

> If a regular-black-hole construction introduces fields with no direct
> kinetic term but nonzero derivative mixing with the graviton, inspect the
> kinetic Schur complement before investing in the background geometry.

This test would have flagged the two-vector benchmark before the more detailed
core analysis.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/auxiliary_mixing_schur_lemma.py
\`\`\`

to verify the matrix identities and the rank-one two-auxiliary-field example.
