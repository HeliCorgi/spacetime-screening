# 選んだ情報を過去へ送れるか：判定条件の改訂とTaub–NUT量子場の障害

**2026-09-23。継続基点：`fd29df1be41391ee94d5c1a2a1458c60423ad545`（PR #8マージ後）。**

**結論：物理的な過去通信は実証していない。今回、既存のスカラー近似を通常の局所量子場として地平面まで正則に使う経路に、状態調整では解消しない障害を特定した。完全な弦理論や時間遡行一般の禁止ではない。**

本ノートが時間遡行側の最新の再開点。[前回の継続](heterotic-taubnut-operational-continuation.md)と[6条件監査](heterotic-taubnut-six-gate-audit.md)の計算は保存するが、「6条件を順番に全部完成する」研究順序を置き換える。NPQT側には戻らない。

区分：KRWは **PUBLISHED RESULT**。計量・作用の変換は **REPRODUCED / CHECKED HERE**。指定した延長への適用は **APPLICATION CANDIDATE WITH EXPLICIT HYPOTHESES**。一般の物理的時間遡行は **OPEN IN THIS WORK**。新規性・優先権は主張しない。

## 1. 何が分かれば「可能」と言えるか

必要なのは一つの具体的な物理的プロトコルである。送信者が異なる二つの操作 `b=0,1` を選べて、受信者がその操作より前の、**別のイベントB**で区別できる記録Yを得ることを調べる。

```math
D_B=\frac12\sum_y|P(y_B\mid\mathrm{do}(b=0))-P(y_B\mid\mathrm{do}(b=1))|>0.
```

連続結果なら和を積分に置き換える。等確率の二値メッセージに対する最適な古典的判別成功率は `(1+D_B)/2`。これは一回の区別可能性であり、独立な反復・resetを未構成のまま漸近通信容量とも呼ばない。

| 必須の確認 | 実際に固定すべきもの |
|---|---|
| 物理的に許された操作と予測規則 | 背景、初期の資源、送信操作、検出器、接続・境界の規則、各設定の正規化された確率 |
| 本当に過去の受信 | 実験室の時計に沿う有限な通常の経過 `B≪_lab A` と、その同じBでの記録。周期座標の別表記や別実験のコピーではない |
| 正の制御可能な応答 | 受信時に利用できる全結果を含む `D_B>0`。近似誤差・雑音・逆反作用を入れてもその正値を保証できること |

同じ準備とは、同じ資源・法則・設定以外の外部制御を比較するという意味である。**受信結果そのもの、あるいはBを含む全過去履歴を設定間で同一と仮定して、結論を先取りしない。** 大域的自己無撞着性を採用する場合、少なくとも二つの符号化操作が同じ規則の下で許容される必要がある。想像できる全ての局所操作や全ての初期状態で通信できる必要はない。

### 1.1 旧6条件から外す／弱めるもの

- **因果構造を新たに変えること：不要。** 既存CTCが物理的に利用可能なら十分。time machineの動的形成は別の問題。
- **全BRST cohomology・全スペクトルの完全な列挙：不要。** 弦の経路なら、使う操作・状態・観測量が物理的空間に属し、内積と必要な振幅が整合することは必要だが、全状態を分類する必要はない。別理論にBRSTを普遍条件として課さない。
- **同じ純粋状態が無傷で維持されること：不要。** 混合状態・損失・有限雑音があっても記録を区別できればよい。単色散乱固有状態の素朴なL²正常化も普遍条件ではない。
- **postselectionを種類によらず全禁止：修正。** 受信時に利用できない未来の成功フラグでデータを後から選ぶだけでは送信にならない。一方、受信時のherald／erasureを含む物理的手順や、基礎法則から本当に導かれるfinal-state規則は、その規則自体の実現性を検証する。結論を仮定して排除しない。

有限精度で得た二つの分布のTV誤差が `eps0,eps1` 以下なら三角不等式より

```math
D_B^{\rm true}\ge D_B^{\rm calc}-\epsilon_0-\epsilon_1.
```

従って必要なのは正の誤差余裕であって、相互作用が厳密に0であることではない。逆に、不明な相関関数を0と置いて「不可能」ともしない。

