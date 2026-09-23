# 四次元の支持源を完成できるか：量子状態・有限装置・重力

**2026-09-24 / PR #17マージ後のmain `4355ee092a4e237f14e32e0d8bb89afd19644e9d` からの継続。**

目的は、人間が選んだ情報を過去の受信者へ届ける通信路を、現実の3+1次元時空に作れるか。
[前回の四次元監査](four-dimensional-controlled-past-channel.md)で未供給だった支持源を調べる。
以下は二次元QEIの流用ではない。全四次元の場・応力・Einstein方程式を使う。

## 0. 判定

| 検査 | 結果 | 適用範囲 |
|---|---|---|
| 通常scalarで密度と全圧力を合わせる | **一点では成功。** 異方的スクイーズ波束がEllis要求の全応力比を再現 | Minkowski上の正常な状態。喉全体の支持ではない |
| 同じ状態が作る重力 | **先頭Gの初期拘束と初期加速度を構成。** 一点一致の比較例でも計量は極微小な摂動 | 全時間発展・量子揺らぎ・準備装置込みの解ではない |
| 有限Casimirセルを負の支持源に使う | **指定した支柱付き独立セルは不適合。** 支柱の正エネルギーを無視できない | 近平坦の平行板近似、支柱のDEC。全Casimir構成は否定しない |
| 負のstringを滑らかにし真空偏極で支える | **低曲率共形coreに状態非依存の障害。指定profileは全厚さでtrace不一致** | 境界なし共形場、直線product core。有限ring全体や別物質は対象外 |

**人間が制御可能な過去通信装置は今回も認定していない。自然界全方式の禁止でもない。**
異なる幾何の有利な部分を一台の装置へ合成せず、未取得の過去の受信確率を0と置かない。
既存論文の式、今回の導出、模型の仮定、未実施を区別する。独立査読・Lean形式証明は未実施。

## 1. 正常な四次元量子状態で、全応力の一点一致を構成

コード：[scalar_4d_squeezed_support.py](../src/symbolic/scalar_4d_squeezed_support.py)。
通常の実・質量ゼロ・minimal scalar、Minkowski、符号 `(-+++)`。以下は `hbar=c_light=1`。
場全体を有限Fock cutoffへ置き換えない。全三次元の連続運動量に広がる一つのpacketを使う。

### 1.1 状態・規格化

```math
u_0=\frac{a}{\pi[(a+it)^2+|\mathbf x|^2]},\qquad
u_x=-\sqrt2a\,\partial_xu_0
=\frac{2\sqrt2a^2x}{\pi[(a+it)^2+|\mathbf x|^2]^2}.
```

運動量表示は `f_x=-i sqrt(2) a k_x f_0`、`f_0=a exp(-a|k|)/sqrt(pi|k|)`。
全d³k積分で

```math
\int |f_x|^2d^3k=1,\quad \int |\mathbf k||f_x|^2d^3k=2/a,\quad \Box_4u_x=0.
```

packetのannihilatorをbとし、正規化されたunitary squeeze状態
`|s>=exp[s(b²-b†²)/2]|0>`、`s>0` を使う。
`n=<b†b>=sinh²s`、`m=<bb>=-sinh(s)cosh(s)`。
二点関数の真空との差はu_xからなるsmoothなbisolutionで、Hadamard短距離構造を保つ。
局所負値と完全null平均の区別は[FR]を参照。以下のpacket固有の式は今回の導出。

### 1.2 全応力と、前回の不一致の改善

```math
\langle:T_{\mu\nu}:\rangle=
2n\operatorname{Re}\left(\partial_\mu\bar u_x\partial_\nu u_x-\tfrac12\eta_{\mu\nu}\partial\bar u_x\cdot\partial u_x\right)
+2m\operatorname{Re}\left(\partial_\mu u_x\partial_\nu u_x-\tfrac12\eta_{\mu\nu}(\partial u_x)^2\right).
```

任意の二つの波動方程式の解のbilinear保存恒等式から、全時空で `partial^mu T_mu,nu=0`。
原点では時間微分が零、x微分だけが非零で

