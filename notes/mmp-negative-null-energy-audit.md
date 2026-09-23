# 追加の負のnullエネルギーは供給できるか：状態の構成とQEIによる支持限界

**2026-09-23。読取基点：PR #16 head `2c2efbb683f4a8f661de743e2ad9fcaec04b215d`。**
[時間差付きMMP・相対モードの先行監査](mmp-timeshift-relative-mode-audit.md)の§6を継続する。

> **結論：負のエネルギーパルスを持つ正規化された量子状態は構成できる。しかし、同じ透明な2D共形場・時間ホロノミー・先頭JT近似を保つ状態準備だけでは、失われた通過条件を救えない。**
> 信号の全通過経路で必要なのは重み付きnull積分 `I_total<0`。chiral周期がその経路を一周以上含む場合、状態非依存の量子エネルギー不等式（QEI）と共形異常から `I_total>=0` となる。
> 標準NS真空だけの否定を、同じ共形理論内で許容される非定常状態・混合・相関を含む範囲へ広げた。**全4Dの外部量子場・能動的な境界変更・時間依存する口・自然界一般の禁止ではない。**

## 0. 対象と到達点

| 問い | 答え |
|---|---|
| 負のエネルギーを持つ実際の状態を書けるか | **同じCFT内で書ける。** smoothな円周微分同相を実装するunitaryで真空を励起。自由fermion二点関数からも応力を検算 |
| 準備操作と仕事は書けるか | **理想的な2D制御Hamiltonianと、その仕事を書ける。** 4DのMMP装置の製造・stressを構成したのではない |
| パルスの強さ・形・非Gaussian性を変えると救えるか | **下記の条件下では不可。** 特定のパルス族ではなく、QEIの対象状態全体の下限で排除 |
| 測定・後選別・環境相関ならどうか | 同じ場の許容状態として評価する限り、各正規化された状態にも混合にも同じ下限。確率を負のsourceへ読み替えない |
| この結果で全4Dの負エネルギー源を排除したか | **していない。** 2D null QEIを4Dのnull線へ無条件に移植するのは誤り |

既存のNUT証明は変更・転用しない。新しい基本定理や優先権を主張せず、既知QEIを先行のJT通過条件へ接続する。

## 1. 維持する模型、外した状態の制限

`hbar=c_light=1`。先行ノートの光学座標と先頭近似を維持する：

```math
ds_2^2=r_e^2\sec^2\sigma(-d\tau^2+d\sigma^2),\quad
\tau_w=\pi\ell,\quad -\pi/2<\sigma<\pi/2.
```

短縮方向の信号は `D=partial_tau+partial_sigma` に沿って直接通過する。
各透明な共形チャネルの光学長 `C_nu=tau_w+d_nu`、`d_nu>=d>0`、定常時間ホロノミー `Delta>=0` は固定。
field theoryを通常の正のHilbert空間で定義する段階は、先行ノート同様 `Delta<min C_nu` のspacelike helical cylinder側である。
**その後のnull/timelike同一視へ真空・QEIを解析接続しない。**

標準真空だけでなく、同じunitary positive-energy chiral CFTの許容状態を認める。[Q]のVirasoro表現とstress変換則を使う。
まずstress期待値がsmoothで有限の円周エネルギーを持つ状態で示す。QEIの閉じた二次形式のdomainと、積分が定義されるnormal混合へ拡張する。
無限エネルギー・未定義の応力を、半古典背景を支える有限sourceとして認定しない。正規状態の全分類は不要。

状態は非定常でも、左右のsectorや装置とentangledでもよい。相互作用を切った後の同じCFTの状態として通過経路に供給することが前提。
準備中の装置が経路上のfield equation・境界条件・計量を変え続ける場合は、新しい模型として全sourceを入れ直す必要がある。
各チャネルの中心電荷を `c_nu>0`、総和を `c_eff` と書く。異なる磁力線を正の重みで平均する場合も同じ。

## 2. 喉の必要量を、正しいchiral成分の量子演算子へ移す

先行ノートのJT null拘束は任意のsourceについて

```math
B_L(\tau_0)+B_R(\tau_0+\pi)=-\kappa I_\rho,
\quad
I_\rho=\int_{-\pi/2}^{\pi/2}\cos^2\sigma\,
\langle\widehat T_{DD}\rangle_\rho\,d\sigma,
\quad \kappa>0.
```

従って同じ信号の入口・出口の両方に正のleading係数を持つには **`I_rho<0`** が必要。
コードはChristoffel記号から一般のnull拘束を再検算し、特定のsourceや斉次JT解に依存させない。

