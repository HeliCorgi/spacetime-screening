# v8：4D量子stress候補を総監査し、Deutsch則を標準3+1D QFTから導けるか判定する

**2026-09-27。基点 `6a408e42abef6355699d276c1bc45547198954ae`（PR #26 merge後）。**

目的は、[v7](sa-deutsch-fixed-point-v7.md) の `D_past=e^-1>0` を「Deutsch則を仮定したtoy B」のまま残さず、4Dのrenormalized stress候補と、Deutsch fixed-point selectionの3+1D QFT由来を同時に検査すること。SA v5のpulse形状は固定し、再最適化しない。

## 0. 結論

**A=0 / B=5 / C=1。** stress tensor側には実在する強い部分候補が残るが、standard linear 3+1D QFTからexact Deutsch selectorを導く経路はC。

v7のoperation-dependent selectorを

```math
S_D(\Phi)=\rho^*_\Phi,\qquad \rho^*_\Phi=\Phi(\rho^*_\Phi)
```

とする。固定initial state・action・background・global boundary prescriptionを使う通常量子論/QFTでは、局所CP operation `E` をslotへ挿入して得るstate/probabilityは `E` のconvex mixtureに対してaffineである。ところがv7 selectorはそうならない。

v7と同じ `a=1/2`, `c=pi/8`、2 operationのmixing `q=1/2` では、各operationのfixed pointを先に選んでから混ぜたX分散は

```math
V_{\rm affine}=\frac12+\frac{\pi^2}{16},
```

一方、operation自体を先に `Phi_mix=(Phi_++Phi_-)/2` と混ぜて、そのCPTP mapのfixed pointを解くと

```math
V_{\rm fixed(mix)}=\frac12+\frac{\pi^2}{48}.
```

従って

```math
\boxed{\Delta V=\frac{\pi^2}{24}=0.4112335167120566\ldots>0.}
```

一般に `0<a<1`, `0<q<1`, `c!=0` で

```math
\boxed{\Delta V=\frac{8a q(1-q)c^2}{(1-a)^2(1+a)}>0.}
```

これはroundoffではなくexact algebra。したがって **operation-independentなfixed-state standard QFT supermapは、v7のexact Deutsch state-selection lawを再現できない。**

このCは量子重力一般のno-goではない。operation-dependent global boundary、postselection/final-state、明示的非線形量子力学、新しいquantum-gravity state-selection lawは別モデル。ただし、それらは「standard 3+1D QFTからDeutsch則を導出」したことにはならない。

## 1. v7 signal modeをwormhole支持源として二重利用できるか

v7 exact fixed pointは

```math
\langle X\rangle_b=\pm\frac\pi4,\qquad V_X=\frac12,\qquad V_P=\frac56.
```

unit-frequency oscillatorなら

```math
\frac{E_{\rm loop}}{\hbar\omega}=\frac23+\frac{\pi^2}{32}=0.9750918042\ldots,
```

vacuumとの差は

```math
\frac{\Delta E}{\hbar\omega}=\frac16+\frac{\pi^2}{32}>0.
```

さらにminimal scalarのsmooth coherent meanはnull vector `k` に対し

```math
T_{ab}^{\rm coherent}k^ak^b=(k^a\nabla_a\phi)^2\ge0.
```

よってDeutsch signal sectorそのものをexotic throat supportとして使う案は閉じる。support fieldとsignal fieldは分離する。

## 2. stress候補1：Maldacena–Milekhin–Popov

Maldacena–Milekhin–Popov, *Traversable wormholes in four dimensions*, arXiv:1807.04726。

4D Einstein–Maxwell＋charged massless fermion。large magnetic chargeによりlowest Landau levelsが多数の1+1D massless modesを作り、negative Casimir-like null stressを与える。論文はこのquantum stressをEinstein equationへ入れてlong traversable throatを解いており、局所stress matchingより強い。

しかしpublished solutionは意図的に**long**でambient causalityを破らない。time shift / moving mouthsを追加して同じfermion stateとEinstein equationを自己無撞着に解いたtime-machine解ではない。

**判定：B — strongest explicit semiclassical support component。**

## 3. stress候補2：Jiang–Jiang 2026

S. Jiang, J. Jiang, *Stress-energy tensor of quantized scalar fields in a zero-tidal wormhole*, arXiv:2603.01003 / Phys. Rev. D 114, 025001 (2026)。

