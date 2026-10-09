# Family 376 定理・資源・形式化台帳

**2026-10-08／原本SHA `adc7f1241b42e322a6451854ab7e4b4c146bf78a`。**

[監査本文](family376-fluid-gr-bridge-audit.md)に対する一次資料台帳。著者は各稿ともOpenAI、日付は2026-09-27。番号はPDFに表示されたtheorem番号。原稿の主張・付属Leanのstatement・本監査が独立に検証した範囲を区別する。

**共通規約。** 方程式は非相対論的incompressible NS、flat componentwise Laplacian。tは実数の非負時間。torusは空間周期境界、R³版は壁なし・無限遠の支持／energy comparison条件を用いる。各稿のzero dataは速度に関する条件であり、装置・物質の初期energy零を意味しない。effectiveとは微分の任意精度評価プログラムと必要なboundが得られることであり、計算量や物理的noiseの一様制限ではない。

## F01. Finite Instructions and Solenoidal Shear Flows

[固定PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/manuscript.pdf) ／ [TeX](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Finite-Instructions-and-Solenoidal-Shear-Flows-September-27-2026/build/main.tex)

**Theorem 1.1。** 単位平坦torus \(\mathbb T^3\)、空間周期境界、\(u(0)=0\)、任意の固定positive computable \(\nu\)。\(p=0\)、\(f\)は発散零・空間平均零、\(u,f\)の全mixed derivativeが全時間で有界。\(t\ge1\)で1-periodic、整数時刻の近傍で速度零、kinetic energyは一様有界。古典解comparison classで一意。

初期粒子 \(a=(1/8,3/8,1/2)\)、固定strip \(1/2<x_1<1\) への到達 iff halt。履歴を保持する有限recorder、gapped tape、reciprocal affine平面命令、solenoidal shearによる実装。inputはloading、反復部はmachineに依存する。外力装置・有限precision・総投入仕事の定理はない。

PDF SHA-256: `0cdc2abd5b1a3d152fe55f7793ccc3f49ec6e7a79d0f5b4893e10c1b2c061e8d`

## F02. A Fixed Particle Test for Computation in a Forced Viscous Flow

[固定PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/manuscript.pdf) ／ [TeX](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow-September-27-2026/build/main.tex)

**Theorem 1、Corollary 1。** 単位平坦 \(\mathbb T^3\)、空間周期、positive computable \(\nu\)、zero initial velocity。\(f\)はsmoothでmean zero。\(u,f\)のすべての時間・空間微分のsup-normが \(L^\infty_t\cap L^2_t\)。指定した古典解classでglobal smoothかつ一意。solenoidal projectionはvelocityを変えずpressureを変える。

\(a=(1/8,3/8,0)\)、\(1/2<x_1<1\) に入る iff halt。第三座標の履歴 \(z_n=\sum_{i<n}j_i\Lambda^{-i-1}\) を消去せず読む構成とslow scheduling。正確なforce-description class上のparticle testは決定不能という系。\(L^2_t\) boundをeventually stationaryや一様な測定marginに読み替えない。

PDF SHA-256: `87defbd4577b4c8ef80cd148000ffd55e7b3d2ce296d27b04efb16aae92f8c0d`

## F03. Universal Computation with Eventually Stationary Navier Stokes Forcing

[固定PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf) ／ [TeX](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing-September-27-2026/build/main.tex)

**Theorem 1.1（Eventually steady forcing）。** \(\mathbb T^3=(\mathbb R/\mathbb Z)^3\)、flat componentwise Laplacian、mean-zero pressure規約、\(u(0)=0\)。固定positive computable \(\nu\)。\(f\)はsmooth、空間平均零、全mixed derivativeが全時間で有界、**\(t\ge1\)で時間非依存**。明示解はglobal smooth、各有限時間の古典classで一意、kinetic energyは一様有界。基本residual構成は\(p=0\)。Leray projectionでfをsolenoidalにできるがpは変わる。

固定 \(P=(1/4,1/4,0)\)、\(\mathcal O=\{1/32<Y<1/8\}\) へのmaterial trajectoryの到達 iff halt。七行のreversible recording table、別々に分離されたsource/target rectangles（両族間の重なりは許す）、Hamiltonianな抽出・変形・配送、第三座標のmean-zero spatial clock、startup rampを使用。forceの有限formulaは選択runを先に実行しない。

原稿は無限符号化に対するuniform finite-precision toleranceを主張しないと明記。periodic-from-zeroとtime-square-integrable forcingは**別選択**。定常流のbounded kinetic energyは、無限時間の有限総仕事を意味しない。

PDF SHA-256: `0af659c5a6f8e7b07c66d3301055e8a80e616c938ffb6027272e42097374d0d5`

