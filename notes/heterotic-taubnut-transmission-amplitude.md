# Flux-Normalized Taub–NUT Transmission Amplitude for the Explicit BRST State

**Status:** exact free-string/minisuperspace channel calculation, 2026-09-22.

This note continues:

- notes/heterotic-taubnut-explicit-brst-state.md
- notes/heterotic-taubnut-time-travel-decision.md

and uses the explicit untwisted BRST physical state already constructed there.

The purpose is to compute the first properly normalized transmission quantity
for that state.

The result is:

\[
\boxed{
\mathcal T_{\rm H\leftrightarrow NUT}
=
0.998130316064461877\ldots
}
\]

with reflection probability

\[
\boxed{
\mathcal R
=
0.001869683935538123\ldots
}
\]

and

\[
\boxed{
\mathcal R+\mathcal T=1
}
\]

to high numerical precision and analytically by the Wronskian identity.

This is a **flux-normalized one-particle transmission coefficient** for the
explicit BRST physical state in the exact metric+dilaton minisuperspace
problem.

Because the radial operator is real, the horizon↔NUT transmission probability
is reciprocal. The Taub region itself is not a conventional stationary
scattering exterior, so this should not be mislabeled as a standard
asymptotic Taub S-matrix.

It is nevertheless the correct normalized free-string channel coefficient
for the analytically continued physical mode crossing the first chronology
horizon and propagating into the positive NUT region.

Executable check:

src/symbolic/heterotic_taubnut_transmission_amplitude.py

---

# 1. Explicit physical state

Use the anomaly-free model point

\[
k_1=8,
\qquad
k_2=4,
\]

\[
(Q_A,P_A)=(2,0),
\qquad
(Q_B,P_B)=(2,1),
\]

\[
\delta^2=\frac85,
\qquad
\lambda^2=\frac25.
\]

The explicit untwisted BRST state has

\[
j=\frac12+\frac{i}{2},
\qquad
m=-2,
\qquad
\bar M=\omega=\frac{\sqrt{10}}{2},
\]

\[
\ell=1,
\qquad
\bar N=-1.
\]

Its monopole charge and angular separation constant are

\[
q=\lambda\omega=1,
\qquad
\Lambda=\ell(\ell+1)-q^2=1.
\]

The physical-state construction and BRST non-exactness are documented
separately.

---

# 2. Exact radial equation

The exact dilaton-weighted minisuperspace radial equation is

\[
\frac{d}{dx}
\left[
(x^2-1)\frac{dR}{dx}
\right]
+
\left[
\omega^2\frac{D(x)}{x^2-1}
-
\Lambda
\right]R
=
0.
\]

For the explicit state,

\[
\omega=\frac{\sqrt{10}}2,
\qquad
\Lambda=1.
\]

Set

\[
u=\frac{x-1}{2}.
\]

Then the first positive NUT region is

\[
u>0.
\]

The horizon is \(u=0\), while NUT infinity is \(u\to+\infty\).

---

# 3. Horizon and NUT flux bases

Define

\[
a_+
=
\frac{\omega(1+\delta)}{2}.
\]

For the explicit model,

\[
2a_+
=
\omega+2.
\]

The purely future-horizon ingoing branch is

\[
R_H
\sim
u^{-ia_+}.
\]

Its conserved radial flux is

\[
\mathcal J_H
=
-2a_+
=
-(\omega+2).
\]

At NUT infinity the two propagating powers are

\[
u^{-1/2\pm i\rho},
\]

with

\[
\rho=\frac12.
\]

Their fluxes are

\[
\mathcal J_{\pm}
=
\pm2\rho
=
\pm1.
\]

Therefore the unit-flux bases may be chosen as

\[
H_{\rm in}
=
\frac{u^{-ia_+}}{\sqrt{2a_+}},
\]

\[
N_{\rm in}
=
\frac{u^{-1/2-i\rho}}{\sqrt{2\rho}},
\qquad
N_{\rm out}
=
\frac{u^{-1/2+i\rho}}{\sqrt{2\rho}}.
\]

---

# 4. Exact hypergeometric connection coefficients

For the horizon-ingoing solution, write

\[
R_H
=
u^\alpha(1+u)^\beta
\,{}_2F_1(a,b;c;-u),
\]

with

