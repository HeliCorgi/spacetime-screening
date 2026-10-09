# Chronology形成の研究戦略: 帰還倍率から帰還写像の剛性へ

2026-10-09。基点: PR #40 `27e78fe8ab10566c2f54d787ba8e15e1ce0aa65a`。
main: `1ff10c4453f52f9f8f8c2c835a52812ce7faac90`。
署名(-+++)、通常の実スカラー場。新しい形成候補の一覧は作らない。
[検証記録](chronology-return-rigidity-validation.md)、
[有限計算](../src/symbolic/chronology_return_rigidity.py)、
[独立検算](../src/symbolic/chronology_return_rigidity_verify.py)。

## 0. 何を選び、なぜ選んだか

**選択した一件は、局所Hadamard性が要求するnull帰還写像の剛性定理である。**
源を逆算する前に、ESU型refocusingを「形成境界だけ」に実装する修復が原理的に通るかを決める。
今回の証明は、単一軌道の帰還倍率を1に調整しても、近傍の全帰還写像が恒等でなければ不十分であり、
恒等にできたとしても、4次元ではその点は既にchronology-violating領域の**内部**にあることを示す。
これにより、closed-null onsetを保持する修復系列を、対称性や変形の大小に依存せず排除する。
全ての有限資源formationにclosed-null onsetがあるとは証明しない。

### 計算前の三方向の比較

| 方向 | 成功なら元問題に何が言えるか | 失敗なら何が排除されるか | 判断 |
|---|---|---|---|
| 1. covector障害の一般化 | 倍率・横レンズ・非対称変形を個別に試さず、同じ障害を持つ修復全体を棄却できる。特にESU例がformationへの逃げ道かを判別 | 強すぎる一般化だけを棄却。反例を状態構成へ利用できる | **今回実行**。既に使える微局所理論と有限時間geodesic flowだけで閉じられる |
| 2. 障害を避ける動的幾何 | 全ての近接null接続を通過すれば、初めてsource/RSETへ投資する根拠になる | 選んだ修復と境界条件だけを棄却。探索失敗は一般no-goでない | 1の必要条件を先に確定。現在のaffine-frontにprofileを足す探索は停止 |
| 3. 必要応力から同じg/WのSCEEを閉じる | 全段階が成立して初めて物理的formationの存在証明へ進める | 指定source/state/couplingsの組合せを棄却。Bianchiやtrace一致だけでは何も認定しない | Wが既に不可能な幾何で行っても情報利得がないため後順位 |

源・RSETの計算が不要という意味ではない。**幾何の必要条件を通った同じ候補に対してのみ行う**。
今回の一般化が証明できない場合も、任意の補題を積み足すのではなく、どの局所幾何で推論が壊れるかを調べる方針を先に採用した。

### 証拠区分

- **既存結果**: 局所Hadamardのwavefront-set表示、特異性伝播、因果曲線のpush-up、KRW [R,K,Q,W]。
- **指定headの結果**: affine-time frontの直接法によるreturn構成、有限stress診断、修復の判定 [P]。
- **今回の解析的導出**: §3のreturn-germ剛性とchronology境界に対する帰結。§5のmassive ESU負例。
- **有限の記号・有理計算**: §6。連続体定理の形式証明ではない。
- **未検証**: 一般の有限準備からclosed/recurrent generatorを導く命題、反射境界の完全な問題、formation SCEE。

手法の新規性・優先権を主張しない。KRW §6は既にnull self-intersectionとrefocusing例外を論じる。
今回の追加はその方法を**局所Poincare写像の恒等性とchronology境界の排除**として明示的に導出したもの。
独立査読と連続体QFT/GRのLean形式化は未実施。

## 1. 指定headで実際に使われている前提

[P]のクラスは

\[
 g=-2dt\,d\psi+[f(r)-\gamma t]d\psi^2+dr^2+dz^2,
 \qquad \psi\sim\psi+\ell,
 \qquad \gamma,\ell>0.
\tag{1}
\]

全経路を含む時空上で、smoothかつ下に有界なfについて、固定端点のweighted actionを最小化し、
null geodesicを構成している。時間の帰還条件を課すとcovector成分の比は
`exp(gamma*ell/2) != 1`。logistic例では証人が有限boxに入る。
今回はその存在証明を別のmetricに無断で移植しない。

