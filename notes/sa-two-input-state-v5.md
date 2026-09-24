# SA候補の継続v5：二入力の逆散乱、非平衡な準備雑音、有限パルス

**2026-09-25。読取基点：`7724b58b6f571d01c35f6a1ef411aee9d79d62dd`（PR #24マージ後）。**
対象は [Schein–Aichelburgの二荷電殻](https://arxiv.org/abs/gr-qc/9606069)を使うB候補。
[前回の境界・受信ノート](sa-quantum-record-v4.md)と、[先行する散乱尾のノート](sa-quantum-channel-gate.md)を継続する。
MP外部を直接接合する別案の結果は混ぜない。原[A/B/Cプロトコル](../docs/4d-past-signalling-protocol.txt)は変更しない。

## 0. 結論

**Aは未取得。全候補はBの継続であり、今回は一件のBとして記録する。**
以下は四次元RN内部の線形場に対する構成・制約で、全SAの量子状態や過去通信の完成ではない。

1. 既知の**全周波数・全角モードの逆散乱定理**を使えば、内側地平面の指定した二つの出力に対応する、有限の縮退Killingエネルギーを持つ二入力を構成できる。一つの危険な極の相殺だけより強いが、入力の有限時間・外部からのアクセス・全地平面の正則性は保証しない。
2. 一方の出力差を完全に零にし、他方だけへ非零の信号差を出す設計には、一般に**両入力を送信ビットに応じて変える必要がある**。反対側を固定したまま、事前の量子もつれと片側の局所操作だけで置換することはできない。これは明記した線形平均信号と出力指定の制約で、全通信方式の禁止ではない。
3. 正のGaussian混合による**非平衡な状態変更**を明示し、平均だけでなく追加共分散・全相対応力を同じ式で計算した。第一散乱尾を消すには平均の条件に加えて、準備雑音の共分散の条件が必要。非零の準備雑音でもその条件を満たす族がある。ただし**基準状態の量子雑音を除去したわけではない**。
4. 最初の尾を消す非零の滑らかな有限パルスを最適化した。固定した台と積分値で、前回の波形より地平面入力エネルギーを**約36.53%低減**する明示的な滑らか族を得た。これは受信誤り率や装置の総仕事を固定した最適化ではない。

**全SAの応答核、Lorentzianな基準量子状態、全RSET、送信者から二入力へのアクセス、過去側の受信確率は未構成。**
`P(Y|do(0)), P(Y|do(1)), D_past` は全てnull。下記の四次元散乱と条件付き状態変更を合成して、完成した装置とは呼ばない。

## 1. 文献を利用する前の再監査

### 1.1 Taylorの正則状態を「完成した大域状態」として借りない

[T20]は二重の解析接続で得た負定値計量上で二点関数を構成し、内側地平面で有限な繰込み応力を得る。
ただし**同論文§6（PDF pp.14–15）は、Lorentzian時空への一意な解析的継続と、物理的解釈を未解決としている**。
事象地平面で特異であると予想するが、その証明はしていないとも述べる。

従って、先行ノートの「正則状態の存在」は、同論文の構成と留保を合わせた範囲で読む必要がある。
ここで[T20]を全SAにおける正値・CCR・Hadamard条件と外部準備を全て解決する種として使わない。
**この再監査は同論文の有限応力の計算を否定したものでも、Lorentzian状態の不存在証明でもない。**

### 1.2 逆散乱に使うのは量子CTC処方ではない

[KSR] Proposition 3.3 / Theorem 3は、実際の四次元RN波動方程式から得られた線形散乱写像の有界な逆を与える。
使用するのはこの定理で、Deutsch固定点、P-CTC、未来の事後選別を導入しない。
出力を指定する逆設計問題と、その入力を実際の装置で準備して出力を測る実験は別である。
台帳でも、**この段階では未来側の目標波形を数学的な設計入力として指定している**ことを明示する。

## 2. 四次元の式と数値計算領域

自然単位 `c=hbar=1` とし、RN内部を

```math
ds^2=-f(r)dt^2+f(r)^{-1}dr^2+r^2d\Omega_2^2,
\quad f=1-\frac{2M}{r}+\frac{Q^2}{r^2},
\quad r_\pm=M\pm\sqrt{M^2-Q^2}
```

とする。信号は中性・実・質量ゼロ・最小結合scalar。量子支持源を二次元CFTへ置き換えない。
ここでの有限周波数の新計算は **`Q/M=.99`, `r_-<r<r_+`** に限る。
SAの殻に関する以前の `M=R/5` という長さ尺度へ戻せるが、ここでは内部スケールMを1として解く。

omegaはKilling座標tに共役なFourier変数である。地平面間ではtは空間的で、rが時間的になる。
外部の送信器・受信器で測る周波数と、この変数を無条件に同一視しない。

球面調和関数を使い `phi=e^{-i omega t} Phi(r)Y_lm` と書けば、四次元KG方程式は

```math
\frac{d}{dr}\left[\Delta\frac{d\Phi}{dr}\right]
+\left[\frac{\omega^2r^4}{\Delta}-l(l+1)\right]\Phi=0,
\quad \Delta=(r-r_+)(r-r_-).
```

`d=r_+-r_-`, `x=(r_+-r)/d`, `s=log(x/(1-x))` とおくと

```math
\Phi_{ss}+\left[\left(\frac{\omega r^2}{d}\right)^2+l(l+1)x(1-x)\right]\Phi=0.
```

この変換は代数で検算した。地平面基底は `exp(±i nu_h s)/r_h`, `nu_h=omega r_h²/d`。
場の係数にr_hを含めることで、両端の保存流束の規格化を一致させる。
通常のtortoise座標の原点との差は固定位相であり、以下の絶対値・逆写像・エネルギー比に影響しない。
MP外部は非球対称なので、これを外部まで独立なlモードが伝わる結果へ延長しない。

## 3. 指定出力から入力を逆算する

各実周波数・角モードの、r_hを掛けた放射振幅を使うと

```math
\begin{pmatrix}G_1\\G_2\end{pmatrix}
=S\begin{pmatrix}F_A\\F_B\end{pmatrix},
\quad S=\begin{pmatrix}{\cal T}&\overline{\cal R}\\{\cal R}&\overline{\cal T}\end{pmatrix},
\quad |{\cal T}|^2-|{\cal R}|^2=1.
```

[KSR]の有界逆は

```math
S^{-1}=\begin{pmatrix}\overline{\cal T}&-\overline{\cal R}\\-{\cal R}&{\cal T}\end{pmatrix}.
```

従って、`(G1,G2)=(g,0)` という非零の目標に対して

```math
F_A=\overline{\cal T}\,g,\qquad F_B=-{\cal R}\,g
```

が具体的な逆設計である。gは実場のreality条件を保つスペクトルとする。
例えば滑らかな有限時間波形のFourier変換をgとしても、定理のエネルギー空間に入り、逆入力の有限な縮退Killingエネルギーが保証される。
**逆入力自体が有限時間で終わること、自由落下系の応力が有限であること、全地平面を滑らかに延長できることは保証されない。**
出力の二つのcharacteristic traceを指定することと、全横断微分や全量子状態を指定することも違う。

これは**全周波数で定義された逆写像**であり、下の4点を補間しただけの構成ではない。
その存在は文献の定理に依存し、コードは有限周波数で実際のODEと逆写像を別に検算する。
また擬ユニタリな古典流束を、量子チャネルの透過確率や自動的な量子Bogoliubov実装と解釈しない。

### 3.1 数値で得たスペクトルごとの入力エネルギー係数

正の和として定義した二入力のKillingエネルギー密度は、目標gのそれに対して

```math
\mathcal C(\omega,l)=|{\cal T}|^2+|{\cal R}|^2
```

となる。全波束の比はこの量の `omega²|g(omega)|²` による加重平均である。
**単色モードは正常化された信号ではなく、下表の値は全波束・装置のコストではない。**

| omega/kappa+ | l | C(omega,l) |
|---:|---:|---:|
| .02 | 0 | 1.165600581250660 |
| .2 | 0 | 1.153375356663787 |
| 2 | 0 | 1.001683943606679 |
| .2 | 1 | 1.153089171839018 |

[KSR] Proposition 2.5の零周波数係数を別に照合すると

```math
{\cal T}_0=\frac{(-1)^l}{2}\left(\frac{r_-}{r_+}+\frac{r_+}{r_-}\right),
\qquad {\cal R}_0=\frac{(-1)^l}{2}\left(\frac{r_-}{r_+}-\frac{r_+}{r_-}\right).
```

| Q/M | 低周波極限C0 | 第二入力が負担するエネルギー比率の極限 |
|---:|---:|---:|
| .5 | 97 | .49484536 |
| .9 | 3.31672001 | .34924866 |
| .99 | 1.16573044 | .07108438 |
| .999 | 1.01605613 | .00790120 |

近極限化はこのスペクトル上の制御量を改善する。
これを電荷の維持、放電、地平面の安定性、過去通信の成功確率の改善率とは解釈しない。

### 3.2 「事前にもつれさせて、後は片側だけ操作」は代わりにならない

[KSR] Theorem 4は、片側入力から反射側への作用素Rのkernelが零であることを示す。
反対側の入力を同一に保って二ビットの差を取ると

```math
\delta F_B=0,\quad \delta G_2={\cal R}\,\delta F_A.
```

`delta G2=0` を全波形について要求すれば `delta FA=0`、従って `delta G1=0`。
非零の目標 `(delta g,0)` をこの制御クラスでは作れない。

事前の量子相関はこの**平均波形の制約**を避けない。独立な二つの入力系（または局所操作と可換な反対側の観測代数）として分離できる範囲で、A側だけのtrace-preserving局所操作なら

```math
\rho_B'=\mathrm{Tr}_A[(\mathcal E_A\otimes I)\rho_{AB}]=\rho_B.
```

B側の平均入力をビットに応じて変えられないためである。
測定結果の事後選別はここでは使わない。普通の通信でB側へ制御情報を先に届ける場合は、別の操作であり、まさにその因果的アクセスを示す必要がある。
**反射出力を零にすることは過去通信一般の必要条件ではない。** 反射を許す符号、非線形操作、他の観測量を禁止した結果ではない。

## 4. 非平衡な状態を、共分散と応力まで含めて変更する

前節は古典的な平均信号の逆設計。以下は**別の、実装可能性を詰めるための量子状態変更の計算**である。
適切なHadamard基準状態omega0を、まずRN内部の通常のglobally hyperbolicな領域D上に与える。
全SAへ接合されたomega0を得たとはしない。実の滑らかな四次元解u_s,u_iを同じ場の方程式と同じ接合規則から取る。

古典Gaussian変数 `xi~N(0,Sigma)`, `Sigma>=0` を使い、各実現で

```math
\phi\longmapsto\phi+(-1)^b u_s+\sum_i\xi_i u_i
```

というcoherent変位を行った状態の混合を定義する。Weyl代数上では、coherent automorphismで写した正の状態の確率混合なので正値性・正常化・CCRを保つ。
基準状態がGaussianなら、Weyl特性関数は

```math
\chi_b(F)=\chi_0(F)
\exp\left[i(-1)^b u_s(F)-\frac12\boldsymbol u(F)^T\Sigma\boldsymbol u(F)\right].
```

従って、同じ基準状態に対するconnected二点関数の変化は

```math
W_b^{\rm conn}(x,x')-W_0(x,x')=\sum_{ij}\Sigma_{ij}u_i(x)u_j(x').
```

D内でu_iが滑らかなら差はsmoothで、Hadamardの短距離構造も保つ。
**u_iやW0を地平面の先へ滑らかに延長できることは、別に示す必要がある。**

最小結合の4Dテンソルを

```math
\mathcal B_{ab}(u,v)=\nabla_{(a}u\nabla_{b)}v
-\frac12g_{ab}\nabla_cu\nabla^cv
```

とすると、基準が零平均である領域では

```math
\Delta\langle T_{ab}\rangle_{\rm ren}
=\mathcal B_{ab}(u_s,u_s)+\sum_{ij}\Sigma_{ij}\mathcal B_{ab}(u_i,u_j).
```

0/1で同一。各uがsource-freeならこの差は保存する。駆動中はJによる仕事の項を加える必要がある。
これは**同じ繰込み規約での状態差**であり、W0の全繰込み応力やEinstein方程式の残差を求めたものではない。
有限の解エネルギー行列Kと有限Sigmaなら、追加の平均入力エネルギーは `E_signal+Tr(Sigma K)` で有限。
全時空でのdensity matrixの存在や外部装置のlocal preparationはこの代数的構成から主張しない。

### 4.1 平均の相殺だけでは不十分

一側のコンパクトな入力に関する[KSR]の最初の極を考え、

```math
L[f]=\int e^{\kappa_+v}f(v)\,dv,
\quad p=\kappa_+/|\kappa_-|=(r_-/r_+)^2<1,
\quad V=-e^{-|\kappa_-|v}
```

とする。l=0の例外 `r_+=3r_-` は今回の `.99` に当たらない。
対応する尾の係数はLに比例する。`ell_i=L[f_i]`, `ell_s=L[f_s]` なら、その尾による追加の期待応力の先頭係数は

```math
\Delta\langle T_{VV}\rangle
\sim\Gamma^2\left(\ell_s^2+\boldsymbol\ell^T\Sigma\boldsymbol\ell\right)|V|^{2p-2}.
```

GammaはRNの留数と座標規格化を含む非零係数で、今回SI値を割り当てない。
**平均ell_s=0でも、ell^T Sigma ell>0なら零平均雑音がこの尾を復活させる。**
基準状態と計量を正則に保つ仮定では、この正の発散と滑らかなC²計量は両立しない。
全非線形の終状態、弱い特異点を越える可否、有限受信器の破壊までは結論しない。
また[KSR]の枝・未来bifurcation sphereに関する結論を、有限vの全横断点へ拡大しない。

Sigmaがpositive semidefiniteなら

```math
\boldsymbol\ell^T\Sigma\boldsymbol\ell=0
\iff\Sigma\boldsymbol\ell=0.
```

負の共分散を使って相殺するのは不適合で、検証器はその負例を拒否する。

### 4.2 非零の準備雑音を含みながら、最初の尾を追加しない族

`z=kappa+ v`、hは任意の実smooth compact bumpとして

```math
f_h=(1+\partial_z)h,
\qquad \int e^z f_h dz=0,
\qquad \int f_h dz=\int h dz.
```

これは前回の一つの波形だけでなく、**全てのhについて成立する線形な制御族**である。
例えばhとzhから作る二つのfを用い、その係数に有限のGaussian雑音を与える。
全ての実現で第一momentが零なので、その平均だけでなく追加共分散の第一尾も零になる。
一般のnoiseを出力波形に直接加える場合と、**同じ制御写像の上流にだけ**加える場合は違う。

**ここで零になるSigmaの成分は古典的な準備ensembleの雑音。基準W0の量子真空共分散は残る。**
これを全量子雑音が零の状態と解釈すると不確定性関係を誤って破る。
また微分制御を局所の有限装置として実装したこと、装置の後段雑音を全てこの族へ拘束できることは未証明。

実際の表面重力が設計値の `(1+delta)` 倍なら

```math
\int e^{(1+\delta)z}(h+h')dz
=-\delta\int e^{(1+\delta)z}h(z)dz.
```

従って校正誤差や族外の雑音には敏感なままである。**第一momentの除去は全Hadamard性や全地平面正則性の十分条件ではない。**

## 5. 同じ第一尾制約を、少ない入力エネルギーで満たす

ここでは `z in [-1,1]` に台を固定し、

```math
h(z)=e^{-1/(1-z^2)},\quad I=\int h(z)dz,
\quad \int f(z)dz=I,\quad \int e^zf(z)dz=0,
\quad E[f]=\int |f'(z)|^2dz
```

を使う。hは区間外で零。この積分値Iは零周波数信号が零でないことを確かめる指標であり、実際のRamsey受信平均ではない。
共通の地平面規格化・時間尺度を保ったエネルギー比を比べる。

H_0^1(-1,1)での最小化は、Dirichlet Green関数のrepresenter

```math
g_0=(1-z^2)/2,\qquad g_1=\cosh1+z\sinh1-e^z,
```

とGram行列

```math
G=\begin{pmatrix}2/3&2/e\\2/e&1-e^{-2}\end{pmatrix}
```

を用いて厳密に解ける。
`lambda=G^{-1}(I,0)^T`, `f_*=lambda0 g0+lambda1 g1`、

```math
E_{\inf}=I^2(G^{-1})_{00}=4.85589822251954512767\ldots.
```

境界で零延長したf_*は一般にC-infinityではないので、**この値そのものを滑らかな準備パルスの達成値としない**。
smooth compact関数のH1密度性と二つの連続なconstraintを小さいsmooth補正で保つことで、同じinfimumへ近づける。

実際に滑らかな候補として `f=h(z) sum(c_j z^j)` を使い、二constraint付きquadratic minimizationを解いた。
係数は積分行列の解として定義され、配布JSONはその近似小数。丸めた係数で厳密なpole zeroが維持されるわけではない。

| 族 | E | E / 未整形hのE | E / 前回の(h+h')のE |
|---|---:|---:|---:|
| 前回(h+h') | 11.24385487215 | 27.45168475656 | 1 |
| smooth polynomial degree2 | 8.137319089665 | 19.86712928555 | .72371256853 |
| degree4 | 7.913334828594 | 19.32027543558 | .70379197513 |
| degree6 | 7.457707104464 | 18.20786792131 | .66326959831 |
| **degree8** | **7.136049380337** | **17.42254593498** | **.63466217427** |
| H01での下限（そのままのsmooth達成値ではない） | 4.855898222520 | 11.85559478758 | 0.431871300166 |

最後の比率は表示用の丸めで、厳密値はEinf/Eoldを使う。
別検証器はmonomialではなくLegendre基底を用い、原変数の積分ではなく `z=tanh(t)` の積分と、全KKT saddle-point方程式から再計算する。

**このエネルギー削減を、表の二入力逆散乱係数へ掛けて一台の装置の予算にはしない。**
二入力で全出力を指定する問題と、一側で一つのmomentを抑える問題は異なる制御課題である。
同じ受信誤り率・同じ実際の検出信号を保った最適化、外部pumpの仕事、全装置の応力は未計算。

## 6. 有限受信器への接続はどこまで進んだか

物理的な共通W0とsource応答が存在する領域の、前回のRamsey型局所受信器について、
`m_s=u_s(h_R)`, `m_i=u_i(h_R)`, `V0=W0(h_R,h_R)` とすると、今回のensembleを平均した全結果の確率は

```math
P(R=b,Y=y)=\frac{p_b}{2}
\left[1+y(-1)^b e^{-2(V_0+\boldsymbol m^T\Sigma\boldsymbol m)}\sin(2m_s)\right].
```

場の量子平均と準備ensembleのGaussian積分を独立に照合した。
KSRの可逆性により非零の入力解が全域で零になることはなく、通常のRN内部D内では非零のu_sに重なるcompact smearを選べる。
適切な基準状態と局所の操作順序があれば、場の結合を小さく選んで非零の局所分布差を得る道は残る。
**これは内部の通常の未来向き局所実験についての条件付き構成で、同じ外部の過去受信者への通信ではない。**

全SAに必要な `m_s, m_i, V0` は未取得であり、計算対照のGaussian数値を代入しない。
今後必要なのは、二入力がどの殻・どのRNブロックの境界に当たり、一人の外部送信者の選択が双方に届くかの因果的準備問題と、正値・CCR・Hadamard・接合を同時に満たすLorentzian種の構成である。

## 7. 検証・再現・判定範囲

```bash
python src/symbolic/sa_two_input_state_v5.py --output /tmp/sa-v5/forward.json
python src/symbolic/sa_two_input_state_verify_v5.py \
  --evidence /tmp/sa-v5/forward.json --output /tmp/sa-v5/verification.json \
  --report /tmp/sa-v5/report.md
```

2本は互いをimportしない。各々の既定実行が数値検算と負例を行う。
共有依存・既存workflow・既存assert・原A基準は変更しない。
検証器の明示的なevidence/hash照合と兄弟sourceへの参照があるため、既存CI選別器が共有影響と判定する場合は全件fallbackを維持する。検査を省略するための偽装はしない。

- 順方向：四次元Sturm変換、120次Taylor積分、s∈[-100,100]、50/80桁比較。端点の指数tailの解析的上限はODEの全誤差とは分ける。
- 別実装：元のSturm方程式のCayley midpoint＋4段Richardson、s∈[-40,40]、double精度。比較閾値は複素振幅1e-9。この独立確認を40桁精度の保証とは呼ばない。
- パルス：50/80桁の二constraint最適化、70桁のLegendre/KKT別解、全結果Gaussian積分。
- 負例：逆写像の符号、擬ユニタリを確率と誤認、負の共分散、量子真空を捨てる相殺、事前もつれの誤用、未取得確率の0埋め、Aへの誤昇格、stale evidence等。

**今回の配布時点ではローカルのみ。remote CI・GitHub commit・PR・mergeは未実施。**
書き込みツールが公開されず、CLIには認証設定がなくGitHubへのDNS接続も失敗した。ユーザーの許可不足ではない。
独立検証も同じ作成者による別コードで、独立研究者の査読ではない。Lean、全SA mode sum、非線形時間発展は実施していない。
web PDF screenshotは取得エラー。本文の抽出テキストで式と§6を確認したが、Penrose図の新たな目視検証はしていない。
実行version・SHA256・実際の数値差・未実施事項は配布結果JSONとDELIVERYに記録する。

## 8. 一次文献と、今回の計算との境界

- **[SA]** F. Schein, P. C. Aichelburg, *Traversable Wormholes in Geometries of Charged Shells*, PRL **77**, 4130–4133 (1996). https://arxiv.org/abs/gr-qc/9606069 。背景候補の出典。今回その幾何の生成や全量子状態を再現したわけではない。
- **[KSR]** C. Kehle, Y. Shlapentokh-Rothman, *A scattering theory for linear waves on the interior of Reissner–Nordström black holes*, Ann. Henri Poincaré **20**, 1583–1650 (2019), arXiv:1804.05438v2. https://arxiv.org/abs/1804.05438 。Prop.2.5, Prop.3.3, Theorems3–5。逆写像・反射の単射性・第一極の尾は輸入した定理。有限周波数計算、局所制御への適用、準備共分散、パルス最適化は今回の導出・実装。
- **[T20]** P. Taylor, *Regular Quantum States on the Cauchy Horizon of a Charged Black Hole*, CQG **37**, 045004 (2020), arXiv:1904.05941v2. https://arxiv.org/abs/1904.05941 。§6の物理解釈・Lorentzian継続の留保を含めて読む。全SAの物理的種を供給する論文として扱わない。
- **[D22]** E. Tjoa, K. Gallock-Yoshimura, *Channel capacity of relativistic quantum communication with rapid interaction*, PRD **105**, 085011 (2022). https://arxiv.org/abs/2202.12301 。局所の場と検出器の通信という枠組みの参考。今回の非平衡Gaussian平均と有限受信器式は、同論文からSAの解を借りたものではない。
