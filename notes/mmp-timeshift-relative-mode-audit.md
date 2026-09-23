# MMP + 時間差 + 相対モード：喉の通過条件とRoman ringの初回監査

**2026-09-23 / 別系統の研究。基点：main `028fb7d58a7c098affbfa904cf9f82ad71416586`。**

ユーザーが選んだ「MMP型の量子支持ワームホール、物理的な時間差、低エネルギー相対モード、必要ならRoman ring」を具体化する。
[NUTの模型内no-go](nut-null-return-obstruction.md)は変更・転用しない。

> **今回の判定：標準Casimir真空を用いる、以下で明示する先頭次数MMP/JT構成は、過去通信として不成立。**
> 情報担体としての相対モードは残る。しかし、時間差を入れた真空のエネルギー流も重力方程式へ入れると、同じnull信号の入口・出口を両方開くために `Delta < tau_w-d` が必要になる。
> 外部へ出て元の実験室へ戻る過去通信には `Delta > tau_w+d+tau_read` が必要で、両立しない。
>
> **完全な4D時間依存MMP、全量子状態、任意の多口幾何、自然界一般の禁止ではない。** 受動的な真空の単純な組合せを検査した結果であり、動的形成・口の運動・高次補正・別の負のnullエネルギー源は解いていない。

## 0. 何を借り、何を追加したか

| 層 | 既存文献と今回の作業 | 判定 |
|---|---|---|
| 支持構造 | [M]のmassless Landau-level Casimir、共形異常、近AdS2の球対称JT極限 | 無時間差の式を再現 |
| 時間差 | 一周の同一視 `(t,z)~(t+Delta,z+C)` とNS真空を**今回の定常オフセット拡張として採用** | 時間差ゼロの応力を流用しない |
| 喉の反作用 | 時間差付き真空の対角応力と流束を先頭JT方程式へ入れる | 同じ信号の入口・出口条件で障害 |
| 情報担体 | [F]の多flavor Schwinger模型にある相対モード | 二次有効理論で等エネルギー符号化を確認 |
| 多口化 | 独立MMPペアの接続／一つの透明な支持ループの共有を別々に検査 | その二構成は救済しない |
| 全物理 | 動的な4D解、準備装置、全ネットワークの真空・応力・受信確率 | 今回は未構成。上の限定結果と区別 |

既知のAANECに基づく先行議論[T]と結論の方向は整合するが、今回の通過条件は、下記の**具体的な真空応力とJT拘束式**から導く。AANECを追加公理としてコードに置いていない。新しい基本定理・優先権・独立査読済みとは主張しない。

## 1. 模型を固定する

以下は `c_light=hbar=1`。時間は、口が最終的に同じ時計速度を持つ外部静止系で規格化する。
左の外部時計を `T_L=ell*tau`、右を `T_R=ell*tau-Delta` と対応させるので、左から右の一回の自由null通過は外部では `tau_w-Delta` かかる。
今回のpayloadはこのmassless相対モードの直接通過である。喉の中で記憶装置が待機する別プロトコルや、任意のtimelike装置履歴の不存在をこの境界計算だけで主張しない。

- 喉の光学的通過時間 `tau_w=pi ell`。これは喉の固有長ではない。[M, (5.20)]
- 自分自身の二つの口の間の最短の外部光行時間を `d>0` とする。
- 磁力線nuの外部光学長は `d_nu>=d`、一周長は `C_nu=tau_w+d_nu`。
- `Delta>=0` は短くなる向きの物理的な時間ホロノミー。単なる時計の表示替えではない。
- 透明な独立massless NS（反周期）チャネル、同じDelta、正の重みでの球平均を採用する。
- 平均を `<...>_nu`、全中心電荷を `c_eff>0` とする。[M]の主要項では `c_eff=q`。gapped singletや他のKKモード等の修正を全て計算したという意味ではない。
- `Delta<min C_nu` のspacelikeな同一視の側に限って、以下の真空を定義する。null/timelikeな一周へ公式を解析接続して真空と呼ばない。

