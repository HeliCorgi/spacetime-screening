# Heterotic Taub–NUT: interactions, backreaction, and an operational past-return test

**Date:** 2026-09-22.
**Type:** independent calculation and scope correction; not a proof of a time machine.
**Repository target:** `notes/heterotic-taubnut-interactions-backreaction-return-supplement.md`.
**Read snapshot:** PR #4, branch `heterotic-taubnut-fable-independent-audit`, commit `2a05752a0c8dd77829fa26c5701b31a24c143f18`.
**Companion calculation:** `src/symbolic/heterotic_taubnut_interaction_return_checks.py`.

**Integration note:** This supplement preserves the independently committed [interaction/contact-overlap audit](heterotic-taubnut-interactions-backreaction-return.md) at PR-head `e374b4727b5c0eb5703bed1815fc0fb2e999c953`. It adds the separately prepared source-scope audit, regular-null-coordinate checks, and the same-interface causal-return test without replacing that audit or its contact-overlap results.

## 0. Result first

The requested chain was

```text
interactions → finite-g_s backreaction → an observable for actual past return.
```

This investigation gives three substantive results, but does **not** complete that chain:

1. For the proposed neutral spectator polarization, the sphere **self-three-point function vanishes** by an exact free-current selection rule. The corresponding four-current factor does not vanish. Consequently, a vanishing cubic self-amplitude would not establish the absence of interactions or backreaction.
2. The positive NUT region can remain weakly coupled, but a nonzero stationary branch singular on a selected chronology horizon has a **blueshift stress proportional to an inverse squared regular null coordinate**. This supplies a concrete, conditional backreaction mechanism. A branch regular on that horizon avoids this particular divergence; no universal string-theory obstruction follows.
3. In a smooth chart for a specified **future Taub-to-NUT interface**, future causal crossing has a fixed sign of the radial velocity. The same interface cannot be used for a future-directed return in the opposite direction. Reciprocity of an exterior radial scattering problem therefore does **not** give a return protocol to the original Taub laboratory.

There are also essential corrections to the previous notes:

- The number `0.998130316064...` is reproducible as a **scalar radial flux ratio**. It is not an established exact string amplitude, and emphatically not the probability of successful time travel.
- The proposed affine quantum numbers pass the documented anomaly/weight arithmetic. The earlier declaration that a fully admissible heterotic BRST physical state was already proved was too strong. Its global Hilbert-space realization, complete string-BRST conditions and positive physical inner product have not been established in this model.
- A sphere four-string amplitude, a genus-one stress source, and a nonzero operational past-response have **not** been calculated here. Missing physical definitions must not be replaced by assumed values.

**Decision:** the prior claim that only interactions remained after two fully passed physical gates must be withdrawn. The geometric CTC background survives, the scalar calculation survives, and the affine construction remains a conditional candidate. An operational time machine is neither demonstrated nor excluded in full string theory by these calculations.

This note supersedes the physical interpretations, not the correctly scoped algebra, in `heterotic-taubnut-explicit-brst-state.md`, `heterotic-taubnut-transmission-amplitude.md`, and the D3/D4 “passed” entries in `heterotic-taubnut-time-travel-decision.md`.

## 1. What was independently reproduced

The exact target fields in [S1, S2] motivate the diagnostic metric

```math
 ds^2=L^2\left[\frac{dx^2}{p(x)}-\frac{p(x)}{D(x)}
 (dt-\lambda\cos\theta\,d\phi)^2+d\theta^2+\sin^2\theta\,d\phi^2\right],
 \qquad p=x^2-1,
```

```math
 D=(x+\delta)^2-\frac4{k+2}(x^2-1),\qquad
 \Phi=\Phi_0-\frac14\ln D,\qquad t\sim t+4\pi\lambda.
```

Here `L²=k−2` in the repository's dimensionless string units; a restored length normalization should be fixed before quoting dimensional energies or gravitational radii.

For the repository's point `k=8`, `δ²=8/5`, `λ²=2/5`, `ω=√10/2`, `Λ=1`, the scalar radial equation is

```math
 (pR')'+\left(\omega^2D/p-\Lambda\right)R=0.
```

Let `u=(x−1)/2`, and define

```math
 a_+=\frac{\omega(1+\delta)}2,\quad a_-=\frac{\omega(\delta-1)}2,
```

