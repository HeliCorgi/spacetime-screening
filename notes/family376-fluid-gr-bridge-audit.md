# Family 376 と spacetime-screening：計算万能性から重力へ何が移せるか

**監査日：2026-10-08。総合評価 B — 数学的な compiler／検証の接点はあるが、物理的な橋は未構成。**

対象を次の原本に固定した。

- spacetime-screening：`1ff10c4453f52f9f8f8c2c835a52812ce7faac90`
- OpenAI/math：`adc7f1241b42e322a6451854ab7e4b4c146bf78a`、Family 376、2026-09-27付の9稿。

[定理・資源・Leanの台帳](family376-theorem-ledger.md)／[研究課題5件](family376-research-tasks.md)／[検証記録](family376-validation.md)／[記号・有理数検算](../src/symbolic/family376_bridge_checks.py)／[条件付きLean lemma](../src/lean/Family376Bridge.lean)。

## 0. 結論と射程

**Family 376を追加しただけでは、新しいCTC時空、無条件のGR/半古典重力の判定不能性定理、普遍的なchronology-protection定理は得られない。** 得られるのは、具体的な流体compilerの参照実装・効果的符号化の定義・停止検出の仕様と、何をさらに証明しなければ重力へ転送できないかという厳密な問題設定である。

本監査のBは「Einstein–fluidへの埋込みが証明済み」という意味ではない。9稿の具体的な非相対論的PDE構成を部品として使えるため、単なる比喩より先に進める、という評価である。**直接の `halts iff CTC` は現状C（類推／未構成の還元）。** 普通の計算がchronalな背景で行えることと、time-machine候補の可否は独立である。

先の監査の「C＝現在の定式化では判定が付かない」は、計算理論の「決定不能」とは違う。またrepoの過去通信A/B/C、前フェーズの存在／no-go／未確定、今回の接続度A/B/C/Dを混用しない。

ここで「原稿で証明」と記すのは、その原稿の定理・証明に存在する主張である。全証明の独立査読や全Lean依存関係のkernel再検査を終えたとの表示ではない。今回の独立検証は、台帳で特定したstatementの照合、有限符号化の代数、エネルギー等の恒等式、明示的仮定を持つ論理lemmaに限る。

## 1. Family 376が実際に構成するもの

原稿間で共通する基礎は、固定した平坦な三次元空間上の

\[
\partial_t u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u+f,
\quad \nabla\cdot u=0,\quad u(0)=0,
\]

である。\(t\ge0\) は通常の外部時間で、\(\nu>0\) は粘性。algorithmicな評価では正のcomputable realであることを要求し、非計算可能な値ではその値へのoracle相対の意味になる。領域は稿ごとに平坦な \(\mathbb T^3\)、\(\mathbb R^3\)、\(\mathbb R^2\times\mathbb T\)。壁でのno-slip境界条件を共通に課しているのではない。[F01–F09]

有限な機械記述 \((e,w)\) から、全命令分岐を実装した外力の有限評価プログラムを作る。指定された計算を先に走らせ、その軌跡を外力として再生するのではない。gapped radixによるテープ、消去を可逆にする履歴、rectangle/sheet/solid-boxのincompressibleな移動、clock、途中で誤検出しないdetectorが本質である。すべての微分を指定精度で評価できることと、評価計算が効率的・有限資源装置で実装できることは異なる。

予め構成したsmoothな発散零速度 \(U\) に

\[
f_\nu=\partial_tU+(U\cdot\nabla)U-\nu\Delta U,\qquad p=0
\tag{1}
\]

を対応させる。そのような制御入力を許すPDE問題としてこれは正当であり、単なる恒等式だけが論文の成果なのでもない。ただし重力のmatter sourceの存在証明ではない。別解との差のエネルギーにGronwallを適用した一意性は、**そのforce/dataと指定comparison classに関する一意性**であり、任意の3D Navier–Stokes初期値に対する大域正則性の解決ではない。

主稿[F03]は \(t\ge1\) でstationaryなforcing、[F01,F05,F09]はeventually periodic、[F04]はperiodic from zero、[F06,F08]は減衰型である。これらを同時に満たす単一模型と読んではいけない。粒子のopen-setへの到達、速度場の固定閾値、半平面積分の閾値も異なる観測問題である。

特に

\[
u(t+1,x)=u(t,x)\quad\not\Rightarrow\quad (t,x)\sim(t+1,x).
\]

**周期的な流れは、時間を商で同一視した時空ではない。** Family 376の流体解にCTCが含まれる、という解釈は成立しない。

