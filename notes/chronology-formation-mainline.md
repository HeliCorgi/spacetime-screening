# Chronology形成の本線: null return、候補の訂正、存在と形成の分離

2026-10-08。PR #40、読取親 `c6e6cda08ad73e457d135bcb9652a2355add9a9b`。
main基点 `1ff10c4453f52f9f8f8c2c835a52812ce7faac90`。
[検証記録](chronology-formation-validation.md)。署名 `(-+++)`、`c=hbar=1`。

## 0. 今回の目的と結論

目的を **有限資源・因果的な初期状態から、過去への到達を可能にする時空を形成できるか** に戻す。
Family 376の完全な物理compilerやR1のshear gateは、この存在問題の必要条件ではない。
既存の成果は保持するが、それらの完成を本線の前提にしない。

結論は次のように対象別に分かれる。

| 対象 | 今回得た結論 |
|---|---|
| Ori 2005/2007の指定されたvacuum coreを、通常の局所Hadamard KG場とともに滑らかに通過 | 非単位のnull帰還holonomyとHadamard対角条件が矛盾する。全地平面のcompact generationを先に決める必要がない |
| Xavier 2026の単純なz周期商 | 指数・sechの提示例は一般には計量が商へ降りない。正のfactorized vacuum familyで修復すると、非単位holonomyか、永続的な閉null軌道を持つ定常商に分かれる |
| `F(t)=t^3`等で地平面のboostを零にした交差 | boostだけでは検出できないが、近傍を巻くnull測地線と局所Hadamard条件が矛盾する |
| 完全なGrant boost＋並進商 | self-image null chordの帰還covectorが異なるため同じ障害。大質量での片側RSET有限性では救済されない |
| Grant領域を切り取る変更 | CTCを残しつつ上記の自己帰還null chordを全て領域外へ出す幾何学的対照例を構成。物理的な境界・有限装置の完成ではない |
| 時間周期Einstein宇宙 | 固定した繰込み処方と正のLambdaの下で、positive/局所CCR/Hadamardな熱状態と有限RSET、同じ計量の静的mean SCEEを構成。ただしCTCは最初から存在し、因果的な初期状態からの形成ではない |
| 元の有限資源・因果的初期状態からの形成問題全体 | 最新依頼の分類 **4**。ただし「文献がないから」ではなく、下記の具体的排除と実際の対照構成の後にも残る、非compact/境界完成を含む幾何・状態・形成の同時問題 |

指定模型への排除は、全てのbackreacted geometry、全相互作用場、量子重力に対する一般no-goではない。
時間周期Einstein宇宙は、より弱い**永続的な半古典CTC解の存在**の問題に対する構成であり、
今回の形成問題の答えへすり替えない。最小拡張での形成成功も認定しない。

### 証拠の水準

「確立済み」は引用した既知定理・既知の背景式、「既存理論からの解析的帰結」は下に証明を記した適用・合成、
「新しいが整合性のある仮説」は明示的に仮説とした変更案、「未検証」は残る物理的完成、
「明確な矛盾」は同時に課した仮定からの矛盾を意味する。
今回の解析的論証の独立査読と連続体QFT/GRのLean形式化は未実施。
Pythonがwavefront setや状態の存在を自動証明したという主張はしない。

## 1. 対象仕様をすり替えない

求めるのは、同じ一つの大域的模型について、(i)許容される因果的な過去領域とその初期データ、
(ii)有限資源の準備・物質源、(iii)滑らかなLorentz時空、(iv)局所的な量子場の整合性、
(v)その状態から計算した有限で保存するRSET、(vi)同じgの半古典方程式、(vii)物理的な帰還経路、を同時に満たすこと。

CTCの存在は `p << p` で判定し、座標時間の減少だけでは判定しない。
初期CauchyデータのMGHDがglobally hyperbolicなのは定義であり、それだけで全ての拡張の不存在は証明されない。
逆に、一つの都合のよい非一意な拡張を描くことは、装置で形成・制御できることの証明ではない。
「因果的な初期状態」は、永続的CTC時空の中から小さいGH chartだけを切り出すこととは区別する。

有限energy、有限の装置領域、有限準備時間、有限不可逆仕事も別の条件である。
とくに **有限energyからcompact generationを自動的には導けない**。
以下ではこの飛躍を使わず、より局所的な幾何証人から先に検査する。

## 2. 同じ点へ戻るnull covectorによる状態の排除

### 2.1 仮定と証明