```math
 a=\frac12-i(\omega+\tfrac12),\quad
 b=\frac12-i(\omega-\tfrac12),\quad c=1-i(\omega+2).
```

The exterior solution

```math
 R_H=u^{-ia_+}(1+u)^{ia_-}\,{}_2F_1(a,b;c;-u)
```

has asymptotic coefficients obtained from the standard hypergeometric connection formula [S3]. Direct numerical differentiation of this solution was checked at `u=0.01,0.1,1,10`; the relative ODE residual was below `1.4×10⁻⁸¹` at 80-digit working precision. Its Wronskian flux was the same at all four points:

```math
 J_x=2u(1+u)\operatorname{Im}(R^*\partial_uR)
 =-(\omega+2)=-3.581138830084189665999447\ldots.
```

The independent gamma-function computation gives

```math
 T_{\rm radial}=0.998130316064461877277761984126636967187584795257\ldots,
```

```math
 R_{\rm radial}=0.001869683935538122722238015873363032812415204743\ldots,
 \qquad R_{\rm radial}+T_{\rm radial}=1.
```

This confirms a well-defined connection calculation for the **chosen exterior ODE and boundary conditions**. Wronskian conservation in a real second-order ODE is not a proof of target-space quantum unitarity, of a physical Hilbert-space norm, or of causal propagation across a chosen Cauchy-horizon extension.

### Why the exact target metric is not enough

An exact-in-`α′` target metric does not by itself identify the complete kinetic operator, two-point normalization, and interaction vertices for an oscillator-dressed string state. Those require a map from the actual coset vertex operators to the diagnostic scalar problem. [S1] explicitly separates calculation of the background from the response to particle/string probes. No exact coset two-point function has been matched to `R_H` in the audited material.

Nor does a common normalization necessarily cancel between all physically defined channels: global state definitions, reflection factors and projection/holonomy measures must first be established. The ratio above should remain labelled `T_radial`, not `T_string` or `P(past return)`.

## 2. The affine state is still a useful candidate, not a fully certified state

The proposed labels are

```math
 k_1=8,\quad k_2=4,\quad (Q_A,P_A)=(2,0),\quad(Q_B,P_B)=(2,1),
```

```math
 j=\frac12+\frac i2,\quad m=-2,\quad\bar M=\frac{\sqrt{10}}2,
 \quad\ell=1,\quad n=0,\quad\bar N=-1.
```

The anomaly equations in [S1, Eq. (13)] do vanish at this point. In the assumed current conventions,

```math
 K=\begin{pmatrix}8&4\\4&5\end{pmatrix},\quad
 m+\delta\bar M=0,\quad\lambda\bar M+\bar N=0,
```

and

```math
 \frac{-j(j-1)}{k_1-2}+\frac{\ell(\ell+1)}{k_2+2}
 -\frac12(-2,0)K^{-1}\binom{-2}{0}=0.
```

These are legitimate arithmetic successes. They neither establish a complete spectrum nor substitute for its construction.

### 2.1 Scope of the cited BRST results

Hwang–Rhedin [S4, §2] formulate their stated compact-group analysis with positive integer levels and integrable representations. Their equivalence result is not, without additional work, a theorem for this noncompact, asymmetric, heterotic `U(1)²` embedding. Their discussion itself distinguishes the noncompact problem.

The Maldacena–Ooguri no-ghost result [S5, §4.2 and Appendix A] concerns the specified `SL(2,R)` string setup, its Virasoro constraints and a unitary internal sector. A unitary zero-mode principal series is not the same as a positive-norm affine module before constraints; that paper explicitly discusses negative-norm affine descendants. An extra asymmetric gauging cannot be inserted into its conclusion without checking the hypotheses again.

The previous relative-grade argument can be retained as a **conditional algebraic lemma**: in a specified nonnegative-grade relative complex, a nonzero neutral grade-zero vector cannot be the image of a nonexistent grade-zero ghost-number-minus-one vector. What it does not establish is that the proposed left/right tensor product, auxiliary dressing, fermion sectors and global identifications actually supply that vector in the full physical state space.

A complete string-BRST analysis also needs a right superconformal primary and a globally consistent spectator/GSO completion, not just the two conformal weights. These conditions have not been checked by the scripts.

### 2.2 Normalization and global sectors

The individual exterior asymptotic radial mode has

