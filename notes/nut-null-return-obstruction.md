# NUT内部の自己帰還null測地線：固定背景スカラー模型のno-go

**2026-09-23 / 模型内の判定：FAIL。**  
読取基点：main `961928014858e8082a93d682144bd03831e4a280`（PR #14マージ後）。

**今回閉じる対象は、既存の周期的heterotic Taub–NUT計量上で、通常の局所交換関係または局所Hadamard性を保つ大域的な線形スカラー場を使う通信案である。**
Taubでの準備、密閉した環境、独立した受信probe、特定の戻りunitaryを仮定しなくても、この自由場の基礎が成立しない。
**完全なheterotic string、相互作用・計量変更を含むあらゆる模型、自然界一般を否定する定理ではない。**

## 0. 今回の結論と、前の結果との違い

| 問い | 結果 |
|---|---|
| 第一NUT領域全体に、通常の局所Hadamardスカラー二点関数を置けるか | **置けない。** 分布的な波動方程式と局所の特異性条件が、内部の自己帰還null測地線で矛盾する |
| Hadamard性だけ捨て、局所交換関係を保つ場代数にできるか | **分布的な交換子を持つ通常のF-local自由場としても不可**。同じ伝播の矛盾が交換子にも生じる |
| 外部領域 `x>2` へ放射する量子環境なら回避できるか | **同じ自由場をその領域全体に完成する案も不可**。今回の証人となる光の経路は全て `x>12` にあり、境界 `x=2` も地平面も通らない |
| 測定記録による回復、浴との初期相関、非Gaussian状態で回避できるか | それらが**同じ大域的自由場と局所条件を保持する限り不可**。密度行列の固定点・有限エネルギー・Markov性を使わない |
| 放射ODEの解やCTCの幾何も消えたか | **消えていない**。古典解・幾何と、健全な大域的量子場の存在は別 |

これは既知の特異性伝播の方法 [K, M] を、今回具体的に構成・検算したNUT内部の経路に適用する解析的証明である。
基本定理の新発見・優先権は主張しない。数値探索だけではなく、整数による外向き丸め区間評価で経路の存在を保証する。
独立査読・Leanでの形式検証は実施していない。

前回の「滑らかに周期的なnull測地線は存在しない」は維持する。
**それは、始点と終点が同じでも接ベクトルが違うnull測地線区間（self-intersecting null geodesic）を除外しない。**
今回使うのは後者であり、前の径方向の極大だけの議論を破ってはいない。

## 1. 対象模型を固定する

[J, (72), (73), (79)] と既存repoの値を使用する。第一NUT領域を `N=(1,infinity)×S³`、外部環境候補を `E={x>2}⊂N` とする。

```math
p=x^2-1,\qquad D=(x+\delta)^2-a p,
\qquad k=8,\quad a=\frac4{k+2}=\frac25,
```
```math
\lambda=\sqrt{\frac25},\qquad \delta=\sqrt{\frac85}=2\lambda,
\qquad K=(k-2)\alpha'>0,\qquad T=4\pi\lambda.
```

北極側の正則な束座標を `tau=t_N=t-lambda phi` と書く。

```math
g=K\left[\frac{dx^2}{p}+d\theta^2+\sin^2\theta\,d\phi^2
-\frac pD\bigl(d\tau+\lambda(1-\cos\theta)d\phi\bigr)^2\right],
\qquad \tau\sim\tau+T.
```

`D>0` on N。北極chartの接続は[J]の `2 A_phi=1-cos(theta)` であり、対称なt座標の巻き数を独立に同一視してはいけない。

診断用の中性実スカラーは

```math
S_\varphi=-\frac12\int\sqrt{-g}\,e^{-2\Phi}g^{ab}\partial_a\varphi\partial_b\varphi,
\quad \Phi=-\frac14\log D,
\quad g_E=\sqrt D\,g,
\quad P=\Box_{g_E}.
```