## 2. 今回の主結果：スカラー方程式からKRWへ直接接続する

### 2.1 入力と、全弦理論との区別

Johnson–Svendsen [S1, (72),(73),(79)] の計量とdilatonを用いる。

```math
p=x^2-1,\quad D=(x+\delta)^2-\frac{4p}{k+2},\quad K=(k-2)\alpha'>0,
```
```math
g=K\left[\frac{dx^2}{p}-\frac pD(dt-\lambda\cos\theta\,d\phi)^2+d\Omega_2^2\right],
\quad\Phi=\Phi_0-\frac14\log D,\quad t\sim t+4\pi\lambda.
```

前回と同じ `k=8, delta=sqrt(8/5), lambda=sqrt(2/5)`、Hopf束によるコンパクトな `S^3` 切片、Taubから第一NUTへ向かう**一つのHausdorffなoutgoing延長**を固定する。ここで量子化するのは、リポジトリで診断に使ってきた**中性・実・質量ゼロ・局所スカラー場**

```math
S_\varphi=-\frac12\int\sqrt{|g|}\,e^{-2\Phi}g^{ab}\partial_a\varphi\partial_b\varphi,
\quad P_\Phi=\Box_g-2\nabla^a\Phi\nabla_a.
```

この作用が全heterotic物理スペクトルと相互作用を厳密に表すとは仮定しない。

### 2.2 四次元の正確な変換

補助計量 `g_E=e^{-2Phi}g` を定義する。これはスカラー作用の書換えであり、未知の全string compactificationをEinstein frameまで構成したという意味ではない。四次元では

```math
\sqrt{|g_E|}=e^{-4\Phi}\sqrt{|g|},\qquad
\sqrt{|g_E|}g_E^{ab}=e^{-2\Phi}\sqrt{|g|}g^{ab},
\qquad \Box_{g_E}=e^{2\Phi}P_\Phi.
```

従って、上のスカラー模型は `(M,g_E)` 上の**通常の最小結合・質量ゼロKlein–Gordon場と作用ごと同じ**である。未知のpotentialへのKRW定理の拡張を使わずに済む。変換は `D>0` で滑らかかつ可逆、光円錐・因果曲線・domain of dependenceを変えない。定数 `Phi0=0` を計算の規約にすれば `g_E=sqrt(D)g`。

この点のDは

```math
D=\frac35(x+\sqrt{10})(x+\sqrt{10}/3)>0\qquad(x>-1).
```

二つの零点はともに `x<-1`。問題の未来地平面近傍に、conformal factorの零・極はない。次元を変えて同じ式を適用する負例もコードで排除する。

### 2.3 正則チャートで地平面を検査

`r_*'=sqrt(D)/p`, `q=t-r_*`, `xi=dq-lambda cos(theta)dphi`, `d=1+delta` とすると

```math
g_E=K\left[-\frac p{\sqrt D}\xi^2-2\xi\,dx+\sqrt D\,d\Omega_2^2\right].
```

`H={x=1}` で、極座標の軸を除くチャートでは

```math
\det g_E\big|_H=-K^4d^2\sin^2\theta\ne0,\qquad
(g_E)^{xx}=\frac p{K\sqrt D},\qquad
\nabla_{g_E}x\big|_H=-\frac1K\partial_q.
```

軸の `sin(theta)=0` はDirac-monopoleの北・南チャートで扱う座標の問題で、時空の退化ではない。地平面の誘導計量は `Kd dOmega_2²`、kernelは `n=partial_q`。さらに

```math
\nabla_n n\big|_H=-\frac1d n.
```

従って生成線はnull geodesicの再パラメータ化である。qも周期 `T=4pi lambda` を持つので各生成線はHopf fibreとして閉じる。アフィン接ベクトルは周期的である必要はなく、`dq/daffine ∝ exp(q/d)`。一周の接ベクトル倍率は、この規約で

```math
e^{T/d}=33.4162774950530781786754384976\ldots.
```

これは帰還するnull線の幾何の診断であり、通信率や弦の散乱確率ではない。

### 2.4 大域的仮定を確認する：ここは数値assertではない

`M=(-1,1+epsilon)×S^3`（十分小さい正のepsilon）を上のq束チャートで延長した時空とし、`Sigma={x=0}` を選ぶ。

