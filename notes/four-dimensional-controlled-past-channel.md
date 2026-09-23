# 3+1次元で、制御可能な過去向き情報通信路を作れるか

**2026-09-24。基点 main `20607d7643c46dcc6b07b16b3d79a3d7606842c4`。**
これは四次元の計量・応力・場・信号を明示する新しい監査である。
[先頭MMP/JTのQEI結果](mmp-negative-null-energy-audit.md)や[NUTの結果](nut-null-return-obstruction.md)を、別の四次元模型へ無条件に移植しない。

> **到達点：四次元で、条件付きの古典的過去経路、必要な重力源、正常な量子場の負エネルギー状態、通常方向の信号・受信統計を具体化した。**
> **人間が準備・維持・制御できる過去通信装置を構成した、という結果ではない。** 最重要の未供給資源は、自己無撞着で安定な負の重力源と、その状態を保った大域的な時刻接続である。
> 一方、四次元の全方式を禁止する定理も主張しない。薄層・境界・別の量子場は、単一スケールの滑らかな喉とは区別する。

## 0. 四次元のどの部分を計算したか

| 計算 | 対象 | 結果・限界 |
|---|---|---|
| 重力source | `R_t × R_x × S²` のEllis喉 | 全Einsteinテンソル・保存・必要な負のnull応力を厳密計算。ghostによる完成は正常物質ではない |
| 異なる薄層候補 | 四次元Visser型球面接合と滑らかなcollar | 表面応力と別の薄層スケールを計算。滑らかな単一スケールの制約を流用しない |
| 量子状態 | 四次元Minkowskiの通常の実massless scalar | `d³k`で規格化した有限エネルギー状態。負の局所密度は得るが、圧力と持続条件が支持要求に合わない |
| 情報の輸送 | 球面薄殻の四次元スカラー場 | 全角運動量の式、`l=0..4`の流束、有限時間source、未来側の無条件受信統計を検算 |
| 物理的な時計制御の文献例 | Frolov–Krtouš–Zelnikov [FKZ] の四次元ring wormhole | 正の質量shellが時刻接続を変える式を再現。ringを支える負のstringと量子反作用は仮定のまま |

**これらを違う幾何のまま足し合わせて「一台の完成装置」とはしない。** とくに球面喉の透過率をringの時間差へ掛けることはしていない。
角変数を分離して径方向ODEを解くのは四次元場の部分波解析であり、二次元CFTへ支持理論を置き換えることではない。

## 1. 成功の意味：送り手の操作で、同じ実験室の過去の記録を変える

送信者がbit `b=0,1`を選び、共通の準備資源の下で局在したsource

```math
S_J=\int d^4x\sqrt{-g}\,J_b(x)\phi(x),\qquad J_b=(-1)^bJ
```

を切り替える。受信結果yの全分布を保持し、失敗を捨てない。
最終的に必要なのは、同一の外部実験室のproper-time順序で `tau_R<tau_S` かつ

```math
D_R=\frac12\int dy\,|p(y_R|\mathrm{do}(0))-p(y_R|\mathrm{do}(1))|>0.
```

受信記録まで同じ過去として固定して「禁止」を定義に埋め込まない。一方、操作ごとに未来境界条件やincoming stateを勝手に選び直さない。
[MTY]型の物理的な時刻接続Deltaが**実装されている場合**の時間的必要条件は

```math
\Delta>\tau_{\rm throat}+d_{\rm ext}/c+\tau_{\rm read}.
```

これは完成した背景方程式の解ではなく、通信の合否基準である。帯域制限した波のpeakやWigner delayを、選択後に立ち上がる信号frontと同一視しない。

## 2. 四次元の支持問題：正常なsourceを要求する

コード：[wormhole_4d_geometry_support.py](../src/symbolic/wormhole_4d_geometry_support.py)。
まず [FR, (47),(48)] の滑らかな基準幾何を使う：

```math
ds^2=-c^2dt^2+dx^2+r(x)^2d\Omega_2^2,\qquad r(x)=\sqrt{x^2+b^2},\quad b>0.
```

