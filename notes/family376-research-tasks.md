# Family 376 接続後の研究課題：最大5件

2026-10-08。前提と出力classは[監査本文](family376-fluid-gr-bridge-audit.md)、入力定理は[Family 376台帳](family376-theorem-ledger.md)。以下は存在を認定した模型ではなく、反証条件を持つ研究課題である。各成功の射程を広げない。

## R1 — 有限energyの閉じたdriverによる相対論的shear gate（最優先）

**数学的定式化。** まず空間compactなCauchy面 \(\Sigma\simeq\mathbb T^3\) を選び、有限時間 \([0,T]\) だけを対象にする。物理的な長さL、速度A、smoothな時間pulse bを固定し、非相対論的参照gate

\[
U(t,x,y,z)=A b(t/T)\sin(2\pi y/L)e_x,
\qquad b(0)=b(1)=0
\]

を、局所正規直交frameで近似する。Family 376のshear分解の一部を移植する問題であり、このgate一つはuniversal machineではない。未知量を \(g\)、causal viscous fluidのthermodynamic variablesと四速度、driverの物理場 \(D\) とする。

\[
G+\Lambda g=8\pi G_N(T_{\rm fluid}+T_D),\quad
\nabla T_{\rm fluid}=F=-\nabla T_D.
\]

driverは例としてMaxwell場＋動的な荷電成分を候補にできるが、電流を外部関数として固定せず、その方程式・stress・charge conservationを明記する。torusの総charge constraintも満たす。対象は有限区間の閉じた系で、非停止runの永久動作は要求しない。

**必要な仮定。** 固定EOS、輸送係数、hydrodynamic frame、正エネルギーとentropy条件、有限initial driver energy、speed<c、Einstein constraints、smooth initial data。BDNK等の既知のcausality/hyperbolicity条件に加え、選んだdriverとの結合について同じ条件が維持される必要がある。compact正密度背景を単にflat time-symmetric初期計量へ載せてconstraintを無視しない。時間・観測frameをmatter clock等に対して定義する。

**既知の定理。** [R1,R2：本文](family376-fluid-gr-bridge-audit.md)のEinstein–viscous-fluid双曲性／局所存在の枠組み。F04のshear program。任意の追加driverを含めた本系の局所存在まで既知とは主張しない。

**未解決部分。** constitutive lawとdriverの選択、constraint解、非potential forceの実現、driverとの結合によるhyperbolicity、相対論・重力補正のbound。外力の任意指定から閉じたsourceへの最初の未完成な矢印である。

**数値検証。** 選んだdriverで \(\nabla(T_{\rm fluid}+T_D)\) とconstraint residualを評価し、収束試験・energy accountingを行う。物理的worldtube内で

\[
\|u_{\rm fluid}-U\|_{C^1([0,T]\times\Omega)}<\varepsilon,
\quad \sup_{0\le t\le T}E_\Sigma(t)<E_{\max}<\infty
\]

を目標にする。Eは指定normalに対する全matterの切断energyであり、非定常compact時空の一意な保存ADM energyではない。interval bounds／解析評価でGronwall errorが決めたdetector marginより小さいことまで示す。fを逆算して貼り付けるだけの計算は不合格。

**Lean形式化。** 最初はenergy・constraint・error budgetの代数と有限shear composition。full BDNK–Einstein existenceの形式化は本PRの範囲外。

**成功の意味。** 自由な外力という仮定を、有限区間の閉じた物理sourceに置き換える最初のbridgeが得られる。任意長計算、CTC、量子場の存在はまだ従わない。

**失敗の意味。** 指定driver／EOS／資源上限のgateが実現できない。すべての相対論的計算を禁止したことにはならない。

## R2 — 無限精度と有限資源を分離するcompiler誤差予算

**定式化。** F06の \(\epsilon_n=b^{-(N+1)2^{(n+3)^2}}\) と、F03/F09のgapped tapeを別々に解析する。各stepでrecordのmargin \(d_n\)、輸送mapのLipschitz bound \(L_n\)、driver／初期位置誤差 \(\eta_n\)、実行時間 \(T_n\)、仕事 \(W_n\) を計算し、soundnessとcompletenessの両方を保証する不等式を作る。F07の速度detectorには、固定閾値に加えてforcingの大きさ／support半径を資源として含める。

**仮定。** どのnormで摂動するか、finite arithmeticの誤差モデル、noiseの確率分布またはdeterministic bound、固定した観測apparatusを先に決める。発散していないcoordinate amplitudeだけを資源と数えない。

**既知。** Familyの全点routingと有限時間安定評価、ODEのGronwall、エネルギー恒等式。本PRで5292例の有理tape更新とscaleの検算を提供。

**未解決。** 指定noise classで全段を保証する \(\exists\eta>0\forall n\) 型定理、あるいはその非存在。原稿のexact-data universalityはその定理ではない。

**数値。** 有理・区間演算で有限prefixを検査可能。非常に小さい \(\epsilon_n\) は対数で扱い、underflowした零を成功にしない。有限prefixの成功から無限runへ外挿しない。

**Lean。** radix tail bound、affine update、finite product誤差、量化記号を区別したconditional transferが候補。今回のLeanは具体的compilerを移植していない。

