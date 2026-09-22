# Heterotic Taub–NUT: interactions, backreaction, and an operational return test

**Date:** 2026-09-22.  
**Status:** calculated diagnostics and a corrected evidence boundary, **not** an interacting time-machine construction or a chronology-protection theorem.

Baseline: PR #4, branch `heterotic-taubnut-fable-independent-audit`, commit `2a05752a0c8dd77829fa26c5701b31a24c143f18`.

This note supersedes the physical interpretations of the earlier **D3/D4 PASS** labels in `heterotic-taubnut-explicit-brst-state.md`, `heterotic-taubnut-transmission-amplitude.md`, and `heterotic-taubnut-time-travel-decision.md`. It does not discard their reproducible arithmetic. In particular, **0.998130316... is a radial-ODE flux fraction, not a probability of travelling into the past and not an established exact string amplitude.**

## 1. Executive result

Three new calculations can be stated without assuming the conclusion.

1. For the proposed factorized, zero-spectator-momentum vertex, the free left spectator current makes the same-polarization sphere three-point function vanish. Its four-current factor is nonzero. This selects an elastic four-point function and mixed couplings to other fields as the next interaction tests; it does not remove interactions.
2. A precisely defined **nonderivative neutral-scalar radial contact overlap** is finite: `I4 = 0.45476328` in the normalization below. This rules out a divergence of that particular overlap, not a string-amplitude divergence.
3. In a regular horizon chart, two counter-streaming null sources with nonvanishing limiting coefficients give an invariant `T_ab T^ab ~ (x-1)^(-2)`. Their center-of-mass energy also grows without bound in the fixed-background approximation. This is a conditional instability/backreaction diagnostic. The actual quantum source, its production, and the response of the coupled string background have not been calculated.

The operational question is still undecided. There is no computed finite, controllable earlier-reception probability. There is also no proof that every admissible state necessarily produces the dangerous counter-stream.

### Correction to the previous construction

The anomaly equations, the proposed gauge-charge cancellation, and the conformal-weight arithmetic are useful **necessary-condition checks**. They did not establish all of the following: the global asymmetric-coset Hilbert space, auxiliary left/right gluing, full superconformal BRST conditions, a critical modular-invariant heterotic completion, a positive physical inner product, and a normalizable preparation with specified global continuation.

A grade-zero argument for non-exactness is conditional on the correctly specified relative complex and its allowed states. A principal-continuous representation of the parent algebra does not by itself establish the no-ghost theorem for the asymmetric heterotic quotient. The BRST and AdS3 results in [2,3] are methods and comparison results, not a substitute for that missing application.

Accordingly the previous object is retained as an **algebraic vertex candidate**, not rejected as nonexistent and not certified as a complete physical string state. Likewise real-ODE Wronskian conservation is not a proof of unitarity of quantum evolution on the CTC spacetime. The original background paper itself separates its exact geometry calculation from the full-CFT probe/backreaction problem [1, discussion in section 4].

## 2. Inputs and normalization

Use the nonrotating source metric/dilaton of [1, equations (72)–(79)], in a local angular gauge:

```math
p=x^2-1,\qquad D=(x+\delta)^2-\frac{4p}{k+2},\qquad K=(k-2)\alpha'>0,
```
```math
ds^2=K\left[\frac{dx^2}{p}-\frac{p}{D}(dt-\lambda\cos\theta\,d\phi)^2
+d\theta^2+\sin^2\theta\,d\phi^2\right],\quad
\Phi=\Phi_0-\frac14\log D,\quad t\sim t+4\pi\lambda.
```

The source uses string units; restoring the overall positive length-squared factor does not affect the dimensionless flux ratio. Numerical overlap calculations use these units. We restrict those calculations to `x>1`, `D>0`.

Retain the previous numerical point as a diagnostic input:

```math
k=8,\quad \delta=\sqrt{8/5},\quad\lambda=\sqrt{2/5},\quad
\omega=\sqrt{10}/2,\quad\Lambda=1.
```

The neutral dilaton-weighted scalar equation is

```math
(pR')'+\left(\omega^2D/p-\Lambda\right)R=0.
```