## 2. 現在のrepoのどこに接続するか

現mainの文書・Python・Leanを、PDE、Turing/halting、stress、state、chronologyの観点で調べた。既存の閉じたEinstein–viscous-fluid compilerは確認できなかった。次表は、現在あるものと接続に不足するものを分けた対応表である。

| repoの箇所 | 現在の対象 | Family 376との接点／不足 |
|---|---|---|
| [THEORY](../THEORY.md)、scalar–tensor・QTG等 | 共変作用、曲率応答、背景と摂動の健全性 | PDEの明確な作用・principal partという要件は共通。流体compilerや量子状態の供給ではない |
| [SA v4](sa-quantum-record-v4.md)、[v5](sa-two-input-state-v5.md) | MP/RN接合、散乱、有限modeの二入力制御 | 流体の記録を入力制御に使う余地はあるが、全SA上の単一positive Hadamard Wが未構成 |
| [operational v6](sa-closed-operational-loop-v6.md)–[v8](stress-deutsch-qft-v8.md) | channel、固定点選択、affinity | 有限machine encodingと量子操作の定義を区別できる。NSはDeutsch則を導出しない |
| [CBSSL v9](chronology-backreaction-selection-v9.md) | 仮説的なmetric/state選択則 | 最適化の探索難度は問えるが、許容集合の非空性や最小値の達成をcompilerが保証しない |
| [v10](cbssl-rset-core-v10.md) | Popov近似RSETのconstant core root、別途課したtimelike quotient | 流体・driverの応力を足せば別方程式。既存の2変数rootをそのまま保てない |
| [v11](cbssl-global-rset-v11.md) | spacelike flat quotientのimage/Casimir対照、global completion不足 | 外力の計算万能性はHadamard imageの許容域やglobal Wを変えない |
| [NUT null-return](nut-null-return-obstruction.md) | 指定自由場の特異性伝播に基づく障害 | halting detectorの軌道と、KG principal symbolのnull bicharacteristicは別物 |
| [B1](../research/auxiliary_volume_B1/README.md) | 古典的bounce・有限曲率候補 | 提示されたglobal timeはCTC detectorと相容れない。量子状態・流体計算の定理は未供給 |
| [既存Lean](../src/lean/ChronologySixGate.lean) | 仮定付きの因果順序lemma | 本監査の条件付き還元lemmaを隣接配置できる。幾何・QFTの仮定を形式検証済みにしない |

v10のCTCは \(L^2-\Delta^2<0\) の同一視によって入力される。計算結果が計量を変えてCTCを形成したものではない。v11のspacelike image公式の適用外を「全timelike stateの不存在」と読み替えることも、本監査では行わない。PR #39の追加監査はmain未統合の別成果として扱う。

[F08]のscalar potentialsは、incompressible速度を生成する古典的なpotentialである。**Klein–Gordon場、そのpositive二点関数、あるいはRSETを意味しない。** 同様に、流体粒子の軌跡は一般に測地線ではなく、特にnull測地線ではない。

## 3. NSからEinstein方程式への橋：Bianchi identityが最初のゲート

固定renormalized couplingsを採用して

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
+\alpha H^{(1)}_{\mu\nu}+\beta H^{(2)}_{\mu\nu}
=8\pi G\bigl(T^{\rm fluid}_{\mu\nu}+T^{\rm drive}_{\mu\nu}
+T^{\rm other}_{\mu\nu}+\langle T_{\mu\nu}\rangle_{\rm ren}[g,W]\bigr)
\tag{2}
\]

を考える。\(H^{(i)}\) は局所共変な曲率countertermの変分で保存する。共変な自由場のRSETも適切な繰込みで保存する。従って、外力を受けるfluidだけを右辺へ置くのは一般には不整合である。

\[
\nabla_\mu T_{\rm fluid}^{\mu\nu}=F^\nu,
\qquad \nabla_\mu T_{\rm drive}^{\mu\nu}=-F^\nu
\tag{3}
\]

という**全stressの保存**を実現するdriverが必要になる。driverの方程式、有限エネルギー、境界、charge、反作用まで指定しなければ、式(1)の自由なbody forceはEinsteinのsourceとして完成しない。重力側の必要stressを単に \(G_{\mu\nu}/8\pi G\) と逆定義することもmatter実現の証明ではない。[R1,R3]

非相対論的な \(f\) がNewtonian重力 \(-\nabla\Phi\) であるとも限らない。例えば \(U=(a(t)\sin 2\pi y,0,0)\) では