Taub内では元の計量が、時間方向 `-K dx²/(1-x²)` と正定値のコンパクトな空間切片に分かれる。任意の閉じたx区間上で空間計量・lapseは滑らかで一様に非退化である。従って因果曲線が内点のxに留まったままinextendibleになることはなく、Taub内の各x切片はCauchy面になる。

未来向きの横断方向も確認できる。Hでfuture nullなnに対して `g_E(v,n)=-K v^x<=0` だから `v^x>=0`。Taubから出る同じHを未来向きに逆横断してSigmaへ戻ることはない。接する因果曲線についても、`A=xi(v)>0` なら因果条件が `v^x>=-p A/(2sqrt(D))+sqrt(D)|v_Omega|^2/(2A)` を与え、Hのnull障壁性を保つ（`A=0` のもう一つのfuture null方向は正のpartial_x）。これによりSigmaはこの選択したMでもachronal・edgelessであり、`0<x<1` はその未来domain of dependenceにある。

一方、Hには過去へ何周してもSigmaに達しないnull生成線がある。`x>1` にも、固定x・固定角度で `g_E(partial_q,partial_q)<0` の閉じたtimelike fibreがあり、これを繰り返すpast-inextendible曲線はSigmaを避ける。従ってこのMにおいて

```math
H^+(\Sigma)=\{x=1\}\simeq S^3.
```

H自身をcompact setに選べば、全てのpast null generatorはそこに留まる。KRW [S2, §2] の**compactly generated**の定義を満たす。また各生成線が過去へ繰り返し同じfibreを巡るので、その全点がpast terminal accumulation pointになる。したがってKRWのbase setはこの模型では **B=H全体**。

これは任意のNUT延長・非周期時間・異なるorbifold prescriptionについての証明ではない。ここで明記した滑らかなコンパクトHopf延長についての幾何学的論証である。Pythonは局所的な計量恒等式を検算するのであって、compactnessやKRWの定理を形式証明していない。

### 2.5 KRWを適用した、限定された否定結果

KRW [S2, §5, Theorems 1/2] は、compactly generated Cauchy horizonのbase pointsで、初期の通常の場代数のF-localな延長と、初期Hadamard二点関数の正則なHadamard延長に障害を与える。特に後者の局所Hadamard parametrixとの差は有界ですらない。

本模型では §2.2で対象のKG作用へ正確に写り、§2.4で幾何条件を確認したので、次の結論になる。

> **指定したコンパクトTaub→NUT延長の上で、この実・質量ゼロスカラーを通常の局所量子場として扱い、初期Taub領域でHadamardな状態を選ぶ限り、未来地平面全体まで局所Hadamard性を保つ延長は存在しない。**

Hadamard性は通常の量子場の短距離特異性を制御する条件で、繰り込みされた局所量を定義する基盤である。これは単なる単色モードのL²発散でも、一つの準備だけの失敗でもない。

ただし、**特定の観測者が必ず無限大のエネルギーを測る、任意の有限幅検出器が発散する、弦の曲率が必ず発散する、通信容量が0である、とはこの適用だけから言わない。** 特定経路で応力の極限が有限でも、地平面点での標準的なpoint-splittingの定義には障害があるという範囲である。未知の全backreactionを解いたわけではない。

## 3. 前回の「正則source」はなぜ量子問題を解かないか

前回の `J_b` は、古典的な平均場 `v_b` を未来地平面で正則にする。線形なc-number sourceにより場を `varphi -> varphi+v_b` とずらすと、平均を引いた**connected二点関数は変わらない**。

```math
C_b(x,x')=\langle(\varphi-\langle\varphi\rangle)_x
(\varphi-\langle\varphi\rangle)_{x'}\rangle_b=C_0(x,x').
```

零平均からなら非connectedな二点関数は `W_b=W_0+v_b(x)v_b(x')`。正則なvによるsmooth項は、KRWの非Hadamard特異性を消せない。従って **B_J=0という平均場の調整だけでは、健全な量子通信媒体を得ていない**。有限個のsmooth modeの励起・混合によるsmoothな補正についても同じである。

