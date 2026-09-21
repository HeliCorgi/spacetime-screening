# Direct Odd-Sector Ghost in the Asymptotic Exterior

This note states the strongest result currently obtained for the
Eichhorn-Fernandes two-vector regular-black-hole benchmark.

The derivation uses the **original two-vector action directly**.  It does not
depend on importing the published one-vector generalized-Proca perturbation
coefficients, although those coefficients provide an independent cross-check.

## 1. Scope of the statement

For the regular branch with

\[
M>0,\qquad q>0,\qquad \ell>0,
\]

consider odd \(l=2\) perturbations in the asymptotically static exterior.

The direct four-dimensional harmonic expansion gives a quadratic action in:

- the odd metric variables \(Q,W\);
- the two odd vector perturbations \(u_A,u_B\).

After passing to active/null vector combinations,

\[
U
=
\frac{-a\,u_A+b\,u_B}
{\sqrt{a^2+b^2}},
\]

\[
V
=
\frac{b\,u_A+a\,u_B}
{\sqrt{a^2+b^2}},
\]

the velocity-active variables are \(W,U\), while \(Q,V\) are nondynamical.

## 2. Direct four-dimensional source-action expansion

The brute-force calculation in

\[
\texttt{src/symbolic/direct\_two\_vector\_odd\_l2.py}
\]

constructs the full four-dimensional curvature and the original vector
Lagrangian through quadratic order.

It finds:

\[
\mathcal L_{\rm EH}^{(2)}
\supset
\frac{12\pi}{5}\dot W^2,
\]

and for one original vector profile \(p(r)\),

\[
\mathcal L_V^{(2)}
\supset
-\frac{96\pi p}{5f}
\dot W\,\dot u
-
\frac{192\pi p}{5rf}
Q\,\dot u,
\]

with

\[
\boxed{
\frac{\partial^2\mathcal L_V^{(2)}}
{\partial\dot u^2}
=
0.
}
\]

Thus the original vectors possess no independent direct transverse kinetic
term; all time derivatives enter through metric-vector mixing.

For the complete \(A-B\) theory the unreduced velocity Hessian has one
positive, one negative, and one zero eigenvalue.

That fact alone is not yet a physical-ghost statement because \(Q\) and the
velocity-null vector combination must be removed.

## 3. The derivative-null vector is genuinely auxiliary

The direct active/null audit gives:

- \(V\) has no quadratic velocity;
- \(V\) has no \(W\dot V\) mixing;
- \(V\) has no \(Q\dot V\) mixing.

All one-velocity terms align with the active direction \(U\).

The original action supplies an algebraic \(V^2\) stiffness.  On the exact
regular branch,

\[
b^2-a^2
=
\frac{
Mq
}{
r(r^3+2q\ell^2)
}
>0,
\]

and the common axial vector coefficient is

\[
C(r)
=
\frac{
36Mq\ell^2r^3
}{
(r^3+2q\ell^2)^3
}
>0.
\]

Hence the algebraic stiffness of \(V\) is positive for finite \(r>0\).

The exact \(Q-V\) algebraic mixing also vanishes.

Therefore \(V\) is an ordinary local auxiliary direction in the asymptotic
exterior; it is not the negative derivative-active mode.

## 4. The metric variable \(Q\) is auxiliary asymptotically

The exact direct \(Q^2\) coefficient \(E_Q(r)\) satisfies

\[
\boxed{
\lim_{r\to\infty}
r^2E_Q
=
\frac{48\pi}{5}>0.
}
\]

By continuity, there exists a sufficiently large finite radius beyond which

\[
E_Q>0.
\]

Thus \(Q\) can be eliminated locally in an open asymptotic region.

## 5. Reduced physical kinetic matrix

After eliminating \(Q\), the remaining temporal kinetic matrix for
\((W,U)\) has determinant

\[
\det K_{\rm red}(r).
\]

The direct calculation gives the exact asymptotic coefficient

\[
\boxed{
\lim_{r\to\infty}
r^5\det K_{\rm red}
=
-
\frac{
1152\pi^2
}{
25
}
M\ell^4
\left(
16M^2+q^2
\right).
}
\]

For

\[
M>0,\qquad \ell>0,
\]

this is strictly negative.

Therefore, for every allowed \(q>0\), there exists a sufficiently large but
finite open region in which

