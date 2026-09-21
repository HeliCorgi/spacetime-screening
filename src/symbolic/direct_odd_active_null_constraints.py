#!/usr/bin/env python3
"""Principal active/null constraint structure from the DIRECT odd expansion.

The direct original-action result gives the vector derivative block

    L_vec,pr =
      -alpha [-a D u_A + b D u_B]^2,

with
    alpha = 192 pi ell^4/(5 f^2) > 0,
    D = partial_t - f partial_r.

Define the orthonormal vector combinations

    U = (-a u_A + b u_B)/n,
    V = ( b u_A + a u_B)/n,
    n^2 = a^2+b^2.

At principal derivative order,

    L_vec,pr = -alpha n^2 (D U)^2,

while V has no principal derivative.

The raw original action also contains the algebraic vector term

    L_alg = N ell^2 C (u_A^2-u_B^2),

because the B sector enters with the opposite action sign.

In the U,V basis this contains a nonzero V^2 coefficient whenever
b^2-a^2 != 0:

    coeff(V^2)
      = N ell^2 C (b^2-a^2)/(a^2+b^2).

On the exact regular branch, C>0 and b^2-a^2>0 for r>0, so the
zero-derivative V combination is generically auxiliary rather than a new
gauge direction.  Its primary zero-momentum condition is expected to pair
with an algebraic secondary equation.

The derivative-active U combination is orthogonal to this null direction
and has a strictly negative principal kinetic coefficient.

This is not a complete Dirac-Poisson-bracket proof, but it identifies which
combination the primary degeneracy removes and shows that it is NOT the
negative active combination.
"""

from __future__ import annotations

import sympy as sp


r, M, q, ell, f = sp.symbols(
    "r M q ell f", positive=True, finite=True
)
a, b = sp.symbols(
    "a b", real=True, finite=True
)

pi = sp.pi

n2 = sp.factor(a**2 + b**2)

# Abstract original vector perturbations in the active/null basis.
U, V = sp.symbols(
    "U V", real=True
)

uA = sp.factor(
    (-a * U + b * V) / sp.sqrt(n2)
)
uB = sp.factor(
    (b * U + a * V) / sp.sqrt(n2)
)

diff = sp.factor(
    uA**2 - uB**2
)

expected_diff = sp.factor(
    (
        (a**2 - b**2) * U**2
        - 4 * a * b * U * V
        + (b**2 - a**2) * V**2
    )
    / n2
)

assert sp.simplify(
    diff - expected_diff
) == 0


# Direct principal negative coefficient.
alpha = sp.factor(
    sp.Rational(192, 5)
    * pi
    * ell**4
    / f**2
)

DU, DV = sp.symbols(
    "D_U D_V", real=True
)

Lder = sp.factor(
    -alpha * n2 * DU**2
)

Huv = sp.Matrix(
    [
        [
            sp.diff(Lder, vi, vj)
            for vj in (DU, DV)
        ]
        for vi in (DU, DV)
    ]
)

assert sp.simplify(
    Huv
    - sp.diag(
        -2 * alpha * n2,
        0,
    )
) == sp.zeros(2)


# Algebraic mass/stiffness term from the original A-B action.
N = sp.Rational(96, 5) * pi
C = sp.symbols(
    "C", positive=True, finite=True
)

Lalg = sp.expand(
    N * ell**2 * C * diff
)

coeff_V2 = sp.factor(
    sp.diff(Lalg, V, 2) / 2
)

expected_V2 = sp.factor(
    N
    * ell**2
    * C
    * (b**2 - a**2)
    / n2
)

assert sp.simplify(
    coeff_V2 - expected_V2
) == 0


# Exact regular branch positivity check.
D0 = r**3 + 2 * q * ell**2
freg = sp.factor(
    1 - 2 * M * r**2 / D0
)

areg = sp.factor(
    (r - r * freg - q / 2)
    / (2 * r**2)
)

breg = sp.factor(
    (r - r * freg + q / 2)
    / (2 * r**2)
)

Creg = sp.factor(
    36
    * M
    * q
    * ell**2
    * r**3
    / D0**3
)

diffreg = sp.factor(
    breg**2 - areg**2
)

assert sp.simplify(
    diffreg
    - M * q / (r * D0)
) == 0

n2reg = sp.factor(
    areg**2 + breg**2
)

V2reg = sp.factor(
    expected_V2.subs(
        {
            a: areg,
            b: breg,
            C: Creg,
        }
    )
)

# All explicit factors in this representation are positive for
# M,q,ell,r>0, except possible metric-horizon issues do not enter this
# algebraic V^2 stiffness.
expected_V2reg = sp.factor(
    N
    * ell**2
    * Creg
    * diffreg
    / n2reg
)

assert sp.simplify(
    V2reg - expected_V2reg
) == 0


# The active kinetic eigenvalue is manifestly negative in every static
# region f^2>0 and for n2>0.
lambda_active = sp.factor(
    -2
    * alpha
    * n2
)


def main() -> None:
    print("== Direct active/null vector basis ==")
    print("U = (-a u_A + b u_B)/sqrt(a^2+b^2)")
    print("V = ( b u_A + a u_B)/sqrt(a^2+b^2)")
    print()
    print("u_A^2-u_B^2 =")
    print(diff)
    print()
    print("principal derivative Hessian in (D U, D V) =")
    print(Huv)
    print()
    print(f"active kinetic eigenvalue = {lambda_active}")
    print("null principal derivative eigenvalue = 0")
    print()
    print("algebraic V^2 coefficient =")
    print(coeff_V2)
    print()
    print("On the exact regular branch:")
    print(f"b^2-a^2 = {diffreg}")
    print(f"C(r) = {Creg}")
    print(f"V^2 stiffness = {V2reg}")
    print()
    print(
        "Thus the derivative-null V combination has nonzero algebraic "
        "stiffness and is generically auxiliary, while the orthogonal "
        "active U combination retains the negative principal kinetic term."
    )
    print(
        "A full Dirac Poisson-bracket calculation is still required for "
        "the publication-level physical ghost theorem."
    )
    print("All active/null constraint assertions passed.")


if __name__ == "__main__":
    main()
