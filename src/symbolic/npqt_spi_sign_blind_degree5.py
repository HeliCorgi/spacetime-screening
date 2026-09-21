#!/usr/bin/env python3
"""Degree <= 5 SPI sign-blind gate from class-B CM/ZM syzygies.

Published class-B warped-product syzygies (Santosuosso et al.,
gr-qc/9809012) relate the Carminati-McLenaghan / Zakhary-McIntosh invariants.

On the aligned spherical NPQT stratum

    Weyl type D parameter q,
    mixed traceless-Ricci eigenvalues (-theta,-theta,theta,theta),

the standard CM normalizations are

    r1 = theta^2,
    r2 = 0,
    r3 = theta^4/4,
    w1 = 6 q^2,
    w2 = -6 q^3,
    m1 = -2 q theta^2.

Using the published syzygies gives

    m2 = m3 = 4 q^2 theta^2,
    m4 = 0,
    m5 = -8 q^3 theta^2,
    m6 = 0.

Hence the whole CM+ZM generator set through degree five is invariant under
theta -> -theta at this stratum.

Santosuosso et al. state that the CM+ZM set is complete to degree five for
general spacetimes: any scalar polynomial curvature invariant of degree <= 5
can be expressed rationally in that set.  Therefore all degree <= 5 SPIs are
sign blind here.

The literature completeness statement is an input; this script verifies the
specialized algebra and syzygies only.
"""

from __future__ import annotations

import sympy as sp

q, theta = sp.symbols("q theta", nonzero=True, real=True)

r1 = theta**2
r2 = sp.Integer(0)
r3 = theta**4 / 4

w1 = 6 * q**2
w2 = -6 * q**3
m1 = -2 * q * theta**2

# Published type-D / class-B syzygies:
# (3 m2 - w1 r1) w1 - 3 m1 w2 = 0
m2 = sp.factor((w1 * r1 + 3 * m1 * w2 / w1) / 3)

# m3 - m2 = 0
m3 = m2

# 6 m4 + w1 r2 = 0
m4 = sp.factor(-w1 * r2 / 6)

# (3 m5 - w1 conjugate(m1)) w1 - 3 m3 w2 = 0.
# The present purely-electric/aligned family has real m1.
m5 = sp.factor((w1 * m1 + 3 * m3 * w2 / w1) / 3)

# 2(3 m6 - m1 r1) w2 + m1^2 w1 = 0
m6 = sp.factor((2 * m1 * r1 * w2 - m1**2 * w1) / (6 * w2))

assert m2 == 4 * q**2 * theta**2
assert m3 == 4 * q**2 * theta**2
assert m4 == 0
assert m5 == -8 * q**3 * theta**2
assert m6 == 0

# Remaining published syzygies.
assert sp.simplify(6 * w2**2 - w1**3) == 0
assert sp.simplify((3 * m2 - w1 * r1) * w1 - 3 * m1 * w2) == 0
assert sp.simplify((3 * m5 - w1 * m1) * w1 - 3 * m3 * w2) == 0
assert sp.simplify(6 * m4 + w1 * r2) == 0
assert sp.simplify(m3 - m2) == 0
assert sp.simplify(
    2 * (3 * m6 - m1 * r1) * w2 + m1**2 * w1
) == 0

ricci_syzygy = sp.factor(
    (-12 * r3 + 7 * r1**2) ** 3
    - (12 * r2**2 - 36 * r1 * r3 + 17 * r1**3) ** 2
)
assert ricci_syzygy == 0

generators = {
    "r1": r1,
    "r2": r2,
    "r3": r3,
    "w1": w1,
    "w2": w2,
    "m1": m1,
    "m2": m2,
    "m3": m3,
    "m4": m4,
    "m5": m5,
    "m6": m6,
}

for name, value in generators.items():
    assert sp.simplify(value.subs(theta, -theta) - value) == 0, name

target = 48 * q**2 * theta
assert sp.simplify(target.subs(theta, -theta) + target) == 0
assert target != 0

def main() -> None:
    print("== NPQT degree<=5 scalar-invariant sign gate ==")
    for name, value in generators.items():
        print(f"{name} = {value}")
    print()
    print("Every checked CM/ZM generator is even under theta -> -theta.")
    print(f"Target W2*theta = {target} is odd.")
    print()
    print("With the published degree-five completeness of CM+ZM as input,")
    print("all scalar polynomial Riemann invariants through degree five are")
    print("blind to the sign required by the NPQT spherical target.")
    print("All degree-five sign-gate assertions passed.")

if __name__ == "__main__":
    main()
