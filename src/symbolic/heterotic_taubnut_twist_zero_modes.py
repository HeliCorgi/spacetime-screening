#!/usr/bin/env python3
"""Heterotic Taub-NUT chronology twist: global U(1)_B sector and zero modes.

Source conventions follow Johnson & Svendsen (2004) as reproduced in
notes/heterotic-ctc-operational-traversal.md (Sec. 7.2):

    U(1)_A :  g1 -> exp(eps_A s3/2) g1 exp(delta eps_A s3/2)
    U(1)_B :  g1 -> g1 exp(lambda eps_B s3/2),   g2 -> g2 exp(i eps_B s3/2)

with left heterotic charge vectors (Q_A,P_A), (Q_B,P_B) and right
supersymmetric-fermion embedding (delta,0), (lambda,1).

Part 1 (classical lift): the target-space chronology winding
    Delta t = 4 pi lambda w
lifts to the parent boundary condition
    g1(sigma+2pi) = g1(sigma) exp(2 pi lambda w s3),   g2 periodic.
This script shows by direct 2x2 matrix algebra that the sigma-dependent
gauge transformation eps_B(sigma) = -2 w sigma maps this twisted lift to a
periodic lift in which g1 is constant and g2 winds w times along the
Hopf fibre of SU(2)=S^3, with the same gauge-invariant target coordinate
t(sigma) = 2 lambda w sigma.  It also checks that the gauged R_A x R_B
action on (t_L, t_R, psi) is free with the single invariant
t = t_R - delta t_L - lambda psi, and that the slice t_L = t_R = 0 is a
global slice (fixed-x sections of the target are SU(2) = S^3 wherever the
hyperbolic chart is nondegenerate, i.e. away from the horizons x = +-1).

Part 2 (zero modes): with each gauged current written as a sum of chiral
U(1) currents J_i of level kappa_i and charges (q_i^A, q_i^B), the note's
three anomaly equations are exactly the equalities of the left and right
level matrices K_L = K_R.  The large gauge transformation eps_B = 2 w sigma
shifts every zero mode by 2 kappa_i q_i^B w.  The note's zero-mode gauge
constraints G_A, G_B (sums of left and right matter charges) are NOT
invariant: they shift by 4 w (Q_A Q_B + P_A P_B) and 4 w (Q_B^2 + P_B^2),
which is exactly compensated by the winding of the Karabali-Schnitzer
auxiliary gauge bosons.  The total (matter + auxiliary) constraints are
invariant.

All results are REPRODUCED / SYNTHESIS checks of standard gauged-WZW
technology applied to the Taub-NUT embedding; no representation-theoretic
assumption is asserted.
"""

import sympy as sp

# ---------------------------------------------------------------------------
# Part 1: classical lift of the chronology winding and its gauge image
# ---------------------------------------------------------------------------

lam, delta, sigma = sp.symbols("lambda delta sigma", real=True)
w = sp.Symbol("w", integer=True)

Id = sp.eye(2)


def exp_s3(a):
    """exp(a * s3) for the diagonal generator s3 = diag(1, -1)."""
    return sp.Matrix([[sp.exp(a), 0], [0, sp.exp(-a)]])


def gauge_B(g1, g2, eps):
    """U(1)_B action with parameter eps on (g1, g2): right multiplication."""
    return g1 * exp_s3(lam * eps / 2), g2 * exp_s3(sp.I * eps / 2)


# (i) eps_B = 4 pi w acts trivially on SU(2), nontrivially on SL(2,R).
monodromy_su2 = exp_s3(sp.I * 4 * sp.pi * w / 2)
monodromy_sl2 = exp_s3(lam * 4 * sp.pi * w / 2)
assert sp.simplify(monodromy_su2 - Id) == sp.zeros(2, 2)
assert sp.simplify(monodromy_sl2 - exp_s3(2 * sp.pi * lam * w)) == sp.zeros(2, 2)
assert sp.simplify(monodromy_sl2.subs({lam: sp.Rational(1, 3), w: 1}) - Id) != sp.zeros(2, 2)

