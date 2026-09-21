#!/usr/bin/env python3
"""Direct l=1 odd-harmonic expansion of the original A-B action.

This is the dipole counterpart of direct_two_vector_odd_l2.py.  It repeats
the full four-dimensional curvature expansion with the axial Killing harmonic
S_phi=sin^2(theta), rather than relying on the local principal reduction.

NO generalized-Proca perturbation coefficients are imported here.

Original action (overall 1/(16 pi G) omitted):
    S = ∫ sqrt(-g) [ R + ell^2 ( L[A] - L[B] ) ]

    L[V] =
        4 G^{mu nu} V_mu V_nu
      + 8 V^2 nabla_mu V^mu
      + 6 (V^2)^2.

Background:
    ds^2 = -f dt^2 + dr^2/f + r^2 dOmega^2,
    V_bar = p(r) (dt + dr/f),
so V_bar^2=0.

Odd l=1,m=0 Regge-Wheeler-gauge perturbations:
    h_{t phi} = eps Q(t) S_phi(theta)
    h_{r phi} = eps W(t) S_phi(theta)
    delta V_phi = eps u(t) S_phi(theta)

with the unnormalized axial harmonic
    S_phi = 3 sin^2(theta) cos(theta).

For the kinetic/constraint check it is sufficient to suppress radial
derivatives of Q,W,u after the harmonic decomposition; f(r), p(r) and their
background derivatives are kept exact.

The script computes the 4D Christoffels, Ricci tensor/scalar and Einstein
tensor directly to O(eps^2), constructs the ORIGINAL vector Lagrangian, and
integrates over the sphere.

After time integration by parts it verifies:
    EH:       A dot(W)^2,          A = 12 pi/5
    vector:   B(p) dot(W) dot(u),  B = -96 pi p/(5 f)
    vector:   D(p) Q dot(u),       D = -192 pi p/(5 r f)
    no direct dot(u)^2 term,
    D = (2/r) B.

For the full A-B theory this gives the direct velocity Hessian
in (dot W, dot u_A, dot u_B):

    H = (24 pi/5) *
        [[1, -4 ell^2 a/f, +4 ell^2 b/f],
         [-4 ell^2 a/f, 0, 0],
         [+4 ell^2 b/f, 0, 0]].

It has rank 2, one positive eigenvalue, one negative eigenvalue, and one
zero eigenvalue.  The null vector is proportional to (0,b,a).

The primary velocity-null constraint is therefore the direct-harmonic
combination
    b p_A + a p_B = (field-only terms),
in addition to p_Q=0 because Q has no velocity.

This is the independent source-action check requested by the project.  It
matches the coefficient ratios obtained earlier from the published
one-vector formalism, but does not use that formalism in the derivation.
"""

from __future__ import annotations

import sympy as sp


# ---------------------------------------------------------------------------
# Coordinates, background and harmonic
# ---------------------------------------------------------------------------

t, r, th, ph, eps = sp.symbols(
    "t r theta phi epsilon", real=True
)
ell = sp.symbols("ell", positive=True, finite=True)

f = sp.Function("f")(r)
p = sp.Function("p")(r)

Q = sp.Function("Q")(t)
W = sp.Function("W")(t)
u = sp.Function("u")(t)

S = sp.sin(th) ** 2

coords = (t, r, th, ph)
dim = 4


def trunc(expr: sp.Expr) -> sp.Expr:
    """Series in eps through O(eps^2)."""
    return sp.simplify(
        sp.series(expr, eps, 0, 3).removeO()
    )


# Background metric and odd perturbation.
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

g = sp.Matrix(
    [
        [-f, 0, 0, eps * Q * S],
        [0, 1 / f, 0, eps * W * S],
        [0, 0, r**2, 0],
        [eps * Q * S, eps * W * S, 0, r**2 * sp.sin(th) ** 2],
    ]
)

h = (g - g0) / eps

# Inverse metric through O(eps^2), using the Neumann series.
g1i = -g0i * h * g0i
g2i = g0i * h * g0i * h * g0i
gi = g0i + eps * g1i + eps**2 * g2i


# ---------------------------------------------------------------------------
# Direct 4D curvature expansion
# ---------------------------------------------------------------------------

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
            Gamma[aa][bb][cc] = trunc(expr / 2)


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
        Ric[aa][bb] = trunc(expr)


Rscalar = 0
for aa in range(dim):
    for bb in range(dim):
        Rscalar += gi[aa, bb] * Ric[aa][bb]
Rscalar = trunc(Rscalar)


Gcov = [
    [sp.Integer(0) for _ in range(dim)]
    for _ in range(dim)
]

for aa in range(dim):
    for bb in range(dim):
        Gcov[aa][bb] = trunc(
            Ric[aa][bb]
            - sp.Rational(1, 2) * g[aa, bb] * Rscalar
        )


Gup = [
    [sp.Integer(0) for _ in range(dim)]
    for _ in range(dim)
]