一つのチャネルについて、光学null座標を `v=t+z`、起点を0に取る。ray上では

```math
v=2\ell(\sigma+\pi/2),\quad 0\le v\le2\tau_w,
\quad L=C+\Delta.
```

`L` はこの成分のchiral周期。情報パルス自体の `u=t-z` 成分ではなく、null拘束が測る反対chiral成分を使う。
[M, Appendix F (F.29)]の共形異常は

```math
\widehat T_{DD}=4\ell^2 T^{\rm cyl}_{vv}(v)+\frac{c}{12\pi}.
```

traceに比例する項はnull収縮で消えるが、右のtracelessな異常項は消してはいけない。
従って

```math
\boxed{I_\rho=\frac c{24}+2\ell\int_0^{2\tau_w} w(v)\langle T(v)\rangle_\rho\,dv,}
\quad w(v)=\sin^2\!\frac{v}{2\ell}.
```

ここで `T=T_vv^cyl`、真空では `T_0=-pi c/(12L^2)`。
前回の不足量は `I_0=c[1-4 tau_w^2/L^2]/24` であり、この規約と一致する。

## 3. 円周QEIを導出する：直線の不等式を誤用しない

[Q, §2 (2.7)–(2.11), Theorem 4.1]のchiral変換則とpositive-energyスペクトルを用いる。
物理座標v、円周Lで

```math
U(F)T(v)U(F)^\dagger=F'(v)^2T(F(v))-
\frac c{24\pi}\{F,v\},\qquad
\int_0^L T(v)dv\ge-\frac{\pi c}{12L}.
```

正のsmooth periodic weight `h>0` に対し

```math
J_h=\int_0^L\frac{dv}{h(v)},\quad
F'(v)=\frac{L}{J_h h(v)},\quad F(v+L)=F(v)+L
```

と選ぶ。これは正則な円周微分同相で、unitaryに実装できる。
変換した重み付き演算子の第一項は `(L/J_h) integral T` となる。
また

```math
\{F,v\}=-\frac{h''}{h}+\frac12\frac{h'^2}{h^2},\qquad
\int_0^L h\{F,v\}dv=\frac12\int_0^L\frac{h'^2}{h}dv.
```

ゆえに次の円周版を得る：

```math
\boxed{\int_0^L h\langle T\rangle_\rho dv\ge
-\frac{\pi c}{12J_h}-\frac c{48\pi}\int_0^L\frac{h'^2}{h}dv.}
```

smoothで正のhでは変換真空がこの下限を達成する。これは[Q]の基本変換・スペクトルからの本ノートの再導出で、円周項を無断で落としていない。

### 3.1 信号区間がchiral周期を巻かない場合

**`L>=2 tau_w`** とする。上のwを円周の残りでは0に延長する。
`L>2 tau_w` なら、積分を行わない開いた弧があり、`h=w+epsilon` に対する `J_h` はepsilon→0で発散する。
`L=2 tau_w` でもwは一点で二次の零を持つため `J_h` は発散する。

wの0延長はC1で、sqrt(w)はH1。適用はsmoothな非負weightからの極限として行う。
具体的にはsqrt(w)をH1と一様normでsmooth近似し、二乗し、正のepsilonを加える。固定epsilonの極限後にepsilon→0とする。
stress期待値がsmoothなら左辺は一様近似で収束し、右辺のDirichlet積分もこのH1極限で収束する。
未定義の不連続smearingを直接量子演算子へ代入する手順ではない。

結果は

```math
\int w\langle T\rangle_\rho dv\ge
-\frac c{12\pi}\int\left(\frac d{dv}\sqrt w\right)^2dv
=-\frac c{48\ell}.
```

よって異常項と合わせて

```math
\boxed{I_\rho\ge\frac c{24}+2\ell\left(-\frac c{48\ell}\right)=0.}
```

**必要条件I<0と両立しない。** あるパルスを最適化した結果ではなく、許容状態全体への下限である。
異常を落とした計算なら負値だけが残り、偽の救済となる。

### 3.2 MMPの時間差に戻す

`Delta>=tau_w-d` なら、全てのチャネルで

```math
L_\nu=\tau_w+d_\nu+\Delta\ge2\tau_w.
```

各reduced stateへ上の不等式を適用して加えると、相関の有無によらず `I_total>=0`。
従って前回の通過条件

```math
\Delta<\tau_w-d
```