Mを滑らかなtime-oriented Lorentz多様体とし、
`P=Box_g-m^2-xi R`（または同じ実principal symbolを持つ滑らかなnormally hyperbolic operator）を使う。
Wは `D'(M x M)` のbisolutionで、各点の十分小さい正規GH近傍で通常のHadamard条件を満たすと仮定する。

局所Hadamard条件は、対角において未来null covector kについて

\[
(p,k;p,-k)\in WF(W),
\]

を要求し、その点で許す二つのcovectorは正確に逆符号でなければならない。
ここで「平行ならよい」ではない。`WF(W)`は二変数の**同時の正スケール変換**に関してconicであり、
片方だけを任意に再スケールするものではない。[K,R]

M内のnull測地線区間がpから同じpへ戻り、affineにparallel transportされたcovectorが
`k1 != k0` になったとする。第一変数の特異性をこのbicharacteristicに沿って伝播させると、

\[
(p,k_1;p,-k_0)\in WF(W)
\]

となる。これは対角の局所Hadamard条件と矛盾する。
第一変数のprincipal symbolは `k0 != 0` のnull集合でreal principal typeであり、
この伝播にM全体のCauchy面は必要ない。

**帰結:** 同じ模型に通常のglobal bisolutionと全点局所Hadamard性を要求するなら、
このようなnull returnは許されない。positivity、Gaussian性、stationarity、energy条件より前の障害である。
滑らかなmassやcurvature couplingはlower-order項なので、この証人を消さない。

この方法自体の優先権は主張しない。KRWのSection 6は、自己交差・almost-closed null geodesicsによる
compact-generation外への拡張を既に論じている。[K]
本稿は具体的な計量・covector・領域条件を計算して、その論法を適用する。

### 2.2 閉軌道のnonaffinityからの判定

閉じたnull軌道の接線Kを周期座標psiで規格化し、

\[
\nabla_KK=\kappa(\psi)K
\]

とする。affine接線 `l=h K` は

\[
\frac{dh}{d\psi}=-\kappa h,
\qquad \frac{h(\ell)}{h(0)}=
\exp\left[-\int_0^\ell\kappa(\psi)d\psi\right].
\tag{H}
\]

右辺が1でなければ2.1の矛盾が出る。向きを反転すると倍率は逆数になるが、非単位であることは変わらない。
単にnonzero surface gravityを持つ**閉じていない**black-hole generatorを禁止する命題ではない。
倍率が1のときはこの検査が決められないだけで、状態の存在が従うわけでもない。

## 3. Oriのclassical formationを量子状態の段階で検査する

### 3.1 Ori 2005

原著のvacuum core [O05] を、横方向の具体的な調和関数を選んで

\[
g=-2dTdz+\{a(x^2-y^2)/2-T\}dz^2+dx^2+dy^2,
\quad z\sim z+\ell,
\]

とする。コードは4D計量から `det g=-1`、`Ricci=0` を再計算する。
中央の `T=x=y=0` で `K=partial_z` は閉null測地線の非affine接線で、

\[
\nabla_KK=-\tfrac12 K,\qquad h(\ell)/h(0)=e^{\ell/2}\ne1.
\]

したがって、**このcoreの閉generatorを含む領域全体で通常のHadamard KG状態を維持する案は不成立**。
初期のvacuum/dust/classical geometryの計算を否定しているのではない。

### 3.2 Ori 2007

原著 [O07] のpseudo-Schwarzschild coreで `t=2m-r, psi=v` とすると、

\[
g=-2dt\,d\psi-\frac{t}{2m-t}d\psi^2
 +(2m-t)^2(d\theta^2+\sinh^2\theta\,d\phi^2).
\]

`psi` の周期をellとする。4Dの `Ricci=0` を再計算し、`t=0` の閉null orbitについて

\[
\kappa=-\frac1{4m},\qquad h(\ell)/h(0)=e^{\ell/(4m)}\ne1
\]

を得る。よって同じHadamard obstructionがある。

[既存のcounterexample監査](chronology-realizability-counterexample-audit.md)は、Ori 2007の
古典的な初期値構成と拡張の非一意性を既に区別している。
今回加えるのは、**この具体的coreを量子場とともに完成する際の、帰還covectorによる排除**である。
原著がこの量子結論を証明したとも、既存Pythonが既に証明していたとも帰属させない。

