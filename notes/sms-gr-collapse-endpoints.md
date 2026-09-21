# GR Endpoint Benchmarks for Nonlinear SMS Collapse

Once a supermassive star actually enters a GR-collapse branch, the
Spacetime-Screening formation test needs concrete endpoint observables.

Two complementary GR benchmarks are useful.

## 1. Uniformly rotating mass-shedding benchmark

Shibata & Shapiro (2002) performed axisymmetric fully relativistic
simulations of a uniformly rotating SMS at the onset of radial collapse.

Their collapse forms an apparent horizon and leads approximately to

\[
\boxed{
\frac{M_{\rm BH}}{M}\simeq0.9,
}
\]

\[
\boxed{
\frac{J_{\rm BH}}{M_{\rm BH}^2}\simeq0.75,
}
\]

with roughly

\[
\boxed{
\frac{M_{\rm disk}}{M}\simeq0.1.
}
\]

This is an idealized mass-shedding configuration, not a direct model of the
Chon et al. protostars.

Its value here is as a clean strong-field rotating-GR benchmark.

## 2. Rotating SMS-core benchmark with nuclear physics

Fujibayashi et al. (2025) perform GR hydrodynamics for rotating supermassive
stellar cores with a detailed equation of state and approximate nuclear
burning.

In the models they study:

- a BH forms;
- rotation produces a torus;
- shock heating associated with the torus drives an explosion/outflow;
- the ejecta mass saturates at approximately
  \[
  M_{\rm eject}\sim10^{-2}M;
  \]
- characteristic ejecta velocity saturates around
  \[
  v_{\rm eject}\sim0.2c;
  \]
- explosion energy reaches approximately
  \[
  E_{\rm exp}\sim10^{-4}Mc^2
  \sim10^{55}-10^{56}\ {\rm erg}
  \]
  for their SMS-core masses.

This gives a more modern endpoint benchmark for rotating collapse.

## 3. Relation to the accreting-SMS fate problem

These rotating-collapse calculations should not be confused with the
Nagele–Umeda constant-accretion result.

Nagele & Umeda show that some accreting SMSs never reach a BH-collapse branch
because nuclear burning produces a pulsation or explosion first.

Thus the full logic is:

\[
\boxed{
\text{GRI}
\to
\begin{cases}
\text{pulsation/explosion},\\
\text{strong-field collapse}.
\end{cases}
}
\]

Only the second branch should be compared against the rotating BH endpoint
benchmarks.

## 4. Screened-collapse comparison vector

For any candidate principal-safe screening theory, measure

\[
\boxed{
\left\{
t_{\rm AH},
\frac{M_{\rm AH}}{M},
a_{\rm rem},
\frac{M_{\rm disk}}M,
\frac{M_{\rm eject}}M,
\frac{E_{\rm eject}}{Mc^2}
\right\}.
}
\]

If no apparent horizon forms, use instead

\[
\boxed{
\left\{
R_{\rm min},
K_{\rm max},
\frac{M_{\rm core}}M,
\frac{M_{\rm eject}}M,
\frac{E_{\rm eject}}{Mc^2}
\right\}.
}
\]

These quantities provide a direct GR-versus-screened comparison without
requiring the exterior cosmological simulation to resolve the central
strong-field region.

## 5. Immediate use

The first nonlinear Spacetime-Screening collapse calculation should not try to
reproduce the whole cosmological simulation.

It should take a GR-collapse SMS configuration as initial data near the
strong-field matching surface and ask:

1. does an apparent horizon form?
2. does curvature remain bounded?
3. does the physical principal operator remain hyperbolic?
4. what fraction of the mass becomes a compact remnant/disk/ejecta?
5. is the result continuous as the matching surface is moved outward?

## References

- M. Shibata, S. L. Shapiro,
  *Collapse of a Rotating Supermassive Star to a Supermassive Black Hole:
  Fully Relativistic Simulations*,
  ApJL **572**, L39–L43 (2002),
  DOI \`10.1086/341516\`, arXiv:astro-ph/0205091.
- S. L. Shapiro, M. Shibata,
  ApJ **577**, 904–908 (2002),
  DOI \`10.1086/342246\`.
- S. Fujibayashi et al.,
  *Powerful Explosions from the Collapse of Rotating Supermassive Stars*,
  ApJ **981**, 119 (2025),
  DOI \`10.3847/1538-4357/adb0b8\`,
  arXiv:2408.11572.