\[
\alpha=-ia_+,
\]

\[
a
=
\frac12
-
i\left(
\omega+\frac12
\right),
\]

\[
b
=
\frac12
-
i\left(
\omega-\frac12
\right),
\]

\[
c
=
1-i(\omega+2).
\]

Useful exact differences are

\[
b-a=i,
\]

\[
c-a
=
\frac12-\frac{3i}{2},
\]

\[
c-b
=
\frac12-\frac{5i}{2}.
\]

At NUT infinity,

\[
R_H
\sim
A_{\rm out}
u^{-1/2+i/2}
+
B_{\rm in}
u^{-1/2-i/2},
\]

with

\[
\boxed{
A_{\rm out}
=
\frac{
\Gamma(c)\Gamma(i)
}{
\Gamma(b)\Gamma(c-a)
}
}
\]

and

\[
\boxed{
B_{\rm in}
=
\frac{
\Gamma(c)\Gamma(-i)
}{
\Gamma(a)\Gamma(c-b)
}.
}
\]

These are the standard Gauss-hypergeometric connection coefficients for the
infinity basis.

---

# 5. Flux-normalized amplitudes

The scattering relation is

\[
N_{\rm in}
\longrightarrow
r\,N_{\rm out}
+
t\,H_{\rm in}.
\]

With the basis above,

\[
\boxed{
r
=
\frac{A_{\rm out}}{B_{\rm in}}
}
\]

and

\[
\boxed{
t
=
\sqrt{\frac{a_+}{\rho}}
\frac{1}{B_{\rm in}}.
}
\]

Since \(\rho=1/2\) and \(2a_+=\omega+2\),

\[
\boxed{
t
=
\sqrt{\omega+2}
\,
\frac{
\Gamma(a)\Gamma(c-b)
}{
\Gamma(c)\Gamma(-i)
}.
}
\]

This is a phase-convention-dependent complex amplitude.

The invariant physical quantities are

\[
\mathcal T=|t|^2,
\qquad
\mathcal R=|r|^2.
\]

---

# 6. Closed forms for reflection and transmission

Using

\[
|\Gamma(1+iy)|^2
=
\frac{\pi y}{\sinh(\pi y)},
\]

\[
|\Gamma(iy)|^2
=
\frac{\pi}{y\sinh(\pi y)},
\]

and

\[
\left|
\Gamma\left(\frac12+iy\right)
\right|^2
=
\frac{\pi}{\cosh(\pi y)},
\]

one obtains

\[
\boxed{
\mathcal R
=
\frac{
\cosh\left[\pi(\omega-\tfrac12)\right]
\cosh(\tfrac{3\pi}{2})
}{
\cosh\left[\pi(\omega+\tfrac12)\right]
\cosh(\tfrac{5\pi}{2})
}.
}
\]

The transmission probability is

\[
\boxed{
\mathcal T
=
\frac{
\sinh\left[\pi(\omega+2)\right]
\sinh\pi
}{
\cosh\left[\pi(\omega+\tfrac12)\right]
\cosh(\tfrac{5\pi}{2})
}.
}
\]

For

\[
\omega=\frac{\sqrt{10}}2,
\]

this gives

\[
\boxed{
\mathcal R
=
0.0018696839355381227\ldots
}
\]

and

\[
\boxed{
\mathcal T
=
0.9981303160644618773\ldots
}
\]

so

\[
\boxed{
99.8130316064\%\text{ transmission}
}
\]

in this free-string/minisuperspace channel.

---

# 7. Exact flux conservation

The hypergeometric coefficients obey

\[
|B_{\rm in}|^2
-
|A_{\rm out}|^2
=
\omega+2.
\]

This is precisely the horizon flux magnitude for the unit-amplitude
horizon mode.

The underlying hyperbolic identity is

\[
\cosh\left[\pi(\omega+\tfrac12)\right]
\cosh\left(\frac{5\pi}{2}\right)
-
\cosh\left[\pi(\omega-\tfrac12)\right]
\cosh\left(\frac{3\pi}{2}\right)
\]

\[
=
\sinh[\pi(\omega+2)]
\sinh\pi.
\]

Therefore

\[
\boxed{
\mathcal R+\mathcal T=1
}
\]

exactly.

No missing flux is required at the free minisuperspace level.

