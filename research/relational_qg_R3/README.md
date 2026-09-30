# Relational QG R3

A specified nonlinear, preferred-foliation Hamiltonian candidate, not a completed quantum-gravity theory. Read [REPORT_JA.md](REPORT_JA.md) for the exact action, new assumptions, calculated results, and failed/open gates.

Executable checks:

```bash
python src/symbolic/relational_qg_r3_constraints.py --output /tmp/r3.json
python src/symbolic/relational_qg_r3_verify.py --evidence /tmp/r3.json --output /tmp/r3-verify.json
python src/symbolic/relational_qg_r3_selfsource.py --output /tmp/r3-selfsource.json
```

Run these commands from the repository root. Only the existing SymPy and mpmath dependencies are needed.

Two tensor modes are counted on the regular second-class constraint branch. The flat mixed constraint symbol is elliptic; no global nonlinear well-posedness theorem is claimed. The finite polynomial kernel is a declared change from R2's exact Gaussian, not a hidden regulator-independent prediction.

The direct nonlinear initial-constraint expansion agrees with the pair-potential binding mass at second order. This is not a complete nonlinear time evolution or a singularity-resolution proof.