## F04. Geometric Programs for Solenoidal Forcing

[固定PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/manuscript.pdf) ／ [TeX](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Geometric-Programs-for-Solenoidal-Forcing-September-27-2026/build/main.tex)

**Theorem 1.1（particle）と1.2（sheet）を分ける。** 粒子版は単位\(\mathbb T^3\)、positive computable \(\nu\)、\(u(0)=0\)、\(p=0\)。fはsmooth・mean zero・solenoidal、**時刻0から1-periodic**。全mixed derivativeは有界。shearの順序付けで同時には一成分だけを動かし自己移流を零にできる。\(a=(1/4,1/2,1/4)\)、\(1/2<x_1<7/8\) がhalt detector。

sheet版はside length 10の \(\mathbb T_{10}^3\)。有限な有理rectangle族、source内／target内はそれぞれ分離、source-targetの重なりは許す。正の対角affine mapをsource sheetの**全点**に実現する。平面の面積変化は第三方向で補償するため、任意の非単位determinantを持つsolid-volume mapを許すのではない。

現selected Lean comparatorは**sheet theorem**。このentryだけで同稿のfixed-particle halting detectorやすべてのsolid-box関連命題まで形式検証済みとはしない。

PDF SHA-256: `1e54090582721ee2edcecf924b7c6176b8f6e3a5c037d861e6e6befb2cb6ba17`

## F05. Prefix Instructions and Incompressible Flows

[固定PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/manuscript.pdf) ／ [TeX](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Prefix-Instructions-and-Incompressible-Flows-September-27-2026/build/main.tex)

**Theorem 1.1（interspersed histories／moving sheets）。** 単位\(\mathbb T^3\)、空間周期、positive computable \(\nu\)、zero initial data。constructed \(p=0\)、mean-zero smooth force。速度と外力の全mixed derivativeが有界、\(t\ge1\)で1-periodic、kinetic energy一様有界、古典comparison classの一意性。

\(a=(1/8,1/4,1/4)\)、\(1/2<x_1<1\) への到達 iff halt。有限prefix instruction、履歴、moving sheetsを用い、二次元変形の面積をnormal scalingで補償する。inputはloadingへ分離する。53頁に含まれる他のvariantは、上記の支持条件・detector・時間プロファイルと自由に合成できるものではない。

PDF SHA-256: `8cd581420ec9967ac33296ba4f91342cb275bd63db72d0db630139381d3aa59e`

## F06. Computation under Rapidly Vanishing Navier Stokes Forcing

[固定PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/manuscript.pdf) ／ [TeX](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing-September-27-2026/build/main.tex)

**Theorems 3.1、4.1、5.1は別構成。** 共通して3次元、positive computable viscosity、zero data、smoothな明示解。速度とforceの任意のmixed derivativeが任意の逆時間多項式より速く減衰する。

3.1は\(\mathbb R^3\)のmoving curls。共通の固定compact support \([-2,1]\times[-1,2]\times[-1,1]\)、\(p=0\)、原点の粒子が \(X_1<-1\) に到達 iff halt。4.1は**alternating fractional memories**、\(\mathbb R^3\)、固定compact support、\(p=0\)、\((-1,0,0)\)から \(X_1>0\) を検出。selected Leanは後者。scope文書ではsupportはmachine/inputにも共通とされる。非compact空間の一意性は指定energy comparison classに限る。

4.1の符号は \(b=2(1+\max(|Q|,|\Gamma|))\)、偶数digit、blank=0。\(K_n=N+2n+2\)、\(C_n=(g_q+\xi_n+b^{-K_n}\eta_n)/b\)、\(s_n=(N+1)2^{(n+3)^2}\)、\(\epsilon_n=b^{-s_n}\)。二つの座標がdonorとrecipientを交互に担当し、donorを固定して次のblockを追記する。\(s_{n+1}>s_n+1+2K_n\) が履歴読み出しを分離する。有限時間で無限stepを実行するのではなく、後半で必要precisionが増す。

5.1はtorus上の別lattice方式。\(a=(1/4,1/2,1/2)\)、\(1/2<x_1<1\) がdetector。mean-zero forceのprojection版はpressureが変わる。固定compact支持・rapid decay・fixed macroscopic velocity marginをすべて同時に持つと読まない。

PDF SHA-256: `931c07840228968ba5c7531964bb51266bdfc50915baa7f20b8ce15a57a6c551`

## F07. Velocity Field Detection of Computation in Forced Navier Stokes Flows

[固定PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/manuscript.pdf) ／ [TeX](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows-September-27-2026/build/main.tex)

