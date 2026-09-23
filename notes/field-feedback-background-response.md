# 接続時の場・背景応答：測定雑音、操作依存の応力、正則な周回状態の障害

**2026-09-23。基点：main `43e22f1012f41736e015c889fe8fc0bddd5b41ff`（PR #12マージ後）。**
[前回の接続検査](chronology-loophole-attack.md)と[場・送受信器の導出](taubnut-field-detector-closure.md)を引き継ぐ。

> **今回の到達点：** 同じ場・検出器の測定結果をコピー／反転して送信する操作から、場の状態変化と背景を駆動する応力の差を導出した。
> さらに、**送信に使う場の観測量を保存して戻す構成には、非零の交換子がある限り正則な周回固定状態がない**ことを示した。
> **大域NUTの戻り写像、計量の全反作用、自然界一般の禁止を導いた結果ではない。** 散逸や別の戻り写像は対照として残す。

## 0. 判定の範囲

| 問い | 結果 |
|---|---|
| 測定・記録・コピー／NOTは場を変えるか | **変える。** connected二点関数にも操作依存の項が出る。単なる古典sourceの議論では足りない |
| 同じ観測量Aを保存して戻す無損失構成は成立するか | **条件付きで不可。** 全状態を対象としたWeyl恒等式から正則固定状態の不存在を導く |
| 何らかの損失を入れても不可能か | **その一般化は不可。** 正の環境雑音を持つ減衰模型では当該周辺量に有限の定常分散がある |
| 背景に与えるsourceは分かったか | **診断用スカラーの状態差による応力・dilaton sourceを導出。** 装置・環境を含む全sourceや全計量応答は未導出 |
| 小さい反作用でCTCが必ず消えるか | **不可。** 内部の厳密にtimelikeな閉曲線は十分小さい計量摂動で残る |
| 過去通信が自然界で可能／不可能か | 成功例・普遍的no-goは得ていない。今回は具体的な保存型周回構成を棄却 |

既存のKRW棄却と操作非依存processのno-goは維持する。今回の結果をそれらから独立な確率証拠として数えず、「10%」の数値を機械的に下げない。新規性・優先権は主張しない。

## 1. 使う場と、まだ仮定している実験領域

計量・dilatonはJohnson–Svendsen [J, (72),(73),(79)] とrepoの規約：

```math
p=x^2-1,\quad D=(x+\delta)^2-\frac4{k+2}p,\quad K=(k-2)\alpha',
```
```math
g=K[p^{-1}dx^2-pD^{-1}(dt-\lambda\cos\theta\,d\phi)^2+d\Omega_2^2],
\quad \Phi=-\tfrac14\log D,\quad t\sim t+4\pi\lambda.
```

定数Phi_0は0。診断用の実massless scalar作用は四次元で

```math
S_\varphi=-\tfrac12\int\sqrt{-g}\,e^{-2\Phi}g^{ab}\partial_a\varphi\partial_b\varphi
=-\tfrac12\int\sqrt{-g_E}\,g_E^{ab}\partial_a\varphi\partial_b\varphi,
\qquad g_E=e^{-2\Phi}g=\sqrt D\,g.
```

これはスカラー作用の書換えであり、full heterotic作用をEinstein重力＋一場へ切り詰めてよいという定理ではない。
NUTの全域はglobally hyperbolicでない。以下ではまず、正の場代数・正しい順序を持つ開いた実験領域での操作を求める。小さいNUT chartにも局所的な場の理論を定義できるが、そのchartを一周する実験へ拡張したとはしない。
[F1,F2] の検出器／局所probe手法の適用仮定をこの点で保持する。

結合を含む実smooth compact smearingで

```math
A=\varphi(f_A),\quad B=\varphi(f_B),\quad [A,B]=i\delta_c\mathbf1
```

とする。delta_cは背景のdeltaと別。smearingの体積要素はg_E。点状の裸の場やFock cutoffは使わない。

## 2. 前回の装置に、記録に基づく制御を入れる

実験室の順序を **受信測定B → 記録yを運ぶ → 送信制御A** とする。受信qubitを場と独立な `|+x>` に準備し、

```math
U_B=\exp(-iZ_B B)
```

で相互作用させ、Pauli Yの結果y=±1を記録する。場に誘起するKraus演算子は