これは二つの漸近平坦な端を結ぶが、そのままでは同じ外部実験室へ戻る時刻接続を持たない。
`t`がglobal timeである未加工の幾何にはCTCがない。片側の時計表示を変更してもこれを時間機械へ変えられない。

正規直交枠で、Einstein方程式が要求する全応力は

```math
T_{\hat a\hat b}=\operatorname{diag}(-A,-A,A,A),\qquad
A(x)=\frac{c^4b^2}{8\pi G(x^2+b^2)^2}.
```

コードは四次元metricからChristoffel、Ricci、Einsteinを直接計算し、全成分と共変保存を照合する。
径方向の `k^hat=(1,1,0,0)` で `T_kk=-2A<0`。
NECを満たす古典的な通常物質だけでは、このsourceを供給できない。密度だけを合わせ、横方向の圧力を落とすこともできない。

以下は `c=hbar=1`：

```math
\int_{-\infty}^{\infty}T_{kk}dx=-\frac1{8Gb},\qquad
E_{\rm proper}=\int4\pi r^2\rho\,dx=-\frac{\pi b}{2G}.
```

**後者は選んだ静止sliceでの物質のproper-volume積分で、ADM質量でも製造仕事でもない。** SIでは `-pi c^4 b/(2G)`。
`b=1m`なら `rho(0)≈-4.81545×10^42 J/m³`、`E_proper≈-1.90106×10^44 J`。
これは「これだけ費用を払えば製造できる」という数値ではない。

### 2.1 ghostを許すと解は書けるが、正常な支持資源にはならない

```math
S_{\rm ghost}=+\frac12\int\sqrt{-g}\,(\nabla\psi)^2d^4x,
\qquad \psi=\frac{\arctan(x/b)}{\sqrt{4\pi G}}
```

なら上の全Einstein方程式と場の方程式を満たす。通常の実scalarの作用の符号は逆である。
正の内積を選んだ通常のcanonical解釈では、このghostのHamiltonianは下に有界でない。
**ghostという名前の追加物質を、人が準備できる負エネルギーと認定しない。**

さらに [GGS1, (34),(35)] の四次元Einstein–ghost系の正則な球対称摂動方程式には

```math
H=-\partial_x^2-\frac{3b^2}{(x^2+b^2)^2}
```

が現れる。論文と同じtrial `u=(1+x²/b²)^(-1)` のRayleigh商を再計算すると

```math
\omega_0^2\le-\frac{11}{8b^2},\qquad
\tau_{\rm efold}\le\sqrt{\frac8{11}}\frac b c.
```

`b=1m`で上限は約`2.845ns`。これは**既出の不安定性の再現**で、新しい禁止定理ではない。
collapseまでの時間は初期摂動量にも依存し、単発の光信号まで必ず失敗するとは言えない。[GGS2] は崩壊前の信号も検討している。
能動的な安定化を今回否定したのでも、4Dで実装したのでもない。

## 3. 四次元の量子エネルギー不等式から出す、範囲付きの支持診断

[FE, (5.5)] の四次元Minkowskiにおける通常の実自由scalarでは、静止慣性観測者に沿う平均に

```math
\int g(t)^2\langle:T_{00}:\rangle dt\ge
-\frac1{16\pi^2}\int|g''(t)|^2dt
```

がある。これは**timelike sampling**であり、四次元のnull線の平均に同じ下限があるとは言わない。[NR] は後者の下限不存在を示す。

短時間区間内に収まる正規化samplerを

```math
g_T(t)=\frac2{\sqrt{3T}}\cos^2\frac{\pi t}{2T}\quad(|t|<T),
\qquad g_T=0\quad(|t|\ge T)
```

とする。`g_T`はH²で、smoothなsamplerのH²極限として使用する。規格化と二階微分の積分を厳密に計算すると

```math
\int g_T^2=1,\qquad \int(g_T'')^2=\frac{\pi^4}{3T^4},\qquad
\bar\rho\ge-\frac{\pi^2}{48T^4}.
```