**Theorem 1.1の二つの実現。** positive computable \(\nu\)、zero initial velocity、\(p=0\)、smoothの指定comparison classで一意。縦速度が横流れによるadvection–diffusionで運ばれるため、単に粒子labelを追うのではなくEulerianな場の観測になる。

**torus**：単位\(\mathbb T^3\)の固定strip \(1/32<Y<1/8\) で、ある時点・点の \(u_3>1/2\) iff halt。fはfixed horizontal compact region×circleに支持を持つ（regionはinstanceに依存してよい）。微分boundは**各有限時間slab**。全時間の一様boundや一様kinetic boundはここでは主張されず、後期の高速stirringを無料と数えてはいけない。

**cylinder**：\(\mathbb R^2\times\mathbb T\)。\(u_3\ge0\)で可積分、\(\int_{\{X_2>0\}\times\mathbb T}u_3>1/2\) iff halt。fの全mixed derivativeは全時間で有界だが、horizontal supportがcompactなのは**各有限時間区間ごと**で、同じ固定compact setではない。全空間での資源を別途数える。

いずれも通常のfixed-threshold eventであるが、force摂動・量子noise・有限装置での全時間robustness定理ではない。fのmean-zero／solenoidal性は両版に無条件で追加しない。

PDF SHA-256: `a69fca6b458f542aefe5d21cd36fef355f37d7b22dc517474304888b847f00bc`

## F08. Scalar Potentials and Slow Clocks for Forced Fluid Computation

[固定PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/manuscript.pdf) ／ [TeX](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation-September-27-2026/build/main.tex)

**Theorem 1.1。** \(\mathbb R^3\)、固定compact support、positive computable \(\nu\)、zero initial、\(p=0\)。任意のj,αについて速度・forceの微分が \(C_{j,\alpha}(1+t)^{-1-j}\) 以下。全mixed derivativeがspace-time \(L^2\)、kinetic energyは有界。比較classは非compact空間用のenergy regularityを含む。

原点粒子が \(X_1<-1\) iff halt。三つのscalar potentialsからcurlで流れを作り、\(\tau=\log(1+t)\)等の遅いがontoなclockで全有限計算時刻へ達する。potentialsは**古典的流体生成関数**であり、quantized scalarやHadamard stateではない。機械的な\(\int|f\cdot U|\)が有限になり得ても、controllerの全energyと有限precisionまで保証しない。

PDF SHA-256: `82005335f0aac60fbd7f84ba2d4aee576671a54cc39b2662e263063e62ac45e1`

## F09. Incompressible Box Transport and Finite Computation

[固定PDF](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Incompressible-Box-Transport-and-Finite-Computation-September-27-2026/manuscript.pdf) ／ [TeX](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Incompressible-Box-Transport-and-Finite-Computation-September-27-2026/build/main.tex)

**Theorem 3.4（balanced box routing）と4.1（balanced three-stack realization）。** 前者は有理solid boxesの有限族間の、正の対角affine、**determinant 1**の写像を、source boxの近傍全体でsmooth compactly supported divergence-free flowに実現する。source同士とtarget同士はそれぞれ分離、両族間の重なりは許す。速度の時間支持は単位区間の中央半分。

後者は\(\mathbb R^3\)、\(u(0)=0\)、\(p=0\)。\(f=f_0+\nu f_1\)、共通compact spatial support、全mixed derivative有界、\(t\ge1\)で1-periodic。\(a=(4,0,0)\)、\(\mathcal O=(-1,2)^3\) へ入る iff halt。任意positive real νでformulaが成立し、computableνでeffective、他はrelative。repeated fieldは入力に依存せずmachineだけに依存してよい。

三stackはwork left/rightとhistory。prefix長の総和を保存する各命令がdet1を保証する。fresh blankをhistoryへ運び、命令recordへ置換して可逆性を保つ。noncompact一意性は\(C_tH_x^2\cap C_t^1L_x^2\)、有限時間のu,∇u有界、pressure modulo time-only constantが\(C_tH_x^1\)であるclass。76頁すべての付随命題を選択された一つのLean theoremと同一視しない。

PDF SHA-256: `ef2428fde699d046033669ce92129753b4e6114617f25e24cdc871a28c3e99b6`

## 10. Leanで何を確認でき、何をまだ再実行していないか

[scope文書](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/376.md)とComparatorChallengesの6設定を直接照合した。**6設定は5個の異なる定理targetに対応**し、2設定が同じbalanced theoremを指す。

