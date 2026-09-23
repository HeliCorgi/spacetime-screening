# 「残る10%」への反証試行：フィードバック整合性とNUTの逃げ道

**2026-09-23 / 条件付きno-goの適用・独立検算・不成功だった反証試行。**

**結論：通常の量子操作を任意に接続できる、操作に依存しない線形の過去向き通信路は成立しない。** これは明記した操作論的クラスの否定であり、自然界の過去通信全体の禁止ではない。
**同時に、NUT内部を閉じたnull測地線の反復で一括排除する試みは失敗した。** 対象計量にはそのような内部測地線がない。肯定側に不利でない結果も保存する。

読取基点は未マージPR #11の `ad05b9b59a595765a822f7c18155820bdafbf1dc`、mainは `4bc7d4b022345a1b618a0f44b1481ebb1954ea94`。
[前回の場・検出器ノート](taubnut-field-detector-closure.md)と[KRW監査](operational-past-signalling-focus.md)を引き継ぐ。
PR #11へ追記し、mainは変更しない。既存の計算は取り消さない。

会話の「可能10%、不可能90%」は主観的な見立てで、校正された統計でも自然界での成功頻度でもない。このノートでは、既知の障害を独立な証拠として二重計上したり、検査項目の数だけ10%を減らしたりしない。優先権も主張しない。

## 0. どの逃げ道を攻めたか

| 逃げ道／主張 | 今回の判定 | 範囲 |
|---|---|---|
| 弱く雑音のある過去通信なら、普通の装置と自由に接続できる | **条件付きで棄却** | 操作非依存・線形・全フィードバックで正規化、を同時要求すると信号差は0 |
| 場から得た局所確率を、そのまま長いB→Aの実験室へ接続する | **無条件の接続を棄却** | 前回の確率式を直接検査。接続後の物理核が変わる可能性までは排除しない |
| NUT内部にも閉じた光の測地線があるので反復発散する | **この反証試行が失敗** | 第一NUT領域のnull測地線に内部閉軌道なし。CTCや駆動された信号は残る |
| exactな弦補正・小さい結合なら地平面の問題は消える | **その保証を棄却** | exact計量にも非零のboostが残る。実際の弦振幅／全逆反作用のno-goではない |
| F-local場代数のあるCTC円筒を持ち込めば安定な装置になる | **根拠不足・適用範囲を縮小** | 2次元massive模型でgenericな計量変形は不適合。4次元NUTへの定理ではない |
| 通過可能ワームホール／P-CTC容量の論文が成功例になる | **その読み替えを棄却** | 時間方向と物理的実装が別。既知の肯定的計算そのものは否定しない |

## 1. フィードバック試験は、何を仮定するか

受信Bが実験室の固有時で送信Aより先、B→Aには通常の記録伝送と計算をするtimelike経路があるとする。前回のNUT配置はその幾何学的経路を持つ。
まずBで得たビットyを保存し、Aで **0固定・1固定・yをコピー・yを反転** のいずれかを送れるかを問う。

以下のno-goの仮定は次の三つである。

1. 外部の過去向き過程が、実験室内でどの操作を選ぶかによらない一つの線形確率汎関数／processで表現できる。
2. B→Aの実験室で、通常の量子instrument（特に上の4つの古典制御）を自由に選べる。補助系・記録・失敗結果も含める。
3. 全結果の確率は正で総和1。操作や成功例ごとの事後的な再正規化を追加しない。

**この三つが、CTC幾何や局所場の存在だけから自動的に従うとはしていない。** 特に、長い実験室を外部から独立した「入力B・出力A」の二端子装置と見なせることは追加の構成上の仮定である。
装置を変えるたび背景や大域的gluingが変わる、外部との未記述の相関が必要、特定のフィードバックが実装不能、確率法則が非線形、といった場合はこの定理の外である。

これは「過去へ送れない」を自由選択の定義へ入れた証明ではない。事前に過去の受信分布を固定せず、出力から入力への任意の核を認めた上で、接続した実験の正規化を検査する。ただし、**通常の自由な接続可能性を持たない過去通信まで定義から除外はしない**。

