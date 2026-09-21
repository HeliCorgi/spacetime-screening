# NPQT Mixed-Invariant Atlas

**Status:** NEW CALCULATION CANDIDATE / CONSTRUCTIVE DIAGNOSTIC.

This note implements Task A1 from RESEARCH_HANDOFF.md.

The exact spherical target inherited from the displayed cubic NPQT rational
term is

\[
\boxed{
T_{\rm sph}=W_2\Theta,
}
\]

where \(\Theta\) is the repeated angular eigenvalue of the traceless Ricci
tensor on a generic local spherical configuration.

The current result is mixed:

\[
\boxed{
\text{an alternative invariant chart exists and covers the old type-I pole,}
}
\]

but

\[
\boxed{
\text{it still fails }C^0\text{ at the spherical simultaneous-zero stratum.}
}
\]

More importantly, the simultaneous zero appears to be a **discrete
invariant-coordinate branch problem**, not merely a bad denominator choice.

---

# 1. Published invariant-theory background

## 1.1 Four-dimensional Weyl identity

A standard four-dimensional dimensionally dependent identity gives

\[
\boxed{
C_{acde}C_b{}^{cde}
=
\frac14 g_{ab}C_{cdef}C^{cdef}.
}
\]

Therefore, for traceless Ricci \(Z_{ab}\),

\[
\boxed{
Z^{ab}C_{acde}C_b{}^{cde}=0.
}
\]

This removes the most direct polynomial cubic candidate of schematic form

\[
W^2Z.
\]

The repository reproduces this identity on a generic purely-electric
Lorentzian algebraic Weyl family in

src/symbolic/npqt_mixed_invariant_atlas_cubic_gate.py.

The identity is standard four-dimensional invariant theory; no novelty is
claimed for it.

## 1.2 Class-B warped-product scalar invariants

Santosuosso, Pollney, Pelavas, Musgrave and Lake,
*Invariants of the Riemann tensor for Class B Warped Product Spacetimes*,
arXiv:gr-qc/9809012, analyze scalar polynomial curvature invariants for class-B
warped products, which include spherical, planar and hyperbolic spacetimes.

They show that the curvature has four functional invariant degrees of freedom
and advocate the independent set

\[
\boxed{
\{R,r_1,r_2,w_2\}.
}
\]

They also emphasize an important qualification: this set is not "complete" in
the strict classical invariant-theory sense in which every other invariant is
an integral rational function of it. Root choices are required; for example,
one Weyl invariant cannot be obtained rationally from another without a
branch choice.

This distinction is directly relevant here.

Their syzygies also include

\[
\boxed{
6m_4+w_1r_2=0.
}
\]

Hence whenever the cubic traceless-Ricci invariant \(r_2\) vanishes on the
class-B locus,

\[
m_4=0.
\]

The repository's direct tensor calculation below independently reproduces this
vanishing on the NPQT simultaneous-zero stratum.

---

# 2. Cubic polynomial gate

A natural first attempt is a degree-three scalar

\[
T_{\rm poly}^{(3)}
\sim
Z^{ab}W_{acde}W_b{}^{cde}.
\]

But the four-dimensional Weyl identity gives

\[
T_{\rm poly}^{(3)}
=
\frac14W_2 Z^a{}_a
=
0.
\]

Thus the target

\[
W_2\Theta
\]

cannot be obtained from this direct polynomial contraction.

This is not yet a proof that every possible cubic mixed contraction vanishes,
but it closes the shortest obvious polynomial route.

Reproducibility:

    python src/symbolic/npqt_mixed_invariant_atlas_cubic_gate.py

---

# 3. Alternative rational chart

Define

\[
\boxed{
M_{22}
=
W_{ab}{}^{cd}
(Z^2)_c{}^a
(Z^2)_d{}^b,
}
\]

\[
\boxed{
M_{23}
=
W_{ab}{}^{cd}
(Z^2)_c{}^a
(Z^3)_d{}^b.
}
\]

Consider the general local spherical algebraic-curvature family

\[
E=\operatorname{diag}(-2q,q,q)
\]

for the purely-electric Weyl tensor, and

\[
Z_{ab}
=
\begin{pmatrix}
a&b&0&0\\
b&a-2\Theta&0&0\\
0&0&\Theta&0\\
0&0&0&\Theta
\end{pmatrix}_{ab}.
\]

Direct contraction gives

\[
W_2=48q^2,
\]

\[
M_{22}
=
-4q
\left[(a-\Theta)^2-b^2\right]
\left[-a^2+2a\Theta+b^2+3\Theta^2\right],
\]

and

\[
M_{23}
=
4q\Theta
\left[(a-\Theta)^2-b^2\right]
\left[-a^2+2a\Theta+b^2+3\Theta^2\right].
\]

Therefore

\[
\boxed{
M_{23}=-\Theta M_{22}.
}
\]

Whenever

\[
M_{22}\neq0,
\]

one obtains the alternative chart