---

# 8. Numerical complex amplitudes in one convention

Using the principal Gamma-function branches associated with the basis chosen
above,

\[
\boxed{
t
\approx
0.8218196740254493
+
0.5681045145474256\,i
}
\]

and

\[
\boxed{
r
\approx
0.005318598861655839
+
0.04291149544920237\,i.
}
\]

Thus

\[
|t|
\approx
0.999064720546\ldots
\]

and

\[
|r|
\approx
0.04323984153\ldots.
\]

The overall phases depend on radial basis conventions; \(\mathcal T\) and
\(\mathcal R\) do not.

---

# 9. Why this is physical for the explicit BRST state

The radial channel is not being evaluated for an arbitrary scalar probe.

The quantum numbers inserted above are exactly those of the explicit
untwisted heterotic BRST physical state already constructed:

\[
j=\frac12+\frac i2,
\qquad
m=-2,
\qquad
\bar M=\frac{\sqrt{10}}2,
\]

\[
\ell=1,
\qquad
\bar N=-1.
\]

Its gauge constraints, BRST closure/non-exactness and heterotic mass-shell
completion were checked separately.

The spectator oscillator used to complete the heterotic physical state is
neutral under the Taub--NUT gauge group and factors out of the radial flux
ratio.

Thus the same BRST normalization multiplies the NUT in/out and horizon
branches and cancels in the probability ratio.

Accordingly,

\[
\boxed{
\mathcal T=0.998130316\ldots
}
\]

is the flux-normalized free one-string transmission coefficient associated
with that physical state.

---

# 10. Taub→NUT interpretation

There is one important causal qualification.

The NUT region \(x>1\) is stationary with \(t\) timelike, so the
NUT-infinity in/out basis has an ordinary scattering interpretation.

Inside the Taub region \(|x|<1\), however, \(x\) is timelike and \(t\) is
spacelike. Therefore the Taub side is not another static asymptotic
scattering exterior.

The exact coefficient above is most cleanly defined as the
**horizon↔NUT transmission coefficient**.

Because the radial differential operator has real coefficients, the
two-channel Wronskian problem is reciprocal:

\[
\boxed{
\mathcal T_{\rm H\to NUT}
=
\mathcal T_{\rm NUT\to H}.
}
\]

A future-directed Taub mode analytically continued through the regular
chronology horizon into the outgoing NUT channel inherits this same
barrier-transmission magnitude.

Therefore it is reasonable to use

\[
\boxed{
\mathcal T_{\rm Taub\to NUT}
\simeq
0.99813
}
\]

as shorthand for this free-string channel, provided one does not pretend
that the Taub side supplies a conventional asymptotic S-matrix state.

---

# 11. What this changes

Before this calculation:

\[
\text{explicit BRST state}
+
\text{nonzero hypergeometric connection}.
\]

Now:

\[
\boxed{
\text{explicit BRST state}
+
\text{flux-normalized unitary horizon↔NUT channel}
+
\mathcal T\simeq99.8\%.
}
\]

So the statement

\[
\text{“physical string propagation into the first NUT/CTC region is
suppressed by a horizon barrier”}
\]

is not supported for this explicit state.

At the free-string/minisuperspace level, the barrier is instead almost
transparent.

---

# 12. What remains before operational time travel

This is still not an interacting time-machine experiment.

The remaining gates are now:

1. promote the minisuperspace radial normalization to an exact coset
   two-point/reflection amplitude for the explicit vertex;
2. verify finite tree-level OPE/factorization involving this state;
3. test chronology-related pair production or condensate instabilities;
4. control finite-\(g_s\) backreaction;
5. define a relational BRST-invariant observable representing a completed
   return to the preparation event's causal past.

The first free-string transmission gate is now passed.

The next serious place where chronology protection can still appear is the
interaction/backreaction sector.

---

# 13. Status statement

For the explicit anomaly-free model point,

\[
\boxed{
\mathcal T_{\rm free}
=
0.998130316064\ldots
}
\]

for the chronology-relevant BRST physical state.

Therefore:

\[
\boxed{
\textbf{physical access to the first NUT/CTC region is strongly supported in
the free-string channel.}
}
\]

Operational past-directed time travel remains unproved because the
interaction, backreaction and relational-return gates remain open.
