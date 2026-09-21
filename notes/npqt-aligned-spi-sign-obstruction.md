# Aligned NPQT Scalar-Invariant Sign Obstruction

**Status:** NEW CALCULATION CANDIDATE / conditional no-go for SPI-only lifts.

This note sharpens the mixed-invariant atlas problem at the aligned
spherical/type-D simultaneous-zero stratum.

The exact spherical target is

\[
\boxed{
T_{\rm sph}=W_2\Theta.
}
\]

The aligned algebraic curvature family is

\[
\operatorname{spec}(E)=(-2q,q,q),
\]

\[
\boxed{
Z^a{}_b
=
\operatorname{diag}
(-\Theta,-\Theta,\Theta,\Theta).
}
\]

For \(\Theta\neq0\), this has the Ricci eigenvalue pattern associated with the
Segre class \([(1,1)(11)]\), while the Weyl tensor is Petrov D for \(q\neq0\).

---

# 1. Degree-five result

The Carminati--McLenaghan / Zakhary--McIntosh generators specialize to

\[
r_1=\Theta^2,
\qquad
r_2=0,
\qquad
r_3=\frac14\Theta^4,
\]

\[
w_1=6q^2,
\qquad
w_2=-6q^3,
\]

\[
m_1=-2q\Theta^2.
\]

Using the published class-B warped-product syzygies,

\[
(3m_2-w_1r_1)w_1-3m_1w_2=0,
\]

\[
(3m_5-w_1\bar m_1)w_1-3m_3w_2=0,
\]

\[
6m_4+w_1r_2=0,
\qquad
m_3=m_2,
\]

together with the \(m_6\) relation, gives

\[
\boxed{
m_2=m_3=4q^2\Theta^2,
}
\]

\[
\boxed{
m_4=m_6=0,
}
\]

\[
\boxed{
m_5=-8q^3\Theta^2.
}
\]

Every generator is invariant under

\[
\Theta\rightarrow-\Theta.
\]

Santosuosso et al. state that the CM+ZM invariant set is complete through
degree five for a general four-dimensional spacetime.  Therefore:

\[
\boxed{
\text{all scalar polynomial curvature invariants of degree }\le5
\text{ are sign blind on this stratum.}
}
\]

By contrast,

\[
W_2\Theta
=
48q^2\Theta
\]

is odd under the same sign flip.

Reproducibility:

    python src/symbolic/npqt_spi_sign_blind_degree5.py

---

# 2. All-degree algebraic result

Zakhary and McIntosh constructed algebraically complete sets of
four-dimensional Riemann invariants adapted to the Petrov and Segre types.

A later invariant analysis quotes the relevant specialization:

\[
\boxed{
\text{Petrov D}
+
\text{Segre }[(1,1)(11)]
\quad\Longrightarrow\quad
\{R,I,I_6,K\}
\text{ algebraically complete}.
}
\]

In tensor notation,

\[
I_6
=
\frac1{12}
S^\alpha{}_\beta S^\beta{}_\alpha,
\]

\[
I
=
\frac1{24}
\bar C_{\alpha\beta\gamma\delta}
\bar C^{\alpha\beta\gamma\delta},
\]

\[
K
=
\frac14
\bar C_{\alpha\gamma\delta\beta}
S^{\gamma\delta}S^{\alpha\beta},
\]

with

\[
\bar C
=
\frac12(C+i\,{}^\star C).
\]

For the aligned NPQT family, direct tensor contraction gives

\[
\boxed{
I=q^2,
}
\]

\[
\boxed{
I_6=\frac{\Theta^2}{3},
}
\]

\[
\boxed{
K=-2q\Theta^2.
}
\]

The Ricci scalar \(R\) is independent of the sign of the traceless-Ricci
parameter \(\Theta\).

Therefore

\[
\boxed{
\{R,I,I_6,K\}_{\Theta}
=
\{R,I,I_6,K\}_{-\Theta}.
}
\]

Conditional on the published algebraic-completeness classification, the two
aligned curvature tensors

\[
(q,\Theta)
\qquad\text{and}\qquad
(q,-\Theta)
\]

cannot be distinguished by any algebraic scalar Riemann invariant without
curvature derivatives.

But the required spherical target obeys

\[
\boxed{
T_{\rm sph}(q,-\Theta)
=
-T_{\rm sph}(q,\Theta).
}
\]

Hence:

\[
\boxed{
\text{no single-valued function of algebraic scalar Riemann invariants can
represent }W_2\Theta\text{ on both aligned sign branches.}
}
\]

This is the current strongest version of the sign obstruction.

Reproducibility:

    python src/symbolic/npqt_aligned_spi_all_degree_gate.py

---

# 3. The obstruction accumulates at the maximally symmetric core

Scale the tracefree curvature data by

