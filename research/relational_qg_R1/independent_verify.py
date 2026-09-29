"""Independent high-precision and spatial-discretization checks.
Does not import the forward prediction generator.
"""
from pathlib import Path
import json, hashlib
import mpmath as mp
import numpy as np
from scipy.special import roots_legendre
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parent
with mp.workdps(70):
    def ker(x):return mp.erf(x/2)/x if x else 1/mp.sqrt(mp.pi)
    def f(x):return 2*ker(3*x)-ker(4*x)-ker(2*x)
    lo,hi=mp.mpf('.5'),mp.mpf('.75')
    for _ in range(240):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    root=(lo+hi)/2
    assert abs(f(root))<mp.mpf('1e-60')
    d=mp.mpf('1')
    fourier=(2/mp.pi)*mp.quad(lambda k:mp.sin(k*d)/(k*d)*mp.exp(-k*k),[0,1,mp.inf])
    assert abs(fourier-ker(d))<mp.mpf('1e-55')
    details={'phase_zero_d_over_ell':mp.nstr(root,60),
             'phase_zero_residual':mp.nstr(f(root),12),
             'kernel_at_r_over_ell_1':mp.nstr(ker(d),50),
             'Fourier_error_at_1':mp.nstr(abs(fourier-ker(d)),12),
             'finite_packet_width_sigma_over_ell_0p05_node':mp.nstr(root*mp.sqrt(1+mp.mpf('.05')**2),35)}

# Infinite cubic lattice momentum dispersion; integrate within the first
# Brillouin zone (for the listed spacings it includes [0,8]^3).
# Gaussian tails outside [0,8]^3 are negligible; differences of potentials
# eliminate the zero-momentum singularity.
def lattice_phase_root(a,nquad):
    z,w=roots_legendre(nquad)
    k=(z+1)*4; w=w*4
    if a:
        sym=4*np.sin(a*k/2)**2/a**2
    else:
        sym=k*k
    yyzz=sym[:,None]+sym[None,:]
    wyz=w[:,None]*w[None,:]
    spectrum=[]
    for sx in sym:
        s=sx+yyzz
        spectrum.append(np.sum(wyz*np.exp(-s)/s))
    spectrum=np.asarray(spectrum)
    def phase(d):
        dc=2*np.cos(3*k*d)-np.cos(4*k*d)-np.cos(2*k*d)
        return 4/np.pi**2*np.dot(w*spectrum,dc)
    return float(brentq(phase,.5,.85,xtol=1e-13))

lattice=[]
for a,nq in [(0,96),(0,160),(.25,160),(.125,160),(.0625,160)]:
    val=lattice_phase_root(a,nq)
    lattice.append({'lattice_spacing_over_ell':a,'quadrature_per_axis':nq,'node_d_over_ell':val})
    print(lattice[-1])

fwd=json.loads((ROOT/'results.json').read_text())
assert abs(float(details['phase_zero_d_over_ell'])-fwd['quantum_phase']['phase_zero_d_over_ell'])<5e-14
assert abs(lattice[1]['node_d_over_ell']-float(details['phase_zero_d_over_ell']))<1e-7
out={'high_precision':details,'lattice_checks':lattice,'forward_results_sha256':hashlib.sha256((ROOT/'results.json').read_bytes()).hexdigest(),
     'all_assertions_passed':True,'scope':'Checks the defined weak-field model; not a proof of nonlinear general covariance or 3D phase emergence.'}
(ROOT/'verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(details)
