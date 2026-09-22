# Heterotic Taub–NUT：過去への情報送信に必要な6条件の監査

**監査日：2026-09-23。結論：6条件すべての成立は示せていない。**  
**Operational closed timelike signalling は未実証。時間遡行一般の不可能性の証明でもない。**

読取基点：`main` の `0a3d64f542e81e3f00a8fafb89c8986d3914207e`（PR #4 マージ後）。
計算は [chronology_six_gate_checks.py](../src/symbolic/chronology_six_gate_checks.py)、実行結果は [JSON](data/chronology_six_gate_checks.json)。条件付き因果補題は [ChronologySixGate.lean](../src/lean/ChronologySixGate.lean)。

このノートは以前の `explicit-brst-state`、`transmission-amplitude`、`time-travel-decision` 各ノートの無条件な D3/D4 PASS 解釈を採用しない。過去の文章は監査履歴として保存する。先の [interaction audit](heterotic-taubnut-interactions-backreaction-return.md) と [supplement](heterotic-taubnut-interactions-backreaction-return-supplement.md) による訂正を引き継ぎ、さらに具体的な状態式の反例と **Taubの時間発展** を計算した。

## 0. 一目で分かる判定

| 条件 | 今回の判定 | 実際に分かったこと／残るもの |
|---|---|---|
| 1. 完全なBRST cohomologyの物理状態 | **未成立** | 異常相殺・ゲージ電荷・共形ウェイトの算術は再現。完全な非対称heterotic複体、補助場の左右接合、superconformal BRSTまでは構成していない。 |
| 2. 正ノルム・正常化可能 | **スカラー診断では部分成立、弦では未成立** | Taubの有限時刻には正で有限のKGノルムを持つスカラーモードを置ける。外側の単色径方向モードの素朴なL²積分は対数発散。どちらも物理的BRST内積の代用ではない。 |
| 3. full string spectrumに含まれる | **未成立** | 全射影・GSO・電荷格子・大域的gluingは未確定。Fableの特定のSU(2) descendant式は一般の巻き数で誤りと確認。 |
| 4. backreaction込みで維持 | **指定スカラー準備に条件付き障害** | 正則な有限時刻データから、選んだ未来地平面で非正則になる成分が生成される例を計算。ただし、その成分をゼロに調整した解もあり、全状態の排除にはならない。連立した弦背景の応答は未計算。 |
| 5. NUT到達と因果構造 | **アクセスと構造変更を分離** | 固定背景ではCTCは既にある。到達しても近似上は計量を変えない。有限固有時間のCTCは書けるが、実際の物理状態の到達・動的な因果構造変更は未確立。 |
| 6. 選択した情報を過去へ送る | **未成立／限定的な経路は禁止** | 完全な延長でなおchronalな過去の受信点へは、通常の因果的経路で戻れない。既にCTC領域内にいる受信者への制御可能な量子信号は未計算。 |

**`0.998130316…` は指定した外側スカラーODEの流束比であり、過去への送信成功率ではない。** CIが緑になることも6条件の物理的成立を意味しない。

## 1. 問いの定義と、計算に固定した入力

調べる対象はJohnson–Svendsenの非回転heterotic coset [S1]。背景の世界面記述およびそこから抽出される幾何はあるが、幾何の厳密性を、投入する弦の物理状態・全相互作用・全genusの制御と同一視しない。元論文自身もprobeに対する応答を別の計算としている。

入力するstring-frame計量・dilatonは、局所的な角度ゲージで

```math
p=x^2-1,\qquad D=(x+\delta)^2-\frac{4p}{k+2},\qquad K=(k-2)\alpha'>0,
```
```math
ds^2=K\left[\frac{dx^2}{p}-\frac pD(dt-\lambda\cos\theta\,d\phi)^2
+d\theta^2+\sin^2\theta\,d\phi^2\right],\quad
\Phi=\Phi_0-\tfrac14\log D,\quad t\sim t+4\pi\lambda.
```

以下では `k=8, δ=√(8/5), λ=√(2/5), ω=√10/2, Λ=1`。`|x|<1` がTaub、`x>1` が第一NUT領域。**Taubではxが時間、tは空間的な周期座標**である。外側領域の二端点の散乱計算だけでは、Taubでどの初期状態を準備したかは決まらない。