`g_E` はNで滑らかな正のconformal変換。null bicharacteristicの像はgと同じである。
仮定は、E（従ってN）上に定義された分布 `W∈D'(E×E)` が両変数でPの解で、各点の十分小さいglobally hyperbolicな近傍で通常のHadamard形を持つこと。
別証明では、分布的交換子Cが同じ方程式を満たし、各小近傍で通常のPauli–Jordan交換子と一致するというF-local性を仮定する。

**全Eがglobally hyperbolicだとは仮定しない。** 用いる伝播定理は微局所的なものであり、全体のCauchy面を要求しない。
Hadamard性の通常の特徴付けは小さい近傍にのみ適用する。
任意の浴の状態・境界条件を選んでも、この模型の完成ならこれらの条件を満たさなければならない。

## 2. 全Hamilton方程式を満たすnull測地線族

Kをaffine parameterの定数スケールへ吸収する。座標は `(tau,x,theta,phi)`、共役運動量は `(p_tau,p_x,p_theta,p_phi)`。

```math
2H=p p_x^2+p_\theta^2+
\frac{[p_\phi-\lambda(1-\cos\theta)p_\tau]^2}{\sin^2\theta}
-\frac Dp p_\tau^2.
```

任意の `j>1` に対して

```math
p_\tau=-1,\quad p_\phi=j-\lambda,\quad
\cos\theta=\frac\lambda j,\quad p_\theta=0
```

を取る。ここでjは**Killingエネルギーで規格化した測地線の角運動量**であり、量子場の整数modeラベルや弦の表現ラベルではない。
局所Hadamard条件は全てのnull方向を含むため、特定の量子modeを選んでこのcotangent方向を消すことはできない。

Hamilton方程式から

```math
\dot\phi=j,\qquad \dot\theta=0,\qquad \dot p_\theta=0,
\qquad \dot\tau=\frac{(x+\delta)^2}{x^2-1}-\lambda j,
```
```math
\dot x^2=(x+\delta)^2-j^2(x^2-1),\qquad
\ddot x=\delta-(j^2-1)x.
```

点を曲げる外力や反射鏡はない。径方向の自然な極大を通る滑らかな自由null測地線である。
`p_tau=-1` なので、timelike Killingベクトル `partial_tau` に対して未来向きの向きを一貫して選べる。

`c=j²-1`, `A_j=sqrt[(c+1)(c+delta²)]` と置くと、径方向の厳密解は

```math
x_j(\sigma)=\frac{\delta+A_j\cos(\sqrt c\,\sigma)}{c}.
```

中央 `sigma=0` が径方向の極大である。区間を

```math
-L_j\le\sigma\le L_j,\qquad L_j=\frac{3\pi}{j}
```

と取れば、`x(-L)=x(L)`、`Delta phi=6pi`、角位置は一致する。
残る束の閉合条件は

```math
F(j)=2\int_0^{L_j}\left[\frac{(x_j(\sigma)+\delta)^2}{x_j(\sigma)^2-1}-\lambda j\right]d\sigma-T=0.
```

## 3. 浮動小数の根ではなく、区間保証による存在

コード：[nut_null_return_certificate.py](../src/symbolic/nut_null_return_certificate.py)。標準ライブラリのみ使用。

`j∈[51/50,41/40]=[1.02,1.025]` を取る。以下を全区間について外向きに評価する。

```text
x_j(L_j) ∈ [12.328071013872, 22.455466798657]
x_j(0)   ∈ [50.791263131431, 63.905859968172]
0 < sqrt(c) L_j < pi
```

したがって全ての候補区間は `x>12>2` にあり、係数は滑らかで、Fはjの連続関数である。
`0<=sigma<=L_j` でxは単調減少し、

```math
\frac d{dx}\frac{(x+\delta)^2}{x^2-1}
=-\frac{2(x+\delta)(\delta x+1)}{(x^2-1)^2}<0
```

