# Direct Two-Vector Odd Expansion from the Original Action

This note closes the most important methodological gap identified in the
third-party review of this repository.

Earlier odd-sector calculations used the published generalized-Proca
one-vector perturbation formalism as a mapping/check.  Here the relevant
kinetic and primary-constraint structure is rederived **directly from the
original two-vector action**.

No published odd-parity coefficient \(C_i\) is used in the derivation below.

## 1. Original action

Omitting the common normalization \(1/(16\pi G)\),

\[
S
=
\int d^4x\sqrt{-g}
\left[
R
+
\ell^2
\left(
\mathcal L[A]
-
\mathcal L[B]
\right)
\right],
\]

with

\[
\mathcal L[V]
=
4G^{\mu\nu}V_\mu V_\nu
+
8V^2\nabla_\mu V^\mu
+
6(V^2)^2.
\]

The static regular branch has

\[
ds^2
=
-f(r)dt^2
+
\frac{dr^2}{f(r)}
+
r^2d\Omega^2
\]

and null vectors

\[
A_\mu dx^\mu
=
a(r)
\left(
dt+\frac{dr}{f}
\right),
\]

\[
B_\mu dx^\mu
=
b(r)
\left(
dt+\frac{dr}{f}
\right).
\]

## 2. Direct \(l=2,m=0\) odd harmonic

Use Regge-Wheeler gauge and the unnormalized axial harmonic

\[
S_\phi
=
3\sin^2\theta\cos\theta.
\]

Insert directly

\[
h_{t\phi}
=
\epsilon Q(t,r)S_\phi,
\]

\[
h_{r\phi}
=
\epsilon W(t,r)S_\phi,
\]

and

\[
\delta A_\phi
=
\epsilon u_A(t,r)S_\phi,
\qquad
\delta B_\phi
=
\epsilon u_B(t,r)S_\phi.
\]

The brute-force symbolic calculation constructs:

1. \(g^{\mu\nu}\) through \(O(\epsilon^2)\);
2. all Christoffel symbols;
3. \(R_{\mu\nu}\), \(R\), and \(G^{\mu\nu}\);
4. the complete original vector Lagrangian;
5. the angular integral;
6. the quadratic temporal derivative sector.

This is implemented in

\[
\texttt{src/symbolic/direct\_two\_vector\_odd\_l2.py}.
\]

GitHub Actions run #8 verifies the calculation independently on Python 3.11
and 3.12.

## 3. Direct Einstein-Hilbert kinetic term

After time integration by parts, the direct \(l=2\) Einstein-Hilbert
calculation gives

\[
\boxed{
\mathcal L_{\rm EH}^{(2)}
\supset
\frac{12\pi}{5}\dot W^2.
}
\]

Thus the direct positive metric kinetic coefficient is

\[
\boxed{
A_{\rm EH}
=
\frac{12\pi}{5}.
}
\]

The same calculation gives the nondynamical-\(Q\) derivative coupling

\[
\boxed{
\mathcal L_{\rm EH}^{(2)}
\supset
\frac{48\pi}{5r}Q\dot W.
}
\]

No one-vector perturbation formalism is involved in either result.

## 4. Direct one-vector derivative structure

For one original vector with background profile \(p(r)\), direct expansion
gives

\[
\boxed{
\mathcal L_V^{(2)}
\supset
-\frac{96\pi p}{5f}
\dot W\,\dot u
}
\]

after time integration by parts.

The direct \(Q\dot u\) coefficient is

\[
\boxed{
-\frac{192\pi p}{5rf}.
}
\]

Hence

\[
\boxed{
D_{Q u}
=
\frac{2}{r}
B_{W u}.
}
\]

Most importantly,

\[
\boxed{
\frac{\partial^2\mathcal L_V^{(2)}}
{\partial\dot u^2}
=
0.
}
\]

There is no intrinsic transverse-vector kinetic term in the original action.

This is now a result of the direct four-dimensional expansion, not an
inference from generalized-Proca notation.