両例とも全地平面のcompact generationやANECを先に判定する必要がない。
ただし、大きなbackreactionによって計量・閉軌道・帰還写像が変われば別模型であり、再検査する。
「classical backgroundに量子stressを少し足せるだろう」でこの矛盾を埋めることはできない。

## 4. Xavier 2026: 周期性の欠落と、ゼロboost修復の二分

### 4.1 原稿と既存repoの解釈の訂正

[X] の式(1)、本文II、付録Aは

\[
g=-2h(z,t)dt dz+[h(z,t)-f(x,y,z)]dz^2+dx^2+dy^2
\tag{X}
\]

を、**t,x,yを変えずにzとz+ellを同一視する商**として書く。
本文の指数例は `h=exp[k(epsilon z-alpha t)]`、図の例は `h=sech^2[k(z-2t)]`。
閉null軸の条件は `f(0,0,z)=h(z,0)`、横方向の勾配零である。
脚注11の一般局所vacuum解は `h=P(z)Q(z-2t)` とされる。

このsimple deck transformationでは計量係数がz周期でなければならない。
指数例の比は `h(z+ell,t)/h(z,t)=exp(k epsilon ell)`。
実パラメータでは `k epsilon=0` が必要である。
sech例も非零実kでは周期的でない（例えばt=z=0とz=ellの値が異なる）。
横調和性だけではfのz周期性は保証されない。
従って、これらを無条件に滑らかな時間機械の大域的計量として使うことはできない。

**局所vacuum性を否定したのではない。** local metricがRicci-flatでも、指定された商へ降りるとは限らない。
[既存監査の第5節](chronology-realizability-counterexample-audit.md)はこの問題を検査せず、
提示された周期coreとゼロboost tuningを有効な幾何候補として扱っていた。
その解釈は本節で訂正する。原稿の「外部source・matching未指定」という留保だけでは不足する。

### 4.2 一般factorized familyを実際に修復して調べる

P,Qを滑らかな正関数、tを全実数とする。hの周期性は

\[
P(z+\ell)Q(s+\ell)=P(z)Q(s)\quad\hbox{for all }z,s
\]

なので、ある一定の `c>0` について

\[
P(z+\ell)=cP(z),\qquad Q(s+\ell)=Q(s)/c.
\tag{F}
\]

**P,Qを個別に周期的と仮定してしまってはいけない。**
例えば `P=e^{-z}, Q(s)=e^s` なら `h=e^{-2t}` は正しく周期商へ降りるが `c=e^{-ell}` である。

指定された閉null軸において、直接計算で

\[
\Gamma^z_{zz}=\frac{h_z+h_t/2}{h}=P'/P
\]

となる。従って(H)の倍率は `1/c`。

* `c != 1`: 正しく商へ降りる例でも、閉null generatorの非単位holonomyにより2節のHadamard条件と矛盾する。
* `c = 1`: P,Qが周期的になる。次の**大域的**座標変換を使える。

`A'=Q` として

\[
v=\tfrac12[A(z)-A(z-2t)],\quad
 dv=Q(z-2t)dt+\tfrac12[Q(z)-Q(z-2t)]dz.
\]

Qの一周期積分は一定なのでvはz周期である。`v_t=Q(z-2t)>0` かつQは正の周期関数なので、
各zについてtの全実線をvの全実線へ写す。計量は

\[
g=-2P(z)dv dz+[P(z)Q(z)-f(x,y,z)]dz^2+dx^2+dy^2.
\tag{S}
\]

**vに依存しない。** 軸条件 `f(0,0,z)=P(z)Q(z)` を保持すると、
`x=y=0, v=constant` の閉null orbitは全てのvで既に存在する。
軸を一周するspacelike graph `v=v(z)` も、誘導計量 `-2P v' dz^2>0` が
全周で `v'<0` を要求して周期性に反するため存在しない。
因果的な初期coreから「最初の」閉null orbitを形成する提示仕様にはならない。

### 4.3 実在する周期修復の負例

`P=1, Q(s)=2+cos s, ell=2pi`、
`f=2+cos z+a(x^2-y^2)/2` を選ぶ。この時

\[
v=2t+[\sin z-\sin(z-2t)]/2,
\quad
 g=-2dv dz-a(x^2-y^2)dz^2/2+dx^2+dy^2.
\]

これは滑らかでRicci-flatな正しい周期商である。
`x^2>y^2` でv,x,y一定のz円はCTCとなる。
`|v-2t|<=1` だから、十分負のvを選べば、CTC全体を任意に早いt領域へ移せる。
修復でCTCを消したのではなく、**形成以前から存在していた**ことを明示した。

