# NUTの戻り経路と環境：密閉周回の障害・実計量の放射応答・新鮮な環境の代価

**2026-09-23。読取基点：main `1b43a09eb67ae97fce3d2076c37f82743a0df702`（PR #13マージ後）。**
[前回の場・背景source](field-feedback-background-response.md)と[接続検査](chronology-loophole-attack.md)の続き。
今回は任意の減衰率をNUTの予測として置かず、戻り部の環境を保持した検査と、実際のNUT外部領域の応答を分けて計算する。

## 0. 結論と採否

| 対象 | 今回の結果 | 範囲 |
|---|---|---|
| 場と再利用環境を一つの密度行列として閉じ、測定記録を使わないunitaryで戻す | **固定送信0・1の各々について棄却** | 独立準備された受信probe、非零のWeyl交換子、全結果の保持。戻りunitaryは任意で、Aの保存・Gaussian性・有限分散は不要 |
| 前回の減衰を同じ有限bathの再使用で実現 | **その置換は不成立** | bathの出力と相関まで保持すると、捨てたはずの雑音が残る |
| 新しいthermal bathを毎回供給する一mode比較模型 | **全一modeに正常な定常状態が存在** | 前回の一観測量だけの対照から前進。実際のNUT reservoirの構成ではない |
| 実NUTの径方向に放射を逃がす | **外向き応答を具体的に計算、非零** | exact metricのスカラーODE、明示したoutgoing境界条件。大域retarded核やbath状態ではない |
| 定常NUT bathを無記憶の環境として一周使う | **自動的な採用は不可** | single-valued neutral observableのKilling周期に相関が再来する。短時間近似や全ての非定常環境を禁止しない |
| 環境・装置・背景を含む物理的過去通信 | **成立例は得ていない** | 密閉型は上の仮定でFAIL。開放型に必要な相関・応答・装置sourceは明確化したが、全弦理論のNOではない |

既存のKRWによるTaub準備案の棄却を維持するが、NUT-onlyへ転用しない。
会話の「可能10%」を校正済み確率として扱わず、検査数で機械的に減らさない。
以下の純度・Weyl・コンパクト性の議論は自己完結した条件付き証明。新しい基本法則や優先権を主張しない。

## 1. 密閉した環境まで戻す場合：任意のunitary混合にも残る障害

コード：[closed_reservoir_return.py](../src/symbolic/closed_reservoir_return.py)。
前回と同じ局所の場・probeを使う。実smearingによる場の演算子を

```math
[A,B]=i\delta_c\mathbf1,\qquad
M_y=\frac12(e^{-iB}-iy e^{iB}),\quad y=\pm1,
\qquad D_r=e^{irA}
```

とする。ここでA,Bは事象ではなく場の演算子、delta_cは背景パラメータdeltaと別。
受信probeは場＋環境と独立な `|+x>`。Y測定記録は保持し、結果の選別はしない。

### 1.1 今回外す仮定、残す仮定

循環する場Fと再利用環境Eの状態を、正・trace 1のtrace-class密度演算子rho_FEとする。
F–Eの初期相関は任意でよい。通常の有限mode bosonic模型や、密度行列で記述できるbathを含む。
Weyl表示はregularとする。局所場の一般のtype-III代数を、無断でこのtype-I記述と同一視しない。

固定送信r=+1または−1について、戻り部U_rはF＋Eの**任意のunitary**でよい。
Aを保存する必要も、線形・Gaussian・passiveである必要もない。ただし次を要求する。

- 戻り部が測定結果yまたは受信probeのcoherent recordへアクセスしない。
- 循環する環境を捨てて新品へ交換せず、rho_FE自体が一周の固定状態になる。
- 同じループ内で任意に状態を再正規化する規則を追加しない。

測定記録を使う能動的な回復、初めからprobeが相関している準備、開放された無限bathの代数的定常状態は、この命題の外。
特に**単発の開放実験に、全宇宙の密度行列の固定点を要求する命題ではない**。

### 1.2 純度恒等式からの証明

