# 選んだ情報を過去へ送れるか：受信記録まで含めた通信判定

**2026-09-23 / 研究対象：operational past-directed signalling。**

**結論：物理的な過去通信は未実証。今回棄却したのは、異なるCTC固定点を得ただけで「選んだビットを送れる」と認定する手順であり、時間遡行一般ではない。**

読取基点：`main` の `fd29df1be41391ee94d5c1a2a1458c60423ad545`（PR #8マージ後）。
[前回の継続ノート](heterotic-taubnut-operational-continuation.md)と[six-gate audit](heterotic-taubnut-six-gate-audit.md)を引き継ぐ。
今回の新しい判定基準と再開点はこちら。古い計算・反例は取り消していない。

## 1. 6条件を、目的に合わせて修正する

「完全な6条件を順番に全部解く」ことを研究の目的にしない。目的は、許容された送信操作を変えることで、実験室の時計で先に起きた受信事象の記録分布が変わるかである。

| 旧条件 | 今後の扱い |
|---|---|
| 完全なBRST cohomology | stringによる実現案では、使う状態・操作・観測量の物理性を証明する。**全cohomologyの分類を先に完成させる必要はない。** |
| 正ノルム・正常化 | 正の正常化された実験確率を要求する。波束・混合状態も許す。単色一般化固有状態の素朴なL²発散だけで通信を否定しない。 |
| full string spectrum | 実際に使う符号化と相互作用の許容性は必要。**全スペクトルの列挙は不要。** 限定したsectorが閉じていると勝手に仮定もしない。 |
| backreaction込みで状態が維持 | **通信過程全体が自己無撞着に実行できること**へ変更。受信器への吸収・散乱・状態変化は通信の一部であり、入力状態の完全保存は不要。|
| NUT到達が因果構造を変える | 既存CTCを利用する可能性の判定では、**新規の因果構造変更を必須から外す**。Taubからのアクセス、NUT内での利用、chronalな初期状態からの装置形成は別問題。 |
| 選んだ情報を過去へ届ける | 中心の判定として残す。送信設定の選択装置・記録と受信器を含む確率を求める。相関・振幅・固定点の差だけでは認定しない。 |

これらは未知のBRST内積や相互作用を「成立済み」にする変更ではない。不要な全分類を避け、実際のプロトコルに必要な部分を特定する変更である。特定の準備の失敗はそのプロトコルを棄却するが、全プロトコルの不可能性までは与えない。

## 2. 操作的な最小仕様

受信事象Bと送信事象Aを結ぶ短い実験室世界線で、固有時が `tau_B < tau_A` となることを先に指定する。周期座標の数値の大小だけで「過去」と呼ばない。

同じ外部準備・同じ大域的法則の下で二つの許容された操作を実行し、結果を選別しない分布から

```math
\Delta_{\rm do}=\frac12\sum_y
|P(y_B\mid\mathrm{do}(b=0))-P(y_B\mid\mathrm{do}(b=1))|
```

を評価する。bit選択を物理装置Rに記録する実装では、その装置も含む `P(R=b,y_B)` を求める。選択がどう行われたかを指定せず、相関 `P(y|R=b)` を自動的に介入確率と同一視しない。

**「同じ準備」は、循環する全変数や受信結果まで同じに固定する、という意味ではない。** それでは最初から信号を定義で禁止してしまう。外から与える準備と法則は同じでも、ループ内部の解は操作に応じて変わり得る。逆に、欲しい未来bitとの相関を過去の入力へ手で挿入するだけでも証明にはならない。その相関がどの物理法則から生じるかを示す必要がある。

非線形なCTC処方では、別々の入力に対する出力を平均したものが、ラベルを保持した混合入力の出力になるとは限らない。[B1]が指摘するlinearity trapである。本研究では線形性を追加公理として強制せず、**採用する処方のまま両方を計算し、実験的に何を比較したかを区別する**。

## 3. 受信者の場所：幾何だけで排除できる案と残る案

コード：[taubnut_receiver_event_geometry.py](../src/symbolic/taubnut_receiver_event_geometry.py)。

これは新しい時空の発見ではなく、[J1, 式(72)–(73)]と既存repo計量の再検算である。

```math
p=x^2-1,\quad D=(x+\delta)^2-\frac{4p}{k+2},\quad K=(k-2)\alpha',
\qquad t\sim t+L,\quad L=4\pi\lambda.
```

従来と同じ `k=8, delta=sqrt(8/5), lambda=sqrt(2/5), alpha'=1` を固定する。

### 3.1 chronalな元の実験室へ戻す案

