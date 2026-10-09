#!/usr/bin/env python3
"""Independent rational/interval checks for the closed-shear linear benchmark.

Standard library only. No import of the forward calculation. All interval
arithmetic rounds outwards to a fixed integer scale. Matrix-exponential
remainders use a submultiplicative norm and a geometric bound on the tail.
This encloses the specified constant-coefficient LINEAR model, not nonlinear GR.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import platform
from typing import Any

SCALE = 10**75
DIM = 5


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def ceiling(a: int, b: int) -> int:
    if b <= 0:
        raise ValueError("positive denominator required")
    return -((-a)//b)


@dataclass(frozen=True)
class Interval:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def rational(value: F | int) -> Interval:
        q = F(value)
        return Interval((q.numerator*SCALE)//q.denominator,
                        ceiling(q.numerator*SCALE,q.denominator))

    def __add__(self, other: Interval) -> Interval:
        return Interval(self.lo+other.lo,self.hi+other.hi)

    def __mul__(self, other: Interval) -> Interval:
        products = [self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return Interval(min(products)//SCALE,ceiling(max(products),SCALE))

    def widen(self, amount: F) -> Interval:
        if amount < 0:
            raise ValueError("negative enclosure radius")
        radius = ceiling(amount.numerator*SCALE,amount.denominator)
        return Interval(self.lo-radius,self.hi+radius)

    def contains(self, q: F) -> bool:
        return F(self.lo,SCALE) <= q <= F(self.hi,SCALE)

    def magnitude(self) -> F:
        return F(max(abs(self.lo),abs(self.hi)),SCALE)

    def width(self) -> F:
        return F(self.hi-self.lo,SCALE)

    def serial(self) -> dict[str,str]:
        return {"lo":str(F(self.lo,SCALE)),"hi":str(F(self.hi,SCALE))}


def zero_matrix() -> list[list[F]]:
    return [[F(0) for _ in range(DIM)] for _ in range(DIM)]


def identity() -> list[list[F]]:
    out = zero_matrix()
    for i in range(DIM):
        out[i][i] = F(1)
    return out


def multiply(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum((a[i][k]*b[k][j] for k in range(DIM)),F(0))
             for j in range(DIM)] for i in range(DIM)]


def exp_enclosure(a: list[list[F]], h: F, degree: int = 32) -> tuple[list[list[Interval]],F]:
    if h < 0 or degree < 1:
        raise ValueError("positive time and degree required")
    norm = max(sum(abs(q) for q in row) for row in a)
    z = h*norm
    require(z < degree+2, "Taylor tail ratio < 1")
    term = identity(); total = identity(); scalar = F(1)
    ah = [[q*h for q in row] for row in a]
    for n in range(1,degree+1):
        term = [[q/n for q in row] for row in multiply(term,ah)]
        total = [[total[i][j]+term[i][j] for j in range(DIM)] for i in range(DIM)]
        scalar *= z/n
    first_omitted = scalar*z/(degree+1)
    tail = first_omitted/(1-z/(degree+2))
    enclosed = [[Interval.rational(q).widen(tail) for q in row] for row in total]
    return enclosed,tail


def interval_action(a: list[list[Interval]], v: list[Interval]) -> list[Interval]:
    out = []
    for i in range(DIM):
        total = Interval(0,0)
        for j in range(DIM):
            total = total+a[i][j]*v[j]
        out.append(total)
    return out


def atan_inverse(n: int, terms: int = 70) -> tuple[F,F]:
    total = sum((F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(terms)),F(0))
    next_term = F((-1)**terms,(2*terms+1)*n**(2*terms+1))
    return min(total,total+next_term),max(total,total+next_term)


def gate_time_interval() -> tuple[F,F]:
    a,b = atan_inverse(5); c,d = atan_inverse(239)
    plo,phi = 16*a-4*d,16*b-4*c
    scale=10**90; root=isqrt(3*scale*scale)
    slo,shi=F(root,scale),F(root+1,scale)
    require(slo*slo < 3 < shi*shi, "sqrt(3) integer certificate")
    require(F(3)<plo<phi<F(22,7), "Machin pi bracket")
    return plo/shi,phi/slo


def algebra_and_uniform_bounds() -> dict[str,Any]:
    # State = (v, E, B, pi_xy, displacement). Q=1/2 z^T H z, excluding displacement.
    a = [[F(v) for v in row] for row in
         [[0,1,0,1,0],[-2,0,-1,0,0],[0,1,0,0,0],
          [F(-1,10),0,0,-100,0],[1,0,0,0,0]]]
    weights = [F(1),F(1,2),F(1,2),F(10)]
    for i in range(4):
        for j in range(4):
            lhs = weights[i]*a[i][j]+weights[j]*a[j][i]
            require(lhs == (F(-2000) if i==j==3 else 0), "rational energy symmetrizer")
    # Negative control: reverse the plasma current in Ampere's equation.
    require(weights[0]*F(1)+weights[1]*F(2) != 0, "reject sign-reversed current")
    ct=F(1,10); cl=F(1,3)+F(4,3)*ct
    require(0<ct<cl<1 and cl==F(7,15), "causal equilibrium speeds")
    require(F(1,3)+F(4,3)*F(1,1000)/F(1,10000)>1, "reject acausal relaxation")
    # Analytic proof in the note: |p| <= mu/sqrt(2), skew generator is a contraction.
    nu=F(1,1000); Tupper=F(66,35); omupper=F(7,4); sqrt2lower=F(7,5)
    require(F(5,3)**2<3<omupper**2 and sqrt2lower**2<2, "radical bounds")
    velocity=nu*Tupper*omupper/sqrt2lower
    time_derivative=nu*(Tupper+1/sqrt2lower)
    displacement=nu*F(22,7)**2/(4*sqrt2lower)
    require(max(velocity,time_derivative)==F(13,5000), "uniform scaled C1 bound")
    require(displacement<F(9,5000), "uniform displacement bound")
    return {"matrix":a, "C1_velocity_part":str(velocity),
            "C1_time_part":str(time_derivative),
            "displacement_relative_bound":str(displacement),
            "uniform_C1_bound":"13/5000", "rounded_displacement_bound":"9/5000"}


def nonlinear_symbol_bounds() -> dict[str,str]:
    """Rational margins used in the separate frozen-symbol proof."""
    delta=F(1,1000); alpha=F(1,10); longitudinal=F(7,15); c=F(15,2)
    radius=(longitudinal-alpha)/3
    defect=((F(5,3)+longitudinal)*delta+F(4,3)*delta**2)/(1-delta)
    projector=defect/(radius-defect)
    Hchange=delta+c*(2*delta+delta**2)
    lower=1-c*projector**2-Hchange
    upper=1-c+c*projector**2+Hchange
    require(defect==F(1601,749250), "acoustic norm bound")
    require(projector==F(1601,89974), "Riesz projection bound")
    require(lower>F(98,100) and upper<F(-648,100), "definite spectral subspaces")
    require(0<alpha-defect<longitudinal+defect<1, "causal squared-speed interval")
    require((1+4*delta)/3<1 and delta**2/alpha<F(1,2), "energy/entropy tube margins")
    # A visibly too-large tube must not pass this certificate.
    bad=F(1,2)
    bad_defect=((F(5,3)+longitudinal)*bad+F(4,3)*bad**2)/(1-bad)
    require(bad_defect>=radius, "reject unsupported large-stress tube")
    return {"stress_tube":"1/1000", "defect":str(defect),"projector":str(projector),
            "positive_signature_bound":str(lower),"negative_signature_bound":str(upper),
            "scope":"rational bounds for the rest-frame matrix lemma, not a nonlinear evolution bound"}


def check_rounding() -> None:
    for p in [F(-7,3),F(-1,17),F(0),F(1,3),F(9,2)]:
        require(Interval.rational(p).contains(p), "input outward rounding")
        for q in [F(-11,7),F(2,9),F(3)]:
            require((Interval.rational(p)*Interval.rational(q)).contains(p*q), "multiply rounding")
            require((Interval.rational(p)+Interval.rational(q)).contains(p+q), "add rounding")
    try:
        Interval(1,0)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid interval accepted")


def certified_endpoint(a: list[list[F]]) -> dict[str,Any]:
    h=F(1,128); Tlo,Thi=gate_time_interval()
    m=int(Tlo/h)
    require(int(Thi/h)==m and m==232, "unique final step index")
    step,tail=exp_enclosure(a,h)
    z=[Interval.rational(q) for q in [0,1,0,0,0]]
    max_width=F(0)
    for _ in range(m):
        z=interval_action(step,z)
        max_width=max(max_width,max(q.width() for q in z))
    restlo,resthi=Tlo-m*h,Thi-m*h
    middle=(restlo+resthi)/2
    partial,partial_tail=exp_enclosure(a,middle)
    norm=max(sum(abs(q) for q in row) for row in a)
    require(norm*resthi<1, "short final-step exponential bound")
    # Mean-value estimate for the tiny exact time bracket, with exp(x)<=1/(1-x).
    timing_error=(resthi-restlo)/2*norm/(1-norm*resthi)*max(q.magnitude() for q in z)
    endpoint=[q.widen(timing_error) for q in interval_action(partial,z)]
    require(max(q.width() for q in endpoint)<F(1,10**30), "endpoint enclosure sufficiently narrow")
    # This shows a nonzero stored displacement at gate readout, not a persistent memory.
    require(F(endpoint[4].lo,SCALE)>F(3,5), "nontrivial displacement witness")
    require(endpoint[0].hi<0, "viscous endpoint is NOT an exact stop")
    return {"time_lo":str(Tlo),"time_hi":str(Thi), "full_steps":m, "step":str(h),
            "Taylor_degree":32, "step_norm_tail":str(tail),
            "max_grid_width":str(max_width), "time_uncertainty_error":str(timing_error),
            "endpoint":[q.serial() for q in endpoint], "_intervals":endpoint}


def decimal_string(q: F, precision: int = 12) -> str:
    with localcontext() as ctx:
        ctx.prec=precision
        return str(Decimal(q.numerator)/Decimal(q.denominator))


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence",type=Path,help="optional forward JSON for an end-to-end check")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    check_rounding()
    bounds=algebra_and_uniform_bounds()
    matrix=bounds.pop("matrix")
    cert=certified_endpoint(matrix)
    enclosed=cert.pop("_intervals")
    crosscheck=False
    if args.evidence:
        evidence=json.loads(args.evidence.read_text(encoding="utf-8"))
        require(evidence.get("schema")=="r1-closed-shear-v1", "evidence schema")
        values=evidence["diagnostics"]["endpoint"]
        require(len(values)==DIM, "endpoint dimension")
        # Printed forward values have 35 significant digits; this allowance covers print rounding only.
        for box,value in zip(enclosed,values):
            require(box.widen(F(1,10**33)).contains(F(value)), "independent endpoint enclosure")
        require(evidence["relaxation"]["nonlinear_viscous_causality_proved"] is False,
                "do not upgrade linear checks to nonlinear causality")
        crosscheck=True
    result={"schema":"r1-closed-shear-independent-v1", "python":platform.python_version(),
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "arithmetic":"Fraction plus outward fixed-integer intervals; no floating input",
            "uniform_bounds":bounds,"nonlinear_rest_symbol":nonlinear_symbol_bounds(),"certificate":cert,"forward_json_crosscheck":crosscheck,
            "endpoint_width_max":decimal_string(max(q.width() for q in enclosed)),
            "status":"all independent linear checks passed",
            "not_certified":["nonlinear Einstein evolution", "nonlinear positive-viscosity closure",
                             "quantitative nonlinear remainder", "Hadamard/RSET/SCEE/CTC"]}
    text=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(text,end="")


if __name__=="__main__":
    main()
