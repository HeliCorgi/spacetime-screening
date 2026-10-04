# B1 — auxiliary-volume bounce candidate (separate from the R series)

**NEW CALCULATION CANDIDATE.** This is a specified potential within the existing
VCDM / type-II minimally modified gravity framework, not a from-scratch
quantum-gravity theory and not a revival of the rejected R4 cosmology claim.
R1–R5 files, branches and conclusions are not changed by this import.

The chosen potential is `V(phi)=(phi^2-mu^2 cos^2(phi/mu))/3`, with `mu>0`.
Read [REPORT_JA.md](REPORT_JA.md) for the action, conventions, derivations,
primary-source attribution and limitations. In particular, the general Dirac
analysis and reduced scalar perturbation coefficients are taken from the cited
literature; the scripts do not independently rederive those general results.

## Included checks and limits

The supplied code checks the homogeneous action reduction, positive-density
dust/stiff backgrounds, an exact homogeneous anisotropic stiff family, and the
signs of the published scalar quadratic coefficients after substitution of the
chosen isotropic stiff background. The second script independently contracts
the four-dimensional Christoffel/Riemann tensors for the isotropic geometry.
It is not an independent rederivation of every forward calculation.

The homogeneous completeness arguments are in the report. No general nonlinear
inhomogeneous stability, cubic strong-coupling control, full quantum Hadamard
state, loop analysis, cosmological/PPN fit, metric microcausality, or generic
singularity resolution is certified. Positive quadratic coefficients alone do
not establish those properties. The preferred foliation and the undetermined
scale mu remain explicit. R-series spatial filters are not added to this action.

## Run from the repository root

The existing repository SymPy dependency is sufficient. No CI dependency or
workflow is changed.

```bash
python src/symbolic/auxiliary_volume_b1_checks.py --output /tmp/b1-rerun.json
python src/symbolic/auxiliary_volume_b1_verify.py
```

Both CI entry points use explicit imports of the preserved scripts below. The
checks entry point needs no generated input; without arguments it prints JSON.
The geometry verifier reads the **committed** results.json and the adjacent
check_candidate.py, validates the source hash and scope flags, and writes
verification.json in this directory. It does not depend on another CI shard's
output. For an independent local regeneration of the archived pair, run:

```bash
cd research/auxiliary_volume_B1
python check_candidate.py --output results.json
python verify_geometry.py
```

The tracked JSON/log files are archived evidence, not a substitute for executing
the checks. A different Python environment can change metadata and file hashes.
Use [SHA256SUMS.txt](SHA256SUMS.txt) to verify the supplied original files.

## Import provenance and verification

Source attachment: `auxiliary_volume_B1_checks.zip`.
Archive SHA256: `87a58a0d60e44b8948da25acef7efa0414166d39288b10f07c2d30eb43a42b03`.
All eight original archive members are stored here byte-for-byte, including the
original report, scripts, results, logs, dependency declaration and checksums.
The original report's statement that GitHub was not changed describes the
calculation before this import, not the delivery status of this PR.

This separate branch is based on main commit
`e4b78b1f64b132d8d85d55393bd7f93a216097e1`; it does not depend on unmerged R PRs.

Actually rerun for this import: Python 3.13.5 / SymPy 1.14.0, both entry points,
py_compile of the entry points and source modules, archived checksums, and a
comparison of the rerun forward JSON against the archived result. All passed;
no scientific equation, assertion, tolerance or original file was changed.
This is targeted local validation, not a full repository or Lean run.

The repository selector may select the existing full-Python fallback because
shared research modules and committed evidence are added. No duplicate manual
multi-version workflow is requested. The latest remote CI status belongs to the
PR/check run; no remote success is asserted by this archival README. The PR is
for review only and is not merged automatically.

## Files

- [Forward action and coefficient checks](check_candidate.py)
- [Independent isotropic curvature check](verify_geometry.py)
- [Original forward evidence](results.json)
- [Original geometry evidence](verification.json)
- [Original execution log](run.log)