```math
M_y=\langle y_Y|U_B|+x\rangle
=\tfrac12(e^{-iB}-iy e^{iB}),\qquad \sum_yM_y^\dagger M_y=1.
```

その結果に従い、同じ送信相互作用の符号を変える：

```math
D_{r_y}=e^{ir_yA},\qquad
r_y=+1,\ -1,\ y,\ -y
```

をそれぞれ固定0、固定1、コピー、NOTと呼ぶ（y=+1をbit 0に対応させる）。全操作は

```math
N_y^{(f)}=D_{r_y}M_y,\quad
\mathcal E_f(\rho)=\sum_yN_y^{(f)}\rho N_y^{(f)\dagger}.
```

全てCPTP。制御方式fを確率q_fで選ぶflag Fも保持すると

```math
\rho'_{FY\varphi}=\sum_{f,y}q_f|f,y\rangle\langle f,y|\otimes N_y^{(f)}\rho N_y^{(f)\dagger}.
```

従って `P(F=f)=q_f`。未来の成功flagによる再正規化をしていない。incoming fieldと受信qubitの未知の相関を無視できることや、記録の搬送・qubit準備が可能なことは、実装の仮定である。
CTC上の全装置が自動的にこのCP分解を持つとは言わない。

## 3. 場の完全な特性関数と応力の変化

### 3.1 Gaussian入力に対する厳密式

初期状態omegaは平均0のquasifree状態。任意の実smearing hに対して

```math
H=\varphi(h),\quad a_h=\Delta(f_A,h),\quad b_h=\Delta(f_B,h),
\quad c_h=\tfrac12\omega(\{B,H\}),\quad V_h=\omega(H^2),
\quad V_B=\omega(B^2),\quad\nu=e^{-2V_B}.
```

Weyl関係から、記録yを保持した未正規化の特性関数が

```math
\chi_{f,y}(h)=\omega(M_y^\dagger D_{r_y}^\dagger e^{iH}D_{r_y}M_y)
=\frac12e^{ir_ya_h-V_h/2}[\cos b_h+iy\nu\sinh(2c_h)]
```

となる。h=0ではP(y)=1/2。これは任意入力ではなく平均0 Gaussian入力での値であり、次の周回で再度P(y)=1/2と仮定してはいけない。

コピー／NOTをk=+1／−1と書くと、yを全て足して

```math
\boxed{\chi_k(h)=e^{-V_h/2}[\cos a_h\cos b_h-k\nu\sin a_h\sinh(2c_h)] .}
```

固定送信r=±1なら `chi_r(h)=exp(ir a_h-V_h/2) cos b_h`。
これは場そのものの状態変化であって、通信核Kの分母を手で変えた式ではない。
**出力は一般にGaussianでない。** コードでは四次cumulantが非零の正の正準Gaussian入力例も検査する。以後の読み出しを分散だけで計算するGaussian近似は使わない。

### 3.2 connected二点関数は変わる

コピー／NOTの平均は0で、二次微分から

```math
\boxed{V_k(h)=V_h+a_h^2+b_h^2+4k\nu a_hc_h .}
```

固定送信は平均r a_h、connected分散 `V_h+b_h²`、raw二次モーメントは `V_h+a_h²+b_h²`。
固定した古典sourceのdisplacementだけならconnected二点関数を変えない、という前回の結果とは矛盾しない。今回は**測定・条件付き操作・全結果の混合**を追加したのである。

記録yに条件付けた平均は `r_y a_h+2y nu c_h`、connected分散は `V_h+b_h²−4nu²c_h²`。
正値性はKraus構成から従う。さらに `c_h²≤V_B V_h` を使うと

```math
V_k(h)=(a_h+2k\nu c_h)^2+V_h+b_h^2-4\nu^2c_h^2
\ge(1-e^{-1})V_h+b_h^2.
```

最後は `4V_B exp(-4V_B)≤1/e` による。相関項が負になることを理由に不正な状態とはしない。

### 3.3 背景を駆動する応力の操作依存項

`e_A(z)=Delta(f_A,z), e_B(z)=Delta(f_B,z), c_B(z)=Re W(f_B,z)` とする。
正しい局所Hadamard理論では全てsmooth homogeneous solutions。二点関数の差は

```math
\delta W_k=e_A\otimes e_A+e_B\otimes e_B
+2k\nu(e_A\otimes c_B+c_B\otimes e_A).
```

