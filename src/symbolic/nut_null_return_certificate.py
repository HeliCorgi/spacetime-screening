#!/usr/bin/env python3
"""Integer interval certificate for a self-returning null ray in the NUT exterior.

No floating-point arithmetic, root finder, quadrature library, or external data
is used in the existence certificate. Intervals have rational endpoints with
fixed denominator 10**80. Every operation rounds outwards. Machin's formula and
Taylor remainders enclose pi and cosine; monotone Riemann sums enclose the only
integral. See notes/nut-null-return-obstruction.md for the geometric/microlocal
argument, which is NOT formalized by this program.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial, isqrt
import platform

SCALE = 10**80


def ceil_div(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError
    return -((-a) // b)


@dataclass(frozen=True)
class Interval:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError('reversed interval')

    @staticmethod
    def rational(n: int, d: int = 1) -> Interval:
        if d == 0:
            raise ZeroDivisionError
        return Interval(n*SCALE//d, ceil_div(n*SCALE, d))

    def __add__(self, other: Interval) -> Interval:
        return Interval(self.lo+other.lo, self.hi+other.hi)

    def __neg__(self) -> Interval:
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: Interval) -> Interval:
        return self + (-other)

    def __mul__(self, other: Interval) -> Interval:
        products = [a*b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return Interval(min(products)//SCALE, ceil_div(max(products), SCALE))

    def __truediv__(self, other: Interval) -> Interval:
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError('denominator interval contains zero')
        pairs = [(a*SCALE, b) for a in (self.lo, self.hi)
                 for b in (other.lo, other.hi)]
        return Interval(min(a//b for a, b in pairs),
                        max(ceil_div(a, b) for a, b in pairs))

    def __pow__(self, n: int) -> Interval:
        if n < 0:
            return ONE / (self**(-n))
        value, base = ONE, self
        while n:
            if n & 1:
                value = value*base
            base = base*base
            n //= 2
        return value

    def sqrt(self) -> Interval:
        if self.lo < 0:
            raise ValueError('negative square root interval')
        lower = isqrt(self.lo*SCALE)
        upper = isqrt(self.hi*SCALE)
        if upper*upper < self.hi*SCALE:
            upper += 1
        return Interval(lower, upper)

    def contains(self, value: Fraction) -> bool:
        return Fraction(self.lo, SCALE) <= value <= Fraction(self.hi, SCALE)

    def bounds(self, digits: int = 12) -> str:
        factor = 10**(80-digits)
        def dec(n: int) -> str:
            sign = '-' if n < 0 else ''
            n = abs(n)
            return f'{sign}{n//10**digits}.{n%10**digits:0{digits}d}'
        return f'[{dec(self.lo//factor)}, {dec(ceil_div(self.hi, factor))}]'


ZERO = Interval.rational(0)
ONE = Interval.rational(1)
TWO = Interval.rational(2)


def atan_reciprocal(q: int, terms: int = 64) -> Interval:
    """Alternating-series bound for atan(1/q), q >= 2."""
    if q < 2 or terms < 1:
        raise ValueError('invalid arctangent expansion')
    total = ZERO
    for k in range(terms):
        total = total + Interval.rational((-1)**k, (2*k+1)*q**(2*k+1))
    remainder = Interval.rational(1, (2*terms+1)*q**(2*terms+1))
    # Symmetric remainder is deliberately conservative.
    return total + Interval(-remainder.hi, remainder.hi)


def pi_interval() -> Interval:
    return (Interval.rational(16)*atan_reciprocal(5)
            - Interval.rational(4)*atan_reciprocal(239))


def cos_point(point: int) -> Interval:
    """Cosine at the exact rational point/SCALE, by Taylor's theorem."""
    u = Interval(point, point)
    if not 0 <= point <= 4*SCALE:
        raise ValueError('cosine argument outside certified range')
    u2 = u*u
    term, total = ONE, ONE
    degree = 40
    for k in range(1, degree+1):
        term = term*u2 / Interval.rational((2*k-1)*(2*k))
        total = total + (term if k % 2 == 0 else -term)
    # Degree 2*degree+1 Taylor polynomial (odd coefficients vanish).
    rem = u**(2*degree+2) / Interval.rational(factorial(2*degree+2))
    return total + Interval(-rem.hi, rem.hi)


def cosine(u: Interval, pi: Interval) -> Interval:
    if not (0 <= u.lo and u.hi <= pi.lo):
        raise ValueError('monotonic cosine interval must be within [0, pi]')
    # Cosine decreases on [0, pi].
    return Interval(cos_point(u.hi).lo, cos_point(u.lo).hi)


