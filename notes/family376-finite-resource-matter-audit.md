# Family 376: 有限資源・因果的相対論的物質源への埋込み監査

2026-10-08。読取基点は PR #40 の `c074780bf48f6b9acda92a94c1b74b28f96f362c`。
対象は **計算を実行する閉じた物質系**。CTC形成・Hadamard・RSET・SCEEの判定は今回変更しない。

## 0. 結論と分類の意味

**総合判定 D: 現時点では、Family 376の任意長計算を有限資源の因果的相対論的物質初期値問題へ埋め込む構成は未認定。**

本依頼の A/B/C/D は、既存の[接続監査](family376-fluid-gr-bridge-audit.md)の「接続度B」と別の分類である。

| 判定 | この監査で認める意味 |
|---|---|
| A | 一つの固定された因果的物質理論で、全入力に対する合法な有限資源データ、全計算時間の発展、停止検出の同値が証明済み |
| B | 不足する補題を具体的に限定した条件付き結果。単に「埋込みが存在すると仮定する」ことではない |
| C | 明示した構成と要求の同時成立を排除。全ての計算や全ての相対論的物質の禁止ではない |
| D | 現行の証拠では上記の存在・排除のいずれにも到達しない |

無変更NSの局所初期値問題を有限伝播速度の理論として扱う案は **C**。
固定の正の不可逆コストを払い続ける永久反復を有限の使用可能資源で動かす案も、後述の仮定下で **C**。
しかし、急速減衰型や別の符号化・物質理論までこのCに含めない。
現行R1の有限時間gateは部分成果であり、任意長計算のA/B認定ではない。

「有限時間のある解がある」「どの有限prefixにもそれぞれ解がある」「一つの同じ解で全prefixを実行する」は異なる。
この区別は追加Leanで、資源予算の簡単な量化記号の反例として検査する。

## 1. 原本・更新・証明の射程

OpenAI/math の今回確認したmainは `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`。
初回監査の原本は `adc7f1241b42e322a6451854ab7e4b4c146bf78a`。
**9稿それぞれのbuildディレクトリのGit tree SHAを現在の原本と照合し、旧取得原本と全9件一致を確認した。**
TeX入力一式の同一性を調べたのであって、更新全体に変更がないという主張ではない。
差分APIの上限付きファイル一覧から「変更なし」と推定していない。

[現在の形式化scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/376.md)のblobも `b43f10df2d8fb85337f2b74abe299de009d0ad38` で旧版と一致する。
原論文のproof全体の独立査読、upstream Leanの全依存・comparatorの再buildは行っていない。
以下の「原稿定理」は原稿の正確な主張であり、今回の小さなテストが全定理を証明したという意味ではない。

### 1.1 共通のPDEと符号化

3空間次元、非相対論的、非圧縮、平坦な成分ごとのLaplacian:

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u+f,
\qquad \nabla\cdot u=0,\qquad u(0)=0.
\tag{F}
\]

粘性は固定の正数。algorithmic assertionはcomputableな粘性に対するもの。
一部の稿は非computableな正の粘性についても、その値をoracleとした相対的評価を許す。
T³は空間周期境界、R³とR²×Tは壁なしで、支持条件と指定されたsmooth/energy comparison classを用いる。
速度の初期値零は、静止流体のrest energy・装置・メモリが零という意味ではない。

有限の遷移表を可逆な履歴付き命令へ変換し、gapped radix coordinatesにtapeやhistoryを保存する。
有限affine命令を、shear・Hamiltonian輸送・solid-box輸送などで実装し、clockとloadingを付加する。
**選択された計算を先に実行してその軌道を再生するのではない。** 全分岐を記述して速度場を作り、

\[
f=u_t+(u\cdot\nabla)u-\nu\Delta u
\]

を外力とする数学的構成である。これはNSに対する有効な構成法だが、閉じた装置場の方程式・stressを構成する作業ではない。
記述のeffective性は任意の要求精度で関数・微分を評価できること。計算時間の一様上限、有限の物理精度、実験的な初期データ準備を意味しない。