固定送信では記録を足した操作が

```math
\sum_yM_y\rho M_y^\dagger
=\tfrac12(e^{-iB}\rho e^{iB}+e^{iB}\rho e^{-iB})
```

なので、一周mapは

```math
\mathcal C_r(\rho)=\tfrac12(\tau_++\tau_-),\qquad
\tau_\pm=U_rD_r e^{\pm iB}\rho e^{\mp iB}D_r^\dagger U_r^\dagger.
```

rhoはtrace-classなのでHilbert–Schmidtであり、無限次元でも

```math
\operatorname{Tr}\rho^2-\operatorname{Tr}\mathcal C_r(\rho)^2
=\tfrac14\|\tau_+-\tau_-\|_2^2.
```

固定状態なら左辺0。従ってtau_+=tau_-であり、共通のU_r,D_rを消すと

```math
e^{2iB}\rho e^{-2iB}=\rho.
```

一方、Weyl関係は

```math
e^{-2iB}e^{isA}e^{2iB}=e^{-2is\delta_c}e^{isA}
```

を与える。したがって `chi(s)=Tr(rho exp(isA))` は

```math
(1-e^{-2is\delta_c})\chi(s)=0,\qquad\chi(0)=1
```

を満たす必要がある。delta_c≠0なら、例えば `s_n=pi/((2n+1)delta_c)`、n≥1でchi(s_n)=0だがs_n→0。
これはregularityの連続性と矛盾する。

> **結論：上の密閉・記録非使用の戻り構成には、delta_c≠0のとき、固定送信のいずれについても正規化された密度行列の周回固定点がない。**

これは前回のA保存型no-goを、**任意の戻りunitaryと、任意に相関した再利用bath**へ拡張する。
有限分散も有限エントロピーも仮定しない。一般の代数的定常状態や、記録を戻す相互作用までは排除しない。
コピー／NOTでは測定結果に応じた操作が入り、同じrandom-unitary分解ではない。任意Uでコピー／NOTまでこの純度証明を移植しない。
それでも、同一構成の「固定0」「固定1」が成立しないことは、この方式による符号化の採否には十分である。

### 1.3 有限Fock cutoffに現れる偽の固定状態

d次元へ切ると、random-unitary channelには `I_d/d` という固定状態がある。
しかし正準CCRを有限行列で正確には表せず、上のWeyl平行移動の連続性の議論を代替しない。
oscillator Hamiltonian `H=N+1/2` のこの状態のエネルギーはd/2であり、cutoffを増やすと発散する。
**小さいFock行列に定常解が出たことを、本来のbosonic密度行列の存在証明にしない。**

## 2. 同じbathを再利用すると何が残るか

前回の比較規約を `A=alpha P, B=beta Q`, `[Q,P]=i` とする。
測定のP分散増分はbeta²。q方向の条件付き変位はPと可換なので、これは固定0・1・copy・NOTで共通。
beam splitterでPとbathのP_Eを混合する場合、その全共分散は

```math
V_{P,\mathrm{new}}=O\left[V_P+\begin{pmatrix}\beta^2&0\\0&0\end{pmatrix}\right]O^T,
\qquad O^TO=I.
```

F–E相関を保持すれば `Tr V_new=Tr V+beta²`。系だけの見かけの減衰でこの増分は消えない。
eta=1/4、beta=3/5、初期 `V_P=I/2` の例では、同じbathを6回使うと `V_P=1.58 I`。
このOは60度のmode混合でO^6=Iだが、共分散は戻らない。

毎回productの新しいbath（分散v_E）を入れる模型なら

```math
V_{P,*}=v_E+\frac{\eta\beta^2}{1-\eta}.
```

しかし同じ定常入力から出るbathには

```math
V_{P_E,\mathrm{out}}=v_E+\beta^2,\qquad
\operatorname{Cov}(P,P_E)_{\mathrm{out}}
=-\sqrt{\frac{\eta}{1-\eta}}\,\beta^2
```

