# v9：新しいtoy物理法則 — Chronology-Backreaction State-Selection Law (CBSSL)

**2026-09-27。基点 `fbf98de97fe11b9dea40e7d195227ea4a088b5a5`（v8 merge後）。**

これは既存理論から導いた法則ではない。**closed causal loopが存在する場合だけ発動する、新しい量子重力state-selection lawのtoy proposal**として定義する。文献上の「世界初」を主張しない。Deutsch fixed-point、CTC path integral、quantum supermap、semiclassical Einstein equationを境界として、今回の具体的な合成則と検算を提案する。

## 0. 結論

提案する法則を **Chronology-Backreaction State-Selection Law (CBSSL)** と呼ぶ。

chronology cut `Sigma` 上のstate `rho`、3+1D metric `g`、future laboratoryの**完全な物理operation** `E` に対し、ordinary local QFT/apparatus dynamicsが一周して `Sigma` へ戻るreturn channelを

```math
Phi_{g,E}: rho -> rho'
```

とする。CBSSLはphysical pair `(g_*,rho_*)` を次の**lexicographic minimization**で選ぶ：

```math
(g_*,rho_*) = LexArgMin_{g,rho in A}
  ( C_loop[rho,g,E], R_sc[g,rho], I_ref[rho,g] ).
```

第一成分はchronology mismatch、第二成分はsemiclassical Einstein residual、第三成分は参照stateへの情報距離。

```math
C_loop = D_B^2(rho, Phi_{g,E}[rho]) >= 0,
```

```math
E_{mu nu}[g,rho]
=G_{mu nu}+Lambda g_{mu nu}-8 pi G <T_{mu nu}>_{rho,ren},
```

```math
R_sc = int_C d^4x sqrt(-g) w(x)
 E_{mu nu} E_{rho sigma} q^{mu rho}q^{nu sigma} >=0,
```

```math
q^{mu nu}=g^{mu nu}+2u^mu u^nu,
```

```math
I_ref = S(rho || rho_ref).
```

`u^mu`はapparatusが定めるfuture timelike unit vectorで、signature `(-,+,+,+)` では `q` がpositive definiteになる。`w` はchronology-support上の固定されたnonnegative weight。renormalization scheme・counterterms・`rho_ref` はoperationごとに変えない。

**stationary chronology solutionとして認める条件は、最小値で `C_loop=0` かつ `R_sc=0`、finite renormalized stress、外部から固定されたasymptotic/gauge chargesの保存。** どれかを満たすadmissible stateがなければ、その仮定したstationary CTC geometryはphysical solutionではない。

このlawは明示的にnon-affineである。これはv8でstandard QFTからDeutsch selectorを導けなかった原因を、今回は**新しい物理公理として意図的に採用する**もの。

**判定は A=0 / B=1 / C=0。** toy law内部ではv7の `D_past=e^-1` を再現するが、full 3+1D SA RSETとbackreactionまで未解なので現行protocolのAには上げない。

## 1. なぜこの3段階か

### 1.1 chronology consistencyを最優先

Bures mismatch

```math
D_B^2(rho,sigma)=2(1-Tr sqrt(sqrt(rho) sigma sqrt(rho)))
```

はnonnegativeで、`rho=sigma`のときだけ0。有限cutoffでは通常のdensity matrixを使う。continuum QFTへ上げるときはlocal algebraic stateと対応するfidelity/relative-entropy構造へ置き換える必要がある。

`C_loop=0` は

```math
rho = Phi_{g,E}(rho)
```

なのでDeutsch consistencyを再現する。しかし**これだけ**ではDeutsch則ではない。次にgravity residualを評価する。

### 1.2 fixed pointでもEinstein方程式を壊すなら不許可

`R_sc=0` は

```math
G_{mu nu}+Lambda g_{mu nu}
=8 pi G <T_{mu nu}>_{ren}
```

を要求する。つまり「量子回路上ではfixed pointだが、そのstateのRSETがwormholeを破壊する」解はここで落ちる。

これはv7に欠けていた部分を法則そのものへ組み込む。

### 1.3 まだ固定点が複数ならleast-changeを使う

`C_loop=R_sc=0` が複数ある場合だけ

```math
min S(rho||rho_ref)
```

を使う。`rho_ref`はchronologyを形成する前のlocal Hadamard/reference stateから固定し、future operationごとに変えない。

identity loopでは全stateがfixed pointになる。古典2状態controlで

```math
rho_ref=diag(2/3,1/3)
```

とするとrelative entropyのunique minimumは同じ `diag(2/3,1/3)`。Deutsch maximum-entropy ruleなら `I/2` を選ぶので、CBSSLはDeutschの単なる言い換えではない。

