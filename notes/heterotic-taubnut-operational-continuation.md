# Heterotic Taub–NUT：状態候補・地平面通過・操作的信号の続き

**2026-09-23 / NEW CALCULATION CANDIDATES + 限定したBRST対照検算。優先権は主張しない。**

**結論：operational closed timelike signalling は今回も実証していない。**
ただし「未確立」と繰り返すだけでなく、相対ゲージ複体、候補の列挙、Taub時間の伝達、制御sourceからNUTへの正則なスカラー接続を実際に計算した。

読取基点は `main` の `71bc9be79a3af76b4ad53d1145830329aca6b094`。
[6条件監査](heterotic-taubnut-six-gate-audit.md)と[文献対照検算](heterotic-taubnut-literature-bridge.md)を引き継ぐ。以前の無条件な `BRST/free-string PASS` へ戻さない。ブラックホール側のNPQT接合計算は今回の変更に含めない。

## 1. 6条件の判定

| 条件 | 今回の到達点 | 弦理論での判定 |
|---|---|---|
| 1. 完全なBRST cohomologyの物理状態 | 仮定した2つのAbelianゲージ電流の相対oscillator複体で、Q・homotopy・cohomologyの行列を検査 | **未認定**。許容moduleへの大域的埋め込み、Virasoro／superconformal BRSTを含まない |
| 2. 正ノルム・正常化可能 | source停止後にKG-unitの正則スカラーモードを作る構成例 | **未認定**。BRST物理内積、全場の量子状態の正常化・Hadamard性は別 |
| 3. full string spectrumで許容 | 制限したneutral・unflowed・affine-primary ansatzで、正周波数の必要条件を満たす3組を厳密に列挙 | **未認定**。GSO・格子・全射影・左右接合・spectral flowを確定していない |
| 4. backreaction込みで維持 | incoming正周波数の3モードは全て非正則な未来成分を持つ。調整sourceは回避できるが、滑らかなsource誤差で再発 | **未認定**。全背景多重項とsource装置の連立応答は未計算 |
| 5. NUT到達が因果構造を変える | 指定した外部sourceを許すスカラー近似でNUTへの正則接続を構成。固定背景なので計量変化は0 | **構造変更は未計算**。物理的な弦の到達も未認定 |
| 6. 選んだ情報を過去の受信者へ届ける | Taub内のretardedなsource応答は準備以前に0。NUT内の量子的検出確率は得ていない | **未実証**。同じ許容準備で2設定を比較する実験は未構成 |

**5は二つの要求を区別する。** 既存のCTCを使うだけなら、新たに因果構造を変えることは論理的な必要条件ではない。しかし今回求められた「到達による構造変更」は実際に評価すべき追加条件であり、ここでは達成していない。

## 2. 計算A：相対Abelian BRSTを実際の複体として検査

コード：[heterotic_taubnut_relative_brst_complex.py](../src/symbolic/heterotic_taubnut_relative_brst_complex.py)。

旧候補の電流規約のもとで

```math
K=\begin{pmatrix}8&4\\4&5\end{pmatrix},\qquad \det K=24
```

と、補助Heisenberg電流のlevel `-K` を仮定する。許容される電荷sectorと自由Fock moduleが存在し、相対条件でghost零modeを除くことも**仮定**である。これらを完全な非対称coset内に構成したとはしない。

各正mode番号n・ゲージ方向について、可逆な線形変換により、boson `x,y` とGrassmann変数 `b,c` を

```math
Qb=x,\quad Qy=c,\quad Qx=Qc=0
```

とできる。元の変数では `x=J_{-n}+\widetilde J_{-n}`、`y=(2n)^{-1}K^{-1}(J_{-n}-\widetilde J_{-n})` に対応する。微分とhomotopyは

```math
Q=\sum(x\partial_b+c\partial_y),\qquad
H=\sum(b\partial_x+y\partial_c),\qquad
QH+HQ=N_{\mathrm{occ}}.
```

したがってこの**仮定した自由oscillator module内部**では、正の有限occupationを持つ閉状態は `Q(Hv/N_occ)` としてexactになる。全有限gradeへの議論はこの恒等式によるものであり、小さい行列の成功だけから外挿したものではない。