### 1.2 9稿を混合しない

各稿はOpenAI、2026-09-27。F番号は[既存の定理台帳](family376-theorem-ledger.md)と共通。
末尾の出典表から現在の固定TeXへ移れる。詳しい初期粒子座標・comparison spaceも同台帳に残す。

| ID・原稿定理 | 領域・駆動・初期条件 | 実装・観測と資源の範囲 |
|---|---|---|
| F01 *Finite Instructions and Solenoidal Shear Flows*, Thm 1.1 | 単位T³、u(0)=0、p=0、発散零・平均零のf、t≥1で1周期、全mixed derivative有界 | recorderとshear。粒子(1/8,3/8,1/2)が1/2<x1<1へ入る iff halt。kinetic energy有界。永久駆動の全仕事は別 |
| F02 *A Fixed Particle Test for Computation in a Forced Viscous Flow*, Thm 1, Cor 1 | 単位T³、u(0)=0、smooth平均零f。u,fの全微分の空間supがL∞t∩L²t | 履歴を第三座標に保持しslow scheduling。粒子(1/8,3/8,0)、1/2<x1<1。有限機械的仕事を示せても装置の有限資源とは別 |
| F03 *Universal Computation with Eventually Stationary Navier–Stokes Forcing*, Thm 1.1 | 単位T³、u(0)=0、平均零f、**t≥1で定常**、全mixed derivative有界 | 七行recorder、Hamiltonian輸送、空間clock。P=(1/4,1/4,0)、1/32<Y<1/8。周期型と時間L²型は別選択。一様有限精度耐性は主張しない |
| F04 *Geometric Programs for Solenoidal Forcing*, Thm 1.1/1.2 | 粒子版は単位T³、fは時刻0から周期的・solenoidal・平均零、p=0。sheet版はT³の辺長10 | 粒子(1/4,1/2,1/4)、1/2<x1<7/8。sheet全点の正対角写像は第三方向で面積補償。selected Leanはsheet命題で、粒子停止検出全部ではない |
| F05 *Prefix Instructions and Incompressible Flows*, Thm 1.1 | 単位T³、u(0)=0、p=0、平均零f、t≥1で周期的、全mixed derivative有界 | 履歴付きprefixとmoving sheets。粒子(1/8,1/4,1/4)、1/2<x1<1。bounded kinetic、有限全仕事・一様noise耐性ではない |
| F06 *Computation under Rapidly Vanishing Navier–Stokes Forcing*, Thm 3.1/4.1/5.1 | R³のmoving-curl/alternating-memory版は固定compact支持、p=0、u(0)=0、全微分が任意逆多項式より速く減衰。5.1は別torus構成 | 3.1は原点からX1<−1、4.1は(−1,0,0)からX1>0。4.1の固定支持はmachine/inputにも共通。5.1は(1/4,1/2,1/2)からstrip。fixed-size無限反復と同じ散逸条件ではない |
| F07 *Velocity-Field Detection of Computation in Forced Navier–Stokes Flows*, Thm 1.1 | 単位T³とR²×Tの別構成、zero data、p=0 | torusは固定stripのu3>1/2、微分boundは各有限slab。cylinderは非負u3の半平面×circle上の積分>1/2。fの支持は各有限時間でcompactだが共通固定compactとは限らない。fのcompact支持はuのcompact支持でもない |
| F08 *Scalar Potentials and Slow Clocks for Forced Fluid Computation*, Thm 1.1 | R³、固定compact支持、u(0)=0、p=0、u,fのj時間微分はC(1+t)^−1−j | curlを生成する三つの古典potentials、onto clock。原点からX1<−1。積分仕事は評価可能。potentialsは独立な相対論的scalar matterではない |
| F09 *Incompressible Box Transport and Finite Computation*, Thm 3.4/4.1 | R³、p=0、u(0)=0、f=f0+νf1、固定compact支持、t≥1で周期的 | determinant 1のsolid boxesの近傍全体を輸送。particle(4,0,0)が(−1,2)³へ入る iff halt。repeated fieldはmachineに依存、loadingはinputも符号化 |