```math
\boxed{\langle:T_{\hat a\hat b}:\rangle_0=\operatorname{diag}(-A_s,-A_s,A_s,A_s),\qquad
A_s=\frac{4(1-e^{-2s})}{\pi^2a^4}>0.}
```

これはEllis喉の全応力比と一致する。**前回の球対称packetの圧力不一致を、全ての正常scalarの禁止へ一般化してはいけない。**
空間積分ではmの寄与が相殺され、`E=2sinh²s/a>0`。
中央の密度が負となる中心時間区間の半幅は

```math
t_{\rm neg}=a\tan\left[\frac18\arccos(\tanh s)\right].
```

実際の四次元null ray `(t,x,y,z)=(v,v,0,0)` では

```math
\int_{-\infty}^{\infty}\langle:T_{kk}:\rangle dv
=\frac{4\sinh^2s}{\pi a^3}>0.
```

通常項は実積分、異常項は複素平面の極位置（下半平面に極なし）でも照合。
これはこの平坦背景の状態の結果であり、任意のcurved-space ANECを仮定したものではない。
有限区間の負値を否定する結果でもない。

半径bのEllis要求 `A=c_light^4/(8pi G b²)` に中央の値を合わせると

```math
a=\left[\frac{32(1-e^{-2s})}{\pi}\right]^{1/4}\sqrt{\ell_Pb}.
```

`b=1m,s=.5` なら `a=6.404053467e-18m`、中心負値の持続幅は `5.85959e-27s`、全エネルギーは約 `2.68106e-9 J`。
**大きな一点密度があることと、広く持続する喉を作ることは別。** SI値は公称定数によるスケール診断。

### 1.3 準備操作の境界

一つの正常なoscillatorの正の周波数を `omega_0 -> omega_1 -> omega_0` と四分の一周期だけ変える比較では

```math
M=\begin{pmatrix}0&1/\omega_1\\-\omega_1&0\end{pmatrix},\quad
W=\frac{(\omega_1^2-\omega_0^2)^2}{4\omega_0\omega_1^2}\ge0.
```

`omega_1/omega_0=exp(s)` なら同じsqueezed covarianceを作れる。
ただし、**これを空間tailのある四次元packetへ局所的に実装する有限pumpは構成していない**。
一つのmodeの準備対照を、場の局所装置や無償の負の重力源と同一視しない。

## 2. 同じ量子状態から、初期の四次元重力応答を求める

コード：[scalar_4d_semiclassical_initial_data.py](../src/symbolic/scalar_4d_semiclassical_initial_data.py)。
[ADM]の3+1形式。先頭Gで、初期sliceはR³、lapse=1、shift=0、`K_ij=0`。
`gamma_ij=(1+chi)^4 delta_ij`、`chi=O(G)`。
`t=0` で `T_0i=0` なのでmomentum拘束が成立し、Hamiltonian拘束は

```math
\nabla^2\chi=-2\pi G\rho,\quad
\chi(\mathbf x)=\frac G2\int\frac{\rho(\mathbf y)}{|\mathbf x-\mathbf y|}d^3y.
```

SIではGを `G/c_light^4` へ置換。量子状態を曲率に応じて修正する寄与は形式的には次のG次数。
**全noise kernelを計算して半古典近似を保証したのではない。** 少数modeのスクイーズ状態では特に、平均だけで揺らぎを小さいと認定しない。

### 2.1 異方性を残す解

`q=r/a`、`D=1+q²`、x軸に対する角度thetaを用い、
`rho=a^-4[rho_0(q)+rho_2(q)P_2(cos theta)]` と書く。

```math
\rho_0=\frac8{\pi^2}\left[\frac{n+m}{D^4}+\frac{8q^2[(n+m)q^2+n-3m]}{3D^6}\right],\qquad
\rho_2=\frac{128q^2[(n+m)q^2+n-3m]}{3\pi^2D^6}.
```

`chi=(ell_P/a)²[U_0+U_2 P_2]` の解は

