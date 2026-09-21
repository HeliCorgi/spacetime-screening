# Sum/Difference Vector Basis: Where the Hidden Singularity Lives

The regular solution is easiest to understand after replacing the original
vectors \(A_\mu,B_\mu\) by

\[
U_\mu=\frac{A_\mu+B_\mu}{\sqrt2},
\qquad
V_\mu=\frac{A_\mu-B_\mu}{\sqrt2}.
\]

This basis separates a regular auxiliary profile from a singular,
divergence-free null profile.

## 1. Background profiles

On the regular branch,

\[
f(r)
=
1-\frac{2Mr^2}{r^3+2q\ell^2},
\]

\[
A=a(r)dv,
\qquad
B=b(r)dv.
\]

The sum/difference profiles are

\[
\boxed{
u(r)
=
\frac{\sqrt2Mr}
{r^3+2q\ell^2}
}
\]

and

\[
\boxed{
v(r)
=
-\frac{q}
{2\sqrt2\,r^2}
}.
\]

Thus

\[
U=u(r)dv,
\qquad
V=v(r)dv.
\]

## 2. One combination is regular

At the center,

\[
u(r)
\sim
\frac{M}{\sqrt2 q\ell^2}r.
\]

So

\[
\boxed{
U_\mu
\text{ is regular and vanishes linearly at }r=0.
}
\]

Its divergence is

\[
\boxed{
\nabla\cdot U
=
\frac{
6\sqrt2Mq\ell^2
}{
(r^3+2q\ell^2)^2
}
}.
\]

## 3. The other combination is singular but divergence-free

The difference field is exactly

\[
v(r)
=
-\frac{q}{2\sqrt2 r^2}.
\]

Therefore

\[
\boxed{
V_\mu\sim r^{-2}
}
\]

at the center.

Nevertheless,

\[
\boxed{
\nabla_\mu V^\mu=0.
}
\]

This explains why the singular profile can remain partially hidden in the
background equations.

It is Coulomb-like in its radial falloff but is a null auxiliary field rather
than a Maxwell field.

## 4. All simple scalar invariants vanish

Both fields are parallel to the same null covector \(dv\). Hence

\[
U^2=0,
\qquad
V^2=0,
\qquad
U\cdot V=0.
\]

Define the cross tensor

\[
T_{\mu\nu}
=
U_\mu V_\nu+V_\mu U_\nu.
\]

Even though its components diverge, its polynomial norm obeys

\[
T_{\mu\nu}T^{\mu\nu}
=
2U^2V^2+2(U\cdot V)^2
=
0.
\]

Thus the singular auxiliary structure is invisible to ordinary polynomial
scalar invariants.

This is a useful warning:

\[
\boxed{
\text{finite scalar invariants}
\not\Rightarrow
\text{all dynamical coefficients are regular}.
}
\]

## 5. The tensor-principal deformation is exactly this cross tensor

The original quadratic vector combination is

\[
A_\mu A_\nu-B_\mu B_\nu.
\]

In the new basis,

\[
\boxed{
A_\mu A_\nu-B_\mu B_\nu
=
U_\mu V_\nu+V_\mu U_\nu.
}
\]

Since \(U,V\) are parallel on the background, the profile amplitude is

\[
2uv
=
-\frac{Mq}
{r(r^3+2q\ell^2)}.
\]

Near the center,

\[
\boxed{
2uv
\sim
-\frac{M}{2\ell^2r}.
}
\]

This is precisely the \(1/r\) growth that enters the hidden Schwarzschild
tensor principal cone.

So the perturbative singularity can be traced to a very specific object:

\[
\boxed{
\text{regular }U
\times
\text{singular divergence-free }V.
}
\]

## 6. Interaction structure in the new basis

Let

\[
S=U^2+V^2,
\qquad
P=U\cdot V,
\]

and denote

\[
\Theta_U=\nabla\cdot U,
\qquad
\Theta_V=\nabla\cdot V.
\]

The Einstein-tensor term becomes

\[
\boxed{
4G^{\mu\nu}
(A_\mu A_\nu-B_\mu B_\nu)
=
8G^{\mu\nu}U_\mu V_\nu.
}
\]

The cubic difference becomes

\[
\boxed{
8\left(
A^2\nabla\cdot A
-
B^2\nabla\cdot B
\right)
=
4\sqrt2\,S\Theta_V
+
8\sqrt2\,P\Theta_U.
}
\]

The quartic difference is

\[
\boxed{
6\left[
(A^2)^2-(B^2)^2
\right]
=
12SP.
}
\]

Thus the theory is not best interpreted as "one good vector minus one ghost
vector."

It is an off-diagonal constrained \(U\)-\(V\) system.

## 7. Background simplification versus perturbations

On the exact background,

\[
S=P=0,
\qquad
\Theta_V=0.
\]

This kills many terms in the background action/equations.

But perturbations need not preserve these equalities at first nontrivial
order.

This is why a background can look exceptionally regular even though its
quadratic fluctuation operator remembers the singular \(V\) profile.

## 8. Design lesson for a replacement screening theory

The current vector benchmark suggests a stronger regularity criterion than
finite metric curvature:

A viable screening completion should require not only

\[
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}<\infty,
\]

but also that every background structure entering a physical principal symbol
remain regular.

Schematically,

\[
\boxed{
\text{metric regularity}
+
\text{principal-symbol regularity}
+
\text{constraint regularity}.
}
\]

A model that relies on cancellation between individually singular auxiliary
fields should be treated as suspect until all three are checked.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/sum_difference_basis.py
\`\`\`

to verify the exact \(U,V\) profiles, their divergences, the cross-tensor
amplitude, and the algebraic rewriting of the interaction.