# (ii) Twisted lift of the t-winding loop at fixed (x, theta, phi):
#      g1(sigma) = g1_0 exp(lambda w sigma s3),  g2(sigma) = g2_0.
g1_0 = sp.Matrix(2, 2, sp.symbols("a b c d", real=True))
g2_0 = sp.Matrix(2, 2, sp.symbols("p q r s"))
g1_tw = g1_0 * exp_s3(lam * w * sigma)
g2_tw = g2_0

# Monodromy of the twisted lift is the eps_B = 4 pi w gauge element.
assert sp.simplify(
    g1_tw.subs(sigma, sigma + 2 * sp.pi) - g1_tw * exp_s3(2 * sp.pi * lam * w)
) == sp.zeros(2, 2)

# (iii) Apply the sigma-dependent gauge transformation eps_B(sigma) = -2 w sigma.
g1_per, g2_per = gauge_B(g1_tw, g2_tw, -2 * w * sigma)
assert sp.simplify(g1_per - g1_0) == sp.zeros(2, 2)  # g1 becomes constant
hopf = exp_s3(-sp.I * w * sigma)
assert sp.simplify(g2_per - g2_0 * hopf) == sp.zeros(2, 2)  # g2 winds the Hopf fibre
# The gauge image is periodic for every integer w.
assert sp.simplify(g2_per.subs(sigma, sigma + 2 * sp.pi) - g2_per) == sp.zeros(2, 2)
assert sp.simplify(g1_per.subs(sigma, sigma + 2 * sp.pi) - g1_per) == sp.zeros(2, 2)

# (iv) Gauge-invariant target coordinate.  With
#      g1 = exp(t_L s3/2) h(x) exp(t_R s3/2),  g2 = ... exp(i psi s3/2),
#      the only R_A x R_B-invariant linear combination is
#      t = t_R - delta t_L - lambda psi.
tL, tR, psi = sp.symbols("t_L t_R psi", real=True)
coords = sp.Matrix([tL, tR, psi])
gen_A = sp.Matrix([1, delta, 0])
gen_B = sp.Matrix([0, lam, 1])
t_inv = tR - delta * tL - lam * psi
grad_t = sp.Matrix([sp.diff(t_inv, c) for c in coords])
assert sp.simplify(grad_t.dot(gen_A)) == 0
assert sp.simplify(grad_t.dot(gen_B)) == 0
# Uniqueness: the annihilator of span(gen_A, gen_B) is one-dimensional.
M = sp.Matrix.hstack(gen_A, gen_B).T  # 2 x 3
assert M.rank() == 2  # free action, two-dimensional orbits
null = M.nullspace()
assert len(null) == 1
assert sp.simplify(null[0] / null[0][1] - grad_t / grad_t[1]) == sp.zeros(3, 1)
# Global slice t_L = t_R = 0: the (t_L,t_R)-block of the generators is
# invertible iff lambda != 0, so every orbit meets the slice exactly once
# and the fixed-x section of the target is the SU(2) group manifold S^3.
block = sp.Matrix([[1, delta], [0, lam]])
assert sp.simplify(block.det() - lam) == 0

# Twisted lift: (t_L, t_R, psi) = (0, 2 lambda w sigma, 0).
# Periodic (Hopf) lift: (t_L, t_R, psi) = (0, 0, -2 w sigma).
t_twisted = t_inv.subs({tL: 0, tR: 2 * lam * w * sigma, psi: 0})
t_hopf = t_inv.subs({tL: 0, tR: 0, psi: -2 * w * sigma})
assert sp.simplify(t_twisted - t_hopf) == 0
assert sp.simplify(
    t_twisted.subs(sigma, sigma + 2 * sp.pi) - t_twisted - 4 * sp.pi * lam * w
) == 0

print("Part 1: twisted lift g1(s+2pi)=g1(s)exp(2 pi lam w s3) is the gauge image")
print("        (eps_B = -2 w sigma) of a periodic lift with g1 constant and g2")
print("        winding w times along the Hopf fibre; same invariant t = 2 lam w sigma.")

# ---------------------------------------------------------------------------
# Part 2: zero-mode algebra of the large U(1)_B gauge transformation
# ---------------------------------------------------------------------------