が残る。上の数値では系0.62、bath0.86。bathを再度0.5かつ無相関として使う処理が、従来の減衰mapに隠れていた。
これは通常のcollision modelの「使用済みancillaを捨てて交換する」という仮定 [C1,C2] に対応する。
**P方向の雑音収支は、任意フィードバックでの総熱量の正の下限ではない**。Qへの制御が仕事・冷却を伴い得るため、熱と呼ぶには両quadratureと装置を含める必要がある。

## 3. 新しい環境が供給される場合の肯定対照を、全一modeへ完成する

この節だけは**比較模型**。NUTからetaやthermal stateを得たものではない。
標準thermal attenuator [G] を各操作の後に置き、`0<=eta<1`, `v_E>=1/2` とする。

### 3.1 固定送信には明示的な正常固定状態がある

`c=sqrt(eta)`, `mu_r=-r alpha c/(1-c)` とすれば、全二quadratureの特性関数は

```math
\chi_{r,*}(s,t)
= e^{i\mu_rs-v_E(s^2+t^2)/2}
\prod_{j=1}^{\infty}\cos(\beta c^j t).
```

thermal密度行列をQ方向へmu_rだけ変位し、P方向へ
`sum_{j>=1} beta c^j epsilon_j`（独立な公平符号epsilon_j）だけランダム変位した混合状態である。
符号級数は絶対収束し、正・trace 1のnormal stateを構成する。単なる一変数のBochner正定値性ではなく、量子状態の混合としての構成。

```math
\langle Q\rangle=\mu_r,\quad V_Q=v_E,\quad
V_P=v_E+\frac{\eta\beta^2}{1-\eta},\quad
\langle H\rangle=v_E+\frac{\mu_r^2}{2}
+\frac{\eta\beta^2}{2(1-\eta)}.
```

alpha=0.7、beta=0.6、eta=1/4、v_E=1/2では `<H>=0.805`, `V_P=0.62`。
無限積の尾部誤差は `beta² t² eta^(N+1)/(2(1-eta))` 以下。
全特性関数の再帰式と両二次モーメントを50/80桁で検査した。有限Fock切断ではない。

### 3.2 copy／NOTにも少なくとも一つの有限エネルギー固定状態がある

Gaussian閉包を使わずに存在を示す。`H=(Q²+P²)/2` として、前回のKraus mapから

```math
\langle H\rangle_{\mathcal E_f(\rho)}
\le(1+\epsilon)\langle H\rangle_\rho
+\frac12(\alpha^2+\beta^2+\alpha^2/\epsilon),\quad\epsilon>0.
```

理由は `D_r^dagger Q D_r=Q-r alpha`、`sum r_y M_y^dagger M_y=F_f(Q)`、`|F_f|<=1` と、
`2|alpha Q|<=epsilon Q²+alpha²/epsilon`。Pの増分はbeta²。
attenuator後はエネルギーがeta倍され、`(1-eta)v_E` が加わる。
eta>0に対しepsilon=(1−eta)/(2eta)を選ぶと

```math
E_{n+1}\le a E_n+b,\qquad a=(1+\eta)/2<1,
```
```math
b=\frac\eta2(\alpha^2+\beta^2)
+\frac{\eta^2\alpha^2}{1-\eta}+(1-\eta)v_E.
```

従って反復状態のエネルギーは一様に有界。oscillatorの有限エネルギー集合はtrace normでcompact：
最初のN個のFock状態への射影をPi_Nとすると、外側確率は `E/(N+1/2)` 以下、射影誤差はその平方根の2倍以下。
有限次元部分のcompactnessと合わせる。
Cesaro平均rho_bar_Nの収束部分列を取り、CPTP写像のtrace-norm連続性と
`||C(rho_bar_N)-rho_bar_N||_1<=2/N` を使うと、正・trace 1・有限エネルギーの固定点が得られる。
eta=0はthermal stateへの完全resetで直接成立する。

これは**固定点の存在**であり、一意性や各反復の収束率の証明ではない。新鮮な環境を含む大域NUT実験の存在証明でもない。
数値例の存在に用いるエネルギー上界は `b/(1-a)=1.392222...`。