完全な対象時空でBがchronalであり、信号が計量の因果経路に沿うなら、`B << A <= B` はpush-upによって `B << B` を与え矛盾する。[既存Lean補題](../src/lean/ChronologySixGate.lean)の条件付き結論を使える。BRST全分類を待つ必要はない。

同じoutgoing地平面チャートでは `g(v,n)=-K v^x/(1+delta)` であり、未来向き因果ベクトルは地平面上で `v^x >= 0`。この局所検算だけから全ての別延長・非計量的応答を排除しない。

### 3.2 NUTにいる受信者を使う案

固定角度、`x=2` にBを `t=0`、Aを `t=L/4` と置く。二事象は同じ点ではない。増加するt方向を未来と取ると、短い円弧B→Aも、残りの円弧A→Bもtimelikeである。

```math
\Delta\tau_{B\to A}=\frac L4\sqrt{Kp/D},\qquad
\Delta\tau_{A\to B}=\frac{3L}4\sqrt{Kp/D}.
```

`alpha'=1` 単位で、それぞれ `2.74080866537383...`、`8.22242599612150...`。一周は `10.96323466149533...`、静止軌道の加速度二乗は `0.08245675506693...` で有限。物理的な秒へ換算した値ではない。

このBはchronalではない。したがって3.1の仮定をここへ移して禁止するのは誤りである。一方、閉路上の時計・受信器・記憶・駆動装置の全状態が整合することは、timelike曲線の存在からは従わない。各円弧の固有時を、商時空全体の一価な実数時計と取り違えない。

**今回の判定対象として残すのは、このNUT内プロトコル。** Taubからの装置搬入やchronalな初期状態からの形成は、より強い別の実現可能性問題として残す。幾何上の存在、準備可能性、実際の通信を区別する。

## 4. 受信器を含む最小CTC回路で、通信判定器を検証

コード：[chronology_reference_bit_channel.py](../src/symbolic/chronology_reference_bit_channel.py)。

**これはTaub–NUTから導いた有効理論ではない。** Deutsch型の有限次元処方[D1,T1]に基づく対照模型で、物理的な過去通信を認定する際の誤判定を検査する。以下の有限行列は今回の実装・導出であり、原理上のlinearity trap自体は既知[B1]。優先権は主張しない。

D：受信記録qubit、S：送信carrier、C：戻るqubit、R：選んだbitを保持する古典flagを使う。tensor順序はD,S,C。Rを保持した全状態は16次元だが、古典flagの二つの対角blockとして正確に実装する。

Dは0で準備し、**送信操作より先に** `CNOT(C -> D)` でCを読む。その後、SとCに

```math
U_\vartheta=cI-is\,\mathrm{SWAP}_{SC},\qquad c^2+s^2=1
```

をかける。戻り枝には同じdepolarizing channel

```math
\mathcal D_\eta(X)=\eta X+(1-\eta)\operatorname{tr}(X)I/2,
\qquad 0\le\eta\le1
```

を入れる。受信測定によるdephasingも計算に含める。環境をtraceするこの有限回路が重力中に実装できるとは仮定しない。

### 4.1 bitを一つに固定した計算

Sの入力を `rho_b=|b><b|` とすると、Cの一周mapは

```math
\mathcal F_b(\tau)=\eta[c^2\mathcal Z(\tau)+s^2\rho_b]+(1-\eta)I/2,
```

となる。ここでZはZ基底のdephasing、tauはtrace 1。任意の演算子への線形拡張ではrho_bとIの項にtraceを掛ける。

```math
g=\eta c^2<1,\quad d=\eta s^2,\quad
\zeta=\frac{d}{1-g},\qquad
\tau_b=\frac12[I+(-1)^b\zeta Z].
```

この固定点は一意、正常化され、正である。一周mapのChoi行列は対角で、固有値の下限は `(1-eta)/2 >= 0`。trace保存も検査した。traceless差に対するtrace normの収縮率は高々gであり、`0<=zeta<=1`。これは**固定点反復の数学的安定性**であって、重力のbackreaction安定性ではない。

各bを別々に固定した二つの計算では、Dの記録分布の距離はzetaとなる。例として

```math
c=3/5,\quad s=4/5,\quad\eta=3/4
\quad\Rightarrow\quad g=27/100,\quad\zeta=48/73.
```

しかし、この結果だけで未知の選択bitが受信器へ送られたとはまだ言えない。

### 4.2 Rにbitを保持して、一つの実験を計算する

通常のDeutsch product処方を文字どおり使い、

```math
\rho_{RS}=\sum_b p_b|bb\rangle\langle bb|,\qquad
\rho_{RSC}=\rho_{RS}\otimes\bar\tau
```