操作的送信を、送信イベントAで選ぶ設定 `b=0,1` による、受信イベントBの無条件の測定分布の差として定義する。比較する二実験は、設定選択以前の許容された準備と、時空／場の大域的な接続規則を共有する。送信後の結果によるpostselectionや、設定ごとに過去の境界データを取り替えることは信号に数えない。

```math
\Delta_B=\frac12\sum_y\left|P(y_B\mid\operatorname{do}(b=0))
-P(y_B\mid\operatorname{do}(b=1))\right|.
```

必要なのは `Δ_B>0`、適切なBRST／ゲージ不変の受信観測量、正規化された確率、同じ実験室の時計でBがAより前であること。周期的なtの位相が一周して一致するだけでは、この条件を満たさない。

## 2. 条件1：BRST――再現した算術と、証明していない同一視

旧候補の入力は

```math
(k_1,k_2)=(8,4),\quad(Q_A,P_A)=(2,0),\quad(Q_B,P_B)=(2,1),
```
```math
j=\tfrac12+\tfrac i2,\quad\ell=1,\quad
m=-2,\quad\bar M=\tfrac{\sqrt{10}}2,\quad\bar N=-1.
```

[S1, 式(13)] の異常相殺式の残差は3本とも厳密に0。ゲージ電荷も `m+δ Mbar=0`、`λ Mbar+Nbar=0`。先行ノートの電流規約と補助場減算を仮定すると

```math
K_L=K_R=\begin{pmatrix}8&4\\4&5\end{pmatrix},\quad
h_{\rm num}=\frac1{12}+\frac13=\frac5{12},\quad
\frac12J^TK^{-1}J=\frac5{12},\quad h_{\rm formal}=0.
```

これは実行可能な必要条件の整合性検査である。**この減算が許された左右補助場状態と正しい全Hilbert空間に実現されることは、式の相殺からは証明できない。**

相対AbelianゲージBRST複体を適切に固定し、許容状態を非負のoscillator gradeのFock表現で構成できる場合、grade 0・ghost number 0の閉じた状態に、grade 0・ghost number −1の前像がないという議論は有効になり得る。しかし、それは指定した複体内部の議論であり、正しい大域セクター、全supercurrent、string BRST、物理的内積まで自動的に決めない。

[S2] はBRST–coset対応の有力な方法であり、Abelianの場合の先行結果にも言及する。一方、そこで扱う表現・群・補助状態の仮定を無視してよいわけではない。[S3] は別の非コンパクトcoset族でBRSTとGKOによる結果の差を明示する。この定理は今回のprincipal-continuous／非対称heterotic模型を否定しないが、**compact模型や親AdS3の定理 [S4] を、そのまま完全な証明として転用することを許さない**。

現時点で不足しているのは、実際のゲージ・reparametrization・superconformal ghostを含む複体、許容される補助電荷と左右接合、ノルムを保つcohomologyの実現である。今回はその全構成を得ていない。従って旧候補は**条件付きの代数的vertex候補**のまま。存在も不存在も全理論については決めていない。

## 3. 条件3の具体的な反例：FableのSU(2) descendant式

Fableノート§3は、even spectral flowに関して

```math
(\bar K^+_{-1})^{k_2w}|0\rangle
```

を重み `k₂w²` のflowed vacuumとして記している。これは一般の整数wには正しくない。

まず `[L_0,K^+_{-1}]=K^+_{-1}` だから、この演算子の文字どおりのgradeは `k₂w`。`k₂=4,w=2` では **8であって16ではない**。

さらに、`E=K^+_{-1}, F=K^-_1` と置くと

```math
[F,E]=k_2-2K^3_0,\qquad
F E^n|0\rangle=n(k_2-n+1)E^{n-1}|0\rangle,
```
```math
N_0=1,\qquad N_n=\|E^n|0\rangle\|^2=n(k_2-n+1)N_{n-1}.
```

`k₂=4` のn=0,…,8について `N_n=[1,4,24,144,576,0,0,0,0]`。可積分真空表現では `E^5|0>=0` のnull vectorを商で除くので、w=2に対応するとされた `E^8|0>` 自体がゼロになる。これはスクリプトが検証する具体的な反例である。