球平均、近極限・長い喉、弱い先頭反作用という[M]の近似を保つ。任意に加速中の口、異なるclock rate、時間依存Delta、非断熱に生成された状態には、そのまま適用しない。
時間差を物理的に作る工程を解いたのではなく、**その後にこの真空に落ち着くという受動的な候補**を先にテストする。

相対モードの通信性能と、支持する場の真空は別の計算である。透過率1を幾何の存在証明にしない。

## 2. 時間差を入れたCasimir応力

コード：[mmp_timeshift_throat_gate.py](../src/symbolic/mmp_timeshift_throat_gate.py)。

光学座標のnull変数 `u=t-z, v=t+z` に対し、一周の変化は

```math
u\mapsto u-(C_\nu-\Delta),\qquad
v\mapsto v+(C_\nu+\Delta).
```

NSの右・左向き周波数の間隔はそれぞれ `2pi/(C_nu-Delta)` と `2pi/(C_nu+Delta)`。
通常の2D真空のchiral Casimir係数[M, (5.24)]を用いると

```math
T^{\rm flat}_{uu}=-\frac{\pi c_{\rm eff}}{12}
 \left\langle(C_\nu-\Delta)^{-2}\right\rangle_\nu,
\quad
T^{\rm flat}_{vv}=-\frac{\pi c_{\rm eff}}{12}
 \left\langle(C_\nu+\Delta)^{-2}\right\rangle_\nu.
```

一つの線では、固有周長 `sqrt(C²-Delta²)` の普通の円筒真空をboostする別計算とも一致する。
正の場状態を定義できるspacelike円筒での計算であり、時刻の対応だけを付け替えた確率ではない。

喉では `tau=t/ell`, `sigma=z/ell` を使い、

```math
ds_2^2=r_e^2\sec^2\sigma(-d\tau^2+d\sigma^2),
\qquad -\pi/2<\sigma<\pi/2.
```

[M, Appendix F, (F.29)]の共形異常を加える。traceに比例する項は、同論文の先頭近似と同様に背景半径の補正側へ分ける。
残るtracelessな2D sourceを

```math
\widehat T_{ab}=\begin{pmatrix}e&j\\j&e\end{pmatrix},
```
```math
e=\frac{c_{\rm eff}}{24\pi}
-\frac{\pi c_{\rm eff}\ell^2}{12}
\left\langle(C_\nu-\Delta)^{-2}+(C_\nu+\Delta)^{-2}\right\rangle_\nu,
```
```math
j=\frac{\pi c_{\rm eff}\ell^2}{12}
\left\langle(C_\nu-\Delta)^{-2}-(C_\nu+\Delta)^{-2}\right\rangle_\nu
```

と書ける。`Delta>0` なら `j>0`。真空は時間に依存しなくても、エネルギー流は零でない。
`Delta=0,d_nu=0` では `e=-c_eff/(8pi), j=0` となり[M, (5.27)]に一致する。
[M, (5.30)–(5.31)]の `E=A/ell²-q/(8ell)`、`ell_*=16A/q`、`E_*=-q²/(256A)`（`A=r_e³/G`）も別に再現した。

**重要：時間差付きのエネルギーをellで極小化するだけでは、流束の重力拘束を満たしたことにならない。** 以下は対角・非対角の全先頭方程式を検算する。

## 3. 入口・出口を同じ信号で比較する

### 3.1 先頭JT方程式と、流束に応じる解

球面面積の小さい相対補正をvarphiとする。単位AdS2計量 `g_hat=sec²sigma diag(-1,1)` の上で、[M, §5.3.2]の先頭方程式は

```math
(\widehat g_{ab}\widehat\Box-\widehat\nabla_a\widehat\nabla_b
-\widehat g_{ab})\varphi=\kappa\widehat T_{ab},
\qquad \kappa=2G/r_e^2>0.
```