前の会話の未反映Hopfパッチではなく、この**実際の27e78fe8...の内容**を基点にした。
今回の定理は(1)、fの下界、Killing対称性、gammaの一定性、small-backreaction仮定を必要としない。
代わりに、ある実際のnull returnとその小さい近傍のgeodesic flowが同じ場の定義域内にあることを使う。

## 2. 言える「必要十分条件」と、言えない必要十分条件

### 2.1 証明に実際に使う微局所条件

Nをsmoothでtime-orientedなLorentz多様体の開領域とする。作用素は

\[
 P=\Box_g-m^2-\xi R-V(x),\quad V\in C^\infty(N,\mathbb R).
\]

より一般には、同じreal principal typeのnull principal symbolを持つsmoothなscalar operatorでよい。
主記号の正負・定数倍を除き、Hamiltonianを

\[
 H(x,k)=\tfrac12g^{ab}k_ak_b,\quad
 \mathcal N^+=\{(x,k):H=0,\ k\ne0,\ g^{-1}k\text{は未来向き}\}
\]

とし、そのHamilton flowをPhi_sと書く。sはaffine parameterであり、計量のcoordinate timeではない。

pの小さいnormal-convexかつ**intrinsically GH**な近傍Uを選ぶ。
UがM全体に対してcausally convexであることは要求しない。それを要求すればreturnを先に排除してしまう。
U内の短いnull geodesicによる局所Hadamard関係を

\[
 C_U^+=\{(x,k;y,-l):(x,k)=\Phi_s(y,l),
 \text{対応する短いgeodesicがU内},\ (y,l)\in\mathcal N^+\}
\tag{2}
\]

とする。s=0の対角を含み、sの正負の両方を許す。

証明が実際に使うWの条件は、次の二つだけで足りる。

\[
 W\in\mathcal D'(N\times U),\qquad P_xW\in C^\infty(N\times U),
 \qquad WF(W|_{U\times U})=C_U^+.
\tag{3}
\]

通常のglobal bisolutionと局所Hadamard条件は(3)を満たす。
さらに局所化すると、必要なのは近い対角null方向のWF下側包含と、帰還点対でのC_U^+への上側包含である。
(3)はその二つを一度に保証する明瞭な条件であり、作用素の全てのregularity仮定について最弱性を証明したとの主張ではない。
positivity、CCR、第二変数の場の方程式、stationarity、Gaussian性、Einstein方程式、energy条件は証明には使わない。
これらを不要とする**物理的存在定理**ではなく、より弱い必要条件だけで矛盾させるという意味である。

smoothnessをC-infinityからどこまで下げられるか、spin/gauge/相互作用場への一般化は今回の定理には含めない。
相互作用WのP_xWが非smoothなら(3)の伝播議論をそのまま使えない。

### 2.2 globalな「return関係の整合性」

全点局所Hadamardを仮定する場合、対角の全null covectorを第一変数について伝播した関係R_g^+は
`R_g^+ subset WF(W)`。さらにWFは閉集合なので、そのclosureも含まれる。
従って各点で適切なUについて

\[
 \overline{R_g^+}|_{U\times U}=C_U^+
\tag{4}
\]

が必要。右から左への包含は短いlocal geodesicがglobal関係にも含まれるため自動である。
closureはjoint cotangent bundleのzero sectionを除いた空間で取り、片方のcovectorだけが零に近づく極限も勝手に捨てない。

(4)は「対角から伝播で強制されるwavefront点が局所Hadamardの許容集合からはみ出さない」ことと同値。
**それだけでW、positivity、CCR、Hadamard係数、RSET、SCEEが存在するという必要十分条件ではない。**
§5.2に、(4)の幾何を完全に保つのにKG bisolution自体が零しかない反例を与える。

## 3. 選んで実行した定理: 局所return-germ剛性

### 定理 RR

時空次元d>=3、(3)を仮定する。有限の正affine parameter Lに対して、
N内の非定常な未来null geodesic segmentがpから同じpへ戻るとする。
全経路とその小さい摂動のtubeはN内に含まれる。大域的なgeodesic completenessは不要。
有限のphase-space軌道がsmoothな開領域に完全に含まれる場合、小さい初期データ摂動の有限時間包含はODEの連続依存から従う。
別途の大域安定性仮説を課しているのではない。境界へ当たるrayについてはこの推論をそのまま用いない。

