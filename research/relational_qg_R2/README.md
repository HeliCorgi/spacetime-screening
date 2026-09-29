# Relational quantum model R2

A conserving weak-field continuation of [R1](../relational_qg_R1/REPORT_JA.md).
No new fundamental parameter or replacement kernel is introduced. This is not
a claim of completed generally covariant quantum gravity.

[Derivations, corrections and limitations (Japanese)](REPORT_JA.md)

Run from the repository root with its existing SymPy/mpmath dependencies:

```bash
python src/symbolic/relational_qg_r2_dynamics.py --output /tmp/r2.json
python src/symbolic/relational_qg_r2_verify.py --evidence /tmp/r2.json --output /tmp/r2-verify.json
```

Both scripts also run standalone without output/evidence options, so CI shards
need not share intermediate artifacts.

[Forward source](../../src/symbolic/relational_qg_r2_dynamics.py) ·
[Independent verifier](../../src/symbolic/relational_qg_r2_verify.py) ·
[Forward evidence](results.json) · [Independent evidence](verification.json)

The original point-probe phase zero is conditional. A conserved-recoil example
moves it from 0.654976... to 0.734317... times ell. Circular orbital frequencies
are bounded in the retained Newtonian model and match its quantum core
oscillator scale. A conserved quadrupole pulse has a calculable, nonzero vacuum
dephasing. Spatial nonlocality and preferred-frame effects are quantified,
not relabeled as exact microcausality or general covariance.