\[
q\rightarrow\epsilon q,
\qquad
\Theta\rightarrow\epsilon\Theta.
\]

Then

\[
I=\epsilon^2q^2,
\]

\[
I_6=\frac{\epsilon^2\Theta^2}{3},
\]

\[
K=-2\epsilon^3q\Theta^2.
\]

These are identical for the \(+\Theta\) and \(-\Theta\) branches for every
\(\epsilon\).

Both branches therefore approach the same maximally symmetric algebraic
curvature point in scalar-invariant space.

Their required targets are instead

\[
T_\pm
=
\pm48\epsilon^3q^2\Theta.
\]

Thus the discrete branch ambiguity occurs arbitrarily close to

\[
W=Z=0.
\]

Reproducibility:

    python src/symbolic/npqt_aligned_spi_core_scaling_gate.py

This is stronger than merely finding a remote singular chart.

The problem lies directly in any scalar-invariant neighborhood of the core.

---

# 4. Consequence for NPQT representative design

The mixed-invariant atlas established that the old explicit type-I pole is
chart-specific: another rational chart can cover that point.

The present result identifies a different, more structural obstruction.

At the aligned stratum, scalar curvature invariants lose precisely the
discrete information required to choose the sign of \(\Theta\).

Therefore changing denominators cannot by itself solve the problem globally.

The following combination is incompatible:

\[
\boxed{
\begin{aligned}
&\text{single-valued local scalar function of algebraic Riemann invariants}\\
&+\ \text{exact recovery of }W_2\Theta\text{ on both aligned sign branches}.
\end{aligned}
}
\]

This does **not** reject every possible 4D NPQT base.

It rejects an important construction class.

---

# 5. What is not ruled out

The obstruction does not currently exclude:

1. a theory whose covariant action is deliberately restricted to one
   invariant branch;
2. a root/sign prescription with additional branch data;
3. Cartan/frame invariants rather than scalar polynomial invariants;
4. curvature-derivative invariants;
5. nonlocal covariant structures;
6. additional dynamical fields that carry the missing orientation/branch
   information;
7. a different spherical reduced target whose 4D lift does not require this
   signed eigenvalue.

Each escape route has a cost.

A root/sign prescription immediately reopens the \(C^2\) differentiability
gate.

Additional local fields reopen kinetic/constraint/principal-safety gates.

Derivative invariants may introduce higher-order principal dynamics.

Nonlocal structures require the NLQT operator analysis rather than solving
the local-base problem automatically.

---

# 6. Branch restriction is not automatically sufficient

One possible response is to declare that the physical regular-black-hole
solution lives only on one sign branch.

That is not yet enough for the repository's acceptance criterion.

The local 4D action used in the perturbation problem must have a
differentiable domain containing an open set of curvature perturbations around
the target background.

A historical or global instruction such as

\[
\text{"choose the sign continuously from the asymptotic solution"}
\]

is not, by itself, a local single-valued covariant Lagrangian.

This point is strengthened by the chronology-side predictive-realizability
lesson: existence of a desired branch is weaker than having that branch
selected by a well-defined local evolution law.

---

# 7. Current conditional no-go

The defensible statement is:

\[
\boxed{
\begin{minipage}{0.88\linewidth}
On the Petrov-D / Segre-\([(1,1)(11)]\) aligned spherical stratum, and
conditional on the published Zakhary--McIntosh algebraic-completeness
classification, no single-valued function of algebraic scalar Riemann
invariants can reproduce the signed NPQT target \(W_2\Theta\) on both
\(\Theta\) branches.
\end{minipage}
}
\]

**Status:** NEW CONDITIONAL NO-GO CANDIDATE.

No priority claim is made.

It is not a theorem about:

- derivative-dependent gravity;
- nonlocal gravity;
- extra-field completions;
- branch-restricted theories;
- arbitrary non-scalar curvature concomitants.

---

# 8. Root structure of the spherical angular mode

For a general spherical traceless-Ricci spectrum

\[
\{\lambda_1,\lambda_2,\Theta,\Theta\},
\qquad
\lambda_1+\lambda_2+2\Theta=0,
\]

with the CM normalizations

\[
r_1=\frac14\operatorname{tr}(S^2),
\qquad
r_2=-\frac18\operatorname{tr}(S^3),
\]

the repeated angular eigenvalue obeys

\[
\boxed{
3\Theta^3-3r_1\Theta+2r_2=0.
}
\]

Thus \(\Theta\) is naturally an algebraic root over the scalar-invariant
field.

At the aligned stratum,

\[
r_1=\Theta_0^2,
\qquad
r_2=0,
\]

the polynomial becomes

\[
\boxed{
3x(x-\Theta_0)(x+\Theta_0).
}
\]

The invariant data therefore admit the three roots

\[
0,\qquad+\Theta_0,\qquad-\Theta_0.
\]

For either nonzero root,

