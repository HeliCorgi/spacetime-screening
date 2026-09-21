# Principal-Safety Gate: Analytic Class II / GQTG vs Nonlocal QTG

This note applies the repository's updated principal-safety gate to the two
main post-vector candidates:

1. analytic Class-II QTG-TNT / four-dimensional generalized
   quasi-topological gravity (GQTG);
2. nonlocal quasitopological gravity (NLQT).

The key lesson from the rejected two-vector model is that a regular background
does not suffice.  The physical quadratic operator must remain nondegenerate,
ghost-free, and well defined on the target regular-black-hole background.

## 1. Gate A — auxiliary derivative mixing

The two-vector failure had the structure

\[
K_{\rm red}
=
C-B^{\rm T}A^{-1}B,
\]

with no direct auxiliary kinetic term,

\[
C=0,
\]

and nonzero derivative mixing \(B\).  A surviving active direction therefore
inherited a negative kinetic sign.

### Analytic Class II / GQTG

These are pure-metric theories.

There is no additional auxiliary matter/vector sector of the type that caused
the two-vector failure.

**Result:**

\[
\boxed{\text{PASS / not applicable}}
\]

for this specific auxiliary-mixing gate.

### Nonlocal QTG

The fundamental formulation is also pure metric,

\[
S_{\rm NLQT}
=
S_{\rm QT}
-
\frac12
\int\sqrt{|g|}
\,
\hat{\mathcal E}^{ab}
\mathcal F_{ab}{}^{cd}
\hat{\mathcal E}_{cd}.
\]

The auxiliary \(e_{ab},\lambda_{ab}\) variables used in the source's
linearized proof are an equivalent reformulation, not new fundamental
black-hole hair.

**Result:**

\[
\boxed{\text{PASS / not applicable}}
\]

for the original two-vector-style gate.

## 2. Gate B — local order-reduction / strong coupling

Passing Gate A is not enough.

Analytic Class-II QTG-TNT reduces, for static spherical symmetry, to the
four-dimensional GQTG family.  The cubic member contains Einsteinian cubic
gravity.

These theories are constructed so that their linearized equations on
maximally symmetric backgrounds possess a reduced Einstein-like spectrum,
while the equations on generic backgrounds contain higher-derivative
structures.

That mismatch is precisely the known strong-coupling problem of ECG/GQTG.

Published black-hole odd-parity analyses also find an asymptotically
degenerate principal part for spherical solutions approaching maximally
symmetric asymptotics.

Therefore a local analytic Class-II / GQTG tower, regarded as a complete
nonperturbative theory, fails the project's requirement that the physical
principal operator have stable rank across the backgrounds of interest.

\[
\boxed{
\text{local analytic Class II / GQTG: FAIL as a complete screening theory}
}
\]

This does not rule out using finite GQTG terms perturbatively as EFT
corrections below their cutoff.

## 3. Gate C — regular-core resummation

There is a second issue specific to trying to obtain a regular finite-curvature
vacuum core from an analytic four-dimensional GQTG tower.

The repository's all-order spherical calculation finds that every finite
curvature order contributes

\[
F_n
\sim
-\frac12 c^n r^3
\]

on an exact de Sitter-type core,

\[
f=1-cr^2.
\]

A finite truncation therefore vanishes as

\[
r^3
\]

at the center.

A normally/uniformly convergent infinite tower also retains this \(r^3\)
suppression and cannot equal a nonzero mass integration constant.

If the curvature variable approaches a finite limiting value as

\[
c(r)-c_*
\sim
a r^p,
\]

then a nonzero mass requires a nonuniform resummed spherical response

\[
\boxed{
\mathcal G(c)
\sim
|c-c_*|^{-3/p}.
}
\]

Consequently,

\[
\mathcal G'(c)
\sim
|c-c_*|^{-3/p-1},
\]

and

\[
\mathcal G''(c)
\sim
|c-c_*|^{-3/p-2}.
\]

This is a **resummation gate**, not by itself a proof that the fundamental
four-dimensional action is singular.

A successful local infinite-tower proposal would have to demonstrate that its
full physical quadratic operator remains finite and nondegenerate despite the
nonuniform spherical resummation.

No such construction is assumed here.

## 4. Gate D — nonlocal order restoration

The 2026 NLQT proposal was designed specifically to cure the local QT
order-reduction problem.