## 2. 前回の場の確率式を直接攻撃する

コード：[operational_feedback_consistency.py](../src/symbolic/operational_feedback_consistency.py)。

前回の記録付き場・検出器実験では、受信Y測定をビットyに読み替えると、局所のA→B順序の下で

```math
K(y\mid b)=\frac{1+(-1)^{y+b}d}{2},\qquad
d=e^{-2V_B}\sin(2\Delta_{AB}),\qquad |d|\le1.
```

識別可能性は `D_B=|d|`。これは**開いた局所実験**の式であり、まだ大域的なループの式ではない。
ここへフィードバック `b=f(y)` を、その核を変えず通常の積と和で接続すると、全履歴の重みは

```math
Z_f=\sum_yK(y\mid f(y)).
```

厳密計算の結果は

```math
Z_{b=0}=Z_{b=1}=1,\qquad
Z_{\rm copy}=1+d,\qquad Z_{\rm NOT}=1-d.
```

従って4つ全ての操作で正規化するためには **d=0** が必要。
例えば雑音を含む正常なbinary channel `d=1/3` でも、コピーで4/3、反転で2/3となる。
これは「矛盾した測定が実際に起きる」という予言ではなく、**その開いた核を不変なまま閉路へ接続する構成の失敗**である。

### 2.1 非対称なノイズ、有限アルファベットでも同じ

一般のbinary kernelを

```math
K=\begin{pmatrix}u&v\\1-u&1-v\end{pmatrix}
```

とするとコピー／反転の重みは `1+(u-v)` と `1-(u-v)`、信号差は `|u-v|`。
対称性や完全伝送は不要である。

一般の有限な受信集合Yと送信集合Bでも、全ての写像 `f:Y→B` に対して `sum_y K(y|f(y))=1` を要求すると、任意の一つのyだけ送信値を変えた二つのfの差から `K(y|b)=K(y|b')` が出る。従って全ての行が入力非依存になる。
コードでは2×2、3×2、2×3、3×3で全決定的fを列挙し、線形制約のrankと解を厳密に検査する。一般のサイズの結論は、この二写像の差の証明による。

### 2.2 「ほんの少しの雑音で救う」には限界がある

前向き制御にも誤りを入れ、コピー相関がrのbinary channelとすると、閉路の重みは `Z=1+dr`。
有限のdとrを保つ限り、単なる不完全性で正規化の問題は消えない。r=0という無情報の前向き操作だけを残せば回避できるが、自由なコピー／反転能力を捨てている。

核自体を変えて救う場合も、元の二つの条件付き分布からのTV距離が各々epsilon以下なら、コピー／反転の正規化を厳密に直すには少なくとも `epsilon >= |u-v|/2` が必要。二つの列をその平均へ移す無信号核で、この下限を達成できる。
一般に、二つの列の許容修正をepsilon_0,epsilon_1、正規化誤差をepsilon_Nとするなら

```math
|u-v|\le\epsilon_0+\epsilon_1+\epsilon_N
```

が必要。この誤差尺度は、**仮定した古典kernelの変化**であり、重力の計量摂動や量子重力の誤差そのものではない。

### 2.3 再正規化すれば数式上は救えるが、法則が変わる

`K(y|f(y))/Z_f` は `Z_f>0` のとき正規化できる。従って「どの数理的ループ処方も不可能」ではない。
しかし、コピーを確率q、反転を1-qで混ぜてから一度だけ閉路正規化すると、コピーを選んだflagの確率は

```math
\frac{q(1+d)}{q(1+d)+(1-q)(1-d)}.
```

q=1/2なら `(1+d)/2`。先にそれぞれの処方を正規化してから混ぜる手順とは違う。
これは通常のaffineな操作の混合則を保てないことを示す負例である。
基礎法則が本当にこうしたfinal-state／非線形規則を与える可能性は、この代数で否定できない。しかし、その法則を場・装置から導く必要がある。普通の量子場公式に分母だけを手で足して成功とはしない。

## 3. 量子版は既知のone-party process定理に一致する