```math
U_l(q)=\frac{2\pi}{2l+1}\left[q^{-l-1}\int_0^q y^{l+2}\rho_l(y)dy
+q^l\int_q^\infty y^{1-l}\rho_l(y)dy\right],\quad l=0,2.
```

コードにはrational/arctanの閉形式を保存。二階微分を方程式へ厳密代入し、別のGreen積分を50/80桁で直接求積する。
原点で正則、`q U_0 -> n`, `q U_2 -> 0`。先頭ADMエネルギーは別の空間積分と同じ `E=2n/a`。

### 2.2 初期拘束だけでなく、全Einstein成分

`S_ij=T_ij`、`S=delta^ij S_ij` に対し

```math
\ddot\gamma_{ij}=4\partial_i\partial_j\chi+16\pi G S_{ij}-8\pi G S\delta_{ij}
```

を初期加速度とすると、先頭Gで `G_00=8pi G rho`, `G_0i=0`, `G_ij=8pi G S_ij` が全て成立。
これは**初期拘束と初期加速度まで**で、全時間の非線形解ではない。

`|rho|<=72(n+|m|)/[pi²a⁴(1+q²)⁴]` という正の球対称包絡から、Newton核の積分を使って

```math
\boxed{\sup_{\mathbf x}|\chi|\le\frac{24}{\pi}(n+|m|)\frac{\ell_P^2}{a^2}.}
```

包絡の角度依存はangle²に線形なので、その両端の多項式不等式も検算する。
`b=1m,s=.5` の比較では上限 `4.180571428e-35`、原点 `2.235078184e-36`。
**同じ状態から得た初期値は、R³上の極微小な重力摂動。喉を生成したデータではない。**
振幅の小ささだけから全未来の挙動や全最小面の不存在を証明したとも言わない。

## 3. 有限Casimir装置の支持部を含める

コード：[casimir_4d_finite_apparatus.py](../src/symbolic/casimir_4d_finite_apparatus.py)。
[C]の四次元Maxwell真空＋DEC支柱を再現。面積A、間隔d、`u=pi² hbar c_light/(720d⁴)>0` として

```math
T^{\rm Cas}_{\hat a\hat b}=u\operatorname{diag}(-1,1,1,-3),\quad E_{\rm Cas}=-uAd,\quad F=3uA.
```

真空応力だけでは板でdivergenceが残る。断面Sの支柱に圧縮 `p=F/S` が必要。
DECを**支柱だけ**へ課すと

```math
E_{\rm strut}\ge\rho_sSd\ge Fd=3|E_{\rm Cas}|,\qquad
\boxed{E_{\rm all}\ge2|E_{\rm Cas}|>0.}
```

板の正エネルギーを足せば増える。Sを小さくしても下限は不変。
`A=1cm²,d=1um` では真空 `-4.33375e-14 J`、支柱下限 `1.30013e-13 J`。
有限端効果は未計算。力と負エネルギーの相対誤差上界をepsilon_F,epsilon_Eとすると、下限は
`[2-3epsilon_F-epsilon_E]|E_0|`。十分小さい補正に対する符号の余裕を明記する。

全保存則・静止・局在性なら `integral T_ij d³x=0` というLaue条件が成り立ち、弱場の遠方質量には全装置のエネルギーが入る[C, §II]。
**独立に釣合う同種セルを集め、負の真空部分だけをFKZの負の線源にする設計は不適合。**
量子物質全体へDECを仮定したり、正の全質量だけで全ワームホールを禁止したりしない。
巨大なセル総和の値を、強重力下で正確に解いた製造費とはしない。

### 3.1 限定された局所テンソルの禁止と、その反例

string接方向をzとし、板の法線が横断面内だけにある正のCasimir混合の強度をUとする。
`rho_C=-U`, `p_x,C+p_y,C=-2U`。
目標 `diag(-Q,0,0,Q)`, Q>0に対し、装置は `rho_app=U-Q`, `p_x,app+p_y,app=2U` が必要。
DECなら和は `<=2rho_app=2U-2Q` で、2Q>0の矛盾。横断面内の回転でも変わらない。