F09の非compact一意性classは、例えば u∈C_tH²_x∩C¹_tL²_x、各有限時間のu,∇u有界、pressureを時間のみの関数を除いてC_tH¹_xとするもの。
指定された明示解の一意性であって、任意の3D NSデータのglobal regularity定理ではない。

F06のalternating encodingは b=2(1+max(|Q|,|Γ|)) と偶数digitを使う。
K_n=N+2n+2、s_n=(N+1)2^((n+3)^2)、ε_n=b^(−s_n) という縮小を含む。
全微分の減衰は、全長のtapeに対する固定noise marginを与えない。
F07の「>1/2」も、全ての停止入力について「≥1/2+共通γ」を証明したことにはならない。

形式化scopeは6 comparator設定・5 target theoremに対応し、重複targetを二つの独立証明と数えない。
今回追加するLeanはこれらをimportせず、資源の条件付き論理のみを検査する。

## 2. 有限資源の定義を先に固定する

一つのmachine/inputの実験で、物質・driver・clock・memory・読出しを合わせた合法な初期データを与える。
少なくとも次の量を区別する。

\[
E_{\Sigma}(t)=\int_{\Sigma_t}T^{total}_{\mu\nu}N^\mu N^\nu\,d\Sigma,
\quad E_{driver}(0),\quad
W_{irr}[0,T],\quad V(t),\quad \varepsilon_{prep},\varepsilon_{read}.
\]

非定常compact時空のEΣは、保存するADM energyではない。
保存量・使用可能な仕事の予算を用いるなら、そのエネルギー源と時計を別に指定する。
有限energyの連続体が有限個の情報状態しか持たないと仮定しない。
固定noise floor、有限分解能、有限帯域は採用する場合に明記する追加仮定である。

**三つの区別が不可欠。** (i)各有限TでEΣが有限、(ii)一つの同じ実験でsup_{t≥0}EΣが有限、
(iii)不可逆な累積仕事も有限、は同値でない。さらに各prefixごとに別の予算を与えることは、任意長runの固定予算ではない。

空間compactなT³宇宙、R³上のcompactな速度/forcing、漸近平坦な有限物質実験室も異なる。
R³全域に一定の静止質量密度を置けば、uがcompactでもrest energyは無限である。
物質を切断すると自由境界と外圧・表面stressが問題になる。荷電物質の外部EM場や重力場の支持までcompactとは限らない。
正の背景密度を持つtorusの拘束を解いたことから、真空外部へ同じ解を貼れるとはいえない。

準備済みCauchy dataと有限時間の準備過程も別である。prepare phaseを解として与え、有限energyの装置でそのdataを作り、
因果的な伝播と要求精度を満たす必要がある。zero initial fluid velocityやfinite formulaだけではこの項目は未証明。

## 3. 候補ごとの11条件

「既知」は指定された物質理論の定理・恒等式、「条件付」は合法なstate領域や有限時間に限定した帰結、
「未」は埋込みとして不足、「不適合」は記した直接案の要求違反。空欄を成功で埋めない。