smoothな差なので、同一背景でのpoint splittingによる応力差には共通の繰込み定数が消える。[M, Appendix B] のsmooth covariance差に関する事実と整合する。
ただし本操作は非GaussianなCP mapであり、[M]のsymplectic finite-rank定理そのものを適用したとは言わない。

```math
t_{ab}(u)=\nabla_a u\nabla_b u-\tfrac12(g_E)_{ab}(\nabla u)^2,
```
```math
\mathcal B_{ab}(u,v)=\nabla_a u\nabla_b v+\nabla_a v\nabla_b u
-(g_E)_{ab}\nabla^c u\nabla_c v,
```
```math
\boxed{\delta\langle T^E_{ab}\rangle_k=t_{ab}(e_A)+t_{ab}(e_B)+2k\nu\mathcal B_{ab}(e_A,c_B).}
```

よって **copy−NOTの応力差は `4nu B_ab(e_A,c_B)`**。固定0と固定1のraw応力は同じ。
任意のnull接ベクトルlへの射影差は `8nu(l·∇e_A)(l·∇c_B)` で符号不定。
「フィードバック反作用は常に正のエネルギーなのでCTCを消す」とは導けない。負の状態差と絶対エネルギーの負値も別である。

これは固定背景上の物質応答を全結合次数で求めた式。装置・switchingの仕事と応力、全背景の量子揺らぎは含めていない。
[H] のとおり、平均応力を知るだけで半古典重力の妥当性が保証されるわけでもない。

## 4. 保存型の戻り部には、正則な固定状態がない

### 4.1 初期状態に依存しない恒等式

送信操作 `exp(ir_y A)` はAの任意の関数と可換。従って任意のr_+,r_-、任意の場状態について

```math
\boxed{\mathcal E_f^*(e^{isA})=\cos(s\delta_c)e^{isA}.}
```

これはGaussian特性関数の反復ではなく、Weyl演算子積を直接簡約した恒等式。全Kraus分岐をコードで検査する。
有限二次モーメントがあれば

```math
\mathcal E_f^*(A)=A,\qquad \mathcal E_f^*(A^2)=A^2+\delta_c^2.
```

測定が送信観測量へ加える雑音は、コピー・NOT・固定送信のいずれでも同じで、同じAを生成子とする送信制御では除去できない。

### 4.2 周回整合性を課した条件付きno-go

戻り部Rが `R^*(exp(isA))=exp(isA)` を満たすと仮定する。全場のidentity returnまでは不要で、AのWeyl族を保存すればよい。
このRが実際のNUTから導かれたとはしない。時空のt周期性だけから、相互作用する場の戻り写像がこの性質を持つとは推論できない。

一周map `R∘E_f` の固定状態があれば、その特性関数chiは

```math
\chi(s)=\cos(s\delta_c)\chi(s),\qquad\chi(0)=1
```

を満たす。delta_c≠0として `s_n=1/(n delta_c)` を取ると、全てのnでcos(1/n)≠1なのでchi(s_n)=0。
s_n→0でchi(0)=1と矛盾する。

> **命題：上の測定・同じAでの送信制御・Aを保存する戻り写像・独立準備された受信probeという構成には、delta_c≠0のとき正則な固定状態が存在しない。**

正則とはWeyl族の期待値がsに連続であること [M, Appendix A]。
有限分散だけでなく、無限分散だが正則な状態へ逃げることもできない。Hadamard／通常のquasifree状態は正則。
これは全CTC量子論のno-goでも、全点で応力が発散するとの命題でもない。
N回反復できると仮定した場合には `Var_N(A)=Var_0(A)+N delta_c²` だが、N回実験やエネルギーの実在をここから断定しない。

δ_c=0ではこの矛盾は消える。同時に前回のsimple-generated符号化の送信信号も0になるが、別の観測量・別符号化の通信を禁止する結果ではない。

## 5. 反作用・環境がこの障害を救う可能性も検査

Aを正準quadratureとして規格化した一つのmodeの減衰環境を**比較模型として追加**する。戻り部を透過率eta、環境分散V_envで

```math
R_\eta^*(e^{isA})=e^{-(1-\eta)V_{\rm env}s^2/2}e^{i\sqrt\eta sA},\quad 0\le\eta<1
```

とすると

```math
V_{n+1}=\eta(V_n+\delta_c^2)+(1-\eta)V_{\rm env},\qquad
V_*=V_{\rm env}+\frac{\eta\delta_c^2}{1-\eta}.
```