**何を否定しないか。** even spectral flowが同じ可積分表現クラスへ移ることまで否定したわけではない。正しい代表は複数の異なるmodeを必要とし得る。比較文献 [S5, App. D.26–D.29] にもその構造が見えるが、そちらの超対称模型の式をheterotic模型へそのまま移してはいけない。また、この誤りは巻き数を導入しない旧 `j=1/2+i/2` 候補の算術を反証するものではない。

従って「Fableの全結果が誤り」ではなく、**この特定の式は物理状態の存在を示す証拠から除外する**。Hopf fibreの可縮性はトポロジカルなwinding保存則の不存在を支持するが、holonomy、global quotient、full BRSTの同一視まで単独で証明しない。

## 4. 条件2：どのノルムを計算したのか

### 4.1 外側の単色波は素朴な径方向L²ではない

与えた背景から作る中性dilaton-weightedスカラー方程式は

```math
(pR')'+(\omega^2D/p-\Lambda)R=0.
```

旧外側散乱解を `u=(x-1)/2` とunit incident fluxで正規化すると、遠方で

```math
R\sim u^{-1/2}\left(r u^{i/2}+u^{-i/2}\right),\qquad
\mathcal R=|r|^2=0.0018696839355381227\ldots.
```

従って

```math
\int^{u_{\max}}dx\,|R|^2
=2(1+\mathcal R)\log u_{\max}+O(1),\quad
2(1+\mathcal R)=2.0037393678710762454\ldots.
```

干渉項の対数振動は有界積分を与える。これは**指定したスカラー径方向積分**の非可積分性であって、一般化された散乱状態やBRST内積の不存在ではない。delta正規化された状態を直ちに排除してはいけない。

### 4.2 Taubの有限時刻には正で有限のスカラーKGノルムがある

未来をx増加方向に選ぶ。Taubの有限時刻切片は空間的S³である。`q=λω=1, ℓ=1, m_phi=0` のmonopole-harmonicは局所表示で `Y∝e^{-iωt}sinθ` と書ける。角度ゲージの接合と `2λω=2` は整合し、角度方程式の固有値はΛ=1、`∫₀^π sin³θ dθ=4/3`。

`x=tanhη` とし、座標測度でYを正規化する。全体の正の定数を吸収すれば、場 `Φ=K^{-1/2}Yv(η)` のKG内積は

```math
(\Phi,\Phi)_{\rm KG}=i(v^*\dot v-v\dot v^*).
```

任意の有限η₀で `v₀=1/√(2Ω₀), vdot₀=−iΩ₀v₀` とすれば **KG norm=1**。空間切片もコンパクトなので、この単一スカラーモードは有限の初期ノルムを持つ。

ただしKG積は全解空間で正定値ではなく、正のモード部分空間を選んでいる。一つの正ノルムモードは、全量子状態のHadamard条件・全弦のno-ghost theoremを意味しない。

### 4.3 旧wavepacketの主張への制約

旧電荷を固定して `j=1/2+is` だけ変えると、仮定した減算規約では

```math
h_{\rm coset}(s)=\frac{s^2-1/4}{6}.
```

spectatorの重みを `p_Y²/2` として質量殻を保つには `p_Y²=(1/4-s²)/3` が必要。spectatorがコンパクトならpYは自由な連続変数ではない。従って「近傍のsを任意に重ねて正常化できる」とは、電荷格子と全質量殻を解かずには言えない。非コンパクトspectatorを追加するなら模型の追加仮定として明記する必要がある。

## 5. 新計算：外側の散乱ではなくTaubの時間発展

### 5.1 時間依存振動子への正確な変換

`x=tanhη` とすると、前節のスカラー方程式は

```math
\ddot v+\Omega^2(\eta)v=0,\qquad
\Omega^2=\omega^2D-\Lambda p
=6+2\sqrt{10}\tanh\eta+\tfrac12\tanh^2\eta.
```

漸近周波数は

```math
\Omega_- =2-\omega>0,\qquad\Omega_+=2+\omega,\quad\omega=\sqrt{10}/2.
```

これは正しいTaub時間での方程式であり、外側径方向ODEの相反性を時間発展と読み替えたものではない。ただし依然として中性スカラー診断であり、exact string correlatorではない。

### 5.2 有限時刻の正則準備から未来基底へ

`z=(1-x)/2`, `h=−1/2+i/2`, `α=iΩ₊/2`, `β=iΩ₋/2` とし