以上は指定simple deck・正factorized family・閉軸条件に対する二分である。
別のdeck map、tの領域制限、動的境界、別のvacuum ansatzを導入するなら、その新しい模型と初期データを再構成する必要がある。
ゼロboostの数値だけを根拠に形成可能と判定することはできない。

## 5. boostを零にした滑らかな交差にも別の障害がある

次のクラスを考える。

\[
g=-2dt d\psi-F(t)d\psi^2+a(t)^2h_{AB}dy^A dy^B,
\quad \psi\sim\psi+\ell,
\]

aは正でsmooth、hはRiemannian、`F(0)=0`、`F(t)<0` on `t<0`、`F(t)>0` on `t>0`。
初期側は `g^{tt}=F<0`、後側のpsi円はtimelike。
 transverse部分はcompactでもnoncompactでもよい。固定した横位置のbase null測地線は全計量でも測地線である。

`partial_t` はaffine nullで、そのcovectorは `(0,-1)`。
もう一方のnull測地線をt自身でaffineにparametrizeすると

\[
V=(1,-2/F),\qquad V^\flat=(2/F,1).
\tag{W}
\]

任意の `t_j -> 0-` に対して

\[
\int_{t_j}^{t'_j}-\frac2{F(s)}ds=\ell
\]

を満たす `t_j<t'_j<0` が存在する。FがsmoothでF(0)=0なので、
あるCについて `|F(s)|<=C|s|`、従って積分は0に近づくと発散する。
両端点はpsiを一周して同じpsiに戻り、地平面上の一点へ近づく。

その地平面点の一つの小さいconvex normal neighborhood Uを固定する。
十分大きなjでは両端点はU内にあり、U内の短いnull接続は `partial_t` 方向である。
一方、Uの外を巻く(W)に沿った特異性伝播は、その点対に `(2/F,1)` 方向のWFを強制する。
これはUのHadamard parametrixが許す方向ではない。従ってWの全点局所Hadamard性と矛盾する。

例えばF=tでは `t=-s -> t'=-s exp(-ell/2)`。
F=t^3では `t'=-s/sqrt(1+ell s^2)`。
後者は `F'(0)=0`、地平面orbitのholonomyは1だが、上の近傍の論証はそのまま成立する。
無限次でflatなsign crossingにも同じsmoothness評価を使える。
曲率が有限、地平面のboostが零、横空間がnoncompact、という変更だけではこのクラスを救済しない。
任意のdegenerate horizonを包含する一般定理と称してはいけない。

## 6. Grant: 非compact性を検査し、領域切取りの本当の逃げ道も残す

### 6.1 完全な商のself-return

被覆Minkowski計量を `-du dv+dy^2+dz^2`、deck mapを

\[
\Gamma(u,v,y,z)=(u/2,2v,y+1,z)
\]

とする。[G,T]のboost＋transverse translationの規格化例。
整数n>0に対して

\[
u=1,\quad v=-\frac{n^2}{2^n+2^{-n}-2}
\]

を選ぶとpと `Gamma^n p` の直線intervalは厳密にnull。
その接線のtransverse成分はnで非零、帰還時のboostはu,v成分だけを変える。
したがってdeck mapで始点へ戻したcovectorは元と一致せず、比例すらしない。
2節により、**完全なGrant商の全点に通常のHadamard bisolutionを置く案は不成立**。

nを大きくすると `uv -> 0-`。これらはpolarized hypersurfacesに対応する。
大質量でchronal側からの特定RSET極限が有限になり得るという[T]の計算と矛盾しない。
全点Hadamard性と片側のtensor成分の極限は違う。[K] Section 6もこの区別を指摘している。

### 6.2 完全な証人が領域に入っているか

上のnull chordの中点は

\[
(uv)_{mid}=v(2^n+2^{-n}+2)/4.
\]

端点はuv=0へ近づくが、中点は大きく負になる。
**端点の集積だけを使って、任意に薄く切り取った領域のno-goを証明したことにはできない。**
これを明示的な負例で検査する。

Rindler側に `u=r exp(-eta), v=-r exp(eta)` とおくと、
計量は `dr^2-r^2 d eta^2+dy^2+dz^2`、deck mapは `eta -> eta+log2, y -> y+1`。
領域を `uv>-R^2`、`R=29/20=1.45` に制限する。
`r=289/200=1.445` の閉Killing orbitのnormは

\[
K^2=1-r^2(\log2)^2<0.
\]

よってCTCは残る。この不等式はlog2の正の有理級数とtailで保証した。
一方、null self-image chordの最大rは

\[
r_{peak}(n)=\frac n2\coth\frac{n\log2}{2}\ge\frac32>R.
\]

`x coth x` はx>0で増加する。微分の符号は `sinh x cosh x>x` から得られる。
Minkowski上のnull測地線は直線なので、この領域には全体が含まれる非自明な自己帰還null測地線がない。
CTCがあるだけで2節の証人が必ずある、という逆向き推論への幾何学的反例である。

この切取りにはtimelikeな穴／境界と非compact方向が残る。
透明にMinkowskiへ完成すれば失われたchordが戻る。
反射壁等を置けば、wall stress、境界条件、境界を含む場代数・Hadamard処方、準備過程が必要である。
どちらも今回構成していない。切取りを「有限の物理装置」と呼ばない。
この領域の実際のchronology horizonをuv=0と未検証で同定することもしない。


### 6.3 切取りの逃げ道を、drift方向の周期化で有限化できるか

そこで停止せず、切取りを有限の空間へ近づける自然な変更も検査する。
追加の同一視 `y~y+B`（B>0）を導入すると、`Gamma^n` とこの並進のm回の合成のdriftは
`b=n+mB`。そのnull chordは

\[
uv=-\frac{b^2}{2^n+2^{-n}-2},\qquad
r_{peak}=\frac{|b|}{2}\coth\frac{n\log2}{2}.
\]

n>=1ではcothの因子が3以下なので `r_peak<=3|b|/2`。
任意の正整数Nについて、N+1個の数 `0,1/B,...,N/B` の小数部分をN区間へ入れるpigeonhole原理から、
ある `1<=n<=N` と整数mで `|n+mB|<=B/N` を得る。
`N>3B/(2R)` を選べばr_peak<R。
`b=0` の場合も、uv=0上に純boostのnull chordがあり、帰還covectorの倍率は非単位である。

従って **任意のB>0について、drift方向をこの並進で周期化すると、切取りの内側にbad null returnが戻る**。
Bが無理数でも回避できない。コードはB=1,10/7,sqrt(2),sqrt(101)を別々に検査する。
この結果は、6.2の「穴＋並進drift」の回避をそのままtorus化して有限装置とする変更を排除する。
一般の端部・反射壁・非周期的な局在装置まで排除したわけではない。


## 7. 正のHadamard状態と同じgのSCEEを実際に閉じる対照構成

### 7.1 Eternal Einstein宇宙の時間商

これは形成問題から条件を外した**対照問題**である。

\[
M_a=(\mathbb R/2\pi a\mathbb Z)_\tau\times S^3,
\qquad g_a=-d\tau^2+a^2d\Omega_3^2.
\tag{E}
\]

空間点一定の時間円はCTCで、全点がchronology-violating。
過去にchronalなCauchy初期状態を持たない。
被覆上のround S3 null測地線は2pi aで同じ点・同じcovectorへ戻るため、2節の非単位return obstructionはない。
KRWが述べるrefocusingの例外と整合する。[K]

### 7.2 Two-point functionの構成とpositivity

通常のmassless conformally coupled real scalarを一つ用いる。
S3の実直交固有関数 `Y_{jA}` をradius aのvolumeで規格化する。
frequencyは `omega_j=j/a`、degeneracyはj^2、j=1,2,...。
逆温度beta>0を用い、`b=beta/a, n_j=(exp(b j)-1)^-1` として

\[
W_\beta=\sum_{j,A}\frac{Y_{jA}(\Omega)Y_{jA}(\Omega')}{2\omega_j}
[(1+n_j)e^{-i\omega_j(\tau-\tau')}+n_j e^{i\omega_j(\tau-\tau')}].
\tag{2pt}
\]

各weightは非負。任意のsmooth test functionに対する二次形式は、modeへの射影の絶対値二乗の非負和なのでpositive。
被覆のquasifree thermal stateも使える。[SV]
全周波数がj/aなので、Wは両変数で独立に2pi a周期であり商へ降りる。
商上のtest functionを時間方向のpartition of unityでcompactに持ち上げても同じ二次形式となる。
Fourier係数は分布を定義する成長条件を満たす。

反対称部分はn_jに依存せず、被覆の通常のcommutatorと一致する。
小さいinjective GH chartではそのchartのPauli–Jordan関数に一致するため局所CCR/F-local条件を満たす。
商全体に一意なretarded propagatorがあるとは仮定しない。

被覆vacuumの閉形式は、角距離chiについて

\[
W_0=\frac1{8\pi^2a^2[\cos((\Delta\tau-i0)/a)-\cos\chi]}.
\]

小さいchartで通常のHadamard形を持つ。熱補正はjについて指数減衰し、任意回微分による多項式増大を支配するのでsmooth。
従って(2pt)は商上で全点**局所Hadamard**である。
これは有限modeのpositivityから連続体へ外挿した主張ではなく、全mode級数の解析である。
実時間の商周期2pi aと、虚時間KMSの逆温度betaを同一視しない。

### 7.3 固定したrenormalizationとSCEE

繰込み処方を先に固定する。[A]の標準的conformal-scalar ESU Casimir値に対応する
local covariant prescriptionを用い、その処方でmatchedした重力側の有限curvature-squared係数を零とする。
G>0とLambda>0も先に固定する。異なる処方で係数を移す場合は両辺を一緒に変えなければならない。

\[
S(b)=\frac1{240}+\sum_{j=1}^\infty\frac{j^3}{e^{bj}-1},\quad
\rho=\frac{S(b)}{2\pi^2a^4},\quad p=\rho/3.
\tag{RSET}
\]

真空項は `rho_vac=1/(480pi^2 a^4)`。[A]
等方性・保存則とconformal traceからpを得る。
(E)で `R=6/a^2, Ric^2=Riem^2=12/a^4`、Weyl平方・Euler密度・Box Rは全て零なので、trace anomalyも零。
RSETは全点で有限であり、空間切断のenergy `E=2pi^2a^3 rho` も有限。
この切断はspacelikeだがCauchyではなく、有限energyの初期準備を証明するものではない。

独立な二つの静的mean semiclassical Einstein equationsは

\[
3/a^2-\Lambda=8\pi G\rho,\qquad
-1/a^2+\Lambda=8\pi G\rho/3.
\]

同じaを(2pt)と(RSET)に使って解くと

\[
\boxed{a^2=\frac3{2\Lambda},\qquad S(b)=\frac{9\pi}{16G\Lambda}.}
\tag{SC}
\]

Sはb>0で連続・厳密減少し、b->infinityで1/240、b->0でinfinity。
従って、先に固定した `0<G Lambda<135pi` に対して、**唯一の有限のb>0が存在**する。
必要stressをGから逆定義したのではなく、実際の状態のRSETの級数がこの値を取ることを示した。
Lambda=0ではこの静的radiation ansatzに解はない。

### 7.4 具体値の区間証明

先に `G=1, Lambda=1/100000000` を固定した。
convergentな全spectrum級数の8000項と、正のtailの解析的上界を使い、
60桁の外向きinterval演算で

\[
0.0138455100136228553444093234128933984378
 <b<
0.0138455100136228553444113234128933984378
\]

を保証した。各端点のtargetとの差は約5.1e-14、tailは3.0e-35未満。
高温漸近式はbracketのseedだけで、最終方程式の代用にはしていない。
occupation multiplicityを先に和する別のLambert級数とも照合した。

| 量 | 参考値（G=1の単位） |
|---|---:|
| a | 12247.4487139158904909864203735 |
| beta | 169.572173809854823119617824043 |
| rho | 3.97887357729738339422209408431e-10 |
| 空間切断energy | 14428.6855893209710748704090463 |
| 実時間周期 | 76952.9898097118457326421815803 |

**得られたのは、標準自由場のmean SCEEにおける永続的な自己無撞着解である。**
形成、物理的準備、非線形安定性、smearingしたstress fluctuationの小ささ、量子重力の全補正は認定していない。
小さい曲率だけで半古典近似の全ての制御が完了したとも言わない。
元の広い「CTC＋Hadamard＋有限RSET＋同じgのmean SCEEがどこかで共存するか」という問題と、
最新の「因果的初期状態から形成できるか」はこの実例で明確に分離される。

## 8. 既知の制約を、仮定ごとに照合する

| 結果 | 必要な仮定・射程 | 今回何を決め、何を決めないか |
|---|---|---|
| KRW [K] | smoothな場の模型、初期GH領域のHadamard状態、bisolution延長、compactly generated Cauchy horizon。localized版もある | base pointでHadamard破綻。全RSET成分が全経路で数値的にinfinityになるとは言わない。finite energyからcompact generationは導かない |
| Hawking [H] | 指定の初期面・生成条件・energy条件。非compact初期面でのcompact generationの議論を含む | 古典energy条件だけで全形成を禁止しない。Oriのcompact initial coreとcompactly generated horizonを混同しない |
| Topological censorship [TC] | 漸近平坦性、global causalityの仮定、適切なANEC等 | それらを満たす可視topological shortcutを制限。CTC域のGH性を先に仮定して全CTCを排除したとはしない |
| QEI [FR] | 場・次元・coupling・平均を取る曲線とsamplingに依存 | timelike平均の不等式を4D null worldlineへ無断移植しない。4Dの単一null線上には対応する一般下界がない場合がある |
| 最近のQNEI [Q26] | interacting QFTの特定のsemilocal/null平均・領域の条件 | null不等式が全て存在しないとは言わない。今回の曲がったchronology境界・wallのRSETを自動的に評価しない |
| Achronal ANEC [AN] | complete achronal geodesicやself-consistency等の条件 | 閉causal曲線や任意の不完全generatorへ同一の結論を使わない。一般曲率・全状態で無条件に確立した仮定として置かない |
| Backreaction | 同じgからWを作り、固定したfinite countertermsでRSETを求めて方程式を閉じる | bad null returnを持つexact gならmass・状態選択・有限countertermではWF矛盾を消せない。g自体を変更した候補は再解析する |

この表は文献の列挙を結論とするためではない。
本稿の具体的排除は2–6節、構成は6.2と7節で行い、この表でその射程を越えていないかを検査する。

## 9. 矛盾を避ける変更を、同じ目的を保つかまで検査する

| 変更 | 実際に得たもの | 形成問題への残り |
|---|---|---|
| mass増大・nonGaussian状態・CBSSL選択 | 通常KGのprincipal symbolと局所Hadamardを保持する限り2節を回避しない | 別の状態を選ぶだけでは不可 |
| generatorのboostを零にする | 5節の交差は依然不可。Xavierのpositive factorized periodic修復は4節の二分 | 別の幾何の帰還写像・近傍まで調べる必要がある |
| compact generationを外す | Ori/完全Grantは今回の別の局所検査にかかる | 非compactというラベルだけでは足りない |
| 領域を切り取る | 6.2のように幾何の証人を実際に消せる | wall/境界条件/全応力/有限準備を伴う一つの完成が未検証 |
| 全null光円錐がrefocusする空間へ替える | 7節のpositive Hadamard stateとmean SCEEを実際に構成 | eternal CTC。形成を証明する初期過去がない |
| hard cutoffやnonlocal principal operator | 通常の特異性伝播の仮定を外せる可能性 | 元のHadamard仕様からも外れ得る。新しいaction、unitarity、局所極限、保存、sourceと形成解を提示するまで成功ではない |
| 相互作用・full string/quantum gravity | 本稿の通常free KGの射程外 | 整合的な拡張であることだけから有限資源形成が従わない |

変更の可能性を未検証のまま「最小拡張で可能」とは認定しない。
一方、6.2や7節があるため「全CTCは必ず同じnull-return no-goにかかる」とも主張しない。

## 10. 戦略の更新と、本当に残る障害

最速の本線は、R1の非線形流体評価やuniversal compilerを完成してからgeometryを探すことではない。
**候補の大域的同一視とnull帰還を先に確定し、量子状態がそもそも置ける候補だけに物質源・backreactionの計算を投入する。**
今回、古典形成の有力な既存coreと最近のゼロboost候補をこの順序で検査できた。

現在残る問題は、次を同じ一つの形成過程として両立することである。

1. CTCが初期から存在しておらず、有限資源で準備した因果的な過去から始まる。
2. 形成境界とその近傍で、bad null returnとKRWの障害を回避する。
3. 回避のために切り取った領域を、保存則・場の境界条件・wall stressを含む物理模型へ完成する。
4. その完成したgのpositive Hadamard W、有限RSET、同じgのSCEEが同時に成立する。

6.2のGrant collarは2の一部を本当に回避するが3と4を解いていない。
7節のESUは2と4のmean-field版を実現するが1を満たさない。
これが、今回の分類4の**具体的な境界**である。全物質の一般no-goも、最小拡張による形成解もまだない。

次に有益なのは、切取りで消えたnull経路を物理的な境界・接合が再導入するか、あるいは
refocusing型の許容state–geometryを保ちながら初期chronal領域に接続できるかを、
一つの完全なgとfield domainで判定することである。
前者を優先し、透明接合・反射境界・動的wallを区別する。単純なdriftの周期化は6.3で既に排除した。単に「Hadamard性を仮定する」「壁は無視する」ことはしない。
ユーザーに補題を一つずつ選ばせる研究計画には戻さない。

## 11. 再現用コードと非主張

- [geometry forward](../src/symbolic/chronology_null_return.py): Levi-Civita/Ricci、周期性、座標pullback、degenerate交差、Grant証人と領域の負例。
- [独立verifier](../src/symbolic/chronology_null_return_verify.py): Hamilton方程式、独立covector計算、有理証人、別のlog2級数、周期修復。
- [ESU対照](../src/symbolic/chronology_esu_control.py): KG・曲率invariant・Einstein代数、収束級数＋tailによる熱状態root。

forward/verifierの一致は独立した物理査読ではない。有限のmodeや格子を連続体の存在証明に代用しない。
ノートのWFとglobal stateの論証が理論部分であり、コードはその入力となる具体的等式・区間・負例を検査する。

## 一次資料

- [K] Kay–Radzikowski–Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, CMP 183 (1997) 533–556, [gr-qc/9603012v2](https://arxiv.org/abs/gr-qc/9603012v2), especially Theorem 2/2' and Section 6.
- [R] Fewster–Verch, *Algebraic quantum field theory in curved spacetimes*, [1412.5945](https://arxiv.org/abs/1412.5945), local Hadamard/microlocal formulation.
- [O05] Ori, *A new time-machine model with compact vacuum core*, PRL 95 (2005) 021101, [gr-qc/0503077](https://arxiv.org/abs/gr-qc/0503077).
- [O07] Ori, *Formation of closed timelike curves in a composite vacuum/dust asymptotically-flat spacetime*, PRD 76 (2007) 044002, [gr-qc/0701024v3](https://arxiv.org/abs/gr-qc/0701024v3), core metric Eq.(2).
- [X] Xavier, *Closed Timelike Curves from a Vacuum Traveling Wave*, [2607.00788v1](https://arxiv.org/html/2607.00788v1), Eq.(1),(2), Appendix A, footnote 11. 2026年7月のpreprint。今回の周期性訂正は原著の結論として引用しない。
- [G] Grant, *Cosmic strings and chronology protection*, PRD 47 (1993) 2388, [hep-th/9209102](https://arxiv.org/abs/hep-th/9209102).
- [T] Tanaka–Hiscock, *Massive scalar field in multiply connected flat spacetimes*, PRD 52 (1995) 4503, [gr-qc/9504021](https://arxiv.org/abs/gr-qc/9504021).
- [A] Altaie, *Back reaction of quantum fields in an Einstein universe*, PRD 65 (2002) 044028, [gr-qc/0104100](https://arxiv.org/abs/gr-qc/0104100), conformal-scalar thermal/Casimir stress. 時間商への降下と形成の判定は本稿で別に行う。
- [SV] Sahlmann–Verch, *Passivity and microlocal spectrum condition*, CMP 214 (2000) 705–731, [math-ph/0002021](https://arxiv.org/abs/math-ph/0002021). 適用先はまずGH被覆である。
- [H] Hawking, *Chronology protection conjecture*, PRD 46 (1992) 603, [DOI](https://doi.org/10.1103/PhysRevD.46.603).
- [TC] Friedman–Schleich–Witt, *Topological censorship*, PRL 71 (1993) 1486, [gr-qc/9305017](https://arxiv.org/abs/gr-qc/9305017).
- [FR] Fewster–Roman, *Null energy conditions in quantum field theory*, PRD 67 (2003) 044003, erratum PRD 80 (2009) 069903, [gr-qc/0209036](https://arxiv.org/abs/gr-qc/0209036).
- [AN] Graham–Olum, *Achronal averaged null energy condition*, PRD 76 (2007) 064001, [0705.3193](https://arxiv.org/abs/0705.3193).
- [Q26] Fliss–Rolph, *Curious QNEIs from QNEC: New Bounds on Null Energy in Quantum Field Theory*, JHEP 09 (2026) 273, [2510.26247v2](https://arxiv.org/html/2510.26247v2). 最新結果を認識することと、本候補に適用条件を満たしたと認めることは別である。