なので被積分関数は単調増加する。従って左・右端点の矩形和が厳密な積分下界・上界になる。
1024分割の結果は

```text
F(1.02)  ∈ [-0.293256783220, -0.291827106638]
F(1.025) ∈ [ 0.096018060361,  0.099047367761]
```

**中間値の定理により、厳密な根 `j*∈(1.02,1.025)` が存在する。** 一意性は不要であり、証明していない。

区間評価の構成：分母 `10^80` の整数端点、四則演算の外向き丸め、整数平方根、Machinの公式 `pi=16 atan(1/5)-4 atan(1/239)` の交代級数剰余、cosのTaylor剰余。
求積ライブラリや経験的な精度一致に存在証明を依存させない。
四則演算は別の厳密Fraction演算との比較を含み、分母が0を含む区間の拒否も検査する。
256分割でも両端の符号を保証し、1024分割で再確認する。
プログラム自体の形式検証ではなく、全演算規則と剰余の根拠を明示した再現可能な計算機援用証明である。

### 3.1 別の高精度検算

コード：[nut_null_return_geometry.py](../src/symbolic/nut_null_return_geometry.py)。SymPyで実際の四次元逆計量・Hamilton方程式・円錐角の運動量方程式・radial解を検算する。
独立のmpmath根探索と求積を50/80桁で実行した結果：

```text
j*       = 1.02392055766650680185878582575799091878528607...
x_return = 14.20651030656226005840921311205496551765...
x_max    = 53.28138841256275840874617043076082363296...
theta    = 0.90500674512061998895855019745...
p_x(start/end) = +/-0.02673063924903720482771900876635221989...
Delta tau/T = 1 ; Delta phi/(2pi) = 3
```

これらは無次元座標・規格化した測地線量で、通信成功率ではない。
実際の接ベクトルを計量に代入し、null性・Killingエネルギー・径方向加速度を区間上の複数点で照合する。
解析式が全区間を保証し、点での検査だけから外挿しない。

### 3.2 束の同一視と、同じ接ベクトルではないこと

北極chartのHopf座標を

```math
z_1=\cos(\theta/2)e^{i\tau/(2\lambda)},\qquad
z_2=\sin(\theta/2)e^{i(\tau/(2\lambda)+\phi)}
```

と書くと、`Delta tau=T`, `Delta phi=6pi` により `(z_1,z_2)` が厳密に同じ点へ戻る。
これは全NをR時間の被覆に置き換えた構成ではない。
対称座標 `t=tau+lambda phi` の増分は `5T/2` であり、tとphiの周期を独立に適用すると誤判定する。
コードはこの符号に敏感な対照も検査する。

共通の北極chartで、端点の共変運動量は正のbについて

```math
\kappa_0=(-1,b,0,j_* -\lambda),\qquad
\kappa_1=(-1,-b,0,j_* -\lambda).
```

`b>0` は `0<sqrt(c)L<pi` から従う。よって両者は一致せず、比例すらしない。
**同じ時空事象に異なるnull方向で再来する一つの滑らかな測地線区間**である。
端点を滑らかな周期軌道として継ぎ足すことはできず、前回の「周期的null軌道不存在」と両立する。

## 4. 量子場の障害：自己帰還点のwavefront矛盾

ここが物理模型を棄却する部分である。既知の原理を二つだけ使う。

**局所Hadamard形。** 十分小さいglobally hyperbolic近傍Uで、二点関数の対角 `P=P'` にあるwavefrontは

```math
(P,\kappa;P,-\kappa)
```

という対応だけを許す（Wでは片方の時間向き、交換子では両向き）。
異なる二つのnull covectorを同じ点の二変数へ勝手に組み合わせることは許されない。[M, Theorem 9] をここではUにのみ使う。