```math
 |x^{-1/2+i/2}|^2=x^{-1},\qquad
 \int_1^X dx\,|R|^2=\ln X.
```

This does not disqualify a generalized scattering mode. It does show that a finite-norm packet has not been supplied simply by writing one such mode. Moreover, this radial `L²` measure is not automatically a positive physical Klein–Gordon/string inner product: `x` is timelike in Taub, and the NUT region contains periodic time and no ordinary global Cauchy surface. A physical inner product and allowed packet superposition must be defined independently.

Similarly, contractibility of a Hopf fibre proves the absence of a protected topological winding charge, not the disappearance of every possible global CFT contribution. For example, [S6] identifies singular one-loop behavior even in the **untwisted** sector of Misner strings. Lack of a separate winding sector cannot alone exclude chronology-related instability.

### 2.3 A concrete old formula that CI did not test

The Fable-derived note also represented a flowed vacuum as `(K^+_{−1})^{k₂w}|0>` with weight `k₂w²`. But `[L₀,K^+_{−1}]=K^+_{−1}` assigns that written monomial grade `k₂w`, not `k₂w²`. For `k₂=4,w=2`, the two values are 8 and 16. Whatever the correct extremal descendant is, that monomial is not its general formula. The old code verified a zero-mode shift, not this representation-theoretic identification. This does not refute the Hopf-topology observation, but it illustrates why a green CI is not a full cohomology certificate.

**Updated status:** anomaly-free model point and conditional neutral affine candidate, with physical admissibility still to be proved. It is not proved absent either.

## 3. Interactions: the smallest calculation that is actually available

Keep the proposed spectator factor, conditionally:

```math
 V_{\pm}^{(-1)}\sim J_Y\,\bar\psi^Y e^{-\bar\varphi}\widehat\Phi_{\pm},
 \qquad J_Y=i\partial Y,\qquad p_Y=0.
```

`Φ−` denotes the candidate conjugate of `Φ+`; its existence and norm are part of the pending physical construction. Normalize the free spectator current by `⟨J_Y(z)J_Y(w)⟩=(z−w)⁻²`.

### 3.1 Cubic self-amplitude: an exact conditional zero

For three external states with this same zero-momentum spectator polarization,

```math
 \langle J_Y(z_1)J_Y(z_2)J_Y(z_3)\rangle=0.
```

There is no complete Wick pairing of three Gaussian currents. Consequently their tree-level self-three-point amplitude vanishes, whenever the product-CFT vertex ansatz is valid. Right-moving picture changing does not alter that left-moving factor.

This is a selection rule, **not** an instability and **not** an absence-of-interaction theorem. The process with two such excitations and a different gravitational/dilaton intermediate state need not have this odd-current factor. In particular, an excitation that carries stress can source the background even if its own cubic self-coupling vanishes.

### 3.2 Four-point self-scattering is not killed by the spectator rule

Wick contraction yields

```math
 \langle J_1J_2J_3J_4\rangle=
 \frac1{z_{12}^2z_{34}^2}+\frac1{z_{13}^2z_{24}^2}
 +\frac1{z_{14}^2z_{23}^2}.
```

With insertions at `0,z,1,∞`, including the weight-one infinity limit,

```math
 K_Y(z)=\frac1{z^2}+1+\frac1{(1-z)^2},\qquad K_Y(1/2)=9.
```

The nonzero factor does not prove a nonzero **complete** amplitude; other factors and the integration can still matter. It demonstrates that the cubic zero is not enough to stop the calculation.

A minimally informative neutral process is `Φ+ Φ− Φ+ Φ−`. With canonical external normalization, its genus-zero amplitude has the schematic structure

```math
 \mathcal A^{(0)}_{+-+-}
 =g_{s,0}^{\,2}\int_{\mathcal M_{0,4}}d^2z\,
 K_Y(z)\,\mathcal C^{\rm BRST}_{+-+-}(z,\bar z;\text{pictures, projections}).
```

The remaining factor must include the noncompact coset blocks and their coefficients, the heterotic gauge/holonomy projection, superghost and right-moving superdescendant factors, and the physical two-point normalization. The sphere requires total right picture number `−2`; four `−1`-picture vertices without picture-changing insertions would not be a valid amplitude.

**Not calculated here:** `C^{BRST}_{+-+-}` and the moduli integral. Assigning it the value 1, multiplying the scalar transmission ratio by `g_s²`, or borrowing a BTZ coefficient would not compute this amplitude.