`a=-e` と書くと、一つの特解と全三つの斉次モードは

```math
\varphi=\kappa[a(1+\sigma\tan\sigma)-j\tau\tan\sigma]
+\frac{h_c\cos\tau+h_s\sin\tau}{\cos\sigma}+h_0\tan\sigma.
```

コードは計量からChristoffel記号を作り、全三成分の方程式へ直接代入する。
流束項 `-kappa*j*tau*tan(sigma)` を落とすと非対角方程式に `-kappa*j` の残差が残る負例も検査する。
定数a,jの source に対する先頭JT解であり、動的4D形成解ではない。

### 3.2 同時刻の「二つの口が開いている」では不十分

喉から外側のnear-extremal領域へ半径が増大するため、両端のleading coefficient

```math
B_L(\tau)=\lim_{\sigma\to-\pi/2}\cos\sigma\,\varphi,
\quad B_R(\tau)=\lim_{\sigma\to+\pi/2}\cos\sigma\,\varphi
```

は、**信号が各端にいる時刻に**正である必要がある。これは[M]型の両側外部へのmatchingの必要条件。
有限cutoffの全matching条件や4Dの全解の十分条件と同一視しない。

短縮方向のnull信号は `tau_R=tau_L+pi`。よって

```math
\boxed{B_L(\tau_0)+B_R(\tau_0+\pi)=\kappa\pi(a-j).}
```

`h_c,h_s,h_0`、開始時刻tau_0は全て消える。**対称な初期条件だけを選んだ否定ではない。**
同時刻の和は別の式であり、それを代わりに使うと障害を見落とす。

この必要条件は、特解の形を知らなくてもnull拘束から導ける。ray上のvarphiをf(sigma)、`D=partial_tau+partial_sigma` とすると

```math
\frac{d}{d\sigma}\left(\cos^2\sigma\,\frac{df}{d\sigma}\right)
=-\kappa\cos^2\sigma\,\widehat T_{DD},
```
```math
B_R(\tau_0+\pi)+B_L(\tau_0)
=-\kappa\int_{-\pi/2}^{\pi/2}\cos^2\sigma\,\widehat T_{DD}\,d\sigma.
```

`T_DD=2(e+j)` を入れると同じ式。任意の追加斉次解でこの和を調整することはできない。
逆向きの通過なら `kappa*pi*(a+j)` であり、方向を取り違えない。

### 3.3 MMPの支持と過去通信の時間条件は両立しない

両端を開くには `a-j>0` が必要。応力の式を使って

```math
\mathcal G_+\equiv
4\tau_w^2\left\langle(C_\nu+\Delta)^{-2}\right\rangle_\nu-1>0,
\quad B_L+B_R=\frac{\kappa c_{\rm eff}}{24}\mathcal G_+.
```

全ての `d_nu>=d` から

```math
\mathcal G_+\le\frac{4\tau_w^2}{(\tau_w+d+\Delta)^2}-1
=\frac{(\tau_w-d-\Delta)(3\tau_w+d+\Delta)}
{(\tau_w+d+\Delta)^2}.
```

従って

```math
\boxed{\Delta<\tau_w-d.}
```

同じ実験室へ外部経路で戻り、読み出しを完了する時間は

```math
t_{\rm receive}-t_{\rm send}
=\tau_w+d+\tau_{\rm read}-\Delta
>2d+\tau_{\rm read}\ge0.
```

**この先頭・NS真空・受動構成で、選んだ情報を過去へ届けることはできない。**
時計差を増やしても、同じ支持構造を保ったまま短い近道へ進むことができない。
これは`Delta<C`の定義を、そのまま過去通信不能と言い換えた結果ではない。障害は遅くとも `Delta=tau_w-d`、null一周は `Delta=tau_w+d` で、その間には `2d` の差がある。
AANECを仮定する[T]の先行議論と整合するが、ここでは具体的sourceの計算で条件を得た。