**有限である。** 当該一観測量の定常特性関数も

```math
\chi_*(s)=e^{-V_{\rm env}s^2/2}\prod_{j=1}^{\infty}\cos(\delta_c\eta^{j/2}s)
```

として連続・正定値に構成できる。Gaussian変数と独立な符号付き幾何減衰キックの和の特性関数であり、単なる分散の形式解ではない。
コードは有限積・再帰式・尾部上界 `delta_c² s² eta^(N+1)/(2(1−eta))` を検査。
**全場・全観測量の固定状態や、過去の受信統計の構成ではない。**

正準規約[Q,P]=iで、位相非依存の量子attenuatorには `V_env≥1/2` が必要。
`X=sqrt(eta)I, Y=(1−eta)V_env I` に対するCP条件を検算し、真空雑音を削除したeta<1の写像が不適合となる負例も保持する。

NUTにそのようなreservoir・新鮮な環境・熱の逃げ先が存在することは導いていない。
それでも、この対照を残すことで「測定雑音があるから全ての散逸付きCTC装置も不可能」という誤った結論を避ける。

## 6. 実際のTaub–NUT計量に対する応力と背景応答の条件

### 6.1 計量・dilatonのsourceを混同しない

元のスカラー作用をg,Φで変分すると

```math
T^g_{ab}=e^{-2\Phi}t^g_{ab}(\varphi),\qquad
\mathcal O_\Phi=\frac1{\sqrt{-g}}\frac{\delta S_\varphi}{\delta\Phi}
=e^{-2\Phi}(\nabla\varphi)^2_g.
```

sourceのないところでも一般に

```math
\boxed{\nabla_g^aT^g_{ab}=\mathcal O_\Phi\nabla_b\Phi,}
```

であって、g-frameのスカラー応力だけを保存されたEinstein方程式のsourceと扱ってはいけない。
結合中はさらにsource装置・switchingの力がある。同一背景での状態差にも同じWard恒等式が成立する。
一方g_Eでの最小結合スカラーの応力差は、結合領域の外で保存される。

これは背景応答を解くための必要なsource整合性である。full heterotic模型はmetricだけでなくdilaton・B-field・gauge fieldsを持つ [J]。
概念的には背景多重項q^Iについて `L_IJ δq_f^J = δJ_I^(field,f)+δJ_I^(apparatus,f)` を、正しい境界条件・量子応答込みで解く必要がある。
**このLの逆やδg_f、装置の応力を今回計算したとはしない。** 固定k=8のexact幾何へ、未検証の最低次Einstein方程式だけを当ててfull string backreactionと呼ばない。

### 6.2 実計量での独立した応力・Ward検査

radial homogeneous solution `u(x)=log[(x−1)/(x+1)]/2` は `∂x(p u')=0`。
そのテンソルt_E(u)を、実際の四次元metric inverseから独立計算すると

```math
t^E_{xx}=\frac1{2p^2},\quad t^E_{tt}=\frac1{2D},\quad
 t^E_{t\phi}=-\frac{\lambda\cos\theta}{2D},\quad
 t^E_{\theta\theta}=-\frac1{2p}.
```

phi-phi成分も含めてコードで検査し、E-frameの保存とg-frameの非零dilaton項を照合した。
例えば `e_A=a u, e_B=b u, c_B=c u` という形の**局所応力計算の対照**なら、応力は `(a²+b²+4k nu a c)t_E(u)`。
この形のe,cを物理的なglobal smear／Hadamard状態から構成したとはしない。uは地平面で発散し、NUT全域の正規化状態ではない。対照tensorを通信率へ転用しない。

### 6.3 小さい反作用だけでは内部CTCは消えない

固定した閉曲線gammaのg_E-unit接ベクトルnはg_E(n,n)=−1。
同じmanifold・同じ曲線の同一視の下で、h=δg_Eに

```math
\sup_\gamma|h(n,n)|<1
```

があれば(g_E+h)(n,n)<0のまま。連続な時間向きも保てる。これは特定ゲージの一成分を観測量と見なすのでなく、同一視した曲線上のtensor評価である。

repoの値 `k=8,delta=sqrt(8/5),lambda=sqrt(2/5),alpha'=1` で

```math
-g^E_{tt}|_{x=2}=5.852414840058954925865990862202\ldots.
```