It defines

\[
\hat{\mathcal E}_{ab}
=
P_{acde}R_b{}^{cde}
-\frac12\mathcal L_{\rm QT}g_{ab},
\]

and adds

\[
-\frac12
\hat{\mathcal E}^{ab}
\mathcal F_{ab}{}^{cd}
\hat{\mathcal E}_{cd}.
\]

For a finite \(2N\)-derivative truncation of \(\mathcal F\), the source shows
that both the full equations and the linearized equations on generic,
maximally symmetric, and spherically symmetric backgrounds have the same
order,

\[
2N+4.
\]

Thus the specific derivative-order reduction responsible for local QT strong
coupling is removed.

**Result:**

\[
\boxed{
\text{NLQT order-reduction gate: PASS}
}
\]

within the construction stated in the source.

## 5. Gate E — zero-free quadratic form factor

The proposed infinite-derivative choice is

\[
\mathcal F
=
\frac{
e^{\Omega(\hat{\mathcal D})}-\mathbb I
}{
\hat{\mathcal D}
},
\]

where \(\Omega\) is entire and \(\Omega(0)=0\).

On perturbation subspaces where

\[
\mathcal D
=
\hat{\mathcal D}
=
\hat{\mathcal D}^{\dagger},
\]

the quadratic operator factorizes schematically as

\[
\boxed{
\hat{\mathcal D}
\,
e^{\Omega(\hat{\mathcal D})}.
}
\]

Since an exponential of an entire function has no finite zeros,

\[
\ker
\left[
e^{\Omega(\hat{\mathcal D})}
\right]
=
0.
\]

Hence the linearized kernel is the same as the original
\(\hat{\mathcal D}\) kernel and no additional pole is introduced.

The source establishes this restricted factorization for:

1. perturbations around maximally symmetric backgrounds;
2. spherically symmetric perturbations of spherically symmetric vacuum
   backgrounds.

**Result:**

\[
\boxed{
\text{NLQT zero-free gate: PASS on the proven subspaces}
}
\]

## 6. Gate F — generic nonspherical regular-BH perturbations

This is the decisive remaining gap.

For a general background/perturbation, the source explicitly distinguishes

\[
\mathcal D
\neq
\hat{\mathcal D}
\]

in general, and \(\hat{\mathcal D}\) is not generally self-adjoint.

The clean factorization

\[
\hat{\mathcal D}
e^{\Omega(\hat{\mathcal D})}
\]

therefore does **not** constitute a proof for generic odd/even nonspherical
perturbations of the regular black hole.

This is exactly the sector in which the two-vector benchmark failed.

Thus:

\[
\boxed{
\text{NLQT generic nonspherical RBH principal gate: OPEN}
}
\]

The next serious calculation should derive the odd-parity black-hole
quadratic/pseudodifferential operator and inspect its kernel, kinetic
signature, and characteristic structure.

## 7. Gate G — four-dimensional covariant-action differentiability

There is an additional issue for this repository because the target dimension
is four.

The NLQT paper notes that exact four-dimensional QT densities reproducing the
same regular-BH spherical equations require nonpolynomial gravitational
densities.

Therefore the nonlocal completion does not automatically erase the
repository's earlier four-dimensional covariant-lift problem.

A complete 4D candidate must specify a base \(\mathcal L_{\rm QT}\) for which

\[
\mathcal L_{\rm QT},
\qquad
\frac{\partial\mathcal L_{\rm QT}}{\partial R_{\mu\nu\rho\sigma}},
\qquad
\frac{\partial^2\mathcal L_{\rm QT}}
{\partial R_{\mu\nu\rho\sigma}
 \partial R_{\alpha\beta\gamma\delta}}
\]

are well defined on the regular black-hole background.

The rational representative previously analyzed in this repository fails this
test.

Therefore:

\[
\boxed{
\text{NLQT as a fully specified 4D completion: OPEN}
}
\]

until a regular four-dimensional QT base action is supplied.

## 8. Current gate matrix