### 3.3 固定状態の違いを「選んだbitが届く」にしない

上の二つの固定設定状態を別々に選ぶと、受信Y分布の距離は比較例で0.519519876175339...。
一方、一つのincoming stateと**独立に保持された設定flag**から始め、受信後に制御する実験なら

```math
P(F=f,Y=y)=q_f\operatorname{Tr}(M_y\rho M_y^\dagger).
```

flagとの識別差は0。これは前向きinstrumentの正規化からの結果で、全ての大域的相関処方の禁止ではない。
**全一modeの定常状態を作れたことを、過去の選択bitを運ぶ実験の証明と混同しない。**

## 4. 実際のNUTには放射の逃げ先があるか：外向き応答を計算する

コード：[nut_outgoing_reservoir.py](../src/symbolic/nut_outgoing_reservoir.py)。
同じexact metric [J] の第一NUT、x>1を使う。

```math
p=x^2-1,\quad D=(x+\delta)^2-a p,\quad a=4/(k+2),\quad K=(k-2)\alpha',
\quad t\sim t+T,\quad T=4\pi\lambda.
```

中性single-valued scalarの時間modeは `omega_n=n/(2lambda)`。
Hopf束の接続を含む角関数はmonopole harmonics [W] で、
`q=lambda omega_n=n/2`, `ell=|q|,|q|+1,...`, `L²=ell(ell+1)-q²`。
これは診断用scalarの大域的角ラベルで、full string spectrumやBRST認定ではない。
コードはn=2,ell=1,m=0の角関数sin(theta)も直接検査する。奇数nに不可能なm=0を使わない。

径方向方程式は

```math
\partial_x(p\partial_xR)+[\omega^2D/p-L^2]R=0.
```

無限遠の指数は `R~x^(-1/2±is)`、

```math
s^2=\omega^2(1-a)-L^2-\tfrac14.
```

repoの `k=8,delta=sqrt(8/5),lambda=sqrt(2/5)`、最小角枝ell=n/2、n>0では

```math
s_n^2=(3n^2-4n-2)/8.
```

n=1は−3/8でevanescent、n=2,3,4はそれぞれ1/4,13/8,15/4で伝播可能。
この三つの指数自体は旧ノートの候補と整合し、新発見として数えない。
**今回追加したのは外部領域のDirichlet-to-Neumann応答である。**

### 4.1 外向き境界条件を明記したexact解

`z=2/(x+1)`, `h=1/2-is`, `v=-i omega(1+delta)/2` と置き、

```math
R_{\rm out}(x)
=(z/2)^h(1-z)^v\,{}_2F_1(h-i\omega,h-i\omega\delta;2h;z).
```

無限遠で `R_out~x^(-1/2+is)` の単位係数。e^(−i omega t)規約で外向きである。
方程式のhypergeometricへの変換を厳密代数で検算し、別に元のODEの微分残差を調べた。
この境界条件は**外へ放射する候補環境として今回加えたもの**であり、full CFTから一意に選ばれた真空条件とは呼ばない。

境界x=x_b>1での応答を

```math
\mathcal Y_n(x_b)=p(x_b)\frac{R_{\rm out}'(x_b)}{R_{\rm out}(x_b)}
```

と定義する。保存流束は `j=p Im(R* R')=s`。
よって

```math
\boxed{\operatorname{Im}\mathcal Y_n(x_b)=s/|R_{\rm out}(x_b)|^2>0.}
```

j≠0なのでRは実x>1上で0にならず、この応答は有限。
50/80桁の結果（同じ規約、x_b=2）：

| n | Re Y_out | Im Y_out |
|---|---:|---:|
| 2 | −0.34060037974395681714 | 4.09378655935067070657 |
| 3 | −0.31981763651124485449 | 6.91764616077312155639 |
| 4 | −0.34232693067599695226 | 9.36074977888544297641 |

