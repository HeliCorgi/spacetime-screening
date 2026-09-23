"""Four-dimensional Ellis throat: exact tensor checks and scoped source tests.

Sources: Ford--Roman gr-qc/9510071 (47)--(51); Gonzalez--Guzman--Sarbach
0806.0608 (34)--(35); Fewster--Eveson gr-qc/9805024 (5.5).
The short-sampling QEI comparison is a local-flat diagnostic, not an exact
curved-spacetime bound. No time-shifted global solution is asserted.
"""
from __future__ import annotations

import platform
import sympy as s
import mpmath as mp


def exact_geometry() -> None:
    t, x, th, ph = s.symbols("t x theta phi", real=True)
    b, G = s.symbols("b G", positive=True)
    coords = (t, x, th, ph)
    r2 = x*x + b*b
    metric = s.diag(-1, 1, r2, r2*s.sin(th)**2)
    inv = metric.inv()
    dim = 4
    gamma = [[[s.simplify(sum(inv[a, d]*(s.diff(metric[d, c], coords[e])
                 + s.diff(metric[d, e], coords[c])-s.diff(metric[c, e], coords[d]))
                 for d in range(dim))/2) for e in range(dim)]
                 for c in range(dim)] for a in range(dim)]
    ric = s.zeros(dim)
    for a in range(dim):
        for c in range(dim):
            ric[a, c] = s.simplify(sum(
                s.diff(gamma[d][a][c], coords[d])-s.diff(gamma[d][a][d], coords[c])
                + sum(gamma[d][d][e]*gamma[e][a][c]-gamma[d][c][e]*gamma[e][a][d]
                      for e in range(dim)) for d in range(dim)))
    assert ric == s.diag(0, -2*b*b/r2**2, 0, 0)
    scalar = s.simplify(s.trace(inv*ric))
    assert scalar == -2*b*b/r2**2
    ein = s.simplify(ric-metric*scalar/2)
    frame = s.diag(1, 1, 1/s.sqrt(r2), 1/(s.sqrt(r2)*s.sin(th)))
    source = s.simplify(frame*ein*frame/(8*s.pi*G))
    A = b*b/(8*s.pi*G*r2**2)
    assert source == s.diag(-A, -A, A, A)
    assert s.simplify(source[0, 0]+source[1, 1]) == -2*A
    # Covariant conservation of the full tensor, not just its density.
    mixed = s.simplify(inv*ein/(8*s.pi*G))
    for c in range(dim):
        div = sum(s.diff(mixed[a, c], coords[a]) for a in range(dim))
        div += sum(gamma[a][a][d]*mixed[d, c]-gamma[d][a][c]*mixed[a, d]
                   for a in range(dim) for d in range(dim))
        assert s.simplify(div) == 0
    volume_energy = s.integrate(-A*4*s.pi*r2, (x, -s.oo, s.oo))
    radial_anec = s.integrate(-2*A, (x, -s.oo, s.oo))
    assert s.simplify(volume_energy+s.pi*b/(2*G)) == 0
    assert s.simplify(radial_anec+1/(8*G*b)) == 0
    # Ghost completion is explicit, and its kinetic sign is not hidden.
    psi = s.atan(x/b)/s.sqrt(4*s.pi*G)
    assert s.simplify(s.diff(r2*s.diff(psi, x), x)) == 0
    dpsi = s.Matrix([s.diff(psi, q) for q in coords])
    standard = dpsi*dpsi.T-metric*(dpsi.T*inv*dpsi)[0]/2
    assert s.simplify(ein/(8*s.pi*G)+standard) == s.zeros(4)
    assert s.simplify(ein/(8*s.pi*G)-standard) != s.zeros(4)
    print("EXACT 4D: all Einstein components, conservation, ghost completion and null integral.")
    print("rho=pr=-b^2/[8pi G(x^2+b^2)^2], pt=-rho; integral Tkk dx=-1/(8Gb).")
    print("Proper-volume matter energy=-pi*b/(2G), NOT ADM mass or construction work.")


def exact_bounds() -> None:
    y = s.symbols("y", real=True)
    g = 2/s.sqrt(3)*s.cos(s.pi*y/2)**2
    assert s.integrate(g*g, (y, -1, 1)) == 1
    d2 = s.simplify(s.integrate(s.diff(g, y, 2)**2, (y, -1, 1)))
    assert d2 == s.pi**4/3
    # g is extended by zero, in H^2; use smooth H^2 approximation in the QEI.
    qei_const = s.simplify(d2/(16*s.pi**2))
    assert qei_const == s.pi**2/48
    # Reproduce a published 4D ghost-gravity perturbation result, not a new theorem.
    trial = 1/(1+y*y)
    potential = -3/(1+y*y)**2
    norm = s.integrate(trial**2, (y, -s.oo, s.oo))
    energy = s.integrate(s.diff(trial, y)**2+potential*trial**2,
                         (y, -s.oo, s.oo))
    assert s.simplify(energy/norm) == -s.Rational(11, 8)
    print("QEI sampler: integral g''^2=pi^4/(3 T^4); flat 4D rho_average>=-N*pi^2/(48 T^4).")
    print("PUBLISHED STABILITY BOUND reproduced: omega_min^2<=-11/(8 b^2).")
    print("Instability is NOT a proof that every single signal is destroyed or all active control is impossible.")