すると次が必要である。

**(i)** 帰還covectorは正確に初期covectorと一致する。

**(ii)** その周期orbitに横断的な局所section上の、**スケールを捨てないcotangent return map** Piは、
初期点の近傍で恒等写像である。固定点やD Pi=Iの確認だけで、このgermについての結論の検証を代用できない。

**(iii)** pには異なる未来null方向の閉geodesicが存在し、したがってp<<p。
pはchronology-violating集合C={x:x<<x}の内部にある。

**対偶:** pがchronology境界、あるいは任意のchronology-respecting点であるとき、
そこを通る一つの完全に含まれたnull自己帰還があるだけで(3)は不可能。
帰還倍率が1であっても排除できる。全horizonのcompact generationは不要。

### 証明

**第1段階: 一つのrayのcovector。**
alpha_0=(p,k_0)、Phi_L(alpha_0)=(p,k_1)とする。
(2),(3)から `(p,k0;p,-k0)` はWF(W)にある。
第一変数のreal-principal-type特異性伝播 [K,Q] により
`(p,k1;p,-k0)` もWF(W)にある。
P_xはproduct全体のk_x=0で退化し得るが、今回の軌道は常にk_x!=0なので、その近傍でのreal-principal-type伝播だけを用いる。
局所Hadamardの対角で許されるのはk1=k0だけである。
二変数の同時正倍というconicityは、片側だけの倍率を消さない。
この段階はd>=3を必要としない。

**第2段階: rayの近傍全体へ。**
k1=k0の場合、Phi_L(alpha_0)=alpha_0であり、phase space内の周期orbitである。
有限のsmooth orbitなので、近傍のalphaにも[0,L]とその少し先までsmoothなflowが定義される。
causticがあってもcotangent Hamilton flowのsmoothnessは失われない。

Uのlocal temporal coordinate uを選び、
`S={alpha in N^+: u(base(alpha))=u(p)}` を横断sectionとする。
`X_H u != 0` なので、Lに近い一意でsmoothな帰還時間T(alpha)>0を選んで

\[
 \Pi(\alpha)=\Phi_{T(\alpha)}(\alpha)\in S
\]

とできる。ここでは初期alphaはalpha_0近傍のS内。

(3)は、同じU内の**全ての近いalpha**の対角特異性を含む。
従って `(Phi_L(alpha),-alpha)` はWF(W)に属する。
両端のbaseはU内でalpha_0に近いので、(2)より

\[
 \Phi_L(\alpha)=\Phi_{s(\alpha)}(\alpha),\qquad |s(\alpha)|\ll L,
\tag{5}
\]

でなければならない。ここで右側はU内の短いlocal flowである。
s(alpha)はlocal temporal coordinate uの差を使うimplicit function theoremでsmoothに選べる。
これにより

\[
 \Phi_{L-s(\alpha)}(\alpha)=\alpha.
\]

横断sectionへの近い帰還の一意性からPi(alpha)=alpha。
したがってPiは**germとして恒等**である。
この結論には小さいcurve perturbationが同じ領域を通ることが不可欠であり、cut-offを横断したrayを使えない。

**第3段階: chronology。**
同じbase pでk0に近い未来null covectorを変える。
d>=3では、その近傍に非比例な二つの未来null方向がある。
第2段階により両方のrayが正の時間後にphase spaceで閉じる。
一方を一周してから他方を一周する未来因果曲線には、pで非平行なnullの角が生じる。
join直前の点aと直後の点bを十分近く取れば、局所的にa<<bとなる。
残りのloop部分がp<=aおよびb<=pを与え、push-up [W] によりp<=a<<b<=pからp<<pを得る。
Cは開集合なのでpはその内部にある。証明終。

2次元では未来null coneの方向が離散であり、第3段階はそのまま成立しない。
KRW §6の2D null-strip例を誤って排除しないため、d>=3を外さない。

### 一つのreturn branchについての正確な必要十分条件

