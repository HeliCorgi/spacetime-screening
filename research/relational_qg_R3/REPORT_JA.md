# R3：非線形Hamiltonian候補、二自由度の拘束、重力自身の結合エネルギー

基点：R2 `7e25b4db8a81b6287c9f07e593a1c0f2310132de`。R1/R2は履歴として変更しない。

**NEW CALCULATION CANDIDATE。非線形の作用を一つ明示し、その正則な拘束分岐、平坦背景の物理二偏極、および重力の自己源を二次まで検算した研究版。完全な非線形量子重力・一般の初期値問題の適切性・特異点解消を証明したものではない。**

## 0. 今回変更した仮定

R2は保存源を線形TT場に接続したNewtonian/quadrupole closureであり、非線形のWard completionではなかった。今回は保存則に都合のよい応力を後付けする代わりに、重力と物質を同じcanonical actionから変分する候補を選ぶ。

ただし次はR2からの定理ではなく、新たな設計条件である。

1. 漸近平坦な分岐に、運動量のtraceを除く拘束 `C=gamma_ij pi^ij=0` を導入する。ell=0ではアクセス可能なmaximal slicingのGRになるが、ell>0では物理的なpreferred foliationを伴う。
2. Gaussianの逆演算子を無条件に曲がった空間へ外挿せず、有限次数 `A_m=(1+ell^2 L/m)^m` を用いる。mは離散的な模型選択であって、同じ模型の実験ごとに変えてよい調整値ではない。今回はm=2を最も具体的に調べ、m=4,8,16,32は静的Gaussian極限の比較とする。
3. 以下の曲率演算子の順序と係数を指定する。線形一致だけでは任意の三次以上の曲率項を決められない。それらは本候補では0に設定し、量子補正から保護されるとはしない。

新しい連続的な重力定数は導入しない。しかし「新しい物理的仮定を加えていない」とは言わない。

## 1. 線形場の再定義から出発する

R1の観測計量は `h_obs=F h`、`F=exp(-ell^2 L/2)` だった。平坦背景でこれを自由作用へ代入すると、観測計量の二次作用は `A=F^(-2)=exp(ell^2 L)` を持ち、物質は観測計量に最小結合する形になる。

これは同じ線形応答の書き換えであって、そのまま非線形完成ではない。曲がった空間ではL自身が計量に依存する。単に `partial -> nabla` として、Aを固定したまま変分してはいけない。

有限次数を次で定義する（Lの定義域・境界条件を固定する）：

$$
A_m(L)=(1+\ell^2L/m)^m,\qquad
B_m(L)=\sum_{j=1}^{m}\binom mj(\ell^2/m)^jL^{j-1}.
$$

従って `L B_m=A_m-I`。L=0でもBは多項式として定義される。スカラー、対称空間テンソルには、それぞれのrough Laplacian `L=-D_i D^i` を使う。内積は正定値な空間計量と `sqrt(gamma)d^3x`。この自己共役な実現でAは正で、Aの逆は空間的な楕円演算子の逆である。

`A_m=1+ell^2 L+[(m-1)/(2m)]ell^4 L^2+...`。R1との低波数一致はO(ell^2 L)まで。r~ellでの一致や非線形m→∞極限を自動的に保証しない。

## 2. 非線形作用を明示する

`c=hbar=1`、`M_P^2=(8 pi G)^(-1)`。gamma_ijは空間計量、pi^ijは共役運動量密度。`p^ij=pi^ij/sqrt(gamma)`、`p=gamma_ij p^ij` とする。

$$
S_m=\int dt\,d^3x\,[\pi^{ij}\dot\gamma_{ij}+\pi_\phi\dot\phi
 -N\mathcal H_m-N^i\mathcal H_i-\mu C]-\int dt\,E_\infty.
$$

添字mは多項式次数であってmatterの略ではない。境界項は標準の漸近平坦な時間並進を定義するADM項。追加の高空間微分境界項は採用した減衰条件で消える。