def thin_shell_and_smoothing() -> None:
    b, eps, G = s.symbols("b eps G", positive=True)
    x = s.symbols("x", real=True)
    # Israel junction: intrinsic coordinates (time,theta,phi).
    jump = s.diag(0, 2/b, 2/b)
    shell_mixed = -(jump-s.eye(3)*s.trace(jump))/(8*s.pi*G)
    sigma, pressure = -shell_mixed[0,0], shell_mixed[1,1]
    assert s.simplify(sigma+1/(2*s.pi*G*b)) == 0
    assert s.simplify(pressure-1/(4*s.pi*G*b)) == 0
    assert s.simplify(sigma+pressure) == -1/(4*s.pi*G*b)
    # Smooth 4D regularization of r=b+|x|, rather than a delta-source QEI.
    radius = b+s.sqrt(x*x+eps*eps)-eps
    rp, rpp = s.diff(radius,x), s.diff(radius,x,2)
    rho = (1-rp**2-2*radius*rpp)/(8*s.pi*G*radius**2)
    pr = (rp**2-1)/(8*s.pi*G*radius**2)
    pt = rpp/(8*s.pi*G*radius)
    assert s.simplify(rho.subs(x,0)-(1-2*b/eps)/(8*s.pi*G*b*b)) == 0
    assert s.simplify(pr.subs(x,0)+1/(8*s.pi*G*b*b)) == 0
    assert s.simplify(pt.subs(x,0)-1/(8*s.pi*G*b*eps)) == 0
    assert s.simplify(s.diff(pr,x)+2*rp/radius*(pr-pt)) == 0
    print("EXACT 4D shell: sigma=-1/(2pi Gb), p=1/(4pi Gb); required exotic shell source is not supplied.")
    print("SMOOTH collar r=b+sqrt(x^2+eps^2)-eps keeps a finite separate layer scale eps.")
    print("Local-flat necessary diagnostic for eps<<b: eps^3 <= N*pi^3*lP^2*b/(12 f^4). Not a sufficiency theorem.")

def scales(dps: int) -> tuple:
    with mp.workdps(dps):
        # Nominal SI values, NOT measured to dps digits: c,h exact, G uncertain.
        cl = mp.mpf(299792458)
        hb = mp.mpf("6.62607015e-34")/(2*mp.pi)
        grav = mp.mpf("6.67430e-11")
        lp = mp.sqrt(hb*grav/cl**3)
        f = mp.mpf("0.01")
        bmax = mp.sqrt(mp.pi**3/6)*lp/f**2
        b = mp.mpf(1)
        rho = -cl**4/(8*mp.pi*grav*b*b)
        proper_E = -mp.pi*cl**4*b/(2*grav)
        source_ratio = (b/bmax)**2
        e_fold = mp.sqrt(mp.mpf(8)/11)*b/cl
        zeta = mp.sqrt(3)-mp.sqrt(2)
        n = 2*zeta*zeta/(1+zeta*zeta)
        m = mp.sqrt(2)*zeta/(1+zeta*zeta)
        neg_const = 4*(m-n)/mp.pi**2
        packet_width = (8*mp.pi*neg_const)**mp.mpf("0.25")*mp.sqrt(lp*b)
        epsmax = (mp.pi**3*lp**2*b/(12*f**4))**(mp.mpf(1)/3)
        vals = (bmax, rho, proper_E, source_ratio, e_fold, packet_width, epsmax)
        print(f"dps={dps}; LOCAL-FLAT diagnostic, N=1,f=.01: b_max={mp.nstr(bmax, 14)} m")
        print(f"  b=1m: rho={mp.nstr(rho, 12)} J/m^3; proper integral={mp.nstr(proper_E, 12)} J")
        print(f"  required/QEI magnitude={mp.nstr(source_ratio, 12)}; ghost e-fold upper={mp.nstr(e_fold, 12)} s")
        print(f"  point-density-matching 4D packet width={mp.nstr(packet_width, 12)} m, duration={mp.nstr(packet_width/cl, 12)} s")
        print(f"  separate thin-layer diagnostic: eps_max={mp.nstr(epsmax,12)} m (necessary only)")
        assert source_ratio > mp.mpf("1e60")
        assert packet_width < mp.mpf("1e-16")*b
        return vals


def main() -> None:
    print(f"Python {platform.python_version()}; SymPy {s.__version__}; mpmath {mp.__version__}")
    exact_geometry()
    exact_bounds()
    thin_shell_and_smoothing()
    v50, v80 = scales(50), scales(80)
    with mp.workdps(85):
        assert all(abs(a-b) < mp.mpf("1e-45")*max(abs(b), mp.mpf("1e-90"))
                   for a, b in zip(v50, v80))
    print("PASS 4D geometry/source/stability algebra and numerical reproducibility.")
    print("Curved QEI corrections, topology creation, moved-mouth matching and active stabilization are NOT solved.")


if __name__ == "__main__":
    main()
