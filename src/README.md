# Source code

This directory is reserved for reproducible symbolic and numerical work.

Planned structure:

- `symbolic/` — curvature invariants, series expansions, field equations.
- `collapse/` — spherical-collapse experiments.
- `stability/` — perturbation and mode analysis.
- `thermo/` — horizon structure and thermodynamics.
- `tests/` — regression tests for analytical limits.

Code in this directory is licensed under Apache-2.0.

The first implementation target is a small symbolic script that reproduces the
Schwarzschild and Hayward curvature invariants and verifies the regular-center
series expansions recorded in `notes/derivations.md`.