## 5. Direct two-vector velocity Hessian

The \(A\) sector enters with \(+\ell^2\) and the \(B\) sector with
\(-\ell^2\).

For velocities

\[
(\dot W,\dot u_A,\dot u_B),
\]

the direct Hessian is

\[
\boxed{
H
=
\frac{24\pi}{5}
\begin{pmatrix}
1
&
-\dfrac{4\ell^2a}{f}
&
+\dfrac{4\ell^2b}{f}
\\[2mm]
-\dfrac{4\ell^2a}{f}
&
0
&
0
\\[2mm]
+\dfrac{4\ell^2b}{f}
&
0
&
0
\end{pmatrix}.
}
\]

Its characteristic polynomial is

\[
\lambda
\left[
\lambda^2
-
\frac{24\pi}{5}\lambda
-
\frac{9216\pi^2\ell^4}
{25f^2}
(a^2+b^2)
\right].
\]

Therefore the eigenvalues are

\[
\boxed{
\lambda_0=0,
}
\]

and

\[
\boxed{
\lambda_\pm
=
\frac{12\pi}{5}
\left[
1
\pm
\sqrt{
1+
\frac{64\ell^4(a^2+b^2)}{f^2}
}
\right].
}
\]

For nonzero vector hair,

\[
\lambda_+>0,
\qquad
\lambda_-<0.
\]

Thus the **unreduced odd velocity Hessian** has one positive, one negative,
and one zero direction.

This is not yet by itself a physical-ghost theorem because nondynamical
constraints must still be reduced.

## 6. Direct primary null direction

The null eigenvector is

\[
\boxed{
v_0
\propto
(0,b,a).
}
\]

Equivalently, the vector combination

\[
b\,\delta A_{\rm odd}
+
a\,\delta B_{\rm odd}
\]

has no quadratic velocity.

The direct derivative momenta obey, at principal level,

\[
\boxed{
b\,p_A
+
a\,p_B
=
\text{terms containing no velocities}.
}
\]

In the temporal derivative truncation used by the direct calculation, the
right-hand side vanishes exactly.

The other primary nondynamical relation is

\[
\boxed{
p_Q=0,
}
\]

because \(Q\) has no independent time derivative after the required boundary
integrations.

Thus the primary rank/constraint structure found earlier is reproduced
directly from the \(A-B\) action.

## 7. Independent comparison with the one-vector mapping

Only **after** completing the direct derivation do we compare with the
published one-vector formalism.

The direct ratios are

\[
\frac{H_{W A}}{H_{WW}}
=
-\frac{4\ell^2a}{f},
\]

and

\[
\frac{H_{W B}}{H_{WW}}
=
+\frac{4\ell^2b}{f}.
\]

These agree exactly with the independently specialized generalized-Proca
source coefficients.

Therefore the two routes agree on:

- absence of a direct vector kinetic term;
- signs of both metric-vector mixings;
- rank-one vector derivative structure;
- the zero vector derivative combination;
- the negative induced derivative direction.

This is the requested cross-check.

## 8. Direct raw form: the vectors are algebraic

Before moving derivatives by parts, the direct original-action expansion has
a particularly informative form.

Define

\[
X
=
\dot W
-
Q'
+
\frac{2Q}{r}.
\]

For one vector,

\[
\boxed{
\mathcal L_V^{(2)}
\supset
\mathcal N
\left[
C(r)u^2
+
\frac{p(r)}{f(r)}
u\,\dot X
\right],
}
\]

where, for the chosen \(l=2\) normalization,

\[
\mathcal N
=
\frac{96\pi}{5},
\]

and

\[
C(r)
=
G^\theta{}_\theta
+
2\nabla_\mu\bar V^\mu.
\]

There is no derivative acting on \(u\) in this raw representation.

Thus the vector perturbation is algebraic:

\[
2C u
+
\frac{p}{f}\dot X
=
0.
\]