コードはgradeを保つ全monomial基底を作り、`Q²=0`、homotopy恒等式、ghost numberごとのkernel/imageのrankを有理数で検査する。各grade Nにはmode番号1〜Nを含める。

| worldsheet grade | 基底の次元 | Qのrank合計 | cohomology次元合計 |
|---:|---:|---:|---:|
| 0 | 1 | 0 | 1 |
| 1 | 8 | 4 | 0 |
| 2 | 40 | 20 | 0 |
| 3 | 160 | 80 | 0 |

grade 0の1は**一つの仮定した電荷primaryに付随するゲージoscillator真空**であり、全string Hilbert空間の次元ではない。負例として、ghostを誤って可換にすると `Q²≠0` になることを検出する。

Hwang–Rhedin [R2, §3] の相対複体・homotopy法を参考にした限定した再現検算である。非コンパクト／非対称heterotic模型への適用条件、全string BRST、正の物理的pairingはこの計算で埋まらない。[R3] のno-ghost定理も異なるcoset族についてのもので、無条件には移植しない。

## 3. 計算B：旧候補を含む3つの必要ラベル

背景は前の監査と同じ

```math
k_1=8,\quad k_2=4,\quad \delta=\sqrt{8/5},\quad\lambda=\sqrt{2/5},
\quad t\sim t+4\pi\lambda.
```

neutral・unflowed・fermion Cartan電荷0のaffine-primary ansatzに限定する。正の整数nについて

```math
\omega_n=\frac{n}{2\lambda},\quad m=-n,\quad\bar M=\omega_n,
\quad\bar N=-\frac n2,\qquad j=\frac12+is,
```
```math
\Lambda=\ell(\ell+1)-\frac{n^2}{4},\qquad
s^2=\frac{5n^2}{8}-\ell(\ell+1)-\frac14.
```

ここで `2λω=n` はscalarのHopf周期との整合条件でもある。`0≤ell≤2`、`ell−n/2` が非負整数、`s²>0` を課すと、正周波数の組は次の3つになる。

| n | ell | s² | 左のSU(2)磁気量子数の可能な選択 |
|---:|---:|---:|---:|
| 2 | 1 | 1/4 | 0 |
| 3 | 3/2 | 13/8 | 1/2 |
| 4 | 2 | 15/4 | 0 |

半整数spinの行で左磁気量子数を0に固定してはいけない。コードはこのparityも検査する。負周波数、他の磁気縮退、discrete series、励起、charged／flowed sectorはこの「3組」の数に含めない。

ゲージ電荷と形式的な重みは

```math
m+\delta\bar M=0,\quad\lambda\bar M+\bar N=0,\qquad
h_{\mathrm{num}}=\frac{1/4+s^2+\ell(\ell+1)}6=\frac{5n^2}{48},
```
```math
\frac12(-n,0)K^{-1}(-n,0)^T=\frac{5n^2}{48}.
```

従って従来の減算規約では `h_formal=0`。**3つの完全なBRST状態を発見したという意味ではない。** 全接合を決めずにcompactラベル・零modeだけからmembershipを認定しない [R4]。中心電荷6の必要算術も確認したが、内部CFT・格子・GSOを固定したcritical heterotic完成ではない。

## 4. 計算C：principal-continuous scalarの非混合は起きない

コード：[heterotic_taubnut_horizon_transfer_family.py](../src/symbolic/heterotic_taubnut_horizon_transfer_family.py)。

Taubで `x=tanh eta`、`p=x²−1`、`D=(x+delta)²−4p/(k+2)` と置くと、同じdilaton-weighted中性scalar方程式は

```math
\ddot v+\Omega^2v=0,\qquad
\Omega^2=\omega^2D-\Lambda p,\qquad
\Omega_\pm=\omega(\delta\pm1)>0.
```

`z=(1−x)/2`、`alpha_H=i Omega_+/2`、`beta_H=−i Omega_−/2`、`h=−1/2+is`、`a=alpha_H+beta_H−h`、`b=alpha_H+beta_H+h+1` とする。未来正周波数unit-KG modeは