| 条件 | E: Einstein–Euler/Maxwell–Euler | B: Einstein–BDNK＋driver | I: 現行R1のMaxwell–二IS流体 | V: Einstein–Vlasov/Maxwell–Vlasov |
|---|---|---|---|---|
| finite total energy | compactな滑らかな合法dataなら有限。準備装置・全runは未 | 有限切断は条件付。driver全体と全runは未 | 正密度の厳密初期dataで有限。全gate/全runの定量上界は未 | 適切な空間・運動量支持のdataで有限。外場tailと全runは別 |
| compact/finite support | T³なら有限体積。真空への切断は自由境界問題 | 密度下界を使う局所理論と真空境界を区別。driver支持は未 | T³全体。固定physical wavelengthの有限実験室ではない | kinetic matter支持は有限時間に制御可能なclass。EM/metric支持は別 |
| finite-time preparation | 初期データ定理はprepare phaseを与えない | 同左、外力装置も未 | 準備済み電場・二流体dataのみ。物理的準備は未 | 初期distributionの有限プログラムと実際の準備は別 |
| finite propagation speed | causal EOS、timelike u、適切なreductionで既知 | 許容係数とframeの条件下で既知。追加driverは要検査 | 平衡coneと小stressの凍結rest-frame補題。解が許容tubeを保つ証明は未 | massive mass shellの速度<c。Maxwell/Einsteinは適切なgaugeでnull cone |
| hyperbolicity | 正密度・sound speedの条件下の標準framework [R1] | 係数制約下で強双曲 [R2]、任意結合の定理ではない | 非平衡の限定した凍結symbol検査。共通Cauchy reduction・全gate estimateは未 | Vlasovはmass shell上のtransport。coupled局所理論あり [R5] |
| DEC/NEC | e≥|p|等のEOS条件下で満たす。EMを加えても条件維持 | derivative/frame寄与を含む実際のstressを別に検査。因果性だけでは保証しない | π/wのop norm≤10^-3ならtype-I DECの十分条件。初期π=0。tube不変性は未 | f≥0のfuture mass shell積分はDEC/NEC。負のfを使う閉包は不可 |
| smoothness | smooth dataの局所解。shockを避ける全runは未 | 局所regularityと全時間smoothnessは別 | 初期dataとlinear modeはsmooth。nonlinear全時間は未 | smooth dataの局所regularity。全run continuationは別 |
| stability | 有限時間continuous dependence。計算historyの全時間shadowingは未 | equilibrium stability [R2]。compiler全run安定性ではない | 線形energyと誤差bound。二流体全sector・任意長run安定性は未 | PDE stabilityと読出しの論理marginは別。compiler未 |
| well-posed IVP | 拘束・gauge・EOSを固定したclassで局所 [R1] | 条件付き局所framework [R2] | 特定のentropy law・動的電荷を含む全系への定理適用/estimateが残る | admissible distribution/constraintsで局所 [R5] |
| gravitational backreaction | 同じ解のEinstein発展として含める。NS軌道保持は未 | 同左。力を後から逆定義しない | 初期拘束・FLRW背景は厳密。計量一次は相殺、二次以降は未認定 | Einstein sourceはkinetic stress。NS compilerを保持する還元は未 |
| conservation laws | ∇Ttotal=0、電荷・粒子保存。外部fだけを加えると未閉鎖 | driverを含む交換項の整合性が必要 | 定義した方程式の全stress/charge/entropy恒等式あり | collisionless kinetic/Maxwellの交換によりtotal保存 |

全候補の**任意長計算の埋込み**はD。Eの正密度・有限時間の小振幅比較は条件付きBの局所的足場でしかない。
Eulerへν=0として変更すれば、Family 376のν>0原稿の定理をそのまま引用できない。
Bのdriverとの結合、Iの共通切断、Vの必要なmoment closureの証明を省略しない。
Vは有望な別の因果的物質classだが、collisionless分布を粘性NSと同一視できない。

### 3.1 既存定理が担当する部分

[R1]のEinstein–Maxwell–Euler解析は、適切な未知量・電磁場微分を含む双曲型reductionを扱う。
単にEinstein tensorへ任意のNS stressを代入する定理ではない。
[R2]のBDNKは許容輸送係数・hydrodynamic frameの下で、Einstein結合の因果性・強双曲性とequilibrium stabilityを扱う。
これをdriverの任意結合や一様なglobal計算安定性に拡張しない。

2026-07-06の[R3]は、bulk/shear・baryonを含みheat/diffusionを持たないsingle-fluid IS classについて、
非線形causalityの必要十分条件、強双曲性の十分条件、constraint propagationとEinstein結合を扱う。
現行R1のentropy-completed law、二つの異なるrest frame、動的Maxwell couplingへの適用は個別の照合が必要。
「新しい論文にIsrael–Stewartとある」ことだけでR1の残りを埋めない。