### 3.1 平坦時空の定理と、曲がった喉への近似適用を区別する

喉の静止観測者はgeodesicで、曲率の代表長はb。`cT=f b`, `f<<1`として、
近傍により短い境界スケールがなく、短時間のflat-leading QEIが支配し、繰込みされた幾何項も摂動的であるという [FR, PF] 型の**局所平坦近似**を追加する。
N個の同種自由scalarなら、喉に必要な定常密度との比較で

```math
b\ \lesssim\ \frac{\sqrt{N\pi^3/6}}{f^2}\ell_P.
```

`N=1,f=.01`では約`3.674×10^-31m`。`b=1m`の密度は、同じsamplingのflat-leading許容負値より約`7.408×10^60`倍大きい。
**単一スケールの巨視的な滑らかな喉を、このsourceで支える案はこの近似診断で不適合。**

この数値は四次元曲率補正を全て保証した絶対定理ではない。境界付きCasimir、別のcoupling、量子場の種類、多数種の自己無撞着な重力cutoffを再計算してはいない。
Nを自由につまみとして大きくして、実現例が完成したことにもしていない。

### 3.2 薄層を使う別の四次元幾何は、同じ上限では排除しない

[Visser]型の理想的な薄殻 `r=b+|x|` では、Israel接合から

```math
\sigma_{\rm shell}=-\frac{c^4}{2\pi Gb},\qquad
p_{\rm shell}=\frac{c^4}{4\pi Gb}
```

が必要。delta分布の殻へ上の滑らかなQEIを直接使ってはいけない。
滑らかな比較collarとして `r=b+sqrt(x²+epsilon²)-epsilon` を置くと、`c=1`で

```math
\rho(0)=\frac{1-2b/\epsilon}{8\pi Gb^2},\quad
p_x(0)=-\frac1{8\pi Gb^2},\quad
p_\perp(0)=\frac1{8\pi Gb\epsilon}.
```

`epsilon<<b`で短時間scaleを `T=f epsilon` とする同種の局所平坦診断は

```math
\epsilon^3\lesssim\frac{N\pi^3}{12f^4}\ell_P^2b.
```

`b=1m,N=1,f=.01`では`epsilon≲4.072×10^-21m`。
**これは薄層の必要条件であり、実現する量子状態・材料を与えない。しかし、b自体をPlanck近傍に限る単一スケールの結論を、この別幾何へ押し付けてもいけない。**
境界や装置の応力、全coupled semiclassical equationは未解決の入力である。[DS] の二方向smearingも、curved throatに無条件では移植しない。

## 4. 真の3+1次元量子場で、負のsource候補を作る

コード：[scalar_4d_negative_packet.py](../src/symbolic/scalar_4d_negative_packet.py)。
ここは四次元Minkowskiの局所的なsource診断であり、先の曲がった喉の状態ではない。
`[a_k,a_p^dagger]=delta³(k-p)`、`c=hbar=1`とし、全三次元運動量に

```math
f(\mathbf k)=\frac{a}{\sqrt{\pi |\mathbf k|}}e^{-a|\mathbf k|},
\qquad\int d^3k|f|^2=1,\qquad
u(t,r)=\frac{a}{\pi[(a+it)^2+r^2]}
```

という正周波数packetを使う。`Box_4 u=0`で、典型的な長さaは喉半径bとは別。

```math
|\Psi_\zeta\rangle=\frac{|0\rangle+\zeta|2_f\rangle}{\sqrt{1+\zeta^2}},
\quad n=\langle a_f^\dagger a_f\rangle=\frac{2\zeta^2}{1+\zeta^2},
\quad m=\langle a_fa_f\rangle=\frac{\sqrt2\zeta}{1+\zeta^2}.
```

二点関数の真空との差はuから作るsmoothなbisolutionなので、通常の短距離特異性を保つ。
これは有限モードcutoffを場全体と取り違えた状態ではなく、四次元の連続運動量に広がる一つのpacketの有限粒子状態。
ただしpacketには空間tailがあり、その厳密な形のlocal preparation装置までは構成していない。