## 2. globally hyperbolic領域では発動しない

closed causal returnがなく `Phi_{g,E}` を定義できないgeometryではCBSSL chronology termを使わない。ordinary initial-value QFTのstateをそのまま使用する。

したがって「全宇宙で非線形Schrodinger equation」を導入する提案ではない。non-affinityはchronology-return algebraに限定する。

これはnonlinear quantum mechanicsで知られるsuperluminal-signalling問題を完全に証明回避したわけではない。**設計上のlocality条件**として、chronology selectorはminimal chronology-return algebraのreduced stateと、そのcausal return mapだけを見る。

spacelike complementのlocal trace-preserving operationでchronology algebraのreduced density operatorが変わらない場合、selectorも変えない。Bell-pair＋remote unitaryのexact controlをコードで検査した。

## 3. operationの「混ぜ方」を曖昧にしない

v8で

```math
S_D(q Phi_+ +(1-q)Phi_-)
!= q S_D(Phi_+)+(1-q)S_D(Phi_-)
```

だった。新法則ではこれはbugではなくfeatureだが、**同じreduced channelの異なるensemble decompositionへ依存すると物理法則にならない。**

そこでCBSSLのinput `E` は、隠れたKraus decompositionではなく、chronology cutを横切る**全degree of freedomを含むcomplete CPTP operation**と定義する。

randomizer bitを保持したままloopへ入れる場合、そのclassical registerもoperationの一部。randomizerを物理的にeraseしてからloopへ入れる場合だけ、reduced mixed channelがinputになる。

この規則で「classical random choiceをどのdecompositionで書いたか」による曖昧さを避ける。

## 4. v7 positive channelを新法則で再現

SA v5 signal componentは固定し、v7と同じ一mode return mapを使う：

```math
a=1/2, eta=1/4, lambda=1, c=pi/8.
```

`do(b)`ごとのloop mapはcontractiveでfixed pointがuniqueなので、CBSSL第一段階だけでstateが確定する。

```math
<X>_0=+pi/4,
<X>_1=-pi/4,
V_X=1/2,
V_P=5/6.
```

finite Ramsey receiverについて

```math
P(Y=+1|do(0))=(1+e^-1)/2=0.683939720585721...,
```

```math
P(Y=+1|do(1))=(1-e^-1)/2=0.316060279414279...,
```

```math
boxed(D_past=e^-1=0.367879441171442...>0).
```

copy/NOTについてもv7のfull bosonic mapsはfixed pointを持つので、v6のnormalization contradictionは生じない。

## 5. stress tensorについて、このtoyで新たに良い点

selected loop modeのvacuumからのenergy excessは

```math
Delta E/(hbar omega)=1/6+pi^2/32=0.4750918042...>0.
```

しかもbit 0/1でmean fieldが `+phi_c/-phi_c`、connected covarianceが同じなら、free scalarのquadratic stress tensorは

```math
<T_{mu nu}>_0
=<T_{mu nu}>_ref+T_{mu nu}[phi_c]
=<T_{mu nu}>_1.
```

したがって**bitを変えるたびにgeometryまで変える必要は少なくともこのsignal sectorからは出ない**。これはfuture bitをgeometry-dependent boundary inputへ隠すより良い。

ただしこのpositive-energy signal fieldはwormholeのexotic supportではない。v8で確認した通りminimal scalarのcoherent contributionはnull方向でnonnegative。background support sectorは別に必要。

## 6. chronology protectionも同じ法則から出せる

finite-dimensional CPTP mapにはfixed pointがあるが、CBSSLのadmissible setにはfinite RSET、charge conservation、semiclassical residualなどを要求する。

controlとして、唯一のfixed pointがenergy `1` のreplacement channelに対しadmissible energy cap `1/2` を課すと、admissible fixed pointは存在しない。

CBSSLはこのときfuture resultをpostselectするのではなく、**そのstationary chronology geometryがfield equations/boundary constraintsのsolutionではない**と判定する。

つまり同じ法則が

- admissible fixed pointあり → paradox-free chronology branch
- admissible fixed pointなし → chronology protection branch

を持つ。

## 7. cutを変えても同じlawであるための条件

chronology cutをordinary unitary propagation `U` で移動すると

```math
rho -> U rho U^dagger,
Phi -> U o Phi o U^dagger.
```

Bures distanceとquantum relative entropyはunitary invariantなので第一・第三順位は不変。`R_sc`は同じ4D region上のtensor integralとして定義するため、単なるcut relocationでは不変であることを要求する。

コードでは2-level conjugationのcontrolを持つ。full QFTでのcut-independenceは未証明で、Aへ上げる前の必須検査。

