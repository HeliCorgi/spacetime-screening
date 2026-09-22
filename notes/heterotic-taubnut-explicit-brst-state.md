# Explicit Untwisted BRST Physical State in Exact Heterotic Taub–NUT

**Status:** explicit construction / adversarial check, 2026-09-22.

This note answers the chronology gate:

\[
\boxed{
\text{Can one actually construct one untwisted BRST-physical heterotic state
with chronology-relevant Taub--NUT quantum numbers?}
}
\]

The result is:

\[
\boxed{
\textbf{YES: an explicit untwisted physical state can be constructed.}
}
\]

The construction is exact at the worldsheet zero-mode/current-algebra level,
uses an anomaly-free integer-charge point of the Johnson--Svendsen heterotic
coset, and has a nontrivial relative gauge-BRST cohomology class.

With a neutral spectator heterotic oscillator, it obeys the standard heterotic
NS physical-state weights

\[
(h_L,h_R)=(1,\tfrac12).
\]

Its exact quantum numbers also match the propagating principal-continuous
solution of the minisuperspace radial equation derived previously, and its
horizon-to-NUT hypergeometric connection coefficients are finite and nonzero.

Executable algebra:

src/symbolic/heterotic_taubnut_explicit_brst_state.py

This result establishes the physical-state existence gate. It does not yet
establish an interacting operational return to the causal past.

---

# 1. Exact anomaly-free background point

Take

\[
\boxed{
k_1=8,\qquad k_2=4,
}
\]

so that \(k_1=k_2+4\).

Choose integer left-moving heterotic charges

\[
\boxed{
(Q_A,P_A)=(2,0),
\qquad
(Q_B,P_B)=(2,1),
}
\]

and embedding parameters

\[
\boxed{
\delta^2=\frac85,
\qquad
\lambda^2=\frac25,
}
\]

with positive roots.

The three Johnson--Svendsen anomaly equations are

\[
-k_1(1-\delta^2)
=
2(Q_A^2+P_A^2-\delta^2),
\]

\[
k_1\delta\lambda
=
2(Q_AQ_B+P_AP_B-\delta\lambda),
\]

\[
k_2+k_1\lambda^2
=
2(Q_B^2+P_B^2-(1+\lambda^2)).
\]

For these values all three vanish identically.

The left and right gauge-current level matrices agree:

\[
\boxed{
K_L=K_R
=
K
=
\begin{pmatrix}
8&4\\
4&5
\end{pmatrix},
}
\]

with

\[
\boxed{
K^{-1}
=
\begin{pmatrix}
5/24&-1/6\\
-1/6&1/3
\end{pmatrix}.
}
\]

---

# 2. Explicit untwisted affine primary

Choose the \(SL(2,\mathbb R)_{8}\) principal continuous representation

\[
\boxed{
j=\frac12+\frac{i}{2}.
}
\]

Its quadratic Casimir is

\[
\boxed{
-j(j-1)=\frac12.
}
\]

Choose hyperbolic Cartan eigenvalues

\[
\boxed{
m=-2,
\qquad
\bar M=\frac{\sqrt{10}}2.
}
\]

For \(SU(2)_4\), choose the integrable representation

\[
\boxed{\ell=1},
\]

with

\[
n=0,
\qquad
\boxed{\bar N=-1}.
\]

Since \(0\le\ell\le k_2/2=2\), this is allowed.

Set the heterotic gauge-fermion Cartan excitations to zero:

\[
s_1=s_2=f_1=f_2=0.
\]

No discrete chronology-winding label \(w\) is introduced. This is an
untwisted state.

---

# 3. Both exact gauge constraints vanish

The gauge-neutrality combinations are

\[
\mathcal G_A
=
m+\delta\bar M
+
Q_As_1+P_As_2,
\]

\[
\mathcal G_B
=
\lambda\bar M+\bar N
+
Q_Bs_1+P_Bs_2.
\]

For the explicit state,

\[
\delta\bar M=2,
\qquad
\lambda\bar M=1.
\]

Hence

\[
\boxed{\mathcal G_A=-2+2=0},
\qquad
\boxed{\mathcal G_B=1-1=0}.
\]

The chiral matter gauge-charge vectors are

\[
\boxed{
J_L=(-2,0),
\qquad
J_R=(2,0).
}
\]

The auxiliary gauge bosons take opposite charges,

\[
a_L=(2,0),
\qquad
a_R=(-2,0),
\]

so each chiral total gauge zero mode vanishes separately.

---

# 4. Exact coset conformal weight

The bosonic affine-primary contribution from \(SL(2,\mathbb R)_8\) is