正規順序化した全応力は

```math
\langle:T_{\mu\nu}:\rangle=
2n\operatorname{Re}\!\left(\partial_\mu\bar u\,\partial_\nu u
-\frac12\eta_{\mu\nu}\partial\bar u\cdot\partial u\right)
+2m\operatorname{Re}\!\left(\partial_\mu u\,\partial_\nu u
-\frac12\eta_{\mu\nu}(\partial u)^2\right).
```

 t=0では

```math
\rho(0,r)=\frac{4a^2[(n+m)r^2+(n-m)a^2]}{\pi^2(a^2+r^2)^4},
\qquad E=\int4\pi r^2\rho dr=\frac n a>0.
```

`zeta=sqrt(3)-sqrt(2)`で
`rho(0,0)=-0.09108566555/a^4`、`E=0.1835034191/a`。
中央は負でも周囲の正の寄与を含む全エネルギーは正。**負値だけを切り取って支持sourceへ代入しない。**

圧力も計算すると中央では `p_x=p_perp=rho<0`。Ellisの要求 `p_perp=-rho>0` と一致しない。
密度だけを1mのEllis喉に合わせるならSIで `a≈4.945×10^-18m`、時間scale `a/c≈1.650×10^-26s`となるが、これは全喉の支持ではない。
四次元の球対称保存則の二本を、一般bisolutionの恒等式から検算し、運動量積分と空間積分からも独立に規格化・エネルギーを確認する。

正規化Gaussianのtimelike samplingには厳密なflat bound `-3/(64pi²T⁴)`を使用。
一つのpacket族についてsamplingごとの最小平均も2×2の厳密な固有値式へ還元して比較した。
全状態に対する禁止をこの小さい族の探索だけから推論しない。

## 5. 四次元の喉を、情報自体は通せるか

コード：[wormhole_4d_signal_scattering.py](../src/symbolic/wormhole_4d_signal_scattering.py)。
ここではsourceが既に存在すると仮定したVisser型球面薄殻を使う。**ring型とは別幾何**である。
通常のminimal scalarを

```math
\phi(t,x,\Omega)=\sum_{lm}\frac{u_{lm}(t,x)}{r(x)}Y_{lm}(\Omega)
```

と展開すると、四次元波動方程式から厳密に

```math
[-\partial_t^2+\partial_x^2-V_l(x)]u_{lm}=0,\qquad
V_l=\frac{l(l+1)}{r^2}+\frac{r''}{r}
```

となる。薄殻では `r''/r=2delta(x)/b`。`u`の連続と`[u_x]=2u/b`を課す。
**角運動量の障壁と、殻自身の散乱を保持する。** metricの支持sourceとsignal fieldは別のもの。

`q=omega b/c`、外向きJost多項式を

```math
P_l(q)=\sum_{k=0}^l\frac{i^k(l+k)!}{k!(l-k)!(2q)^k}
```

と置くと、一つの喉の透過振幅は

```math
t_l(q)=\frac{iq}{P_l(q)[(iq-1)P_l(q)+qP_l'(q)]},
\quad r_l=t_l-\bar P_l/P_l.
```

正規化は両側の単位入射流束。全角lの式を与え、`l=0..4`で流束保存を厳密検算し、別の球Bessel解の二側接合でも照合する。
とくに

```math
\eta_0=|t_0|^2=\frac{q^2}{1+q^2},\qquad
\eta_1=\frac{q^6}{(q^2+1)(q^4+4)}.
```

`q=1`で`eta_0=.5`, `eta_1=.1`, `eta_2≈.0008643042351`。
**すべての角モードが完全透過するとは仮定していない。** 局在ビームの実験では対応する角分布を含む必要がある。
薄殻のスカラーpoint interactionは正のself-adjoint散乱模型だが、殻自身のrenormalized stressをその特異極限で解いたわけではない。

### 5.1 時間的に切り替えるsourceと、後選別しない受信

s-waveの振幅に対応する時間応答は