\[
\boxed{
T_{\rm alt}
=
-W_2\frac{M_{23}}{M_{22}}
=
W_2\Theta.
}
\]

This construction uses only scalar contractions and does not label a Weyl
eigenvalue branch.

Reproducibility:

    python src/symbolic/npqt_mixed_invariant_atlas_chart1.py

---

# 4. The alternative chart covers the explicit old type-I pole

The previously identified singular direction of the displayed representative
has

\[
(e_1,e_2,e_3)=(1,5,-6),
\]

\[
z_1=z_2=1,
\qquad
z_0=-1+\frac8{\sqrt{61}},
\]

for which

\[
D_{\rm old}
=
(WZZ)W_2-2W_3Z_2
=
0.
\]

At exactly the same real Lorentzian algebraic curvature tensor, the new
invariants are

\[
\boxed{
M_{22}
=
-\frac{138240}{3721}
\neq0,
}
\]

\[
\boxed{
M_{23}
=
+\frac{138240}{3721}.
}
\]

Therefore

\[
\boxed{
T_{\rm alt}=496
}
\]

is finite there.

This is a concrete constructive result:

\[
\boxed{
\text{the explicit old denominator-zero point is chart-specific,}
}
\]

not a common zero of all spherical-equivalent rational invariant charts.

Reproducibility:

    python src/symbolic/npqt_mixed_invariant_atlas_old_pole.py

This keeps the representative-design program alive.

---

# 5. Chart 1 still fails at the spherical simultaneous zero

Now consider the type-D aligned point

\[
\operatorname{spec}(E)=(-2q,q,q),
\]

\[
\operatorname{spec}(Z)
=
(-\Theta,-\Theta,\Theta,\Theta).
\]

At this point

\[
M_{22}=M_{23}=0.
\]

Take a spherical Ricci path

\[
Z_{\rm sph}(\epsilon)
=
\operatorname{diag}
(-\Theta+\epsilon,-\Theta-\epsilon,\Theta,\Theta).
\]

Then

\[
\lim_{\epsilon\to0}
T_{\rm alt}
=
48q^2\Theta.
\]

Take instead an off-spherical Ricci path with the same exact type-D Weyl
tensor,

\[
Z_{\rm off}(\epsilon)
=
\operatorname{diag}
(-\Theta+\epsilon,-\Theta+\epsilon,\Theta,\Theta-2\epsilon).
\]

Then

\[
\lim_{\epsilon\to0}
T_{\rm alt}
=
-48q^2\Theta.
\]

Hence

\[
\boxed{
\text{chart 1 has no }C^0\text{ extension at this simultaneous zero.}
}
\]

Reproducibility:

    python src/symbolic/npqt_mixed_invariant_atlas_chart1_c0.py

This is a complementary failure to the old chart:

- the old chart has the explicit type-I pole;
- chart 1 covers that pole;
- chart 1 still fails the aligned simultaneous-zero gate.

---

# 6. The simultaneous-zero stratum is scalar-invariant sign blind

At the aligned point,

\[
Z^a{}_b
=
\operatorname{diag}
(-\Theta,-\Theta,\Theta,\Theta),
\]

one has

\[
\boxed{
Z^2=\Theta^2 I.
}
\]

The checked scalar invariants are

\[
Z_2=4\Theta^2,
\]

\[
Z_3=0,
\]

\[
Z_4=4\Theta^4,
\]

\[
WZZ=16q\Theta^2,
\]

together with

\[
W_2=48q^2,
\qquad
W_3=96q^3.
\]

Thus they are unchanged under

\[
\Theta\rightarrow-\Theta.
\]

The direct \(W^2Z\) cubic vanishes.

The CM-type odd quintic generator with two Weyl and three traceless-Ricci
factors,

\[
M_4
\sim
Z^{ag}Z^{ef}Z^c{}_d
\left[
C_{ac}{}^{db}C_{befg}
+
{}^\star C_{ac}{}^{db}{}^\star C_{befg}
\right],
\]

also vanishes directly.

This agrees with the published class-B syzygy

\[
6m_4+w_1r_2=0,
\]

because

\[
r_2\propto Z_3=0
\]

at this point.

Reproducibility:

    python src/symbolic/npqt_spherical_sign_blind_spi_gate.py

## 6.1 Complete degree-five gate

The sign-blindness can be upgraded from selected examples to the full
degree-five scalar polynomial invariant sector.

On the aligned stratum the CM normalizations are

\[
r_1=\Theta^2,\qquad
r_2=0,\qquad
r_3=\frac14\Theta^4,
\]

\[
w_1=6q^2,\qquad
w_2=-6q^3,\qquad
m_1=-2q\Theta^2.
\]

The published class-B syzygies then imply

\[
m_2=m_3=4q^2\Theta^2,
\]

\[
m_4=m_6=0,
\]

\[
m_5=-8q^3\Theta^2.
\]

Every member of the complete CM+ZM degree-five set is therefore invariant
under