を入力する。Cは一つの周回固定点で、Rと初めにproductである。Rは回路と相互作用せず、最後まで保持する。ここではこれが混合入力の処方であり、別々の固定点を平均する手順へ変更しない[B1, 式(1)–(5)]。

`z_p=p_0-p_1` とすると

```math
\bar\tau=\frac12[I+\zeta z_pZ],\qquad
P(b,y)=p_b\frac{1+(-1)^y\zeta z_p}{2}.
```

したがって

```math
P(y\mid R=0)=P(y\mid R=1),\qquad
\Delta_R=0,\qquad I(R:D)=0.
```

公平なbitなら `P(b,y)=1/4`。`48/73` をこの実験の通信距離とすることはできない。Rの偏りを `p_0=1/3` に変えた検査も行い、分布は偏るが個々のbitとの相関は0のままである。

**なぜ起きるか。** 最初の受信作用の直後にはRとDは無相関である。その後の送信unitaryはS,Cに作用する。S,Cをtraceして得るR,Dの同時分布は、この後段のtrace-preserving操作で変わらない。一つの固定点が入力ensemble全体に依存することは、試行ごとのflag値を伝えることではない。

この議論は「RとCのproduct」「Dが先に記録」「後の操作がDへ作用しない」という構造に依存する。全てのCTC模型やTaub–NUTの全観測量に対するno-goではない。非線形理論で準備手順・混合の意味が異なるなら、その別の規則を明示して再計算する必要がある。

### 4.3 相関を許す別処方も明示して、禁止を先取りしない

入力を

```math
\Omega_{RSC}=\sum_b p_b|bb\rangle\langle bb|\otimes\tau_b
```

へ変えると、R,Sの周辺状態もCの周辺状態も4.2と同じである。しかしRとCは初めから相関している。同じ受信器・送信unitary・noiseを使うと、公平なbitと上の数値例で

```math
P_{\rm corr}(b,y)=\frac1{292}
\begin{pmatrix}121&25\\25&121\end{pmatrix},
\qquad\Delta_R=48/73.
```

これは正常化された正の分布である。各R blockでCの戻り状態は `p_b tau_b` となり、周辺のCTC固定点条件も満たす。一方4.2では

```math
P_{\rm product}(b,y)=\frac14
\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad\Delta_R=0.
```

つまり、**同じ局所入力周辺状態と周辺固定点条件だけでは、記録されたbitの通信統計は決まらない**。4.3は標準product処方ではなく、linearity trapで誤って得る平均がどの追加相関に相当するかを示す対照である。

相関処方を幾何・物理作用から導ければ、検討すべき候補になり得る。ここで禁止したことにはしない。しかし、欲しいbit相関を入力へ入れてからそれを読むだけでは、選択可能な過去通信の構成にはならない。その相関が自発的に生じる、物理的に準備できる、あるいは大域的法則が強制する、という導出は今回ない。

**診断結果：設定ごとの正の固定点・正常化・収縮性はそろっても、操作的な通信認定には足りない。**

## 5. 後から選別したデータも排除する

通常の順序付き量子回路の負例として、固定したBell対の片方をBで測り、もう片方を後で `X^b` の後に測る。後の測定結果0だけを残せば、Bの条件付き分布に距離1を作れる。しかし全試行の分布の距離は0であり、選別の採用率は両設定とも1/2。

これは普通のpostselectionで過去通信を偽装できる例である。後の採否を過去の受信者が知れることを仮定しない。P-CTC等の根本的な非線形処方を検討する場合も、普通の実験での後選別の成功をその処方の物理的実現と同一視しない。

## 6. Taub–NUT研究へ何を戻すか

[J1]はall-orders alpha-primeでCTCを含む幾何を与えるが、probeと完全なCFTの応答は別計算と明記する。前回の正則スカラーsourceも、R・D・環境を含む量子的確率規則を与えていない。

[T1]はD-CTC条件の近似解を、CTCのないglobally hyperbolicなQFTでも構成できると示す。したがって今回の有限行列が成功しても、時空にCTCが実装された証拠ではない。[H1]の2026年のhardware論文も、abstractで述べられるのはdecoder回路・postselection・classical feedbackの実装であり、これを物理的な過去通信の実験と数えない。本研究ではそのhardware実験を再現していない。

他方、追加の整合規則の下で過去通信を論じる別模型もある[S1]。今回のproduct模型の0という結果を、それらやstring theoryの普遍的な禁止へ拡大しない。

次に必要なのは、**Taub–NUT上の局所的な送信・受信作用と、R・D・環境の接合から、どの同時確率が導かれるか**である。局所的な有効場理論を入口にしてもよいが、その適用範囲と地平面を跨ぐときの限界を明示する。[Q1]のsource–detector形式のように、振幅だけでなくinclusiveな確率・応答を計算する。