```math
F_+(z)=z^\alpha(1-z)^\beta\,{}_2F_1(a,b;c;z),\quad
 a=\alpha+\beta-h,\ b=\alpha+\beta+h+1,\ c=1+2\alpha.
```

`F₊∼e^{-iΩ₊η}` なので `u_out=F₊/√(2Ω₊)` はKG-unitの未来正周波数基底になる。これは後述の選択した未来延長で正則な枝に対応する。

前節の有限時刻初期データを

```math
v=\alpha_0u_{\rm out}+\beta_0u_{\rm out}^*,\qquad
|\alpha_0|^2-|\beta_0|^2=1
```

に分解した結果は次の通り。

| 準備時刻η₀ | 瞬間的正周波数データから生じる `|β₀|²` |
|---:|---:|
| 0 | 0.002668579603463413898 |
| 1 | 0.000093652834906026110 |
| 2 | 0.000001938930118047611 |
| 4 | 0.000000000663577393156 |

「瞬間的正周波数」はここでの明示的な初期データ選択であり、唯一の真空や全場のHadamard状態を指定したという意味ではない。

逆に有限時刻のデータを `u_out(η₀), udot_out(η₀)` に取れば、**β₀=0の調整された解**を得る。この対照例があるため、混合の存在から全許容状態の不可避な破綻を結論してはいけない。50桁／80桁計算でこのゼロの残差はそれぞれ約10⁻¹⁰⁵／10⁻¹⁶⁴（絶対値二乗）であり、物理的な微小生成率ではなく数値丸めである。

### 5.3 Taubの過去漸近基底から未来漸近基底へ

今度は `α=iΩ₊/2, β=−iΩ₋/2` を使い、`c_in=1+2β` とする。

```math
u_{\rm in}=\frac{z^\alpha(1-z)^\beta}{\sqrt{2\Omega_-}}
 {}_2F_1(a,b;c_{\rm in};1-z).
```

Gaussの接続公式 [S6] から

```math
\alpha_B=\sqrt{\frac{\Omega_+}{\Omega_-}}
 \frac{\Gamma(c_{\rm in})\Gamma(-2\alpha)}
 {\Gamma(c_{\rm in}-a)\Gamma(c_{\rm in}-b)},\qquad
\beta_B=\sqrt{\frac{\Omega_+}{\Omega_-}}
 \frac{\Gamma(c_{\rm in})\Gamma(2\alpha)}{\Gamma(a)\Gamma(b)}.
```

具体的に

```math
|\beta_B|^2=
\frac{\cosh[\pi(\omega-1/2)]\cosh[\pi(\omega+1/2)]}
 {\sinh[\pi(2-\omega)]\sinh[\pi(2+\omega)]}
=0.077615394080350761309\ldots,
```
```math
|\alpha_B|^2=1.077615394080350761309\ldots,
\qquad |\alpha_B|^2-|\beta_B|^2=1.
```

スクリプトはGamma関数の算術だけでなく、`z=0.15,0.4` で接続した関数自体の等式を検算する。これが今回の**Taub時間のmode mixing**である。元の外側流束比 `T_radial=0.998130316…` とは異なる観測量。`|β_B|²` も送信成功確率ではないし、この単一モード計算で弦全体の粒子生成率を求めたわけでもない。

## 6. 条件4：どの準備が地平面で危険になるか

### 6.1 観測者の座標特異性と区別する

`dr_*/dx=√D/p` とし、未来向きにTaubからx>1へ出る**outgoing延長**で `q=t-r_*` を使う。径方向計量は

```math
ds_{\rm fib}^2=K[-pD^{-1}dq^2-2D^{-1/2}dq\,dx].
```

これはx=1で非退化。`d=1+δ` とすると `r_*∼(d/2)log|x−1|`。前節の未来正周波数枝は `e^{-iωt}z^{iΩ₊/2}∼e^{-iωq}` で、選択した地平面で正則。

一方、同じt依存を持つ反対の径方向枝は

```math
\Phi_{\rm bad}\sim B_s e^{-i\omega q}|x-1|^{-i\Omega_+},\qquad
|\partial_x\Phi_{\rm bad}|^2\sim
\frac{|B_s|^2\Omega_+^2}{(x-1)^2}.
```

