# Degeneracy of the Explicit 4D Covariant Lift

This note analyzes the explicit representative four-dimensional lift used in

Johanna Borissova and Raúl Carballo-Rubio,
*Regular black holes from pure gravity in four dimensions*,
Phys. Rev. D **113**, 124004 (2026),
https://doi.org/10.1103/6x2z-qbkh

The paper constructs four-dimensional covariant densities
\(\mathcal H,\mathcal T,\mathcal P,\mathcal K\) whose restriction to generic
warped-product geometries reproduces the two-dimensional variables
\(\eta,\tau,\psi,\mathcal R\).

The important result here is:

\[
\boxed{
\text{the displayed rational lift for }\mathcal P,\mathcal K
\text{ is }0/0\text{ on the exact single-function branch}.
}
\]

The spherical reduced action remains perfectly finite. The issue concerns
using this particular four-dimensional representative away from spherical
symmetry, for example to derive a tensor principal symbol.

## 1. Representative action

The paper gives the four-dimensional action

\[
S[g]
=
\int d^4x\sqrt{-g}
\left[
H_2(\mathcal P)
-H_3(\mathcal P)\mathcal H
+H_4(\mathcal P)\mathcal K
+2H_4'(\mathcal P)(\mathcal H^2-\mathcal T)
\right].
\]

The lift is explicitly presented as one exemplary construction, and the
authors emphasize that different choices of four-dimensional curvature
invariants lead to inequivalent lifts that agree after spherical reduction.

## 2. Common denominator

The displayed densities \(\mathcal P\) and \(\mathcal K\) contain

\[
D
=
I_{C^2}I_{R^2C}
+
2I_{\hat R^2}I_{C^3}.
\]

On a generic warped-product geometry define

\[
\Omega=\mathcal R+2\eta+2\psi,
\]

and

\[
A
=
\eta^2-2\tau.
\]

Using the invariant identities in the paper,

\[
I_{C^2}=\frac{\Omega^2}{3},
\qquad
I_{C^3}=\frac{\Omega^3}{18},
\]

and the relevant Ricci/Weyl contractions, direct symbolic reduction gives

\[
\boxed{
D
=
-\frac13
A\Omega^3.
}
\]

## 3. Numerators vanish by the same factor

For the ratio appearing in \(\mathcal P\),

\[
N_{\mathcal P}
=
I_{\hat R^3}I_{C^3},
\]

we find

\[
\boxed{
N_{\mathcal P}
=
-\frac1{12}
A(\mathcal R-2\psi)\Omega^3.
}
\]

For the complete numerator of \(\mathcal K\),

\[
\boxed{
N_{\mathcal K}
=
-\frac13
\mathcal R A\Omega^3.
}
\]

Therefore, when \(A\neq0\), cancellation gives the required reduced values,

\[
\boxed{
\mathcal P=\psi,
\qquad
\mathcal K=\mathcal R.
}
\]

Similarly,

\[
\mathcal H=\eta,
\qquad
\mathcal T=\tau.
\]

So the construction works exactly as designed on a generic warped product.

## 4. The single-function branch sits on the singular surface

The static single-function ansatz is

\[
ds^2
=
-f(r)dt^2
+
\frac{dr^2}{f(r)}
+
r^2d\Omega^2.
\]

For this ansatz,

\[
\tau
=
\frac{\eta^2}{2}
\]

identically.

Hence

\[
\boxed{
A=\eta^2-2\tau=0
}
\]

at every radius, not only at the center.

Consequently,

\[
\boxed{
D=N_{\mathcal P}=N_{\mathcal K}=0.
}
\]

Thus the literal four-dimensional rational formulas give

\[
\frac00
\]

everywhere on the exact Hayward branch.

## 5. Why the spherical calculation is still finite

Introduce an off-branch regulator

\[
A=\delta.
\]

Then

\[
D
=
-\frac13\delta\Omega^3,
\]

and the ratios satisfy

\[
\frac{N_{\mathcal P}}{D}
=
\frac{\mathcal R-2\psi}{4},
\]

\[
\frac{N_{\mathcal K}}{D}
=
\mathcal R.
\]

Therefore the limit

\[
\delta\to0
\]

inside the warped-product family is removable and gives