$$
\mathcal H_m=
\frac{2\sqrt\gamma}{M_P^2}
\left[p^{ij}A_{m,T}^{-1}p_{ij}-\frac12p A_{m,s}^{-1}p\right]
-\frac{M_P^2\sqrt\gamma}{2}\mathcal V_m+\mathcal H_{\rm matter},
$$

$$
\boxed{\mathcal V_m=A_{m,s}{}^{(3)}R
-{}^{(3)}R_{ij}B_{m,T}{}^{(3)}R^{ij}
+\frac12{}^{(3)}R B_{m,s}{}^{(3)}R.}
$$

$$
\mathcal H_i=-2\gamma_{ik}D_j\pi^{jk}+\pi_\phi\partial_i\phi,
\qquad C=\gamma_{ij}\pi^{ij}.
$$

物質の一例は通常の最小結合scalar：

$$
\mathcal H_{\rm matter}=\frac{\pi_\phi^2}{2\sqrt\gamma}
+\sqrt\gamma\left(\frac12\gamma^{ij}\partial_i\phi\partial_j\phi+U(\phi)\right).
$$

質点の場合も、同じ物理計量への最小結合を用い、`H_matter=sum sqrt(m_a^2+gamma^ij p_ai p_aj) delta(x-x_a)` とする。静的な点源の数値は弱場のsource-to-probe近似であり、保持装置を省略した予測に過ぎない。

これはgammaの全次数で書いたfunctionalである。時間についてcanonicalな一階形式、空間について非局所なinverse-Aを含む。有限mのpotentialは有限階の空間微分。各演算子の計量・体積・connection依存性も変分する。

## 3. なぜR B Rの係数が1/2か

平坦背景で `gamma_ij=e^(2 zeta)delta_ij`、lapse `N=1+n` とする。運動量kをz方向に置けば、線形の空間Ricciはscalar sectorで

`R_ij=k^2 zeta diag(1,1,2)`, `R=4k^2 zeta`。

従って `-R_ij B R^ij+c R B R` の係数は `(-6+16c)k^4 B zeta^2`。これをtensor sectorと同じAに合わせるには

$$-6+16c=2\quad\Rightarrow\quad c=1/2.$$

結果、空間potentialの二次部分は

$$
\int N\sqrt\gamma\,\mathcal V_m\big|_{\rm scalar}^{(2)}
=\int [2\zeta L A_m\zeta+4n L A_m\zeta],
$$

$$
\int \sqrt\gamma\,\mathcal V_m\big|_{\rm TT}^{(2)}
=-\frac14\int h^{TT}_{ij}L A_m h^{TT}_{ij}.
$$

静的な低圧源について、lapse variationとzeta variationは

$$
\zeta(\mathbf k)=\frac{\rho(\mathbf k)}{2M_P^2k^2 A_m(k^2)},\qquad n=-\zeta.
$$

従って `Phi=Psi`。これは上のoperator basis内での係数固定であり、任意の非線形作用の一意性定理ではない。

## 4. 二自由度を保つ方法と、その条件

空間diffeomorphismはH_iで生成する。AとBが空間幾何から作られるので、Hは空間scalar density、Cもdensityであり、H_iは対応するLie微分の代数を持つ。

CとHをsecond-classの対にする。平坦背景の非零空間modeでは

$$\boxed{\{\mathcal H_m,C\}(\mathbf k)=-M_P^2 k^2 A_m(k^2).}$$

`k^2 A_m>0` なので、指定した非零modeにzeroはない。全Poisson matrixのブロック構造は

$$
\begin{pmatrix}\{H,H\}&\{H,C\}\\-\{H,C\}^{T}&0\end{pmatrix}.
$$

mixed blockが可逆であれば、`{H,H}`がGRの形に閉じなくてもこの行列は可逆。C保存がlapseを、H保存がmuを決める。境界でN→1を与え、homogeneous lapseの扱いを固定する。これを全時空での可逆性の証明とはしない。

正則な分岐の位相空間計数は

$$\boxed{(12-2\times3-2)/2=2.}$$

独立verifierは6組のcanonical変数で、5拘束のgradient rank=5、Poisson matrix rank=2を直接計算した。3つがfirst class、2つがsecond class。