This is an equation derived from the given target fields. It is not being asserted to include all finite-level string two-point normalization, string oscillators, or interaction effects.

Set `u=(x-1)/2`, `a_+=omega(1+delta)/2`, `a_-=omega(delta-1)/2` and

```math
a=\tfrac12-i(\omega+\tfrac12),\quad b=\tfrac12-i(\omega-\tfrac12),\quad
c=1-i(\omega+2).
```
```math
R_H=u^{-ia_+}(1+u)^{ia_-}\,{}_2F_1(a,b;c;-u),\qquad
B_{\rm in}=\frac{\Gamma(c)\Gamma(-i)}{\Gamma(a)\Gamma(c-b)},\qquad R=R_H/B_{\rm in}.
```

For the stated infinity basis this gives unit incident radial flux. Independent numerical differentiation, rather than only substitution of an asserted identity, gives relative ODE residuals below `2e-35` at `u=0.03,0.5,2,10` and the constant radial current

```math
J_x=\frac{p}{2i}(R^*R'-RR'^*)=-0.998130316064461877\ldots.
```

The previous radial reflection/transmission arithmetic is reproduced. This does **not** select a cosmological Taub vacuum or a physical continuation across a Cauchy horizon.

## 3. Interaction test I: a real spectator selection rule

Consider the proposed factorized vertex schematically,

```math
V_{-1}=c\bar c\,e^{-\bar\varphi}J_Y\,\bar\psi^Y\,\Phi_{\rm candidate},
\qquad J_Y=i\partial Y_L,
```

where `Y` is a decoupled free neutral spectator and all external spectator momenta/windings are zero. Assume the coset factor carries no `Y` dependence. Normalize `⟨J_Y(z)J_Y(w)⟩=1/(z-w)^2`.

The Gaussian Wick rule gives exactly

```math
\langle J_1J_2J_3\rangle=0,
```

so the sphere amplitude with three such same-spectator-polarization vertices vanishes through its left factor. Right picture changing does not alter this left-factor selection rule under the stated factorization.

But

```math
\langle J_1J_2J_3J_4\rangle=
\frac1{z_{12}^2z_{34}^2}+\frac1{z_{13}^2z_{24}^2}+\frac1{z_{14}^2z_{23}^2},
```

which equals `49/144` at `(z1,z2,z3,z4)=(0,1,2,4)`. Thus an elastic choice `V,V†,V,V†` is not excluded by this spectator rule. Other charge, picture, and kinematic constraints still have to be imposed.

Mixed amplitudes `V,V†,V_I`, with `V_I` a graviton/dilaton or another sourced field, need not vanish: their spectator factor can contain just two `J_Y` insertions. **Vanishing of the identical-polarization cubic does not eliminate gravitational backreaction.**

### The actual amplitude still needed

A sphere four-point amplitude has the schematic structure

```math
\mathcal A^{(0)}_4=g_0^2\int_{\mathcal M_{0,4}}d^2z\;
\mathcal I_{\rm ghosts,pictures,Y}(z,\bar z)\,
\langle\Phi_1\Phi_2\Phi_3\Phi_4\rangle_{\rm heterotic\ coset},
\qquad g_0=e^{\Phi_0}.
```

The exact coset blocks, projections/holonomy integrals, global continuation, normalization, and degenerating-modulus prescriptions are not supplied by the radial ODE. They have **not** been computed here. The corresponding genus-one amplitude brings two additional powers of `g0` for normalized closed-string external states, but its coefficient may be singular. This counting alone does not establish perturbative control [4].

A useful warning is [5]: in a different Misner string model some three-point processes are finite while certain four-point channels diverge. That result prevents inferring interaction safety from one finite low-order diagnostic; it is not a Taub–NUT amplitude calculation.

## 4. Interaction test II: finite nonderivative radial overlap

To test one elementary possible radial divergence, define the **diagnostic**, not an asserted heterotic coupling,

```math
I_4=\int_1^\infty dx\,|R(x)|^4=2\int_0^\infty du\,|R_H(u)/B_{\rm in}|^4.
```

