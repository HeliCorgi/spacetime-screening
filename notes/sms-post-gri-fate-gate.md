# Post-GRI Fate Gate: Collapse Is Not Automatically Black-Hole Formation

The Chon et al. cosmological simulation treats stellar-to-BH conversion as a
subgrid operation.  It notes that a supermassive star may encounter the
general-relativistic instability (GRI) before the adopted stellar lifetime.

A second piece of literature is essential here:

C. Nagele & H. Umeda,
*The formation of black holes from rapidly accreting supermassive stars is
not trivial: Simulations of thermonuclear pulsations and explosions*,
Phys. Rev. D **110**, L061301 (2024), arXiv:2408.08352.

They evolve unstable accreting SMS models with a one-dimensional general-
relativistic hydrodynamics code including a nuclear network.

## 1. GRI onset is not the same as BH formation

For their Pop III models, the source Table I gives:

| \(\dot M_*\,[M_\odot/{\rm yr}]\) | \(M_{\rm GRI}[M_\odot]\) | outcome |
|---:|---:|---|
| 0.1 | \(5.325\times10^4\) | collapse |
| 1 | \(9.356\times10^4\) | pulsation |
| 10 | \(1.418\times10^5\) | pulsation |
| 50 | \(2.138\times10^5\) | pulsation |
| 90 | \(2.648\times10^5\) | collapse |
| 100 | \(2.742\times10^5\) | collapse |
| 200 | \(1.846\times10^5\) | pulsation |

The dependence is not monotonic.

In particular,

\[
\boxed{
\dot M_*=1M_\odot/{\rm yr}
\quad\Rightarrow\quad
\text{pulsation, not immediate BH formation}
}
\]

for this published model.

The authors attribute the survival of many unstable stars to nuclear burning
during the comparatively long collapse, of order \(10^6\) s.

## 2. Revised cosmological formation closure

A realistic heavy-seed interface therefore has at least two stages:

\[
\boxed{
\dot M_*(t),\ \text{stellar structure}
\longrightarrow
\omega_0^2=0
}
\]

for the onset of GRI, followed by

\[
\boxed{
\text{unstable SMS}
\longrightarrow
\{\text{BH collapse},\text{pulsation},\text{explosion}\}.
}
\]

The second map depends on:

- core-to-total mass ratio;
- composition/metallicity;
- temperature history;
- nuclear reaction network;
- accretion history;
- relativistic collapse dynamics.

Therefore the repository should not implement

\[
\text{GRI}
\Rightarrow
\text{BH particle}
\]

as an exact physical rule.

## 3. Relevance to Spacetime Screening

This sharpens the screening test.

The GRI itself begins at very small compactness, so a genuinely
high-curvature screening model should leave the onset approximately GR-like.

The more direct competition occurs **during post-GRI collapse**.

A screening mechanism that changes the collapse rate or prevents the
formation of a trapped region can alter the time available for nuclear
burning.

Schematically,

\[
\boxed{
t_{\rm collapse}
\quad\text{vs}\quad
t_{\rm nuc}
}
\]

becomes an important interface variable.

Possible qualitative effects include:

- delayed collapse \(\rightarrow\) more nuclear burning and a larger chance
  of pulsation/explosion;
- faster effective collapse \(\rightarrow\) less time for burning and a
  larger chance of compact-object formation;
- a bounce/screened core \(\rightarrow\) a new fate not present in the GR
  outcome table.

These are **research possibilities**, not predictions.

## 4. New formation-gate observable

The SMS formation benchmark should therefore track two separate quantities:

\[
\boxed{
\Delta M_{\rm crit}(\dot M_*)
}
\]

for the shift of GRI onset, and

\[
\boxed{
\Delta t_{\rm collapse},
\quad
\Delta E_{\rm nuc},
\quad
\Delta M_{\rm eject}
}
\]

for the nonlinear fate after instability.

For a high-curvature-only screening theory, the expectation is that
\(\Delta M_{\rm crit}\) is small while the post-GRI collapse observables are
the more sensitive test.

## 5. Connection to the Nature heavy-seed simulation

Chon et al. report protostellar accretion around the
\(M_\odot/{\rm yr}\) scale in the relevant rapidly growing objects and form
stars of \(5-9\times10^5M_\odot\).

Their adopted star-to-BH conversion therefore bypasses a regime in which
published GR hydrodynamic calculations show that the immediate fate can be
nontrivial.

This does **not** invalidate the Nature simulation.  The authors explicitly
identify stellar lifetime/GRI as an uncertainty.

For this repository it means the cosmological coupling should eventually
replace the conversion rule by

\[
\boxed{
\text{stellar evolution}
+
\text{GR/screened collapse fate solver}.
}
\]

## 6. Reproducibility

The exact Pop III rows used here are stored in

\`data/sms_post_gri_fates.csv\`.

Run

\`src/numerical/sms_post_gri_fate_benchmark.py\`

to verify the source outcome map.

No interpolation of the fate labels is performed.

## References

- C. Nagele, H. Umeda,
  Phys. Rev. D **110**, L061301 (2024),
  DOI \`10.1103/PhysRevD.110.L061301\`,
  arXiv:2408.08352.
- S. Chon et al.,
  Nature **657**, 621–625 (2026),
  DOI \`10.1038/s41586-026-10985-8\`.