```math
h(t)=\delta(t)-\frac cb e^{-ct/b}\Theta(t).
```

有限時間のsource `f(t)=sin²(pi t/T)` (`0<t<T`, それ以外0) を送ると、
応答は `f(t)-(c/b)integral_0^t exp[-c(t-s)/b]f(s)ds`。
厳密に `t<0`では0。smoothingしても因果supportは保持される。sourceをbitで符号反転すると受信平均も反転する。
これは理想化したspherical modeの送信制御であり、発信前から存在するband-limited波束のpeakを過去信号とする手順ではない。

通常の未来方向にある透過coherent modeへ、平均数Nを用いて`±alpha`を符号化する。
雑音が真空、位相参照とmatched-mode readoutが利用可能なら、quadrature測定は

```math
p(y|b)=\frac1{\sqrt\pi}\exp[-(y-(-1)^b\sqrt{2N\eta})^2],
\quad P_{\rm err}^{\rm hom}=\tfrac12\operatorname{erfc}\sqrt{2N\eta}.
```

`N=2,eta=.5`の未来側ideal mode測定では誤り率`0.02275013195`。
これは全結果込みの分布。最適Helstrom測定の下限とは区別する。
一般のfinite-band packetでは`eta=integral |t_l(omega)|²|f_lm(omega)|² domega`等を使い、単色値を自動的に代入しない。
**この数値は過去側の受信確率ではなく、読み出し時間を有限と保証するものでもない。**

同じ外部空間に両口を置き、CTCを生じさせるgluingへ進むと、全周回経路・準備・量子状態が別途必要になる。
二つの独立外部を持つ散乱計算を、そのままpost-CTC時空のretarded実験へ読み替えない。

## 6. 時間差を実際の質量で制御する、実在する四次元候補

コード：[ring_4d_mass_clock_control.py](../src/symbolic/ring_4d_mass_clock_control.py)。
[FKZ]は、diskの縁に負の角欠損`-2pi`を持つring wormholeの**同じ外部空間に二口がある場合**を扱う。
球面薄殻やMMPとは別の幾何で、円盤内部を通る光は負のstring core自体を横断しない。

ring半径aのoblate座標では空間部分は

```math
dl^2=a^2[(\sinh^2\chi+\cos^2\theta)(d\chi^2+d\theta^2)
+\cosh^2\chi\sin^2\theta\,d\phi^2],
```

局所時空metricは`ds²=-exp(2U)c²dt²+exp(-2U)dl²`。
四次元の弱重力近似で、片口を囲むoblate shellの質量Mを変えると、非可縮な周回に沿う時刻接続が変わる。
`m=GM/(ac²)`、shellの短半軸`R=a sinh chi0`、口の距離Lとして、[FKZ, (5.35)] は

```math
I_C\simeq\frac{GM}{ac^2}\left[\arctan\frac aR-\frac aL\right]>0
\qquad(a\ll R\ll L).
```

空間metricのJacobian、source-free領域のoblate Laplace方程式、時刻の接合式を検算する。
[FKZ, (6.1)–(6.9)] の光の帰還時刻は

```math
t_3-t_0=B_{\rm opt}-(e^{I_C}-1)t_2,\qquad
B_{\rm opt}=\frac1c\int_{-L/2}^{L/2}e^{-2U(z)}dz>0,
```
```math
t_{2,\rm onset}=\frac{B_{\rm opt}}{e^{I_C}-1}\simeq\frac{RLc}{GM}.
```

固定点での発信・帰還なので、同じ実験室のproper timeでも符号が保たれる。
読み出しに有限時間が必要なら`B_opt`へその遅延を足す。
**既存のringと近似が維持されるという条件の下では、正の質量による制御から古典的な過去への経路が得られる。** 時計ラベルだけの変更ではない。

例`a=1m,R=10m,L=1000m`、`B_opt≈L/c`で：

| 正のshell質量M | 形式的な帰還条件の到達時間 |
|---:|---:|
| `10³ kg` | 約`4.55×10^19 s`（約`1.44×10^12年`） |
| `10¹² kg` | 約`4.55×10^10 s`（約1440年） |
| `10²⁰ kg` | 約455秒 |

