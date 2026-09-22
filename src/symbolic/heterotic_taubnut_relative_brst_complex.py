#!/usr/bin/env python3
"""Relative Abelian oscillator cohomology, NOT full heterotic string BRST.

Assume an allowed charge sector and free matter/auxiliary Heisenberg modules
with levels K and -K. After an invertible change of variables, each nonzero
mode/gauge direction is a quartet with Q=x*d_b+c*d_y. The homotopy
H=b*d_x+y*d_c obeys {Q,H}=N_occ. We check the actual exterior signs,
nilpotency, homotopy and ghost-resolved cohomology ranks through grade 3.
The algebraic homotopy proves oscillator acyclicity at every finite grade
IN THIS ASSUMED MODULE. It does not construct its global embedding, GSO,
superconformal BRST, physical pairing, or a string source.

Also enumerate the restricted neutral, unflowed, affine-primary necessary
labels at k1=8,k2=4. No full-spectrum membership is inferred.
"""
from __future__ import annotations

from collections import defaultdict
import platform
import sympy as sp

State = tuple[tuple[int, ...], int]
Vector = dict[State, int]


def labels() -> list[tuple[int, sp.Rational, sp.Rational]]:
    k = sp.Matrix([[8, 4], [4, 5]])
    assert k.det() == 24
    assert k - k.T == sp.zeros(2)
    delta, lam = sp.sqrt(sp.Rational(8, 5)), sp.sqrt(sp.Rational(2, 5))
    assert sp.simplify(8*(delta**2-1)-2*(4-delta**2)) == 0
    assert sp.simplify(8*delta*lam-2*(4-delta*lam)) == 0
    assert sp.simplify(4+8*lam**2-2*(5-1-lam**2)) == 0
    assert sp.Rational(3*8, 8-2)+sp.Rational(3*4, 4+2) == 6
    result = []
    for twice_l in range(5):
        ell = sp.Rational(twice_l, 2)
        for n in range(1, twice_l+1):
            if (twice_l-n) % 2:
                continue
            s2 = sp.Rational(5, 8)*n*n-ell*(ell+1)-sp.Rational(1, 4)
            if s2 <= 0:
                continue
            omega = n/(2*lam)
            assert sp.simplify(-n+delta*omega) == 0
            assert sp.simplify(lam*omega-sp.Rational(n, 2)) == 0
            # The left compact weight must be half-integral when ell is.
            left_m = sp.Rational(twice_l % 2, 2)
            assert abs(left_m) <= ell and (ell-left_m).is_integer
            assert (ell-sp.Rational(n, 2)).is_integer
            numerator_h = (sp.Rational(1, 4)+s2+ell*(ell+1))/6
            charge = sp.Matrix([-n, 0])
            subtraction = (charge.T*k.inv()*charge)[0]/2
            assert sp.simplify(numerator_h-subtraction) == 0
            result.append((n, ell, s2))
    assert result == [(2, sp.Rational(1), sp.Rational(1, 4)),
                      (3, sp.Rational(3, 2), sp.Rational(13, 8)),
                      (4, sp.Rational(2), sp.Rational(15, 4))]
    return result


def basis(grade: int) -> list[State]:
    # Two U(1) directions at each positive mode number <= grade.
    weights = [n for n in range(1, grade+1) for _ in range(2)]
    output: list[State] = []

    def visit(i: int, rest: int, powers: tuple[int, ...], mask: int) -> None:
        if i == len(weights):
            if rest == 0:
                output.append((powers, mask))
            return
        w = weights[i]
        for x in range(rest//w+1):
            for y in range(rest//w-x+1):
                for b in (0, 1):
                    for c in (0, 1):
                        cost = w*(x+y+b+c)
                        if cost <= rest:
                            visit(i+1, rest-cost, powers+(x, y),
                                  mask | (b << (2*i)) | (c << (2*i+1)))
    visit(0, grade, (), 0)
    return output


def differential(vector: Vector, homotopy: bool = False,
                 graded: bool = True) -> Vector:
    out: dict[State, int] = defaultdict(int)
    for (powers, mask), coefficient in vector.items():
        for i in range(len(powers)//2):
            # (boson index, ghost index, remove ghost?).
            terms = ((2*i, 2*i, False), (2*i+1, 2*i+1, True)) if homotopy else (
                (2*i, 2*i, True), (2*i+1, 2*i+1, False))
            for boson, ghost, remove in terms:
                bit = 1 << ghost
                present = bool(mask & bit)
                if (remove and not present) or (not remove and present):
                    continue
                p = list(powers)
                factor = 1
                if remove:
                    p[boson] += 1
                else:
                    factor = p[boson]
                    if not factor:
                        continue
                    p[boson] -= 1
                sign = -1 if graded and (mask & (bit-1)).bit_count() % 2 else 1
                out[(tuple(p), mask ^ bit)] += coefficient*factor*sign
    return {s: c for s, c in out.items() if c}


def add(a: Vector, b: Vector) -> Vector:
    out: dict[State, int] = defaultdict(int, a)
    for state, value in b.items():
        out[state] += value
    return {s: c for s, c in out.items() if c}


def ghost_number(state: State) -> int:
    powers, mask = state
    return sum(((mask >> (2*i+1)) & 1)-((mask >> (2*i)) & 1)
               for i in range(len(powers)//2))


def check_complex(grade: int) -> tuple[int, int, int]:
    states = basis(grade)
    groups: dict[int, list[State]] = defaultdict(list)
    for state in states:
        groups[ghost_number(state)].append(state)
        v = {state: 1}
        assert differential(differential(v)) == {}
        anti = add(differential(differential(v, True)),
                   differential(differential(v), True))
        occupation = sum(state[0])+state[1].bit_count()
        assert anti == ({state: occupation} if occupation else {})
    ranks = {}
    for g, domain in groups.items():
        target = groups.get(g+1, [])
        index = {s: i for i, s in enumerate(target)}
        q = sp.zeros(len(target), len(domain))
        for j, state in enumerate(domain):
            for dest, value in differential({state: 1}).items():
                q[index[dest], j] = value
        ranks[g] = q.rank()
    cohomology = {g: len(v)-ranks.get(g, 0)-ranks.get(g-1, 0)
                  for g, v in groups.items()}
    assert all(dim == (1 if grade == 0 and g == 0 else 0)
               for g, dim in cohomology.items())
    return len(states), sum(ranks.values()), sum(cohomology.values())


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}')
    print('Necessary primary labels (n, ell, s^2):', labels())
    print('Relative oscillator complex: grade / dimension / Q rank / H dimension')
    results = [check_complex(grade) for grade in range(4)]
    assert results == [(1, 0, 1), (8, 4, 0), (40, 20, 0), (160, 80, 0)]
    for grade, result in enumerate(results):
        print(grade, *result)
    # A deliberately wrong commuting-ghost implementation must be detected.
    state: State = ((0, 0, 0, 0), (1 << 0) | (1 << 2))
    assert differential(differential({state: 1}, graded=False), graded=False)
    print('Negative control: dropping exterior signs breaks Q^2=0, as expected.')
    print('PASS specified relative-module assertions; full_string_BRST_certified=False')


if __name__ == '__main__':
    main()