\[
\boxed{
\det K_{\rm red}<0.
}
\]

A real symmetric \(2\times2\) kinetic matrix with negative determinant has one
positive and one negative eigenvalue.

Hence:

\[
\boxed{
\text{one odd physical kinetic mode has the wrong sign}
}
\]

throughout that asymptotic open region.

## 6. Why eliminating \(V\) cannot repair the sign

The direct audit actually finds zero velocity mixing for \(V\), so its
elimination leaves the \((W,U)\) kinetic matrix unchanged.

More generally, suppose an algebraic field with positive stiffness \(m_V>0\)
had an unaccounted linear velocity coupling

\[
V\,j^{\rm T}\dot q.
\]

Eliminating it would shift

\[
K
\longrightarrow
K
-
\frac{
jj^{\rm T}
}{
2m_V
}
\]

up to a positive normalization convention.

The correction is negative semidefinite.

It cannot remove an already existing negative kinetic direction.

This robustness check is encoded in

\[
\texttt{src/symbolic/direct\_asymptotic\_ghost\_robustness.py}.
\]

## 7. Interpretation: this is a linear ghost in the stated region

The asymptotic coordinate \(t\) is timelike, and the Einstein-Hilbert
gravitational kinetic term fixes the healthy sign convention.

Therefore the negative eigenvalue is not merely a coordinate sign change.

Within the direct \(l=2\) quadratic theory, after the local nondynamical
directions are removed, the asymptotic exterior contains a genuine
negative-kinetic odd mode.

The technically precise statement is:

\[
\boxed{
\text{the regular two-vector branch has an odd-sector linear ghost
in a sufficiently large finite asymptotic exterior region.}
}
\]

This is enough to fail the repository's principal-safe screening criterion.

It is **not** necessary for the ghost to persist at every radius in order to
rule out the background as a globally healthy perturbative solution.

## 8. Independent \(l=1\) cross-check

A separate direct local analysis of the odd dipole gives

\[
\mathcal L_{l=1,\rm phys}^{\rm pr}
=
-\frac12 Z^2,
\]

with

\[
Z
\propto
a(\partial_r-\partial_t)u_A
-
b(\partial_r-\partial_t)u_B.
\]

The canonical Hamiltonian contains a negative quadratic momentum term.

Because the odd \(l=1\) metric field is a two-dimensional gauge/constraint
sector rather than a local gravitational-wave mode, this independently points
to the same vector ghost.

A full four-dimensional \(l=1\) harmonic expansion is also included in the CI
suite as an additional direct check.

## 9. Relation to the algebraic-vector representation

Before time integration by parts, the vector perturbations are algebraic in
the original action.

Eliminating them instead produces a metric-only action containing

\[
\dot X^2,
\]

where

\[
X
=
\dot W-Q'+\frac{2Q}{r}.
\]

Thus the same problematic degree of freedom can be represented either as:

- an induced negative-kinetic vector-like mode after metric constraint
  reduction; or
- a hidden higher-time-derivative metric sector after algebraic vector
  elimination.

These are two descriptions of the same coupled degeneracy problem, not two
independent instabilities.

## 10. Novelty status

A targeted literature search in September 2026 did not identify a published
odd-parity perturbation or ghost analysis of this exact
Eichhorn-Fernandes two-vector regular-black-hole branch.

That search is not sufficient to establish priority.

The repository therefore labels this result:

\[
\boxed{
\text{NEW CALCULATION CANDIDATE — technically direct, priority unclaimed}.
}
\]

No statement such as "first discovery" should be made without a broader
literature review and independent verification.

## Reproducibility

Key scripts:

\`\`\`bash
python src/symbolic/direct_two_vector_odd_l2.py
python src/symbolic/direct_two_vector_odd_principal_tr.py
python src/symbolic/direct_l2_velocity_linear_audit.py
python src/symbolic/direct_odd_active_null_constraints.py
python src/symbolic/direct_odd_asymptotic_ghost.py
python src/symbolic/direct_asymptotic_ghost_robustness.py
python src/symbolic/direct_ab_odd_fourier.py
python src/symbolic/direct_ab_odd_constraints.py
\`\`\`

The complete symbolic suite is run on Python 3.11 and 3.12 by GitHub Actions.

Persistent run results are posted automatically to:

**GitHub Issue #1 — CI monitor: symbolic calculations.**
