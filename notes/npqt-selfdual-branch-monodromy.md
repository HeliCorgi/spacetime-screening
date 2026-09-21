# NPQT Self-Dual Branch-Monodromy Gate

**Status:** NEW CALCULATION CANDIDATE. Priority is not claimed.

The local principal-plane construction now works for both purely-electric and
generic complex self-dual Weyl curvature near a nonzero type-D point.

This note tests whether that local eigenline can be promoted to a **global
Weyl-only branch choice** on the generic off-spherical curvature space.

The answer is no.

## 1. A single-valued Weyl loop with exchanging eigenlines

Let

[
t=s^2
]

and define the complex symmetric tracefree self-dual Weyl operator

[
mathcal W(t)
=
egin{pmatrix}
a&b&0\\
b&-a&0\\
0&0&0
end{pmatrix},
]

with

[
a=rac{1+t}{2},
qquad
b=rac{1-t}{2i}.
]

Then

[
a^2+b^2=t,
]

so

[
oxed{
mathcal W^2
=
operatorname{diag}(t,t,0).
}
]

Its characteristic polynomial is

[
oxed{
chi(lambda)
=
lambda(lambda^2-t).
}
]

For (t
eq0), the three eigenvalues are

[
{+sqrt t,-sqrt t,0},
]

and are distinct.

Because the matrix depends only on (t=s^2),

[
oxed{
mathcal W(s)=mathcal W(-s).
}
]

However the two nonzero rank-one spectral projectors are

[
P_pm
=
rac12
left(
Bpmrac{mathcal W}{s}
ight),
qquad
B=operatorname{diag}(1,1,0),
]

so

[
oxed{
P_+(-s)=P_-(s).
}
]

Analytic continuation once around

[
t=0
]

therefore returns to the same Weyl tensor while interchanging the two
eigenlines.

This is explicit eigenvalue/eigenprojector monodromy.

## 2. The ambiguity enters the Ricci target

Let a generic fixed Ricci probe be

[
Z=operatorname{diag}(z_1,z_2,z_3),
]

and define the complementary rank-two contractions

[
Theta_pm
=
rac12
operatorname{tr}
left[
(I-P_pm)Z
ight].
]

At

[
t=1,
]

the Weyl operator is

[
mathcal W(1)=operatorname{diag}(1,-1,0).
]

The two sheets give

[
Theta_+
=
rac{z_2+z_3}{2},
]

[
Theta_-
=
rac{z_1+z_3}{2},
]

hence

[
oxed{
Theta_+-Theta_-
=
rac{z_2-z_1}{2}.
}
]

For generic Ricci curvature this is nonzero.

Thus the branch ambiguity does not disappear when the projector is contracted
with the Ricci tensor.

## 3. The obstruction accumulates at the core

Multiply the whole loop by an arbitrary nonzero scale

[
epsilon:
qquad
mathcal W_epsilon
=
epsilonmathcal W.
]

The characteristic polynomial becomes

[
lambda
left(
lambda^2-epsilon^2t
ight),
]

but the projector exchange is unchanged.

Therefore the entire monodromy loop can be placed arbitrarily close to

[
mathcal W=0.
]

So every sufficiently small generic Weyl neighborhood of the maximally
symmetric core contains branch-exchange loops.

## 4. Consequence for representative design

The result is narrower than a no-go for all NPQT completions.

It establishes:

[
oxed{
	ext{a global branch-specific Weyl eigenline projector cannot by itself
define a single-valued 4D representative.}
}
]

The local type-D principal-plane construction is still valid in a
simply-connected patch where the isolated branch has been chosen.

What fails is promotion of that label to the whole generic curvature
neighborhood required by a covariant action.

A viable continuation must therefore do at least one of the following:

1. use a **permutation-symmetric** Weyl expression;
2. use mixed Weyl-Ricci data that selects the required spherical limit without
   reintroducing discontinuity;
3. avoid an eigenline/projector construction entirely.

Any mixed selection must still pass the (C^2) core gate, where both Weyl and
traceless Ricci data may vanish or become degenerate.

## 5. Relation to the self-dual local PASS

The previous note,

[
	ext{`notes/npqt-selfdual-principal-plane-extension.md`,}
]

showed that magnetic Weyl curvature is not a local problem near nonzero type
D.

The combined status is now:

[
oxed{
	ext{local spectral continuation: PASS}
}
]

but

[
oxed{
	ext{global Weyl-only branch selection: FAIL}.
}
]

This makes the next search target substantially more specific:

[
oxed{
	ext{permutation-symmetric or mixed-curvature extension of }W_2Theta.
}
]

## Reproducibility

Run

    python src/symbolic/npqt_selfdual_branch_monodromy.py

The script verifies:

- symmetry and tracelessness of the self-dual operator;
- its characteristic polynomial;
- exact projector exchange under (s	o-s) at fixed Weyl tensor;
- the resulting generic Ricci-contraction mismatch;
- persistence of the monodromy under arbitrary scaling toward the core.
