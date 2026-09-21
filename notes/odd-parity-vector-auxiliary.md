# Odd-Parity Vector Sector: Auxiliary Constraint Structure

This note isolates the odd-parity vector perturbations of the current
two-vector benchmark before deriving the full coupled Regge-Wheeler system.

The key result is simple:

\[
\boxed{
\text{the axial vector perturbations are algebraic auxiliaries}
}
\]

on the regular spherical background.

They do not carry their own second-order wave operator.

## 1. Vector equation

For one vector sector,

\[
\mathcal L[W]
=
4G^{\mu\nu}W_\mu W_\nu
+
8W^2\nabla_\mu W^\mu
+
6(W^2)^2.
\]

Varying with respect to \(W_\mu\) and removing an overall factor gives

\[
\boxed{
\mathcal E^\mu
=
G^{\mu\nu}W_\nu
+
2W^\mu\nabla_\alpha W^\alpha
-
\nabla^\mu(W^2)
+
3W^2W^\mu
=
0
}.
\]

The overall sign of the \(A\) and \(B\) sectors does not change their separate
vector equations.

## 2. Background

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

The regular branch has

\[
f(r)
=
1-
\frac{2Mr^2}{r^3+2q\ell^2},
\]

with

\[
A_\mu dx^\mu=a(r)dv,
\qquad
B_\mu dx^\mu=b(r)dv.
\]

The profiles are

\[
a(r)
=
\frac{r-rf-q/2}{2r^2},
\]

\[
b(r)
=
\frac{r-rf+q/2}{2r^2}.
\]

Both are null:

\[
A^2=B^2=0.
\]

Because \(g^{rv}=1\),

\[
A^\mu\partial_\mu=a(r)\partial_r,
\qquad
B^\mu\partial_\mu=b(r)\partial_r.
\]

Their divergences are

\[
\nabla_\mu A^\mu
=
a'+\frac{2a}{r},
\]

\[
\nabla_\mu B^\mu
=
b'+\frac{2b}{r}.
\]

The difference between \(a\) and \(b\) contains a pure \(r^{-2}\) term, whose
spherical divergence vanishes. Therefore

\[
\boxed{
\nabla\cdot A
=
\nabla\cdot B
=
\frac{
6Mq\ell^2
}{
(r^3+2q\ell^2)^2
}
}.
\]

## 3. Odd-parity vector perturbation

For an axial vector harmonic \(S_A^{\ell m}\), write schematically

\[
\delta W_A
=
w(v,r) S_A^{\ell m}.
\]

The axial harmonic is divergence-free on the two-sphere,

\[
D^A S_A^{\ell m}=0.
\]

At linear order in the odd sector:

\[
\delta(W^2)=0,
\]

because the background vector has no angular component, and

\[
\delta(\nabla\cdot W)=0
\]

for the pure axial perturbation.

Therefore the angular vector equation contains no derivative acting on
\(w\).

The coefficient multiplying the angular perturbation is

\[
\boxed{
C(r)
=
G^\theta{}_\theta
+
2\nabla\cdot W
}.
\]

For both \(A\) and \(B\),

\[
\boxed{
C(r)
=
\frac{
36Mq\ell^2r^3
}{
(r^3+2q\ell^2)^3
}
}.
\]

Thus the coupled linear equation has the schematic form

\[
\boxed{
C(r)\,w_A
+
J_A[h_0,h_1]
=
0
}
\]

where \(J_A\) is built from the odd metric perturbations.

The vector perturbation is therefore auxiliary:

\[
w_A
=
-\frac{J_A}{C}
\]

wherever \(C\neq0\).

## 4. Relation to the effective stress anisotropy

For the regular geometry,

\[
\boxed{
C(r)
=
G^\theta{}_\theta-G^t{}_t
}.
\]

Equivalently, using the effective Einstein-source reconstruction,

\[
C(r)
=
8\pi(\rho+p_t)
\]

in geometric units.

So the algebraic stiffness of the odd vector constraint is exactly controlled
by the tangential stress anisotropy that supported the regular core.

This connects two previously separate calculations in the repository:

\[
\boxed{
\text{regular-core anisotropy}
\quad\leftrightarrow\quad
\text{axial vector constraint strength}
}.
\]

## 5. Endpoint degeneracy

Although

\[
C(r)>0
\]

for finite \(r>0\), it vanishes at both ends:

\[
C(r)\to0
\qquad(r\to0),
\]