\[
h_{SL(2)}
=
\frac{-j(j-1)}{k_1-2}
=
\boxed{\frac1{12}}.
\]

The \(SU(2)_4\) affine-primary contribution is

\[
h_{SU(2)}
=
\frac{\ell(\ell+1)}{k_2+2}
=
\boxed{\frac13}.
\]

Thus

\[
\boxed{
h_{\rm num}=\frac5{12}.
}
\]

In the BRST gauged-WZW realization the auxiliary gauge sector contributes

\[
h_{\rm gauge}
=
-\frac12J^TK^{-1}J.
\]

For either \(J=(\pm2,0)\),

\[
\frac12J^TK^{-1}J
=
\boxed{\frac5{12}}.
\]

Therefore

\[
\boxed{
h_L^{\rm coset}=h_R^{\rm coset}=0.
}
\]

This is an exact cancellation.

---

# 5. Gauge-BRST closure

Because the gauged subgroup is Abelian, the gauge BRST charge has schematic
form

\[
Q_H
=
\sum_{a=A,B}
\sum_n
c^a_{-n}\mathcal J^a_n,
\]

where

\[
\mathcal J^a_n
=
J^a_{{\rm matter},n}
+
J^a_{{\rm aux},n}.
\]

Anomaly cancellation gives zero total gauge-current level and hence
\(Q_H^2=0\).

Take

\[
|\Phi_{\rm coset}\rangle
=
|\Phi_{\rm matter}\rangle
\otimes
|a_L=-J_L,a_R=-J_R\rangle_{\rm aux}
\otimes
|0\rangle_{bc,H}.
\]

All positive total gauge-current modes annihilate this state because the
numerator state and auxiliary state are highest-weight states, while the zero
modes vanish by the explicit charge cancellation.

Thus

\[
\boxed{
Q_H|\Phi_{\rm coset}\rangle=0.
}
\]

---

# 6. Gauge-BRST non-exactness

Use the standard relative gauge-BRST complex,

\[
b_0^A|\Psi\rangle=b_0^B|\Psi\rangle=0.
\]

The constructed state has gauge ghost number \(0\) and oscillator grade \(0\).

If it were exact,

\[
|\Phi_{\rm coset}\rangle=Q_H|\chi\rangle,
\]

then \(|\chi\rangle\) would need ghost number \(-1\) and grade \(0\), since
\(Q_H\) preserves the current/ghost grading.

But in the relative complex the only would-be grade-zero ghost-number-\(-1\)
operators are the \(b_0^a\), which are removed by the relative condition.
Every \(b^a_{-n}\) with \(n>0\) carries positive grade.

Therefore no such \(|\chi\rangle\) exists.

Hence

\[
\boxed{
|\Phi_{\rm coset}\rangle
\text{ is BRST-closed and non-exact in the relative Abelian coset complex.}
}
\]

This is consistent with the general gauged-WZW BRST literature, where the
BRST construction reproduces the coset physical spectrum.

---

# 7. Critical heterotic completion and a full string state

The original heterotic-coset construction allows an unspecified internal CFT
to complete the four-dimensional \(c=6\) sector to the critical heterotic
central charges.

Use a neutral spectator sector containing a compact coordinate \(Y\) and its
right-moving NS superpartner.

Define

\[
\boxed{
|\Psi_{\rm matter}\rangle
=
\alpha^Y_{-1,L}
\bar\psi^Y_{-1/2,R}
|\Phi_{\rm coset}\rangle.
}
\]

Take zero spectator momentum along \(Y\).

Then

\[
h_L=0+1=\boxed{1},
\qquad
h_R=0+\frac12=\boxed{\frac12}.
\]

Thus the standard heterotic NS mass-shell and level conditions are satisfied.

In the \(-1\) picture, an unintegrated vertex is

\[
\boxed{
\mathcal V_{-1}
=
c\bar c\,
e^{-\bar\varphi}\,
(i\partial Y_L)\,
\bar\psi_R^Y\,
\Phi_{\rm coset}.
}
\]

The right-moving state contains one NS fermion and therefore has the usual
odd-fermion GSO parity.

Because the spectator direction is neutral under both gauged Abelian factors,
the Taub--NUT gauge constraints are unchanged.

---

# 8. Full string BRST closure and non-exactness

The positive left Virasoro constraint on
\(\alpha_{-1}^Y|\Phi_{\rm coset}\rangle\) reduces to the ordinary transverse
condition proportional to spectator momentum \(p_Y\), which is zero.

Likewise the positive right super-Virasoro condition on
\(\bar\psi_{-1/2}^Y|\Phi_{\rm coset}\rangle\) is proportional to \(p_Y\) and
vanishes.