は、**標準真空だけでなく、この同じCFTの許容状態を用いる準備**にも必要である。
前回と同じ直接通過・固定時計対応なら、外部を通って元の実験室へ戻る時間は `>2d+tau_read`。
証明を使ったのはCTC形成前の円筒側であり、post-CTC時空の存在を仮定してNOとしたのではない。
連続にこの先頭構成を保って時間差を増す経路は、状態の操作だけではこの障害を越えられない。

### 3.3 長いMMPワームホールを誤って排除しない対照

`L<2 tau_w` では、同じrayがchiral円周を巻く。wを直線上で0延長して円周上の一価なweightと扱うことはできない。
正しいweightはperiodized sum `sum_n w(v+nL)` で、零を持たない場合にはCasimir項が残る。
例えば `tau_w=1,L=5/4,Delta=0` の真空は `I_0=-13c/200<0`。
また `L=tau_w` なら二つの重みの和は `sin^2+cos^2=1`、`I_0=-c/8` とMMPの基準を再現する。
コードは巻く場合の非巻きQEIの使用をValueErrorで拒否する。**通常の長いMMP解の存在に反する定理ではない。**

## 4. 有限の準備エネルギーなら、境界I=0にも余裕が残る

一つのチャネル、`g=L-2 tau_w>0`、`E_rho=integral T` が有限とする。
円周真空に対する理想準備仕事を `W_prep=E_rho+pi c/(12L)>=0` と定義する。
これは当該chiral Hamiltonianに入る仕事で、4D電源・口の駆動・冷却の総費用ではない。

前節の正則化weightで次の積分が厳密に求まる：

```math
J_\epsilon=\frac g\epsilon+\frac{2\tau_w}{\sqrt{\epsilon(1+\epsilon)}},
\qquad
D_\epsilon=\frac{\pi^2}{\tau_w}
[1+2\epsilon-2\sqrt{\epsilon(1+\epsilon)}].
```

`integral(w+epsilon)T=integral wT+epsilon E_rho` を使うと

```math
I_\rho\ge\frac c{12}[\sqrt{\epsilon(1+\epsilon)}-\epsilon]
-\frac{c\tau_w}{6J_\epsilon}
-\frac{2\tau_w\epsilon E_\rho}{\pi}.
```

`1/J_epsilon<=epsilon/g` と `sqrt(epsilon(1+epsilon))>=sqrt(epsilon)` により

```math
I_\rho\ge\frac c{12}\sqrt\epsilon-A\epsilon,\quad
A=\frac c{12}+\frac{c\tau_w}{6g}+\frac{2\tau_wE_\rho}{\pi}>0.
```

`A=c/12+c tau_w/(6g)-c tau_w/(6L)+2 tau_w W_prep/pi` なので正。
`√epsilon=c/(24A)` を選べば

```math
\boxed{I_\rho\ge\frac{c^2}{576A}>0.}
```

これは便宜的で必ずしも最適ではない有限エネルギー下界。仕事を無制限に増やしてもI<0へは入れず、有限仕事ではI=0にも達しない。
多チャネルへは各チャネルの有限エネルギーに対して加算できる。少数の値からの外挿ではなく、上の解析的不等式が根拠。

診断値 `c=1,tau_w=1,L=9/4` では、W_prep=0,0.1,1,10に対応するI下界は
`0.00256849315, 0.00234740334, 0.00132270527, 0.000246532324`。
単位を固定した比較値で、自然界の確率や実装のジュール数ではない。

## 5. 負のパルスの具体的な状態と準備操作

コード：[conformal_negative_energy_preparation.py](../src/symbolic/conformal_negative_energy_preparation.py)。
円周上で、`0<=a<1`、整数 `m>=1`、`k_m=2pi m/L` として

```math
F(v)=v-\frac a{k_m}\sin[k_m(v-v_c)],\quad
F'(v)=1-a\cos[k_m(v-v_c)]>0,
\quad |\psi_F\rangle=U(F)^\dagger|0_{NS}\rangle.
```

F(v+L)=F(v)+L。unitarityからnormは1で、smoothな変換なのでNSの局所短距離構造を保つ。
背景・座標を変えず状態を能動的に変えるので、単なる時計の表示替えではない。

```math
\langle T(v)\rangle_F=-\frac{\pi c}{12L^2}F'(v)^2-
\frac c{24\pi}\left[\frac{F'''}{F'}-\frac32\left(\frac{F''}{F'}\right)^2\right].
```

中心では