Oreshkov–Costa–Brukner [P1, Appendix C, Eq. (19)] は、局所量子操作の線形構造・全CPTP操作に対する正規化から、単一partyのprocessが状態に還元されることを示す。
今回はその既知結果を、具体的な場の送受信式へ接続し、独立の有限行列で再現する。新定理とは呼ばない。

inputをBで受け取る系I、outputをAで送る系Oとして、確率を `p(M)=Tr(WM)` と表す。Mは標準Choi行列の**全転置**という[P1]の規約に固定する。
全CPTP行列 `M>=0, Tr_O M=I_I` について `Tr(WM)=1` を要求する。

完全depolarizing mapのChoi行列 `M_0=I_I⊗I_O/d_O` は正定値なので、任意のHermitian Xで `Tr_O X=0` に対し十分小さい±epsilonについて `M_0±epsilon X` はCPTP。
両符号の正規化の差から `Tr(WX)=0`。部分traceのkernelの直交補は `rho_I⊗I_O` の空間なので

```math
W=\rho_I\otimes I_O,\qquad\rho_I\succeq0,\quad\operatorname{Tr}\rho_I=1.
```

これにより入力の結果は後の出力操作で制御できない。

qubitでは16個の実Pauli係数に対し、正規化制約のrankは13。自由度は密度行列の3個だけになる。
コードは `I_4/2 ± (sigma_i⊗sigma_j)/4`（i=0,…,3、j=1,…,3）の**実際にCPTPである24行列**を用い、正値性・部分trace・rank・解を検査する。

前回の場の受信状態をbackward measure-prepare channelとして書いた候補は

```math
W_{\rm field}=\frac12\left[I\otimes I+
\nu\cos(2\Delta)X\otimes I+\nu\sin(2\Delta)Y\otimes Z\right],
\qquad \nu=e^{-2V_B}.
```

これは0≤nu≤1なら正で、逆方向channelとしてのtrace条件も満たす。しかし `Y⊗Z` 項はone-party processに許されず、Y測定とコピー／NOTのCPTP操作が正規化違反を検出する。
**「正のChoi行列を作れた」と「全フィードバックで物理的に接続できる」は違う。**

多party・複数round・時間に非局在した量子操作の全てをこの単一party式に押し込めていない。[P2]のmulti-round拡張が必要な場合がある。NUTの長い実験室が単一の自由なinstrumentとして閉じているか、これ自体が検証項目である。

## 4. NUT-onlyを光の閉軌道で潰せるか：反証試行は失敗

コード：[taubnut_loophole_geometry.py](../src/symbolic/taubnut_loophole_geometry.py)。

[J]と既存repoの非回転heterotic計量について

```math
p=x^2-1,\quad D=(x+\delta)^2-ap,\quad a=4/(k+2),\quad
K=(k-2)\alpha',\quad x>1,\quad\delta>1,\quad k>2.
```

この範囲は幾何学的式の範囲である。任意の実k,delta,lambdaが異常相殺されたheterotic模型を与えるとはしていない。数値は従来と同じ `k=8,delta=sqrt(8/5),lambda=sqrt(2/5)` を使用する。

Kをaffine parameterへ吸収したnull Hamiltonianは

```math
2\mathcal H=p\,p_x^2+\mathcal L^2-\frac Dp E^2=0,\qquad E=-p_t,
```
```math
\mathcal L^2=p_\theta^2+
\frac{(p_\phi-\lambda E\cos\theta)^2}{\sin^2\theta}.
```

コードは `PoissonBracket(L²,H)=0` を直接検査する。角度の軸では通常の束chartを切り替えるが、この保存量はmonopoleの共変角運動量の大きさとして一価である。
第一NUT領域では `partial_t` がtimelikeなので、非零のfuture nullベクトルにはE>0。

```math
\dot x^2=E^2D-\mathcal L^2p,\qquad
\left(\frac Dp\right)'=
-\frac{2(x+\delta)(\delta x+1)}{(x^2-1)^2}<0.
```

turning pointで `L²/E²=D/p` を代入すると

```math
\ddot x=-\frac{E^2(x+\delta)(\delta x+1)}{x^2-1}<0.
```

