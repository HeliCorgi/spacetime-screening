# SMS Formation-Systematics Layer

The Chon et al. heavy-seed simulation provides a cosmological accretion
environment, but the mapping from that environment to a BH seed remains
astrophysically uncertain even within GR.

This note records the hierarchy of benchmarks rather than collapsing them
into one artificial threshold curve.

## 1. Constant-rate linear-stability benchmark

Saio et al. (2024) solve the relativistic radial pulsation eigenproblem and
provide

\[
M_{\rm crit,GR}(\dot M_*)
\]

for constant accretion rates.

This is the cleanest benchmark for the onset of GRI, but it is not a
cosmological stellar-evolution calculation.

## 2. Constant-rate nonlinear fate benchmark

Nagele & Umeda (2024) continue unstable constant-accretion models with 1D GR
hydrodynamics and nuclear reactions.

They show that the post-GRI fate is non-monotonic in \(\dot M_*\): collapse,
thermonuclear pulsation and explosion are all possible.

Thus even for constant accretion,

\[
M_{\rm crit}
\]

does not determine the remnant.

## 3. Variable cosmological histories

Woods et al. (2021) evolve SMSs using highly variable accretion histories
taken from cosmological flows.

Their models reach roughly

\[
1-2\times10^5M_\odot
\]

before direct collapse during or near the end of main-sequence hydrogen
burning, at ages around

\[
1-1.5\ {\rm Myr}.
\]

They also find substantially more structural diversity than in
constant-accretion models.

Therefore a variable history

\[
\dot M_*(t)
\]

cannot in general be replaced by a single time-averaged accretion rate without
losing information about:

- entropy profile;
- core-to-total mass ratio;
- thermal relaxation;
- burning stage;
- radiative feedback;
- post-GRI fate.

## 4. Repository policy

The formation interface therefore uses the following rule.

### Constant \(\dot M_*\)

It may use:

- Saio et al. interpolation for \(M_{\rm crit,GR}\);
- exact Nagele & Umeda fate labels only at tabulated source rates.

### Variable \(\dot M_*(t)\)

It returns no inferred fate.

A genuine stellar-evolution + relativistic-stability solver is required.

This is implemented in

\`src/numerical/sms_formation_interface.py\`.

The code deliberately raises an error rather than computing an
"effective-\(\dot M\)" fate.

## 5. Consequence for Chon et al.

The Nature calculation can eventually provide the correct outer history, but
the project should pass that history to a stellar-evolution layer before
creating a compact-object particle.

The full formation chain is therefore

\[
\boxed{
\text{AREPO gas flow}
\to
\dot M_*(t)
\to
\text{SMS evolution}
\to
\text{GRI}
\to
\text{nonlinear fate}
\to
\text{screened/BH inner object}.
}
\]

This is more elaborate than the current subgrid conversion, but it identifies
precisely where strong-gravity physics belongs.

## References

- T. E. Woods et al.,
  *On the Evolution of Supermassive Primordial Stars in Cosmological Flows*,
  ApJ **915**, 110 (2021), DOI \`10.3847/1538-4357/abfaf9\`,
  arXiv:2102.08963.
- H. Saio et al.,
  A&A **689**, A169 (2024), DOI \`10.1051/0004-6361/202449971\`.
- C. Nagele & H. Umeda,
  Phys. Rev. D **110**, L061301 (2024),
  DOI \`10.1103/PhysRevD.110.L061301\`.