```math
\langle T(v_c)\rangle_F=-\frac{\pi c}{12L^2}(1-a)^2
-\frac{c a k_m^2}{24\pi(1-a)}.
```

a→1で大きく負になるが、他の場所の正の寄与と必要な準備仕事を捨てない。

自由complex chiral fermion（c=1）の二点関数は、両端に√F'を掛けて引き戻す。
共通位相を除いた対称point-splitting kernelは

```math
K_F(v,\varepsilon)=
\frac{\sqrt{F'(v+\varepsilon/2)F'(v-\varepsilon/2)}}
{2L\sin\{\pi[F(v+\varepsilon/2)-F(v-\varepsilon/2)]/L\}}.
```

短距離展開は `1/(2pi epsilon)-epsilon <T(v)>_F+O(epsilon^3)`。
この独立なfermion計算も同じSchwarzian応力を与える。負のstress tensorを手で処方しただけではない。

### 5.1 装置はどこまで構成したか

smooth switch sを使い `F_s(v)=v-a s sin[k_m(v-v_c)]/k_m` とし、sを0から1へ変える。
そのEulerian vector field `xi_s=partial_s F_s composed with F_s^{-1}` はsmooth。
[Q]の円周微分同相表現では、stressをsmearしたHamiltonian `H_control(s)=integral xi_s(v)T(v)dv` がこの変換を生成する（unitary規約による符号と全体位相は準備時に合わせる）。
物理時間に対しsをC∞でon/offすれば、**2D理論内での理想的な外部駆動による状態準備**になる。

全円周の応力を積分すると、終状態と真空のエネルギー差は

```math
\boxed{W_{\rm prep}=\frac{\pi c}{12L}
\left[m^2\left(\frac1{\sqrt{1-a^2}}-1\right)-\frac{a^2}{2}\right]\ge0.}
```

`1/sqrt(1-a^2)>=1+a^2/2` から正であり、a→1では発散する。
この仕事を供給する外部制御、散乱・有限反射率・ポンプ自身の4D応力は未構成。外部装置を無償な負の重力源とは呼ばない。
ここでは装置費用や雑音を理想化して**肯定側に有利にしても**、作れる状態が§3の下限を越えられないことが決め手である。

### 5.2 数値対照

`c=1,tau_w=1,L=9/4,v_c=1`（先行ノートの `d=1/4,Delta=1`）を使用。

| 準備 | 中心のT(v_c) | 全null積分I | I_extra=I−I_0 | 準備仕事 |
|---|---:|---:|---:|---:|
| 真空 | −0.05171345932 | 0.008744855967 | 0 | 0 |
| m=1,a=0.3 | −0.06966541734 | 0.008407062585 | −0.0003377933822 | 0.0003822081079 |
| m=2,a=0.1 | −0.08785542144 | 0.008164639702 | −0.0005802162654 | 0.001762929273 |
| m=1,a=0.9 | −0.9313594023 | 0.05109300248 | +0.04234814651 | 0.1034581542 |

負の局所エネルギーと、実際に不足を部分的に減らす状態を得た。しかし大きい点状負値が、良い経路平均を意味するとは限らない。
この例で救済が要求する値は `I_extra<-17c/1944`、QEIが許す範囲は `I_extra>=-17c/1944`。
**有限パルス族の探索失敗ではなく、一般下界が厳密な不等号を阻む。**

## 6. どの負エネルギー装置に適用でき、何に適用できないか

squeezing、smoothな外部駆動、測定とfeedback等が**同じ共形場の状態準備**として終わり、その後のrayで同じCFTの応力が評価されるなら、準備手法の違いはQEIを変えない。
ancillaとentangledなら場へ制限したstateに、後選別なら各正規化された許容branchに適用する。branchの成功確率を掛けても、禁止されたI<0のstateは作れない。
これはquantum energy teleportation（QET）を否定する主張ではない。[H]には測定情報と局所操作で負の領域を生む明示的な理論がある。しかしその成果は、この喉が要求する重み付き負値の供給を保証しない。今回はHottaの全プロトコルをMMP上で再現していない。

古典的な装置がray上でNECを満たす追加sourceなら、重みが非負なのでI_app>=0で、救済しない。
別の量子場を追加するなら、その理論・境界・共形異常を含めて計算する。同じ非巻き条件を満たすunitary CFTを増やすだけなら、cに比例する二項が各々相殺してI>=0が残る。
短い新規サイクルや境界相互作用を作ってLを変える場合は、元の模型の単なるstate変更ではない。