```math
u_{\rm out}=\frac{z^{\alpha_H}(1-z)^{\beta_H}}{\sqrt{2\Omega_+}}
{}_2F_1(a,b;1+2\alpha_H;z).
```

前のノートの `beta_H=+i Omega_−/2` 表示とはEuler変換で同じ未来modeになる。過去modeを `u_in=A u_out+B u_out*` とすると、Gauss接続公式 [R5] から

```math
|B|^2=\frac{\cosh[\pi(\omega-s)]\cosh[\pi(\omega+s)]}
{\sinh[\pi\omega(\delta-1)]\sinh[\pi\omega(\delta+1)]}.
```

**実数s、omega>0、delta>1では右辺は厳密に正。** したがってこのscalar principal continuumで「過去の純正周波数」と「未来の純正周波数」を同時に満たす非零modeはない。これは全string state、零周波数、discrete／flowed／charged sectorの排除ではない。

| n | 今回の `|B|²` | `Omega_+ |B|²/2` |
|---:|---:|---:|
| 2 | 0.0776153940803507613091343006903 | 0.138975750776715332724121323326 |
| 3 | 0.0196993368222539828199797719090 | 0.052909545015810769939693970219 |
| 4 | 0.00520610897225950648061635210933 | 0.018643798994208212069903111823 |

Gamma積と独立の双曲線関数式、`|A|²−|B|²=1`、ODEへの数値微分による再代入、Wronskian、3時刻での関数そのものの接続等式を50桁と80桁で比較した。逆接続 `u_out=A* u_in−B u_in*` も検査した。

### 4.1 有限波束の非正則成分は異なるmode間で相殺できない

選んだoutgoing未来延長 `q=t−r_*` で、非正則な成分は

```math
\Phi_{\rm bad}\sim\sum_\nu a_\nu B_\nu\,
\frac{e^{-i\omega_\nu q}|(1-x)/2|^{-i\Omega_{+,\nu}}}{\sqrt{2\Omega_{+,\nu}}}
Y_\nu.
```

相異なるnの周期Fourier因子の積分は0であり、spatial harmonicを正規直交化すれば、有限和について

```math
\lim_{x\to1}(x-1)^2\|\partial_x\Phi_{\rm bad}\|^2_{\rm Haar}
=\sum_\nu |a_\nu|^2\frac{\Omega_{+,\nu}}2|B_\nu|^2>0
```

となる。これは**参照Haar測度での平均二乗微分**であって、renormalized応力や `T_ab T^ab` そのものではない。非零incoming正周波数の有限packetが、異なるmodeの位相調整だけで全体として一様に正則になる案を排除する。個々の点での干渉や全量子状態の議論とは分ける。

一方 `u_out` はunit-KGの正則解であり続ける。初期準備を変える、またはsourceを用いる余地は残る。

## 5. 計算D：同じ初期データから正則な未来modeを作るsource

コード：[heterotic_taubnut_retarded_source_control.py](../src/symbolic/heterotic_taubnut_retarded_source_control.py)。

ここでは旧n=2 modeに限る。外部sourceを許したscalar ODE

```math
\ddot v+\Omega^2v=J
```

を考える。`rho(s)=exp(−1/s)` for `s>0`、それ以外0とし、`s=(eta+1)/2`、

```math
\chi(\eta)=\frac{\rho(s)}{\rho(s)+\rho(1-s)},\qquad
v_b=b\chi u_{\rm out},\qquad
J_b=b(\ddot\chi u_{\rm out}+2\dot\chi\dot u_{\rm out}),\quad b\in\{0,1\}.
```

`chi=0` for `eta≤−1`、`chi=1` for `eta≥1`。sourceはC-infinityかつTaub時間についてcompact supportを持つ。両設定のearly dataは厳密に同じ0で、設定1ではsource停止後に `u_out` となる。

**これは未来の境界データを設定ごとに差し替える操作ではない。** unit-Wronskian modeから作るretarded kernel

```math
G_R(\eta,\xi)=\mathbf1_{\eta>\xi}
\frac{u(\xi)u^*(\eta)-u^*(\xi)u(\eta)}i
```

にsourceを畳み込んだ結果と照合できる。source終了後の係数は

