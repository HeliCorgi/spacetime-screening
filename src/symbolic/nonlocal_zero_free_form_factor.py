#!/usr/bin/env python3
"""Zero-free entire-form-factor toy benchmark.

This is NOT claimed to be the exact action of arXiv:2607.07790.
It encodes a standard design principle for ghost-free infinite-derivative
quadratic gravity:

    O(k^2) = k^2 * F(k^2/M_*^2)

with F(z) entire and zero-free.

A representative choice is
    F(z)=exp(z^N),  N positive integer,

so the propagator is
    Pi(k^2) ~ exp[-(k^2/M_*^2)^N] / k^2
in Euclidean-signature momentum magnitude.

The finite-plane pole set is then unchanged from GR: k^2=0 only.
"""

from __future__ import annotations

import sympy as sp


x,Mstar=sp.symbols("x M_*", positive=True, finite=True)
N=sp.symbols("N", integer=True, positive=True)


def form_factor(x_expr, n):
    z=x_expr/Mstar**2
    return sp.exp(z**n)


def main():
    # Work with concrete representative N=2 for symbolic derivatives.
    n=2
    F=sp.exp((x/Mstar**2)**n)
    operator=sp.factor(x*F)
    propagator=sp.exp(-(x/Mstar**2)**n)/x

    # Exponential is nonzero for every finite complex argument.
    # SymPy expresses this structurally rather than via solve().
    assert F.func == sp.exp

    # IR GR recovery.
    assert sp.limit(F,x,0)==1
    assert sp.limit(operator/x,x,0)==1

    # Residue factor at massless pole is finite/nonzero.
    residue_factor=sp.limit(x*propagator,x,0)
    assert residue_factor==1

    # Euclidean UV suppression.
    assert sp.limit(propagator,x,sp.oo)==0

    # Kinetic prefactor itself never vanishes for x>0.
    # d(log F)/dx is finite for finite positive x.
    log_slope=sp.factor(sp.diff(sp.log(F),x))
    expected=sp.factor(2*x/Mstar**4)
    assert sp.simplify(log_slope-expected)==0

    # Compare to a bad polynomial higher-derivative example:
    # O_bad = x (1 - x/m_g^2), which adds a second pole.
    mg=sp.symbols("m_g", positive=True, finite=True)
    z=sp.symbols("z", finite=True)
    O_bad=sp.factor(z*(1-z/mg**2))
    bad_roots=sp.solve(sp.Eq(O_bad,0),z)
    assert set(bad_roots)=={sp.Integer(0),mg**2}

    print("== Zero-free entire toy form factor ==")
    print(f"F(x) = {F}")
    print(f"O(x) = {operator}")
    print(f"Pi(x) = {propagator}")
    print()
    print("IR:")
    print(f"F(0) = {sp.limit(F,x,0)}")
    print(f"massless-pole residue factor = {residue_factor}")
    print()
    print("UV (Euclidean x -> +infinity):")
    print(f"Pi -> {sp.limit(propagator,x,sp.oo)}")
    print()
    print("No finite extra pole is introduced by exp(z^N),")
    print("because the exponential has no finite zeros.")
    print()
    print("== Contrast: polynomial higher-derivative toy ==")
    print(f"O_bad(x) = {O_bad}")
    print(f"zeros = {bad_roots}")
    print("The extra zero at x=m_g^2 creates an additional propagator pole.")
    print()
    print("This script is a design diagnostic, not a derivation of a")
    print("specific nonlocal-quasitopological action.")
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