The neutral-scalar string-frame measure has `e^{-2Phi}sqrt(|g|)` independent of `x`; angular, time, normalization, and coupling factors have been stripped. This is what a nondifferentiated scalar contact term would require radially. No claim is made that such a contact term with nonzero coefficient exists in this heterotic effective action.

At `u→0`, the leading modulus is finite. At infinity `R=O(u^{-1/2})` times bounded logarithmic oscillations, so `|R|^4=O(u^{-2})`. Both endpoints are integrable. With `r=log u`, 35-digit mpmath quadrature gives:

| Integration range in r | I4 with that cutoff |
|---|---:|
| [-12,12] | 0.4547501046708584278392961079 |
| [-20,20] | 0.4547632717030126224542716946 |
| [-28,28] | 0.4547632756913135498452269382 |

A supported displayed value is

```math
I_4\simeq0.45476328.
```

At cutoff 28, leading lower-tail and upper-envelope estimates are approximately `1.07e-13` and `1.64e-12`; these are asymptotic estimates, not certified interval error bounds. The eight displayed decimals are supported by the convergence comparison.

**What survives:** this particular overlap is not divergent. **What does not follow:** a finite string four-point function, a finite derivative coupling, a positive physical norm, or absence of particle production. In particular, derivative interactions can respond to the counter-streaming invariant in the next section.

## 5. Backreaction test: an invariant counter-streaming obstruction

A divergent frequency seen by a static observer is not enough to diagnose a singular horizon: that observer can have divergent acceleration. Instead use a regular chart and a scalar contraction.

On the radial fibre define `v=t+r_*` with `r_*'=sqrt(D)/p`. Then

```math
ds^2_{\rm fib}=K\left[-\frac pD dv^2+\frac{2}{\sqrt D}dv\,dx\right].
```

The chart determinant is `-K^2/D`, finite at `x=1`. The null covectors

```math
\ell=dv,\qquad n=du=dv-\frac{2\sqrt D}{p}dx
```

satisfy

```math
\ell^2=n^2=0,\qquad\ell\cdot n=-\frac{2D}{Kp}.
```

The same contraction holds in the full local angular coframe when `dt` is replaced by `eta=dt-lambda cos(theta)dphi`. The code verifies this. The angular coframe need not be globally an exact eikonal gradient; no global null-fluid solution is inferred from this local algebra.

Now **assume** two incoherent geometric-optics beams with covariant stress

```math
T_{ab}=A\ell_a\ell_b+B n_a n_b,\qquad A,B\geq0.
```

Direct contraction gives

```math
\boxed{T_{ab}T^{ab}=\frac{8AB D^2}{K^2p^2}.}
```

If both `A` and `B` tend to nonzero limits at the same future horizon,

```math
T_{ab}T^{ab}\sim\frac{2AB(1+\delta)^4}{K^2(x-1)^2}.
```

For null momenta proportional to `omega_i ell` and `omega_o n`,

```math
\boxed{s_{\rm cm}=\frac{4\omega_i\omega_oD}{Kp}
\sim\frac{2\omega_i\omega_o(1+\delta)^2}{K(x-1)}.}
```

These are invariant growth statements, not coordinate-frequency artifacts. With `A` finite and nonzero, keeping the stress invariant bounded requires `B=O((x-1)^2)` or stronger suppression in this coframe normalization. Wavepacket envelope/transport equations decide whether that condition holds.

### What the assumption does and does not buy

The formula gives a **conditional perturbative instability**, not a solved backreacted spacetime. One must actually determine the beams/envelopes from an admissible state, interactions, and boundary conditions. A purely regular ingoing branch has `B=0` and avoids this particular contraction divergence. Its null stress is not zero merely because its quadratic invariant is zero.

The earlier horizon-ingoing scattering solution contains reflected and incident pieces at **infinity**, while remaining purely ingoing at the chosen future horizon. Its nonzero reflection coefficient does not prove `A B != 0` at that horizon. No unavoidable two-stream source has been established here.