The poles of `K_Y` at worldsheet collision points are ordinary OPE/degeneration features. Without the full factorization analysis they must not be relabelled as a chronology instability.

## 4. Backreaction: weak coupling survives, but it is not uniform control

### 4.1 Favorable fact: the first positive NUT region is not forced to strong coupling

At the explicit point,

```math
 D(x)=\frac{3x^2+4\sqrt{10}\,x+10}{5},\quad
 D'(x)=\frac{6x+4\sqrt{10}}5>0\quad(x\ge1).
```

With `g_s(x)=g_{s,0}D(x)⁻¹/⁴`,

```math
 g_s(1)=\frac{g_{s,0}}{\sqrt{1+\delta}}
 =0.66446853959555744\ldots\,g_{s,0}.
```

It decreases as `x` increases on this NUT component. Thus taking a small overall `g_{s,0}` controls the **local coupling**, rather than encountering a mandatory `g_s→∞` at the first horizon.

A genus expansion has additional powers of `g_{s,0}²` per handle. This does not bound coefficients that can diverge with boost, mode sums, state choice, or degeneration limits. The exact target construction fixes `α′` corrections to background fields, not all those coefficients [S1].

### 4.2 The local boost geometry

Let `y=x−1`, `d=1+δ`. At fixed angles, leading order gives

```math
 ds^2_{\rm fib}\simeq L^2\left(\frac{dy^2}{2y}-\frac{2y}{d^2}dt^2\right).
```

Introduce a physical local radial coordinate `r=L√(2y)` and `η=t/d`:

```math
 ds^2_{\rm fib}\simeq dr^2-r^2d\eta^2=-dU\,dV,
 \qquad U=-r e^{-\eta},\quad V=r e^{\eta}.
```

One target-time identification acts as

```math
 (U,V)\mapsto(e^{-b}U,e^bV),\qquad b=\frac{4\pi\lambda}{1+\delta}.
```

Numerically,

```math
 b=3.509043131417428959\ldots,\qquad e^b=33.41627749505307818\ldots.
```

This is a local quotient boost, not a guaranteed energy multiplication experienced by every packet or every CTC orbit. Importing a global flat-orbifold image calculation into the entire curved heterotic background would require further justification. The original authors specifically caution that the embedding matters [S1]; [S7] is a serious instability precedent, not a theorem for this model.

### 4.3 A calculated conditional stress divergence

Near a horizon, with `Ω=ωd`, the two separated scalar branches can be represented locally, up to harmless constant phases, by

```math
 \chi_{\rm in}\sim V^{-i\Omega},\qquad
 \chi_{\rm out}\sim(-U)^{i\Omega}.
```

At the smooth horizon component `U=0,V>0`, the first is regular locally. For a nonzero coefficient `B_s` of the second,

```math
 |\partial_U\chi_{\rm out}|^2
 =\frac{|B_s|^2\Omega^2}{U^2}.
```

Thus a canonically normalized local scalar has a divergent null stress component proportional to `U⁻²` on that branch. A smooth observer crossing with nonzero `u^U` measures a corresponding divergent contribution. If both opposite null streams are present, a useful positive incoherent/two-null-dust diagnostic is

```math
 T_{UU}=A_U/U^2,\quad T_{VV}=A_V/V^2
 \quad\Longrightarrow\quad
 T_{\mu\nu}T^{\mu\nu}=8A_UA_V/(U^2V^2)
```

in the local `ds²=−dU dV` normalization.

The companion script checks these identities and also checks that the regular branch has `∂_Uχ_in=0`. Therefore it does **not** encode the false statement that every mode diverges on the same horizon.

**Crucial limitations:**

- This is a local effective-field diagnostic, not the renormalized genus-one stress tensor of the heterotic string.
- The pure horizon-ingoing exterior solution used to obtain `T_radial` sets the singular coefficient to zero on its selected horizon. A nonzero reflection coefficient at infinity does not by itself prove nonzero singular outgoing data on that horizon.
- The opposite horizon interchanges the branch regularity. A global state/extension must specify which horizons and which boundary conditions are involved.
- No calculation here shows that interactions necessarily regenerate a nonzero `B_s` for every admissible state. Nor has an interacting sector preserving `B_s=0` been constructed.

For a fixed singular stationary component, a dimensionless backreaction diagnostic behaves as