and

\[
C(r)\to0
\qquad(r\to\infty).
\]

More precisely,

\[
C(r)
\sim
\frac{9M}{2q^2\ell^4}r^3
\qquad(r\to0),
\]

and

\[
C(r)
\sim
\frac{36Mq\ell^2}{r^6}
\qquad(r\to\infty).
\]

Thus the algebraic elimination becomes degenerate in the asymptotic vacuum and
at the exact regular center.

This matches the previous result that the independent vector quadratic action
vanishes around Minkowski space.

## 6. Fully extremal branch

For

\[
q\ell^2
=
\frac{16M^3}{27},
\]

the coefficient is

\[
C_{\rm ext}(r)
=
\frac{
419904M^4r^3
}{
(32M^3+27r^3)^3
}.
\]

At the degenerate horizon

\[
r_h=\frac{4M}{3},
\]

we find

\[
\boxed{
C_{\rm ext}(r_h)
=
\frac{9}{8M^2}
}.
\]

So the auxiliary equation itself is nondegenerate on the extremal horizon.

Interestingly,

\[
C_{\rm ext}(r_h)
=
f''(r_h).
\]

The two quantities characterize different structures, but their equality on
this solution is a useful algebraic identity.

Near the center,

\[
C_{\rm ext}
\sim
\frac{6561}{512}
\frac{r^3}{M^5},
\]

while at infinity,

\[
C_{\rm ext}
\sim
\frac{64}{3}
\frac{M^4}{r^6}.
\]

## 7. Why this matters

The full odd-parity problem has now simplified.

There is no need to search for an independent vector axial wave mode.

Instead one should:

1. write the Regge-Wheeler metric perturbations \(h_0,h_1\);
2. solve the two algebraic vector constraints;
3. substitute them back into the quadratic action;
4. inspect the resulting metric kinetic and gradient coefficients.

The critical question becomes

\[
\boxed{
\text{Does integrating out }A_A,B_A
\text{ leave a healthy Regge-Wheeler mode?}
}
\]

The endpoint behavior \(C\to0\) warns that this elimination can become
singular, so asymptotic and core limits must be treated before dividing by
\(C\).

## 8. Connection with generalized-Proca stability literature

The single-vector building block belongs to generalized Proca theory.

With

\[
X=-\frac12W^2,
\]

the interaction can be written, up to a boundary term, as a combination with

\[
G_2(X)\propto X^2,
\qquad
G_3(X)\propto X,
\qquad
G_4(X)\supset \beta_4 X.
\]

The \(G_4\) term linear in \(X\) is equivalent to an Einstein-tensor coupling

\[
G_{\mu\nu}W^\mu W^\nu.
\]

Published odd-parity analyses of generalized Proca black holes have found that
branches with a nonzero longitudinal vector component and this quartic
Einstein-tensor coupling can develop ghost or Laplacian instabilities near the
horizon.

That result is a serious warning but is **not directly a proof** for the
present model, because:

- there are two vector sectors with opposite action signs;
- both background vectors are null;
- there is no conventional Maxwell kinetic term;
- the vectors are intended as auxiliary constraints;
- the exact background differs from the stealth Schwarzschild examples
  analyzed in that literature.

The correct test is therefore the explicit two-vector quadratic action.

Reference:

R. Kase, M. Minamitsuji, S. Tsujikawa, Y.-L. Zhang,
*Black hole perturbations in vector-tensor theories: The odd-mode analysis*,
JCAP **02** (2018) 048,
https://doi.org/10.1088/1475-7516/2018/02/048

## 9. Next calculation

The immediate target is the reduced odd-parity quadratic action:

\[
S_{\rm odd}^{(2)}
=
\int dv\,dr\,
\left[
K_{\rm RW}(r)\dot\Psi^2
-
G_{\rm RW}(r)(\Psi')^2
-
V_{\rm RW}(r)\Psi^2
\right]
\]

after eliminating \(A_A\), \(B_A\), and the nondynamical metric variable.

The signs

\[
K_{\rm RW}>0,
\qquad
G_{\rm RW}>0
\]

would be the first full non-radial ghost/gradient test.

## Reproducibility

Run

\`\`\`bash
python src/symbolic/axial_vector_auxiliary.py
\`\`\`

to verify the common vector divergence, the exact auxiliary coefficient,
its relation to stress anisotropy, and its endpoint/extremal limits.