**成立範囲：**これは正則なsecond-class branchに条件を付けた非線形の構造、および平坦背景でのそのmixed operatorの検証。任意の曲率でのrank不変性、lapseの正値性、無限系の楕円境界値問題・evolutionの適切性は未証明。zero modeは除外したまま忘れるのではなく、境界・全体の時間・cosmologyで別に扱う。

## 5. 波と物理エネルギー

TT sectorでmomentumを消去すると

$$
S^{(2)}_{TT}=\frac{M_P^2}{8}\int
[\dot h^{TT}A_m\dot h^{TT}-\partial_i h^{TT}A_m\partial_i h^{TT}].
$$

A_m(k^2)>0なので、二つのTT modeの二次エネルギーは正。`omega^2=k^2`で新しい時間周波数のpoleはない。

canonical fieldを `h_c=A_m^(1/2)h` とすると、matter couplingは `A_m^(-1/2)h_c T`。静的exchangeは `4 pi G/[k^2 A_m]` になる。これはR1との線形field-redefinition関係を保った設計である。ただし一般の時間依存する全source propagator、量子loop、非線形波形まで検証したわけではない。

二次エネルギーの正値性を、完全なinteracting Hamiltonianの下限と取り違えない。

## 6. 計量が変われば平滑化演算子自身も変わる

$$
\delta A_m^{-1}=-A_m^{-1}(\delta A_m)A_m^{-1},
$$

$$
\delta A_m=\frac{\ell^2}{m}\sum_{j=0}^{m-1}
(1+\ell^2L/m)^j\delta L(1+\ell^2L/m)^{m-1-j}.
$$

scalarに対して、delta gamma_ij=h_ijなら

$$
\delta L f=h^{ij}D_iD_j f+
(D_i h^{ij}-\tfrac12D^j h)D_j f.
$$

tensorには追加のconnection variationがある。これと体積・index contractionの変分を含めることが、自己源の一部である。

非可換な3x3正演算子の制御で、上のFrechet derivativeと有限差分を比較した。Aを固定して微分した場合のゼロという答えは棄却した。これはoperator variationの制御であり、3x3行列を4D場の全方程式の代用にしたわけではない。

## 7. 実際の非線形計算：結合エネルギーがADM質量へ入る

時間対称な漸近平坦初期sliceで `pi^ij=0`、`gamma_ij=e^(2zeta)delta_ij` とし、座標rest-density rho_cを固定する。静止したdust starではなく、momentum=0の初期dataの試験。

constraintは

$$\sqrt\gamma\,\mathcal V_m=16\pi G\rho_c.$$

一次では `A_m Delta zeta_1=-4 pi G rho_c`。二次まで空間積分すると

$$
16\pi G M_{ADM}+2\int d^3x\,\partial_i\zeta_1 A_m\partial_i\zeta_1
=16\pi G M_{rest}+O(\zeta^3).
$$

一次constraintを用いて

$$
\boxed{M_{ADM}=M_{rest}-\frac G2\int d^3x\,d^3y\,
\rho_c(x)\rho_c(y)K_m(|x-y|)+O(G^2).}
$$

cを戻すと質量減少はbinding energy/c²。**粒子間のエネルギーだけに重力を与えて、重力の自己エネルギーを落とした計算ではない。** 同じHamiltonian constraintの二次項から、その結合エネルギーが遠方のADM massに現れることを確かめた。

### 非線形sourceを直接展開して照合

m=2、sigma=ell=1、epsilon=G Mrest/ell とし `zeta=epsilon f+epsilon^2 g+...`。

$$
f(r)=\frac{\operatorname{erf}(r/\sqrt2)}r
-\frac{e}{2\sqrt2}\left[e^{-\sqrt2r}\operatorname{erfc}(1-r/\sqrt2)
+e^{\sqrt2r}\operatorname{erfc}(1+r/\sqrt2)\right].
$$

full spatial potentialとdelta Aを展開すると `A_2 Delta g=S[f]/4`。Sはfから6階までの微分を含む20項で、selfsource.jsonにexactなjet polynomialを保存した。非線形potentialから導くコードと、そのjet式の実装を記号的に一致確認した。