At finite `k`, extrapolating a low-energy source through arbitrarily large `alpha' s_cm` is uncontrolled. The divergence identifies where that approximation needs replacement; it does not specify whether the exact response is a barrier, particle production, a new background, or something else. Time-dependent orbifold backreaction provides a concrete comparison [6], not a theorem transferable without checking the Taub–NUT embedding.

## 6. Small string coupling is not a uniform backreaction bound

For the input dilaton,

```math
g_s(x)=g_0D^{-1/4},\qquad D'=2\frac{k-2}{k+2}x+2\delta.
```

For `k>2, delta>=1, x>=1`, `D'>0`. Therefore

```math
g_s(x)\leq g_{s,h}=\frac{g_0}{\sqrt{1+\delta}}
=0.664468539595557\ldots\,g_0
```

at the numerical point. Arbitrarily small `g0` avoids a dilaton strong-coupling wall in this first NUT region. It does **not** bound high-relative-boost interaction coefficients or infinite image sums.

The local near-horizon radial geometry is Rindler with rapidity coordinate `t/(1+delta)`. One target identification gives a boost

```math
b=\frac{4\pi\lambda}{1+\delta}=3.509043131417429\ldots,\qquad e^b=33.41627749505308\ldots.
```

This is a geometric holonomy statement, not the introduction of a new physical integer winding sector. If, **as a separate toy assumption**, independent image overlaps generate `epsilon_n=epsilon_0 exp(n b)`, the first `epsilon_n>=1` occurs at `n=4,8,16` for `epsilon_0=10^-6,10^-12,10^-24`. The script checks this recurrence only. `epsilon_0` is not a specified value of `g_s^2`; impact parameters, dimensional reduction, and state preparation are not fixed. These are not predictions of how many time-machine circuits can be made. No exact image sum for the asymmetric coset is derived.

### A further invariant cost of a short chronology orbit

For a fixed-position timelike `t` orbit in the string-frame metric,

```math
a^2=\frac p{4K}\left(\frac{p'}p-\frac{D'}D\right)^2,\qquad
\tau_{\rm loop}^2=(4\pi\lambda)^2Kp/D.
```

Near `x=1`,

```math
a^2\sim\frac1{2K(x-1)},\quad\tau_{\rm loop}\to0,\quad
a^2\tau_{\rm loop}^2\to b^2.
```

Thus the arbitrarily short fixed-radius circuit limit requires divergent proper acceleration. This is a property of this orbit family, not a proof that every possible worldline or string process fails.

## 7. What an actual g_s backreaction computation requires

The full problem is not the equation `g_s(x)<1`. A classical/coherent string-field expansion has schematically

```math
Q\Psi+\frac{g_0}{2}\ell_2(\Psi,\Psi)+\cdots=0,\quad
\Psi=\varepsilon\Psi_1+\varepsilon^2\Psi_2+\cdots,
```
```math
Q\Psi_2=-\frac{g_0}{2}\ell_2(\Psi_1,\Psi_1).
```

The products, pictures and normalization must be those of a defined heterotic theory; [7] supplies the structural closed-string-field framework, not those model-specific data. Solving this equation requires the source to satisfy the relevant cohomological solvability conditions. Nonvanishing projections can signal tadpoles, a background shift, radiation, or obstruction to the assumed perturbative family; they are not automatically chronology protection.

In target-space language one needs the renormalized stress and accompanying dilaton, antisymmetric-tensor and gauge-field sources, then their coupled response. Computing only a neutral scalar stress cannot establish that response. For an incoherent one-string preparation the appropriate expectation values must replace a presumed coherent classical field.

**Not calculated here:** the genus-one tadpoles; the exact mixed three-point coefficients sourcing those fields; an all-alpha'-consistent interacting kernel; a perturbed metric/dilaton/B/gauge solution. The two-stream formula is a conditional source diagnostic, not any of these solutions.

## 8. The operational return observable

### 8.1 The radial channels do not fix a time-travel direction

At the future horizon of the advanced chart, `xi=partial_v` is future null. For a future causal tangent `U`,

```math
g(U,\xi)\big|_{x=1}=\frac{K}{1+\delta}U^x\leq0.
```

