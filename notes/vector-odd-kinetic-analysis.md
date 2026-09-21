# Two-Vector Odd Sector: Kinetic Matrix and \(l=1\) Ghost Diagnostic

This note advances the P0 calculation proposed in \`NOVELTY.md\`.

The starting point is the published odd-parity quadratic-action formalism for
generalized Proca / quartic vector-tensor black holes:

R. Kase, M. Minamitsuji, S. Tsujikawa, Y.-L. Zhang,
*Black hole perturbations in vector-tensor theories: The odd-mode analysis*,
JCAP **02** (2018) 048,
arXiv:1801.01787.

The paper derives, for \(l\ge2\), a quadratic action containing

\[
C_1X_g^2
+
2(C_2\dot u+C_3u'+\cdots)X_g
+
C_5\dot u^2
+
C_7u'^2
+\cdots,
\]

where

\[
X_g
=
\dot W-Q'+\frac{2Q}{r}.
\]

After the nondynamical metric variables are removed, the one-vector kinetic
coefficient is

\[
\boxed{
q_2
=
C_5-\frac{C_2^2}{C_1}.
}
\]

The source literature requires \(q_2>0\) for absence of an odd vector ghost.

## 1. Mapping to the current two-vector model

The benchmark action is

\[
S
=
\frac{1}{16\pi G}
\int d^4x\sqrt{-g}
\left[
R+\ell^2(\mathcal L[A]-\mathcal L[B])
\right],
\]

with

\[
\mathcal L[W]
=
4G^{\mu\nu}W_\mu W_\nu
+
8W^2\nabla_\mu W^\mu
+
6(W^2)^2.
\]

The odd-sector derivative mixing comes from the Einstein-tensor / quartic
generalized-Proca interaction.

There is **no Maxwell term**

\[
-\frac14F_{\mu\nu}F^{\mu\nu},
\]

so the direct transverse-vector kinetic and radial-gradient coefficients
corresponding to \(C_5,C_6,C_7\) vanish.

For the two odd vector perturbations

\[
u
=
\begin{pmatrix}
u_A\\
u_B
\end{pmatrix},
\]

define the mixing vector

\[
c
=
\begin{pmatrix}
C_{2A}\\
C_{2B}
\end{pmatrix}.
\]

The direct two-field extension of the published kinetic reduction is then

\[
\boxed{
K_{\rm vec}
=
-\frac{cc^{\rm T}}{C_1}.
}
\]

## 2. Kinetic signature

Because this is an outer product,

\[
\det K_{\rm vec}=0.
\]

Its nonzero eigenvalue is

\[
\boxed{
\lambda_{\rm vec}
=
-\frac{C_{2A}^2+C_{2B}^2}{C_1}.
}
\]

In the static exterior,

\[
C_1>0.
\]

Therefore, whenever the background vector hair is nonzero,

\[
\boxed{
\lambda_{\rm vec}<0.
}
\]

The derivative-active eigenvector is parallel to

\[
(C_{2A},C_{2B}),
\]

while the orthogonal combination has zero principal quadratic kinetic term.

Thus the high-frequency odd vector sector contains:

\[
\boxed{
\text{one negative-kinetic combination}
+
\text{one kinetically degenerate combination}.
}
\]

This is stronger than the earlier observation that the vector action vanishes
quadratically on exact asymptotic Minkowski space.

## 3. Exact regular branch

For the regular branch,

\[
D=r^3+2q\ell^2,
\]

\[
f
=
1-\frac{2Mr^2}{D},
\]

\[
a
=
\frac{r-rf-q/2}{2r^2},
\qquad
b
=
\frac{r-rf+q/2}{2r^2}.
\]

The quartic slopes have opposite signs,

\[
\beta_A=+4\ell^2,
\qquad
\beta_B=-4\ell^2.
\]

For the null background,

\[
C_{2A}
=
-\frac{\beta_Aa}{2fr^2},
\qquad
C_{2B}
=
-\frac{\beta_Bb}{2fr^2}.
\]

Using the Einstein-Hilbert value

\[
C_1=\frac1{2r^2},
\]

the nonzero vector kinetic eigenvalue becomes

\[
\boxed{
\lambda_{\rm vec}
=
-\frac{
8\ell^4(a^2+b^2)
}{
f^2r^2
}.
}
\]

Also,

\[
a^2+b^2
=
\frac{2M^2r^2}{D^2}
+
\frac{q^2}{8r^4}.
\]

Hence near the regular center,

\[
\boxed{
\lambda_{\rm vec}
\sim
-\frac{\ell^4q^2}{r^6}.
}
\]

The metric background is finite-curvature, but the induced odd-vector kinetic
coefficient diverges negatively.

At large radius the coefficient approaches zero from below as \(r^{-6}\),
consistent with the previously identified asymptotic kinetic degeneracy.

## 4. Radial principal matrices

For a null background,

\[
C_{3i}=-fC_{2i}.
\]

With no direct \(C_5,C_6,C_7\) block, the reduced vector principal matrices are

\[
\boxed{
K
=
-\frac{cc^{\rm T}}{C_1},
}
\]

\[
\boxed{
R=-2fK,
}
\]

and

\[
\boxed{
G=f^2K.
}
\]

Therefore the radial high-frequency principal polynomial factorizes as

\[
\boxed{
P_{\rm vec}(\omega,k)
=
(\omega+fk)^2K.
}
\]

The derivative-active vector combination therefore has the double
characteristic

\[
\boxed{
\omega=-fk.
}
\]

The orthogonal vector combination has no principal quadratic operator.

## 5. Why the \(l=1\) sector is especially useful

For odd dipole perturbations,

\[
l=1,
\qquad
L=l(l+1)=2,
\]

all terms proportional to \(L-2\) vanish.

The standard generalized-Proca analysis shows that the local gravitational
odd mode becomes nondynamical for \(l=1\), while the intrinsic vector
perturbation is the propagating local mode.

For two vectors, the principal derivative action reduces to

\[
\mathcal L_{\rm pr}
=
C_1X_g^2
+
2YX_g,
\]

with

\[
Y
=
c^{\rm T}\dot u
+
d^{\rm T}u'.
\]

Completing the square,

\[
\mathcal L_{\rm pr}
=
C_1
\left(
X_g+\frac{Y}{C_1}
\right)^2
-
\frac{Y^2}{C_1}.
\]

The metric dipole is nondynamical.  On the null branch,

\[
d=-fc,
\]

so the local vector derivative action is

\[
\boxed{
\mathcal L_{l=1,\rm vec}^{\rm pr}
=
-\frac1{C_1}
\left[
c^{\rm T}
(\dot u-fu')
\right]^2.
}
\]

This makes the sign transparent.

Define the derivative-active normalized combination \(y\) along \(c\).  Then

\[
\mathcal L
=
-A_{\rm ghost}
(\dot y-fy')^2,
\qquad
A_{\rm ghost}
=
\frac{c^{\rm T}c}{C_1}>0.
\]

Its canonical momentum is

\[
p
=
-2A_{\rm ghost}(\dot y-fy'),
\]

and the principal Hamiltonian density contains

\[
\boxed{
\mathcal H
=
-\frac{p^2}{4A_{\rm ghost}}
+
fp\,y'
+\cdots.
}
\]

The quadratic momentum term is unbounded below.

This provides a cleaner ghost diagnostic than the \(l\ge2\) tensor
characteristic question because there is no local odd gravitational-wave mode
to confuse with the negative vector kinetic combination.

## 6. Current interpretation

The present result strongly suggests that the two-vector regular-black-hole
benchmark has an odd-parity ghost in the derivative-active vector
combination.

However, the project will still label this a

\[
\boxed{\text{NEW CALCULATION CANDIDATE}}
\]

rather than a theorem until the complete two-vector \(l=1\) and \(l\ge2\)
quadratic action is derived directly from the original action rather than by
multi-field extension of the published one-vector coefficient structure.

The remaining publication-level checks are:

1. perform the angular harmonic expansion of both vectors directly;
2. reproduce the \(C_{2A},C_{2B},C_{3A},C_{3B}\) coefficients from the
   original two-vector action;
3. include all lower-derivative \(C_4,C_{11},C_{13}\)-type terms;
4. verify the full primary/secondary constraint count;
5. confirm that the negative-kinetic combination is not removed by an
   additional degeneracy unique to the \(A-B\) action.

Lower-derivative terms cannot change a nonzero high-frequency kinetic sign,
but a previously unidentified constraint could remove the mode entirely.

## 7. Relation to the hidden Schwarzschild tensor characteristic

The same odd quadratic-action coefficients also strengthen the earlier
tensor-principal result.

For the pure metric odd principal block, define

\[
\Delta
=
4\ell^2(a^2-b^2).
\]

The coefficients obey

\[
C_8
=
-\frac{f+\Delta}{2r^4},
\]

\[
D_{WQ}
=
\frac{\Delta}{fr^4},
\]

\[
C_{10}
=
\frac{f-\Delta}{2f^2r^4}.
\]

The radial characteristic discriminant simplifies to

\[
D_{WQ}^2-4C_8C_{10}
=
\frac1{r^8}.
\]

The two coordinate characteristic roots are

\[
v_-=-f,
\]

and

\[
v_+
=
f\frac{f+\Delta}{f-\Delta}.
\]

On the exact regular branch,

\[
\boxed{
f+\Delta
=
1-\frac{2M}{r}.
}
\]

Thus the hidden Schwarzschild factor is not merely a background algebraic
coincidence: it appears directly in the standard odd quadratic-action
principal block.

The final question is whether the same factor remains in the **fully reduced
physical \(l\ge2\) tensor master equation** after the two vector auxiliaries
and nondynamical metric variable are eliminated.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/vector_odd_kinetic_matrix.py
python src/symbolic/vector_odd_reduced_principal.py
python src/symbolic/vector_l1_odd_ghost.py
\`\`\`

to reproduce the negative-semidefinite two-vector kinetic matrix, the radial
vector principal polynomial, the \(l=1\) Hamiltonian sign, and the
Schwarzschild factor in the odd metric principal block.


## 8. Reduced tensor kinetic coefficient and characteristic horizon

The standard odd-action tensor block can be pushed one step further.

Define

\[
\Delta
=
4\ell^2(a^2-b^2).
\]

On the single-function null background,

\[
C_1=\frac1{2r^2},
\]

\[
C_8
=
-\frac{f+\Delta}{2r^4},
\]

\[
D_{WQ}
=
\frac{\Delta}{fr^4},
\]

and

\[
C_{10}
=
\frac{f-\Delta}{2f^2r^4}.
\]

The characteristic discriminant is exactly

\[
\boxed{
D_{WQ}^2-4C_8C_{10}
=
\frac1{r^8}.
}
\]

The reduced tensor kinetic coefficient is

\[
\boxed{
q_T
=
\frac{f-\Delta}{2f^2}.
}
\]

The radial coordinate characteristics are

\[
\boxed{
v_-=-f,
}
\]

and

\[
\boxed{
v_+
=
f\frac{f+\Delta}{f-\Delta}.
}
\]

On the exact regular branch,

\[
\boxed{
f+\Delta
=
1-\frac{2M}{r}.
}
\]

Therefore

\[
\boxed{
r_T=2M
}
\]

is a tensor characteristic horizon.

At that radius the background metric itself is regular and static:

\[
f(2M)
=
\frac{q\ell^2}{4M^3+q\ell^2}
>0.
\]

Moreover,

\[
\boxed{
q_T(2M)
=
\frac1{f(2M)}
>0.
}
\]

So \(r=2M\) is not a tensor ghost surface.  It is a genuine candidate
characteristic horizon of the odd tensor principal block.

Toward the regular metric core,

\[
\boxed{
q_T
\sim
\frac{M}{r}
}
\]

diverges positively.

Hence the tensor kinetic sign remains positive while its characteristic
geometry retains the Schwarzschild-type singular structure.

This substantially strengthens the original local-TT calculation: the hidden
factor \(1-2M/r\) now appears directly in the standard Regge-Wheeler
high-frequency coefficient block.

The final independent check remains a direct two-vector harmonic expansion
from the original action.

## 9. Updated status

The vector benchmark now has **two logically independent problems**:

1. an odd vector negative-kinetic mode candidate, already visible in \(l=1\);
2. a regular-background / singular-characteristic mismatch in the tensor
   sector.

Either one would prevent the model from satisfying the repository's
principal-safe screening criterion if confirmed by direct expansion.
