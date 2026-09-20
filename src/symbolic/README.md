# Symbolic calculations

This directory contains reproducible SymPy checks for the static spherical ansatz

\[
ds^2=-f(r)dt^2+\frac{dr^2}{f(r)}+r^2d\Omega^2.
\]

## Run

From the repository root:

\`\`\`bash
python -m pip install -r requirements.txt
python src/symbolic/black_holes.py
\`\`\`

The script verifies:

- Schwarzschild:
  - \(R=0\)
  - \(R_{\mu\nu}R^{\mu\nu}=0\)
  - \(K=48G^2M^2/r^6\)

- Hayward:
  - exact \(R\), \(R_{\mu\nu}R^{\mu\nu}\), and Kretschmann scalar;
  - finite center limits;
  - Schwarzschild asymptotics;
  - horizon polynomial;
  - extremal radius and mass;
  - outer-horizon surface gravity and Hawking temperature;
  - maximum Hawking temperature.

All expected identities are encoded as symbolic assertions, so a failed algebraic check stops the script.