\[
f=(a'+4\pi^2\nu a)\sin(2\pi y)\,e_x,
\]

で、一般に \(\nabla\times f\ne0\)。純粋なscalar gravitational potentialへの置換は既にここで失敗する。EM等を候補にするなら、その電流・charge・Maxwell stressの保存まで解く必要がある。この負例は本PRのPythonが厳密に検査する。

### 相対論的粘性流体への置換

通常の非相対論的incompressible NSを、名称だけでrelativistic Navier–Stokesにしてはいけない。粘性stressのconstitutive law、frame、EOS、entropy、特性速度、constraint propagationを指定する。

BDNKの一次相対論的粘性流体には、係数・EOS等の仮定下でEinsteinとの結合のcausality／strong hyperbolicityと平衡安定性を示す理論がある。[R1] bulk-onlyのIsrael–Stewart系には別の対称双曲型局所存在理論があるが、shearやdiffusionを無断で追加できない。[R2] **これらはFamily 376のcompilerをその系へ埋め込む定理ではない。** Einstein–EulerやMHDも同様に候補classであって完成した橋ではない。

さらに初期データは、通常のGR符号規約の下で

\[
R(h)+K^2-K_{ij}K^{ij}=16\pi G\rho+2\Lambda,
\quad D_j(K^{ij}-h^{ij}K)=8\pi G j^i
\tag{4}
\]

を満たす必要がある。高次曲率の扱いを変えれば初期値問題も変わる。既存NSの \(u(0)=0\) と機械的に同一視できない。Newtonian/low-Mach極限の有限時間近似があっても、任意長計算を一つの有限パラメータで模倣する全時間定理にはならない。

## 4. 資源・精度・全時間の三つの落とし穴

### 4.1 有界運動エネルギーと有限の総投入仕事は違う

密度1、境界fluxなしのtorusでは

\[
\frac{d}{dt}\frac12\int |U|^2+\nu\int |\nabla U|^2=\int f\cdot U.
\tag{5}
\]

従って非自明なmean-zero定常速度を無限時間維持する実装は、正の粘性散逸率を持ち、総投入仕事が無限になる。周期的実装なら1周期の仕事が \(\nu\int_{\rm cycle}|\nabla U|^2>0\) なので、停止せず同じ処理を繰り返す限り同じ結論である。これは標準エネルギー恒等式の条件付き帰結であって、新しい「全計算禁止定理」ではない。

[F06,F08]の減衰型は別である。固定有限体積内で \(|U|,|f|\le C/(1+t)\) なら \(\int|f\cdot U|\,d^3x\,dt\) は有限にできる。**そのため「万能計算は必ず無限の機械的仕事を要する」という逆の主張も誤り。** それでも有限rest mass、外力装置の仕事、測定エネルギー、有限bits、noise耐性を証明したわけではない。

### 4.2 無限時間計算は無限精度の問題を隠せる

gapped radixで第n桁に差がある二つの符号の間隔は \(O(b^{-n})\)。[F06]のalternating memoryはさらに

\[
s_n=(N+1)2^{(n+3)^2},\qquad \epsilon_n=b^{-s_n}
\]

のような縮小scaleを使う。smoothnessやすべての微分の減衰は、符号間距離の一様な下限ではない。1ステップごとのphysical timeが有限で、全ステップを有限時間へ詰め込むZeno computationでもない。停止までの時間は一般に非有界であり、非停止を有限時間の観測で認定する装置ではない。[F03,F06]

[F07]の速度閾値 \(1/2\) はこの問題への重要な別アプローチである。ただしtorus版は全時間での微分一様有界を要求せず、cylinder版は水平supportを拡大する。固定閾値から、perturbed forceや量子noiseに対する無限時間robustnessは自動的には出ない。

### 4.3 量化記号を入れ替えない

有限prefixのshadowingは概ね

\[
|\delta X(t)|\le e^{Lt}|\delta X(0)|
+\int_0^t e^{L(t-s)}\|\delta u(s)\|_\infty ds
\tag{6}
\]

で見積もる。必要なのはdetectorの位置に応じたmarginとの比較であり、

\[
\forall n\ \exists\varepsilon_n>0\ \text{n段まで正しい}
\quad\not\Rightarrow\quad
\exists\varepsilon>0\ \forall n\ \text{全段で正しい}.
\]

重力が小さい、粘性が小さい、\(\hbar\) が小さい、有限mode数で一致する、という確認だけでは右側を得られない。遅いclockも累積量が無限でなければ全命令を実行しない。\(\int_0^\infty(1+t)^{-2}dt=1\) のclockは停止問題の転送を壊す。固定粘性での \(U_\varepsilon(t)=\varepsilon U(\varepsilon t)\) は粘性項が \(O(\varepsilon)\)、慣性項が \(O(\varepsilon^2)\) になり、外力を一律に \(\varepsilon^2\) 倍するのも誤りである。

## 5. 何を幾何学的detectorにするべきか

| event | 有用性 | 停止との同値に必要な追加証明 |
|---|---|---|
| 局所のmaterial record／smeared scalar record | 最初の橋として最小 | 物理的observerで定義し、gauge・driver・有限時間誤差を制御 |
| trapped surface \(\theta_+,\theta_-<-\delta\) | strict marginを付けられ、GH発展内でも起こり得る。**最も自然な幾何的候補** | 計算recordによる崩壊triggerと非停止側のfalse-positive排除。CTCとは別 |
| geodesic incompleteness | 特異性研究との接点 | 条件付き特異点定理の全仮定。incompletenessからCTCは従わない |
| Cauchy horizon | 既存RN/NUT/SAとの接点 | 選んだpartial Cauchy面、拡張class、生成子、regularityを指定 |
| global hyperbolicity failure | broaderなglobal property | horizon、boundary、欠損点等を分離。GHでないだけでCTCとはいえない |
| CTC／chronology transition | 今回の最終関心 | 実際の閉じたtimelike曲線、形成／拡張の選択、admissible W、全backreaction |

trapped surfaceを推奨するのは、既にhalt iff trapped surfaceが証明されているからではない。局所量にstrict marginを付けられるという、研究設計上の判断である。

### Maximal globally hyperbolic developmentの誤用を避ける

Einstein Cauchy問題のMGHDは、定義上globally hyperbolicでCTCを含まない。[R3] 対象をMGHD自身に固定した `halts iff CTC` は、すぐ停止する機械一つで破綻する。「その先の拡張にCTCがあるか」なら、拡張をすべて量化するのか、一つでもよいのか、どの境界則で選ぶかを指定する必要がある。MGHDの一意性定理は一意なCTC拡張を供給しないし、choiceを避けた構成はcomputable realの意味でのsolver定理でもない。

さらに、結合後の全時空にreal-valuedな滑らかなtime function tがあり \(g^{-1}(dt,dt)<0\) なら、未来因果曲線上でtは単調になりCTCはない。本PRはADMの局所恒等式 \(g^{tt}=-N^{-2}\) だけを計算する。**tが大域的実数値であるという幾何学的仮定は別途必要**である。\(\partial_t\) のnormと \(dt\) のnormも取り違えない。

## 6. 量子場と半古典feedbackをどこまで足せるか

自由実スカラーなら、同じgについて少なくとも

\[
P_xW=P_{x'}W=0,\quad W(\bar f,f)\ge0,
\quad W-W^{\rm T}=iE\ \text{locally},
\quad W-H_g\in C^\infty\ \text{locally}
\tag{7}
\]

を要求する。全CTC時空に一意なretarded propagatorがあるとは仮定せず、CCRとHadamard条件を小さいglobally hyperbolicな近傍で記述する。RSETは固定local covariant renormalizationで

\[
\langle T_{\mu\nu}\rangle_{\rm ren}
=\lim_{x'\to x}D_{\mu\nu'}(W-H_g)+C_{\mu\nu}[g]
\tag{8}
\]

から構成し、(2)へ戻す。[R4,R5]

**Family 376は(7)も(8)も供給しない。** 有限精度で流体速度を計算できることは、positive distribution Wの存在、wavefront set、無限mode極限の保存、繰込みの有限性の証明ではない。一方、Hadamard条件が「計算万能性を禁止する」とする一般定理もここからは得られない。

この区別の簡単な例として、GH背景の通常の自由場で、zero-mean Hadamard状態を滑らかな実KG解 \(\varphi\) によってcoherentにshiftすれば、二点関数は \(W_0+\varphi\otimes\varphi\) となる。差がsmoothであるためHadamard性は変わらず、shift automorphismはpositivityとCCRを保つ。**これはsmooth classical recordとHadamard性が論理的に排他的ではないことの例にすぎない。** \(\varphi\) に万能機械を埋め込んだ証明でも、有限energy・同じgでのSCEEを一般に保証する主張でもない。[R4]

また有限RSETは、stress fluctuationが小さいことではない。

\[
N_{\mu\nu\rho\sigma}(x,x')=\tfrac12
\omega\bigl(\{t_{\mu\nu}(x),t_{\rho\sigma}(x')\}\bigr)
\]

というnoise kernelは分布として扱い、適切なspacetime smearingでmetric/readout誤差を評価する必要がある。[R6] 小さい符号間隔が量子揺らぎで必ず壊れるというno-goも、常に保護されるという定理も未構成。現在ある特定cosmologyでのSCEE局所存在結果を、任意のinhomogeneous Einstein–fluid–QFTやCTCへ拡張してはいけない。[R7]

## 7. KRW／chronology protectionと計算万能性

### 適用条件を保持した場合

KRWは、initial GH領域からcompactly generated Cauchy horizonへ延長する通常のKG二点関数について、base pointsで局所Hadamard形が維持できないことを示す。必要な正則性・bisolution・初期Hadamard等を保持する限りの結果である。通常のpoint-splitting RSETがそこでill-defined/singularになることと、全成分がすべての接近方向から単純に無限大へ行くことは同じではない。[R5]

**「量子場が計算を物理的に停止させる」ことはKRWの結論ではない。** その同時仕様に許容状態がない／半古典記述が破綻する、という結果であって、装置の停止過程や完成した反作用解は別に必要である。Hawkingのchronology protectionも、一般のすべてのCTC時空を排除する証明として使わない。[R8]

noncompactly generated horizon、最初からCTCを持つ時空、異なる境界classはcompact-horizon版KRWの自動適用外だが、そのまま成功候補ではない。polarized hypersurface、自己帰還null測地線、global Wの条件は個別に残る。repoのNUT障害も、普遍的な流体計算禁止ではなく指定場・指定背景に関するもの。[R5]

QEIは場・状態class・smearing等を指定した平均負エネルギーの下限である。任意の古典流体stressへの万能な不等式でも、あらゆる計算機のmemory容量や停止時間の上限でもない。[R9]

### 本監査で実際に示せる条件付き系

compiler \(C(e,w)\) が全入力でadmissible Hadamard系を返し、停止入力なら必ずKRWの全仮定を満たすhorizonを返す、と要求する。

\[
\forall z:\operatorname{Regular}(Cz),\quad
\operatorname{Halts}(z)\Rightarrow\operatorname{KRW}(Cz),\quad
\operatorname{KRW}(s)\Rightarrow\neg\operatorname{Regular}(s).
\tag{9}
\]

すぐ停止するzを代入すると矛盾する。したがって**この仕様を満たすtotal compilerはない**。これは有効な条件付きnon-transfer statementであり、Leanはその論理部分を検査する。ただしKRWをLeanへ形式化したわけではなく、引数として明示している。Family 376のuniversal性やhalting undecidabilityさえ必要ではないので、新発見のchronology protectionと称してはいけない。

逆方向も限定される。式(9)は選択したhorizon detectorとの結合を排除するだけで、計算を通常のchronal領域で行うPDE classは排除しない。**chronology protectionは通常計算の否定ではなく、特定のoutput specificationへの制約になり得る。**

## 8. 決定不能性を得るために本当に必要な還元

有限入力からadmissibleな重力問題の記述へ、computableなtotal map Cを作り、解または拡張の意味を固定して

\[
\operatorname{Halts}(z)\Longleftrightarrow\mathcal P(Cz)
\tag{10}
\]

を示せば、そのclass上の \(\mathcal P\) を判定するalgorithmはhaltingを判定してしまう。ここまでの**論理的なtransfer lemma**は本PRにある。ただし以下が未供給である。

| 必要条件 | Family 376のみで供給されるか |
|---|---|
| 有限記述からforce・NS観測へのeffective compiler | 対象稿の条件下でyes |
| g、matter、driverを含む適法initial/boundary dataへのeffective compiler | no |
| すべての入力についてwell-definedな解／拡張class | GR bridgeではno |
| 出力predicateがCTC等の幾何・diffeomorphism invariantである | no |
| 非停止側も含むsoundnessとcompleteness | NS detectorにはある。CTCにはno |
| 固定物理parametersでの任意長実行／finite-resource class | no |
| positive Hadamard Wと同じgのSCEEへのlift | no |

`if machine halts then timelike quotient else spacelike quotient`と書いてから計量を渡す操作は、halting oracleを使うためcomputable reductionではない。有限cutoffの全例一致や数値探索の不成功でも(10)は証明されない。source側の有限記述・比較class・観測定義が変われば、reduceすべきdecision problem自体を作り直す。

Leanの `Decidable` をTuring computabilityの代用にもしない。今回のlemmaではSourceAlgorithm、TargetAlgorithm、compositionの効果性、source undecidabilityを別々の仮定にしており、その欠落を隠していない。

## 9. 最終評価と次に解く一問

**評価B**：全命令分岐を保つcompiler、finite-prefixのquantitative検証、resource ledger、KRW-awareな還元仕様には、具体的な数学的接続がある。**直接CTC/SCEEの存在・判定不能性は未達**。無条件に新しいtime-machine candidateが増えたとはいえない。

今すぐ得られるno-goは式(5)、(9)のような既知の恒等式／既存定理からの限定的帰結であり、「全CTC不存在」でも「全万能流体の物理的不可能」でもない。新しいundecidability theoremが将来得られる可能性は、式(10)のmissing arrowsを本当に構成した場合に限る。新しい候補を支持するには(2)、(7)、(8)を同時に閉じなければならない。

最優先は[課題R1](family376-research-tasks.md)の**非potentialな1個の流体gateを、有限energyのdriver付きEinstein–causal-fluid系にliftする問題**である。最初からCTCをflagにせず、固定有限時間の誤差・全stress保存・constraintを検査する。ここが未解決のままhorizonや量子場へ進むと、存在しないsourceを前提にした議論になる。

## 一次資料（Family稿の詳細は別台帳）

- **R1** Bemfica–Disconzi–Noronha, *First-Order General-Relativistic Viscous Fluid Dynamics*, [arXiv:2009.11388v2](https://arxiv.org/abs/2009.11388v2). 結合系の双曲性等。universal compilerは含まない。
- **R2** Bemfica–Disconzi–Noronha, *Causality of the Einstein–Israel–Stewart Theory with Bulk Viscosity*, [arXiv:1901.06701](https://arxiv.org/abs/1901.06701). bulk-only等の対象範囲を保持。
- **R3** Sbierski, *On the Existence of a Maximal Cauchy Development for the Einstein Equations — a Dezornification*, [arXiv:1309.7591v3](https://arxiv.org/abs/1309.7591v3). MGHDと拡張問題の区別。
- **R4** Khavkine–Moretti, *Algebraic QFT in Curved Spacetime and quasifree Hadamard states: an introduction*, [arXiv:1412.5945](https://arxiv.org/abs/1412.5945); Benini–Dappiaggi–Hack, *Quantum Field Theory on Curved Backgrounds — A Primer*, [arXiv:1306.0527](https://arxiv.org/abs/1306.0527); Fewster–Rejzner, *Algebraic Quantum Field Theory — an introduction*, [arXiv:1904.04051](https://arxiv.org/abs/1904.04051). 状態、CCR、Hadamard／coherent shiftの枠組み。
- **R5** Kay–Radzikowski–Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, [arXiv:gr-qc/9603012](https://arxiv.org/abs/gr-qc/9603012). Theorem 2/2′、base points、適用外の比較例。
- **R6** Hu–Verdaguer, *Stochastic Gravity: Theory and Applications*, [arXiv:0802.0658](https://arxiv.org/abs/0802.0658). noise kernelと半古典近似の検証。すべての背景の安定性とは読まない。
- **R7** Pinamonti–Siemssen, *Global Existence of Solutions of the Semiclassical Einstein Equation for Cosmological Spacetimes*, [arXiv:1309.6303](https://arxiv.org/abs/1309.6303). 対称性・場・延長条件を保つ。
- **R8** Hawking, *Chronology protection conjecture*, [Physical Review D 46, 603](https://doi.org/10.1103/PhysRevD.46.603). conjectureと証明の区別。
- **R9** Fewster, *Lectures on quantum energy inequalities*, [arXiv:1208.5399](https://arxiv.org/abs/1208.5399). 平均負エネルギーの限定条件。
- **R10** Cardona–Miranda–Peralta-Salas–Presas, *Constructing Turing complete Euler flows in dimension 3*, [PNAS 118, e2026818118](https://doi.org/10.1073/pnas.2026818118); Dyhr–González-Prieto–Miranda–Peralta-Salas, [PNAS Nexus 5, pgag131](https://doi.org/10.1093/pnasnexus/pgag131). 後者のadapted Riemannian metricとHodge viscosityを平坦なEinstein流体へ流用しない。