ただし法線をz方向にも許すと、強度 `(3Q/4,3Q/4,Q/2)` のx,y,z Casimir成分に
DECを飽和する `diag(Q,Q,Q,Q)` を足し、目標を**代数的には**再現できる。
実装された装置ではないが、任意のorientationをこの限定禁止で排除できないという負例を保持した。

## 4. 滑らかな負のconical coreの四次元trace

コード：[ring_4d_conformal_core.py](../src/symbolic/ring_4d_conformal_core.py)。
[FKZ]の負の角欠損を動機とするが、これは**無限の直線に平行移動対称な四次元比較**であり、有限toroidal ringの全解ではない。

```math
ds^2=-dt^2+dz^2+dr^2+F(r)^2d\phi^2,\quad \phi\sim\phi+2\pi,
\quad F(0)=0,\ F'(0)=1,\ F'(\infty)=1+\sigma,\ \sigma>0.
```

F>0 on r>0、F''>=0、十分速い曲率減衰とする。四次元の全曲率・Bianchiから

```math
R=-2F''/F,\quad \rho=-F''/(8\pi GF),\quad p_z=-\rho,\quad p_r=p_\phi=0,
\qquad \boxed{\mu=2\pi\int\rho Fdr=-\frac{\sigma}{4G}.}
```

SIでは `-sigma c_light^4/(4G)`。細くしても、要求される積分負値は小さくならない。

### 4.1 状態非依存の必要条件

境界のない自由な四次元共形場だけを支持源とする。Λ=0、正のrenormalized G、任意だが有限の曲率二乗countertermを許す。
[D]のWeyl anomalyを使うと

```math
\langle T^a{}_a\rangle=\frac{c_W C_{abcd}^2-a_E E_4+\beta\Box R}{16\pi^2},
\quad c_W=N_s/120+N_D/20+N_V/10>0.
```

このproduct metricでは `Riem²=R²`, `Ric²=R²/2`, `C²=R²/3`, `E_4=0`。
したがって

```math
-\frac{R}{8\pi G}=\frac{c_W R^2}{48\pi^2}+\frac{\beta\Box R}{16\pi^2}.
```

`integral Box R dA=2pi[F R']_0^infty=0`。K=-R>=0とすると

```math
\frac{\int K^2dA}{\int KdA}=\frac{6\pi}{c_W\ell_P^2},\qquad
\boxed{\sup K\,\ell_P^2\ge\frac{6\pi}{c_W}.}
```

一Maxwellなら右辺60piで、低曲率の真空自己支持にならない。
**大Nでは下限も下がるため、全大N半古典解を排除しない。**
minimal scalar・質量・相互作用のbeta関数項・壁のtraceは対象外。
有限tubeや有限ringでは積分境界項と幾何を再検査する必要があり、上の積分を無条件に流用しない。

### 4.2 指定したprofileは全厚さで不一致

```math
F(r)=r+\sigma[r-\epsilon\arctan(r/\epsilon)].
```

正則なaxisと目的の角超過を持つが、遠方で
`R~-4sigma epsilon²/[(1+sigma)r⁴]`, `R²=O(r^-8)`, `Box R=O(r^-6)`。
左辺のr^-4を右辺で再現できないため、**このprofileの境界なし共形場だけによる完成は全epsilonで不成立**。
有限betaを変えても救えない。

sigma=1で積分traceだけ合わせる診断では
`Q=int Fhat''²/Fhat du=0.60826307515279...`, `epsilon²/ell_P²=c_W Q/(3pi)`。
一Maxwellなら `epsilon/ell_P=0.08033599239...`。これは解ではなく必要条件の診断値。
trace一致は必要条件にすぎず、それだけで全応力・正の量子状態を認定しない。

## 5. 肯定的な四次元論文も同時に評価

[KQ]は量子化Dirac場・半古典重力・Maxwell場を用いて静的なEDM wormholeを構成している。
ただし応力はnormal orderingを採用する(48)。一般の局所共変なvacuum polarizationを含む全応力も計算済み、と読み替えない。
[KD]の調べた初期値の時間発展はブラックホール形成と信号の捕捉を報告する。
静的な解の存在と、作成・安定化・外部への通信は別の検査である。
これらの数値解は今回再実行しておらず、全高励起・全能動制御の禁止も主張しない。

