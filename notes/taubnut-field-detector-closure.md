# Taub–NUT過去通信：場・送受信器からの判定と現行案のクローズ

**2026-09-23 / 判定：現行の「固定背景＋通常の局所スカラー量子場でTaubから準備する」案は棄却。**
**これはモデルと仮定を固定した否定結果であり、自然界の時間遡行一般を否定する定理ではない。**

読取基点：`main` の `4bc7d4b022345a1b618a0f44b1481ebb1954ea94`（PR #10マージ後）。
[量子場・KRWの監査](operational-past-signalling-focus.md)と[受信記録付き回路](chronology-operational-channel-test.md)を引き継ぐ。
今回はDeutsch型・相関型の回路を選び直さず、**局所場と送受信器の相互作用から確率を導く**。
新しい大域的弦状態、全backreaction、優先権は主張しない。

## 0. 何を閉じたか

| 対象 | 判定 | 判定の種類 |
|---|---|---|
| Taubの通常の量子場を同じ局所理論のまま地平面越しに使う案 | **不可・棄却** | 初期Hadamard状態、実massless KG、既存ノートのコンパクト延長、F-localな場の維持を指定したKRW適用 |
| NUT内部で「計量と波動方程式から遅延核を選べばよい」とする案 | **物理的な通信の導出として不採用** | 今回の具体的な選別不能性。全てのNUT量子論を排除する定理ではない |
| NUT内部の局所送受信過程そのもの | **条件付きで可能** | 正の局所場状態・許される順序の下で同時確率を導出。大域的装置実装は仮定しない |
| 自然界／完全なheterotic stringでの可否 | **この結果からは未判定** | 「未取得の確率を0にする」操作は行わない |

研究上の終了判断は、**この既存案を成功候補として継続採用しない**、である。単なる「もっとモードを計算すればPASSになるかもしれない」という保留には戻さない。
ただし、NUTだけに定義された別の大域量子論や、局所場近似を置き換える弦の実時間過程には別の検証が必要であり、そちらまで「不可能と証明済み」とはしない。

## 1. 文献から持ち込めるものと、持ち込めないもの

Tjoa–Gallock-Yoshimura [F1] は量子場を介した2検出器の非摂動的通信を扱う。
Kasprzak–Tjoa [F2] は場の相関関数と因果伝播核で通信を記述する。そこでの「arbitrary curved spacetimes」は、本文§IIで**globally hyperbolic**に限定され、§IIIの時間順序にはglobal time functionを使う。
Fewster–Verch [F3] の局所probeによる測定も、in/out領域と適切なscattering map、causal factorizationを用いる。

したがって、これらの正規化された通信公式は有用だが、**CTC領域の正しい時間順序・場代数・状態を自動的に供給する定理ではない**。
今回以下では使える局所代数だけを取り出し、NUTへ適用する条件を別に検査する。
Johnson–Svendsen [J] のexact CFTは強い背景入力だが、同論文が算出したalpha-prime修正幾何を、probeに対する全応答や検出確率と同一視しない（PDF pp.3–4）。
full CFTが将来その入力を決定する可能性を否定してもいない。

## 2. 実際の場と送受信器から、どの同時確率が出るか

### 2.1 使用する場・相互作用・記録

まず通常の量子場として扱える領域で、実自由スカラーを使う。
既存の診断用作用は四次元で

```math
S_\varphi=-\frac12\int d^4x\sqrt{-g}\,e^{-2\Phi}g^{ab}\partial_a\varphi\partial_b\varphi
=-\frac12\int dV_{g_E}\,g_E^{ab}\partial_a\varphi\partial_b\varphi,
\qquad g_E=e^{-2\Phi}g.
```

これはこの**スカラー作用**の正確な書換えで、full string actionの等価性ではない。
以下のsmearingは `dV_gE` を使う。結合定数を含む実test function `f_A,f_B` を、送信器・受信器の小さな領域に滑らかに局在させる。
点での裸の場、単色modeのL2規格化、有限mode cutoffを使わない。

選択bit bを保持する記録Rと送信器Sを

```math
\rho_{RS}=\sum_{b=0}^1p_b|bb\rangle\langle bb|,\quad r_b=(-1)^b
```

で準備する。場の初期状態は平均0の正のquasifree状態、受信qubitは `|+x>`。
使用するgapless／simple-generatedな相互作用は

```math
U_A=\exp[iZ_S\varphi(f_A)],\qquad
U_B=\exp[-iZ_B\varphi(f_B)].
```

