#!/usr/bin/env python3
"""First-order critical-mass shift from a modified radial stability eigenvalue.

Let the GR fundamental-mode eigenvalue be

    omega_GR^2(M, mdot),

with critical mass M0 defined by
    omega_GR^2(M0, mdot)=0.

Suppose a screened-gravity stellar calculation changes it by
    Delta omega^2(M, mdot).

At first order, the shifted root M0+Delta M satisfies

    Delta Mcrit
      = - Delta omega^2(M0)
        / [partial_M omega_GR^2]_(M0).

This script verifies the root-shift identity algebraically.  It does not
supply a model for Delta omega^2.
"""

from __future__ import annotations
import sympy as sp

M,M0,eps=sp.symbols("M M0 epsilon", real=True)
slope,domega=sp.symbols(
    "slope delta_omega2", nonzero=True, real=True
)
dM=sp.symbols("Delta_M", real=True)

# Local expansion of the GR eigenvalue near the critical mass.
omega_gr=slope*(M-M0)

# Small modified-gravity correction epsilon*domega.
omega_scr=omega_gr+eps*domega

# Solve the shifted zero.
root=sp.solve(sp.Eq(omega_scr,0),M)[0]
shift=sp.factor(root-M0)

assert sp.simplify(
    shift + eps*domega/slope
)==0

# Equivalent first-order condition evaluated at M=M0+Delta M.
linear_condition=sp.expand(
    omega_scr.subs(M,M0+dM)
)
solution_dM=sp.solve(sp.Eq(linear_condition,0),dM)[0]
assert sp.simplify(solution_dM-shift)==0

def main():
    print("== SMS critical-mass root shift ==")
    print(f"omega_GR^2 = {omega_gr}")
    print(f"omega_screened^2 = {omega_scr}")
    print(f"Mcrit_screened = {root}")
    print(f"Delta Mcrit = {shift}")
    print()
    print(
        "At first order: Delta Mcrit = "
        "-Delta omega0^2 / (d omega_GR^2/dM)|crit."
    )
    print()
    print(
        "A real screening prediction therefore requires the modified "
        "hydrostatic background and radial pulsation operator; changing "
        "G by hand is not sufficient."
    )
    print("All critical-mass-shift assertions passed.")


if __name__=="__main__":
    main()