```math
 \epsilon(U)\sim\epsilon_0(U_0/U)^2.
```

It becomes order one at `|U|∼|U₀|√ε₀`. Even arbitrarily small nonzero coupling need not give a uniform bound as `U→0`. At sufficiently high local energy the effective-field approximation can fail before its predicted divergence; whether string dynamics then removes or regularizes the horizon is precisely what remains unknown.

### 4.4 Why KRW still matters after finding a smooth individual mode

The Kay–Radzikowski–Wald result [S8] obstructs extending ordinary local Klein–Gordon quantum-field states satisfying the initial Hadamard condition across base points of a **compactly generated** Cauchy horizon. It concerns the singularity structure of the two-point distribution, not the existence of one smooth classical solution.

The Taub region and a smooth compact-fibre horizon provide a natural setting to check those hypotheses. The diagnostic dilaton operator can be conjugated locally:

```math
 e^{-\Phi}(\Box-2\nabla\Phi\cdot\nabla)e^{\Phi}
 =\Box+\Box\Phi-(\nabla\Phi)^2.
```

Where the metric and dilaton are smooth, the extra term is a smooth lower-order potential. This explains why the local microlocal question does not disappear because `D` cancels from the measure. A precise application must still check the chosen global extension, compact generation, field equation and state assumptions; extensions of the original theorem to any modified scalar operator should not be asserted without checking the proof.

No KRW theorem for full string theory is claimed here. A UV completion could invalidate a local-QFT hypothesis. What cannot be claimed is that a finite-flux one-mode calculation has already bypassed the QFT obstruction.

### 4.5 What the actual string backreaction calculation needs

Let `B^I=(g,Φ,B₂,A,...)` denote all background fields. A proper calculation must determine the string one-point sources or the relevant real-time effective functional and solve schematically

```math
 \frac{\delta\Gamma_{\rm tree}}{\delta B^I}
 +\frac{\delta\Gamma_1}{\delta B^I}+\cdots=0
```

with specified quantum state and boundary conditions. A formal torus partition integral alone does not choose the real-time state or causal expectation value. The coupled dilaton, antisymmetric tensor and gauge equations cannot be replaced by a scalar Einstein equation at finite level.

**Not obtained:** the Taub–NUT-specific genus-one integrand, the full stress/tadpole sources, or a self-consistent backreacted solution. The calculation here identifies a concrete failure mode and a regular-branch exception; it does not choose between them in the complete theory.

## 5. Operational return: a transmission coefficient is missing causal information

### 5.1 A local one-way-interface result

Define `r_*'(x)=√D/p` and use the smooth coordinate `u=t−r_*`. In the coframe

```math
 \chi=du-\lambda\cos\theta\,d\phi,
```

the metric becomes

```math
 ds^2=L^2\left[-\frac pD\chi^2-\frac2{\sqrt D}dx\,\chi
 +d\theta^2+\sin^2\theta\,d\phi^2\right].
```

The radial/time determinant is nonzero at `x=1`. Choose the time orientation for which increasing `x` is future in the Taub region and `n=∂u` is future null on this **future Taub-to-NUT interface**. At its horizon, for any future causal tangent `v`,

```math
 g(v,n)=-\frac{L^2}{d}v^x\le0
 \quad\Longrightarrow\quad v^x\ge0.
```

For timelike crossing, the inequality is strict. A future-directed worldline therefore cannot cross back through **this same interface** with `v^x<0`.

The other regular coordinate `v_EF=t+r_*` describes the opposite horizon branch. Reversing the scattering boundary condition or the time orientation is not an operational return by the same observer in the same extension.

**Precisely what this rules out:** the suggested shortcut “the real radial ODE is reciprocal, hence go Taub→NUT and come back through the same horizon.” That inference is false. The proof is local and does not exclude travel involving other components of a fully specified extension, extra identifications or dynamics that changes the geometry. Those possibilities require an explicit global trajectory and cannot be inferred from the exterior ODE.

### 5.2 Timelike circles still exist

At fixed `x>1,θ,φ`, the periodic `t` orbit remains a finite-proper-time CTC of the background. Contractibility is irrelevant to whether its tangent is timelike. But that orbit is wholly in NUT, not a demonstrated preparation-and-return experiment originating at a specified Taub event.

A further local diagnostic is the acceleration needed to hold that orbit:

```math
 a^2=\frac{p}{4L^2}\left(\frac{p'}p-\frac{D'}D\right)^2
 \sim\frac1{2L^2(x-1)}.
```

It diverges as the horizon is approached but is finite at fixed `x>1`. This is not a technology-based impossibility argument; it prevents treating arbitrarily near-horizon stationary loops as cost-free inertial probes.

### 5.3 Define the observable that would decide the question

The appropriate target is a **controllable signal response**, not a Wightman correlation and not a coordinate identification.

Specify a laboratory worldline with a relational clock. Let `A` be a preparation operation at clock time `τ_p`, and `B` a receiver measurement at `τ_r<τ_p` on the same identified laboratory history (or on clocks synchronized in a specified initially chronal laboratory). Define

```math
 \mathcal S_{A\to B}
 =\left.\frac{\partial\langle\mathcal O_B\rangle_{j_A}}{\partial j_A}
 \right|_{j_A=0}.
```

The external source choice must encode a freely controllable difference, not merely a correlation imposed by final boundary conditions or postselection. A positive operational result requires a finite, nonzero response for receiver data in the preparation event's already specified causal past, with normalized probabilities and a consistent preparation prescription.

In a standard causally ordered unitary region, linear response is a retarded commutator: expanding a source unitary gives the commutator, and the causal evolution prescription gives its retarded support. On a non-globally-hyperbolic extension those prescriptions must be supplied and shown mutually consistent; they cannot be inferred from a gamma-function connection coefficient.

The detector positions must be defined relationally, and string insertions must be BRST admissible. Writing a fixed coordinate pair `(x,t)` is not by itself a diffeomorphism/BRST-invariant operational observable. Likewise `⟨Φ(B)Φ(A)⟩≠0` alone demonstrates neither controllable signalling nor past return.

**Not obtained:** a complete exact-coset definition or a nonzero value of `S_{A→B}`. The same-interface classical protocol has failed the causal-sign test; a different protocol remains to be explicitly proposed and tested.

## 6. Prior-art evidence: what transfers and what does not

| Source/result | Useful conclusion | Not licensed |
|---|---|---|
| Johnson–Svendsen [S1], global continuation [S2] | Exact background chronology survives `α′` corrections; probes must be treated separately | An exact interacting time machine or all-genus control |
| Hwang–Rhedin [S4] | Precise BRST/coset methods under stated representation assumptions | Automatic noncompact asymmetric heterotic no-ghost theorem |
| Maldacena–Ooguri [S5] | Noncompact string representation and no-ghost technology | Positivity of this new coset by merely naming a principal series |
| Misner strings [S6] | Physical modes and high transmission/pair production can coexist with loop singularities, including in an untwisted sector | The same instability rate in Taub–NUT |
| Horowitz–Polchinski [S7] | Boosted images and gravitational backreaction can invalidate naive weak-coupling intuition in their orbifold models | A ready-made no-go for the full curved heterotic background |
| KRW [S8] | One smooth mode does not establish a Hadamard QFT state at a compactly generated horizon | A theorem forbidding all string-theory CTCs |
| Heterotic Gödel/AdS [S9] | Exact background and spectrum can be destabilized by string sectors | Taub–NUT tachyon condensation already calculated |
| Holographic time machines [S10] | Model-dependent interacting chronology obstructions exist | A universal obstruction applying unchanged here |

Only the primary sources listed below were used for these claims. This was a targeted follow-up and hypothesis audit, not an exhaustive claim that no relevant paper exists anywhere.

## 7. Updated status and the next genuinely decisive computation

| Question | Status after this work |
|---|---|
| Does the background contain CTCs? | Yes, in the published exact target construction |
| Is the scalar radial flux ratio reproducible? | Yes; value and ODE/Wronskian independently checked |
| Is that number a physical past-return probability? | No |
| Is the proposed full heterotic physical state already established? | No; retain as a conditional affine candidate |
| Is its cubic self-amplitude nonzero? | No, for the stated zero-momentum spectator polarization |
| Are all interactions thereby absent? | No; four-current factor survives and other cubic channels need not vanish |
| Is local `g_s` forced to grow on the first positive NUT component? | No |
| Is there a concrete backreaction danger? | Yes, a singular stationary branch has inverse-square blueshift stress; regular branch is an exception |
| Has the full string loop/backreaction problem been solved? | No |
| Does radial reciprocity implement a same-horizon round trip? | No, for the specified time-oriented smooth interface |
| Has a controlled past-response observable been exhibited? | No |