### 3.4 診断例と近似の限界

`tau_w=1,d=1/4`、全磁力線を最短長とした**支持に最も有利な上界**：

| Delta | G_+の上界 | 通常の一周遅延 C-Delta |
|---:|---:|---:|
| 0 | 1.56 | 1.25 |
| 0.5 | 0.30612244897959... | 0.75 |
| 0.75 | 0 | 0.5 |
| 1 | -0.20987654320988... | 0.25 |

無次元比の例で、実装した装置の秒数・通信確率ではない。真の磁力線長分布は支持をさらに弱め得る。
3本の長さ`(1/4,1/2,1)`、重み`(1/2,1/3,1/6)`という比較分布では零点は`Delta=0.5854292309290234...`。この離散分布を実際のMMP磁束分布と称していない。

障害を発散だけに依存させていない。`epsilon_br=kappa*c_eff/(24pi)=10^-6` とするsource診断では、Delta=0.75のとき `kappa*(e,j)=(-7.5e-6,+7.5e-6)` と有限で小さい。
ただし、これだけで4Dの全近似条件や口の運動を認定しない。高次・非球対称・finite-cutoff補正の誤差を計算していないので、先頭次数の不等式を厳密な4D全次数定理へ格上げしない。

## 4. 選んだ情報担体は、どこまで成立したか

コード：[mmp_relative_mode_ring.py](../src/symbolic/mmp_relative_mode_ring.py)。
[F, §4.3.1, (134)–(139)]の多flavorボソン化では、mass matrixはsinglet方向 `s=(1,...,1)/sqrt(N)` にのみ作用する。

```math
M^2=m_\Sigma^2 ss^T,\qquad P_\perp=I-ss^T,\qquad M^2P_\perp=0.
```

`v=(1,-1,0,...)/sqrt(2)` へ

```math
\langle\boldsymbol\varphi\rangle_b=(-1)^b\,a_{\rm sig}v\,f(\tau-\sigma)
```

と符号化すれば、二次有効理論では総vector currentが零、波動方程式が自由、両符号の古典応力が等しい。
N=2,3,5,8で直交flavor変換・mass matrix・kinetic normを厳密検算した。
これはfermionの密度・相対currentという集団励起であり、fermionic coherent stateにbosonic公式を誤用していない。
大域的flavor選別・境界instrument・他の相互作用は未構成。[F]自体のbosonization／追加相互作用への留保も維持する。

この担体を通常の未来向きの単一波束として使い、**比較入力**として純損失率etaを与えた場合は

```math
D_{\rm ideal}=\sqrt{1-e^{-4\eta n}},\qquad
n\ge\frac{\log[1/(4\epsilon(1-\epsilon))]}{4\eta}
```

を二状態の内積から導ける。例えば理想eta=1、誤り率1%にはn=0.80723154018...。
これは平均励起数であり、MMP時間機械の成功率ではない。2次元の「二状態が張る空間」による独立なtrace-distance検査を行い、bosonic Fock空間を切っていない。

**等エネルギーの符号化でも、背景の負の支持源を供給しない。** classical coherent相対モードは `delta T_DD=(D chi)^2>=0`。
同じnull方向へ進むパルスではこの射影は0であって、必ず正ではない。しかし必要な負のnull積分を増やすことはない。
他の方向・他の重力拘束への影響は別にあり、全backreactionが消えたわけでもない。

有限の読出し時間を必ず含める。厳密な帯域制限と有限時間からのオンセットを両方仮定せず、低周波透過の結果を制御前のパルス裾へ外挿しない。

## 5. Roman ringを足す二つの実装検査

### 5.1 独立のMMP支持を保ったペアを並べる

各ペアiが§3の条件を満たすなら、その口間の実際の通過時間 `w_i=tau_i-Delta_i>d_i>0`。
出口から次の入口への外部接続時間を `s_i>=0` として

```math
\sum_i(w_i+s_i)>0.
```