自由場の交換子がc-numberなので、各検出器の固定monopoleによる時間順序付き線形結合は、無関係な全体位相を除いてこの形になる。
これは[F1,F2]に対応する理想化した場–probeモデルであり、heteroticのBRST-closed検出装置を構成したとはしない。
相互作用領域の順序がA→Bとして正当に与えられるとき、全unitaryは `U_B U_A`。
記録Rを最後まで保持して全ての受信結果を数える。

### 2.2 正規化された同時分布の導出

規約を

```math
[\varphi(f_A),\varphi(f_B)]=i\Delta_{AB}\mathbf1,\qquad
V_B=\omega(\varphi(f_B)^2),\qquad \nu_B=e^{-2V_B}
```

とする。Weyl関係とGaussian characteristic functionから

```math
(\rho_B^{(b)})_{01}
=\frac12\omega\!\left(e^{-ir_b\varphi(f_A)}e^{-2i\varphi(f_B)}e^{ir_b\varphi(f_A)}\right)
=\frac12e^{-2V_B}e^{-2ir_b\Delta_{AB}}.
```

従って

```math
\rho_B^{(b)}=\frac12
\begin{pmatrix}1&\nu_B e^{-2ir_b\Delta_{AB}}\\
\nu_B e^{2ir_b\Delta_{AB}}&1\end{pmatrix},\qquad
\rho_{RB}=\sum_bp_b|b\rangle\langle b|\otimes\rho_B^{(b)}.
```

Y基底を `y=+1,-1` として測れば

```math
\boxed{P(R=b,Y=y)=\frac{p_b}{2}\left[1+y(-1)^b e^{-2V_B}\sin(2\Delta_{AB})\right].}
```

この式は**後選別なしの同時確率**。`sum_y P(b,y)=p_b`, `sum_by P=1`。
状態の固有値は `(1±nu_B)/2` で、`V_B>=0` なら正。
Y測定はこのbinary encodingのHelstrom測定になり、等事前確率で

```math
\boxed{D_B=e^{-2V_B}|\sin(2\Delta_{AB})|,\qquad P_{\rm guess}=\frac{1+D_B}{2}.}
```

記録bitを混合に入れると消えてしまう、という前回の**特定のDeutsch処方**の結論は、通常の線形場のこの導出には起きない。
逆に、この式の `Delta_AB,V_B` と順序を未確認のまま数値で埋めれば、また処方を仮定で選ぶことになる。
ここで必要なのはこの二つのsmeared correlatorと適切な実験実装であって、全BRST cohomologyの分類ではない。

場の正値性は `V_B>=0` だけより強い。2-smearing制限でも

```math
W=\begin{pmatrix}V_A&C+i\Delta_{AB}/2\\C-i\Delta_{AB}/2&V_B\end{pmatrix}\succeq0,
\quad V_AV_B-C^2\ge\Delta_{AB}^2/4.
```

例えば `V_A=V_B=C=0, Delta_AB=1` は固有値 `±1/2` となり、物理状態でない。
2-smearingで正でも全場の正値性・局所性・大域的状態の存在までは保証しない。

### 2.3 「交換子が非零だから過去通信」としない

本当にBの読出しが先で、その後に場だけへ `U_A` が作用する通常の実験なら、受信器のreduced stateは部分traceの不変性で変わらない。
コードではBのoff-diagonalに現れるWeyl積

```math
\omega(W_B(-1)W_A(-r_b)W_A(r_b)W_B(-1))=\omega(W_B(-2))
```

を別に評価し、両bitの受信分布が一致することを検査する。
**この結果は通常の前後関係での結論であり、NUT全体にその前後関係を勝手に付けたものではない。**

## 3. NUT内部では、通常の「遅延」という支持条件が選別力を失う

### 3.1 入力計量と実際の波動作用素

[J, (72)–(73)]とrepoの規約を使う。

```math
p=x^2-1,\quad D=(x+\delta)^2-4p/(k+2),\quad K=(k-2)\alpha',
```
```math
ds^2=K[p^{-1}dx^2-pD^{-1}(dt-\lambda\cos\theta\,d\phi)^2+d\Omega_2^2],
\quad t\sim t+T,\quad T=4\pi\lambda.
```

`k=8,delta=sqrt(8/5),lambda=sqrt(2/5)`。第一NUT領域を `N={x>1}` とする。
`D=3(x+sqrt(10)/3)(x+sqrt(10))/5>0`。`Phi_0=0`なら `mu=sqrt(-g)e^{-2Phi}=K² sin(theta)`。
直接inverse metricとdivergenceを計算すると

```math
KP_\Phi=\partial_x(p\partial_x)+\frac1{\sin\theta}\partial_\theta(\sin\theta\partial_\theta)
+\frac{(\partial_\phi+\lambda\cos\theta\partial_t)^2}{\sin^2\theta}
-\frac Dp\partial_t^2.
```