これは**既存の特殊wormholeを前提にした弱場式のscale**であり、工学的な製造時間ではない。高桁の数値再現は近似誤差やGの測定精度を消さない。
二口の近似場全体・switch-onの力学・長時間の量子反作用を再導出したわけではない。

### 6.1 何を未供給のままにしているか

負のconical defectを通常のstring規約 `deficit=8pi G mu/c⁴` に対応させると、

```math
\mu=-\frac{c^4}{4G}\simeq-3.026\times10^{43}\ \mathrm{J/m}.
```

半径1mの理想ringの線エネルギー積分は約`-1.901×10^44 J`。
これは局所conical sourceの規約による量で、ADM質量や製造費ではない。
**正の質量shellを動かす技術と、負のstring・非自明な位相を準備する技術は別問題である。** [FKZ] は後者を通常物質から製造する処方も、量子場・送受信器のpost-CTC同時分布も与えない。

球面模型のQEI数値だけでこのringを禁止せず、逆にこのringの古典的時刻式へ球面模型の透過率を掛けて成功を宣言しない。
実在論文が与える**条件付き肯定の範囲**をそのまま保持する。

## 7. 今回の採否と、現実の装置に足りない物理

**現実の3+1次元で人間が制御可能な過去通信を作れる、という実証は得ていない。**
今回具体的に示したのは以下である。

- 一般相対論の4D候補は式にでき、実在論文には通常の正質量から時刻接続を制御する条件付き構成もある。
- 正常な4D量子場で負のエネルギーは作れる。しかし今回のpacketは全応力と時間幅の要求を満たさない。
- 滑らかな単一スケール喉の巨視的支持は通常scalarの短時間QEI診断で不適合。薄層へ移るなら別スケールが必要で、まだ材料・状態が得られたことにはならない。
- 情報が仮定された喉を透過することは、4D部分波と全結果の受信分布で確認できる。しかしそれを過去向きの同じ大域実験へ接合していない。

そのため**装置としての採用判定は「未成立／採用不可」**。自然界全体の不可能性を主張する判定ではない。
同じ模型を続けるなら、次は負のringまたは薄層の**具体的な作用・正の量子状態・有限core・自己無撞着な4D重力応答**を一つ選び、そこで同じ時刻接続と制御bitの全同時確率を解く必要がある。
その入力がないまま、時刻差や透過率の数値だけを最適化しても物理的成功へは進まない。

## 8. 再現・検証と実施範囲

```bash
python src/symbolic/wormhole_4d_geometry_support.py
python src/symbolic/scalar_4d_negative_packet.py
python src/symbolic/wormhole_4d_signal_scattering.py
python src/symbolic/ring_4d_mass_clock_control.py
```

ローカルはPython 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0。四本のassertとcompileを確認。
厳密計量・保存・source・sampling・部分波の恒等式に加え、独立な50/80桁の運動量積分、エネルギー積分、球Bessel接合、受信分布、SI scaleを照合する。
**SI入力GはCODATA 2022の代表値であり、物理精度が50桁という意味ではない。**

初回のpacket全応力を直接展開する計算は45秒でtimeout。全4Dの一般bilinear保存恒等式を先に証明し、wave equationを代入する同値な計算へ変更した。精度・成立条件を緩めていない。
local cloneはDNS失敗。固定SHAのconnector read/writeを使い、全repoのローカル実行を報告しない。
独立四本なので通常PRの累積差分選別を用いる。既存source・assert・依存・data・workflow・Leanは変更なし。
remote CIの実SHA・対象・run・完了結果はPRコメントに記録。全研究計算の再実行、独立査読、Lean形式証明は今回の範囲ではない。

## 一次資料：借りた内容と今回の導出を分離