This agrees with the direct linear vector equation previously found in
\`axial_vector_auxiliary.py\`.

The apparent vector kinetic term seen after integration by parts is therefore
**induced entirely by metric-vector derivative mixing**.

## 9. Eliminating the algebraic vectors

On the regular branch both vector sectors have the same \(C(r)\).

Their algebraic solutions are

\[
u_A
=
-\frac{a}{2fC}\dot X,
\]

\[
u_B
=
-\frac{b}{2fC}\dot X.
\]

Substitution into the original quadratic action gives

\[
\boxed{
\mathcal L_{\rm eff}^{\rm high}
=
\frac{\mathcal N\ell^2}{4}
\frac{b^2-a^2}{f^2C}
\dot X^2.
}
\]

For the exact regular solution,

\[
b^2-a^2
=
\frac{Mq}
{r(r^3+2q\ell^2)},
\]

and

\[
C
=
\frac{
36Mq\ell^2r^3
}{
(r^3+2q\ell^2)^3
}.
\]

Hence

\[
\boxed{
\mathcal L_{\rm eff}^{\rm high}
=
\frac{2\pi}{15}
\frac{
(r^3+2q\ell^2)^2
}{
r^4f^2
}
\dot X^2.
}
\]

This is independently checked by

\[
\texttt{src/symbolic/direct\_vector\_elimination\_higher\_derivative.py}
\]

and GitHub Actions run #10.

## 10. Endpoint behavior of the eliminated action

At the regular center,

\[
\boxed{
\frac{2\pi}{15}
\frac{
(r^3+2q\ell^2)^2
}{
r^4f^2
}
\sim
\frac{
8\pi q^2\ell^4
}{
15r^4
}.
}
\]

At infinity,

\[
\boxed{
\frac{2\pi}{15}
\frac{
(r^3+2q\ell^2)^2
}{
r^4f^2
}
\sim
\frac{2\pi}{15}r^2.
}
\]

Thus algebraically eliminating the vector auxiliaries is singular at both
ends.

This explains, in a single direct calculation, two earlier observations:

- the asymptotic vector quadratic operator degenerates;
- the regular center can hide singular fluctuation coefficients.

## 11. Higher-time-derivative warning

Since

\[
X
=
\dot W-Q'+\frac{2Q}{r},
\]

we have

\[
\dot X
=
\ddot W
-
\dot Q'
+
\frac{2\dot Q}{r}.
\]

The eliminated metric-only action therefore contains a nonzero
\(\ddot W^2\) Hessian.

This exposes a hidden higher-time-derivative mode after the algebraic vectors
are removed.

However, the project will still avoid writing

> "physical Ostrogradsky ghost proven"

until the complete mixed \(Q,W\) constraint system is reduced.  Higher-
derivative constrained systems can possess nontrivial degeneracies, and the
full \(t,r\)-dependent odd action must be used for the final degree-of-freedom
count.

The current precise statement is:

\[
\boxed{
\text{direct original-action expansion reveals a nonzero hidden
higher-derivative principal term}.
}
\]

## 12. Current status

The original methodological gap is substantially closed.

We now have agreement between:

1. direct four-dimensional \(A-B\) expansion;
2. direct linear vector equations;
3. published one-vector formalism specialized afterward as an independent
   check.

All three identify the same special structure:

\[
\boxed{
\text{no intrinsic vector kinetic term}
+
\text{nonzero metric-vector derivative mixing}
+
\text{one zero vector derivative direction}.
}
\]

The remaining publication-level step is the **full \(t,r\)-dependent
constraint reduction**, including radial derivatives, to decide whether the
negative/higher-derivative direction survives as a physical ghost.

## Reproducibility

Run:

\`\`\`bash
python src/symbolic/direct_two_vector_odd_l2.py
python src/symbolic/direct_vector_elimination_higher_derivative.py
\`\`\`

The same scripts run automatically in GitHub Actions.

Persistent CI results are posted to:

\[
\texttt{GitHub Issue \#1: CI monitor: symbolic calculations}.
\]