prescribed zero-tidal wormhole上でnonminimally-coupled massive scalarを量子化し、Hadamard subtraction＋pragmatic mode-sumでrenormalized stress tensorを直接計算。dimensionless mass/coupling spaceにMorris–Thorne throat conditionsを満たす3領域を見つけ、mass exclusion intervalsも得ている。

ただしmetricをRSETから再解いて元geometryへ戻るglobal semiclassical fixed pointは未構成。

### 3.1 1 m throatのscale診断

single-scale vacuum RSETを

```math
\tau_q=N C\frac{\hbar c}{b_0^4}
```

とし、zero-tidal throatのEinstein tension scale

```math
\tau_E=\frac{c^4}{8\pi G b_0^2}
```

へ合わせると

```math
\boxed{NC=\frac{b_0^2}{8\pi\ell_P^2}}.
```

`b0=1 m` では

```text
N C = 1.523141897782187e68.
```

`C=1e-4` なら `N~1.5e72`。large-N species cutoff estimate `L_species~sqrt(N) l_P` を採る場合は約20 mとなり、1 m geometryをordinary semiclassical EFTで扱うcontrolが失われる。このspecies estimateは任意のUV completionへの普遍定理としては使わない。

**判定：B — exact RSETだがglobal coupled solution未達。**

## 4. stress候補3：Popov long throat

A. Popov, *Semiclassical long throats of the wormholes*, arXiv:1809.06202。

nonconformal scalar vacuum polarizationのlocal/WKB regimeでsemiclassical Einstein equationsのself-consistent long-throat solutionを得る。これは「4D quantum stressをEinstein equationへ入れて自己無撞着wormhole」を満たす重要部品。

ただしlong-throat/local approximationで、asymptotically-flat finite apparatus＋mouth time shift＋CTC stateまで一つにした解ではない。

**判定：B。**

## 5. stress候補4：Kain quantized Einstein–Dirac–Maxwell

B. Kain, *Einstein-Dirac-Maxwell wormholes in quantum field theory*, arXiv:2308.00049。

charged Dirac fieldを量子化し、gravity/Maxwellをsemiclassicalに扱うstatic spherically symmetric wormhole configurationsを構成する。

一方、関連するEDM static solutionsのtime evolution（arXiv:2305.11217）では、調べられたcasesでblack holesが形成され、wormholeを通ったsignalも外へ脱出できない。これはquantized configurations全部のcollapse theoremではないのでCへ一般化しない。

**判定：B — quantum configuration自身のdynamic traversability/time-machine deformationが未解。**

## 6. stress候補5：Mehulic–Prokopec 2026

H. Mehulic, T. Prokopec, *Quantum backreaction and stability of topological wormholes*, arXiv:2603.11724。

`M2 x S2` topological wormhole上でmassive minimally-coupled scalarのone-loop RSETをdimensional regularizationし、static/time-dependent backreactionをlinear order in hbarまで解く。

ただしbackgroundはclassical anisotropic fluidでsupportされ、著者もfully self-consistent semiclassical solveを今後の問題として残す。

**判定：B — explicit backreaction component。**

## 7. Deutsch則の3+1D QFT導出

### 7.1 standard QFT / fixed process

initial state、action、background、global boundary prescriptionを固定し、future laboratoryのlocal CP map `E` のみ差し替える。full field＋apparatusを通常のlinear quantum systemとして扱う限り、unitary/isometry、partial trace、Born ruleの合成は `E` にaffine。

Chiribella–D'Ariano–Perinottiのdeterministic quantum supermapも、physical operation transformationをlinear/CPなhigher-order mapとして特徴づける。今回必要なのはinfinite-dimensional QFT全体の定理ではなく、2つのfinite local operationsのclassical mixtureに関する基本linearityだけ。

v7 Deutsch selectorは冒頭の `pi^2/24` gapでこのaffinityに反する。

**判定：C — exact Deutsch selection cannot be derived from an operation-independent standard linear QFT process on a fixed background。**

### 7.2 CTC path-integral prescriptions

PolitzerやFewster–Higuchi–WellsではCTC上のoperator/path-integral prescriptionsが一意ではなく、unitarity・CCR・orderingに問題が生じる例がある。既存CTC path integralを持ち込むことはDeutsch selectorの導出にはならない。