[R4]のphysical-vacuum Euler局所理論はMinkowski背景の特定EOS・weighted regularity class。
正密度torus、自己重力、放射EOSをそのまま含むと引用しない。
[R5]のkinetic frameworkは有限支持・energy conditionsを整理する比較対象であって、Family 376のkinetic compilerではない。
[R6]の非相対論的極限解析も、固定精度・固定時間の近似から全計算時間の還元へ無条件に移る根拠ではない。

### 3.2 直接のNS移植が不適合な点

parabolic diffusionと非圧縮pressure constraintを、そのまま光円錐内で伝播する相対論的IVPにはできない。
流体粒子の速度をc未満に小さくすることは、摂動・情報の伝播速度をc未満にすることではない。
Eckart/Landau型の瞬時dissipative構成則についても、単なる共変記法が因果性を保証しない [R3]。
BDNKや緩和系への置換は、まさにprincipal partを変えるための変更であり、無変更移植ではない。

Maxwell–Cattaneoの横modeなら
\[
\tau u_{tt}+u_t-\nu u_{yy}=0,
\qquad c_{signal}^2=\nu/\tau.
\]
\(\tau\to0\)でslow rootは熱方程式へ近づくが、固定νでsignal speedは発散する。
極限の一致から、有限τでの任意長計算・任意の細かいencodingの一致は導けない。

## 4. 物理的制約による、限定された排除命題

以下は原論文の新発見と称するものではなく、標準恒等式と明示的仮定の論理的帰結。
独立査読・連続体の形式証明は未実施。適用仮定を通った候補にのみCを付ける。

### N1. 局所データと観測を忠実に保つ、無変更parabolic IVPの移植はできない

仮定: 初期データを局所的に符号化し、ある領域で二つのデータが一致すれば埋込み後も対応するdomain of dependenceに必要なデータが一致する。
その領域内の同じ速度観測を、全ての許容された小摂動について再現すると要求する。

T³上でu=(ψ(y),0,0)を取れば非線形移流は零。初期shearの非負なsmooth bumpの差を、観測点から離して置ける。
周期heat kernelはt>0で正なので、無外力のNS shear差は任意の正時間で観測点に達する。
有限伝播速度の局所理論では、初期bumpの支持からlight coneが届くまで観測値は同じである。矛盾。

**除外するのは全摂動classの局所・因果的な忠実移植。**
特別に全空間へ相関した初期データを準備して一つの設計軌道だけを再生する案や、全く別の計算符号化はこの証明では除外しない。
GRのconstraintが楕円的であること自体を超光速信号と混同しない。ここでの「局所符号化」は必要な明示的仮定である。

### N2. 固定の不可逆コスト下限と有限の使用可能予算は、無限反復と両立しない

仮定: 補充・未計上のenergy源がなく、全実験に使える仕事の予算がB<∞。
各gateの不可逆コストW_j≥w_*>0。energyを熱へ移した後、同じ熱を無制限・無損失で再利用する装置を暗黙に追加しない。

\[
Nw_*\le\sum_{j<N}W_j\le B.
\]

したがって一つの実験のgate数は有限。追加Leanはこの会計命題の整数単位版を証明する。

flat周期NSでは
\[
K(t_1)-K(t_0)+\nu\int_{t_0}^{t_1}\|\nabla u\|_2^2dt
=\int_{t_0}^{t_1}\langle f,u\rangle dt.
\]
非自明な1-periodic fieldを同じ大きさで反復すれば各周期の正の散逸が固定され、全仕事は発散する。
ここで非自明とは∇uが周期全体で恒等的に零でないこと。単なる空間一様並進はこの仮定に入らない。
定常fだけから非零の散逸下限を推定せず、F03の実際の非自明な持続fieldやF01/F04/F05/F09の反復部に対し個別に調べる。