| Comparator JSON名 | solution module | theorem target | 射程 |
|---|---|---|---|
| SolenoidalSheetPrograms | OAI.MathematicalPhysics.SheetFlows.SheetProgram | OAI.Solenoidal.sheet_theorem | F04のsheet。fixed-particle halting全体ではない |
| NavierStokesAlternating | OAI.MathematicalPhysics.AlternatingFlow.Development | OAI.AlternatingNS.alternating | F06のalternating memoryとdetector・effectivity・comparison class |
| NavierStokesVelocity | OAI.MathematicalPhysics.NavierStokes.VelocityDetection.Main | OAI.VelocityDetection.main_result | F07のtorus/cylinder両event |
| BalancedBoxRouting | OAI.Analysis.BoxTransport.Routing | OAI.BoxTransport.Routing.balanced_box_routing | F09のsolid-box輸送 |
| BalancedThreeStack | OAI.MathematicalPhysics.NavierStokes.BalancedTransport.MainResult | OAI.BalancedTransport.balanced_three_stack_realization | F09のzero-data fluid halting |
| ForcedNavierStokesComputation | 同上 | 同上 | 別のchallenge名、同じtarget |

各JSONのpermitted_axiomsは `propext, Quot.sound, Classical.choice`。`enable_nanoda=false`。**challenge側の `sorry` は比較用の穴であって、solutionの証明欠落だと即断しない。** 反対に、solutionという名前だけで全依存定義・物理的射程の一致まで認定しない。

直接読んだsolution entry／wrapperには、SheetProgram.sheet_theorem、AlternatingFlow.Main.alternating、VelocityDetection.MainResult.main_result、BalancedTransport.MainResult.balanced_three_stack_realizationがある。後者は具体的finite machine・computable initializer・material flow・NS residual・halt equivalenceを結論に持つ構成的な証明項であり、単に `halt iff detector` を仮定しただけの論理lemmaではない。ただし、その**全推移的依存closureの再構築は未実施**。

本監査で保存したForcedComputationディレクトリには576本のLean sourceがある。しかし選択targetはSheetFlows、AlternatingFlow、VelocityDetection、BalancedTransport等の別ディレクトリへも分かれるため、その576本の検索だけで全証明を確認したことにはならない。旧ForcedComputation内のStationaryMainに定理があることと、scopeのselected comparatorがその稿の全主張を検査することも別である。

upstream toolchainは **Lean 4.34.1**、spacetime-screening既存CIは **Lean 4.19.0**。本PRは巨大なupstream libraryを移植せず、既存環境で動く独立の条件付きlemmaのみ追加する。**upstream全Familyのkernel／comparator再実行はしていない。原稿群の完全独立査読もしていない。** 今回のCI成功はこの制限を解除しない。

### 本監査の証明状態ラベル

| label | 例 | 何を保証しないか |
|---|---|---|
| 原稿の定理／付属形式化statement | F03のfixed particle、F06のrapid memory、F09のbox transport | 本監査の全proof closure検証、物理的装置 |
| 本監査で再検算した恒等式 | 5292個の有理tape更新、shear residual、energy balance、ADM inverse | 無限機械の全compiler、GR solver、量子state |
| 既知結果の条件付き帰結 | 一定散逸の無限総仕事、KRW仮定を満たすregular compilerの矛盾 | 全流体の禁止、無条件の新規no-go |
| 研究仮説／未構成の橋 | 閉じたEinstein–causal-fluid driver、同じgのQFT feedback | 既知定理から自動的に成立するという保証 |
| 現状の類推 | NSのuniversal性から直ちにhalt iff CTC | existence、undecidability、有限資源実現性のいずれも保証しない |

## 11. 時間・空間・エネルギー条件の取り違えを防ぐ比較

| 性質 | 成立する例 | そこからは従わないもの |
|---|---|---|
| eventually stationary forcing | F03 | driver不要、有限総仕事、時間商 |
| fixed compact support | F06、F08、F09 | 有限bits、有限物質rest mass、noise耐性 |
| rapid decay of all derivatives | F06 | 無限回の計算が有限時間で終わる、一様観測gap |
| fixed velocity threshold | F07 | fixed spatial supportかつ全時間uniform derivativesの同時保証 |
| bounded kinetic energy | 多くの粒子版 | 全投入仕事有限、global RSET有限 |
| global smoothness of the constructed NS solution | 各稿の指定class | arbitrary-data NS regularity、Einstein–fluid global regularity |
| branchwise all-point implementation | F04/F09 | quantum superpositionの線形性、global positive Hadamard W |

## 12. 再取得・引用

すべての資料リンクは上記SHAに固定した。将来mainが更新されたら新旧statementとdefinitionの差分を取る。引用時は各directoryのREADME/BibTeXにある稿の正式titleを用い、Family 376という集合名を個別定理の代わりにしない。

原本収集run `37726298911` はarchive・hash取得の成功であり、Lean buildでも研究結果の再現runでもない。本PRの検証については[検証記録](family376-validation.md)を参照する。