Thus this chart's future-directed crossing has `U^x<=0`. The opposite regular horizon chart has the opposite cross-term sign. Real-ODE reciprocity cannot replace the choice of horizon, time orientation and global extension needed for a Taub-to-NUT preparation or a return itinerary.

A related logical check is worth stating explicitly. If a globally chronology-preserving event `p` can send a future causal influence to `q in I^-(p)`, concatenating with `q<<p` makes `p<<p`. The original premise then fails. This is the definition of chronology, not a new no-go theorem. It forces any proposed return protocol to specify its globally chronology-violating region and extension instead of calling the preparation both globally chronal and on a causal loop.

### 8.2 Periodicity and detector response are not backward messages

The identity `exp(-i omega 4 pi lambda)=1` merely identifies the same point/phase. A mode repeating after a coordinate period does not exhibit a sender-controlled earlier bit. Likewise detecting a CTC-associated background is not evidence of operational past signaling. Detector studies can distinguish such backgrounds even when causal access to the CTC region is absent [8].

A useful operational target is the difference

```math
\Delta P_B=P(b\mid\mathrm{do}(a_1),\mathcal P)-P(b\mid\mathrm{do}(a_0),\mathcal P),
```

where both settings use the same allowed preparation `P`, the sender and receiver are relationally located, and the receiver reads out earlier than the sender operation on a specified reference-clock segment. Both choices must be admissible under the global dynamics; postselecting a different self-consistent history for each setting is not by itself a communication experiment.

In a detector approximation the leading signaling term, for detector preparations that permit this order, is schematically

```math
S_{BA}\propto\lambda_A\lambda_B\int d\tau_A d\tau_B\,
\chi_A\chi_B\,F_{AB}\,
\langle[\widehat{\mathcal O}(\gamma_B),\widehat{\mathcal O}(\gamma_A)]\rangle.
```

Here `F_AB` contains detector coherences and phases; the kernel is the appropriate field commutator/causal response, not the radial Wronskian. The distinction between commutator-controlled signaling and energy transport is explicit in [9]. In quantum gravity the operators and clocks need gauge-invariant relational dressing; a BRST worldsheet correlator does not alone supply target-space localized detector operations.

On a CTC background one must specify a globally consistent response prescription and state. Do not impose an ordinary retarded theta function using periodic `t` and then infer causality from that chosen definition. KRW [10] obstructs the usual Hadamard extension for a linear scalar under its compactly generated Cauchy-horizon hypotheses. It explains why smooth individual modes do not automatically supply the required two-point state. It is not a full heterotic/string-loop theorem, and applicability to a selected global extension must be checked.

**Result:** the criterion for an operational return is now explicit, but its kernel and nonzero earlier-reception probability have not been calculated. A finite radial transmission fraction supplies neither.

## 9. Decision and the smallest missing computation

| Statement | Result and scope |
|---|---|
| Existing radial ODE and 0.998130316... flux fraction | Reproduced mathematically, not a time-travel probability |
| Complete positive-norm heterotic BRST state | Candidate only; previous unqualified PASS withdrawn |
| Same-Y, zero-spectator-momentum sphere cubic | Vanishes by a spectator Wick selection rule |
| Four-spectator-current factor | Nonzero; full coset amplitude not determined |
| Nonderivative scalar radial overlap | Finite, I4 about 0.45476328 |
| Small dilaton coupling in first NUT region | Available by choosing small g0; not a uniform interaction bound |
| Two finite counter-streams at one horizon | Conditional invariant stress/energy growth; source production not established |
| Exact interacting amplitude or backreacted barrier | Not calculated |
| Controllable earlier-reception observable | Defined as a test; nonzero result not established |
| Past-directed time travel in this theory | Neither demonstrated nor universally excluded by this analysis |

The next useful calculation is **not** another flux normalization or an arbitrary large simulation. It is to fix the actual coset vertex/state and normalization, then compute the elastic four-point function and mixed three-point source coefficients with an explicit global continuation. Their factorization and source projections decide whether the two-stream hazard is generated or avoided. Only a controlled result there supports a loop calculation and the relational signaling test.

This note supplies concrete conditional positive and negative tests. It does not infer a probability for a theory being true, a universal impossibility theorem, or an operational time machine.