`box_gE=e^{2Phi}P_Phi`。以下のhomogeneous解と因果構造は両作用素で同じ。

### 3.2 NUT領域の任意の二点は、互いに時間的に到達できる

任意の二点のspatial baseを滑らかな有限長の曲線で結ぶ。その像は `x>1` のコンパクトな範囲に取れる。
その曲線のliftで

```math
h=\dot x^2/p+\dot\theta^2+\sin^2\theta\dot\phi^2,\qquad
 a=\dot t-\lambda\cos\theta\dot\phi>\sqrt{D/p}\sqrt h
```

とすれば、`g(v,v)=K[h-pa²/D]<0` かつ `g(v,partial_t)<0`。
終点のfibre位相は周期Tで同一視されるため、十分大きな整数Nを選び、総fibre進行を終点の位相差に `NT` を足したものへ合わせられる。
曲線上でaを増やせば時間的性質を保ったままその調整ができる。北・南のbundle chartを跨ぐ場合もhorizontal liftとfibre位相で同じ議論が成立する。
逆向きのspatial pathにも同じ構成を適用できる。

したがって、この**連結な第一NUT領域**では

```math
\boxed{I_N^+(z)=I_N^-(z)=N\quad\text{for every }z\in N.}
```

これはtotal viciousnessの具体的な証明である。数値の何本かの経路から外挿したものではない。
従って、任意の非空なsource supportに対して `supp(G_R f) subset J_N^+(supp f)` はN全体を許してしまう。
[F3]の通常の全体的in/out領域も、N内ではそれだけから取れない。
**「causal supportを満たしたから正しい遅延応答」とする選別がここでは機能しない。**

### 3.3 同じ実際の作用素に対する具体的な余剰解

この作用素の静的・角度不変sectorには

```math
u_0(x)=1,\qquad u_1(x)=\frac12\log\frac{x-1}{x+1},\qquad
\partial_x(pu_1')=0
```

がある。N内で滑らかで周期的。
従って `B(z,z')=u_0(z)u_1(z')-u_1(z)u_0(z')` は反対称bisolution。
Green核Gが存在する場合、`G+alpha B` はcompact sourceに対する同じPDEのright-inverse性を持ち、compact test関数でのleft-inverse性もintegration by partsで保つ。
N全体を許す支持条件と周期性も保つ。

具体的に `B(x=2,x'=3)=log(3/2)/2=0.20273255405408...`。
これは実際のTaub–NUTスカラー作用素にある曖昧さであって、回路のパラメータを変えただけではない。
ただし `u_1` は地平面で発散し、Taubからの滑らかな延長を与える解ではない。

**重要な負例：このBを物理的交換子の自由パラメータとして採用してはいけない。**
同じ局所時刻で微小にradial方向へ離れた点は小さなNUT chartではspacelikeだが、`B(2,2+epsilon)=epsilon/3+O(epsilon²)`。
従って無条件の追加は局所交換関係を壊す。これは「二つの物理的NUT量子状態を構成した」という証明ではなく、**PDE・周期性・支持条件だけを満たす候補を棄却する検査**である。

### 3.4 tだけをほどいて通常の被覆空間に戻す方法にも条件がある

Hopf fibreの角度を `psi=t/(2lambda)`（周期2pi）とすれば、接続は

```math
A=d\psi-\tfrac12\cos\theta\,d\phi,\qquad
\frac1{2\pi}\int_{S^2}dA=1.
```

非自明なcircle bundleである。`N=(1,infinity)×S³` は単連結なので、**全Nの被覆としてtだけを非周期化するものはない**。
またstructure groupをcontractibleなRに変えたprincipal bundleはtrivialで、このChern classを保てない。
局所角度patchのtをほどくことはできるが、それを全Nのglobal coveringと呼んでimage sumを正当化するのは誤り。
別manifold・Misner stringを残す幾何・別boundary prescriptionは別の入力である。

## 4. それでもNUT内の局所通信は、条件付きで構成できる

否定するために通常の局所通信まで消してはならない。
同じ角度で、`x_A=2`, `x_B=2+epsilon` として

```math
\Delta t=\int_{x_A}^{x_B}\frac{\sqrt{D(x)}}{p(x)}dx,\qquad
A=(x_A,t=0),\quad B=(x_B,t=\Delta t)
```

を取る。A→Bはfuture radial null ray。十分小さいepsilonなら、両者は一つのconvex normal neighborhoodに入る。
一方、B→Aの実験室worldlineを、radial方向を戻りながらtを `Delta t` からTまで増やす曲線にする。
`c=(T-Delta t)/Delta t>1` として `dt/dx=-c sqrt(D)/p` なら