\[
\mathcal P\to\psi,
\qquad
\mathcal K\to\mathcal R.
\]

This is why the reduced spherical action and its Hayward solution remain
well-defined.

## 6. The off-branch gradients are not removable

A nonspherical perturbation does not merely evaluate \(\mathcal P\) and
\(\mathcal K\); it varies them with respect to independent four-dimensional
curvature components.

Treating the Zakhary-McIntosh invariants as independent variables,

\[
\frac{\partial\mathcal P}
{\partial I_{\hat R^3}}
=
-\frac{I_{C^3}}{D},
\]

and

\[
\frac{\partial\mathcal K}
{\partial I_{\hat R^3}}
=
\frac{2I_{C^3}}{D}.
\]

On the regulated warped-product family,

\[
I_{C^3}
=
\frac{\Omega^3}{18},
\qquad
D=-\frac13\delta\Omega^3,
\]

so

\[
\boxed{
\frac{\partial\mathcal P}
{\partial I_{\hat R^3}}
=
\frac{1}{6\delta}
}
\]

and

\[
\boxed{
\frac{\partial\mathcal K}
{\partial I_{\hat R^3}}
=
-\frac{1}{3\delta}.
}
\]

The values of the ratios have a removable limit, but their generic
four-dimensional gradients do not.

## 7. Could the full action cancel the divergence?

In principle, divergent gradients of individual densities could cancel after
they are combined in the complete action.

For the representative action, the potentially divergent derivative is

\[
\frac{\partial\mathcal L}
{\partial I_{\hat R^3}}
=
\frac{\mathcal B}{6\delta},
\]

where on the single-function branch

\[
\mathcal B
=
H_2'
-\eta H_3'
+\mathcal R H_4'
+\eta^2H_4''
-2H_4.
\]

Using the quasitopological single-function identities,

\[
H_2'
=
\frac12
\left(
H_3-2\psi H_3'
\right),
\]

and

\[
H_3
=
4H_4-4\psi H_4',
\]

this simplifies to

\[
\boxed{
\mathcal B
=
(\mathcal R-2\psi)H_4'
+
(\eta+2\psi)^2H_4''.
}
\]

Therefore a finite first variation of this representative lift requires the
additional condition

\[
\boxed{
(\mathcal R-2\psi)H_4'
+
(\eta+2\psi)^2H_4''
=
0
}
\]

along the background.

This condition is not one of the spherical quasitopological identities.

For the explicit Hayward \(H_4\) given in the paper, direct substitution shows
that it is not an identity. In units \(M=\ell=r=1\), for example,

\[
\boxed{
\mathcal B
=
4+\frac{16}{3}\ln2
\neq0.
}
\]

Thus the first variation of this particular representative four-dimensional
lift is generically singular when approached in a generic invariant
direction.

## 8. What this does *not* mean

This result does **not** show that the spherical Hayward solution is wrong.

It does **not** show that every four-dimensional pure-gravity realization of
the reduced quasitopological theory is singular.

It does **not** invalidate the curvature-response relation

\[
\frac{\psi}{1-\ell^2\psi}
=
\frac{2M}{r^3}.
\]

The paper explicitly stresses that the four-dimensional lifting procedure is
nonunique: different choices of invariants yield inequivalent theories away
from the warped-product sector.

The correct conclusion is narrower:

\[
\boxed{
\text{the specific rational representative lift written in Eqs. (55),(63)-(66)}
}
\]

cannot be naively used as a regular nonspherical perturbation theory on the
single-function branch without specifying a regular off-branch extension.

## 9. Relation to the authors' EFT caveat

The paper itself describes these nonpolynomial theories as a proof of
principle and notes that:

- there are infinitely many inequivalent four-dimensional actions with the
  same spherical reduction;
- such nonpolynomial actions may have pathological properties on generic
  backgrounds;
- their relation to a standard gravitational effective-field-theory
  expansion is not immediate.

The present calculation provides a concrete example of that warning.

## 10. A branch-adapted square-root lift also becomes nondifferentiable

One can avoid the branch-wide \(0/0\) value by using the traceless-Ricci norm
directly on the single-function branch.

There,

\[
I_{\hat R^2}
=
\frac14(\mathcal R-2\psi)^2.
\]