alpha_0でPhi_L(alpha_0)=alpha_0とし、同じtube・local sectionを固定する。
そのbranchから強制される `(Phi_L(alpha),-alpha)` が全てC_U^+に入ることは、
**Piが近傍で恒等であることと同値**。必要性は上の証明、十分性は
`Pi(alpha)=alpha` ならPhi_L(alpha)がalphaの短いlocal flow上にあることから従う。

同じ点へ戻る**一つのrayだけ**なら、伝播で生じる対角点がC_U^+に入ることはk_out=k_inと同値である。
単一rayの条件、近傍branchの条件、stateの条件を区別する。

この「十分」は**このbranchのWF集合整合性**だけに対するもの。
全branchの制御、principal amplitude/transport、低次項によるglobal equation、positivityを含めた状態の十分条件ではない。

## 4. 形成への帰結と、一般化できないところ

### 4.1 源を変えても直らない範囲

future Cauchy horizon H+(S)はachronalで、その点はCに入らない。
従って**H+(S)上に実際の閉null generatorがあれば**RRが適用され、
初期Hadamard状態をその点まで局所Hadamardなbisolutionとして延長できない。
正則なchronology境界上のnull自己帰還についても同様。

Killing対称性、nonzero surface gravity、単調なformation、analyticity、stationarity、
全horizonのcompact generation、small-backreactionは不要。
metricを大きく変えても「境界上のnull自己帰還」を保つ限り失敗する。
ESUのfull refocusingをその境界へ移す修復は、成立すればp<<pを意味し、最初の境界という要求自体を失う。

これは「ESU解は誤り」ではない。ESU時間商の各点は最初からCの内部にあり、RRと整合する。
因果的ESU被覆に時間商を後付けすることを、物質Cauchy発展として認めるものでもない。

### 4.2 証明していない一般化

- 任意の有限energy・有限準備から、closed generatorまたはcompact generationが従うとは言わない。
- denseで閉じないgenerator、無限遠へ逃げるgenerator、境界で反射するrayは別の幾何条件を要する。
- exact returnがないというだけでは、(4)のalmost-return/closure障害がなくなったとは言えない。
- RSETの全成分が全経路で無限大になる、という定量的発散はこの証明からは導かない。
- 全ての相互作用QFT、非局所理論、変化したprincipal symbol、理想boundary domainを同じ定理に含めない。

KRWは閉じないrecurrent generatorsも扱うため、本定理がKRWを全部置き換えるわけではない。
両者は「初期Hadamardを保つformation」を異なる幾何入力で排除する。

## 5. 過大な必要十分主張を防ぐ反例

### 5.1 倍率1は十分でない: 既存のcubic交差

前段の既存対照

\[
 g=-2dt\,d\psi-t^3d\psi^2+dx^2+dz^2,\quad\psi\sim\psi+\ell
\]

のt=x=z=0、p_t=-1を使う。Hamiltonianは

\[
 H=\tfrac12t^3p_t^2-p_tp_\psi+\tfrac12(p_x^2+p_z^2).
\]

一周後にcovectorは元へ戻り、倍率は1。
しかしscreen変分は `delta x'=delta p_x, delta p_x'=0` なので

\[
 D\Pi_{\rm screen}=\begin{pmatrix}1&\ell\\0&1\end{pmatrix}\ne I.
\tag{6}
\]

時間のスケールだけを合わせても横方向のreturn関係が局所Hadamardと合わない。
これは有限数値sampleではなく正確なfirst variationである。

なおD Pi=Iという一次情報だけからgermの恒等性は、一般のcanonical mapについては導けない。canonical map `(q,p)->(q,p+q^3)` はsymplecticでD Pi(0)=Iだがgermは恒等でない。
これは**canonical-map上の反例**であり、そのmapを持つ新しいLorentzian metricを構成したとの主張ではない。

### 5.2 幾何学的refocusingも状態の十分条件でない: 同じESUで低次項だけ変える

既存の時間周期ESU、`(R/(2*pi*a)Z) x S3_a` では全null geodesicがrefocusする。
energy Eでparametrizeすると周期は `2*pi*a/E`。round sphereのgeodesicの厳密式から、
base・方向・大きさの全てが戻り、return-germは恒等。
short local null関係への全global windingの折り畳みも整合する。

しかし同じ幾何上の作用素を

\[
 P_m=\Box-R/6-m^2,\qquad m^2a^2=1/2
\]