**特異性の伝播。** 分布uが滑らかな係数の実principal-typeの方程式 `P_x u=0` を満たすと、そのwavefrontは第一変数のnull bicharacteristicに沿って伝播する。[M, Theorem 6; K, §3]。
第二変数とそのcovectorは固定する。必要な第一covectorは常に非零であり、積多様体上の第一変数作用素の退化部分を通らない。
全Eのglobal hyperbolicityは使わない。causticを通っても、このcotangent上の伝播は止まらない。

仮にE全体の局所Hadamard二点関数Wが存在するとする。
自己帰還点Pで許容される向きにkappa_0（必要なら両covectorの符号を反転）を取れば

```math
(P,\kappa_0;P,-\kappa_0)\in\operatorname{WF}(W).
```

第一変数を今回のnull測地線に沿って伝播すると、同じPへ戻って

```math
(P,\kappa_1;P,-\kappa_0)\in\operatorname{WF}(W)
```

でなければならない。しかし `kappa_1 != kappa_0` なので、これはUにおける局所Hadamardの対角条件に反する。**矛盾。**

> **模型内no-go：指定した固定背景のE上には、各点で通常の局所Hadamard性を持つ大域的スカラーbisolutionは存在しない。従ってN全体にも存在しない。**

この結論に正値性、Gaussian性、定常性、trace-class性、bathの有限性、入力と環境の無相関性、通信路の自由な接続可能性は不要である。
波動方程式を満たす分布という弱い段階で既に矛盾している。
帰還の証人がEの内部のコンパクト領域に全て入っているため、無限遠やx=2での境界条件では途中の特異性伝播を止められない。

### 4.1 Hadamard性を外しても、通常の局所交換関係では救えない

分布的な交換子 `C(f,h)=omega([phi(f),phi(h)])/i` が存在し、自由場方程式を満たし、U内では通常の局所Pauli–Jordan交換子に等しいとする。
局所交換子のwavefrontも対角で `(P,kappa;P,-kappa)` を含み、異なるcovector同士の対角pairを含まない。
同じ第一変数の伝播を使うと矛盾する。局所交換子へのsmoothな修正でもwavefrontは変わらない。
従って、**分布的交換子を持つF-localな自由場代数という完成も不可能**である。

[K, §6, printed p.31] は、まさに「自己交差するが周期的には閉じていないnull測地線」への禁止議論の一般化を明記している。
今回の追加は、以前は閉軌道不存在だけを調べていたNUT外部に、その仮定を満たす具体的な自己帰還区間を構成したことである。
同じ向きの完全なrefocusingを許す特殊例への例外とは違い、ここでは端点のcotangent方向が異なることを直接確認した。

### 4.2 何が禁止され、何は禁止されないか

前回の外向き応答 `Y_n` は古典的なODEの正しい解として残る。
しかし `Im Y_n>0` を持つことは、その応答をE全体のF-local/Hadamardな量子環境へ完成できることを意味しない。
今回、**同じ固定背景自由場を浴とする大域完成は不可**と判定する。

場と任意の補助系を合わせた状態があっても、場の代数へ制限すれば場の二点分布が得られる。
それが同じ自由波動方程式と局所条件を保つなら、環境との相関や測定記録による回復では上の矛盾を回避できない。
場が自由な外部を残す装置（例えば操作がx<=2に局在するもの）でも、経路は外部だけを通るので同様である。

これは、全ての検出器の確率が0になるという計算ではない。
**確率を定義するための大域的媒体が模型内で存在しない**という模型の棄却であり、未定義の確率を0と置くものではない。
普通の小領域だけでの量子通信・古典波・幾何学的CTCを否定していない。

以下は前提を変更した別問題であり、本結論に含めない：

- 相互作用や反作用で、経路を含む領域のprincipal symbol／計量／位相／境界を変更する。
- NUT全体やE全体を量子場の定義域とせず、自己帰還の証人を含まない別の領域へ切り詰める。
- 自由場の分布方程式やF-local性、局所Hadamard性そのものを捨てる非局所・全弦的な理論。