二次初期dataは積分として

$$g(x)=-\frac1{16\pi}\int K_2(|x-y|)S_f(y)d^3y$$

と構成できる。これは摂動的な初期constraintの解であって、全非線形evolutionではない。

球対称sourceをGauss-Legendreで積分し、rmax=30と32で漸近tailも比較した。結果：

- pair-energy積分：`0.207591388559956560049490925954...`
- 非線形constraintから：`0.207591388559956560084354582448...`
- 絶対差：`3.49e-20`
- 中心の二次補正：`g(0)=-0.04372218240368245...`

プロファイルの他のrでの36桁表記は表示精度に過ぎず、格子変更の差は約1.7e-8。mass積分と中心値の精度と混同しない。

例えばepsilon=0.01では、保持した次数で

$$M_{ADM}/M_{rest}=0.9979240861144+O(\epsilon^2).$$

残した高次の理論誤差と、積分の丸め誤差は別物である。

## 8. 核を実装し直したことによる予測の変更

m=2では、a=ell/sqrt(2)として

$$\boxed{K_2(r)=\frac{1-e^{-r/a}(1+r/(2a))}{r}.}$$

`-Delta K_2/(4pi)=exp(-r/a)/(8pi a^3)` は正で全積分1。r>0で `(-Delta)A_2 K_2=0` を記号検証した。point sourceのdistributionと境界は正規化で固定する。

中心で `K_2(0)=1/(2a)`。m>=2なら中心の二階微分も有限。ただし有限mは任意階でsmoothとは限らないので、nonlinear field testにはsmooth matterを使う。

point-probe位相 `2K_m(3d)-K_m(4d)-K_m(2d)` の根は：

| m | d*/ell | Omega0^2 ell^3/(GM) |
|---:|---:|---:|
| 2 | 0.349424262330 | 0.471404520791 |
| 4 | 0.503102583065 | 0.166666666667 |
| 8 | 0.579509411251 | 0.121533978016 |
| 16 | 0.617474332846 | 0.106272697449 |
| 32 | 0.636302248672 | 0.099831358949 |
| static Gaussian limit | 0.654976082566 | 0.094031597258 |

独立検証にはYukawa多項式再帰を使わず、Gamma分布のheat-kernel mixtureを用いた。R2で調べた装置反作用や波束幅の依存はなくなっていない。この表はpoint probesの制御である。

一般のmについて

$$
\Omega_{0,m}^2=\omega_{quantum,m}^2=
\frac{GM}{\ell^3}\frac{m^{3/2}\Gamma(m-3/2)}{6\sqrt\pi\,\Gamma(m)}.
$$

古典の中心軌道周波数と量子調和振動数の一致は維持される。しかし係数や位相零点はUV実装に依存する。**R2の0.655を非線形完成から独立な普遍定数として守らない。**

## 9. 一般共変性の意味を限定する

preferred foliationのclock tauを導入し、`X=-g^mu nu partial_mu tau partial_nu tau>0`、`n_mu=-partial_mu tau/sqrt(X)`、gammaをその接空間への射影とする。P^mu nuを空間的な補助momentum tensor、K_mu nuをextrinsic curvatureとすれば、形式的な座標共変表示は

$$
S=\int\sqrt{-g}\left[
2P^{\mu\nu}K_{\mu\nu}
-\frac2{M_P^2}\left(P^{\mu\nu}A_T^{-1}P_{\mu\nu}-\frac12P A_s^{-1}P\right)
+\frac{M_P^2}{2}\mathcal V_m-uP\right]+S_{matter}[g].
$$

unitary gauge tau=tで前のcanonical actionになる。D,L,Rは葉のintrinsicな演算子と曲率。clockと補助場の変分も含めたdiffeomorphism Noether identityを使う必要がある。

**座標共変な包装と、GRの物理的なrefoliation invarianceは同じではない。** 本候補ではHとCがsecond classであり、葉の選択は物理に残る。tau=tが使えるtimelike-clock領域を越えた退化性、globalなclockの存在、量子constraint anomalyを証明したわけではない。