**特に4Dへの留保は実質的である。** [R]は4D massless scalarのnull線上の有限区間平均がHadamard状態間で下に有界でないことを示す。
従って本ノートの `c/(12pi)` の2D boundを4Dのsqueezed光へ直接使うことはできない。
それらのfieldを4Dの球平均・横方向smearing・装置応力・高次補正込みで使えるかは、ここでは解いていない。

## 7. 採否・再現・未実施

**同じ先頭MMP/JT、固定時間ホロノミー、透明なunitary共形支持場を保ち、状態を操作して失われた直接通過条件を補う方式はFAIL。**
真空だけの留保は外れたが、4D動的形成、boundary matchingの高次誤差、非共形の量子支持、新しい位相やsewingを含む全方式を排除したとはしない。
I=0の境界は両口のstrict positivityを満たさず、零通過時間の成功例として扱わない。高次補正がこのleadingの境界をどう変えるかも未計算。
過去の受信確率を未定義のまま0と置いた結果ではない。

```bash
python src/symbolic/mmp_negative_null_qei.py
python src/symbolic/conformal_negative_energy_preparation.py
```

ローカル Python 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0 で新規2本の全assert成功。
一般JT null拘束、共形異常、circle QEIの変換係数、finite-work bound、fermion point splittingを厳密代数で検査。
独立な50/80桁の求積で、正則化積分、準備仕事、weighted stress、別の正weightのcircle QEIを確認し、40桁以上一致。
fermion短距離差分には2*dps+40のguard digitsを使い、指定したepsilonで展開誤差を照合。全丸め誤差のinterval証明ではない。

新規2本は独立scriptで共有import・入力ファイルなし。既存の研究code・assert・精度・依存・workflow・Leanは変更しない。
PR #16が未マージなら同PRへ追加する。累積差分のPython対象は先行2本を含む4本になり、最後の2本だけに縮めない。
remoteのSHA・対象・run・結果は完了後のPRコメントへ保存する。
local git接続はDNS失敗のため全repoのlocal再実行はしていない。既知QEIそのものや全解析的証明をLeanで形式検証したとはしない。独立査読も未実施。

## 一次資料と確認範囲

- **[Q]** C. J. Fewster, S. Hollands, *Quantum Energy Inequalities in two-dimensional conformal field theory*, Rev. Math. Phys. 17 (2005) 577–612, [math-ph/0412028v2](https://arxiv.org/abs/math-ph/0412028v2)。PDF §2 (2.7)–(2.11)、§3の円周微分同相・positive-energy表現、Theorem 4.1と§4.1のsharpness/domainを本文で確認。今回のcircle weight、有限仕事下界、MMPへの接続を同論文の既出公式と称さない。
- **[F]** E. E. Flanagan, *Quantum inequalities in two-dimensional Minkowski spacetime*, Phys. Rev. D 56 (1997) 4922, [gr-qc/9706006](https://arxiv.org/abs/gr-qc/9706006)。公式abstractで最適化された負エネルギー下界と状態の構成を確認。係数は[Q]のchiral規約に合わせる。
- **[M]** J. Maldacena, A. Milekhin, F. Popov, *Traversable wormholes in four dimensions*, [1807.04726v3](https://arxiv.org/abs/1807.04726v3)。PDF §5.2–5.3、(5.24)–(5.27)、(5.34)–(5.40)、Appendix F(F.29)を確認。共形異常と円筒Casimirを両方保持し、元論文が時間差付き全解を与えたとはしない。
- **[H]** M. Hotta, *Quantum Measurement Information as a key to Energy Release from Local Vacuums*, Phys. Rev. D 78 (2008) 045006, [0803.2272v3](https://arxiv.org/abs/0803.2272v3)。公式abstractの測定・古典通信・条件付き操作による負エネルギー生成を確認。MMPでの装置実装・詳細な収支の再現なし。
- **[R]** C. J. Fewster, T. A. Roman, *Null energy conditions in quantum field theory*, Phys. Rev. D 67 (2003) 044003; erratum D80 (2009) 069903, [gr-qc/0209036](https://arxiv.org/abs/gr-qc/0209036)。出版社abstractの4D null-averaged QEI不存在とerratum表記を確認。本ノートの2D結果の限界として使い、4D救済の成功とは読み替えない。

[Q],[M]のweb screenshotは取得エラーだったため、ページ画像を確認したとは報告しない。抽出本文の式を確認し、図表から新規数値は読んでいない。
検索は今回のQEI・準備・装置という問いに限定。現代物理全体・全2026年文献・他の実現方式の網羅ではない。
