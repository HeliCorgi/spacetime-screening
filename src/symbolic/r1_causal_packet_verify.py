#!/usr/bin/env python3
"""Independent scalar/Fraction and Laplace-residue checks for the linear audit.

No forward module is imported. A supplied JSON is evidence to be checked, not
an input assumption. These tests do not certify a nonlinear Einstein solution.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def eye(n: int) -> list[list[F]]:
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def mul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    bt = transpose(b)
    return [[sum((x*y for x,y in zip(row,col)), F(0)) for col in bt] for row in a]


def rref(a: list[list[F]]) -> tuple[list[list[F]], list[int]]:
    out = [list(row) for row in a]
    pivots = []
    r = 0
    for c in range(len(out[0])):
        p = next((j for j in range(r,len(out)) if out[j][c]), None)
        if p is None:
            continue
        out[r], out[p] = out[p], out[r]
        divisor = out[r][c]
        out[r] = [x/divisor for x in out[r]]
        for j in range(len(out)):
            if j != r:
                scale = out[j][c]
                out[j] = [x-scale*y for x,y in zip(out[j],out[r])]
        pivots.append(c)
        r += 1
        if r == len(out):
            break
    return out, pivots


def inverse(a: list[list[F]]) -> list[list[F]]:
    n = len(a)
    aug = [row+unit for row,unit in zip(a,eye(n))]
    out, pivots = rref(aug)
    require(pivots[:n] == list(range(n)), "singular matrix rejected")
    return [row[n:] for row in out]


def determinant(a: list[list[F]]) -> F:
    n = len(a)
    result = F(0)
    for perm in itertools.permutations(range(n)):
        term = F((-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n):
            term *= a[i][perm[i]]
        result += term
    return result


def characteristic(a: list[list[F]]) -> list[F]:
    """Leibniz polynomial, constant coefficient first; no CAS charpoly call."""
    n = len(a)
    total = [F(0)]*(n+1)
    for perm in itertools.permutations(range(n)):
        p = [F((-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n)))]
        for i in range(n):
            factor = [-a[i][perm[i]], F(perm[i] == i)]
            q = [F(0)]*(len(p)+1)
            for r,x in enumerate(p):
                for s,y in enumerate(factor):
                    q[r+s] += x*y
            p = q
        total = [x+y for x,y in zip(total,p)]
    return total


def exact_checks() -> dict:
    # Different ordering from the forward calculation: E, B, P, v, d.
    A = [[F(x) for x in row] for row in
         [[0,-1,0,-2,0],[1,0,0,0,0],[0,0,-100,F(-1,10),0],
          [1,0,1,0,0],[0,0,0,1,0]]]
    reduced, pivots = rref(transpose(A))
    require(pivots == [0,1,2,3], "one invariant, with d free")
    J = [F(0)]*5
    J[4] = 1
    for row,pivot in zip(reduced,pivots):
        J[pivot] = -row[4]
    require(J == [F(0), F(-1000), F(10), F(1000), F(1)], "derived null covector")
    for h in (F(1,128),F(1,7),F(1,1000)):
        lo = [[F(i==j)-h*A[i][j]/2 for j in range(5)] for i in range(5)]
        hi = [[F(i==j)+h*A[i][j]/2 for j in range(5)] for i in range(5)]
        require(mul([J],mul(inverse(lo),hi))[0] == J, "Cayley preserves derived invariant")
    fake_reset = [F(-1), F(0), F(0), F(0), F(2,3)]
    require(sum(x*y for x,y in zip(J,fake_reset)) != 0, "retained exact reset rejected")
    reset_bound = F(201,100000)
    require(reset_bound < F(3,5), "near reset cannot hold target")

    tuples = [(F(1),F(1),F(1),F(1,1000),F(1,100)),
              (F(2),F(3),F(2),F(1,10),F(1)),
              (F(3,2),F(1,7),F(1,4),F(1,20),F(1,3))]
    for w,Q,k,mu,tau in tuples:
        a = [[F(x) for x in row] for row in
             [[0,-k,0,-2*Q],[k,0,0,0],[0,0,-1/tau,-mu*k/tau],[Q/w,0,k/w,0]]]
        coeff = [x*tau*w for x in characteristic(a)]
        a0,a1,a2,a3,a4 = coeff
        require(a3*a2-a4*a1 == mu*w*k*k, "independent Hurwitz minor 2")
        require(a3*a2*a1-a4*a1*a1-a3*a3*a0 == 2*mu*w*Q*Q*k*k,
                "independent Hurwitz minor 3")
        require(all(x > 0 for x in coeff), "strict modal damping assumptions")

    # Exact principal-minor tests for H(I+C) and H(I-C), including zero minors.
    C = [[F(x) for x in row] for row in [[0,0,0,1],[0,0,-1,0],[0,-1,0,0],[F(1,10),0,0,0]]]
    diag = [F(2),F(1),F(1),F(20)]
    count = 0
    for sign in (-1,1):
        matrix = [[diag[i]*(F(i==j)+sign*C[i][j]) for j in range(4)] for i in range(4)]
        require(matrix == transpose(matrix), "cone form symmetric")
        for length in range(1,5):
            for subset in itertools.combinations(range(4),length):
                minor = [[matrix[i][j] for j in subset] for i in subset]
                require(determinant(minor) >= 0, "cone form positive semidefinite")
                count += 1
    # In particular this field-energy cone test is not a DEC proof.
    return {"normalized_invariant":[str(J[i]) for i in (3,0,1,2,4)],
            "reset_displacement_bound":str(reset_bound), "cone_principal_minors":count,
            "hurwitz_parameter_checks":len(tuples)}


def independent_grid() -> dict:
    """Sparse scalar update, not the matrix code used by the forward check."""
    h, delta = F(1,8), F(1,16)
    zero = (F(0),)*4
    state = {0:(F(0),F(1),F(0),F(0))}  # v,E,B,P
    heat = F(0)
    diffusion = F(0)
    def energy(s: dict) -> F:
        return h*sum((v*v+(E*E+B*B)/2+10*P*P for v,E,B,P in s.values()),F(0))
    def source(s: dict) -> tuple[dict,F]:
        result = {}
        gain = F(0)
        den = 1+delta*delta/2
        for j,(v,E,B,P) in s.items():
            pn = (1-50*delta)/(1+50*delta)*P
            result[j] = (((1-delta*delta/2)*v+delta*E)/den,
                         (-2*delta*v+(1-delta*delta/2)*E)/den, B, pn)
            gain += h*2000*delta*((P+pn)/2)**2
        require(energy(s)-energy(result) == gain, "scalar source heat")
        return result, gain
    initial = energy(state)
    for step in range(1,7):
        state,gain = source(state); heat += gain
        old = state
        state = {}
        for j in range(-step,step+1):
            v0,e0,b0,p0 = old.get(j-1,zero)
            v1,e1,b1,p1 = old.get(j+1,zero)
            state[j] = ((v0+v1+p0-p1)/2,(e0+e1-b0+b1)/2,
                        (b0+b1-e0+e1)/2,(p0+p1+F(1,10)*(v0-v1))/2)
        loss = energy(old)-energy(state)
        require(loss >= 0, "scalar transport contraction")
        diffusion += loss
        state,gain = source(state); heat += gain
        require(energy(state)+heat+diffusion == initial, "independent total ledger")
    return {"initial_energy":str(initial),"heat":str(heat),"numerical_diffusion":str(diffusion)}


def laplace_samples() -> list[dict]:
    """Recover d,v,B,P from residues, without a matrix exponential."""
    with mp.workdps(80):
        tau,mu = mp.mpf(1)/100, mp.mpf(1)/1000
        coefficients = [tau,mp.mpf(1),3*tau+mu,mp.mpf(3),mu]
        roots = mp.polyroots(coefficients, maxsteps=1000, extraprec=100)
        derivative = [4*coefficients[0],3*coefficients[1],2*coefficients[2],coefficients[3]]
        require(all(mp.re(r) < 0 for r in roots), "numerical roots agree with algebraic Hurwitz proof")
        residues = [(tau*r+1)/mp.polyval(derivative,r) for r in roots]
        rows = []
        T = mp.pi/mp.sqrt(3)
        for label,t in [("pi/sqrt(3)",T),("2*pi/sqrt(3)",2*T),
                        ("1000",mp.mpf(1000)),("10000",mp.mpf(10000)),("60000",mp.mpf(60000))]:
            terms = [rr*mp.exp(r*t) for r,rr in zip(roots,residues)]
            d = mp.fsum(terms)
            v = mp.fsum(r*x for r,x in zip(roots,terms))
            P = mp.fsum(-mu*r*x/(1+tau*r) for r,x in zip(roots,terms))
            B = mp.fsum((r+mu/(1+tau*r))*x for r,x in zip(roots,terms))
            require(max(abs(mp.im(x)) for x in (d,v,P,B)) < mp.mpf("1e-60"), "real Laplace inversion")
            rows.append({"time":label,**{name:mp.nstr(mp.re(x),50) for name,x in
                                         [("d",d),("v",v),("P",P),("B",B)]}})
        return rows


def validate(evidence: dict, checks: dict, grid: dict, samples: list[dict]) -> None:
    require(evidence.get("schema") == "r1-causal-reset-v1", "schema mismatch")
    require(evidence.get("parent_sha") == "d679f9585cc89518981ce03f6075bab8fb5256fd", "parent mismatch")
    a = evidence["algebra"]
    require(a["benchmark_normalized_invariant"] == checks["normalized_invariant"], "invariant evidence mismatch")
    require(F(a["reset_displacement_bound"]) == F(checks["reset_displacement_bound"]), "reset bound mismatch")
    require(a["nonlinear_R1_certified"] is False, "unsupported nonlinear certification rejected")
    for key in ("initial_energy","heat","numerical_diffusion"):
        require(F(evidence["local_stencil"][key]) == F(grid[key]), "grid evidence mismatch: "+key)
    for got,want in zip(evidence["diagnostics"]["modal_samples"],samples,strict=True):
        require(got["time"] == want["time"], "time ordering mismatch")
        with mp.workdps(60):
            for key in ("d","v","P","B"):
                require(abs(mp.mpf(got[key])-mp.mpf(want[key])) < mp.mpf("1e-27"), "residue mismatch: "+key)
    require(evidence["negative_midpoint"]["causal_stencil"] is False, "acausal stencil misclassified")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence",type=Path)
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    checks,grid,samples = exact_checks(), independent_grid(), laplace_samples()
    if args.evidence:
        validate(json.loads(args.evidence.read_text(encoding="utf-8")),checks,grid,samples)
    result = {"schema":"r1-causal-reset-independent-v1","python":platform.python_version(),
              "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "exact":checks,"independent_grid":grid,"laplace_samples":samples,
              "forward_json_crosscheck":args.evidence is not None,
              "status":"all implemented independent checks passed",
              "not_certified":["nonlinear Einstein evolution","finite-time preparation",
                               "full nonlinear R1","universal embedding","CTC/Hadamard/RSET/SCEE"]}
    text = json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(text,end="")


if __name__ == "__main__":
    main()
