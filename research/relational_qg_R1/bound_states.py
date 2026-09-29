"""s-wave two-body predictions of the same Gaussian-resolved potential.
Units: r/ell, E * mu*ell**2 / hbar**2, g=mu*G*mA*mB*ell/hbar**2.
"""
from pathlib import Path
import json, numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import erf
R=Path(__file__).resolve().parent
rows=[]
for g in [.1,1.,10.,100.]:
    runs=[]
    for n in [4000,8000]:
        xmax=max(20/g,12.)
        h=xmax/(n+1)
        x=h*np.arange(1,n+1)
        V=-g*erf(x/2)/x
        diag=1/h**2+V; off=np.full(n-1,-.5/h**2)
        e,u=eigh_tridiagonal(diag,off,select='i',select_range=(0,0),tol=1e-11)
        assert e[0]>=-g/np.sqrt(np.pi)-1e-8
        runs.append({'n':n,'xmax':xmax,'ground_energy':float(e[0]),'rms_radius_over_ell':float(np.sqrt(np.sum(x*x*u[:,0]**2)))})
    rows.append({'g':g,'Coulomb_ground_energy':-g*g/2,
                 'finite_potential_lower_bound':-g/np.sqrt(np.pi),
                 'large_g_harmonic_plus_quartic':-g/np.sqrt(np.pi)+1.5*np.sqrt(g/(6*np.sqrt(np.pi)))-9/64,
                 'runs':runs,'refinement_energy_difference':abs(runs[1]['ground_energy']-runs[0]['ground_energy'])})
    print(rows[-1])
(R/'bound_states.json').write_text(json.dumps({'dimensionless_radial_H':'-1/2 d^2/dx^2-g erf(x/2)/x',
        'boundary_conditions':'u(0)=u(xmax)=0; normalized reduced radial wavefunction',
        'rows':rows,'scope':'Nonrelativistic two-body weak-metric regime; not a black-hole-collapse calculation.'},indent=2)+'\n')
