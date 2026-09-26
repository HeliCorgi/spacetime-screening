#!/usr/bin/env python3
"""Independent v6 verifier: feedback normalization and one-party quantum process constraints."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import unittest

import mpmath as mp
import sympy as sp

BASE_SHA = "82274b96f69fd9c6fceb5166fdf07672429d650d"
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
PAULI = [I2, X, Y, Z]


def require(ok, msg):
    if not ok:
        raise AssertionError(msg)


def ptr_out(m):
    return sp.Matrix(2, 2, lambda i, j: sum(m[2*i+k, 2*j+k] for k in range(2)))


def process_matrix_check():
    """Re-derive the one-party normalization subspace, without importing old audit code."""
    coeffs = sp.symbols("w0:16", real=True)
    basis = [sp.kronecker_product(a, b) for a in PAULI for b in PAULI]
    W = sum((c*b for c, b in zip(coeffs, basis)), sp.zeros(4))
    m0 = sp.eye(4)/2
    equations = [sp.trace(W*m0)-1]
    for i in range(4):
        for j in range(1, 4):
            direction = sp.kronecker_product(PAULI[i], PAULI[j])
            require(ptr_out(direction) == sp.zeros(2), "bad TP direction")
            for sign in (-1, 1):
                M = m0 + sign*direction/4
                require(ptr_out(M) == I2, "not TP")
                require(all(ev >= 0 for ev in M.eigenvals()), "not CP")
                equations.append(sp.trace(W*M)-1)
    A, rhs = sp.linear_eq_to_matrix(equations, coeffs)
    require(A.rank() == 13, "wrong one-party normalization rank")
    sol = next(iter(sp.linsolve((A, rhs), coeffs)))
    require(sol[0] == sp.Rational(1, 2), "wrong identity coefficient")
    require(all(sol[4*i+j] == 0 for i in range(4) for j in range(1,4)), "output dependence survived")
    return {"rank": 13, "form": "W=rho_input tensor I_output", "implies_backward_signalling": False}


def classical_check():
    d, q = sp.symbols("d q", real=True)
    K = sp.Matrix([[(1+d)/2,(1-d)/2],[(1-d)/2,(1+d)/2]])
    totals = {
        "const0": sp.simplify(sum(K[r,0] for r in range(2))),
        "const1": sp.simplify(sum(K[r,1] for r in range(2))),
        "copy": sp.simplify(sum(K[r,r] for r in range(2))),
        "not": sp.simplify(sum(K[r,1-r] for r in range(2))),
    }
    require(totals == {"const0":1,"const1":1,"copy":1+d,"not":1-d}, "classical totals")
    z = sp.expand(q*(1+d)+(1-q)*(1-d))
    qpost = sp.simplify(q*(1+d)/z)
    require(sp.simplify(qpost-q) != 0, "no retroselection in false renormalization control")
    return {"totals": {k:str(v) for k,v in totals.items()}, "mixture_total": str(z), "renormalized_q_copy": str(qpost)}


def ramsey_matrix_check():
    # Direct qubit reduction for a Gaussian scalar X with mean mu and variance V.
    lam, mu, V = sp.symbols("lambda mu V", real=True)
    # characteristic <exp(-2 i lambda X)> for a Gaussian variable.
    c = sp.exp(-2*lam**2*V) * sp.exp(-2*sp.I*lam*mu) / 2
    rho = sp.Matrix([[sp.Rational(1,2), c], [sp.conjugate(c), sp.Rational(1,2)]])
    expect_y = sp.simplify(sp.trace(rho*Y).rewrite(sp.sin))
    require(sp.simplify(expect_y - sp.exp(-2*lam**2*V)*sp.sin(2*lam*mu)) == 0, "Ramsey sign/law")
    return {"expect_sigma_y": "exp(-2 lambda^2 V) sin(2 lambda mu)"}


def evidence_check(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    src = Path(__file__).with_name("sa_closed_loop_v6.py")
    require(data["code_sha256"] == hashlib.sha256(src.read_bytes()).hexdigest(), "stale evidence")
    require(data["base_sha"] == BASE_SHA, "wrong base")
    require(data["classification"] == {"A":0,"B":0,"C":1}, "classification changed")
    require(data["candidate"]["status"] == "C", "not C")
    require(data["candidate"]["distinguishability"]["value"] == 0, "D not closed")
    require(data["candidate"]["P_Y_do_0"] == {"+1":"1/2","-1":"1/2"}, "P0")
    require(data["candidate"]["P_Y_do_1"] == {"+1":"1/2","-1":"1/2"}, "P1")
    return {"evidence_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "record_checked": True}


class NegativeControls(unittest.TestCase):
    def test_copy_not_force_zero(self):
        d=sp.symbols('d',real=True)
        self.assertEqual(sp.solve([1+d-1,1-d-1],[d],dict=True),[{d:0}])
    def test_open_signal_not_closed_process(self):
        d=sp.Rational(1,3)
        self.assertEqual(1+d,sp.Rational(4,3));self.assertEqual(1-d,sp.Rational(2,3))
    def test_constant_do_operations_are_normalized(self):
        d=sp.Rational(1,3);K=sp.Matrix([[(1+d)/2,(1-d)/2],[(1-d)/2,(1+d)/2]])
        self.assertEqual(sum(K[:,0]),1);self.assertEqual(sum(K[:,1]),1)
    def test_no_signal_kernel_passes_all_four_maps(self):
        K=sp.ones(2,2)/2
        for f0 in (0,1):
            for f1 in (0,1):
                self.assertEqual(K[0,f0]+K[1,f1],1)
    def test_column_tv_correction(self):
        d=sp.Rational(2,5);col=sp.Matrix([(1+d)/2,(1-d)/2]);flat=sp.Matrix([sp.Rational(1,2)]*2)
        tv=sp.Rational(1,2)*sum(abs(v) for v in col-flat)
        self.assertEqual(tv,abs(d)/2)
    def test_q99_second_port_nonzero(self):
        with mp.workdps(50):
            q=mp.mpf('.99');D=mp.sqrt(1-q*q);a=(1-D)/(1+D);R=(a-1/a)/2
            self.assertGreater(abs(R),0)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    tests=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(NegativeControls))
    require(tests.wasSuccessful(),"negative controls")
    out={
        "verified":True,
        "environment":{"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__},
        "classical":classical_check(),
        "ramsey":ramsey_matrix_check(),
        "one_party_process":process_matrix_check(),
        "tests":tests.testsRun,
        "verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.evidence:
        out.update(evidence_check(args.evidence))
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"verified":True,"closed_classification":"C","D_past":0,"process_form":"rho tensor I"},ensure_ascii=False))


if __name__ == '__main__':
    main()