| Gate | Analytic Class II / local GQTG | Nonlocal QTG |
|---|---|---|
| Auxiliary derivative mixing | PASS / N.A. | PASS / N.A. |
| Covariant polynomial differentiability | PASS order-by-order | Depends on 4D QT base |
| Local order-reduction strong coupling | FAIL / structural concern | PASS by construction |
| Finite-order regular vacuum core | FAIL | RBH inherited from infinite QT base |
| Nonuniform resummation needed | YES | YES in the QT background sector |
| Zero-free no-extra-pole factorization | N.A. | PASS on proven subspaces |
| SS regular-BH perturbations | local strong-coupling concern | PASS / perturbative Birkhoff |
| Generic nonspherical RBH sector | FAIL/known concern for local GQTG class | OPEN |
| Fully regular 4D covariant base | polynomial but no regular RBH completion | OPEN |

## 9. Verdict

### Local analytic Class II / GQTG

Keep as:

- analytic/polynomial building blocks;
- EFT corrections;
- a useful control family.

Do **not** promote them as the full nonperturbative Spacetime Screening
completion.

\[
\boxed{
\text{status: REJECT as complete theory, RETAIN as EFT/building block}
}
\]

### Nonlocal QTG

This is currently the strongest surviving candidate because it directly
targets the two structural failures that killed the local and auxiliary-field
models:

- principal-order reduction;
- extra propagator poles.

However, for the four-dimensional project there are two unresolved gates:

\[
\boxed{
\begin{aligned}
&\text{regular 4D covariant QT base action},\\
&\text{generic nonspherical RBH quadratic operator}.
\end{aligned}
}
\]

Therefore:

\[
\boxed{
\text{status: LEADING CANDIDATE, NOT YET PRINCIPAL-SAFE VERIFIED}
}
\]

## Reproducibility

Run

\`\`\`bash
python src/symbolic/classII_resummation_gate.py
python src/symbolic/nonlocal_qtg_gate.py
\`\`\`

together with the existing GQTG core-scaling scripts.


## 10. Generic factorization warning

The zero-free entire-function argument should not be extended beyond the
subspaces on which the source proves the required operator identities.

Schematically the quadratic operator is

\[
\mathcal Q
=
\mathcal D
+
\hat{\mathcal D}^{\dagger}
\mathcal F(\hat{\mathcal D})
\hat{\mathcal D}.
\]

On the proven subspace,

\[
\mathcal D
=
\hat{\mathcal D}
=
\hat{\mathcal D}^{\dagger},
\]

so

\[
\mathcal Q
=
\hat{\mathcal D}
e^{\Omega(\hat{\mathcal D})}.
\]

For a generic nonspherical regular-black-hole perturbation define

\[
\Delta\mathcal D
=
\mathcal D-\hat{\mathcal D}.
\]

Even in a commuting scalar toy reduction,

\[
\mathcal D=h+\delta,
\qquad
\hat{\mathcal D}=h,
\]

the quadratic eigenvalue becomes

\[
Q(h,\delta)
=
\delta
+
h e^{\Omega(h)}.
\]

The exponential can be zero-free while \(Q\) still vanishes because of the
mismatch term \(\delta\).

Therefore:

\[
\boxed{
e^{\Omega}\ \text{zero-free}
\not\Rightarrow
\mathcal Q\ \text{zero-kernel}
}
\]

unless the factorizing operator relation is established.

This does not demonstrate an NLQT ghost.  It identifies the exact operator
that must be controlled next:

\[
\boxed{
\Delta\mathcal D_{\rm odd/even}
=
\delta
\left(
2\nabla^c\nabla^dP_{acbd}
\right).
}
\]

See \`src/symbolic/nonlocal_qtg_nonspherical_gate.py\`.


## References

- A. Colléaux, I. Kolář, T. Málek,
  *Quasi-topological gravity for 4-dimensional Taub-NUT, near-horizon extreme
  Kerr, and swirling symmetries*, arXiv:2606.17784.
- J. Beltrán Jiménez, A. Jiménez-Cano,
  *On the strong coupling of Einsteinian Cubic Gravity and its
  generalisations*, JCAP **01** (2021) 069, arXiv:2009.08197.
- J. Beltrán Jiménez, A. Jiménez-Cano,
  *On the physical viability of black hole solutions in Einsteinian Cubic
  Gravity and its generalisations*, Phys. Dark Univ. **43** (2024) 101387.
- P. Bueno, P. A. Cano, R. A. Hennigar, Á. J. Murcia,
  *Regular Black Holes in Nonlocal Quasitopological Gravity*,
  arXiv:2607.07790 (2026).