従って全turning pointは厳密な極大であり、極小は存在しない。一定xのnull測地線も、必要な `(D/p)'=0` を満たせない。
もし内部に閉じたnull測地線があれば、一価な実数座標xは閉曲線上で極小を持つか一定となるため矛盾する。よって**第一NUT領域内に完結する閉じたnull測地線はない**。

これはstring-frameと、滑らかな正のconformal factorで関係する補助Einstein-frameで同じ結論（null曲線の像は同じ）である。
有限のいくつかの軌道だけからの推定ではない。

数値対照では `L²/E²=1,2,4` の唯一の径方向極大は、それぞれ
`x=7.34557779284, 2.82013759791, 1.75156671291`。`L²/E² <= 3/5` ではturning pointなし。

**これは過去通信の肯定ではない。** 加速されたtimelike閉曲線や、散乱・導波路・装置で曲げる信号を否定しない。地平面上のnull生成線もこの開領域の外である。
同時に「地平面の反復blueshiftをNUT内の全信号へそのまま移す」不正確なno-goは退けられた。NUT-onlyを反証するには別の議論が要る。

## 5. exactな弦補正が地平面を救う、という保証もない

前回までに得たboost倍率を再現し、今回は運動量スケールの非一様性を検査する。
[J]は背景幾何のalpha-prime補正を与えるが、probeによる応答は別と明記する。ここでall-orders背景とall-interactionsの安定性を同一視しない。

`rho=x-1, d=1+delta, q=t-r_*` とすると、固定角度での補助Einstein計量の先頭項は

```math
ds^2_{E,\rm fib}=-2K\,dq\,d\rho-\frac{2K}{d}\rho\,dq^2.
```

`U=exp(-q/d), V=rho exp(q/d)` で `ds²=2Kd dU dV`。
qの周期 `T=4pi lambda` は、この**局所地平面模型**で

```math
(U,V)\sim(e^{-\gamma}U,e^\gamma V),\qquad
\gamma=\frac{4\pi\lambda}{1+\delta}=3.50904313141742895922\ldots
```

というboostになる。倍率は `exp(gamma)=33.4162774950530781787...`。
`D(1)=d²` と地平面の一次係数から分かるように、delta,lambdaを固定した有限k補正はこのboostを消さない。kの変更と異常相殺電荷の変更を自由に独立にできるとは言わない。
**これは全NUT時空をtだけほどいた大域被覆ではない**。前回のHopf束の障害を回避したと呼ばない。

### 5.1 非一様な低エネルギー診断

局所平坦frameで質量mの運動量と、そのN回boost像を比較すると、二つを合計した不変量は

```math
s_N=2m^2[1+\cosh(N\gamma)].
```

これはLorentz代数からの厳密式。`alpha' m²=10^-6,10^-12,10^-30` と仮に置いた対照では、`alpha' s_N>=1` になる最初のNは **4,8,20**。

この結果が示すのは、そうした反復像を含む寄与について、非零の種運動量を小さくしても、全Nで一様な `alpha' s_N << 1` を保証できないこと。
**実際に全ての像が衝突すること、全状態がその寄与を含むこと、全弦理論で発散すること、どのNで装置が壊れるかは計算していない。** mも装置の予測質量ではない。gamma=0では増大しない負例も検査する。

### 5.2 類似string模型の否定材料と、その限界

Horowitz–Polchinski [S1]、Berkooz et al. [S2] は時間依存orbifoldのprobe／散乱に強い逆反作用の問題を見いだす。これは「弦だから自動的に安全」の反例材料だが、heterotic Taub–NUTへ結論をそのまま移せない。

反対にCraps–Krishnan–Saurabh [S3] は、別のbosonic Milne模型の2→2 tree振幅で低張力極限に問題のUV発散が消える領域を示す。§5ではUV条件を `alpha'(p1-p3)²<=2` 等とし、残るIR発散と区別する。
従って「boostがあるなら全string振幅が必ず病的」も採用しない。full heterotic状態・相互作用・実時間境界規則への接続は残る。

## 6. 肯定材料として使っていた文献を厳しく読み直す

### 6.1 F-localなCTC円筒は、一般の安定した通信装置の証拠ではない

