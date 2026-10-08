#!/usr/bin/env python3
"""Exact interface checks for the Family 376 / gravity audit.

These are elementary identities and finite regression tests, NOT a reproduction
of the full OpenAI/math compiler, a fluid simulation, a GR solution, or a proof
of physical undecidability. No external data, network, or new dependency is used.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
import platform
from typing import Any

import sympy as sp

SPACETIME_SHA = "1ff10c4453f52f9f8f8c2c835a52812ce7faac90"
MATH_SHA = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_shear_energy() -> dict[str, Any]:
    """Unit-volume flat torus, density one; U=(a(t) sin(2 pi y),0,0)."""
    t, x, y, z = sp.symbols("t x y z", real=True)
    nu = sp.symbols("nu", positive=True)
    a = sp.Function("a")(t)
    k = 2 * sp.pi
    coords = (x, y, z)
    u = sp.Matrix([a * sp.sin(k*y), 0, 0])
    div = sum(sp.diff(u[i], coords[i]) for i in range(3))
    adv = sp.Matrix([sum(u[j]*sp.diff(u[i], coords[j]) for j in range(3))
                     for i in range(3)])
    lap = sp.Matrix([sum(sp.diff(u[i], q, 2) for q in coords) for i in range(3)])
    force = u.diff(t) + adv - nu*lap
    require(div == 0 and adv == sp.zeros(3, 1), "solenoidal shear/advection")
    require(sp.simplify(force[0] - (sp.diff(a,t)+nu*k*k*a)*sp.sin(k*y)) == 0,
            "prescribed NS residual")
    kinetic = sp.integrate(u.dot(u)/2, (y, 0, 1))
    dissipation = nu*sp.integrate(sum(sp.diff(ui, y)**2 for ui in u), (y, 0, 1))
    power = sp.integrate(force.dot(u), (y, 0, 1))
    require(sp.simplify(sp.diff(kinetic,t)+dissipation-power) == 0, "energy balance")
    require(sp.simplify(power-dissipation-a*sp.diff(a,t)/2) == 0, "power coefficient")
    # Negative control: non-potential force cannot be pure Newtonian gravity.
    curl_z = -sp.diff(force[0], y)
    require(sp.simplify(curl_z.subs({sp.diff(a,t): 0, a: 1, y: 0})) == -nu*k*k*k,
            "nonzero curl witness")
    # Nontrivial steady mean-zero velocity pays strictly positive dissipation.
    steady_power = sp.simplify(power.subs({sp.diff(a,t): 0, a: 1}))
    require(sp.simplify(steady_power - 2*sp.pi**2*nu) == 0, "steady power")
    return {"kinetic": str(kinetic), "dissipation": str(dissipation),
            "input_power": str(power), "energy_residual": "0",
            "steady_power_density_one": str(steady_power),
            "nonpotential_force_negative_control": "nonzero curl",
            "scope": "shear identity; not an upstream universal flow"}


def check_time_scaling() -> dict[str, Any]:
    """Fixed viscosity does not scale like inertial terms under a slow clock."""
    e, nu, k, a, ad = sp.symbols("e nu k a ad", positive=True)
    actual = e**2*ad + nu*e*k*k*a
    naive = e**2*(ad+nu*k*k*a)
    mismatch = sp.factor(actual-naive)
    require(sp.simplify(mismatch-nu*k*k*a*e*(1-e)) == 0, "fixed-nu scaling")
    require(mismatch.subs({e: sp.Rational(1,2), nu:1, k:1, a:1}) != 0,
            "reject naive force rescaling")
    t = sp.symbols("t", nonnegative=True)
    slow_speed = 1/(1+t)
    require(sp.integrate(slow_speed, (t, 0, t)) == sp.log(t+1), "onto logarithmic clock")
    finite_clock = sp.integrate(1/(1+t)**2, (t,0,sp.oo))
    require(finite_clock == 1, "bounded-clock negative control")
    require(sp.integrate(1/(1+t)**2, (t,0,sp.oo)) == 1, "integrable power bound")
    return {"force_scaling_mismatch": str(mismatch),
            "onto_clock": "log(1+t) -> infinity",
            "rejected_clock": "integral_0^infinity (1+t)^-2 dt = 1",
            "finite_work_bound": "|U|,|f| <= C/(1+t), fixed volume => integrable |U.f|",
            "scope": "does not bound controller energy or precision"}


def encode(word: tuple[int, ...], base: int = 8) -> Fraction:
    """Nearest tape symbol first; even digits, blank=0; trailing blanks agree."""
    if base < 4 or base % 2:
        raise ValueError("base must be even and at least four")
    if any(type(d) is not int or d < 0 or d > base-2 or d % 2 for d in word):
        raise ValueError("digits must be even integers between zero and base-2")
    return sum((Fraction(d, base**(j+1)) for j,d in enumerate(word)), Fraction(0))


def stack_step(left: tuple[int, ...], right: tuple[int, ...], write: int,
               direction: str, base: int = 8) -> tuple[Fraction, Fraction]:
    """The three affine tape-update formulas, NOT the reversible full recorder."""
    A, B = encode(left, base), encode(right, base)
    encode((write,), base)  # validate
    head = right[0] if right else 0
    left_head = left[0] if left else 0
    remainder = base*B-head
    if direction == "R":
        return (Fraction(write)+A)/base, remainder
    if direction == "S":
        return A, (Fraction(write)+remainder)/base
    if direction == "L":
        return base*A-left_head, (Fraction(left_head)+(Fraction(write)+remainder)/base)/base
    raise ValueError("direction must be L, S, or R")


def check_stack_formulas() -> dict[str, Any]:
    digits = (0,2,4,6)
    words = [tuple(w) for n in range(3) for w in itertools.product(digits, repeat=n)]
    cases = 0
    for left, right, write, direction in itertools.product(words, words, digits, ("L","S","R")):
        lh = left[0] if left else 0
        tail_r = right[1:]
        if direction == "R":
            expected = encode((write,)+left), encode(tail_r)
        elif direction == "S":
            expected = encode(left), encode((write,)+tail_r)
        else:
            expected = encode(left[1:]), encode((lh,write)+tail_r)
        require(stack_step(left,right,write,direction) == expected, "affine tape update")
        cases += 1
    for bad in ((1,), (8,), (-2,)):
        try:
            encode(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid tape digit accepted")
    try:
        stack_step((),(),0,"invalid")
    except ValueError:
        pass
    else:
        raise AssertionError("invalid direction accepted")
    return {"exact_cases": cases, "arithmetic": "Fraction, base 8, even digits",
            "scope": "finite affine-update regression, not a universal compiler proof"}


def check_precision_and_volume() -> dict[str, Any]:
    lam, mu = sp.symbols("lambda mu", positive=True)
    require(sp.simplify(sp.diag(lam,mu,1/(lam*mu)).det()) == 1, "normal compensation")
    require(sp.diag(2,3,1).det() != 1, "reject uncompensated sheet-to-volume map")
    gaps = []
    for n in (1,2,4,8,16):
        gap = encode((0,)*(n-1)+(2,))-encode((0,)*n)
        require(gap == Fraction(2, 8**n), "late-digit precision")
        gaps.append({"position":n, "gap":str(gap)})
    # A finite horizon can be controlled while no fixed positive error works forever.
    for N in range(1,16):
        eps_N = Fraction(1,2**(N+2))
        require(all(eps_N*2**n <= Fraction(1,4) for n in range(N+1)), "finite horizon")
    return {"volume_determinant": "lambda*mu/(lambda*mu)=1", "coding_gaps":gaps,
            "warning": "finite-prefix bounds do not prove one all-time error tolerance"}


def check_temporal_coordinate() -> dict[str, Any]:
    N, h = sp.symbols("N h", positive=True)
    b = sp.symbols("beta", real=True)
    g = sp.Matrix([[-N*N+h*b*b, h*b], [h*b,h]])
    ginv = sp.simplify(g.inv())
    require(sp.simplify(ginv[0,0]+1/(N*N)) == 0, "ADM dt covector")
    require(g[0,0].subs({N:1,h:1,b:2}) > 0, "vector/covector negative control")
    require(ginv[0,0].subs({N:1,h:1,b:2}) < 0, "dt remains timelike")
    return {"inverse_tt": str(ginv[0,0]),
            "scope": "local ADM identity; no CTC follows only if t is globally real-valued",
            "not_claimed": "no Einstein equation is solved"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="optional JSON evidence destination")
    args = parser.parse_args()
    evidence = {
        "schema": "family376-bridge-checks-v1",
        "spacetime_base_sha": SPACETIME_SHA, "math_source_sha": MATH_SHA,
        "python": platform.python_version(), "sympy": sp.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": {"shear_energy": check_shear_energy(), "time_scaling": check_time_scaling(),
                   "affine_tape": check_stack_formulas(), "precision_volume": check_precision_and_volume(),
                   "temporal_coordinate": check_temporal_coordinate()},
        "status": "all implemented checks passed",
        "not_proved": ["full Family 376 theorem or its complete Lean dependency closure",
                       "Einstein-fluid compiler", "positive Hadamard state on a new spacetime",
                       "SCEE solution", "CTC existence or CTC undecidability"]}
    text = json.dumps(evidence, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
