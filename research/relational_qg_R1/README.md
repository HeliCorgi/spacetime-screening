# R1 prediction and self-revision workbook

Read `REPORT_JA.md` for the equations, changed assumptions, predictions, and scope.

Run with Python 3.13 (or a compatible environment):

```bash
python -m pip install -r requirements.txt
python compute_predictions.py
python independent_verify.py
python bound_states.py
```

`compute_predictions.py` reconstructs the original anchored 81-state control,
solves the tensor kinetic-coefficient gauge identity, counts physical
polarizations, checks the Fourier and lens integrals, and calculates the
revised model's entangling phase. `independent_verify.py` checks the phase root
with high-precision bisection and tests spatial lattice corrections without
importing the forward script. `bound_states.py` solves the revised two-body
radial Schrodinger problem at two grid spacings.

This is a defined weak-field model and a reproducible research calculation,
not a claimed complete quantum-gravity theory, experimental discovery, or
proof of generic singularity resolution. The revised model is not claimed to
emerge from the original graph Hamiltonian without new assumptions.

Numerical reproducibility is separate from physical model accuracy.