Fewster–Higuchi [Q1] の2/4次元の平坦な時間周期円筒におけるF-local場代数の構成は維持する。
一方、Fewster [Q2, Theorem 6.2, Corollary 6.3] は、**2次元・massive Klein–Gordon・コンパクト領域内で平坦計量から変形した指定クラス**で、genericなCTC円筒がF-quantum incompatibleとなることを証明する。genericはBaireの位相的意味であり、確率1という意味ではない。
これは全ての摂動や4次元massless NUTの定理ではなく、実際の装置のstressによる変形を解いた結果でもない。それでも、特殊な平坦模型の存在だけを頑健性の証拠に数えることはできない。

### 6.2 ワームホールの「通過できる」を「過去に届く」に置き換えない

Gao–Jafferis–Wall [W1] のdouble-traceで通過可能にする構成は、その構成では因果律違反に利用できないと明記する。
Maldacena–Milekhin–Popov [W2] の4次元構成も、外側時空で因果律違反を起こさないlong wormholeである。
これらは他のあらゆるワームホール方式のno-goではないが、そのまま過去通信の成功例として借用できない。

2026年のFreivogel–Fumagalli–Tomasevic [W3] は、同じ4次元系で、低エネルギーの荷電massless fermionがscalarより良く通過することを示す。
これは「scalarが失敗すれば全carrierも失敗」という一般化への注意材料でもある。今回の確認はabstractとversion historyまでで、透過曲線の再現は行っていない。時間方向を変えた実験や時間機械形成を証明した資料ではない。

### 6.3 P-CTCや非線形量子論は、残るが代価を隠せない

Ji–Lloyd–Wilde [P3] のnoisy P-CTCのretrocausal capacityは、その資源を仮定した有意義な定理である。しかし、その資源を自然界が供給するかは別。
本ノート§2.3のような操作依存の正規化・相関・制限によってno-goの仮定を外すことは数理的には可能なので、理論全体を間違いとはしない。
その代わり、単一の自由場の検出器公式だけで正当化せず、選択装置と失敗flagを含む全確率法則を導くことを要求する。

## 7. 今回閉じたクラスと、本当に残った課題

**新しく排除した構成クラス：** 操作非依存・線形・通常の自由な前向きフィードバックに閉じた過去通信装置。これは量子雑音の大小、spin、有限の符号化次元によらない操作論的制約である。
**維持する以前の棄却：** Taubから通常の局所場を地平面越しに延長する固定背景案のKRW障害。
**残る逃げ道：** 大域的な相関や操作依存の背景応答により単一二端子processへ還元できない構成、通常とは異なる確率法則／許容操作、完全な弦の実時間完成、今回と異なる時空・機構。

この残りを「自然界は不可能」と閉じたとはしない。特にNUT-onlyには、今回試した光の内部閉軌道による反証が使えないことまで分かった。

次の具体的な標的は、**同じfield/probe模型のコピー・NOT・固定送信を含めて背景／大域境界の応答を解き、核Kが本当に操作fごとにどう変わるか**である。
出てきた `K_f` を単に別々に正規化するだけでなく、制御flagの分布、局所状態の正値性、装置の前向き記憶、大域整合性を同時に検査する。
一つの実装が成功しても、任意に接続可能な通信路を実現したのか、制限付きの過去相関なのかを区別する。

10%を1%などへ機械的に更新する尤度は得ていない。新しい条件付き制約と既知定理の再確認を分け、主観的見積もりを数値予測へ変換しない。

## 8. 再現・公開

```bash
python src/symbolic/operational_feedback_consistency.py
python src/symbolic/taubnut_loophole_geometry.py
```

ローカルPython 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0で2本ともsuccess。
process行列とHamiltonianは厳密演算。径方向の根・boost診断は50/80桁比較、40桁以上一致。interval arithmeticによる誤差証明ではない。
既存code・assert・参照JSON・依存・CI・Leanは変更しない。新規2本は独立script。PR累積差分には前回の2本も残るため、既存選別器で対象と理由を記録する。
remoteの実際のhead・checkout・run・success/failureはPRコメントで記録し、ローカル成功から推定しない。