従って、前節の明示的な有限時刻準備で得たβ₀≠0を使うと、**そのスカラーtest solutionには、選択した未来延長で非正則な枝が実際に含まれる**。単なる加速した静止観測者の周波数発散ではなく、正則チャートでの場の微分の非有界性である。一般の横断する観測者の局所エネルギーもこの成分に感応する。

これは固定背景上のスカラー近似を地平面まで一様に制御できない例である。任意の小さな非ゼロ振幅でも極限では問題になるが、その大きな局所エネルギーへ低エネルギー応力式を無制限に外挿して、厳密な弦理論の曲率発散を証明したとはしない。

### 6.2 不変量での二流体診断と例外

二つのnull流束があると仮定した局所モデルでは、既存監査と独立の代数検算で

```math
T_{ab}=A\ell_a\ell_b+B n_an_b,\qquad
T_{ab}T^{ab}=\frac{8AB D^2}{K^2p^2}.
```

A,Bの地平面極限が非ゼロなら `(x−1)⁻²` の増大。この式のA,Bは仮定されたbeam係数であり、今回のcoherentモードを無条件に二つのincoherent流体へ置き換えない。実際の量子的sourceには別の計算が要る。

調整されたβ₀=0の解は上の非正則枝を欠く。従って、**「全状態が必ずbackreactionで破壊される」は未証明**である。逆に、一つの正則枝も全場の量子状態の健全性を保証しない。KRW [S7] の量子二点関数に関する仮定と結論は、単一の古典解より強い。

### 6.3 波束の減衰に必要な速さ

非正則な枝に沿うパラメータを `v_bad=−d log|x−1|+const→+∞` とすると、包絡fの微分は `∂_x f=−d f'(v_bad)/(x−1)`。有界性に必要な条件は

```math
f'(v_{\rm bad})=O(e^{-v_{\rm bad}/d}),\qquad
\gamma\ge\frac1{1+\delta}=0.441518440112252888\ldots
```

（`f'∼e^{-γv_bad}` の場合）。べき減衰では不足する。一方、被覆空間でコンパクトな包絡ならこの局所問題を避け得るが、時空の同一視とcompatibleかを確認しなくてはならない。**周期的なf'が同時に無限遠でゼロへ減衰するならf'は恒等的に0**。固定角度の周期的な非正則成分を、単なる局所的な振幅調整だけで一般に救うことはできない。

この議論も「全ての弦の波束がその成分を持つ」という主張ではない。角度・周波数セクター・射影・相互作用から、その成分が本当に生成されるかが次の問題になる。

### 6.4 full backreactionで未計算のもの

`g_s=g_0D^{-1/4}` は第一NUT領域で小さく保てるが、relative boostの大きな相互作用やgenus係数を一様に抑えるとは限らない。必要なのは、背景多重項 `F=(g,B,Φ,A)` の全方程式と正しいsourceによる

```math
\frac{\delta\mathcal E_I}{\delta F_J}\,\delta F_J
=\mathcal S_I[\Psi]
```

などの自己無撞着な応答である。今はsourceを決めるexact cosetの結合・tadpole・物理的準備が不足している。スカラーの発散を真空Einstein方程式へ入れるだけでは、このheterotic模型のfull backreactionを解いたことにならない。今回、それは解けていない。

## 7. 条件5：「アクセス」と「因果構造を変える」は別の要求

固定背景近似は定義上δg=0。NUTへのアクセスが成立しても、それだけで光円錐やCTCの有無を変えるわけではない。**既存のCTCを使うために、因果構造を新たに変えることは必須条件ではない。** 動的な形成を求めるなら別途、初期値問題とbackreactionが必要になる。

好材料も保存する。入力計量でx=2、角度固定のt周期軌道はtimelikeで、α'=1なら

```math
\tau_{\rm loop}=4\pi\lambda\sqrt{Kp/D}=10.9632346614953\ldots,
```
```math
a^2=\frac p{4K}\left(\frac{p'}p-\frac{D'}D\right)^2
=0.08245675506693\ldots.
```

どちらも有限。これは**その背景が既に存在し、制御できるtest bodyが利用可能だと仮定した運動学**であり、CTCを禁止する幾何学的証明にはならない一方、弦による情報送信の実演でもない。