従ってどの有限ringでも過去には戻れない。時刻の再表示 `t_i'=t_i+a_i` で各辺は変わっても、周回総和は不変。
コードで120構成の厳密な有理数対照と、時計再表示の負例を検査する。一般の結論は上の和による。

**「各ペア単独がCTCでない」だけでは、この結論は出ない。** 位置`A1=0,B1=100,A2=101,B2=1`、各wormhole通過時間−2という純粋な幾何対照なら、単独の戻りは98でもringは−2となる。
その対照は§3のMMP支持条件を満たしていない。Romanの幾何学的着想そのものを間違いとしない。

### 5.2 同じCasimirループを全ての喉で共有する

さらに別の**明示的な単純sewing模型**として、全支持チャネルが一つの透明NSループに沿って、m個の別々のAdS2喉を通るとする。
`C=sum_i tau_i+sum_i s_i`、全時間差`Delta_loop>=0`、各喉の時刻規格化は共通。

同じ計算により各喉には

```math
\mathcal G_i=\frac{4\tau_i^2}{(C+\Delta_{\rm loop})^2}-1>0
```

が必要。しかし最短の喉について

```math
\tau_{\min}\le C/m,
\qquad \mathcal G_{\min}\le 4/m^2-1\le0\quad(m\ge2).
```

よってこの支持の共有方法は、時間機械になる以前に少なくとも一つの喉を支えられない。c_effを全体的に増やしても比の障害は変わらない。
234組の不均等な長さの対照も厳密に検査した。

**全ての多口模型を禁止する定理ではない。** 分岐型、複数の独立サイクル、混合・散乱するチャネル、別の支持源には同じ一ループ式を当てない。
[MM]には別の方法による多口構成が実在する。今回その4D解や時間差付き拡張を再現・否定したのではない。

### 5.3 van Vleck抑制を支持源へ掛けない

[V, (6)]の対称なthin-throat近似では

```math
\Delta_{\rm vV}=\left[\frac{m}{U_{m-1}(1+s/R)}\right]^2>0
```

で、`s/R=10`、m=8では約`1.0545e-17`まで小さくなる。
有限mで0ではない。[V, (8)–(9)]の幾何光学的stress proxyは、null一周へ近づくパラメータepsに対してeps^-3の先頭挙動を持つことも検査した。
この極限の近くで半古典近似の信頼性が失われ得るため、proxyを全応力の厳密な発散証明にはしない。

**この4Dのdefocusing係数を、磁力線へ拘束された2DフェルミオンのCasimir支持や透過率へ掛けることは正当化されない。** 二つの文献の有利な係数だけを組み合わせた「成功式」は作らない。

## 6. 今回の結論、次に変えなければならない入力

**採否：標準NS真空を使う先頭MMP/JTの受動的な時間差付きペア、および§5の二つの単純ring構成は、過去通信としてFAIL。**
相対モードの等エネルギー符号化は、未来向き通信の有力な部分として保存する。
これを選んだ当初の「もっとも可能性が高い」は定量的順位付けではなく研究優先順位だった。成功を保証する文献の組合せではない。

再検討には、例えば非定常／別状態の負のnullエネルギーを実際に計算する、複数サイクルの支持を持つ全ネットワークを解く、先頭近似が外れたときの有効方程式を制御する、のような物理入力の変更が必要。
単にetaを1へ近づける、符号化を変える、口の数を増やす、共形異常を落とすだけでは今回の障害は解消しない。

必要な救済量も式にできる。`G_+<0`なら、追加sourceは同じ信号経路上で

```math
I_{\rm extra}=\int_{-\pi/2}^{\pi/2}\cos^2\sigma\,
\delta\widehat T_{DD}\,d\sigma
<\frac{c_{\rm eff}}{24}\mathcal G_+<0
```

を満たす必要がある。最短ループ診断`tau_w=1,d=1/4,Delta=1`では `I_extra<-17 c_eff/1944`。
これは必要量であり、それを供給する物理状態・装置の存在証明ではない。
同じnull方向の古典的なcoherent情報パルスはこの救済をしない。