ここで排除したのは「古典的source調整を、そのまま量子場全体の健全性と解釈すること」。物理的な送信装置を入れた非線形応答、弦の非局所性、異なる背景への動的変化は、この議論の対象外である。

## 4. 応答と雑音から、受信確率へ

線形Gaussianの**条件付き検出模型**では、二設定の受信平均を `-a,+a`、共通分散を有限の `V>0` とすれば

```math
P(y|b)=\frac{1}{\sqrt{2\pi V}}\exp\left[-\frac{(y-(-1)^{b+1}a)^2}{2V}\right],
\quad D_B=\operatorname{erf}\left(\frac{|a|}{\sqrt{2V}}\right).
```

aは**局在した物理的なsourceから検出器への応答**で決め、Vはその物理状態の二点関数と検出器のsmearingで決める。通常の順序付けされた線形場ではretarded propagatorの畳込みがaを、対称二点関数がVを決める [S3]。Feynman/Wightman相関が非零なだけではaを得たことにならない。CTC時空ではさらに大域的予測規則が要る。

コードでは密度の独立した積分とerf式を50/80桁で検算した。

| あくまで検出模型の入力 | D_B | 判別成功率 |
|---|---:|---:|
| a=0, V=1 | 0 | 0.5 |
| a=1, V=1 | 0.682689492137… | 0.841344746069… |
| a=1, V=4 | 0.382924922548… | 0.691462461274… |

雑音のある正例を残すことで「純粋状態が壊れたから通信不能」という誤判定を防ぐ。**この表のa,VをTaub–NUTについて算出したわけではなく、過去への送信成功率の表ではない。** 未計算のTaub–NUT応答はコード内でも `None` とし、0で代用しない。

## 5. 2026年のretrocausal capacity論文は「物理的実現」の答えか

Ji–Lloyd–Wilde [S4] は、**noisy postselected CTCを資源として仮定した場合**の一回・漸近の通信能力を特徴付ける研究である。重要な情報理論的結果だが、Taub–NUTがその資源を実装することや、通常のpostselectionで過去へ送信できることの証明ではない。ここでは最適化された容量定理の再現を主張しない。

### 5.1 成功確率が設定と独立でも、未来の選別は信号ではない

時刻が通常に順序付けされた3-qubit対照系を**全結果込み**で計算した。初期資源は受信側Bと将来へ運ぶCの

```math
\rho_{BC}=v|\Phi^+\rangle\langle\Phi^+|+(1-v)I_4/4,\quad 0\le v\le1.
```

Bは早い時刻にZを測ってyを保存。遅い時刻に送信者がMへbit bを用意し、C,MのBell測定をする。未来の結果hを全て残すと

```math
P(y_B|\mathrm{do}(b))=1/2,\qquad D_B^{\rm unconditional}=0.
```

ところが未来の `h=Phi+` だけを残すと

```math
P(h=\Phi^+|b)=1/4,\qquad
P(y|b,h=\Phi^+)=\frac{1+v(-1)^{y+b}}2,\qquad D_B^{\rm selected}=v.
```

v=1なら、後から選んだデータには完全な「過去のbitとの一致」が現れる。それでも早い受信者の全分布は不変である。**herald成功率がbと独立であることだけでは不十分**。全Bell分岐の正規化・正値性・受信marginalを厳密な行列計算で検算した。

この例は仮想的P-CTCの基礎法則を反証しない。基礎法則が本当に一つのfinal-stateを強制するなら、通常の測定選別とは異なる。その資源を弦理論から導く必要がある。同様に、Deutsch fixed pointを満たすだけで実際の時間遡行を認定しない [S5]。

## 6. 判定と次の課題

| 問い | 今回の結論 |
|---|---|
| 実際に選んだ情報を過去へ送れたか | **いいえ。この研究では未実証** |
| 全ての物理理論で不可能と証明したか | **いいえ** |
| 前回の正則スカラーmodeを通常の量子場のまま地平面全体へ通す案 | **初期Hadamard・指定コンパクト延長・局所自由場という仮定の下では不可** |
| full string theoryが障害を回避するか | **未判定。標準スカラーの仮定をどこで置き換えるかが必要** |
| 回避に成功したと仮定すれば、何を計算するか | **許容された二つの局所符号化から、時計で指定した過去受信記録の完全な確率分布を求める** |