All higher positive modes annihilate the affine-primary/spectator vacuum.

Therefore this state obeys the standard heterotic BRST physical conditions.

It is not a longitudinal spurious state: its polarization is a neutral
spectator direction with zero momentum in that direction.

The norm is the product of the generalized principal-continuous
\(SL(2,\mathbb R)\) norm, the positive \(SU(2)\) norm and positive spectator
oscillator norms. Principal continuous representations
\(j=\tfrac12+is\) are part of the standard \(SL(2,\mathbb R)\) WZW spectrum
and are included in no-ghost analyses.

Thus, with the usual delta normalization of a scattering state,

\[
\boxed{
|\Psi\rangle
\text{ is a nonzero untwisted heterotic BRST physical state.}
}
\]

A finite wave packet may be formed by superposing nearby continuous labels
with spectator momentum adjusted to preserve the mass shell, while keeping
the polarization in a different neutral spectator direction.

---

# 9. Global chronology quantum numbers

Identify the positive target-frequency quantum number with

\[
\boxed{
\omega=\bar M=\frac{\sqrt{10}}2.
}
\]

Then

\[
q=\lambda\omega=\boxed{1}.
\]

Since

\[
t\sim t+4\pi\lambda,
\]

single-valuedness requires

\[
2\lambda\omega\in\mathbb Z.
\]

For this state,

\[
\boxed{
2\lambda\omega=2.
}
\]

Thus the physical state is globally single-valued around the periodic
chronology direction.

The \(B\)-gauge constraint is simultaneously

\[
\lambda\bar M+\bar N=1-1=0.
\]

---

# 10. Exact match to the NUT scattering solution

For \(q=1\) and \(\ell=1\), the scalar/monopole separation constant is

\[
\boxed{
\Lambda=\ell(\ell+1)-q^2=1.
}
\]

At \(k_1=8\),

\[
A=\frac{k_1-2}{k_1+2}=\boxed{\frac35}.
\]

The NUT-infinity radial exponent parameter is

\[
\nu^2
=
\frac14+\Lambda-\omega^2A.
\]

Since \(\omega^2=5/2\),

\[
\boxed{
\nu^2=-\frac14.
}
\]

Thus

\[
\boxed{
R\sim x^{-1/2\pm i/2}.
}
\]

This exactly matches the principal-continuous label

\[
j=\frac12+\frac{i}{2}.
\]

The affine state that passes the BRST constraints is therefore the same
representation expected from the propagating NUT-region minisuperspace mode.

---

# 11. The first positive NUT region is nonsingular

For this explicit anomaly-free background,

\[
D(x)
=
\frac{3x^2+4\sqrt{10}\,x+10}{5}.
\]

Its roots are

\[
\boxed{
x=-\sqrt{10},
\qquad
x=-\frac{\sqrt{10}}3.
}
\]

Both are below \(-1\). Hence

\[
\boxed{
D(x)>0\quad\text{for all }x>1.
}
\]

The entire first positive NUT region is free of the \(D(x)=0\) curvature
singularities.

---

# 12. Exact horizon-to-NUT connection is nonzero

For this state,

\[
C=\Lambda-\omega^2A=-\frac12.
\]

Choose

\[
h=-\frac12+\frac{i}{2},
\qquad
h(h+1)=C.
\]

The exact hypergeometric connection coefficients are

\[
A_h
=
\frac{\Gamma(c)\Gamma(b-a)}
{\Gamma(b)\Gamma(c-a)},
\qquad
B_h
=
\frac{\Gamma(c)\Gamma(a-b)}
{\Gamma(a)\Gamma(c-b)}.
\]

For the explicit state,

\[
b-a=i,
\qquad
a-b=-i,
\]

while all denominator arguments

\[
a,\ b,\ c-a,\ c-b
\]

have real part \(1/2\).

No denominator argument is a non-positive integer pole. Since the Gamma
function has no zeros,

\[
\boxed{
A_h\neq0,
\qquad
B_h\neq0.
}
\]

Thus the explicit BRST-state quantum numbers have nonzero exact continuation
from the chronology horizon into the NUT asymptotic basis.

---

# 13. What is established now

At the explicit anomaly-free model point above, there exists an untwisted
state satisfying:

\[
\boxed{
\begin{aligned}
&\text{both exact gauge constraints},\\
&\text{nontrivial relative gauge-BRST cohomology},\\
&h_L^{\rm coset}=h_R^{\rm coset}=0,\\
&\text{heterotic NS matter weights }(1,\tfrac12),\\
&\text{principal-continuous }SL(2,\mathbb R)\text{ representation},\\
&\text{global }t\text{-periodicity},\\
&\text{NUT-region continuum asymptotics},\\
&\text{nonzero exact horizon-to-NUT connection}.
\end{aligned}
}
\]