Two tasks can now proceed without conflating their outcomes:

**Physical sector and interactions:** construct the full asymmetric coset BRST vertex, its allowed global sector and two-point pairing; then determine the neutral four-point function and its degeneration limits. The nonzero spectator factor is an input, not a replacement for the coset computation.

**Causal realization and backreaction:** specify the actual extension and preparation state; determine whether its interacting evolution unavoidably populates the singular horizon branch or instead yields a stable regular state; finally evaluate the relational signal response. A geometric loop within NUT and an exterior scattering coefficient do not fix that problem.

The strongest defensible current conclusion is **not an operational “yes.”** It is a set of correct conditional calculations plus unresolved physical definitions, with a concrete causal obstruction to the simplest return protocol. A universal “no” has not been proved either.

## 8. Reproduction and delivery

Run:

```bash
python src/symbolic/heterotic_taubnut_interaction_return_checks.py --json notes/data/heterotic_taubnut_interaction_return_checks.json
```

The script has been run locally, including the 80-digit ODE and flux tests. It makes no network calls. Its JSON explicitly records `full_string_BRST_proved=false`, `interacting_coset_amplitude_computed=false`, and `operational_past_return_proved=false`.

Publication adds this supplement, its independent script, and the JSON output under `notes/data/heterotic_taubnut_interaction_return_checks.json`. The script was rerun successfully with Python 3.13.5, SymPy 1.14.0, and mpmath 1.3.0 before publication. It does not certify full-string cohomology or a past-signalling probability.

The previously prepared patch targeted an older PR snapshot and would collide with the already committed interaction/contact-overlap note. It is therefore not applied wholesale. Existing notes, scripts, workflows, and the contact-overlap data are preserved. The scope corrections in sections 0–2 above explicitly supersede the old D3/D4 physical interpretations. This publication does not request a merge or change the PR's draft state; local execution is not a claim that a newly triggered GitHub Actions run has passed.

## Sources

- **[S1]** C. V. Johnson and H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, Phys. Rev. D 70, 126011 (2004). In particular Eq. (13), the background/probe distinction in the introduction, and the concluding discussion. https://arxiv.org/html/hep-th/0405141v3
- **[S2]** H. G. Svendsen, *Global properties of an exact string theory solution in two and four dimensions*, Phys. Rev. D 73, 064032 (2006), especially §§2, 4–5. https://arxiv.org/html/hep-th/0511289v2
- **[S3]** NIST DLMF, §15.8, transformations of the Gauss hypergeometric function, especially 15.8.2. https://dlmf.nist.gov/15.8
- **[S4]** S. Hwang and H. Rhedin, *The BRST formulation of G/H WZNW models*, Nucl. Phys. B 406, 165–186 (1993), especially the assumptions in §2. https://arxiv.org/html/hep-th/9305174v3
- **[S5]** J. Maldacena and H. Ooguri, *Strings in AdS3 and the SL(2,R) WZW Model. Part 1: The Spectrum*, J. Math. Phys. 42, 2929 (2001), §4.2 and Appendix A. https://arxiv.org/html/hep-th/0001053v3
- **[S6]** M. Berkooz, B. Pioline and M. Rozali, *Closed Strings in Misner Space: Cosmological Production of Winding Strings*, JCAP 0408, 004 (2004); the abstract itself distinguishes untwisted and twisted loop singularities. https://arxiv.org/abs/hep-th/0405126
- **[S7]** G. T. Horowitz and J. Polchinski, *Instability of Spacelike and Null Orbifold Singularities*, Phys. Rev. D 66, 103512 (2002). https://arxiv.org/abs/hep-th/0206228
- **[S8]** B. S. Kay, M. J. Radzikowski and R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, Commun. Math. Phys. 183, 533–556 (1997). https://arxiv.org/html/gr-qc/9603012v2
- **[S9]** D. Israël, *Quantization of heterotic strings in a Gödel/Anti de Sitter spacetime and chronology protection*, JHEP 0401, 042 (2004). https://arxiv.org/abs/hep-th/0310158
- **[S10]** R. Emparan and M. Tomašević, *Holography of time machines*, JHEP 03, 212 (2022). https://arxiv.org/html/2107.14200v3
