# Cosmological Heavy-Seed Formation as a Boundary Condition for Spacetime Screening

## Source

S. Chon, S. Hirano, T. Ishiyama, S.-J. Chang, V. Springel,

*Overmassive black holes and little red dots naturally form in simulations*,

Nature **657**, 621–625 (2026).

DOI: \`10.1038/s41586-026-10985-8\`

Preprint: arXiv:2601.04955.

The Nature paper publishes the AREPO simulation source package, runtime and
compile-time configuration, and initial conditions through Zenodo DOI
\`10.5281/zenodo.21242352\`.

## 1. What the simulation actually resolves

The simulation is extremely useful for this project, but it does **not**
resolve the black-hole interior or the singularity-resolution regime.

The calculation follows:

- cosmological halo assembly;
- primordial chemistry and radiative cooling;
- collapse of gas into protostellar sink particles;
- growth of supermassive stars;
- gas capture around the resulting massive BHs;
- radiation feedback;
- migration and galaxy assembly.

The highest-resolution BH-accretion calculation reaches spatial scales of
roughly

\[
500\ {\rm au}.
\]

The typical cosmological BH sink/accretion radius is approximately parsec
scale.

For a \(10^6M_\odot\) BH,

\[
r_s
=
\frac{2GM}{c^2}
\simeq
0.02\ {\rm au}.
\]

Therefore

\[
\frac{500\ {\rm au}}{r_s}
\sim
2.5\times10^4,
\]

and

\[
\frac{1\ {\rm pc}}{r_s}
\sim
10^7.
\]

The simulation never enters the horizon-scale region in which spacetime
screening would be expected to become important.

## 2. Where the simulation uses subgrid prescriptions

Several places are direct interfaces to a screened-BH model.

### A. Stellar collapse to a BH particle

The cosmological run converts a star into a BH particle when its adopted
stellar lifetime ends, provided its final mass exceeds \(260M_\odot\).

For the very massive stars relevant here, the authors use a fiducial lifetime
of \(2\) Myr.

The paper explicitly notes that general-relativistic instability may instead
cause supermassive stars of several \(10^5M_\odot\) to collapse earlier.

Thus the actual transition

\[
\text{supermassive star}
\longrightarrow
\text{compact object}
\]

is **not dynamically simulated in GR**.

It is a subgrid conversion.

This is the cleanest interface for the project's dynamical-formation gate.

### B. Inner accretion boundary

After BH formation, the sink radius is retained if it exceeds the ionized-gas
Bondi radius; otherwise the Bondi radius is used.

The typical radius is around a parsec in the cosmological calculation.

The higher-resolution accretion run uses \(500\) au and \(5000\) au sink
radii.

Gas crossing that unresolved inner boundary is incorporated into the BH
particle.

Thus the simulation directly resolves the external feeding environment, but
not the horizon/ISCO/core flow.

### C. Accretion luminosity

The emitted bolometric luminosity is prescribed by a slim-disk relation.

For low accretion rate,

\[
L_{\rm bol}
=
\epsilon_r\dot M_{\rm acc}c^2,
\qquad
\epsilon_r=0.1.
\]

For

\[
\dot M_{\rm acc}>2\dot M_{\rm Edd},
\]

the prescription becomes

\[
L_{\rm bol}
=
2
\left[
1+
\ln
\left(
\frac{\dot M_{\rm acc}}
{2\dot M_{\rm Edd}}
\right)
\right]
L_{\rm Edd}.
\]

The spectral shape is also prescribed as a broken power law.

Therefore any modification of:

- ISCO binding efficiency;
- photon capture;
- horizon/core boundary conditions;
- inner-disk radiative efficiency;
- super-Eddington photon trapping

would enter the cosmological simulation through this map rather than through
the resolved Bondi-scale flow.

### D. Kinetic feedback

Jets and disk winds are explicitly omitted.

The authors therefore describe the simulated BH growth as a fiducial upper
limit under the assumption that kinetic feedback is absent.

This is another place where a microscopic screened-BH/accretion model could
change the cosmological result.

### E. BH mergers

BH particles are merged once their separation is below \(10\) physical pc.

The actual binary inspiral and strong-field merger are unresolved.

This makes merger dynamics another possible future interface, although it is
less immediately useful than the collapse/accretion boundary.

## 3. Why the external gas dynamics are almost model-independent

For the analytic-GQTG-compatible branch currently being explored in this
repository,

\[
f(r)
=
1-\frac{2M}{r}
+O(r^{-6}).
\]

For the cubic term,

\[
\delta f_3
\sim
-\frac{27}{4}
\frac{\ell^4M^2}{r^6}.
\]

Relative to the Schwarzschild potential,

\[
\frac{|\delta f_3|}
{2M/r}
\sim
\frac{27}{8}
\left(
\frac{\ell}{r}
\right)^4
\frac{M}{r}.
\]

For a \(10^6M_\odot\) seed at \(r=500\) au, even taking the very large choice

\[
\ell\sim M,
\]

this correction is of order

\[
10^{-23}.
\]

Thus a horizon-scale or microscopic screening model will not materially alter
the gas dynamics at the published simulation's resolved inner boundary.

This is useful rather than disappointing:

\[
\boxed{
\text{cosmological formation}
\quad\text{and}\quad
\text{strong-field screening}
}
\]

can be separated to very high accuracy.

## 4. Proposed simulation interface

The Chon et al. calculation can be treated as a realistic **outer-boundary
generator** for a screened-BH collapse/accretion model.

The minimum interface is:

### Inputs supplied by the cosmological simulation

\[
\boxed{
M(t),\quad
\dot M(t),\quad
\rho_{\rm in}(t),\quad
T_{\rm in}(t),\quad
j_{\rm in}(t)
}
\]

at the sink/Bondi boundary, plus the external radiation and merger history.

### Outputs supplied by the screened-BH model

\[
\boxed{
M_{\rm grav}(t),\quad
L_{\rm bol}(t),\quad
{\rm SED}(t),\quad
\epsilon_{\rm rad}(t)
}
\]

and, eventually,

\[
\dot M_{\rm wind},
\qquad
\dot p_{\rm jet},
\qquad
\dot E_{\rm kinetic}.
\]

The outer AREPO calculation need not know the microscopic core metric if these
effective boundary data are supplied.

## 5. First useful experiment

A full modification of AREPO is not yet necessary.

The first controlled experiment is offline:

1. extract a published heavy-seed accretion history
   \[
   M(t),\dot M(t);
   \]

2. feed it into a screened-BH inner model;

3. replace the fixed
   \[
   \epsilon_r=0.1
   \]
   slim-disk luminosity map by the screened-model luminosity map;

4. compare the resulting ionizing luminosity and growth history.

This directly asks whether the strong-field completion could alter the
feedback loop responsible for the short super-Eddington phase.

## 6. What this paper can and cannot test

### It can test

- whether nature provides the required heavy-seed initial masses;
- realistic mass-loading histories;
- whether the screened object can survive extreme super-Eddington feeding;
- whether modified inner-disk efficiency feeds back onto the cosmological
  growth path;
- whether the model remains compatible with LRD-like observables.

### It cannot directly test

- singularity resolution;
- the core principal operator;
- horizon-scale characteristic structure;
- the physical ghost tests developed elsewhere in this repository.

Those remain strong-field calculations.

## 7. Research significance for this repository

This paper supplies something the project previously lacked:

\[
\boxed{
\text{a realistic dynamical external environment for a }10^6M_\odot
\text{ seed}
}
\]

rather than another idealized static metric.

Therefore it is a strong benchmark for the project's **dynamical formation**
criterion, provided the distinction is kept clear:

\[
\text{AREPO}
\to
\text{outer collapse/accretion boundary conditions},
\]

\[
\text{Spacetime Screening}
\to
\text{unresolved strong-field interior and feedback closure}.
\]

## Reproducibility

Run

\`\`\`bash
python src/symbolic/heavy_seed_scale_separation.py
\`\`\`

to reproduce the scale-separation estimates.


## 8. Source-constrained envelope instead of fake precision

The Nature data-availability statement distinguishes between:

- public simulation **inputs/configuration/initial conditions** at Zenodo;
- full simulation **outputs**, available from the corresponding author on
  reasonable request.

Accordingly, this repository does **not** label hand-read values from Fig. 1
as exact simulation data.

Instead, \`data/heavy_seed_source_envelope.csv\` records only numerical anchors
and phase descriptions explicitly stated in the paper.

Important example: the paper contains two MBH1 mass statements in different
simulation contexts:

- the high-resolution isolated-cloud follow-up describes an MBH1 seed with
  final mass \(6\times10^5M_\odot\);
- a later characteristic-mass discussion associates approximately
  \(3\times10^5M_\odot\) and \(6\times10^5M_\odot\) with MBH1 and MBH2.

The repository preserves those contexts separately rather than silently
reconciling them.

For prose such as

> several to a few tens of times the Eddington limit,

the numerical interval used by the harness,

\[
3\le \dot m\le30,
\]

is explicitly marked as an **operational interpretation**, not source data.

## 9. Offline inner-boundary harness

The first coupling code is

\`src/numerical/heavy_seed_boundary_harness.py\`.

It implements the paper's Eq. (4) in dimensionless form,

\[
\frac{L_{\rm bol}}{L_{\rm Edd}}
=
\begin{cases}
\dot m,&\dot m\le2,\\[1mm]
2\left[1+\ln(\dot m/2)\right],&\dot m>2,
\end{cases}
\]

and exposes the inner closure as a replaceable callable.

The baseline is the Chon et al. slim-disk prescription.

A second, deliberately phenomenological closure is included only as an
interface test; it rescales luminosity and can attach wind/kinetic-feedback
fractions. It is **not** presented as a prediction of Spacetime Screening.

This cleanly separates:

\[
\boxed{
\text{source-derived outer history}
}
\]

from

\[
\boxed{
\text{future strong-field closure}.
}
\]

## 10. Next data step

For a quantitative feedback rerun, replace the source-constrained envelope
with one of:

1. author-supplied full \(M(t),\dot M(t)\) outputs;
2. a documented digitization of Fig. 1e/f;
3. a rerun of the archived AREPO setup.

The harness API is already designed so the data source can be replaced without
changing the strong-field closure interface.


## 11. Radiation-feedback adapter

The paper also supplies a concrete baseline SED for accreting BHs:

\[
F_\nu\propto\nu^{-0.6},
\qquad
1{\rm\,eV}<h\nu<10{\rm\,eV},
\]

and

\[
F_\nu\propto\nu^{-1.5},
\qquad
10{\rm\,eV}<h\nu<1{\rm\,keV}.
\]

The source specifies the slopes and intervals but does not explicitly state
the relative normalization of the two branches in the quoted Methods text.

For the repository's interface adapter we therefore make one transparent
additional assumption:

\[
\boxed{
F_\nu\ \text{is continuous at }10{\rm\,eV}.
}
\]

Under that convention,

\[
\frac{B}{A}=10^{0.9}
\]

for the high-energy and low-energy amplitudes.

The resulting baseline has approximately

\[
\boxed{
\frac{L_{E>13.6{\rm eV}}}{L_{\rm bol}}
\simeq0.4584
}
\]

and mean hydrogen-ionizing photon energy

\[
\boxed{
\langle E\rangle_{\rm ion}
\simeq36.10{\rm\,eV}.
}
\]

Thus

\[
Q_H
\simeq
7.93\times10^{9}
\left(
\frac{L_{\rm bol}}{{\rm erg\,s^{-1}}}
\right)
{\rm s^{-1}}.
\]

For example,

\[
L_{\rm bol}=10^{44}{\rm\,erg\,s^{-1}}
\]

corresponds to

\[
Q_H\simeq7.9\times10^{53}{\rm\,s^{-1}}.
\]

This is implemented in

\`src/numerical/heavy_seed_sed_adapter.py\`.

The point is not to assume that a screened object has the same SED.  It gives
a baseline map

\[
L_{\rm bol}
\longrightarrow
Q_H
\]

that can be replaced once the strong-field inner accretion spectrum is
derived.