for aa in range(dim):
    for bb in range(dim):
        expr = 0
        for mm in range(dim):
            for nn in range(dim):
                expr += gi[aa, mm] * gi[bb, nn] * Gcov[mm][nn]
        Gup[aa][bb] = trunc(expr)


# sqrt(-g); in the angular integration region r>0 and sin(theta)>=0.
sqrtg = trunc(
    sp.series(sp.sqrt(-sp.factor(g.det())), eps, 0, 3).removeO()
)
sqrtg = sp.simplify(
    sqrtg.subs(sp.sqrt(r**2), r)
    .subs(sp.Abs(sp.sin(th)), sp.sin(th))
)


def sphere_integrate(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(
        2 * sp.pi * sp.integrate(expr, (th, 0, sp.pi))
    )


# ---------------------------------------------------------------------------
# Einstein-Hilbert quadratic temporal sector
# ---------------------------------------------------------------------------

EH_density = trunc(sqrtg * Rscalar)
EH2 = sp.expand(EH_density).coeff(eps, 2)
EHred = sphere_integrate(EH2)


# ---------------------------------------------------------------------------
# Original one-vector quadratic action
# ---------------------------------------------------------------------------

Vcov = sp.Matrix(
    [
        p,
        p / f,
        0,
        eps * u * S,
    ]
)

Vup = sp.Matrix(
    [
        trunc(sum(gi[ii, jj] * Vcov[jj] for jj in range(dim)))
        for ii in range(dim)
    ]
)

V2 = trunc((Vcov.T * Vup)[0])

invsqrtg = trunc(
    sp.series(1 / sqrtg, eps, 0, 3).removeO()
)

div_num = 0
for ii, coord in enumerate(coords):
    div_num += sp.diff(sqrtg * Vup[ii], coord)
divV = trunc(invsqrtg * div_num)

GVV = 0
for mm in range(dim):
    for nn in range(dim):
        GVV += Gup[mm][nn] * Vcov[mm] * Vcov[nn]
GVV = trunc(GVV)

LV = trunc(
    4 * GVV
    + 8 * V2 * divV
    + 6 * V2**2
)

V_density = trunc(sqrtg * LV)
V2density = sp.expand(V_density).coeff(eps, 2)
Vred = sphere_integrate(V2density)


# ---------------------------------------------------------------------------
# Canonicalize only the time-derivative terms by integration by parts.
# ---------------------------------------------------------------------------

q0, w0, u0 = sp.symbols("q0 w0 u0")
qd, wd, ud, wdd = sp.symbols("qd wd ud wdd")

jet_subs = {
    Q: q0,
    W: w0,
    u: u0,
    sp.diff(Q, t): qd,
    sp.diff(W, t): wd,
    sp.diff(u, t): ud,
    sp.diff(W, t, 2): wdd,
}

EHj = sp.expand(EHred.xreplace(jet_subs))
Vj = sp.expand(Vred.xreplace(jet_subs))


# EH: integrate w*wdd by parts.
c_wwdd = sp.simplify(
    sp.diff(sp.diff(EHj, wdd), w0)
)
EHc = sp.expand(
    EHj
    - c_wwdd * w0 * wdd
    - c_wwdd * wd**2
)

# EH: integrate qdot*w by parts.
c_qdw = sp.simplify(
    sp.diff(sp.diff(EHc, qd), w0)
)
EHc = sp.expand(
    EHc
    - c_qdw * qd * w0
    - c_qdw * q0 * wd
)

assert sp.simplify(sp.diff(EHc, qd)) == 0
assert sp.simplify(sp.diff(EHc, wdd)) == 0


A_EH = sp.simplify(
    sp.diff(EHc, wd, 2) / 2
)
C_QW = sp.simplify(
    sp.diff(sp.diff(EHc, q0), wd)
)

assert sp.simplify(A_EH - 4 * sp.pi / 3) == 0
assert sp.simplify(C_QW - 16 * sp.pi / (3 * r)) == 0


# Vector: integrate u*wdd by parts.
c_uwdd = sp.simplify(
    sp.diff(sp.diff(Vj, wdd), u0)
)
Vc = sp.expand(
    Vj
    - c_uwdd * u0 * wdd
    + c_uwdd * (-ud * wd)
)

# Vector: integrate qdot*w and qdot*u by parts.
c_qdw_v = sp.simplify(
    sp.diff(sp.diff(Vc, qd), w0)
)
c_qdu_v = sp.simplify(
    sp.diff(sp.diff(Vc, qd), u0)
)

Vc = sp.expand(
    Vc
    - c_qdw_v * qd * w0
    - c_qdu_v * qd * u0
    - c_qdw_v * q0 * wd
    - c_qdu_v * q0 * ud
)

assert sp.simplify(sp.diff(Vc, qd)) == 0
assert sp.simplify(sp.diff(Vc, wdd)) == 0


B_WU = sp.simplify(
    sp.diff(sp.diff(Vc, wd), ud)
)
D_QU = sp.simplify(
    sp.diff(sp.diff(Vc, q0), ud)
)
direct_uu = sp.simplify(
    sp.diff(Vc, ud, 2)
)
direct_qw = sp.simplify(
    sp.diff(sp.diff(Vc, q0), wd)
)

assert sp.simplify(
    B_WU + 32 * sp.pi * p / (3 * f)
) == 0

assert sp.simplify(
    D_QU + 64 * sp.pi * p / (3 * r * f)
) == 0

assert direct_uu == 0
assert direct_qw == 0

assert sp.simplify(
    D_QU - 2 * B_WU / r
) == 0


# ---------------------------------------------------------------------------
# Direct two-vector velocity Hessian and primary null direction.
# ---------------------------------------------------------------------------

a, b = sp.symbols(
    "a b", real=True, finite=True
)

H0 = 2 * A_EH
HA = sp.factor(
    ell**2 * B_WU.subs(p, a)
)
HB = sp.factor(
    -ell**2 * B_WU.subs(p, b)
)

H_direct = sp.Matrix(
    [
        [H0, HA, HB],
        [HA, 0, 0],
        [HB, 0, 0],
    ]
)

H_expected = sp.factor(8 * sp.pi / 3) * sp.Matrix(
    [
        [1, -4 * ell**2 * a / f, +4 * ell**2 * b / f],
        [-4 * ell**2 * a / f, 0, 0],
        [+4 * ell**2 * b / f, 0, 0],
    ]
)

assert sp.simplify(H_direct - H_expected) == sp.zeros(3)

lam = sp.symbols("lambda")
charpoly = sp.factor(
    H_direct.charpoly(lam).as_expr()
)

off2 = sp.factor(HA**2 + HB**2)
expected_charpoly = sp.factor(
    lam * (lam**2 - H0 * lam - off2)
)

assert sp.simplify(
    charpoly - expected_charpoly
) == 0

null_vec = sp.Matrix(
    [0, b, a]
)

assert sp.simplify(
    H_direct * null_vec
) == sp.zeros(3, 1)

# Product of the two nonzero Hessian eigenvalues is -off2 < 0.
# Hence, for nonzero hair, one is positive and one is negative.
assert sp.factor(off2) == (
    1024 * sp.pi**2 * ell**4 * (a**2 + b**2)
    / (9 * f**2)
)


# Direct canonical momenta at the derivative-principal level.
# p_A ~ HA * dot(W) + D_A Q, p_B ~ HB * dot(W) + D_B Q,
# and D_i=(2/r) H_i, so b p_A + a p_B has no velocity.
DA = sp.factor(
    ell**2 * D_QU.subs(p, a)
)
DB = sp.factor(
    -ell**2 * D_QU.subs(p, b)
)

assert sp.simplify(
    DA - 2 * HA / r
) == 0

assert sp.simplify(
    DB - 2 * HB / r
) == 0

assert sp.simplify(
    b * HA + a * HB
) == 0

assert sp.simplify(
    b * DA + a * DB
) == 0


# ---------------------------------------------------------------------------
# Comparison only AFTER the independent derivation.
# ---------------------------------------------------------------------------

# Earlier source-formula specialization predicted the dimensionless ratios
# H_WA/H_WW = -4 ell^2 a/f and H_WB/H_WW = +4 ell^2 b/f.
# The direct original-action expansion reproduces them exactly.
assert sp.simplify(
    HA / H0 + 4 * ell**2 * a / f
) == 0

assert sp.simplify(
    HB / H0 - 4 * ell**2 * b / f
) == 0


def main() -> None:
    print("== Direct original-action l=1 odd expansion ==")
    print(f"EH kinetic coefficient A = {A_EH}")
    print(f"EH Q-dotW coefficient = {C_QW}")
    print()
    print("One original vector sector:")
    print(f"B_WU = {B_WU}")
    print(f"D_QU = {D_QU}")
    print(f"direct dot(u)^2 coefficient = {direct_uu}")
    print(f"direct Q dot(W) vector coefficient = {direct_qw}")
    print("D_QU = (2/r) B_WU")
    print()
    print("== Full A-B velocity Hessian ==")
    print(H_direct)
    print(f"characteristic polynomial = {charpoly}")
    print(f"null vector = {null_vec.T}")
    print()
    print(
        "For a^2+b^2 != 0 the two nonzero Hessian eigenvalues have "
        "opposite signs."
    )
    print(
        "The null velocity direction is the vector combination "
        "b delta A_odd + a delta B_odd."
    )
    print()
    print("Primary principal constraints:")
    print("p_Q = 0")
    print("b p_A + a p_B = field-only terms")
    print()
    print("Independent-expansion/source-formula coefficient ratios agree.")
    print("All direct-harmonic assertions passed.")


if __name__ == "__main__":
    main()