**未実施：** 4D動的な口の生成・加速・matching、全磁束分布の再計算、KK／高次／量子重力補正の誤差保証、別の非定常状態の構成、全送受信装置の大域的同時確率、独立査読・Lean形式証明。
今回の式を、これらを全て含む普遍的なchronology protectionにしない。

## 7. 再現と検証

```bash
python src/symbolic/mmp_timeshift_throat_gate.py
python src/symbolic/mmp_relative_mode_ring.py
```

ローカルPython 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0で両方成功、compile成功。
boostとchiral計算、共形異常、全JT成分、斉次モード、null積分、flavor射影は厳密代数。
別の直接null積分・数値微分、二状態のtrace distance、Chebyshevの双曲関数表示を50/80桁で照合し40桁以上一致。
一般の経路長分布の不等式・任意個数ringの和はノートの解析的証明で、有限個の数値例から推定していない。
高精度照合は全丸め誤差のinterval証明ではない。Leanは追加していない。

新規2本は独立、共有module・入力data・依存・CI設定・既存assertを変更しない。通常PRの累積差分選別でPython 3.12の対象検査を用いる。
ローカルのgit接続は今回もDNS失敗だったので、固定SHAをGitHub connectorで読み書きする。全repoをローカルで再実行したとは報告しない。
remoteの対象・checkout SHA・run・結果はPRコメントへ記録する。CIのsuccessを物理的過去通信のsuccessとしない。

## 一次資料と照合範囲

- **[M]** J. Maldacena, A. Milekhin, F. Popov, *Traversable wormholes in four dimensions*, [1807.04726v3](https://arxiv.org/abs/1807.04726v3)。§5.2–5.5、(5.20),(5.24)–(5.27),(5.30)–(5.37),(5.44)–(5.49)、Appendix F(F.29)をPDF抽出本文で確認。論文はDelta=0の自己支持解で、今回の時間差付き解そのものではない。
- **[F]** B. Freivogel, A. Fumagalli, M. Tomašević, *How traversable is a traversable wormhole?*, [2606.12528v1](https://arxiv.org/html/2606.12528v1)。取得できた公式版は2026-06-10のv1。§4.3–4.3.1、(123)–(139)のflavor相対モードと、その後の追加相互作用／bosonizationへの留保を確認。時間機械の構成論文ではない。
- **[T]** M. Tomašević, *On the Inaccessibility of Time Machines*, Universe 9, 159 (2023), [論文](https://www.mdpi.com/2218-1997/9/4/159)。検索で取得した出版社本文の§4、特にAANECのheuristic argumentと(38)–(44)を確認。出版社の直接open/PDF取得は失敗したため、全ページ画像を読んだとはしない。今回の式をこの論文からの既出式と断定しない。
- **[V]** M. Visser, *Traversable wormholes: the Roman ring*, [gr-qc/9702043](https://arxiv.org/abs/gr-qc/9702043)。PDF printed p.3の(2)–(10)を抽出本文とページ画像で確認。thin-throat・4D conformal scalarの推定と信頼性限界を、MMP支持フェルミオンの計算へ混同しない。
- **[MM]** R. Emparan, B. Grado-White, D. Marolf, M. Tomašević, *Multi-mouth Traversable Wormholes*, [2012.07821v2](https://arxiv.org/abs/2012.07821v2), JHEP 05 (2021) 032。公式abstractの分岐的な構成と位相の違いまで確認。全解・時間差導入の再現は行わない。単純serial-ringの否定を全multi-mouthの否定にしないための対照。

MMPのweb screenshotは取得エラーで、同論文のページ画像を確認済みとはしない。図から数値を読み取ってはいない。
検索はこの組合せに絞ったもので、現代物理全体や2026年文献の網羅、他の実現方法の不存在を意味しない。