次はBRST状態の数を増やすだけの探索や、調整sourceをさらに細かく掃引する計算を優先しない。まず **KRWの局所自由場仮定を実際のheterotic観測量がどこで満たさなくなるか** を特定する。具体的には、必要な一つの物理的source・検出observableについて、ゲージ不変の実時間応答と二点pairingを、global prescriptionを固定して構成する。BRST／GSOのmembershipはその操作に必要な範囲で同時に検証する。

もしその構成が通常の局所KG場へのHadamardな延長を要求するなら、この経路は本ノートの段階で止まる。非局所・高エネルギー・新しい背景によってその仮定を変更するなら、変更後の応答・雑音・誤差を明示して `D_B>0` を検査する。「弦だから回避する」は証明にならない。逆に、本ノートから「弦でも必ず不可」とはしない。

## 7. 再現性・適用範囲

```bash
python src/symbolic/heterotic_taubnut_krw_bridge.py
python src/symbolic/operational_past_signal_probability.py
```

ローカルPython 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0で2本ともsuccess。幾何とBell系は厳密代数。Gaussian積分は50/80桁を比較し40桁の一致をassertする。確率0の負例だけでなく、有限雑音の正例、future-postselectionの偽陽性、四次元以外への誤移植を検査する。

既存計算・依存・共有module・参照データ・workflow・Leanは変更しない。独立2本と文書の通常PRとして選別器を使う。remote CIのSHA・run・対象・結果はPRの完了コメントに記録する。**数学の定理・大域幾何の論証・コードのassertを区別する。LeanでKRWやLorentz幾何を証明したとは報告しない。**

## 一次資料・確認範囲

- **[S1]** C. V. Johnson, H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, Phys. Rev. D 70, 126011 (2004), [hep-th/0405141](https://arxiv.org/abs/hep-th/0405141)。§1の周期とS³、§3.6–3.7、(72),(73),(79),(82)をPDF抽出テキストで確認。
- **[S2]** B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, Commun. Math. Phys. 183, 533–556 (1997), [gr-qc/9603012v2](https://arxiv.org/abs/gr-qc/9603012v2)。PDF pp.7–9の定義、pp.27–31のTheorems 1/2/2′と適用限界を確認。定理は既知であり今回の新定理ではない。
- **[S3]** M. Cliche, A. Kempf, *The relativistic quantum channel of communication through field quanta*, [0908.3144](https://arxiv.org/abs/0908.3144)；E. Tjoa, K. Gallock-Yoshimura, *Channel capacity of relativistic quantum communication with rapid interaction*, [2202.12301](https://arxiv.org/abs/2202.12301)。検出器・雑音・通信と相関の区別。後者のglobal hyperbolicityをNUTへ仮に移さない。Gaussian式は本ノートの明記した検出模型で直接導出したもので、両論文の最適容量公式の再現ではない。
- **[S4]** K. Ji, S. Lloyd, M. M. Wilde, *Retrocausal Capacity of a Quantum Channel: Communicating through Noisy Closed Timelike Curves*, Phys. Rev. Lett. 136, 230801 (2026), [2509.08965v3](https://arxiv.org/abs/2509.08965v3), [journal](https://doi.org/10.1103/znyd-npk5)。2026-06-11出版、arXiv v3は2026-06-13。abstractとPDF p.1のP-CTC資源仮定を確認。全容量定理を実装したとはしない。
- **[S5]** J. Tolksdorf, R. Verch, *Quantum physics, fields and closed timelike curves: The D-CTC condition in quantum field theory*, [1609.01496](https://arxiv.org/abs/1609.01496)。abstractの、CTCがない場合にも条件を任意精度で満たせるという適用限界を確認。

検索はTaub–NUT、Hadamard、KRW、operational signalling、retrocausal capacityの限定検索。物理的なTaub–NUT過去通信の完成したプロトコルは今回確認した資料からは得られず、これは文献全体の不存在証明ではない。S1/S2/S4のPDF screenshotを試みたがcache-missで画像取得に失敗した。上記確認は取得できた本文テキストに基づくもので、ページ画像の目視確認済みとはしない。