k1, k2 = sp.symbols("k_1 k_2", positive=True)
QA, PA, QB, PB = sp.symbols("Q_A P_A Q_B P_B", real=True)

# Chiral U(1) sectors: (name, chirality, level kappa, q^A, q^B, zero-mode symbol).
# Levels: WZW Cartan currents J^3 (coefficient of s3/2) have J^3 J^3 ~ (k/2)/z^2;
# a bosonized complex fermion has level 1.  The overall normalization drops
# out of every identity checked below.
m, Mb, Nb, f1, f2, s1, s2 = sp.symbols("m Mbar Nbar f_1 f_2 s_1 s_2", real=True)
sectors = [
    ("SL2_L", "L", k1 / 2, 1, 0, m),  # t_{A,L} = +s3/2
    ("FL1", "L", 1, QA, QB, s1),  # left heterotic fermion 1
    ("FL2", "L", 1, PA, PB, s2),  # left heterotic fermion 2
    ("SL2_R", "R", k1 / 2, delta, lam, Mb),  # t_{A,R}, t_{B,R} on SL(2,R)
    ("SU2_R", "R", k2 / 2, 0, 1, Nb),  # t_{B,R} on SU(2)
    ("FR1", "R", 1, delta, lam, f1),  # right susy fermion (SL(2,R) directions)
    ("FR2", "R", 1, 0, 1, f2),  # right susy fermion (SU(2) directions)
]


def level_matrix(chir):
    K = sp.zeros(2, 2)
    for (_, c, kap, qA, qB, _) in sectors:
        if c != chir:
            continue
        qv = sp.Matrix([qA, qB])
        K += kap * qv * qv.T
    return sp.simplify(K)


K_L = level_matrix("L")
K_R = level_matrix("R")

# The note's anomaly-cancellation equations (all written as expr = 0).
E_AA = -k1 * (1 - delta**2) - 2 * (QA**2 + PA**2 - delta**2)
E_AB = k1 * delta * lam - 2 * (QA * QB + PA * PB - delta * lam)
E_BB = k2 + k1 * lam**2 - 2 * (QB**2 + PB**2 - (1 + lam**2))

# Anomaly cancellation <=> K_L = K_R  (entrywise, up to the factor 2).
assert sp.simplify(2 * (K_L - K_R)[0, 0] + E_AA) == 0
assert sp.simplify(2 * (K_L - K_R)[0, 1] + E_AB) == 0
assert sp.simplify(2 * (K_L - K_R)[1, 1] + E_BB) == 0
print("Part 2a: note's anomaly equations  <=>  K_L = K_R (left/right level matrices).")


def matter_charge(chir, X):
    """Matter zero-mode gauge charge of chirality chir under U(1)_X.

    In the note's sign convention all right-moving charges enter with a plus
    sign, so the note's G_X = J_X^L + J_X^R is the winding-like combination.
    """
    idx = 0 if X == "A" else 1
    tot = 0
    for (_, c, kap, qA, qB, p) in sectors:
        if c == chir:
            tot += (qA, qB)[idx] * p
    return sp.expand(tot)


JL = {X: matter_charge("L", X) for X in "AB"}
JR = {X: matter_charge("R", X) for X in "AB"}

# Reproduce the note's linear forms with Mbar_total = Mb + f1, Nbar_total = Nb + f2.
Mbar_tot, Nbar_tot = sp.symbols("Mbar_tot Nbar_tot", real=True)
G_A_note = m + delta * Mbar_tot + QA * s1 + PA * s2
G_B_note = lam * Mbar_tot + Nbar_tot + QB * s1 + PB * s2
sub_tot = {Mbar_tot: Mb + f1, Nbar_tot: Nb + f2}
assert sp.simplify(JL["A"] + JR["A"] - G_A_note.subs(sub_tot)) == 0
assert sp.simplify(JL["B"] + JR["B"] - G_B_note.subs(sub_tot)) == 0
print("Part 2b: note's G_A, G_B reproduced as J^L + J^R with Mbar = Mb + f1, Nbar = Nb + f2.")

