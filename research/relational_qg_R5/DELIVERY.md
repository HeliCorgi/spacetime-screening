# R5 execution and delivery record

Date: 2026-10-02.
Intended repository: `HeliCorgi/spacetime-screening`.
Intended branch: `relational-qg-r5`.
Base read through the GitHub connector: `a0639dd49667a1dac9585aafa99df6408125c472`.
That `relational-qg-r3` head contains the merged R4 PR #36. The existing R1–R4
files are not altered by this additions-only package.

## Actually executed locally

- Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0.
- R5 forward, 55-digit arithmetic: success.
- R5 verifier without importing the forward code, 60-digit arithmetic: success.
- Positive mixture quadrature refined from 48 to 80 points per coordinate;
  maximum recorded kernel difference approximately 7.2e-24 for the tested rows.
  This is a refinement measurement, not a rigorous quadrature error certificate.
- Exact discriminant identities and 250 rational coefficient pairs checked
  independently by Sturm positive-root counts.
- Repeated-root and near-boundary kernels tested; no split-root approximation
  is used by the forward partial-fraction routine.
- Eight deliberately corrupted evidence files each rejected with exit code 1;
  none writes a successful output file. See `failure_controls.json`.
- Source/data SHA256 chain checked. `py_compile` succeeds for new Python files.
- The optional figures were rendered with NumPy 2.3.5 / Matplotlib in the local
  environment. Their sampled curves are illustrations, not extremal bounds.

The full repository suite, Lean, remote CI, nonlinear evolution, generic curved
constraint rank, quantum anomalies and Hadamard-state construction were NOT run
or certified by this package.

## Development corrections

The first forward run exposed a SymPy Boolean-to-integer summation error in
factor validation. It was corrected by explicit boolean conversion; scientific
thresholds were not changed.

An initial batch of corrupted-evidence tests exceeded the interactive execution
budget because every bad file first incurred all of the expensive mixture
integrals. Cheap independent evidence checks were moved before the unchanged
full verification. The valid evidence still runs the full positive-integral,
root and quadrature checks; invalid evidence is rejected earlier. The rerun of
all eight negative cases completed and is recorded. Timeout was not a pass.

## GitHub delivery status

**Not pushed. No remote commit, branch or PR was created in this turn.**
The available GitHub connector successfully reads the repository but exposes no
write/commit/ref action. Plugin discovery confirms the installed GitHub plugin,
but does not add a write action. Direct Git access was attempted twice and
failed with `Could not resolve host: github.com`; `gh` is not installed.
No credentials were requested or fabricated, and no unrelated service was used
as an upload relay.

The ZIP uses repository-relative paths. A binary-capable Git patch accompanies
it. The patch is additions-only, and can be applied on a branch based on the
recorded base SHA. Its local export commit is packaging provenance only, not a
remote repository commit.

Suggested application in an authenticated local checkout:

```bash
git fetch origin
git switch -c relational-qg-r5 a0639dd49667a1dac9585aafa99df6408125c472
git apply --check /path/to/relational_qg_R5.patch
git apply --index /path/to/relational_qg_R5.patch
git commit -m "R5: inverse-design coefficient domain and shared kernel predictions"
git push -u origin relational-qg-r5
```

Use a clean checkout; do not force-push or merge automatically. The repository's
existing CI policy may choose the full-Python fallback because research JSON
files are added. The new independently runnable assertions live directly under
`src/symbolic/`. No workflow, dependency pin, precision threshold, or assertion
is weakened. A selector modification is not part of this patch.