\[
\Theta\rightarrow-\Theta.
\]

Since the published CM+ZM set is complete through degree five, all scalar
polynomial Riemann invariants through that degree are sign blind here.

Reproducibility:

    python src/symbolic/npqt_spi_sign_blind_degree5.py

## 6.2 All-degree algebraic SPI gate

The stronger Petrov/Segre specialization is documented separately in

- notes/npqt-aligned-spi-sign-obstruction.md
- src/symbolic/npqt_aligned_spi_all_degree_gate.py
- src/symbolic/npqt_aligned_spi_core_scaling_gate.py

Using the published Zakhary--McIntosh algebraic-completeness classification
for Petrov D and Segre \([(1,1)(11)]\), the complete set

\[
\{R,I,I_6,K\}
\]

takes identical values on \((q,\Theta)\) and \((q,-\Theta)\), while
\(W_2\Theta\) changes sign.

Thus the current strongest result is a conditional no-go for a
**single-valued SPI-only algebraic lift** on both sign branches.

## Interpretation

The spherical target changes sign,

\[
W_2\Theta
\rightarrow
-W_2\Theta,
\]

while the standard scalar polynomial invariant coordinates checked above do
not.

Santosuosso et al. already warn that their functionally independent class-B
invariant set does not eliminate algebraic root choices.

The NPQT problem appears to hit exactly such a discrete branch:

\[
\boxed{
\text{functional invariant data}
\not\Rightarrow
\text{single-valued rational recovery of the signed }\Theta.
}
\]

This provides a possible structural explanation for why the displayed
representative and the first alternative chart both develop \(0/0\)-type
behavior on the aligned stratum.

---

# 7. Current status

## Established here

\[
\boxed{
\text{alternative rational chart exists}
}
\]

and

\[
\boxed{
\text{it removes the explicit old type-I pole}.
}
\]

But

\[
\boxed{
\text{chart 1 fails }C^0\text{ at the spherical simultaneous zero}.
}
\]

The scalar-invariant sign-blind check further suggests

\[
\boxed{
\text{the simultaneous zero is a branch-information problem,
not merely a denominator problem}.
}
\]

## Scope

The last statement is currently a **NEW CALCULATION CANDIDATE / structural
warning**, not a universal no-go theorem.

In particular, this note has not proved that every conceivable covariant
Riemann scalar, including arbitrary nonpolynomial functions or
derivative-dependent invariants, fails to distinguish the sign.

It has established that the standard low-degree/class-B scalar-invariant
coordinates become sign blind at the relevant aligned stratum.

---

# 8. Next exact task

The next mainline calculation should no longer be "find another denominator"
in an unconstrained way.

The sharp question is:

\[
\boxed{
\text{Can any single-valued algebraic scalar concomitant of the 4D Riemann
tensor recover the signed }W_2\Theta
\text{ across the aligned stratum?}
}
\]

Do this in two stages.

## Stage 1 — invariant-ring sign gate

Use the published class-B syzygies and a finite scalar generating set to
determine whether the two spherical algebraic curvature tensors

\[
(q,\Theta)
\qquad\text{and}\qquad
(q,-\Theta)
\]

are indistinguishable by **all** scalar polynomial Riemann invariants on the
aligned stratum.

If yes, record a conditional no-go:

\[
\boxed{
\text{SPI-only single-valued lift of }W_2\Theta
\text{ cannot reproduce both sign branches}.
}
\]

## Stage 2 — decide the allowed escape route

If Stage 1 succeeds, the constructive options become much narrower:

1. restrict the theory to one invariant branch;
2. use a nonanalytic root/sign prescription and test its \(C^2\) Hessian;
3. introduce derivative invariants or another covariant structure;
4. abandon this spherical target as the base for a globally differentiable
   4D NLQT action.

Only after resolving this sign gate should another large invariant atlas be
generated.

---

# 9. Literature relation

The 2025/2026 NPQT construction explicitly emphasizes that the
four-dimensional covariant lift of a spherical reduced action is nonunique and
that displayed rational representatives may have denominator-zero issues away
from spherical symmetry.

The present atlas calculation sharpens that open issue.

Relevant references:

1. P. Bueno, P. A. Cano, R. A. Hennigar, Á. J. Murcia,
   *Regular black hole formation in four-dimensional non-polynomial
   gravities*, Phys. Rev. D **113**, 024019 (2026),
   arXiv:2509.19016.
2. J. Carminati, R. G. McLenaghan,
   *Algebraic invariants of the Riemann tensor in a four-dimensional
   Lorentzian space*, J. Math. Phys. **32**, 3135 (1991).
3. K. Santosuosso, D. Pollney, N. Pelavas, P. Musgrave, K. Lake,
   *Invariants of the Riemann tensor for Class B Warped Product Spacetimes*,
   arXiv:gr-qc/9809012.

No priority claim is made for the invariant-theory interpretation until a
targeted literature search for this exact NPQT sign obstruction is complete.