とする。通常のperiodic real scalarであり、automorphic phaseや周期を変えない。
時間Fourier mode n in Z、S3 harmonicのj=l+1>=1について、固有値は

\[
 a^{-2}(n^2-j^2-1/2).
\tag{7}
\]

`2n^2-2j^2-1` は全整数n,jについて奇数なので零にならず、絶対値は少なくとも1。
コンパクトなS1 x S3上のdistributionのFourier展開の一意性から、P_m u=0のdistributional解はu=0のみ。
二点分布でも第二変数を任意のtest functionでsmearすれば同じ議論が使え、P_xW=0はW=0を強制する。
W=0は局所CCRもHadamard対角特異性も持たない。

**同じnull flow・同じreturn-germを保つのに、状態は存在しない。**
よって(4)やPi=IdをHadamard stateの必要十分条件にしてはいけない。
一方m=0ではn=+-jの無限のmodeがあり、既存の共形massless熱状態の構成を否定しない。
これは形成候補を追加したのではなく、同じESUを使ったsufficiencyの反例である。

### 5.3 Grant切取り: 全経路包含の仮定は外せない

既存のcut-off GrantではCTCを残して該当self-return null chord全体を領域外へ出している。
その削除されたchordにRRを適用することはできない。
この例は「CTCなら必ず同じ含まれた証人がある」を否定するが、positive boundary stateや物理wallを構成した例ではない。
またclosed-nullを持たないCTC域もRRの直接対象外。CTCの単なる存在とnull-returnは同値ではない。

## 6. 実行した有限検算と、その意味

forwardは(1)を含むgeneral F(t,x,psi)の逆計量からHamilton方程式を作り、
`d log|p_t|/dpsi=-F_t/2` と、cubic例の8次元Hamilton系のscreen線形化を検査する。
独立verifierはHamilton行列をimportせず、LagrangianのEuler--Lagrange方程式からscreen変分を得る。

ESU対照はJacobi行列がIになることに加え、独立検算でround S3をR4へ埋め込んだgeodesic
`X(lambda)=cos(E lambda/a) X0+(a/E) sin(E lambda/a) V0`
を使い、全近傍族の帰還を確認する。Jacobi行列がIだけでgermを認定していない。

massive対照は多項式のmod 2計算と全residue classの独立検査。
§5.2の全mode結論はFourier完全性と整数の奇偶性の**解析証明**であり、有限cutoff試験の外挿ではない。
forward/verifierの成功をRR自体のmachine proofへ格上げしない。

## 7. 方向3の同時監査: 何をもう計算しなくてよいか

\[
 E_{ab}[g]=G_{ab}+\Lambda g_{ab}+a_1H^{(1)}_{ab}+a_2H^{(2)}_{ab},
\]
\[
 E_{ab}[g]=8\pi G\left(T^{cl}_{ab}[g,D]+\langle T_{ab}\rangle_{ren}[g,W]\right).
\tag{8}
\]

| 段階 | RRで排除されるformation class | RRを通過したgeometry |
|---|---|---|
| 因果的initial data | 境界pがCの外であることが入力。初期GH chartだけを切り出す代用は不可 | 真に因果的な過去領域と拘束を証明する |
| 有限資源 | 有限か否かに依存せずWで失敗。有限energyからcompact generationを仮定しない | 全matter/driverの切断energy、有限準備、incoming dataを別々に評価 |
| 必要stress・局所保存 | Bianchiは必要stressの保存を与えても、Wの不在を救わない | sourceの作用・運動方程式・量子的Ward identityを閉じる |
| positivity/CCR/Hadamard | (3)自体が不可能なので、全条件を持つstateは不可能 | P_xW=P_yW=0、positivity、局所CCRとHadamard係数を全て検証 |
| RSET | 要求した全点Hadamard prescriptionを供給できない | 同じg,Wから計算。有限countertermを固定し保存と有限性を検証 |
| SCEE/backreaction | 同じgを維持するsource調整は無効。大きな変形も境界returnを保つなら無効 | (8)の全tensor、拘束、同じstateのfeedbackを解く |

**T_req=E[g]/(8*pi*G)は逆算診断であってsourceの存在ではない。**
また `T_cl=T_req-RSET` と置くだけでもsourceの運動方程式は得られない。
RRの適用外というだけで、右列をチェック済みにしない。