**反例control:** W_j=2^(−j)なら無限個でも総和は有限。F02/F06/F08の減衰型を上記の正の一様下限で棄却できない。
固定compact支持で|u|,|f|≤C/(1+t)なら、∫|f·u|はC²V∫(1+t)^−2dtで有限。
それでもdriverのrest energy・準備・精度は未証明。有限仕事だけでAにしない。

GRでは、任意のclock vector Xに対し
\[
\nabla_\mu(T^{\mu\nu}X_\nu)=T^{\mu\nu}\nabla_{(\mu}X_{\nu)}.
\]
XがKillingでない場合の幾何学的仕事を捨てて、有限slice energyから固定Bを推定してはいけない。
N2は一般の全GR宇宙を排除する定理ではない。

### N3. 単純な位置radix符号は、固定絶対誤差で全桁を識別できない

仮定: 同じ読出し問題で区別しなければならない二つの配置を、一つのposition coordinateのradixで保持する。
第n桁だけ異なるコードの距離が2b^(−n)で、許容される準備/保持誤差ballの半径η>0がnに依存しない。

十分大きいnで距離≤2ηとなり、二つの誤差ballが重なる。
重なり点で同じ物理状態を二つの異なる論理判定として必ず正しく読むことはできない。
これは当該の**直接符号化の一様robustness**を排除し、exact real-dataのFamily定理を否定しない。
error correction、別座標、別メモリ、η_n→0を許す理論、全ての有限energy連続体系まで排除しない。

F06の急速縮小で小さい振幅をunderflowさせて零として扱う方法は、これを解決せず、情報を捨てている。
F07の固定thresholdも、一様なstrict gapと局所装置による読出しを別に保証する必要がある。

## 5. 現在のR1から何が言えるか

[現行R1本文](r1-closed-shear-driver.md)と[検証範囲](r1-closed-shear-validation.md)を基準にする。
古いローカルpatchの係数・数値で現行結果を上書きしない。
現在の基準は k=Q=w0=1, μ0=1/1000, τ0=1/100、元のgate時間T=π/√3。

厳密な初期dataはh=δ、K=−H0h、E^x=εsin(ky)、B=0、静止した二種の
\(e_s=e_0-\epsilon^2\sin^2(ky)/4\)。全ρ=2e0、総charge=0、拘束を満たす。
初期EΣ=2e0L³は有限。entropy-completed lawと全stress保存も定義済み。
反対向きの一次fluid変分はmetric sourceで相殺し、背景はradiation FLRW。

正粘性linear modeのuniform scaled C1 error <0.26%、変位error <0.18%は同じ線形比較問題の成果。
非平衡π/w tubeの凍結rest-frame symbol補題も、共有切断での非線形解の全gate-time制御を代替しない。
DECは同じtubeで確認可能だが、tubeに解が留まることが未認定である。

**まだないもの:** 明示的非零εについての共通Cauchy reductionの全区間estimate、計算可能なC_*、
full nonlinear physical-frame誤差、準備装置、resetと次gateへのcomposition、任意長のhistory保持。
原R1の残余条件 C_* ε≤0.0074 を、都合のよいC_*を代入して成功にしない。
今回の監査もその数値を算出したとは主張しない。

### 5.1 最小toyを追加して実行する

新規[Python](../src/symbolic/family376_finite_resource_checks.py)は、同じ線形系z=(v,E,B,P)を用いる:

\[
z'=Az,\quad
A=\begin{pmatrix}0&Q/w&0&k/w\\-2Q&0&-k&0\\0&k&0&0\\-\mu k/\tau&0&0&-1/\tau\end{pmatrix},
\quad H=\mathrm{diag}(w,1/2,1/2,\tau/\mu).
\]
\[
HA+A^TH=\mathrm{diag}(0,0,0,-2/\mu),\quad
\mathcal Q=\tfrac12z^THz,\quad \mathcal Q'=-P^2/\mu.
\]