```math
A_J=i\int u^*J\,d\eta=1,\qquad
B_J=-i\int uJ\,d\eta=0.
```

`int uJ=int d(chi' u²)=0` とWronskianによって解析的にも成立し、50/80桁の数値積分で別途検査した。80桁で `|A_J−1|≈2.3e−86`、`|B_J|≈3.1e−85`。これらは丸め残差であり物理的な確率ではない。

### 5.1 NUT側へ正則に接続する値も計算

`r_*'=sqrt(D)/p`、`R=exp(i omega r_*)G` とすると、`exp(−i omega t)R=exp(−i omega q)G`。Gの方程式は

```math
pG''+(p'+2i\omega\sqrt D)G'
+\left(\frac{i\omega D'}{2\sqrt D}-\Lambda\right)G=0.
```

地平面で `d=1+delta`、`G(1)=1/sqrt(2 Omega_+)` と規約を固定すると

```math
G'(1)=\frac{\Lambda-i\omega D'(1)/(2d)}{2+2i\omega d}G(1).
```

コードでは `r_*=d log(|(1−x)/2|)/2+s(x)`、`s(1)=0` とし、見かけの0/0を有理化してから正則modeを構成する。Taub内・地平面・NUT内の5点で上のODEを検査し、

```math
G(2)=0.3309612457484620766097194706353
-0.0512702445757942643751831392371\,i
```

を50/80桁で一致させた。これは**明示した外部sourceと背景を仮定した、制御可能なscalar modeの正則な接続例**である。位相は上記のtortoise定数規約に依存する。

### 5.2 調整に対する頑健性はない

滑らかなsource誤差 `epsilon J_err`、`J_err=chi' u_out*` を加えると

```math
\delta B_J=-i\epsilon\int\dot\chi|u_{\rm out}|^2d\eta
=-0.2069259678838833303854489112468\,i\epsilon\ne0.
```

したがって任意に小さな非零epsilonで非正則な枝が戻る。正則条件はsource空間で非自明な連続線形汎関数 `B[J]=0` のkernel、すなわちcomplex codimension 1（real codimension 2）の条件であり、開集合ではない。

しかしkernelの中にも異なるsource設定はある。**「調整が必要」だけから情報選択一般を禁止することはできない。** 逆にこの構成例だけで相互作用・量子揺らぎ・source装置を含む安定性は示せない。

### 5.3 このsourceを物理的な送信者と同一視しない

sourceは選んだspatial harmonic全体に分布する、**処方された空間的に広がった制御**である。一地点の送信者が選んだbitを因果的に配布して実装する装置は作っていない。sourceを作る物質の応力保存、エネルギー収支、string BRSTとの整合性も未検査である。

`u_out` のunit-KG条件はmodeの規格化であり、設定0と1に対応する二つの正常化された量子実験の確率を与えない。単一粒子状態の全体位相だけを変えても信号にはならない。検出器・位相基準・観測量・状態準備の定義が別途必要。

## 6. backreactionとoperational signallingについて残った境界

[R1] のall-orders alpha-prime背景は、probeの応答が自動的に健全であるとの主張ではない。今回も固定背景であり、`delta g=0`。scalar微分の増大をそのまま弦理論の曲率発散と読まない。KRW [R6] も、仮定したCauchy horizon上の場の二点関数の結果であり、今回の全string theoryへの普遍的禁止ではない。

string field theory側では、背景BRST微分をQとする線形source方程式 `Q Psi=J_string` には少なくとも `Q J_string=0` が必要である（nilpotencyから）。ここで構成したscalar Jについて、そのliftは得ていない。相互作用には適切なstring productsと背景多重項の応答が必要 [R7]。Abelian oscillator複体の検算はこれらを代替しない。

操作的な判定は、以前と同じ

```math
\Delta_B=\frac12\sum_y|P(y_B\mid\mathrm{do}(b=0))-P(y_B\mid\mathrm{do}(b=1))|
```

である。同じ設定選択以前の準備、同じ大域的接続規則を保ち、postselectionなしで `Delta_B>0` を得る必要がある。