**任意の減衰パラメータを選んだ数表ではなく、実際のNUTスカラー作用素と明記した外向き境界からの数値である。**
ただしこれは伝送確率でも、etaでも、背景破壊率でもない。
相関関数のnoise部分・入射状態・実験時間順序は供給せず、大域的retarded kernelとも同一視しない。

### 4.2 放射する応力は非零で、装置との収支が必要

g_E=sqrt(D)g、`sqrt(-g_E)g_E^xx=K p sin(theta)`。
角関数を規格化し、境界振幅u_bの実場 `Re[u_b R(x)/R(x_b) exp(-i omega t)Y]` について、
Killing周期平均の外向きエネルギー流束は

```math
\mathcal F_n=\frac{K\omega_n}{2}|u_b|^2\operatorname{Im}\mathcal Y_n>0.
```

場を無限遠へ出す機構は、幾何学的には塞がれていない。
反対に、この正の外向き流束を「環境をtraceするだけ」の無応力な処理とは見なせない。

## 5. 周期時空のbathは、同じ場所へ戻ると同じ相関を持つ

NUTの周期Killing作用をalpha_tとする。
single-valued neutral scalarの大域代数が存在し、この作用と共変なら `alpha_T(X)=X`。
smooth smearingされた浴の観測量Xについて

```math
C(t)=\omega(X\alpha_t(X)),\qquad C(T)=C(0).
```

平均を引いた相関にも同じ式。定常状態ならFourier周波数はomega_nに離散化される。
分散が有限で非零なら、相関は一周ごとに厳密に再来し、時間軸全体で絶対可積分な減衰相関にはならない。
規格化した相関を単純な `exp(-kappa t)` で近似すると、一周時点の誤差は少なくとも `1-exp(-kappa T)`。

これは**定常な背景bathの相関**への主張で、相互作用する実際の戻りmapをidentityと仮定する主張ではない。
一周より短い区間の局所的減衰、非定常な装置、異なる空間部分を使う環境、recordを介した非Markov相互作用は自動排除しない。
[J]の周期性を、globalなR時間coverや常に新鮮なtime-binの供給と取り違えない。
[C1,C2]のMarkovian collision modelでは、使用済みunitの交換と無相関性を明記している。
**非零のoutgoing radial応答があることと、無記憶bathを一周供給できることは別**である。

## 6. 背景・装置を含めて課す、具体的な収支条件

前回のWard恒等式は `nabla_a T^a_b=O_Phi partial_b Phi+f_b`。
f_bは装置・switching等との力の交換。
今回のstationary背景でxi=partial_tとするとxi(Phi)=0なので、

```math
J^a=-T^a{}_b\xi^b,\qquad\nabla_aJ^a=-f_b\xi^b.
```

したがってスカラー応力が一般のg-frameで単独保存されなくても、source-freeな部分のKillingエネルギー流は保存する。
これはdilaton sourceを捨てた重力方程式が正当化される、という意味ではない。

区間 `[x_L,x_R]` とその上の全Hopf fibre・角方向、すなわち `[x_L,x_R]×S³` にStokesを使う。
周期方向に時間の端面はなく、**存在しない大域的spacelike t=constant面を仮定する必要はない**。
外向きの符号をそろえると、境界流束差は装置が場へ渡すKilling仕事の周期積分に等しい。
装置・環境を含む全sourceが定常・周期的で保存されるなら、全境界流束は相殺される必要がある。

これにより、密閉して入力・仕事・境界流を全て0としながら、正の平均放射だけを維持する案は不適合。
一方、内側からの入射、外部駆動、別のエネルギー流を許す開放系までこの収支で禁止しない。
測定記録のresetに伴う相関処理や仕事も、独立のphysical instrumentとしてsourceへ含める必要がある。

**今回得ていないもの：** 全背景多重項の応答delta g,delta Phi,delta B,delta gauge field、装置のstress、全bath二点関数、全noise kernel、大域的記録の同時分布。
exact k=8の背景へ最低次のEinstein方程式だけを代入してfull heterotic backreactionと呼ぶことはしない。
外向き応答を元に必要なsourceを特定した段階で、CTCが反作用で消えるか残るかを計算済みにはしない。

