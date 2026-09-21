# GR-to-Screened Matching Scale for SMS Collapse

The heavy-seed formation problem naturally separates into a weak/post-
Newtonian GRI stage and a later strong-field collapse stage.

This note defines a model-independent matching parameter for the second stage.

## 1. Curvature-scale variable

Use the Schwarzschild exterior Kretschmann scalar as a diagnostic scale,

\[
K(r)=\frac{48M_{\rm geo}^2}{r^6}.
\]

At the Schwarzschild radius,

\[
r_s=2M_{\rm geo},
\]

\[
K_h=\frac{3}{4M_{\rm geo}^4}.
\]

Therefore

\[
\boxed{
\frac{K(r)}{K_h}
=
\left(\frac{r_s}{r}\right)^6
=
\mathcal C^6,
}
\]

where

\[
\mathcal C=\frac{r_s}{r}.
\]

This does not assert that the stellar interior is Schwarzschild.  It is a
dimensionless scale diagnostic for deciding when a high-curvature completion
must replace a GR calculation.

## 2. Activation parameter

Define

\[
\eta_{\rm act}
=
\frac{K_{\rm act}}{K_h}.
\]

Then

\[
\boxed{
\frac{r_{\rm act}}{r_s}
=
\eta_{\rm act}^{-1/6}.
}
\]

Examples:

\[
\eta_{\rm act}=10^{-6}
\Rightarrow
r_{\rm act}=10r_s,
\]

\[
\eta_{\rm act}=10^{-12}
\Rightarrow
r_{\rm act}=100r_s,
\]

and

\[
\eta_{\rm act}=10^{-24}
\Rightarrow
r_{\rm act}=10^4r_s.
\]

## 3. Separation from GRI onset

The Saio et al. GRI models have

\[
\mathcal C_{\rm GRI}
\simeq
1.1\times10^{-5}
-
1.7\times10^{-4}.
\]

Thus

\[
\frac{R_{\rm GRI}}{r_s}
\simeq
6\times10^3
-
9\times10^4.
\]

For the \(1M_\odot/{\rm yr}\) model,

\[
\mathcal C_{\rm GRI}=2.9\times10^{-5},
\]

so

\[
\boxed{
\eta_{\rm GRI}
=
\mathcal C_{\rm GRI}^6
\simeq5.9\times10^{-28}.
}
\]

This makes the hierarchy explicit:

\[
\boxed{
\text{GRI onset}
\ll
\text{near-horizon curvature}.
}
\]

## 4. Numerical strategy

A future collapse calculation can therefore be organized as:

1. evolve the stellar structure and early collapse with GR while
   \[
   K/K_h\ll\eta_{\rm act};
   \]
2. enter an overlap region before the candidate correction is large;
3. switch or couple to the screened-gravity evolution;
4. verify constraint matching and convergence with respect to the chosen
   overlap radius.

The matching parameter \(\eta_{\rm act}\) should ultimately be derived from
the actual covariant action, not chosen phenomenologically.

## 5. What to measure

For a GR-collapse benchmark, compare:

\[
t_{\rm AH}^{\rm GR},
\qquad
M_{\rm BH}^{\rm GR},
\qquad
M_{\rm eject}^{\rm GR}
\]

against the screened evolution.

If no apparent horizon forms, replace the BH quantities by:

\[
M_{\rm core},
\qquad
R_{\rm min},
\qquad
K_{\rm max},
\qquad
E_{\rm eject}.
\]

The formation question then becomes operational:

\[
\boxed{
\text{Does the high-curvature completion change the endpoint after a
GR-like GRI onset?}
}
\]

## Reproducibility

Run

\`src/numerical/sms_screening_activation_scale.py\`.