今回のretarded scalar構成では、Taub内でsourceより前の点の応答差は厳密に0。これは通常の前向き制御の検算であって、NUT内の受信者の量子論を解いたことではない。完全な時空でchronalな過去の受信者については、前の[条件付きLean補題](../src/lean/ChronologySixGate.lean)の範囲を維持する。既にCTC領域内にある受信者はその補題だけでは排除されない。

**NUT内での二つの許容された量子実験、全backreaction、非零の過去検出確率は今回得られていない。** したがって「過去へ情報を送れた」とは記録しない。同時に「全状態が必ず壊れる」とも記録しない。

## 7. 再現・公開・次の再開点

```bash
python src/symbolic/heterotic_taubnut_relative_brst_complex.py
python src/symbolic/heterotic_taubnut_horizon_transfer_family.py
python src/symbolic/heterotic_taubnut_retarded_source_control.py
```

ローカル：Python 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0。3本ともsuccess。relative複体は厳密整数／有理数。後2本は50/80桁の任意精度浮動小数で、interval arithmeticではない。transferの80桁最大残差はODE `3.1e−81`、Wronskian `3.2e−81`、関数接続 `3.1e−81`。source-controlの正則ODE残差は `4.5e−81` 以下。source積分の初回は実行時間上限に達したため、working precisionもkeyに含むmodeキャッシュを導入して再実行した。精度・assertは下げていない。

3本は共有import・参照データ・新規依存なしの独立script。参照JSONやworkflowを変更せず、通常PRの既存選別器で対象と理由を記録する。Leanは変更せず再実行対象にしない。**remote CIの実際のSHA・run・結果はPRに記録する。ローカルsuccessをremote successと呼ばない。**

今回追加したものは状態候補とsource側の境界を明確にする計算であり、完全なHilbert空間の構成ではない。次の再開点はこのノートで、NPQT側ではない。まずneutral unflowed候補の左右branching、補助電荷、内部CFT、GSO、物理pairingを確定し、その状態に結合できる空間的に局在したBRST-closed sourceを構成する。その後に正規化相関関数から全背景sourceを求め、同じ初期準備の二設定で検出確率を比較する。未知の入力を「自明」と置いて6条件をPASSにしない。

## 一次資料と今回の確認範囲

- **[R1]** C. V. Johnson, H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, [hep-th/0405141](https://arxiv.org/abs/hep-th/0405141)。§3の異常・中心電荷、導入／結論のprobe問題との区別を確認。
- **[R2]** S. Hwang, H. Rhedin, *The BRST Formulation of G/H WZNW Models*, [hep-th/9305174](https://arxiv.org/abs/hep-th/9305174)。§3のrelative条件・homotopyと表現の仮定を確認。
- **[R3]** J. Bjornsson, S. Hwang, *On the unitarity of gauged non-compact WZNW strings*, [0710.1050](https://arxiv.org/abs/0710.1050)。abstractの対象coset・no-ghostの適用範囲を確認。
- **[R4]** T. Quella, V. Schomerus, *Asymmetric Cosets*, [hep-th/0212119](https://arxiv.org/abs/hep-th/0212119)。書誌・abstractを再確認。接合の詳細は既存の文献対照ノートを参照し、今回Taub–NUTのmodular invariantを再構成していない。
- **[R5]** NIST DLMF, [15.8: Transformations of Variable](https://dlmf.nist.gov/15.8)。Gauss関数の接続公式。コードの通常のhypergeometric関数とDLMFの正規化表記を区別。
- **[R6]** B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, [gr-qc/9603012](https://arxiv.org/abs/gr-qc/9603012)。abstractの仮定と二点関数の結論を確認。今回の背景で定理の全仮定を検証したとはしない。
- **[R7]** H. Kunitomo, T. Sugimoto, *Heterotic string field theory with cyclic L-infinity structure*, [1902.02991v4](https://arxiv.org/abs/1902.02991v4)。NS/Rを含むgauge-invariant構成と版履歴を確認。Taub–NUT固有のproducts／振幅は未計算。

文献確認は限定検索と上記範囲の再読であり、最新研究の網羅や未発見の証明ではない。R1/R2のPDFは抽出テキストを確認したが、今回のweb screenshotは取得エラーとなり、ページ画像による再確認はできなかった。新規式の検算は上記の独立scriptに残している。