1. **[MTY]** M. S. Morris, K. S. Thorne, U. Yurtsever, *Wormholes, Time Machines, and the Weak Energy Condition*, Phys. Rev. Lett. **61**, 1446–1449 (1988). [DOI](https://doi.org/10.1103/PhysRevLett.61.1446)。時間差付きwormholeの条件付き基本案。今回の量子状態やscattererの完成を同論文へ帰属させない。
2. **[Visser]** M. Visser, *Traversable wormholes: Some simple examples*, Phys. Rev. D **39**, 3182 (1989). [DOI](https://doi.org/10.1103/PhysRevD.39.3182)。cut-and-pasteとexotic sourceの参照。今回の球面junction・部分波式は直接再導出。
3. **[FR]** L. H. Ford, T. A. Roman, *Quantum Field Theory Constrains Traversable Wormhole Geometries*, Phys. Rev. D **53**, 5496 (1996). [gr-qc/9510071](https://arxiv.org/abs/gr-qc/9510071)。§4.1の(47),(48)をPDF本文・p.12画像で照合。局所平坦なQI適用は近似であるとの留保を保持。
4. **[FE]** C. J. Fewster, S. P. Eveson, *Bounds on negative energy densities in flat spacetime*, Phys. Rev. D **58**, 084010 (1998). [gr-qc/9805024](https://arxiv.org/abs/gr-qc/9805024)。PDF (2.2)–(2.5),(5.5)を照合。今回のcompact sampler・finite packetはその規約からの計算。
5. **[PF]** M. J. Pfenning, L. H. Ford, *Scalar Field Quantum Inequalities in Static Spacetimes*, Phys. Rev. D **57**, 3489 (1998). [gr-qc/9710055](https://arxiv.org/abs/gr-qc/9710055)。公式abstractの短時間展開とcurvature correctionの存在を参照。Ellisの全補正を同論文から取得したとはしない。
6. **[GGS1]** J. A. González, F. S. Guzmán, O. Sarbach, *Instability of wormholes supported by a ghost scalar field. I. Linear stability analysis*, Class. Quantum Grav. **26**, 015010 (2009). [0806.0608](https://arxiv.org/abs/0806.0608)。PDF §III、(34),(35)のpotentialとRayleigh boundを再現。
7. **[GGS2]** 同著者、*II. Nonlinear evolution*, Class. Quantum Grav. **26**, 015011 (2009). [0806.1370](https://arxiv.org/abs/0806.1370)。公式abstractのcollapse前のsignal検討を確認。不安定だから一切通れないという誤解を避けるため。
8. **[FKZ]** V. P. Frolov, P. Krtouš, A. Zelnikov, *Ring wormholes and time machines*, Phys. Rev. D **108**, 024034 (2023). [2305.03887v1](https://arxiv.org/abs/2305.03887v1)。PDF (2.8),(4.12),(5.35),(6.1)–(6.9)とp.17–18画像を確認。4Dの異なるring geometry、弱場・distant-mouth近似と既存negative stringの仮定を保持。
9. **[NR]** C. J. Fewster, T. A. Roman, *Null energy conditions in quantum field theory*, Phys. Rev. D **67**, 044003 (2003). [gr-qc/0209036](https://arxiv.org/abs/gr-qc/0209036)。四次元null-line平均の下限不存在と、timelike平均との違いを公式abstractで確認。
10. **[DS]** J. R. Fliss, B. Freivogel, E.-A. Kontou, *The double smeared null energy condition* (2021). [2111.05772](https://arxiv.org/abs/2111.05772)。四次元の有限幅を扱う別手法の参照。今回のcurved wormholeへDSNECの全式を適用したとはしない。
11. **[Constants]** CODATA 2022 / NIST [Newtonian constant](https://physics.nist.gov/cgi-bin/cuu/Value?bg)。`G=6.67430e-11`、SI定義のc,hを使用。統計的な実現確率は計算していない。

[FE]と[GGS1]のweb PDF画像取得はエラーで、該当式は抽出本文から確認した。図・表から値を転記していない。[FR]と[FKZ]は上記ページ画像も確認済み。
新しい基本定理、優先権、自然界での実装を主張する成果ではなく、実在論文を用いた4Dの再現・具体化・適用範囲の監査である。