smoothな質量項・曲率結合等の低階項だけを変えてもprincipal bicharacteristicと伝播の議論は変わらない。
ただし、任意の非局所的な散逸核や完全なheterotic相互作用までこの一文で覆ったとはしない。

## 5. 最終採否

**同じ周期的NUT背景を保ち、通常の大域的線形スカラー場を送受信・浴の媒体とする現行案は、模型内FAILとして閉じる。**
ここでの「閉じる」はmainやPRを自動マージする操作ではなく、研究上の採否である。
さらに別の減衰率、浴状態、初期相関、コピー／NOT回路を選び直すだけでは、この障害を解消しない。

この結論は、以前のTaubから地平面を渡すno-goをNUT-onlyへ転用したものではない。
証人の数値は `x=14.206...` から `x=53.281...` までであり、存在の区間証明では全経路に対する厳密な `12<x<64` を用いる。地平面へ近づく極限も、無限周回の極限も取っていない。
量子重力でCTCの幾何が消えるかは計算していない。自然界についての「可能10%」を機械的に変更することもしない。

## 6. 再現・検証・独立レビュー用の確認点

```bash
python src/symbolic/nut_null_return_certificate.py
python src/symbolic/nut_null_return_geometry.py
```

ローカル：Python 3.13.5、SymPy 1.14.0、mpmath 1.3.0で両方成功。
存在証明のcertificateは標準ライブラリと整数のみ。幾何の別検算は厳密代数＋50/80桁、40桁以上一致。
80桁で直接の計量・null・向きの最大残差は約 `4.22e-81`。
初回のSymPyの構造的な等値assertは、式の差を厳密に簡約するassertへ修正。式・精度・成立条件は弱めていない。

レビューの要点は、(i) 北極束座標の閉合、(ii) 全Hamilton方程式とradial反転、(iii) 根の存在と全経路がE内にあること、(iv) 局所対角wavefrontを片方の変数だけで伝播する論理、の四つである。
CIは(i)–(iii)の代数・証明書を検査する。(iv)の既知定理および本適用は本文の解析的証明であり、Python/Leanの形式証明とは呼ばない。

ローカルのgit cloneはDNS失敗したため、全repoをローカルで検査したとはしない。
新規二本は独立で、共有import・入力data・依存・CI・Lean・既存assertに変更なし。
通常のPR累積差分選別器で二本をPython 3.12で検査し、実際のcommit・checkout・CI run・結果はPRに記録する。

## 一次資料・照合範囲

- **[J]** C. V. Johnson, H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, [hep-th/0405141](https://arxiv.org/abs/hep-th/0405141)。本文(72)–(73)の北／南のmonopole connection、(79)のdilaton、(81)の対称chart、導入のHopf fibre周期を照合。
- **[K]** B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, [gr-qc/9603012v2](https://arxiv.org/abs/gr-qc/9603012v2)。§3の伝播、§5の証明手法、**§6 printed pp.31–32のself-intersecting-but-not-closedなnull測地線への拡張と特殊なrefocusing例外**を確認。今回は地平面の定理そのものの適用ではない。
- **[M]** I. Khavkine, V. Moretti, *Algebraic QFT in Curved Spacetime and quasifree Hadamard states: an introduction*, [1412.5945v3](https://arxiv.org/abs/1412.5945v3)。Theorem 6（printed p.46）、Theorem 9（pp.48–49）、smoothな低階項の留保を確認。Theorem 9のglobal hyperbolicityを全NUTに無断で仮定せず、小近傍内のHadamard形に使用。

webでPDF抽出本文を確認した。ページ画像の取得は内部エラーとなり、画像を目視済みとは記載しない。図表から数値を読んだのではなく、数式を独立導出・検算した。
検索は本模型と特異性伝播に限定し、全文献の網羅や結果の優先権を主張しない。