Therefore the simple chronology-protection statement

\[
\boxed{
\text{“no physical untwisted string state can carry the required NUT quantum
numbers”}
}
\]

does not survive this explicit construction.

---

# 14. What is still not established

This does not yet prove an operational trip to the past.

The remaining gates are:

1. a properly normalized physical coset/string two-point or flux observable
   for this specific state;
2. finite interacting amplitudes and sensible factorization;
3. absence of pair-production, condensation or other chronology-sector
   instability;
4. finite-\(g_s\) backreaction control;
5. a gauge-invariant relational observable representing a completed
   closed-timelike return.

The first remaining question is no longer whether a physical state exists.
It is whether the physical transmission observable for this state remains
finite and nonzero after full normalization and interactions.

---

# 15. Effect on the time-travel verdict

Before this construction, the chain was

\[
\text{exact CTC geometry}
+
\text{minisuperspace transmission}
+
\boxed{\text{physical state OPEN}}.
\]

Now it is

\[
\boxed{
\text{exact CTC geometry}
+
\text{explicit untwisted BRST physical state}
+
\text{nonzero exact minisuperspace horizon-to-NUT connection}.
}
\]

So a state-space chronology-protection mechanism is no longer available at
this explicit point.

The current verdict becomes

\[
\boxed{
\textbf{physical access to the NUT/CTC region is supported at the
free-string/minisuperspace level.}
}
\]

Operational past-directed time travel remains unproved because the
interaction, backreaction and return-observable gates remain.

---

# 16. Prior-art status

The ingredients are standard:

- heterotic cosets use anomaly-cancelled asymmetric gauged WZW models;
- gauged-WZW BRST quantization reproduces coset physical spectra and has
  nontrivial cohomology;
- principal continuous \(SL(2,\mathbb R)\) representations
  \(j=\tfrac12+is\) occur in the WZW spectrum and are covered by no-ghost
  analyses;
- hyperbolic-basis continuous representations are standard in BTZ string
  quantization.

No prior work located in this project explicitly constructs the
Johnson--Svendsen Taub--NUT state above and matches it to its nonzero
horizon-to-NUT radial connection.

Label this:

**NEW CALCULATION CANDIDATE / requires independent reproduction.**

Do not make a priority claim.

---

# 17. References

1. C. V. Johnson and H. G. Svendsen,
   *An Exact String Theory Model of Closed Time-Like Curves and Cosmological
   Singularities*, Phys. Rev. D **70**, 126011 (2004),
   arXiv:hep-th/0405141.

2. C. V. Johnson,
   *Heterotic Cosets*, arXiv:hep-th/9409061.

3. D. Karabali and H. J. Schnitzer,
   *BRST Quantization of the Gauged WZW Action and Coset Conformal Field
   Theories*, Nucl. Phys. B **329** (1990) 649.

4. S. Hwang and H. Rhedin,
   *The BRST formulation of G/H WZNW models*, arXiv:hep-th/9305174.

5. S. Hwang and H. Rhedin,
   *Construction of BRST invariant states in G/H WZNW models*,
   arXiv:hep-th/9501084.

6. J. Maldacena and H. Ooguri,
   *Strings in AdS3 and the SL(2,R) WZW Model. Part 1: The Spectrum*,
   J. Math. Phys. **42** (2001) 2929, arXiv:hep-th/0001053.

7. S. Hemming and E. Keski-Vakkuri,
   *The spectrum of strings on BTZ black holes and spectral flow in the
   SL(2,R) WZW model*, Nucl. Phys. B **626** (2002) 363,
   arXiv:hep-th/0110252.

8. S. Hemming,
   *On Free Field Realizations of Strings in BTZ*,
   arXiv:hep-th/0304009.

---

# 18. Restart point

Do not search again for a state. An explicit untwisted state has now been
constructed.

Restart from the vertex

\[
\boxed{
\mathcal V_{-1}
=
c\bar c\,e^{-\bar\varphi}
(i\partial Y_L)\bar\psi_R^Y
\Phi_{
j=\frac12+\frac i2,\,
m=-2,\,
\bar M=\frac{\sqrt{10}}2;\,
\ell=1,\,
\bar N=-1
}.
}
\]

The next task is to turn its already-nonzero minisuperspace connection into a
properly normalized BRST/coset transmission observable and then test
interactions/backreaction.
