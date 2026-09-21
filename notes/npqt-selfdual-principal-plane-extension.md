# NPQT Self-Dual Principal-Plane Extension Toy

**Status:** NEW CALCULATION CANDIDATE. Priority is not claimed.

The previous local calculation in
`notes/npqt-principal-plane-spectral-extension.md` used a real
purely-electric Weyl matrix.  This note lifts the same construction to the
complex self-dual Weyl operator, so magnetic Weyl curvature is included at the
local algebraic level.

## 1. Self-dual Weyl operator

In four dimensions the Weyl tensor can be represented by its self-dual
operator

[
mathcal W
]

on the complex three-dimensional space of self-dual bivectors.  Its real and
imaginary parts encode the electric and magnetic Weyl tensors.

Consider the local split family

[
operatorname{spec}(mathcal W)
=
(-2ho,ho+delta,ho-delta),
]

with (ho) and (delta) allowed to be complex.

Define

[
a=operatorname{tr}(mathcal W^2),
qquad
b=operatorname{tr}(mathcal W^3).
]

Then

[
a=2(delta^2+3ho^2),
]

[
b=6ho(delta^2-ho^2).
]

## 2. Simple-eigenline projector

For the isolated simple eigenvalue

[
lambda_s=-2ho,
]

the spectral projector is

[
oxed{
P_s
=
rac{
mathcal W^2+lambda_smathcal W+
left(lambda_s^2-rac12aight)mathcal G
}{
3lambda_s^2-rac12a
}.
}
]

The denominator is

[
oxed{
9ho^2-delta^2.
}
]

At the type-D point

[
delta=0,
]

this becomes

[
9ho^2.
]

Therefore, for a non-conformally-flat type-D point

[
ho
eq0,
]

the simple self-dual eigenline and its complementary two-dimensional spectral
cluster continue analytically through sufficiently small generic complex
splittings.

This is the same local spectral-gap mechanism as in the purely-electric toy,
but it no longer assumes (B_{ab}=0).

## 3. Exact type-D invariant form

At exact type D,

[
a=6ho^2,
qquad
b=-6ho^3,
]

hence

[
oxed{
ho=-rac ba.
}
]

The simple-line projector becomes

[
oxed{
P_D
=
rac13
left(
mathcal G-rac{mathcal W}{ho}
ight)
=
rac13
left(
mathcal G+rac abmathcal W
ight).
}
]

The symbolic check also verifies the type-D minimal polynomial

[
oxed{
(mathcal W+2homathcal G)
(mathcal W-homathcal G)=0.
}
]

Ferrando and Sáez describe the same type-D geometry in terms of a normalized
canonical self-dual eigenbivector (mathcal U), with the real principal
(2+2) structure tensor

[
oxed{
Pi
=
2mathcal Ucdotar{mathcal U}.
}
]

Thus the simple self-dual eigenline determines the real Weyl principal
two-plane structure.  Once (mathcal U) is normalized, its remaining sign
freedom drops out of (Pi).

## 4. What this resolves

The previous handoff listed magnetic Weyl curvature as a separate local
obstruction to the principal-plane strategy.

This calculation sharpens that status:

[
oxed{
	ext{magnetic Weyl curvature does not obstruct the local spectral-gap
continuation near a nonzero type-D point.}
}
]

Equivalently, the local problem can be formulated directly in the self-dual
operator without choosing a purely-electric frame.

This is only a **local** result.

## 5. What remains open

The main unresolved gates are now:

1. a globally single-valued choice of the continuation across generic
   self-dual Weyl eigenvalue branch permutations;
2. Petrov II/III/N directions, where diagonalizable spectral-cluster logic can
   fail;
3. the conformally-flat core
   [
   ho	o0,
   ]
   where the spectral gap vanishes;
4. an explicit real four-index concomitant for the spacelike principal-plane
   projector suitable for insertion directly into the action;
5. proof that
   [
   T_{m ext}=W_2Theta_{m ext}
   ]
   admits a genuine (C^2) curvature extension through the core;
6. restoration and Hessian analysis of the complete cubic NPQT density.

The strongest remaining bottleneck is therefore no longer "include magnetic
Weyl" by itself.  It is the **global/core regularity of the principal-plane
selection**.

## Literature relation

J. J. Ferrando and J. A. Sáez develop intrinsic type-D descriptions in which
the canonical self-dual Weyl eigenbivector determines the principal (2+2)
structure, including explicit curvature concomitants:

- *On the classification of type D spacetimes*, arXiv:gr-qc/0212086;
- *An intrinsic characterization of 2+2 warped spacetimes*,
  arXiv:1005.1491;
- *Type D vacuum solutions: a new intrinsic approach*, arXiv:1309.4633.

These references support the exact type-D principal-structure step.  The
off-type-D open-neighborhood and (C^2) core-extension problem considered
here remains the repository's task.

## Reproducibility

Run

    python src/symbolic/npqt_selfdual_principal_plane_toy.py

The script checks:

- the complex self-dual spectral invariants;
- the simple-root projector;
- the gap (9ho^2-delta^2);
- the invariant type-D relation (ho=-b/a);
- the invariant exact-type-D projector;
- the type-D minimal polynomial.