git cloneはこの実行環境でDNS失敗。リポジトリ全体のローカル実行はしていない。GitHub connectorで既存SHAを読んで変更を保存する。
既知のprocess定理と大域的な幾何の論証をLeanで形式証明したとはしない。

## 一次資料と確認範囲

- **[P1]** O. Oreshkov, F. Costa, C. Brukner, *Quantum correlations with no causal order*, Nature Communications 3, 1092 (2012). [arXiv:1105.4464](https://arxiv.org/abs/1105.4464)。本文のinstrument仮定、Appendix Cの(18)–(19)、PDF p.9を抽出本文で確認。
- **[P2]** T. Hoffreumon, O. Oreshkov, *The Multi-round Process Matrix*, Quantum 5, 384 (2021). [論文](https://quantum-journal.org/papers/q-2021-01-20-384/)。abstractとmulti-round／記憶の適用範囲を確認。全定理の再現なし。
- **[P3]** K. Ji, S. Lloyd, M. M. Wilde, *Retrocausal capacity of a quantum channel: Communicating through noisy closed timelike curves*, PRL 136, 230801 (2026). [2509.08965v3](https://arxiv.org/abs/2509.08965v3)。2026-06-13改訂、abstractと仮定資源を確認。capacity全体の再現なし。
- **[J]** C. V. Johnson, H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*. [hep-th/0405141v3](https://arxiv.org/abs/hep-th/0405141v3)。(72)–(73)、導入のprobe区別、結論のMisner挙動を確認。
- **[Q1]** C. J. Fewster, A. Higuchi, *Quantum Field Theory on Certain Non-Globally Hyperbolic Spacetimes*. [gr-qc/9508051](https://arxiv.org/abs/gr-qc/9508051)。abstractと既存ノートの対象確認。
- **[Q2]** C. J. Fewster, *Bisolutions to the Klein-Gordon Equation and Quantum Field Theory on 2-dimensional Cylinder Spacetimes*. [gr-qc/9804012](https://arxiv.org/abs/gr-qc/9804012)。Theorem 6.2／Cor. 6.3、massive・2D・genericの意味、§7の4Dへの留保を本文で確認。
- **[S1]** G. T. Horowitz, J. Polchinski, *Instability of Spacelike and Null Orbifold Singularities*. [hep-th/0206228](https://arxiv.org/abs/hep-th/0206228)。abstractで対象とprobe不安定性を確認。NUTへの定理移植なし。
- **[S2]** M. Berkooz et al., *Comments on Cosmological Singularities in String Theory*. [hep-th/0212215](https://arxiv.org/abs/hep-th/0212215)。§4の逆反作用、§5の特定の振幅相殺への留保を確認。full Milne振幅の再導出なし。
- **[S3]** B. Craps, C. Krishnan, A. Saurabh, *Low Tension Strings on a Cosmological Singularity*. [1405.3935](https://arxiv.org/abs/1405.3935)。導入・§5・脚注15のUV/IR分類と低張力の限定を本文で確認。
- **[W1]** P. Gao, D. L. Jafferis, A. C. Wall, *Traversable Wormholes via a Double Trace Deformation*. [1608.05687v3](https://arxiv.org/abs/1608.05687v3)。abstractの因果性の限定を確認。
- **[W2]** J. Maldacena, A. Milekhin, F. Popov, *Traversable wormholes in four dimensions*. [1807.04726v3](https://arxiv.org/abs/1807.04726v3)。abstractのlong wormhole／因果性を確認。
- **[W3]** B. Freivogel, A. Fumagalli, M. Tomasevic, *How traversable is a traversable wormhole?* [2606.12528v1](https://arxiv.org/abs/2606.12528v1)。取得した公式ページは2026-06-10のv1。abstract・version historyを確認。別模型のcarrier依存の注意例。

PDFは抽出本文で該当箇所を確認した。web screenshotは取得エラーで、今回ページ画像による確認はできなかった。図表から新規の値を読み取ってはいない。
検索は上の逃げ道に絞ったものであり、全時空・全理論・全論文の網羅や、未発見の反例の不存在を保証しない。
