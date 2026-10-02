"""Render the analytic coefficient region and selected members (not an extremum scan)."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent


def make_figures():
    b=np.linspace(0,1/3,1200)
    root=np.maximum(1-3*b,0)**1.5
    low=np.maximum(0,(9*b-2-2*root)/27)
    high=np.maximum(0,(9*b-2+2*root)/27)
    fig,ax=plt.subplots(figsize=(8.4,5.0))
    ax.fill_between(b,low,high,alpha=.25,label='Allowed positive-factor class')
    ax.plot(b,high,linewidth=1.2)
    ax.plot(b,low,linewidth=1.2)
    ax.plot([.25,1/3],[0,1/27],linestyle='none',marker='o')
    ax.annotate(r'R4: $(b,c)=(1/4,0)$',xy=(.25,0),xytext=(.125,.009),
                arrowprops={'arrowstyle':'->'})
    ax.annotate(r'Equal three factors: $(1/3,1/27)$',xy=(1/3,1/27),
                xytext=(.085,.036),arrowprops={'arrowstyle':'->'})
    ax.plot([0],[0],marker='x',linestyle='none')
    ax.set(xlabel=r'$b$',ylabel=r'$c$',xlim=(-.006,.345),ylim=(-.002,.041),
           title=r'R5: exact coefficient region for $A(z)=1+z+bz^2+cz^3$')
    ax.text(.03,.65,'At least two positive factors; origin excluded.\nThis is NOT a full-gravity stability region.',
            transform=ax.transAxes)
    ax.legend(loc='upper left');ax.grid(alpha=.25);fig.tight_layout()
    fig.savefig(HERE/'allowed_region.png',dpi=160)

    def kernel(x,kind):
        if kind=='two_equal':
            y=x*np.sqrt(2);return (-np.expm1(-y)-np.exp(-y)*y/2)/x
        if kind=='three_equal':
            y=x*np.sqrt(3);return (-np.expm1(-y)-np.exp(-y)*(5*y/8+y*y/8))/x
        a=float(kind);b=1-a
        return (1-(a*np.exp(-x/np.sqrt(a))-b*np.exp(-x/np.sqrt(b)))/(a-b))/x
    x=np.linspace(.004,1.5,1000)
    fig2,ax2=plt.subplots(figsize=(8.4,5.0))
    for kind,label in [('two_equal',r'$(1/2,1/2,0)$: R4 kernel'),
                       ('three_equal',r'$(1/3,1/3,1/3)$'),
                       ('0.99',r'$(0.99,0.01,0)$'),
                       ('0.9999',r'$(0.9999,0.0001,0)$')]:
        y=2*kernel(3*x,kind)-kernel(4*x,kind)-kernel(2*x,kind)
        ax2.plot(x,y,label=label)
    ax2.axhline(0,linewidth=.8,linestyle='--')
    ax2.set(xlabel=r'$d/\ell$',ylabel=r'$\ell\,\Delta K$',
            title='R5: a phase reversal survives, but its location is not universal')
    ax2.grid(alpha=.25);ax2.legend(loc='lower left');fig2.tight_layout()
    fig2.savefig(HERE/'phase_family.png',dpi=160)
    return fig,fig2


if __name__=='__main__':
    make_figures()
