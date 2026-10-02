# B1：体積の時間発展を残す別候補（VCDMの具体的ポテンシャル）

2026-10-02。R4/R5の延命版ではない。空間平滑化核も C=gamma_ij pi^ij=0 も今回の作用に加えない。
既存のVCDM / type-II minimally modified gravityの拘束構造を利用し、ポテンシャルを一つ固定して、新たに背景・異方性・線形摂動の符号を検算する。

**既知理論をゼロから発明したという主張はしない。完全な量子重力・任意の特異点解消・観測宇宙の再現も主張しない。**

## 1. 借りる構造と、今回指定するもの

M^2=(8 pi G)^(-1)、c=hbar=1。ADM規約は K_ij=(dot gamma_ij-D_i N_j-D_j N_i)/(2N)。

$$
S_g=M^2\int dt\,d^3x\,N\sqrt\gamma\left[
\frac12({}^{(3)}R+K_{ij}K^{ij}-K^2)-V(\phi)
-\frac34\lambda^2-\lambda(K+\phi)-\frac{\lambda^i}{N}\partial_i\phi
\right].
$$

この作用構造は De Felice, Doll & Mukohyama, arXiv:2004.12549、および Ganz et al., arXiv:2212.13561v2 Eq. (7)に基づく。二つの局所重力自由度を持つ拘束理論という性質は既存の解析に依拠する。今回その全Dirac解析を再導出していない。

今回選ぶポテンシャルは

$$ V(\phi)=\frac{\phi^2-\mu^2\cos^2(\phi/\mu)}3,\qquad \mu>0. $$

これは一つの逆設計上の選択。量子重力からmuやcos²形が導かれたのではない。先行研究との厳密な新規性調査は行わず、優先権を主張しない。
主な摂動テストの物質は、通常の正符号の自由massless scalar：

$$ S_\chi=-\frac12\int d^4x\sqrt{-g}\,g^{\mu\nu}\partial_\mu\chi\partial_\nu\chi. $$

phiは補助変数で、chiが物理的な物質場。一様背景のchiは P=rho を満たす。dustは背景存在の別controlとしてのみ調べる。

## 2. 一様背景と旧反例の回避

既存作用から得る背景式（物理単位のrho）：

$$ \rho=M^2(\phi^2/3-V),\quad H=V_\phi/2-\phi/3,\quad
\dot\phi=3(\rho+P)/(2M^2),\quad\dot\rho+3H(\rho+P)=0. $$

今回の選択では

$$ \rho=\rho_c\cos^2(\phi/\mu),\qquad H=\frac\mu6\sin(2\phi/\mu),\qquad
\rho_c=\frac{M^2\mu^2}3. $$

従って同じ作用から

$$ H^2=\frac\rho{3M^2}(1-\rho/\rho_c),\qquad
\dot H=-\frac{\rho+P}{2M^2}(1-2\rho/\rho_c). $$

Friedmann式を後付けで差し替えたのではない。とくにH=0の点を割り算で除外せず、補助変数の背景式で連続した時間発展を与える。

w=P/rhoを一定としてx=mu(1+w)t/2、phi=mu atan(x)の分岐を取ると

$$ a(t)=a_b(1+x^2)^{1/[3(1+w)]},\quad\rho(t)=\rho_c/(1+x^2). $$

w=0ならdustの正密度解、w=1ならcanonical scalarのstiff解。低密度でFriedmann式はGRのものへ相対補正O(rho/rho_c)で戻る。局所PPNや全背景のGR極限を今回新たに計算したわけではない。

## 3. canonical scalarの場合の曲率と継続

w=1ではx=mu*t、

$$ a=a_b(1+x^2)^{1/6},\quad \chi=\chi_0+M\sqrt{2/3}\,\operatorname{asinh}x. $$

四次元曲率は

$$ R=\frac{2\mu^2(3-x^2)}{3(1+x^2)^2},\qquad
R_{abcd}R^{abcd}=\frac{4\mu^4(9-12x^2+5x^4)}{27(1+x^2)^4}. $$

全実tで有限。Kretschmannは4mu^4/3以下。a>=a_b>0であり、空間R^3上の一様な解は全実tへ定義される。null affine lengthはintegral a dt、timelike proper lengthはintegral dt/sqrt(1+p²/a²)で、両端で発散する。この特定の一様幾何はcausal geodesically complete。tはglobal time。
任意の崩壊・ブラックホール・一般の非一様初期データへの主張ではない。

## 4. Bianchi I：完全等方性だけの偶然にはしない

$$ ds^2=-dt^2+a(t)^2\sum_i e^{2\beta_i(t)}(dx^i)^2. $$

lambdaを消去すると、一様作用は

$$ L=M^2a^3\left[\frac{\sum_i\dot\beta_i^2}{2N}+2\phi\dot a/a+N(\phi^2/3-V)\right]
+\frac{a^3\dot\chi^2}{2N}. $$

sum beta_i=0。次の族を同じ作用のEuler方程式へ代入した：

$$ a=a_b(1+x^2)^{1/6},\quad \phi=\mu\arctan x,\quad
\beta_i=d_i\operatorname{asinh}x,\quad\sum_i d_i=0, $$