診断用のheat ledger h'=P²/μを足せばQ+hは保存する。
これは**quadratic conformal-modeの会計**であり、非線形の熱流体・driver場・Einstein解をh一変数で構成したことではない。
既存R1のnonlinear entropy completionと混同しない。

implicit midpoint z_{n+1}−z_n=Δ A(z_{n+1}+z_n)/2では、代数的に
\[
\mathcal Q_{n+1}-\mathcal Q_n=-\Delta P_{mid}^2/\mu.
\]
有理数の演算で各stepのh増分を同じ値にすれば、Q+hの残差は厳密に零。
その恒等式を解析的に導出した上で、現在の係数、z0=(0,1,0,0)、**診断区間T=2**で32/64/128/256 stepを計算する。
これは既存gate終点T=π/√3の区間証明書の置換ではない。
80桁matrix exponentialを参照する数値収束試験で誤差比は約4、256stepのmax endpoint errorは約2.893e−5。
この浮動小数点の比較を厳密な連続体誤差保証と呼ばない。

negative controlsは、EM currentの符号反転、heatの欠落、負の粘性、零relaxation、
DECを保っても超光速になる輸送係数、資源超過、radixのnoise-overlapを検出する。
正のcost floorのないsummable sequenceは拒否しない。

追加[Lean](../src/lean/Family376FiniteResources.lean)は自然数単位のcost ledger、
正cost floorでのgate数上界、無限反復との矛盾、∀prefix∃budgetと∃budget∀prefixの違いを扱う。
physical cost floorやfull PDEをaxiomの裏に隠して証明済みと呼ばず、仮定を関数引数として残す。

## 6. A/Bへ進むための最小の還元補題

必要な形は一つの固定した理論Lに対する、全ての有限machine/inputからのtotal computable map
\[
C:(M,w)\longmapsto \text{合法なEinstein--matter準備/初期データ},\qquad
\operatorname{Halts}(M,w)\iff\operatorname{Detector}(\operatorname{Dev}(C(M,w))).
\]
単にここで同値を仮定した条件付き論理は、物理的Bの認定にはならない。
最小の未完成な補題群は次の五つである。

1. **Matter/constraint/compiler lemma.** 固定EOS・輸送係数・driver・gaugeを指定し、全入力で制約を満たすsmooth dataと有限準備資源を有効に構成する。停止oracleで未来のforcingやmetricを選ばない。
2. **Closed-driver and preparation lemma.** 外力を動的装置で置換し、全応力保存・電荷・境界条件・有限速度を示す。clock/loading/読出しを含む一つの全run資源予算を定義・制御する。
3. **All-time continuation lemma.** 同じ解が全ての計算時刻t_nまで存在し、t_n→∞、DEC/NEC・因果的双曲領域・smoothnessと空間/energy boundsを維持する。有限時間局所存在だけでは足りない。
4. **Simulation and error lemma.** 全点routing、history保存、各stepの誤差とdetector marginを評価する。例えばe_{n+1}≤L_n e_n+η_n、e_n<d_n/2を同じ資源付き解の全nで満たす。各nごとの別のε選択では足りない。
5. **Local detector equivalence lemma.** 有限装置の因果的記録がhaltingに対してsoundかつcompleteである。非停止側のfalse positiveを永久に排除し、停止側は有限時刻に記録する。無限半平面の瞬時積分を局所観測に置き換えるときも補題を要する。

一つのfinite-prefixについてのみ上記の時間制御を仮定するなら、有限時間continuous dependenceと誤差評価から条件付きBの近似gateへ進める。
任意長計算のB/Aとは区別する。compilerの関数は有限記述から計算可能でなければならず、論理的な存在やclassical choiceだけでは不十分。

## 7. 次に解く問題を一つに固定

**現行R1の同じMaxwell–二粘性流体系で、指定されたT=π/√3まで、共通Cauchy切断の非線形解と計算可能な誤差定数を構成する。**
初期data・EOS・entropy lawは変更せず、具体的なε>0を一つ示し、π/w≤10^-3、positive density/entropy、
全matter slice energy、物理frameのC1誤差とconstraint propagationを同時に検査する。
これは有限区間のBを実質的に前進させる課題であり、今回の「D」を文言だけで「A」にするものではない。
その後に初めて準備・reset・composition・全run資源と停止同値へ進む。