殻x∈[1.5,2.5]ではその下限が `2.8058745871294484574891137714341...`。
p/sqrt(D)の単調性を厳密に導き、50/80桁でも比較した。
**これらは許容摂動の幾何学的余裕であって、実際のhや崩壊エネルギーではない。** 小さい応力から小さいhが従うことも、背景の応答を解かずには保証できない。
大きい／特異な反作用でCTCが消える可能性は残る一方、「少しでも装置を置けば必ずCTCが消える」はこの幾何からは出ない。

## 7. 検証・再開点

```bash
python src/symbolic/field_feedback_backreaction.py
python src/symbolic/taubnut_feedback_stress.py
```

ローカル Python 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0。
Weyl wordを正規形まで直接簡約し、任意制御r_+,r_-の恒等式とKraus completenessを検算。
Gaussian入力の厳密式に加え、無限次元Schrodinger表現 `A=0.7P, B=0.6Q` で、変換された波動関数を独立積分した。

| 比較模型の操作 | Q二次モーメント | P二次モーメント |
|---|---:|---:|
| 固定0／固定1 | 0.99 | 0.86 |
| コピー | 0.403951886100333911944331418376... | 0.86 |
| NOT | 1.57604811389966608805566858162... | 0.86 |

入力はいずれも1/2。A方向の雑音増分は(0.7×0.6)²で操作非依存。**Taub–NUTの数値予測ではない。**
積分は50/80桁・40桁以上一致。初回の無限区間求積が時間上限に達したため、Gaussian尾部の解析的上界を置いた有限区間Gauss–Legendre積分に変更した。積分打切り誤差は10^(−dps−20)未満に制御し、既存の一致assert・精度は下げていない。丸め・求積全体をinterval arithmeticで形式保証したものではない。

新規2本は独立で共有import・入力data・依存・workflow・Leanの変更なし。通常のPR累積差分選別を使用。remoteの実際のhead・checkout・対象・結果はPRに記録する。
git cloneはDNS失敗し、全repoをローカルで再実行したとはしない。全ソースcompileと全研究計算の実行は区別する。

**次の検証対象は具体化した。** 保存型の戻り部は棄却し、NUTの実際の戻り写像がAをどう混合・減衰させるか、必要なreservoir／装置応力／dilaton sourceが同時に整合するかを調べる。
新しい比較模型のetaをNUTから導いたものと置いて成功にしない。場の状態だけの固定点では、外部へ記録されたビットと過去の受信確率の証明にならない。

## 一次資料と確認した範囲

- **[J]** C. V. Johnson, H. G. Svendsen, *An Exact String Theory Model of Closed Time-Like Curves and Cosmological Singularities*, [hep-th/0405141](https://arxiv.org/abs/hep-th/0405141)。PDF (72),(73),(79)、pp.24–25のmetric/dilaton、結論のprobe backreactionの留保を確認。web screenshotは取得エラーだったためページ画像を確認済みとはしない。
- **[F1]** E. Tjoa, K. Gallock-Yoshimura, *Channel capacity of relativistic quantum communication with rapid interaction*, [2202.12301](https://arxiv.org/abs/2202.12301)。局所qubit–fieldの非摂動手法とglobally hyperbolicの前提。今回のfeedback式を論文の既出式と断定しない。
- **[F2]** C. J. Fewster, R. Verch, *Quantum fields and local measurements*, [1810.06512](https://arxiv.org/abs/1810.06512)。CP instrument、局所coupling、因果的順序を持つ合成の前提を確認。全NUTへの拡張定理ではない。
- **[M]** J. Mandrysch, M. Navascués, *Quantum Field Measurements in the Fewster-Verch Framework*, [2411.13605v2](https://arxiv.org/html/2411.13605v2)（2025-10-28改訂）。HTML §2–3、Appendix Aのregularity、Appendix Bのsmooth covariance差を確認。非Gaussianな今回のmapをsymplectic変換と同一視しない。
- **[H]** B. L. Hu, E. Verdaguer, *Stochastic Gravity: Theory and Applications*, [0802.0658](https://arxiv.org/abs/0802.0658)。平均応力とnoise kernelを区別する枠組みを参照。NUTのEinstein–Langevin解を借用したわけではない。

有限の指定模型・文献範囲での導出と反証試行である。全string spectrum、全相互作用、全時空を網羅した調査ではない。
