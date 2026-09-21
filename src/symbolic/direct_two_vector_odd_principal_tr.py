#!/usr/bin/env python3
"""Direct full-(t,r) odd principal mixing from the original action.

This script does NOT import generalized-Proca odd coefficients.

It computes the linearized 4D Einstein tensor directly for

    ds^2 = -f dt^2 + dr^2/f + r^2 dOmega^2

with the l=2,m=0 Regge-Wheeler-gauge perturbation

    h_{t phi} = eps Q(t,r) S_phi,
    h_{r phi} = eps W(t,r) S_phi,

    S_phi = 3 sin^2(theta) cos(theta).

For a null background vector

    V_bar = p(r) (dt + dr/f)

and axial perturbation

    delta V_phi = eps u(t,r) S_phi,

the O(eps^2) metric-vector mixing from the ORIGINAL term
4 G^{mu nu} V_mu V_nu is controlled by

    V_bar_a delta G^{a phi}.

The direct calculation verifies that its highest-derivative piece is

    (3 cos theta)/(2 r^2 f)
    * (partial_t - f partial_r) X,

where

    X = dot W - Q' + 2 Q/r.

After angular integration, one original vector sector contributes

    L_mix,pr =
        (96 pi / 5) * (p/f) * u
        * (partial_t - f partial_r) X.

Integrating by parts gives the derivative-principal mixing

    L_mix,pr ~
        -(96 pi / 5) * (p/f)
        * (dot u - f u') * X.

Combining A and B with signs +ell^2 and -ell^2, and the independently
directly-derived Einstein-Hilbert coefficient A_EH=12 pi/5, yields

    L_pr =
        A_EH X^2
        + K X[-a D u_A + b D u_B],

    D = partial_t - f partial_r,
    K = 96 pi ell^2/(5 f).

Completing the derivative square gives

    L_pr =
        A_EH [ X + ... ]^2
        - (192 pi ell^4)/(5 f^2)
          [-a D u_A + b D u_B]^2.

Thus, directly from the original action, the vector derivative block is
rank one and negative semidefinite; the orthogonal combination
b D u_A + a D u_B has zero principal derivative term.

This independently reproduces the earlier reduced vector principal
characteristic D^2 ~ (omega+f k)^2.
"""

from __future__ import annotations

import sympy as sp


t, r, th, ph, eps = sp.symbols(
    "t r theta phi epsilon", real=True
)

ell = sp.symbols(
    "ell", positive=True, finite=True
)

f = sp.Function("f")(r)
p = sp.Function("p")(r)

Q = sp.Function("Q")(t, r)
W = sp.Function("W")(t, r)

coords = (t, r, th, ph)
dim = 4

S = 3 * sp.sin(th) ** 2 * sp.cos(th)


# ---------------------------------------------------------------------------
# Linearized metric and inverse
# ---------------------------------------------------------------------------

g0 = sp.diag(
    -f,
    1 / f,
    r**2,
    r**2 * sp.sin(th) ** 2,
)

g0i = sp.diag(
    -1 / f,
    f,
    1 / r**2,
    1 / (r**2 * sp.sin(th) ** 2),
)

h = sp.zeros(4)
h[0, 3] = h[3, 0] = Q * S
h[1, 3] = h[3, 1] = W * S

g = g0 + eps * h
gi1 = -g0i * h * g0i
gi = g0i + eps * gi1


def trunc1(expr: sp.Expr) -> sp.Expr:
    expr = sp.expand(expr)
    return sp.simplify(
        expr.coeff(eps, 0)
        + eps * expr.coeff(eps, 1)
    )


Gamma = [
    [[sp.Integer(0) for _ in range(dim)] for _ in range(dim)]
    for _ in range(dim)
]

for aa in range(dim):
    for bb in range(dim):
        for cc in range(dim):
            expr = 0
            for dd in range(dim):
                expr += gi[aa, dd] * (
                    sp.diff(g[dd, cc], coords[bb])
                    + sp.diff(g[dd, bb], coords[cc])
                    - sp.diff(g[bb, cc], coords[dd])
                )
            Gamma[aa][bb][cc] = trunc1(expr / 2)


Ric = [
    [sp.Integer(0) for _ in range(dim)]
    for _ in range(dim)
]

for aa in range(dim):
    for bb in range(dim):
        expr = 0
        for cc in range(dim):
            expr += (
                sp.diff(Gamma[cc][aa][bb], coords[cc])
                - sp.diff(Gamma[cc][aa][cc], coords[bb])
            )
            for dd in range(dim):
                expr += (
                    Gamma[cc][cc][dd] * Gamma[dd][aa][bb]
                    - Gamma[cc][bb][dd] * Gamma[dd][aa][cc]
                )
        Ric[aa][bb] = trunc1(expr)


Rscalar = 0
for aa in range(dim):
    for bb in range(dim):
        Rscalar += gi[aa, bb] * Ric[aa][bb]
Rscalar = trunc1(Rscalar)


Gcov = [
    [sp.Integer(0) for _ in range(dim)]
    for _ in range(dim)
]

for aa in range(dim):
    for bb in range(dim):
        Gcov[aa][bb] = trunc1(
            Ric[aa][bb]
            - sp.Rational(1, 2)
            * g[aa, bb]
            * Rscalar
        )


Gup1 = [
    [sp.Integer(0) for _ in range(dim)]
    for _ in range(dim)
]

for aa in range(dim):
    for bb in range(dim):
        expr = 0
        for mm in range(dim):
            for nn in range(dim):
                expr += (
                    gi[aa, mm]
                    * gi[bb, nn]
                    * Gcov[mm][nn]
                )
        expr = sp.expand(expr)
        Gup1[aa][bb] = sp.simplify(
            expr.coeff(eps, 1)
        )