従って条件5は、(5a) 物理状態の到達・利用可能な因果経路と、(5b) 準備による背景の因果構造変更に分ける。(5a)は完全な物理状態からの接続が未完成、(5b)は未計算。固定幾何の存在自体は [S1] の既知結果である。

## 8. 条件6：受信者をどこに置くかで結論が違う

### 8.1 同じ未来地平面を逆向きには渡れない

§6のoutgoing延長で未来向きnull生成ベクトルを `n=∂q` とする。x=1で未来向き因果ベクトルvについて

```math
g(v,n)=-\frac K{1+\delta}v^x\le0\quad\Rightarrow\quad v^x\ge0.
```

従ってTaubから出た**同じ**未来向きinterfaceを、過去のTaub実験室へ向けて逆横断できない。別の延長や別の地平面を使う経路までこの局所式だけで排除はしない。

### 8.2 完全な時空でchronalな受信点への帰還の禁止

`B≪A` を実験室の通常のtimelike経過、`A≤B` を送り返すcausal pathとする。滑らかなLorentz時空のpush-up性より

```math
B\ll A\ \land\ A\le B\quad\Rightarrow\quad B\ll B.
```

従って、受信点Bが**使用する完全な時空延長において** `B≪B` ではないなら、その帰還経路は存在しない。chronology-violating集合の定義は [S8] を参照。単に「当初はchronalだった局所パッチ」という意味では足りない。

さらに物理信号のsupportがmetric-causalな到達関係の内側にあると仮定すれば、同じ結論が信号に適用される。**このsupport性が今回のfull string theoryで成立すること自体は、ここでは証明していない。**

この論理だけをLeanにした。`receiver_on_ctc`, `no_causal_return_to_chronal`, `no_signal_to_chronal_past` の3補題は、push-upとsignal supportを明示した仮定として受け取る。Lean 4.19.0のkernel checkに成功し、`#print axioms`は3本とも追加公理なしを報告した。Lorentz幾何のpush-upの証明も、heterotic理論の因果性も、このファイルが内包しているわけではない。

### 8.3 既にCTC領域にいる受信者は、この補題では除外されない

BがNUTのchronology-violating部分にあれば上のchronal仮定は成立しない。そこで§1の `Δ_B>0` を実際に作るためには、実験室のworldline、受信時計、送信操作の二つの選択、両方に許された同じ準備、全量子論の確率規則が必要となる。

今回のODE流束、Bogoliubov係数、周期位相、素朴なCTC軌道のいずれも、このsender-controlled応答を計算していない。**ここに非ゼロの通信確率を代入してはいけない。** 正規化されたretarded／relationalな応答が得られない現状で、条件6は未成立のままである。

## 9. 先行研究の使い方と、採用しなかった飛躍

| 文献 | この監査で使用する内容 | 使用していない強い主張 |
|---|---|---|
| [S1] exact heterotic Taub–NUT | 幾何・dilaton・異常式・probe問題との区別 | 全genusの安定性や送信可能性の保証 |
| [S2] gauged-WZW BRST | 条件を指定したcoset cohomology構成の方法 | 今回の全大域Hilbert空間が自動確定 |
| [S3] noncompact BRST/GKO | no-ghost定理には群・表現・構成上の仮定が必要 | ここで使ったprincipal continuous候補の一括排除 |
| [S4] AdS3 string spectrum | 親SL(2,R)表現・no-ghost問題の比較 | 非対称heterotic quotientへの無条件適用 |
| [S5] compact affine flow | 正しいdescendant構造の比較 | SU(2)の式だけで完全な弦状態を認定 |
| [S6] DLMF | Gauss関数の1−z接続公式 | Gamma係数をそのまま情報通信確率と解釈 |
| [S7] KRW | 指定のCauchy horizonとHadamard二点関数の障害 | 全string theory・全CTCへの普遍的禁止定理 |
| [S8] causality | chronology-violating集合と完全な時空上の因果関係 | initially chronalなら未来の全延長でもchronalという仮定 |

検索は模型名、BRST、spectrum、hyperbolic coset、Taub–NUT、spectral flowを組み合わせた限定検索と一次資料の再読。全論文を網羅した検索や新規性の証明ではない。今回の結果には優先権を主張しない。計算や解釈を既知の一般論へ取り違えず、適用条件を固定した。

## 10. 計算資源・再現方法・CIの意味