# Large gauge transformation eps_B(sigma) = 2 w sigma: flow parameter for a
# sector of charge q^B is eta_i = 2 w q^B_i; every zero mode shifts by
# kappa_i eta_i = 2 kappa_i q_i^B w (both chiralities, note's sign convention).
shift = {p: p + 2 * kap * qB * w for (_, c, kap, qA, qB, p) in sectors}

dG = {
    X: sp.expand((JL[X] + JR[X]).subs(shift, simultaneous=True) - (JL[X] + JR[X]))
    for X in "AB"
}
assert sp.simplify(dG["A"] - 2 * w * (K_L + K_R)[0, 1]) == 0
assert sp.simplify(dG["B"] - 2 * w * (K_L + K_R)[1, 1]) == 0
# Explicit values.
dG_B_explicit = sp.expand(w * (k1 * lam**2 + k2 + 2 * lam**2 + 2 + 2 * QB**2 + 2 * PB**2))
assert sp.simplify(dG["B"] - dG_B_explicit) == 0
dG_A_explicit = sp.expand(w * ((k1 + 2) * delta * lam + 2 * (QA * QB + PA * PB)))
assert sp.simplify(dG["A"] - dG_A_explicit) == 0
# Using the anomaly equations these equal 4 w (Q_B^2 + P_B^2) and 4 w (Q_A Q_B + P_A P_B).
assert sp.simplify(dG["B"] - 4 * w * (QB**2 + PB**2) - w * E_BB) == 0
assert sp.simplify(dG["A"] - 4 * w * (QA * QB + PA * PB) - w * E_AB) == 0
print("Part 2c: matter-only G_A, G_B are NOT invariant:")
print("         dG_B = 4 w (Q_B^2+P_B^2),  dG_A = 4 w (Q_A Q_B + P_A P_B)  (on the anomaly surface).")

# Auxiliary (Karabali-Schnitzer) gauge bosons: one non-chiral boson per gauged
# U(1), level matrix -K in each chirality, charge matrix = identity.
aL = sp.Matrix(sp.symbols("aL_A aL_B", real=True))
aR = sp.Matrix(sp.symbols("aR_A aR_B", real=True))
CL = sp.Matrix([JL["A"], JL["B"]]) + aL  # holomorphic total zero-mode constraints
CR = sp.Matrix([JR["A"], JR["B"]]) + aR  # antiholomorphic
# Flow of the auxiliary zero modes under eps_B = 2 w sigma: -K * eta with eta = (0, 2w).
eta = sp.Matrix([0, 2 * w])
shift_aux = {}
for i in range(2):
    shift_aux[aL[i]] = aL[i] - (K_L * eta)[i]
    shift_aux[aR[i]] = aR[i] - (K_R * eta)[i]
full_shift = dict(shift)
full_shift.update(shift_aux)
dCL = sp.simplify(CL.subs(full_shift, simultaneous=True) - CL)
dCR = sp.simplify(CR.subs(full_shift, simultaneous=True) - CR)
assert dCL == sp.zeros(2, 1)
assert dCR == sp.zeros(2, 1)
print("Part 2d: total constraints (matter + auxiliary gauge boson) are exactly invariant;")
print("         the auxiliary boson absorbs the shift -2 K^{XB} w per chirality.")

# Previous-phase boson shifts: Delta Phi_1 : Delta Phi_2 = (Q_B+lambda) : (P_B+1).
# The non-chiral boson Phi_1 pairs FL1 (left charge Q_B) with FR1 (right charge
# lambda); its winding shift is proportional to the sum of the two zero-mode shifts.
dPhi1 = (shift[s1] - s1) + (shift[f1] - f1)
dPhi2 = (shift[s2] - s2) + (shift[f2] - f2)
assert sp.simplify(dPhi1 - 2 * w * (QB + lam)) == 0
assert sp.simplify(dPhi2 - 2 * w * (PB + 1)) == 0
print("Part 2e: bosonized shifts reproduce Delta Phi_1 : Delta Phi_2 = (Q_B+lambda) : (P_B+1).")

print("OK: heterotic Taub-NUT twist zero-mode checks passed.")