## 8. 元問題への寄与、最大の障害、次の単一作業

### 寄与

親版の倍率・profile・small-perturbationに依存した排除を、
**任意のsmoothな4D geometryのnull return-germ**に対する必要条件へ強めた。
closed-null onsetを保つ限り、boost echo、横レンズの調整、ESU型full refocusing、大きい非対称backreactionの全てが
formationの救済にはならない。fieldのsourceを解く前に、まとまった修復系列の合否を決めた。

これは「全てのformationが不可能」の一般定理ではない。
元問題全体は従来の分類4、今回排除したclosed-null-onset仕様は限定no-go。
新しい必要条件を通った物理的formation解も、今回は提示していない。

### 最大の障害

有限資源・有限の因果的準備という物理的条件から、全経路を含むnull recurrence、
またはKRWのcompact generationが必ず従うという橋はまだない。
有限energy integralをcompactなsupportと同一視するとこの橋を捏造してしまう。
反対に、閉じないgeneratorや切取りを許すことが、物理的sourceとHadamard stateの存在を保証するわけでもない。

### 次に一つだけ行う作業

**既存のmoving Grant cutを、明示したbulk Robin境界問題として固定し、反射を含む完全なcanonical return関係を判定する。**
新metricを列挙せず、親版§2のwall `r=R(T)` と同じbulkを使用する。
過去のchronal annulusから閾値を有限時間で横切るsmooth timelike wall、固定した実Robin係数、
内wall・z方向の境界も明記し、normal KG場のgeneralized bicharacteristicsを追う。
outer wallのintrinsic KGを仮定した以前の排除や、smooth potentialへの置換を答えにしない。

判定は、全ray包含・reflection伝播・local boundary-Hadamard関係を実際に照合して、
(i)非恒等なreturn branchまたは局所関係を破る集積を見つけてそのboundary completionを排除するか、
(ii)幾何の必要条件を通ることを示して、その**同じdomain**でのpositive W/source/SCEEを方向3へ渡すか。
(ii)でもformation成功とはしない。

この仕事を選ぶ理由は、現系列で残る明示的な回避が「pathの削除と境界domain」に依存しているため。
RRや有限厚化の再証明は代替にならず、boundary型を決めずにsourceだけ計算するのも無効。
非再帰的formationを有限準備一般から一括分類する巨大な補題より、対象・成功/失敗の意味が限定され、両結果に情報価値がある。

## 出典

- [P] 指定headの [dynamic-front](https://github.com/HeliCorgi/spacetime-screening/blob/27e78fe8ab10566c2f54d787ba8e15e1ce0aa65a/notes/chronology-dynamic-front.md)、特に§3.1、§5.4。
  前段の [ESU/Ori/Grant](https://github.com/HeliCorgi/spacetime-screening/blob/27e78fe8ab10566c2f54d787ba8e15e1ce0aa65a/notes/chronology-formation-mainline.md) も同じheadで固定。
- [R] Radzikowski, *Micro-local approach to the Hadamard condition in quantum field theory on curved space-time*, CMP 179 (1996), 529--553, https://doi.org/10.1007/BF02100096 . local GH近傍でのHadamard/WFの基礎。
- [K] Kay--Radzikowski--Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, CMP 183 (1997), 533--556, https://arxiv.org/abs/gr-qc/9603012 . 特に§3、§5、§6。refocusing例外も原著にある。RRを原著の定理番号へ偽って帰属させない。
- [Q] Khavkine--Moretti, *Algebraic QFT in Curved Spacetime and quasifree Hadamard states: an introduction*, https://arxiv.org/abs/1412.5945 . Remark22、Theorem6、§3.4。
- [W] Witten, *Light Rays, Singularities, and All That*, Rev. Mod. Phys. 92 (2020), 045004, https://arxiv.org/abs/1901.03928 . §5.1--5.2、特にFig.26--27に対応する本文。因果曲線の角とtimelike変形の幾何。図の転載・図からの数値読取は行わない。

この文書の解析的証明を引用文献が既に完成した定理であると記述していない。
新しいquantum-gravity仮定や新物理は使わず、証明で実際に使った仮定を(3)とRRに限定した。