### 7.3 chronology horizon

Kay–Radzikowski–Waldはcompactly generated Cauchy horizonのbase pointsで通常のF-local algebra/Hadamard extensionが破綻し、RSET等がill-defined/singularになることを示す。全CTC geometryのno-goではないが、「ordinary Hadamard QFTをそのままchronology horizonへ延ばせばDeutsch則が自然に出る」という経路を支持しない。

## 8. 統合判定

| component | status | 残る壁 |
|---|---|---|
| MMP fermion Casimir | B | self-consistent 4D supportだがlong・ambient-causal |
| Jiang–Jiang RSET | B | exact RSETだがprescribed geometry |
| Popov long throat | B | self-consistent local/long-throat regime、time machineなし |
| Kain quantized EDM | B | static QFT solution、dynamic traversability未解 |
| Mehulic–Prokopec | B | one-loop backreaction、classical supportが残る |
| Deutsch from standard QFT | **C** | exact non-affinity gap `pi^2/24` |

**A=0 / B=5 / C=1。** Bの数は「5台の装置」ではなく、support/backreactionの5系統の部分候補。

v7の

```math
P(Y|do(0))\ne P(Y|do(1)),\qquad D_{\rm past}=e^{-1}
```

はDeutsch ruleを**新しい基礎法則として仮定するB**の内部では維持される。しかしstandard 3+1D QFTからそのruleまで通す今回の目標はC。

## 9. 次に残る計算問題は一つだけ

standard QFT内でDeutsch則をさらに探すのは同じconvex-linearity obstructionを繰り返す。

> **Deutsch selectorと同じnon-affine state selectionを生む、明示的なquantum-gravity / nonlinear global-boundary functionalをまず定義し、その理論自身のBorn rule、局所operation、renormalized 4D stress tensor、Einstein limitが整合するかを計算する。**

これは既存QFTのparameter tuningではなく、新しい基礎法則候補の問題。

## 10. 再現

```bash
python src/symbolic/stress_deutsch_qft_v8.py --output /tmp/v8.json
python src/symbolic/stress_deutsch_qft_verify_v8.py --evidence /tmp/v8.json --output /tmp/v8-verify.json
```

local Python 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0で実行し、`A=0/B=5/C=1`, `NC(1m)=1.523141897782187e68`, `Delta V=pi^2/24` を確認。別検証器はforwardをimportせずexact algebraとSI scaleを再計算する。

## 11. 文献

- J. Maldacena, A. Milekhin, F. Popov, *Traversable wormholes in four dimensions*, arXiv:1807.04726.
- S. Jiang, J. Jiang, *Stress-energy tensor of quantized scalar fields in a zero-tidal wormhole*, arXiv:2603.01003, Phys. Rev. D 114, 025001 (2026).
- A. Popov, *Semiclassical long throats of the wormholes*, arXiv:1809.06202.
- B. Kain, *Einstein-Dirac-Maxwell wormholes in quantum field theory*, arXiv:2308.00049.
- B. Kain, *Are Einstein-Dirac-Maxwell wormholes traversable?*, arXiv:2305.11217.
- H. Mehulic, T. Prokopec, *Quantum backreaction and stability of topological wormholes*, arXiv:2603.11724.
- D. Deutsch, *Quantum mechanics near closed timelike lines*, Phys. Rev. D 44, 3197 (1991).
- H. D. Politzer, *Path integrals, density matrices, and information flow with closed timelike curves*, Phys. Rev. D 49, 3981 (1994).
- C. J. Fewster, A. Higuchi, C. G. Wells, *Classical and Quantum Initial Value Problems for Models of Chronology Violation*, arXiv:gr-qc/9603045.
- B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, arXiv:gr-qc/9603012.
- G. Chiribella, G. M. D'Ariano, P. Perinotti, *Transforming quantum operations: quantum supermaps*, arXiv:0804.0180.
- G. Dvali, M. Redi, *Black Hole Bound on the Number of Species and Quantum Gravity at LHC*, arXiv:0710.4344.

**scope discipline:** Cは「standard linear QFTからexact Deutsch selectorを導く」ことへの障害。quantum gravity一般のDeutsch-like非線形則の不存在証明ではない。