## 8. v8のnon-affinity gapを「新法則の実験的特徴」に変える

v7 parameterで `q=1/2`：

```math
V_selected-then-mixed=1/2+pi^2/16,
```

```math
V_mixed-operation-then-selected=1/2+pi^2/48,
```

```math
boxed(Delta V=pi^2/24=0.4112335167120566...).
```

standard fixed-process QFTでは許されない差だが、CBSSLではchronology region固有のobservable signatureになる。

従ってこのlawはfalsifiableなtoy ruleであり、「Deutsch fixed pointを別名で書いただけ」ではない。

## 9. 既存理論との境界

- **Deutsch 1991**：CTC registerにfixed-point conditionを課す。CBSSLはchronology consistencyを第一条件に含むが、gravity residualとrelative-entropy tie-breakを追加し、admissible finite-RSET fixed pointがなければgeometryを不許可にする。
- **Politzer 1994**：CTC量子論には非等価な処方があり得る。従ってCBSSLは「CTCなら必然」ではなく明示的な新仮説。
- **Chiribella–D'Ariano–Perinotti 2008**：ordinary quantum supermapsはlinear/CPなoperation transformation。v8が示したnon-affinityを、CBSSLはchronology sectorだけで意図的に破る。
- **Morimae 2014 / process matrices**：single-partyのstandard process-matrix frameworkはordinary quantum physicsへ縮退する。CBSSLはそのframework外のnon-affine law。
- **P-CTC**：future outcome postselectionを使う。CBSSLはfuture measurement outcomeを選別せず、selected state上でordinary Born ruleを使う点で別物。
- **nonlinear QMのsignalling問題**：一般のnonlinear quantum dynamicsはrelativityと緊張する。CBSSLはchronology-return algebra限定＋reduced-state dependenceを設計条件にするが、multipartite quantum gravityでの完全なno-superluminal proofはまだない。

## 10. 3+1D量子重力への埋め込み案

regulated chronology-cut Hilbert space `H_Sigma^Lambda` でまずlawを定義し、cutoffを外す。

admissible sequence `(g_Lambda,rho_Lambda)` が

1. local Hadamard limitを持つ、
2. `<T_mn>_ren`がfixed renormalization prescriptionで収束、
3. `C_loop -> 0`,
4. `R_sc -> 0`,
5. asymptotic chargesが一定、
6. cut relocationで同じphysical stateへunitary/algebraic equivalence、

を満たす場合にだけcontinuum CBSSL solutionと呼ぶ。

これはまだ解いていない。ここがtoy lawをA候補へ上げる主計算になる。

## 11. 現在の分類

```text
A = 0
B = 1   CBSSL toy quantum-gravity law
C = 0
```

CBSSL内部では

```math
P(Y|do(0)) != P(Y|do(1)),
D_past=e^-1>0
```

まで明示済み。

Aにしない理由は：

- CBSSL自体が新しい仮説で実験・既存QGから未導出、
- full SA 3+1D return map未計算、
- CBSSL-selected stateのfull RSET未計算、
- metricとRSETのglobal self-consistent solution未構成、
- multipartite relativistic consistency/cut independence未証明。

## 12. 次の一問

このlawをこれ以上言葉で拡張せず、次は一問だけ：

> **SA二殻のregulated 3+1D scalar fieldについてCBSSLの `C_loop=0` stateをmode basisで構成し、その同じstateのHadamard-subtracted `<T_{mu nu}>_ren` を計算して `R_sc` が0へ近づくmetric/state pairを一つ見つけられるか。**

これが通れば、初めて「新lawを仮定した3+1D quantum-gravity toy A」に近づく。

## 13. 一次文献／比較対象

- D. Deutsch, *Quantum mechanics near closed timelike lines*, Phys. Rev. D 44, 3197 (1991), https://doi.org/10.1103/PhysRevD.44.3197
- H. D. Politzer, *Path integrals, density matrices, and information flow with closed timelike curves*, Phys. Rev. D 49, 3981 (1994), https://arxiv.org/abs/gr-qc/9310027
- G. Chiribella, G. M. D'Ariano, P. Perinotti, *Transforming quantum operations: quantum supermaps*, https://arxiv.org/abs/0804.0180
- T. Morimae, *The process matrix framework for a single-party system*, https://arxiv.org/abs/1408.1464
- S. Lloyd et al., *Quantum mechanics of time travel through post-selected teleportation*, Phys. Rev. D 84, 025007 (2011), https://doi.org/10.1103/PhysRevD.84.025007

**このノートのCBSSLは、上記文献で確立された法則ではない。今回新しく定義したtoy physical lawである。**