$$ \chi=\chi_0+M\sqrt{2/3-\sum_i d_i^2}\operatorname{asinh}x,\quad
\sum_i d_i^2<2/3. $$

全背景方程式の残差は0。rho_total=rho_chi+rho_shear=rho_c/(1+x²)で、

$$ \rho_{\rm shear}/\rho_{\rm total}=\frac32\sum_i d_i^2<1 $$

は一定。異方性は消えないが、このstiff族では収縮に伴って割合が発散しない。

各方向のscale factorは有限時刻で正で滑らか、H_iとdot H_iは有界。両端でa_i~|t|^(1/3 +/- d_i)。sum d=0とsum d²<2/3から|d_i|<2/3なので、その最小指数は-1/3より大きい。保存された空間運動量を使うとnull/timelike affine lengthは少なくともintegral |t|^p dt (p>-1/3)型で発散する。この族もcausal geodesically complete。

これはBianchi Iの解析族であり、空間依存した異方性の非線形安定性ではない。

## 5. 背景の式だけで合格にしない：物質scalar摂動

出典：Ganz et al. arXiv:2212.13561v2 Eqs. (33)-(40)。今回のコードはそのreduced action係数へ上のstiff背景を代入し、符号を解析的に評価する。七つの変数から一つの物理scalarへのconstraint reduction自体を独立に再導出したとはしない。

conformal time etaに対する作用を

$$ S^{(2)}_S=\frac{M^2}2\int d\eta d^3k\ z_k^2(|\mathcal R_k'|^2-c_R^2 k^2|\mathcal R_k|^2) $$

とし、x=mu*t、q=k/(a*mu)、Z=z²/a²とすると

$$ Z=\frac{6(1+x^2)[q^2(1+x^2)+1]}{q^2x^2(1+x^2)+x^2+2}>0, $$

$$ c_R^2=\frac{3q^4x^2(1+x^2)^3+6q^2(1+x^2)^2(x^2+3)+3x^4+13x^2+2}
{3(1+x^2)[q^2(1+x^2)+1][q^2x^2(1+x^2)+x^2+2]}>0. $$

全ての有限な実x,qについて、分子・分母が非負の偶数冪と正の定数項からなることを厳密確認した。物理的にk!=0の摂動に適用する。H=0やdot H=0で元のslow-roll型中間変数が発散しても、最終係数の特異性は可除。

tensorは同じVCDM作用の標準の二偏極、正の運動項とc_T²=1。この一般の式は既存解析に依拠する。

**限界：** z''/z由来のモード増幅、全非線形安定性、三次作用でのstrong coupling、loopとHadamard状態までは証明しない。bounceでは

$$ c_R^2(0,q)=\frac{9q^2+1}{3(q^2+1)} $$

となり、1を超えるqもある。k依存・時間依存の縮約係数だけをfront velocityと同一視しないが、厳密なmetric microcausalityが証明済みとは決して扱わない。

参考のUV boundary-layer check：mu=1, large kでu=k*tを固定した先頭方程式は

$$ v_{uu}+\left[1+\frac{2u^2+10}{(u^2+2)^2}\right]v=0, $$

$$ v=e^{-iu}(u+i)/\sqrt{u^2+2} $$

という透過解を持つことを記号検算した。これは先頭のboundary layerのみで、全波数のparticle productionや全量子状態のHadamard証明ではない。

## 6. 候補の評価

- 正密度のdust背景とstiff背景：作用の式を厳密に満たす。
- 今回の一様・Bianchi I stiff族：有限曲率でcausal geodesically complete。
- canonical scalarの等方背景上：線形のghost/gradientの符号条件を通る。
- muは未測定、量子重力から未導出。
- preferred foliationは残る。
- R5の空間核は入れず、その短距離予測は引き継がない。
- 完全な量子重力、ブラックホール特異点回避、CMB/PPNの総合適合、一般の初期値問題は未検査。
- キル済みR4の汎用宇宙論拡張を、遡って合格にしない。

**判断：** 次の解析に進める具体的候補。宇宙の重力として採用済みではない。

## 7. 再現

```
python check_candidate.py --output results.json
python verify_geometry.py
```

check_candidate.pyは元のlambda入り一様作用の消去、背景残差、Bianchi I残差、既存scalar係数への代入と正値性を記号検算。
verify_geometry.pyはforwardをimportせず、四次元metricのChristoffelとRiemannから曲率を再計算する。

途中で補助verifierの有理式をPolyへ渡す前に分母をcancelする処理が必要だった。最初の実行はPolynomialErrorで停止し、修正後に全検査を再実行した。数学的条件や閾値は弱めていない。
この作業ではGitHubやR1-R5を変更していない。

## 出典

- A. De Felice, A. Doll, S. Mukohyama, A theory of type-II minimally modified gravity, arXiv:2004.12549: https://arxiv.org/abs/2004.12549
- A. Ganz, P. Martens, S. Mukohyama, R. Namba, Bouncing Cosmology in VCDM, arXiv:2212.13561v2: https://arxiv.org/html/2212.13561v2

VCDMの作用・自由度解析・一般scalar二次係数は既存研究。今回のcos²指定、式への代入、表示した一様/異方解と符号の確認を、全理論の独立再証明と混同しない。既存論文の異なるbounceモデルについての観測適合性を、この対称解へ移植しない。