Together with

\[
I_R
=
\mathcal R-4\eta+2\psi,
\]

this gives, on a branch of fixed sign,

\[
\psi
=
\eta+\frac{I_R}{4}
\pm\frac12\sqrt{I_{\hat R^2}}.
\]

For the Hayward solution,

\[
\mathcal R-2\psi<0
\]

for finite \(r>0\), so the appropriate branch is

\[
\boxed{
\psi
=
\eta+\frac{I_R}{4}
+\frac12\sqrt{I_{\hat R^2}}.
}
\]

This reconstructs the correct value without the \(0/0\).

However,

\[
\frac{\partial\psi}
{\partial I_{\hat R^2}}
=
\frac{1}{4\sqrt{I_{\hat R^2}}},
\]

which diverges when the traceless Ricci tensor vanishes.

For Hayward,

\[
I_{\hat R^2}
=
\frac{
1296M^4\ell^4r^6
}{
(r^3+2M\ell^2)^6
},
\]

so it vanishes both at the de Sitter core and asymptotically.

Thus the square-root alternative trades a value singularity for a
differentiability singularity.

See
\`src/symbolic/branch_adapted_lift.py\`.

## 11. Weyl-ratio densities have additional degeneracy surfaces

The representative density

\[
\mathcal H
=
-\frac16 I_R
+
\frac{I_{C^3}}{I_{C^2}}
\]

contains a Weyl-invariant ratio.

On a warped product,

\[
I_{C^2}
=
\frac{\Omega^2}{3},
\qquad
I_{C^3}
=
\frac{\Omega^3}{18},
\]

so after cancellation,

\[
\frac{I_{C^3}}{I_{C^2}}
=
\frac{\Omega}{6}.
\]

But the literal four-dimensional derivatives are

\[
\boxed{
\frac{\partial\mathcal H}{\partial I_{C^3}}
=
\frac{3}{\Omega^2},
}
\]

and

\[
\boxed{
\frac{\partial\mathcal H}{\partial I_{C^2}}
=
-\frac{1}{2\Omega}.
}
\]

For the Hayward solution,

\[
\Omega(r)
=
\frac{
12Mr^3(r^3-4M\ell^2)
}{
(r^3+2M\ell^2)^3
}.
\]

Therefore

\[
\Omega=0
\]

at

\[
r=0,
\qquad
r^3=4M\ell^2,
\]

and \(\Omega\to0\) at infinity.

So the representative Weyl-ratio lift possesses additional
nondifferentiable surfaces even apart from the branch-wide
\(\mathcal P,\mathcal K\) degeneracy.

See
\`src/symbolic/weyl_ratio_degeneracy.py\`.

## 12. Consequence for the tensor-principal-symbol program

The original next step was:

\[
\text{take the explicit 4D Hayward action}
\rightarrow
\text{compute the TT Hessian}.
\]

For this representative lift that procedure is ill-defined before the lift is
regularized, because the exact background lies on the singular invariant
surface

\[
D=0.
\]

The next meaningful options are therefore:

1. construct a different covariant lift whose densities are regular on the
   single-function branch;
2. work with a polynomial/infinite-tower quasitopological realization where
   no rational projector of this type is needed;
3. use the nonlocal quasitopological completion and extract its actual
   quadratic operator;
4. define the theory fundamentally through the reduced spherical sector only,
   in which case nonspherical perturbations are outside its domain and it
   cannot yet serve as a full four-dimensional screening theory.

## 13. Updated design lesson

The project now has a fourth regularity requirement in addition to metric and
principal-symbol regularity:

\[
\boxed{
\text{covariant-lift regularity}.
}
\]

A four-dimensional action intended as a fundamental or effective completion
must be differentiable on the background in the directions needed to define
its physical perturbations.

Having a finite symmetry-reduced action is not sufficient.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/covariant_lift_degeneracy.py
python src/symbolic/covariant_lift_action_gradient.py
python src/symbolic/branch_adapted_lift.py
python src/symbolic/weyl_ratio_degeneracy.py
\`\`\`

to verify the common factor, the removable spherical ratios, the divergent
four-dimensional invariant gradients, and the additional first-variation
cancellation condition.