## 7. 再開条件と再現

今回の採否は、**記録非使用の密閉unitary戻り案をFAIL**、外部reservoirを供給する案を**具体的な開放系の入力を要する別案**とする。
後者を再検討する場合、任意etaを足す代わりに、上のY_nを含む外部応答と整合するpositiveかつ局所極限の正しいbath状態、周期相関を含む戻りinstrument、装置・環境の境界流を一緒に指定する。
その条件で固定0／1、copy／NOT、保持flagの全結果を計算する。全BRST分類を自動的に先行必須へ戻さない。

```bash
python src/symbolic/closed_reservoir_return.py
python src/symbolic/nut_outgoing_reservoir.py
```

ローカル：Python 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0。独立2本の全assertが成功。
純度・Kraus・Weyl・bath共分散・Lyapunovの代数、radial作用素変換・保存流束を厳密検算。
外向き応答はn=2,3,4、x=2,3,7で元のODE・流束を検査し、50/80桁で40桁以上一致。
80桁最大残差はODE約1.23e−79、流束約1.27e−80。全一mode固定状態の特性関数も50/80桁で検査。
無限積には尾部上界を使用。高精度浮動小数と一致検査であって、全丸め誤差のinterval証明ではない。

初回の有限行列計算は時間上限に達し、共通積を段階的にexpandして再計算。hypergeometric残差の構造比較と、平方根の形の違いによるassertも、式の差の厳密簡約に修正した。仮定・精度・対象・assertを弱めていない。
local cloneはDNS失敗のため全repoのlocal実行は未実施。固定SHAをGitHub connectorで読み書きする。
新規2本は共有import・入力dataなし。既存code・参照data・依存・workflow・Leanは変更しない。
remoteでは通常のPR累積差分選別器を使い、実際のSHA・対象・run・最終結果をPRへ記録する。
純度による無限次元no-go、compactnessによる存在、Stokesの大域議論をPythonやLeanで形式証明したとは報告しない。

## 一次資料と確認範囲

- **[J]** C. V. Johnson, H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, [hep-th/0405141](https://arxiv.org/abs/hep-th/0405141)。PDF (72)–(73)、monopole connection、既存repoのdilaton規約を照合。全alpha-prime背景とprobe応答は別。今回p.24–25のweb screenshotは取得エラーで、ページ画像確認済みとはしない。
- **[C1]** F. Ciccarello, G. M. Palma, V. Giovannetti, *Collision-model-based approach to non-Markovian quantum dynamics*, [1207.6554](https://arxiv.org/abs/1207.6554)。公式abstractでbath相関・再使用とMarkov/non-Markovの区別を確認。全master equationの再導出は行わない。
- **[C2]** A. Corr, S. Cusumano, G. De Chiara, *Continuous Variable Structured Collision Models*, [2503.03832v2](https://arxiv.org/html/2503.03832v2)。HTML §2.1–2.2、特に初期product covarianceと各unitの交換、§3のsecondary environmentを確認。環境内部が複雑でも新しいunitの供給は追加仮定である。
- **[G]** Z. Van Herstraeten, S. Guha, N. J. Cerf, *Classical capacity of quantum non-Gaussian attenuator and amplifier channels*, [2312.15623v2](https://arxiv.org/html/2312.15623v2)。HTMLのbeam-splitter dilation、thermal environment、displacement covarianceを確認。今回のfeedback固定状態を同論文の結果と称さない。
- **[W]** T. T. Wu, C. N. Yang, *Dirac monopole without strings: Monopole harmonics*, Nuclear Physics B 107 (1976), 365–380, [DOI](https://doi.org/10.1016/0550-3213(76)90143-7)。書誌・公式abstractのbundle sectionとしての角関数を確認。n=2の角固有値と今回の径方向式はコードで直接検算。

検索はNUTのreservoir、collision model、periodic correlations、monopole harmonicsに限定。2026年までの全研究の網羅や、他の実現方式の不存在を証明するものではない。