```math
ds^2=K(1-c^2)dx^2/p<0.
```

実験室の固有時ではBがAより前である。商時空上のAとt=TのAは同一事象。
`epsilon=0.01,alpha'=1` の経路検算では

```math
\Delta t=0.010197558814294146799417238570122...,
\quad\Delta\tau_{B\to A}=10.971293581078948671160553705161... .
```

有限epsilon例の数値は経路の計算であり、convex neighborhoodのinjectivity radiusを検証した値ではない。
局所場の存在論証には「十分小さいepsilon」を使う。

通常のlocal KG commutatorは、局所null cone上に非零のprincipal singularityを持つ。
したがって、この小さなA→B区間の近くに実test functionsを選んで `Delta_AB!=0` とできる。
local Hadamard状態では滑らかなsmearingに対する `V_B` は有限。結合を小さく調整すれば `sin(2Delta_AB)!=0` とでき、§2の記録付き同時確率は `D_B>0` となる。

**条件付きの肯定命題：** この局所場・送信bit準備・受信記録と、長いB→A実験室履歴を、一つの物理的で大域的に整合したNUT実験へ両設定とも拡張できるなら、過去通信は可能。
局所送信は普通のforward signallingであり、同じ二事象を結ぶ長い実験室worldlineとの組合せが過去通信を作る。

ただし、**局所diamondでの正しい確率を、そのdiamondを出て一周する実験室へ貼り合わせられることは、この計算で示していない**。
送信bitを後から選ぶ装置と過去の受信記録を含む、その大域拡張こそ必要な物理の問題である。
独立に局所解を貼るだけで成功と認定しない。無条件なglobal time orderingも置かない。

## 5. 既知定理から閉じられる範囲

### 5.1 Taubからの通常の局所場完成は、不可能として閉じる

[既存KRWノート](operational-past-signalling-focus.md)は、一つのHausdorff outgoing延長に対して `H^+(Sigma)=S³`、compact generation、base set `B=H` を論証した。
その局所作用素をmassless KGへ写す同じ変換を今回も使う。
KRW [K, Theorems 1/2] により、初期の通常の場代数をそのままF-localに延長することができず、初期Hadamard二点関数のHadamardな延長にも障害がある。

従って、**この仮定一式を保持したまま§2の実験をTaubから地平面を越えて完成する計画は、成立しない**。
これは単に数値計算が終わらなかったという理由ではなく、使用したい理論の条件が両立しないための棄却である。
未計算のbackreactionを推定値で埋める必要もなく、この固定背景の完成案は止められる。

ここから `V_B=infinity` や `D_B=0` を代入することは**しない**。
KRWは特定の有限幅検出器すべての発散、通信容量0、全string theoryの禁止を主張しない。
**確率が定義されない入力模型の棄却**と、**定義された確率がbit非依存であること**は別である。

### 5.2 NUTのみの別理論を、同じ定理で排除しない

Fewster–Higuchi [H] は、時間的平行移動でMinkowski時空を商にしたCTC円筒にF-local場代数を構成している。
これはTaub–NUTの構成ではないが、**CTC／total viciousness／非大域的双曲性だけで全ての局所量子場を禁止する議論への反例**になる。
また、[H]はその構成に非一意性も示す。
NUT内部にだけ定義する理論へ、Taubの初期Hadamard条件を後から追加して自動的に棄却してはいけない。

従ってNUT-onlyの任意の完成や、full CFTが与える非局所・相互作用込みの実時間規則についての普遍的否定は、この研究からは得られない。
**現在のスカラー入力だけからglobal同時確率を導いたとの主張は不採用**とするが、それをNUT-only全プロトコルのno-goとは呼ばない。

## 6. 最終判断・仮説・再開条件

**採否：既存のTaub準備・固定背景局所スカラー案はFAILとしてクローズする。**
これまでの正則古典source、mode透過、有限回路固定点を追加しても、この否定条件を解消しない。

**自然界での可否：この範囲を越えた二択の証明は得られていない。**
肯定には一つの大域的に適合する操作的実現が必要であり、否定にはその実現の全てを排除する範囲が必要。
本ノートは、局所的な条件付き肯定と、特定の大域完成の否定を両方残す。
「どんな仮説を置いてもよい」ならYES/NOを作れてしまうが、それを物理的結論として採用しない。