**再開点：同じ幾何に対し、有限局所pump・全renormalized stress・揺らぎ・非線形発展を一緒に計算すること。**
今回の一点一致、有限セル、直線coreのいずれかだけを成功した通信装置と呼ばない。

## 6. 再現・検査・統合

```bash
python src/symbolic/scalar_4d_squeezed_support.py
python src/symbolic/scalar_4d_semiclassical_initial_data.py
python src/symbolic/casimir_4d_finite_apparatus.py
python src/symbolic/ring_4d_conformal_core.py
```

独立四本。既存研究コード・assert・精度・共有依存・参照data・workflow・Leanは変更しない。
ローカルPython 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0で全assert成功・compile成功。
厳密代数と独立した50/80桁の運動量・空間・null・Green・曲率積分を照合した。
全丸め誤差のinterval保証ではない。SI定数の物理精度が80桁になるわけでもない。

ローカルcloneはDNS失敗のため全repoの再実行は未実施。固定SHAからconnectorで提出する。
ユーザーの明示的な許可に従い、PR差分と最新CIを確認してから統合する。実際のhead、merge SHA、run、対象と結果はPRの完了記録へ残す。
CI成功は実装した検算の成功であり、過去通信成功・独立査読・形式証明ではない。

## 一次資料と利用箇所

- **[C]** B. Arderucio Costa, G. E. A. Matsas, *Can quantum mechanics breed negative masses?*, Phys. Rev. D **105**, 085016 (2022), [arXiv:2112.08881v3](https://arxiv.org/abs/2112.08881v3)。§II–III、(12)–(22)の真空応力・力学的釣合い・DEC・有限板近似。PDF本文とprinted p.4画像を確認。orientationの反例と応用境界は今回の追加。
- **[D]** M. J. Duff, *Twenty Years of the Weyl Anomaly*, Class. Quantum Grav. **11**, 1387–1404 (1994), [hep-th/9308075](https://arxiv.org/abs/hep-th/9308075)。(21)–(31)の四次元不変量と係数。PDF本文で確認、該当ページ画像は取得エラー。coreの積分条件とprofileの否定は今回の導出。
- **[ADM]** E. Gourgoulhon, *3+1 Formalism and Bases of Numerical Relativity* (2007), [gr-qc/0703035](https://arxiv.org/abs/gr-qc/0703035)。3+1 Einstein方程式と初期値問題。packetのmultipole解・包絡上界・初期加速度の成分検算は今回の計算。
- **[FR]** C. J. Fewster, T. A. Roman, *Null energy conditions in quantum field theory*, Phys. Rev. D **67**, 044003 (2003), [gr-qc/0209036](https://arxiv.org/abs/gr-qc/0209036)。有限null平均と完全ANECの区別。今回のpacketの式を論文の既出公式とはしていない。
- **[FKZ]** V. P. Frolov, P. Krtouš, A. Zelnikov, *Ring wormholes and time machines*, Phys. Rev. D **108**, 024034 (2023), [arXiv:2305.03887](https://arxiv.org/abs/2305.03887)。前回検証した負の角欠損・線源を動機に使用。今回の直線coreは有限ringの全解ではない。
- **[KQ]** B. Kain, *Einstein-Dirac-Maxwell wormholes in quantum field theory*, Phys. Rev. D **108**, 084010 (2023), [arXiv:2308.00049v2](https://arxiv.org/abs/2308.00049v2)。静的構成、PDF (48)のnormal orderingを確認。該当画像取得は失敗。数値解の再実行はしない。
- **[KD]** B. Kain, *Are Einstein-Dirac-Maxwell wormholes traversable?*, Phys. Rev. D **108**, 044019 (2023), [arXiv:2305.11217v2](https://arxiv.org/abs/2305.11217v2)。公式abstractの時間発展の結果を確認。全初期値・全能動制御への禁止と読み替えない。

検索と検算の範囲は今回の支持源に限定した。現代物理全方式の網羅や、自然界一般のYES/NOの証明ではない。