**成功／失敗。** 実装ごとの必要precisionと資源scaling、限定したrobustness theoremまたはno-goが得られる。特定schemeの一様誤差耐性の失敗は、Familyのexact-data定理や他のuniversal PDEを否定しない。

## R3 — CTCより先に、trapped-surface detectorへの還元を試す

**定式化。** 有限記述zから、計算recordとcollapse triggerを含む合法なEinstein–matter初期データ \(C(z)\) をeffectively構成し、指定classの発展で

\[
\operatorname{Halts}(z)\iff
\exists\text{ smooth closed two-surface }S:\theta_+(S),\theta_-(S)<-\delta
\]

を目標にする。\(\delta>0\) は指定normalizationで固定したmargin。計算flagからmetricのtopologyをoracleで選ぶ方法は許さない。

**仮定。** R1の閉じたdriverとR2の誤差制御、拘束を満たすdata、許容matter class、解のregularity、初期trapped surfacesの排除、record以外からのaccidental collapseを排除する条件。

**既知。** null expansionsとtrapped surfacesのGR幾何、MGHDの枠組み。本監査は新しいhalt–collapse同値定理を発見したとは主張しない。

**未解決。** 全入力のeffective total compiler、非停止側のfalse positive排除、任意長計算を維持するresource class。trapped surfaceからの特異点定理には別のエネルギー・大域条件が必要で、CTCとは同値でない。

**数値。** 有限の停止／非停止prefixについてEinstein constraints・expansions・marginの収束を検査できる。永遠の非停止側を有限計算だけで保証できない。

**Lean。** generic many-one transferは今回提供済み。具体的なgeometry predicateとeffective data constructionは未実装。

**成功／失敗。** 全条件が成立すれば、その指定classのtrapped-surface eventに関するundecidability theoremになる可能性がある。CTC theoremではない。失敗ならdetectorかsourceを見直し、GR一般の判定可能性を断定しない。

## R4 — KRW-aware compiler guardの具体化

**定式化。** `halt -> compactly generated horizon`を目指す任意の候補に、initial GH領域、partial Cauchy面、generator、compact imprisonment、global KG bisolution extension、初期Hadamardのcertificate欄を設ける。全仮定が通れば、全入力regularという仕様を論理guardで拒否する。

**仮定。** KRWに必要なsmoothness／場のclass等を維持する。thin shell、特異境界、nonlocal principal operatorは勝手に同じclassとしない。normがnullになっただけでCauchy horizonと判定しない。

**既知。** KRW Theorem 2/2′、repoの個別NUT null-return。今回の `no_regular_horizon_compiler` は仮定を入力として矛盾を導く。

**未解決。** 実際の新しいfluid-driven geometryに対するcertificate。KRW適用外の場合はbad null-returnやpolarized hypersurfaceを別に検査し、成功扱いにはしない。

**数値。** generator探索は仮説生成に使える。compact generationや全点Hadamard failureを有限sampleから証明できない。幾何certificateには解析／厳密区間評価が必要。

**Lean。** 本PRのlemmaが担当するのは論理的合成のみ。KRW自体と幾何certificateの形式化は未実施。

**成功／失敗。** 成功ならその候補の同時仕様を棄却できる。普遍計算や全CTC時空の禁止ではない。certificate不成立はKRW非適用／未判定であって、候補の存在証明ではない。

## R5 — 有限prefixのHadamard・RSET・noise・backreactionの同時制御

**定式化。** R1の有限時間GH背景から出発し、指定したfree KG場とpositive Hadamard初期stateを置き、同じgでpoint-splitting RSETを作り、fluid・driver・quantum stressを含むSCEEを解く。指定したsmooth detector smearing fと符号margin dに対して、metric correctionとnoise-induced readout errorがdより小さいことを目標にする。

**仮定。** 固定renormalized \(G,\Lambda,\alpha,\beta\)、場種・coupling、initial Wのpositivity/CCR/Hadamard、物理的smearing scale、semi-classical expansion regime。quantum fieldとdriverが相互作用するなら、自由場のseparate conservationをそのまま使わずcoupled theoryを定義する。

**既知。** GH上のHadamard/Wick量の枠組み、coherent smooth shift、noise kernel。対称cosmologyのSCEE局所存在を、このinhomogeneous系全体の既知定理として引用しない。

**未解決。** 同じg・Wでの非局所feedback、driver結合、finite countertermを固定した解の存在と誤差bound、揺らぎ下のrecord安定性。mean RSET有限とnoise小の両方が必要。

**数値。** 有限mode・smearing・point-splittingの収束と保存則、constraint residual、noise boundsを順に検査。cutoff依存を隠さず、有限mode positivityをcontinuum positivityに代用しない。

**Lean。** covarianceの有限次元positivityやsmearingの代数は候補。continuum QFT＋Einstein solutionは今回形式化していない。

**成功／失敗。** 成功なら有限prefixがその半古典classで成立する。無限runもCTCも自動的には従わない。失敗は指定背景・state・smearing・regimeの限界であり、量子場がすべての計算を停止させるという結論ではない。