\[
\left.
\frac{\partial}{\partial x}
(3x^3-3r_1x+2r_2)
\right|_{x=\pm\Theta_0}
=
6\Theta_0^2
\neq0.
\]

So a **chosen** nonzero branch is locally analytic at a fixed aligned point.

At the maximally symmetric core,

\[
r_1=r_2=x=0,
\]

all roots coalesce and the same derivative vanishes.

Reproducibility:

    python src/symbolic/npqt_spherical_theta_root_gate.py

This clarifies the obstruction:

\[
\boxed{
\text{local branch analyticity away from the core: possible}
}
\]

but

\[
\boxed{
\text{single-valued branch selection on the full spherical invariant space:
not supplied by SPIs}.
}
\]

## 8.1 Principal absolute-root prescription fails at \(C^1\)

The simplest single-valued real prescription on the aligned family is

\[
\Theta_{\rm abs}
=
\sqrt{3I_6}
=
|\Theta|.
\]

It gives

\[
T_{\rm abs}
=
48q^2|\Theta|.
\]

At

\[
\Theta=0,
\qquad
q\neq0,
\]

the one-sided derivatives are

\[
\partial_\Theta T_{\rm abs}|_{0^+}
=
+48q^2,
\]

\[
\partial_\Theta T_{\rm abs}|_{0^-}
=
-48q^2.
\]

Therefore the principal absolute-root completion is not \(C^1\).

Such cusp points occur arbitrarily close to the maximally symmetric core by
taking \(q\) arbitrarily small but nonzero.

Reproducibility:

    python src/symbolic/npqt_spi_absolute_root_c1_gate.py

This rejects the most direct branch-independent square-root repair.  It does
not reject a locally signed tensorial principal-plane construction.

## 8.2 Full cubic density inherits the sign obstruction

The displayed cubic NPQT density has the structure

\[
\mathcal Z_{(3)}
=
P_{(3)}(R_{abcd})
+
\frac92\frac ND,
\]

where \(P_{(3)}\) is polynomial in curvature and

\[
\left.\frac ND\right|_{\rm sph}
=
W_2\Theta.
\]

On the paired aligned tensors, all polynomial SPIs agree, so

\[
P_{(3)}(+\Theta)
=
P_{(3)}(-\Theta).
\]

But

\[
\boxed{
\mathcal Z_{(3)}(+\Theta)
-
\mathcal Z_{(3)}(-\Theta)
=
9W_2\Theta
=
432q^2\Theta.
}
\]

A deformation which vanishes identically on all spherical configurations
takes the same zero value on both branches and cannot erase this distinction.

Therefore the obstruction applies to the entire class of representatives
that preserve the **pointwise spherical density** by adding
spherical-vanishing terms.

Reproducibility:

    python src/symbolic/npqt_full_cubic_sign_pair_gate.py

This does not rule out changing the reduced action by a spherical total
derivative while preserving only the spherical equations of motion.

# 9. Next research decision

The previous plan was to keep generating alternative rational scalar charts.

That is no longer the highest-value task.

The immediate decision is now between two routes.

## Route A — test branch/root completion

Construct the minimal algebraic root needed to recover the signed angular
Ricci mode on the spherical class-B locus.

Then test:

\[
C^0,\qquad C^1,\qquad C^2
\]

at:

- the aligned sign-degenerate stratum;
- the maximally symmetric core;
- generic nonspherical perturbations.

If the Hessian fails, branch/root completion is rejected quickly.

## Route B — search for a different 4D base

Instead of forcing the displayed spherical target into a globally
single-valued local scalar action, search for a different QT/NPQT base whose
spherical regular response is compatible with a differentiable covariant
completion.

Given the repeated rational/projector/branch failures already found, Route B
may become preferable if the minimal root construction fails the \(C^2\)
gate.

No full NLQT Hessian calculation should be attempted before this decision is
resolved.

---

# 10. References

1. E. Zakhary, C. B. G. McIntosh,
   *A Complete Set of Riemann Invariants*,
   Gen. Rel. Grav. **29**, 539--581 (1997),
   DOI 10.1023/A:1018851201784.

2. K. Santosuosso, D. Pollney, N. Pelavas, P. Musgrave, K. Lake,
   *Invariants of the Riemann tensor for Class B Warped Product Spacetimes*,
   Comput. Phys. Commun. **115**, 381--394 (1998),
   arXiv:gr-qc/9809012.

3. R. Torres, F. Fayos,
   *On regular rotating black holes*,
   Gen. Rel. Grav. **49**, 2 (2017),
   arXiv:1611.03654.

4. P. Bueno, P. A. Cano, R. A. Hennigar, Á. J. Murcia,
   *Regular black hole formation in four-dimensional non-polynomial
   gravities*,
   Phys. Rev. D **113**, 024019 (2026),
   arXiv:2509.19016.