## 10. Reproduction and audit trail

New files:

- `src/symbolic/heterotic_taubnut_interaction_backreaction_audit.py`
- `src/numerical/heterotic_taubnut_contact_overlap.py`
- `notes/data/heterotic_taubnut_contact_overlap.json`

Commands:

```sh
python src/symbolic/heterotic_taubnut_interaction_backreaction_audit.py
python src/numerical/heterotic_taubnut_contact_overlap.py --output notes/data/heterotic_taubnut_contact_overlap.json
```

Both scripts were executed successfully in the working environment: **Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0**. Numerical precision is 35 decimal digits; reported overlap precision is deliberately lower. The prior head's CI run #94 was successful; that is not claimed as CI evidence for these new files. Subsequent CI must be identified by its new commit.

The symbolic tests verify their explicit assumptions and algebra, not representation-theoretic or global physical claims. Existing scripts and historical notes are retained for auditability; this note and the updated PR description supersede their unqualified physical interpretations.

## 11. Primary references and scope

[1] C. V. Johnson and H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, Phys. Rev. D 70 (2004) 126011. [arXiv:hep-th/0405141](https://arxiv.org/abs/hep-th/0405141). Metric/dilaton equations (72)–(79); section 4 distinguishes geometry from probes/backreaction. The paper's all-alpha' background is input, not a completed interaction analysis.

[2] S. Hwang and H. Rhedin, *The BRST formulation of G/H WZNW models*. [arXiv:hep-th/9305174](https://arxiv.org/abs/hep-th/9305174). General coset BRST technology; not a ready-made no-ghost/completion theorem for this specific asymmetric heterotic model.

[3] J. Maldacena and H. Ooguri, *Strings in AdS3 and the SL(2,R) WZW Model. Part 1: The Spectrum*. [arXiv:hep-th/0001053](https://arxiv.org/abs/hep-th/0001053). Parent-spectrum/no-ghost comparison with a different string background.

[4] D. Tong, *Lectures on String Theory*. [arXiv:0908.0333](https://arxiv.org/abs/0908.0333). Perturbative worldsheet framework and genus counting.

[5] M. Berkooz, B. Durin, B. Pioline and D. Reichmann, *Closed Strings in Misner Space: Stringy Fuzziness with a Twist*. [arXiv:hep-th/0407216](https://arxiv.org/abs/hep-th/0407216). Finite lower-point and divergent higher-point processes in a different orbifold; comparison only.

[6] G. T. Horowitz and J. Polchinski, *Instability of Spacelike and Null Orbifold Singularities*. [arXiv:hep-th/0206228](https://arxiv.org/abs/hep-th/0206228). Large-boost/backreaction mechanism in specified orbifolds; not a Taub–NUT heterotic no-go.

[7] B. Zwiebach, *Closed String Field Theory: Quantum Action and the B-V Master Equation*. [arXiv:hep-th/9206084](https://arxiv.org/abs/hep-th/9206084). Structural interaction/solvability framework; heterotic products and pictures still need definition here.

[8] A. Alonso-Serrano, E. Tjoa, L. J. Garay and E. Martín-Martínez, *Particle detectors under chronological hazard*, JHEP 07 (2024) 001. [arXiv:2402.17825](https://arxiv.org/abs/2402.17825). Detector response to chronology-associated backgrounds is distinct from a controllable backward signal.

[9] R. H. Jonsson, E. Martín-Martínez and A. Kempf, *Information transmission without energy exchange*. [arXiv:1405.3988](https://arxiv.org/abs/1405.3988), particularly the leading detector signaling term. Used for the operational commutator criterion, not as a time-travel construction.

[10] B. S. Kay, M. J. Radzikowski and R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*. [arXiv:gr-qc/9603012](https://arxiv.org/abs/gr-qc/9603012). Scope-limited Hadamard/field-algebra obstruction, not a full quantum-gravity theorem.

**Search scope:** targeted primary-source checks on this date of the exact background and cited BRST, Misner-interaction, orbifold-backreaction and detector literature. This is not a complete proof that no relevant later paper exists. No novelty or priority claim is made.