## 8. 出典と固定されたbuild

全F稿の現在のURLは、下表slugに対して
`https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/<slug>-September-27-2026/build/main.tex`。
各build subtreeが旧取得原本と一致することのみを確認した。upstream Lean依存closureの同一性/正当性の証明ではない。

| ID | slug | 現在照合したbuild Git tree SHA |
|---|---|---|
| F01 | Finite-Instructions-and-Solenoidal-Shear-Flows | `827e9224135ab8925068a767be0179edec901715` |
| F02 | A-Fixed-Particle-Test-for-Computation-in-a-Forced-Viscous-Flow | `2f61703e7b692890aaea9199b25ba0c9aa2aafc8` |
| F03 | Universal-Computation-with-Eventually-Stationary-Navier-Stokes-Forcing | `bbd93ed809281f45632e1b96b30599d33100e3f2` |
| F04 | Geometric-Programs-for-Solenoidal-Forcing | `b3db2e3348769a54e985d2a32b025202caf1a8cd` |
| F05 | Prefix-Instructions-and-Incompressible-Flows | `8d30c8d7ac47558e8635d063a4d9a993d85d1eab` |
| F06 | Computation-under-Rapidly-Vanishing-Navier-Stokes-Forcing | `c224934ed73de88919f3abca3a2206eeb05429d6` |
| F07 | Velocity-Field-Detection-of-Computation-in-Forced-Navier-Stokes-Flows | `b7aafa91a9ea91e38ed0b0f28e1291410fb9995b` |
| F08 | Scalar-Potentials-and-Slow-Clocks-for-Forced-Fluid-Computation | `955ec64fb812d2181ecf2b1801dc974b6f3dced3` |
| F09 | Incompressible-Box-Transport-and-Finite-Computation | `57d6a3b07b1a69c64ef2727c51aa039e3e4ada6b` |

[R1] D. Pugliese, J. A. Valiente Kroon, *On the evolution equations for ideal magnetohydrodynamics in curved spacetime*, arXiv:1112.1525. https://arxiv.org/abs/1112.1525

[R2] F. S. Bemfica, M. M. Disconzi, J. Noronha, *First-Order General-Relativistic Viscous Fluid Dynamics*, Phys. Rev. X 12, 021044 (2022), arXiv:2009.11388v2. https://arxiv.org/abs/2009.11388v2

[R3] I. Cordeiro, E. Speranza, F. S. Bemfica, M. M. Disconzi, J. Noronha, *Nonlinear Causality and Strong Hyperbolicity of Einstein-Israel-Stewart Theories of Transient Relativistic Fluid Dynamics*, arXiv:2607.05639v1, 2026-07-06. Sections II–VIと適用classを参照。 https://arxiv.org/html/2607.05639v1

[R4] M. M. Disconzi, M. Ifrim, D. Tataru, *The relativistic Euler equations with a physical vacuum boundary: Hadamard local well-posedness, rough solutions, and continuation criterion*, arXiv:2007.05787. ここでのHadamardは初期値問題の適切性の意味で、量子場のHadamard状態ではない。 https://arxiv.org/abs/2007.05787

[R5] H. Andréasson, *The Einstein–Vlasov System/Kinetic Theory*, Living Rev. Relativ. 14, 4 (2011), arXiv:1106.1367. kinetic matterの定義・既存局所理論の範囲を参照。 https://arxiv.org/abs/1106.1367

[R6] A. Hegade K R, J. L. Ripley, N. Yunes, *Non-relativistic Limit of First-Order Relativistic Viscous Fluids*, arXiv:2305.09725. https://arxiv.org/abs/2305.09725

検証の実施範囲は[再現記録](family376-finite-resource-validation.md)。