matterは通常の最小結合なので固定されたsmooth geometry上の局所QFTを保持できるが、そのことは重力も含むUV完成を意味しない。inverse spatial operatorによりmetric microcausalityは保証しない。

## 10. 宇宙論・特異点での失敗を結果として残す

AF分岐のC=pi=0をflat homogeneous cosmologyへそのまま使うと、isotropic momentumは0となり、R3=0なのでconstraintはrho=0を要求する。正密度の膨張宇宙へそのまま適用できない。

候補となる拡張はcompact sliceで `C=pi-sqrt(gamma)<pi/sqrt(gamma)>` とするCMC条件で、homogeneous volume-momentum pairを残すこと。しかしこの拡張の全constraint algebraは今回完成していない。

しかもhomogeneous CMC controlではA(0)=1、R3=0、空間微分0なので背景方程式はGRのflat FLRWのままになる。dust解a(t)~t^(2/3)は

$$ {}^{(4)}R=4/(3t^2),\qquad R_{abcd}R^{abcd}=80/(27t^4). $$

従って空間分解能だけから一般のbig-bang singularityを消したとは言えない。これは明示的な反例である。

## 11. 量子化と未解決のgate

正則なconstraint surfaceではDirac bracketを定義できる。位相空間path integralには `delta(H)delta(C)sqrt(det{chi_A,chi_B})` と空間gauge-fixingが必要。二次TTのpositive normは確認したが、このmeasure、loop counterterms、放射安定性まで検算したとはしない。

- nonlinear functionalは明示したが、全背景のrank保存・lapse>0・適切な初期値問題は未証明。
- exact Gaussianの非線形m→∞極限は未証明。finite-m結果をその証明にしない。
- preferred foliationの起源と観測制約は未解決。
- vacuum energyはA(0)=1で消えない。宇宙定数の説明をしていない。
- cubic以上のoperatorはloopで一般に再生成され得る。係数を0に置くことは保護対称性ではない。
- 二次までのADM binding一致は、一般の1PN波形・強重力完成ではない。
- compact CMCと宇宙論のconstraint branchは別検討。

## 12. 再現と既知構造との比較

```bash
python src/symbolic/relational_qg_r3_constraints.py --output /tmp/r3.json
python src/symbolic/relational_qg_r3_verify.py --evidence /tmp/r3.json --output /tmp/r3-verify.json
python src/symbolic/relational_qg_r3_selfsource.py --output /tmp/r3-selfsource.json
```

各scriptはoptional I/Oを除き単独でも実行可能。verifierはforwardをimportしない。CI shard間の生成物交換は不要。既存のSymPy/mpmathだけを使い、CI・requirements・精度基準は変更しない。

先行研究の機構を、このR3作用の証明に流用しない。比較対象：

- [Mukohyama & Noui, Minimally Modified Gravity: a Hamiltonian Construction](https://arxiv.org/abs/1905.02000)：空間共変で二自由度を持つHamiltonian構成の一般的な先行例。
- [Bellorin & Restuccia, Quantization of the Horava theory at the kinetic-conformal point](https://arxiv.org/abs/1606.02606)：second-class constraints、楕円的なlapse、二tensor modesの先行解析。R3とは作用が異なる。
- [Bellorin, Restuccia & Sotomayor](https://arxiv.org/abs/1302.1357)：余分なmodeを拘束で消す先行例。
- [Gao & Yao, Spatially covariant gravity theories with two tensorial degrees of freedom](https://arxiv.org/abs/1910.13995)：二自由度のために必要な退化性とconsistencyを区別する比較。
- [Hu & Gao, Covariant 3+1 correspondence](https://doi.org/10.1103/PhysRevD.105.044023)：unitary gaugeの健全性と全領域の共変退化性を同一視しないための比較。

独創性・優先権は主張しない。新規計算候補は、ここで指定したA/B curvature構成の係数matching、operator variation、自己源の二次展開、ADM bindingとの照合、finite-m予測の関係である。