def arithmetic_controls() -> None:
    """Compare outward bounds to independent exact Fraction arithmetic."""
    values = [Fraction(n, d) for n, d in ((-7, 3), (-1, 7), (0, 1),
                                         (2, 9), (1, 1), (13, 5))]
    for a in values:
        ia = Interval.rational(a.numerator, a.denominator)
        assert ia.contains(a)
        for b in values:
            ib = Interval.rational(b.numerator, b.denominator)
            assert (ia+ib).contains(a+b)
            assert (ia-ib).contains(a-b)
            assert (ia*ib).contains(a*b)
            if b:
                assert (ia/ib).contains(a/b)
    for a in [Fraction(1, 7), Fraction(2), Fraction(8, 5), Fraction(49, 9)]:
        root = Interval.rational(a.numerator, a.denominator).sqrt()
        assert Fraction(root.lo, SCALE)**2 <= a <= Fraction(root.hi, SCALE)**2
    assert cos_point(0).contains(Fraction(1))
    for bad in (Interval(-1, 1), ZERO):
        try:
            _ = ONE/bad
        except ZeroDivisionError:
            pass
        else:
            raise AssertionError('zero-containing denominator was accepted')
    # Endpoints of non-point intervals, including a negative denominator.
    ia, ib = Interval.rational(-3)+Interval(0, SCALE), Interval(-5*SCALE, -2*SCALE)
    for a in (Fraction(ia.lo, SCALE), Fraction(ia.hi, SCALE)):
        for b in (Fraction(ib.lo, SCALE), Fraction(ib.hi, SCALE)):
            assert (ia/ib).contains(a/b)
            assert (ia*ib).contains(a*b)


def ray_data(j: Interval, pi: Interval) -> tuple[Interval, ...]:
    delta = Interval.rational(8, 5).sqrt()
    lam = delta/TWO
    c = j*j-ONE
    amplitude = ((c+ONE)*(c+Interval.rational(8, 5))).sqrt()
    half_length = Interval.rational(3)*pi/j  # three azimuthal turns
    angle = c.sqrt()*half_length
    x_end = (delta + amplitude*cosine(angle, pi))/c
    x_max = (delta+amplitude)/c
    return delta, lam, c, amplitude, half_length, angle, x_end, x_max


def closure_residual(j: Interval, pi: Interval, panels: int) -> Interval:
    delta, lam, c, amp, length, angle, _, _ = ray_data(j, pi)
    samples = []
    for k in range(panels+1):
        x = (delta+amp*cosine(angle*Interval.rational(k, panels), pi))/c
        assert x.lo > 2*SCALE
        # In the north-pole gauge t_N=t-lambda*phi and for a=lambda^2,
        # dt_N/dsigma=(x+delta)^2/(x^2-1)-lambda*j.
        f = (x+delta)**2/(x*x-ONE)-lam*j
        samples.append(f)
    left = sum((v.lo for v in samples[:-1]), 0)
    right = sum((v.hi for v in samples[1:]), 0)
    # x decreases, while d[(x+delta)^2/(x^2-1)]/dx < 0.
    # Hence the integrand increases and the two rectangle sums enclose it.
    integral = TWO*length*Interval(left, right)/Interval.rational(panels)
    return integral-Interval.rational(4)*pi*lam


def main() -> None:
    print(f'Python {platform.python_version()}; exact integer interval certificate')
    arithmetic_controls()
    pi = pi_interval()
    assert pi.lo > Interval.rational(314159, 100000).hi
    assert pi.hi < Interval.rational(314160, 100000).lo
    print('pi enclosure:', pi.bounds(30))
    left = Interval.rational(51, 50)  # 1.02
    right = Interval.rational(41, 40)  # 1.025
    entire = Interval(left.lo, right.hi)
    data = ray_data(entire, pi)
    assert data[2].lo > 0
    assert 0 < data[5].lo < data[5].hi < pi.lo
    assert data[6].lo > 2*SCALE
    assert data[7].hi < 64*SCALE
    assert (data[1]/entire).hi < SCALE
    print('Uniform lower-radius enclosure, j in [1.02,1.025]:', data[6].bounds())
    print('Uniform radial-maximum enclosure:', data[7].bounds())
    for panels in (256, 1024):
        fl = closure_residual(left, pi, panels)
        fr = closure_residual(right, pi, panels)
        assert fl.hi < 0 < fr.lo
        print(f'panels={panels}; F(1.02) in {fl.bounds()}; F(1.025) in {fr.bounds()}')
    print('CERTIFIED: continuity and opposite signs give a root j* in (1.02,1.025).')
    print('The entire null segment lies at x>2, returns in the Hopf quotient, and has opposite radial covectors.')
    print('No floating-point calculation entered the existence certificate.')
    print('The local-Hadamard obstruction uses the analytic propagation theorem in the note; not a Lean proof.')


if __name__ == '__main__':
    main()