### 次の小さな計算単位

NUT内の二つの有限な相互作用領域A,Bを固定し、受信器のblank stateと選択flagを明示する。まず実際の場に対する二つのcouplingと大域的gluingを指定し、`P(R=b,y_B)` または操作的応答を導く。**分からないgluingをDeutsch productや相関処方で埋めない。** 戻り枝が本当に得られた場合だけ、その局所演算子・有限エネルギー符号化をBRST/GSOの許容sectorへ対応させ、実験全体の逆反作用を評価する。

無信号を示すには、その計算で0となる理由と適用される全操作の範囲を示す。正の信号を示すには、相関を仮定して入力したのではないこと、受信時計の順序、全試行の正常化、許容された準備と相互作用をそろえる。

## 7. 再現・CI・新規性の境界

```bash
python src/symbolic/chronology_reference_bit_channel.py
python src/symbolic/taubnut_receiver_event_geometry.py
```

ローカルPython 3.13.5 / SymPy 1.14.0で両方success。回路は30組の有理数parameter、全matrix-unitからのChoi、unitarity、trace、固定点、保持flagの分布、異なる相関処方、postselection負例を厳密に検査。一般式の導出は§4、有限parameter検査と一般証明を混同しない。幾何も厳密な根号式でassertし、小数は表示だけ。

幾何script初回のassertはSymPyの同値な入れ子根号の簡約不足で失敗した。`sqrtdenest`で正確に同値変形して再実行した。許容誤差への置換やassert削除は行っていない。

共有コード・入力データ・依存・workflow・Leanは変更しない。新規2本を通常PRの累積差分選別器で検査し、実際のhead/base/checkout SHA・run・Python版・完了結果はPRへ記録する。全件二版検証とは呼ばない。Leanは新しい論理公理を増やすためには使わず、既存の条件付き補題を参照する。

**ラベル：** 幾何は既存結果の再現、linearity trapは既知原理の対照計算、receiver＋partial-SWAP＋noiseの明示式と二処方比較は本repoの計算候補。新規性の網羅的調査・優先権主張はしない。物理的なstring channelは未認定。

## 一次資料・今回確認した範囲

- **[J1]** C. V. Johnson, H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, [hep-th/0405141v3](https://arxiv.org/abs/hep-th/0405141v3)。式(72)–(73)、導入・結論のprobe/backreactionの留保をPDF抽出テキストで確認。
- **[D1]** D. Deutsch, *Quantum mechanics near closed timelike lines*, [Phys. Rev. D 44, 3197 (1991)](https://doi.org/10.1103/PhysRevD.44.3197)。書誌・abstractを確認。具体的固定点規則はB1とT1の表示式も照合。
- **[B1]** C. H. Bennett, D. Leung, G. Smith, J. A. Smolin, *Can closed timelike curves or nonlinear quantum mechanics improve quantum state discrimination or help solve hard problems?*, [0908.3023v2](https://arxiv.org/abs/0908.3023v2)。PDFの式(1)–(5)、保持reference、linearity trap、非線形処方への適用範囲を確認。
- **[T1]** J. Tolksdorf, R. Verch, *Quantum physics, fields and closed timelike curves: The D-CTC condition in quantum field theory*, [1609.01496v2](https://arxiv.org/abs/1609.01496v2)。式(1.1)、Proposition 3.3と結論を抽出テキストで確認。QFT定理をTaub–NUT上で実証したとはしない。
- **[Q1]** R. Dickinson, J. Forshaw, P. Millington, *Probabilities and signalling in quantum field theory*, [1601.07784v2](https://arxiv.org/abs/1601.07784v2)。inclusive detector確率とretarded連鎖の議論を確認。globally orderedなQFTの議論をCTCへ無条件適用しない。
- **[S1]** J. Bub, A. Stairs, *Quantum Interactions with Closed Timelike Curves and Superluminal Signaling*, [1309.4751](https://arxiv.org/abs/1309.4751)。abstractの追加整合規則と過去信号提案を確認。全回路の再現・正否の独立認定は未実施。
- **[H1]** S. N. Morapakula, K. Ikeda, *Closed Timelike Curve Decoding on Quantum Hardware*, [2607.27473](https://arxiv.org/abs/2607.27473)。2026年9月23日閲覧。abstractのreplacement map、post-selected decoder、classical-feedbackの範囲を確認。Taub–NUTの導出や実時間遡行の証拠として使わない。

文献検索は限定的であり、全ての時間遡行模型の不存在を検索で証明したものではない。J1/T1のPDF画像取得はエラーだったため画像を確認済みとはしない。Q1の冒頭ページ画像は確認した。数式の一次資料照合は抽出本文と上記範囲による。