```bash
python -m pip install sympy==1.14.0 mpmath==1.3.0
python src/symbolic/chronology_six_gate_checks.py --json /tmp/six-gate.json
lean src/lean/ChronologySixGate.lean
```

ローカル環境はPython 3.13.5、SymPy 1.14.0、mpmath 1.3.0。50桁と80桁の計算を独立に実施し、表示したmixing係数は35桁以上一致。ODEを数値微分して再代入した最大relative residualは約 `6.2e−51`／`2.0e−81`、正規化Wronskian residualは約 `1.1e−50`／`1.7e−80`。これは任意精度浮動小数の検算であり、interval arithmeticによる厳密な誤差証明ではない。

GitHub Actions **Chronology six-gate checks run #1**（run ID `35750693174`、code commit `1a18f6798cc6253291def7b5d642bc8194aede39`）で、Python 3.11、3.12、Lean 4.19.0の3jobのsuccessを確認した。Leanのログでは3補題とも追加公理への依存なし。workflowは計算結果とLeanログをartifactとして保存する。

今回の閉形式と少数のmode検査に大規模なparameter sweepは不要だった。未確定のHilbert空間や相互作用kernelを仮に埋めた巨大計算は、gate判定を改善しないため実行していない。**計算のPASSと物理的な6条件のPASSは別のboolean**として、JSONにも `all_six_physical_gates_passed: false` を保存する。

## 11. 最短の次の研究点

完全な6条件を通すために残るのは、まず非対称cosetの大域的状態構成と物理内積を固定し、具体的vertexをその中で認定すること。次に、そのvertexの正規化された二点・混合三点／四点関数から、準備した状態が未来地平面で非正則成分を生成するかを求める。スカラー計算ではその問題が初期準備に依存すると既に分かった。

そのsourceで背景多重項の応答を解き、最後に許された二つの送信設定について **同じ準備から** `P(y_B|do(b))` を算出する。受信点をchronalな元の実験室に置く案なら§8の因果補題を回避する物理的根拠も必要になる。NUT内に置く案なら、その補題ではなく測定・自己無撞着性・情報制御の問題を解かなくてはならない。

**到達点は「全部YES」ではない。** 一つの不正確な状態代表を具体的に除外し、Taub時間の準備依存の不安定化候補を計算し、許されない帰還経路を条件付きで明確化した。現存するCTC幾何を実験可能な情報通信装置へ昇格させる証明はまだなく、同時に全ての状態・全ての受信者に対する不可能性も示していない。

## 参考文献

- **[S1]** C. V. Johnson, H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, Phys. Rev. D **70**, 126011 (2004). [hep-th/0405141v3](https://arxiv.org/html/hep-th/0405141v3), 特に§3、式(13)・(14)・(72)–(79)、§4。
- **[S2]** S. Hwang, H. Rhedin, *The BRST Formulation of G/H WZNW Models*. [hep-th/9305174v3](https://arxiv.org/html/hep-th/9305174v3), 特に§2–3とAbelian構成への言及。
- **[S3]** J. Björnsson, S. Hwang, *On the unitarity of gauged non-compact WZNW strings*. [0710.1050v4](https://arxiv.org/pdf/0710.1050v4), abstractと仮定を指定したno-ghost／BRST–GKO比較。
- **[S4]** J. Maldacena, H. Ooguri, *Strings in AdS3 and the SL(2,R) WZW Model. Part 1: The Spectrum*. [hep-th/0001053](https://arxiv.org/abs/hep-th/0001053).
- **[S5]** A. Dei, A. Sfondrini, *Integrable spin chain for stringy Wess–Zumino–Witten models*. [1806.00422](https://arxiv.org/pdf/1806.00422), App. D.26–D.29（比較模型のdescendant）。
- **[S6]** NIST Digital Library of Mathematical Functions, [§15.8 Transformations of Variable](https://dlmf.nist.gov/15.8), 通常のGauss関数と正規化されたboldface関数の区別に注意。
- **[S7]** B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*. [gr-qc/9603012v2](https://arxiv.org/html/gr-qc/9603012v2), Theorem 2。
- **[S8]** E. Minguzzi, *The boundary of the chronology violating set*. [1603.08190](https://arxiv.org/pdf/1603.08190), chronology-violating集合の定義と境界の因果解析。
