# R5 — constrained spatial-kernel design, not a full-gravity certification

Start with [the Japanese derivation](REPORT_JA.md).
The frozen class is `A(z)=1+z+b*z^2+c*z^3=prod(1+alpha_i*z)`,
three nonnegative factors summing to one, at least two strictly positive.
Its exact coefficient region, common weak-field predictions and explicit
boundary failures are distinguished from untested nonlinear/quantum conditions.

From the repository root (existing SymPy/mpmath dependencies):

```bash
python src/symbolic/relational_qg_r5_inverse_design.py --output /tmp/r5.json
python src/symbolic/relational_qg_r5_verify.py --evidence /tmp/r5.json --output /tmp/r5-verify.json
python src/symbolic/relational_qg_r5_inverse_design.py --b 31/100 --c 3/100
python src/symbolic/relational_qg_r5_inverse_design.py --alpha 1/2 3/10 1/5
python src/symbolic/relational_qg_r5_inverse_design.py --eta 1/20
```

The two primary scripts run independently without arguments and do not require
cross-shard generated files. Optional evidence verification additionally checks
source/data hashes. Coefficient arguments are exact rationals or finite decimal
strings; no approximate polynomial root determines class membership.

The independent verifier uses positive Fourier integrals and a positive
Gamma/Dirichlet mixture, not the forward script's signed partial fractions.
Its quadrature is refined separately from the arbitrary-precision arithmetic.

Run the explicit negative evidence controls with:

```bash
python research/relational_qg_R5/run_failure_controls.py
```

Optional figures (NumPy/Matplotlib are needed only for this rendering command):

```bash
python research/relational_qg_R5/plot_results.py
```

- [Allowed coefficient region](allowed_region.png)
- [Different phase zeros in the same family](phase_family.png)
- [Forward evidence](results.json)
- [Independent verification](verification.json)
- [Negative evidence controls](failure_controls.json)
- [Run and delivery status](DELIVERY.md)

The plots illustrate equations and selected members; they are not a numerical
proof of global extrema. The all-family claims are derived in the report.
Neither initial-data solutions nor the generally covariant quantum theory are
replaced or silently certified by these results.
