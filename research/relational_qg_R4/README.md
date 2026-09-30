# R4_2: nonlinear spherical initial-data solver

[日本語の作用・計算・限界](REPORT_JA.md)

R4 repairs nonuniform-lapse kinetic ordering by S N S and keeps the m=2
spatial curvature action. It provides time-symmetric spherical initial data
and the constraint-preserving lapse. It is not a full evolution program or a
proved generally covariant quantum-gravity theory.

From repository root:

```bash
python -m pip install -r requirements.txt
python src/symbolic/relational_qg_r4_ordering.py
python src/numerical/relational_qg_r4_initial_data.py --epsilon 1 --output /tmp/r4.json
python src/symbolic/relational_qg_r4_verify.py --evidence /tmp/r4.json
```

The default numerical run compares two resolutions for epsilon=0.01,0.1,0.5,1,2,4
at coordinate sigma=ell. `--profiles /tmp/profiles.json` also exports all
finest-grid coefficients. No output files are written unless requested.

Without `--evidence`, the verifier reads this directory's committed
[results](results.json), not output shared by another CI shard.
[Independent checks](verification.json), [exact ordering checks](ordering.json),
and [failure controls](failure_controls.json) are stored separately.

Boundary, strong residual, lapse, and refinement checks abort on failure.
A successful solve certifies only the implemented numerical tests, not global
existence, nonspherical stability, or a nonsingular future spacetime.
