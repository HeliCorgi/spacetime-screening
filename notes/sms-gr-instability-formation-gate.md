# Supermassive-Star GR-Instability Formation Gate

The Chon et al. heavy-seed simulation converts very massive stellar sink
particles into BH particles using a prescribed stellar lifetime.  The paper
explicitly notes that supermassive stars can instead collapse earlier through
the general-relativistic instability (GRI), and that the threshold depends on
the stellar accretion rate.

This creates a more direct formation test for Spacetime Screening than the
post-BH luminosity closure alone.

## 1. Published GR benchmark

Saio, Nandal, Ekström and Meynet (2024) solve the general-relativistic linear
adiabatic radial pulsation problem for rapidly accreting primordial
supermassive stars.

The star is unstable when the squared frequency of the fundamental radial
mode becomes negative,

\[
\omega_0^2<0.
\]

The critical mass is defined by

\[
\boxed{
\omega_0^2(M_{\rm crit},\dot M_*)=0.
}
\]

Their Table 1 gives:

| \(\dot M_*\,[M_\odot\,{\rm yr}^{-1}]\) | \(M_{\rm crit,GR}\,[M_\odot]\) |
|---:|---:|
| 0.05 | \(8.2\times10^4\) |
| 0.1 | \(1.06\times10^5\) |
| 1 | \(2.16\times10^5\) |
| 10 | \(4.56\times10^5\) |
| 100 | \(7.08\times10^5\) |
| 1000 | \(1.06\times10^6\) |

For their \(0.01M_\odot\,{\rm yr}^{-1}\) model no GRI is reached in the
computed evolution.

Umeda et al. (2016), using stellar evolution including GR effects, found the
same qualitative trend but somewhat different thresholds.  For example they
report roughly

\[
M_{\rm GRI}\simeq(2-3.5)\times10^5M_\odot
\]

for

\[
\dot M_*\simeq0.3-1M_\odot\,{\rm yr}^{-1},
\]

and approximately

\[
8\times10^5M_\odot
\]

for

\[
\dot M_*=10M_\odot\,{\rm yr}^{-1}.
\]

The difference between methods is useful: the GR benchmark itself has stellar
structure / stability-systematics and should not be treated as an exact
universal curve.

## 2. Connection to Chon et al.

The 2026 Nature simulation obtains very massive protostars of

\[
5-9\times10^5M_\odot,
\]

and explicitly states that stars above several \(10^5M_\odot\) can undergo
GR instability before the adopted \(2\) Myr stellar lifetime.

Thus the Nature heavy seeds lie directly in, or above, the published GRI
threshold range.

This means the first strong-gravity formation interface is actually

\[
\boxed{
\text{cosmological gas inflow}
\rightarrow
\text{accreting SMS}
\rightarrow
\text{radial GR instability}
\rightarrow
\text{compact-object seed}.
}
\]

## 3. Screening observable

Do not parameterize this as an ad hoc coordinate-dependent \(G_{\rm eff}(r)\).

The clean observable is the shift of the physical radial stability eigenvalue:

\[
\Delta\omega_0^2(M,\dot M_*).
\]

Equivalently define

\[
\boxed{
\Delta M_{\rm crit}(\dot M_*)
=
M_{\rm crit,screened}
-
M_{\rm crit,GR}.
}
\]

Near the GR critical point,

\[
\omega_{0,\rm GR}^2(M_0,\dot M_*)=0,
\]

the first-order root shift is

\[
\boxed{
\Delta M_{\rm crit}
=
-
\frac{
\Delta\omega_0^2(M_0,\dot M_*)
}{
\left.
\partial_M\omega_{0,\rm GR}^2
\right|_{M_0,\dot M_*}
}.
}
\]

This relation is purely a root-shift identity.  The hard physics is computing
\(\Delta\omega_0^2\) from a specific principal-safe screening theory.

## 4. Formation-gate questions

For a candidate screening theory ask:

1. Does a hydrostatic/accreting SMS equilibrium still exist up to the GR
   benchmark mass?
2. Is the radial pulsation problem well posed and ghost-free?
3. At what mass does its physical fundamental mode satisfy
   \[
   \omega_0^2=0?
   \]
4. Does screening delay collapse,
   \[
   \Delta M_{\rm crit}>0,
   \]
   accelerate it,
   \[
   \Delta M_{\rm crit}<0,
   \]
   or eliminate this instability channel?
5. If collapse begins, does the theory dynamically form the proposed
   screened compact object rather than a singular GR BH?

Only question 3 can be addressed by linear stability; question 5 requires a
nonlinear collapse calculation.

## 5. Why this matters observationally

Changing \(M_{\rm crit}\) changes:

- the seed mass;
- the time of BH formation;
- how long the new seed remains embedded in the dense gas reservoir;
- the duration of the initial super-Eddington phase;
- subsequent radiative feedback.

Chon et al. explicitly note that earlier GRI collapse would leave the BH in
dense gas longer and could extend rapid growth.

Thus

\[
\Delta M_{\rm crit}(\dot M_*)
\]

is a concrete bridge between strong-gravity physics and the cosmological
heavy-seed calculation.

## 6. Repository benchmark

Source values are stored in

\`data/sms_gri_gr_benchmark.csv\`.

The numerical helper

\`src/numerical/sms_gri_benchmark.py\`

performs a clearly labelled piecewise log-log interpolation inside the
published Saio et al. table.  It never extrapolates outside the source range.

The symbolic helper

\`src/symbolic/sms_gri_critical_mass_shift.py\`

checks the first-order root-shift formula.

No screening-induced shift is currently claimed.

## References

- H. Saio, D. Nandal, S. Ekström, G. Meynet,
  *Linear adiabatic analysis for general relativistic instability in
  primordial accreting supermassive stars*, arXiv:2406.18040 (2024).
- H. Umeda, T. Hosokawa, K. Omukai, N. Yoshida,
  *The Final Fates of Accreting Supermassive Stars*,
  ApJL **830**, L34 (2016), arXiv:1609.04457,
  DOI \`10.3847/2041-8205/830/2/L34\`.
- S. Chon et al.,
  *Overmassive black holes and little red dots naturally form in
  simulations*, Nature **657**, 621–625 (2026),
  DOI \`10.1038/s41586-026-10985-8\`.