**作業仮説（証明ではない）：** 通常の局所装置をTaubから準備する経路では、量子場／背景の応答が装置の完成を妨げる可能性を優先する。
根拠はKRWと既存のsource誤差による非正則成分であり、完全な弦の逆反作用を計算した予測ではない。
初めからNUTにいる装置までこの仮説だけで否定しない。定量的な成功確率や主観確率は付けない。

この案を再開する条件は、単なる別modeや別回路ではなく、**上の失敗した仮定を置き換える具体的な大域場代数・状態・送受信instrumentの構成**。
最低限、使うsmeared correlatorの正値性・局所極限・大域gluingと、二つの送信設定と受信記録の共通の物理的実装を示す。
Taubから搬入する案なら地平面で何が変わるか、NUT-onlyならその独立した状態・操作の大域完成を示す。
full BRST／full spectrumの全分類、状態の完全保存、新規CTC形成を自動的に先行必須へ戻さない。

## 7. 再現と検査範囲

```bash
python src/symbolic/taubnut_nut_green_selection.py
python src/symbolic/field_receiver_joint_probability.py
```

前者はinverse metric、密度、4D作用素、timelike lift、Chern数、bisolutionと局所性を破る負例をSymPyで検算。
radial null経路と実験室固有時は50/80桁で比較。
後者はWeyl積から全receiver matrixと保持bit付き確率を生成し、trace、Hermiticity、Helstrom距離、真に早い読出しの不変性、正値性違反の負例を検算する。
さらに `Phi_A=-Delta*P, Phi_B=Q` の連続Schrodinger表現で、移動したGaussian波動関数の確率密度を直接積分する独立検算を50/80桁で実施。Fock空間の切断ではない。

対照値の例は `Delta=0.2,V_B=0.5` で `D=0.143259002150415777...`、`V_B=2` なら `D=0.007132445734374718...`。
**これらはTaub–NUTの数値予測ではない。** `Delta=pi/2` なら非零commutatorでもこのencodingのDは0となる負例も保持。
任意精度積分は40桁以上一致したが、interval arithmeticによる誤差証明ではない。

ローカルはPython 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0、2本ともsuccess。
最初のHelstrom恒等式のassertはSymPyの指数関数／三角関数の未簡約で失敗し、`expand_complex`による同値変形を加えて再検算した。assert・精度は緩和していない。
この環境のgit cloneはDNS解決に失敗したので、GitHub connectorで固定SHAを読み書きする。localで全repoのCIを実行したとはしない。
remoteは独立2本の通常PR選別を使用し、実際のrun・SHA・結果をPRへ記録する。Lean・既存code・reference data・依存・workflowは変更しない。
大域幾何の証明、既知KRW、局所Hadamardの存在はPythonで形式証明したものではない。

## 一次資料・照合範囲

- **[J]** C. V. Johnson, H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, [hep-th/0405141v3](https://arxiv.org/abs/hep-th/0405141v3), PDF pp.3–4、(72)–(73)を再読。背景とprobeの応答を区別。
- **[F1]** E. Tjoa, K. Gallock-Yoshimura, *Channel capacity of relativistic quantum communication with rapid interaction*, [2202.12301](https://arxiv.org/abs/2202.12301), globally hyperbolicの前提、§III–IV、(56)–(65)のnoise／commutator依存を確認。§2は規約を固定したspecializationで、論文の全capacity計算の再現ではない。
- **[F2]** M. Kasprzak, E. Tjoa, *Transmission of quantum information through quantum fields in curved spacetimes*, [2408.00518v2](https://arxiv.org/html/2408.00518v2), §II.1、§III.1を本文で確認。global hyperbolicityとtime orderingの前提に注意。
- **[F3]** C. J. Fewster, R. Verch, *Quantum fields and local measurements*, [1810.06512](https://arxiv.org/abs/1810.06512)。局所probe・scattering map・causal factorizationの構成を参照。今回その全定理をNUTへ拡張していない。
- **[K]** B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, [gr-qc/9603012v2](https://arxiv.org/abs/gr-qc/9603012v2)。Theorems 1/2、§5を再確認。PDF p.5のページ画像でも仮定と結論を確認。
- **[H]** C. J. Fewster, A. Higuchi, *Quantum Field Theory on Certain Non-Globally Hyperbolic Spacetimes*, [gr-qc/9508051](https://arxiv.org/abs/gr-qc/9508051), abstract、§2–4のF-local構成・非一意性を確認。NUTへの適用は主張しない。

検索は上記模型・local probes・causal propagator・CTC量子場に絞ったもの。全2026年文献の網羅や「他に解決論文が存在しない」ことの証明ではない。
[J,F1,H]のPDF抽出本文は取得できたが、ページ画像の取得はcache-missだった。その3点を目視済みとはしない。