# Background vector covector is p(dt+dr/f).
Gmix = sp.factor(
    Gup1[0][3]
    + Gup1[1][3] / f
)


# ---------------------------------------------------------------------------
# Gauge-invariant odd derivative X and direct principal identity
# ---------------------------------------------------------------------------

X = (
    sp.diff(W, t)
    - sp.diff(Q, r)
    + 2 * Q / r
)

DX = (
    sp.diff(X, t)
    - f * sp.diff(X, r)
)

principal_Gmix = sp.factor(
    3 * sp.cos(th)
    / (2 * r**2 * f)
    * DX
)

remainder = sp.expand(
    Gmix - principal_Gmix
)

# The remainder may contain first derivatives but must contain no
# second derivatives of Q or W.
second_derivatives = [
    sp.diff(Q, t, 2),
    sp.diff(Q, t, r),
    sp.diff(Q, r, 2),
    sp.diff(W, t, 2),
    sp.diff(W, t, r),
    sp.diff(W, r, 2),
]

for atom in second_derivatives:
    assert not remainder.has(atom)


# ---------------------------------------------------------------------------
# Angular integral of the ORIGINAL 4 G^{mu nu} V_mu V_nu cross term
# ---------------------------------------------------------------------------

# At O(eps^2), the cross term is
#   8 p u S_phi * Gmix
# times sqrt(-g)_0 = r^2 sin(theta).
# Keeping only principal_Gmix:
angular_integral = sp.simplify(
    2 * sp.pi
    * sp.integrate(
        sp.sin(th) ** 3
        * sp.cos(th) ** 2,
        (th, 0, sp.pi),
    )
)

assert sp.simplify(
    angular_integral
    - 8 * sp.pi / 15
) == 0


# 8 * (3) * (3/2) = 36 before the angular integral.
mix_prefactor = sp.simplify(
    36 * angular_integral
)

assert sp.simplify(
    mix_prefactor
    - 96 * sp.pi / 5
) == 0


# ---------------------------------------------------------------------------
# Full A-B principal derivative sector
# ---------------------------------------------------------------------------

AEH = sp.Rational(12, 5) * sp.pi

a, b = sp.symbols(
    "a b", real=True, finite=True
)

DuA, DuB, Xsym = sp.symbols(
    "D_uA D_uB X", real=True
)

Kmix = sp.factor(
    sp.Rational(96, 5)
    * sp.pi
    * ell**2
    / f
)

Z = sp.factor(
    Kmix
    * (
        -a * DuA
        + b * DuB
    )
)

Lprincipal = sp.expand(
    AEH * Xsym**2
    + Z * Xsym
)

Ldiag = sp.expand(
    AEH
    * (
        Xsym
        + Z / (2 * AEH)
    ) ** 2
    - Z**2 / (4 * AEH)
)

assert sp.simplify(
    Lprincipal - Ldiag
) == 0


negative_block = sp.factor(
    -Z**2 / (4 * AEH)
)

expected_negative = sp.factor(
    -sp.Rational(192, 5)
    * sp.pi
    * ell**4
    / f**2
    * (
        -a * DuA
        + b * DuB
    ) ** 2
)

assert sp.simplify(
    negative_block - expected_negative
) == 0


# Null principal derivative direction.
# Active covector in vector-derivative space is (-a,b).
# Orthogonal direction is (b,a).
assert sp.simplify(
    (-a) * b
    + b * a
) == 0


# Principal vector matrix in D u = dot u - f u'.
cvec = sp.Matrix(
    [-a, b]
)

Kvec_direct = sp.factor(
    -sp.Rational(384, 5)
    * sp.pi
    * ell**4
    / f**2
) * (
    cvec * cvec.T
)

# Hessian of the negative block with respect to (DuA,DuB).
Hvec = sp.Matrix(
    [
        [
            sp.diff(
                expected_negative,
                vi,
                vj,
            )
            for vj in (DuA, DuB)
        ]
        for vi in (DuA, DuB)
    ]
)

assert sp.simplify(
    Hvec - Kvec_direct
) == sp.zeros(2)

assert sp.factor(
    Hvec.det()
) == 0

null_vec = sp.Matrix(
    [b, a]
)

assert sp.simplify(
    Hvec * null_vec
) == sp.zeros(2, 1)


def main() -> None:
    print("== Direct full-(t,r) odd principal expansion ==")
    print("V_bar_a delta G^{a phi} =")
    print(Gmix)
    print()
    print("highest-derivative part =")
    print(principal_Gmix)
    print()
    print("remainder contains no second derivatives of Q or W.")
    print()
    print(f"angular integral = {angular_integral}")
    print(f"mixing prefactor = {mix_prefactor}")
    print()
    print("== Direct A-B derivative sector ==")
    print("L_pr =")
    print(Lprincipal)
    print()
    print("completed square =")
    print(Ldiag)
    print()
    print("negative vector derivative block =")
    print(negative_block)
    print()
    print("vector principal Hessian =")
    print(Hvec)
    print(f"det = {sp.factor(Hvec.det())}")
    print(f"null direction = {null_vec.T}")
    print()
    print(
        "Thus the direct original action reproduces the rank-one "
        "negative-semidefinite D=(partial_t-f partial_r) vector block."
    )
    print(
        "In Fourier language this active combination has the double "
        "background-null factor (omega+f k)^2, up to Fourier-sign convention."
    )
    print("All direct full-(t,r) principal assertions passed.")


if __name__ == "__main__":
    main()
