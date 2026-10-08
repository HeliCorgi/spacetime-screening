# R1: 閉じたMaxwell・二流体shear driverの構成と検証

2026-10-08。親PR #40、読取head `0ab94331d8aef62148acac1d89e3235979e6ea83`。
[元のR1](family376-research-tasks.md#r1--有限energyの閉じたdriverによる相対論的shear-gate最優先)の続き。
**総合状態: 部分達成。正の粘性を含む完全な非線形Einstein gateの数値的認定ではない。**

## 0. 今回何を得たか

| 対象 | 結果と射程 |
|---|---|
| 駆動源 | 電流を外部指定せず、Maxwell場と正負二流体の同じ方程式で閉じた |
| 初期Einstein/Maxwell拘束 | 正密度・有限切断energy・総charge 0を満たす厳密な初期データ族 |
| 非線形構成則 | shear relaxationとentropy currentを明記。全応力保存・entropy生成の恒等式を検査 |
| 非粘性比較模型 | 標準双曲型局所存在論による小振幅・有限時間構成と一次解を記述。具体的な振幅閾値は未算出 |
| 非線形粘性の凍結principal symbol | 指定構成則の流体静止frameで、`||pi/w|| <= 10^-3` の有限行列補題を導出・検算 |
| 正粘性の線形gate | 全時間区間のscaled C1相対誤差 `<0.26%`、変位誤差 `<0.18%` を解析的に評価 |
| 独立検算 | 有理数・外向き丸め・Taylor剰余による線形終点の包囲。区間幅 `<2.27e-37` |
| 未認定 | 共通Cauchy切断での完全な粘性結合系の非線形誤差上界、具体的な非零振幅の合否 |

新しい一般no-go、NS universal compiler、CTC、Hadamard/RSET/SCEEの解は得ていない。
以下の新しい計算・補題はこのノートの導出であり、Family 376や引用文献が既に証明したと帰属させない。
独立査読・この連続体模型のLean形式化は未実施。

## 1. 固定する物理模型

署名 `(-+++)`、`c=1`、rationalized Maxwell単位。`G_N>0`、`Lambda=0`。
`eta` はconformal time、`mu` はshear viscosityであり別の記号。
空間は `Sigma=T^3_L`、時間は実区間。同一視は空間方向のみ。

二種 `s=+,-` に粒子密度 `n_s>0`、entropy per particle `s_s`、四速度 `u_s`、
rest energy `e_s>0`、pressure `p_s=e_s/3`、tracefree transverse shear stress `pi_s` を置く。

\[
T_s^{\mu\nu}=w_su_s^\mu u_s^\nu+p_sg^{\mu\nu}+\pi_s^{\mu\nu},\quad
w_s=e_s+p_s,\quad u_s^2=-1,\quad u_{s\mu}\pi_s^{\mu\nu}=0,\quad \pi_{s\mu}{}^\mu=0.
\]

EOS、temperature、chargeを

\[
e_s=\kappa n_s^{4/3}\exp(s_s-s_0),\quad
\mathcal T_s=e_s/n_s,\quad q_s=\pm q,\quad
J^\mu=q(n_+u_+^\mu-n_-u_-^\mu)
\]

と固定する。`s0=1` はentropy基準の選択。Gibbs関係
`de=(w/n)dn+n T ds`、`c_s^2=1/3` を満たす。
これは二つの保存chargeを持つ現象論的radiation-fluid模型であり、
実際の電子・陽電子のannihilation、heat/diffusion、kinetic UV completionを証明した模型ではない。

Maxwellの符号は

\[
\nabla_\nu F^{\mu\nu}=J^\mu,\quad \nabla_{[\alpha}F_{\beta\gamma]}=0,\qquad
\nabla_\mu(n_su_s^\mu)=0,\qquad
\nabla_\mu T_s^{\mu\nu}=q_sn_sF^{\nu\lambda}u_{s\lambda}.
\]

`F^{0i}=E^i`, `F^{ij}=epsilon^{ijk}B_k` なら局所inertial frameで
`E_dot=curl B-J`, `B_dot=-curl E`、物質の力は `rho_q E+J cross B`。

\[
T_{EM}^{\mu\nu}=F^{\mu\lambda}F^\nu{}_{\lambda}-\tfrac14g^{\mu\nu}F^2,
\quad G^{\mu\nu}=8\pi G_N(T_+^{\mu\nu}+T_-^{\mu\nu}+T_{EM}^{\mu\nu}).
\]

従って `div T_EM=-F.J` と二種の力が打ち消し、`div T_total=0`。
電流にも反作用があり、電磁場・反対符号流体がdriverの有限energy reservoirである。
`T=G/(8pi G_N)` の逆定義や、所望軌道から外力を逆算して貼る操作は使わない。
相対論的二流体・Maxwell結合の既存例は [S1,S2]。これらの論文を本模型のGR gateの証明とはしない。

### 1.1 entropyを閉じる非線形shear relaxation

`Delta^{mu nu}_{alpha beta}` は `u` に直交する対称tracefree projector、
`D=u.nabla`, `theta=div u`, `sigma=Delta nabla u` とする。bulk、heat、diffusionは零。

\[
\tau(e)=\tau_0(e/e_0)^{-1/4}>0,\quad
\mu(e)=\mu_0(e/e_0)^{3/4}>0.
\]

各種に次のoriginal-IS型のentropy completionを採用する。

\[
\tau\Delta D\pi+\pi
=-2\mu\sigma-\frac{\tau}{2}\pi\{\theta+D\log[\tau/(\mu\mathcal T)]\}.
\tag{1}
\]

number/energy方程式から

\[
De=-\frac43e\theta-\pi:\sigma,\quad Dn=-n\theta,\quad
D\log[\tau/(\mu\mathcal T)]=\frac53\theta+\frac2e\pi:\sigma.
\]

よって(1)は、係数微分を未知のまま残さないfirst-orderな式

\[
\boxed{\tau\Delta D\pi+\pi=-2\mu\sigma-\tfrac43\tau\theta\pi
-\tfrac{\tau}{e}(\pi:\sigma)\pi}
\tag{2}
\]

になる。この最後の項を理由なく落とさない。

\[
S^\mu=\left[ns-\frac{\tau}{4\mu\mathcal T}\pi:\pi\right]u^\mu,
\qquad \boxed{\nabla_\mu S^\mu=\frac{\pi:\pi}{2\mu\mathcal T}\ge0}.
\tag{3}
\]

証明は(1)を `pi` と縮約し、`n T Ds=-pi:sigma` を代入するだけである。
`pi:pi>=0` は `pi` がfluid rest space上のtensorであることによる。
コードはこの恒等式と、(2)末尾を落とすと残る
`-tau (pi:pi)(pi:sigma)/(2 mu T e)` を検査する。
また、非粘性の固定isentropic EOS `e=kappa n^(4/3)` を粘性下でも強制すると、
energyとnumber方程式が `pi:sigma=0` を要求する。一般のdissipative shearには使えない。

この構成則を定義してentropyが増えることだけでは非線形双曲性は証明されない。
近年のIS解析 [S4] も平衡時の速度検査と非線形の条件を明確に分離している。
本模型への適用は、電荷結合と(2)の項を実際に含むprincipal partについて行う。

## 2. 有限energy・総charge零・拘束を満たす厳密な初期データ

`k=2pi/L`, `epsilon` を振幅、`E_*=1` を基準field amplitudeとする。

\[
h_{ij}=\delta_{ij},\quad K_{ij}=-H_0h_{ij},\quad
E^x=\epsilon\sin(ky),\quad E^y=E^z=0,\quad B=0,
\]
\[
u_+=u_-=N,\quad \pi_+=\pi_-=0,\quad s_+=s_-=s_0,
\quad e_+=e_-=e_0-\frac{\epsilon^2}{4}\sin^2(ky),\quad
n_s=(e_s/\kappa)^{3/4}.
\tag{4}
\]

`epsilon^2<4e0` なら両密度は厳密に正。

\[
\rho_{total}=e_++e_-+\frac12E^2=2e_0,\quad j_i=0,
\quad H_0^2=\frac{16\pi G_Ne_0}{3}.
\]

Hamiltonianは `R(h)+K^2-K_ij K^ij=6H0^2=16pi G_N rho_total`。
Momentum constraintは `D_j(K^{ij}-h^{ij}K)=0=8pi G_N j^i`。
Maxwell constraintは `div E=partial_x E^x=0=rho_q`、`div B=0`。
粒子numberの総chargeは二種の同一データで厳密に零。

有限の初期切断energyは

\[
E_\Sigma(0)=2e_0 L^3,\qquad E_{EM}(0)=\epsilon^2 L^3/4.
\tag{5}
\]

このenergyは全matterのnormal energy。非定常compact時空の保存ADM energyではない。
初期電場の準備を無から生成したとは主張しない。有限energyの準備済みCauchy dataを与える問題である。
空間compactな模型であり、漸近平坦な実験室への埋込み・境界装置の構築ではない。

**負例:** 電場を加えてfluid密度を減らさず同じ `h,K,H0` を維持すると、
Hamiltonian residualは `-8pi G_N epsilon^2 sin^2(ky)` で零ではない。
また `K=0,h=delta,Lambda=0` に正energyを置く方法も不適合。

## 3. 自己重力背景、時計、観測frame

`epsilon=0` は、(2)の粘性tensorも零の厳密なradiation FLRW解。

\[
g_0=a(\eta)^2(-d\eta^2+dx^2+dy^2+dz^2),\quad a=1+H_0\eta,
\quad e_s=e_0a^{-4},\ n_s=n_0a^{-3}.
\tag{6}
\]

`kappa=e0/n0^(4/3)`。背景normalのproper timeは
`t=eta+H0 eta^2/2`。空間rod labelを初期 `x,y,z` に固定する。
背景に対するwave-map gaugeを選び、exact metricのnormal `N` と初期軸から得たorthonormal triadで
`v_s^hat i=(u_s.e_hat i)/(-u_s.N)` を比較する。

targetはcomoving spatial label `y` 上のsinusoidであり、physical wavelengthは `aL`。
任意に指定した固定physical-wavelength pulse全ての実装ではない。
proper-time pulseが必要なら、以下の `sin(Omega eta)` を上記の既知の `eta(t)` で合成して先に固定する。
`eta` の周期を時間商にすることはない。

二流体の反対向き一次速度と一次shear stressは全stressで打ち消す。
電磁stressと初期密度補償は二次。従って、この対称なdata族のmetric一次変分は零で、
metric/backreactionの最初の非自明項は `O(epsilon^2)`。
**有限振幅でmetricを背景へ固定してよいという主張ではない。**

## 4. 駆動が閉じた一次shear

まず非粘性 `pi=0`。conformally rescaledな一次fieldを

\[
v_+^{\hat x}=\epsilon v(\eta)\sin(ky),\quad v_-^{\hat x}=-v_+^{\hat x},\quad
E^{\hat x}=\epsilon a^{-2}\mathcal E(\eta)\sin(ky),\quad
B^{\hat z}=\epsilon a^{-2}\mathcal B(\eta)\cos(ky)
\]

とする。`Q=q n0`, `w0=4e0/3`。radiation EOSのためexpansion dragが相殺され、
物理場のconformal weightsを正しく入れると

\[
v'=\frac{Q}{w_0}\mathcal E,\quad
\mathcal E'=-k\mathcal B-2Qv,\quad
\mathcal B'=k\mathcal E.
\tag{7}
\]

ここでcurrent `2Qv` は解自身の未知量。初期 `(v,E,B)=(0,1,0)`。

\[
\Omega^2=k^2+2Q^2/w_0,\quad
v=\frac{Q}{w_0\Omega}\sin(\Omega\eta),\quad
\mathcal E=\cos(\Omega\eta),\quad
\mathcal B=\frac{k}{\Omega}\sin(\Omega\eta).
\tag{8}
\]

`T=pi/Omega` におけるtagged positive-fluid displacementは

\[
\delta x_+(T,y)=\frac{2\epsilon Q}{w_0\Omega^2}\sin(ky)+O(\epsilon^2).
\tag{9}
\]

全bulk fluidの一方向shearではなく、区別可能な一種のshearと他種の反対向き応答である。
初期 `curl E=-epsilon k cos(ky)e_z` は非零なので、potential forceの類推ではない。

正の二次wave energy

\[
\mathcal Q_0=(\mathcal E^2+\mathcal B^2)/4+w_0v^2/2=1/4
\tag{10}
\]

は閉じた(7)で保存する。これは `epsilon^2 L^3` を除いたconformal perturbation energyであり、
(5)の全切断energyと同じものではない。

半周期後に電場は反転し、停止後も次の運動が始まる。readout時点のgateであって、
外部操作なしの永久記憶・任意形状pulse・driver resetは構成していない。

## 5. 非粘性の非線形有限時間構成: 定性的な解析的帰結

非粘性EOSを固定し、任意の有限 `T` で `a>0` の背景(6)を取る。
十分小さい `|epsilon|` の(4)は、同じEinstein–Maxwell–二Euler方程式のsmoothなCauchy developmentを
`[0,T]` に持ち、その一次変分は(8)、metric一次変分は零になる。
これは以下の標準双曲型論の適用であり、正粘性の結論に読み替えない。

Eulerを `zeta=(sqrt(3)/4) log(e/e_ref)` とrest-space velocityで書くと、凍結principal blockは

\[
\begin{pmatrix}u\cdot\xi&c_s\xi_\perp^T\\c_s\xi_\perp&(u\cdot\xi)I_3\end{pmatrix},\quad c_s^2=1/3.
\]

timelike time covectorで正のsymmetrizerを持つ。二fluidのLorentz forceとMaxwell currentは
相手の微分を含まず、metricのfirst-order reductionでconnectionもlower-orderである。
Einsteinのwave block、Maxwell block、二つのEuler blockを結合して局所energy estimateを閉じる。
constraint伝播はcharge保存、Bianchi identity、全stress保存から得る。
単一charged fluidの既存reduction [S3] を二流体の証明済み定理として引用するのではなく、
上記のderivative orderを確認している。

smooth背景の有限区間を有限個の局所存在区間で覆い、高いSobolev normでのcontinuous dependenceを使う。
`H^m`, `m>=9` 等で十分にsmoothなdataを使えば、二階parameter variationを低いnormで評価できる。
`R=X_epsilon-X_0-epsilon X_1` に対する差分energy estimateは

\[
\|R\|_{C^0H^{m-2}\cap C^1H^{m-3}}
\le (C_{in}+T C_{src})e^{C_{st}T}\epsilon^2.
\tag{11}
\]

係数は正密度・timelike velocity・非退化metricのtube内での係数微分と背景normで決まる。
Sobolev embeddingによりvelocityとmetricの必要な `C^1` 評価になる。
同じsmooth解のcompact切断で `sup_[0,T] E_Sigma<infinity`。
具体的に `E_Sigma=2e0 L^3/a+O(epsilon^2)`。

**(11)の定数と許される具体的なepsilonは今回は計算していない。**
従って、例えば `epsilon=0.01` の完全な非線形gateが指定marginを通ると数値認定はしない。
この解析的帰結は独立査読・形式化しておらず、正粘性結合系の代用でもない。

## 6. 正粘性の線形gateを全時間で評価する

(2)のlinearizationで `pi_+^hat x hat y=epsilon a^-4 P(eta) cos(ky)`、反対種は逆符号。
`tau=tau0 a`, `mu=mu0 a^-3` と `4theta/3` 項によりconformal時間の定数係数へ戻る。

\[
v'=Q\mathcal E/w_0+kP/w_0,\quad
\mathcal E'=-k\mathcal B-2Qv,\quad \mathcal B'=k\mathcal E,\quad
\tau_0P'+P=-\mu_0kv.
\tag{12}
\]

比較値を **`k=Q=w0=1`, `e0=3/4`, `n0=q=1`, `mu0=1/1000`, `tau0=1/100`** に固定。
長さ・密度の単位を選んだdimensionless benchmarkであってSI値ではない。
例えば `H0=1/100` ならdimensionless `G_N=1/(40000pi)`。

平衡時のcharacteristic speedsは

\[
c_T^2=\mu_0/(\tau_0w_0)=1/10,\quad
c_L^2=1/3+4\mu_0/(3\tau_0w_0)=7/15<1.
\tag{13}
\]

正のrelaxation storageを含めると

\[
\mathcal Q=(\mathcal E^2+\mathcal B^2)/4+w_0v^2/2+\tau_0P^2/(2\mu_0),\quad
\boxed{\mathcal Q'=-P^2/\mu_0\le0}.
\tag{14}
\]

この損失はdriverを無から供給する項ではなく、完全なthermodynamic completionでheat/entropyへ入る。
(3)はそのために必要であり、波のenergy損失を全energyの消滅と数えない。

### 6.1 finite sampleを用いないuniform bound

`P(0)=0` と(14)から

\[
|v|\le1/\sqrt{2w_0},\qquad |P|\le\mu_0 k/\sqrt{2w_0}.
\]

非粘性解との差を `X=(sqrt(2w0) delta v,delta E,delta B)` に取る。
非粘性generatorはskew-adjointなので

\[
|X(\eta)|\le\nu k^2\eta,\quad
|\delta v|\le\nu k^2\eta/\sqrt{2w_0},\quad \nu=\mu_0/w_0.
\tag{15}
\]

`delta v'=Q delta E/w0+kP/w0` も同時に評価する。
`A0=1/sqrt(3)`, `Omega=sqrt(3)` に対し

\[
\|\delta v\|_{1,*}:=
\sup_{[0,T]\times\Sigma}\max\{
|\delta v|/A_0,\ |\partial_\eta\delta v|/(\Omega A_0),\
|\partial_y\delta v|/(kA_0)\}.
\]

`pi<22/7`, `5/3<sqrt(3)<7/4`, `sqrt(2)>7/5`, `T<66/35` を用いると

\[
\boxed{\|\delta v\|_{1,*}<13/5000=0.0026},\qquad
\boxed{\frac{|\delta d(T)|}{2/3}<121/68600<9/5000=0.0018}.
\tag{16}
\]

node sampling、root fitting、浮動小数点の桁一致から推測した上界ではない。
これは**線形解間**のbound。非線形Einstein補正を含むboundではない。

### 6.2 独立に包囲した終点

`T=pi/sqrt(3)=1.81379936423421785...`。値はepsilonを除いたmodal amplitudes。

| 量 | (12)の値 |
|---|---:|
| v(T) | -0.0002279295703417076643 |
| E(T) | -0.9993959041245718143 |
| B(T) | 0.000438238870267276743 |
| P(T) | -0.00000976323138940158338 |
| d(T) | 0.6662660729228784230 |
| 変位相対誤差 | 0.0006008906156823654 |
| Q(0)-Q(T) | 0.0003018822388826083 |

正粘性では `v(T)` は厳密な零でない。この不一致を成功判定で隠さない。
独立verifierはMachin公式と整数平方根でTを包囲し、
`h=1/128` の232stepと最後の端数stepを32次matrix exponential＋厳密剰余で包囲する。
全endpointの区間幅は `2.264e-37` 未満。これは線形ODEの包囲である。

## 7. 非線形rest-frame principal-symbolの限定的な補題

平衡速度(13)だけで非線形causalityをPASSにしないため、(2)の非平衡項を含めた補題を追加した。
以下は各点で係数を凍結した流体静止frameの物理的変数についての計算。
`P=pi/w`, `||P||_op<=delta=10^-3`, `alpha=mu/(tau w)=1/10`。
`n` はここだけ単位wave direction（粒子密度ではない）とする。

`w` を凍結してvariationを規格化し、energyとSTF stressをY、速度variationをvとする。
`theta=n.v`, `sigma=(nv^T+vn^T)/2-I theta/3` に対して

\[
Bv=(\theta+P:\sigma,\quad
2\alpha\sigma+\tfrac43P\theta+\tfrac43P(P:\sigma)).
\]

momentum inertiaを `M=I+P`、stress divergence mapを `D Y=(delta e/3)n+delta pi.n` と書く。
`L=M^-1 D B=M^-1 A` の3x3 acoustic blockは、`r=P n` として

\[
A=\alpha I+\tfrac{1+\alpha}{3}nn^T+\tfrac13nr^T+\tfrac43rn^T+\tfrac43rr^T.
\tag{17}
\]

コードはSTF式からBを作り、(17)を別に照合する。任意の対称tracefree Pを残して

\[
H=M-\frac3{4\alpha}Mnn^TM,\qquad \boxed{HL=L^TH}
\tag{18}
\]

を記号的に検査する。H自体は不定符号であり、正symmetrizerと誤認しない。

平衡 `L0=alpha I+(1+alpha)nn^T/3` のsquared speedsは `1/10,1/10,7/15`。
operator normによる一様な摂動評価は

\[
\|L-L0\|\le d:=\frac{(5/3+7/15)\delta+(4/3)\delta^2}{1-\delta}
=\frac{1601}{749250}.
\]

縦modeの周囲にradius `r0=(7/15-1/10)/3=11/90` のRiesz contourを取る。
Neumann resolvent評価でそのrank-one projector `PiL` と平衡projector `nn^T` の差は

\[
\|\Pi_L-nn^T\|\le s:=d/(r0-d)=1601/89974.
\]

`||H-H0||<=h=delta+(15/2)(2delta+delta^2)=6403/400000`。
横invariant subspace上の単位vectorには
`x^T H x >= 1-(15/2)s^2-h >0.98`、縦subspaceでは
`x^T H x <= 1-15/2+(15/2)s^2+h <-6.48`。
(18)により異なるspectral subspaceはH-直交である。
従って `H(I-2PiL)` は正、Lはそのinner productでself-adjoint。
横modeが縮退してもdefinite subspace内で対角化でき、単なるdiscriminant samplingに依存しない。

全squared speedsは

\[
36662/374625\le c^2\le351251/749250,
\quad \text{すなわち約 }[0.09786,0.46881]\subset(0,1).
\tag{19}
\]

zero-speed modesも除外しない。`C=M^-1 D`、`CB=L` が可逆なので
`z=L^-1 C Y`, `Y0=Y-Bz` によって、principal blockは
`z_t+v_x=0`, `v_t+L z_x=0`, `(Y0)_t=0` に分かれる。
particle-density variationは `delta n-n_background(n.z)` を取れば追加のzero-speed modeとなる。
これによりrest-frame frozen systemのzero eigenvaluesもsemisimpleである。
回転covarianceにより `n=e1` の記号検査は任意方向の同じ恒等式を与える。

**射程:** これは指定構成則の有限行列補題とそのnorm評価である。
二流体の異なるrest frameを同じCauchy timeへ写したfull reduction、
このtube内で解が全gate時間留まる非線形estimate、およびその計算可能な定数を、この補題だけで認定しない。
なお同じtubeでは `|p+lambda(pi)|/e <= (1+4delta)/3=251/750<1` なので各流体はDECを満たす。
entropy storageは `tau(pi:pi)/(4mu T) <= n delta^2/alpha=10^-5 n`。
従って `s>=1/2` ならentropy densityも正である。tubeに解が留まる評価は依然必要。
[S4]の一般結果をこの正確な構成則へ適用する場合も全条件の照合を要する。

## 8. full R1へ残る一つの判定問題

(2)を保持したEinstein–Maxwell–二粘性流体系で、共通切断・固定gaugeについて

\[
\sup_{0\le\eta\le T}\|v_{+,\epsilon}-\epsilon v_{+,lin}\|_{1,*}
\le C_*\epsilon^2,
\quad \|\pi_s/w_s\|_{op}\le10^{-3},\quad
\sup E_\Sigma\le E_{max}<\infty
\tag{20}
\]

を、明示的な非零epsilonと計算可能なC_*でcertifyすること。
physical frame、proper-time conversion、density・entropy positivity、Einstein/Maxwell constraint propagationを含める。
例えばfull relative error 1%を要求するなら線形に0.26%を割り当てた残りについて
`C_* epsilon <= 0.0074`（規格化したC_*）が必要である。
今回C_*を任意に小さい数へ置いてPASSにはしていない。

これは「外力を貼る」問題から、具体的な閉じた非線形PDEの有限時間誤差証明へ課題を絞った、という進展。
(20)を満たす前に元R1全体を完了へ変更しない。
ここで得るdevelopmentはglobal timeを持つ有限GH slabで、CTCを含まない。
その後のRSET・Hadamard・semiclassical feedbackは別課題のまま。

## 9. 再現と一次資料

[検証記録](r1-closed-shear-validation.md)、
[順方向計算](../src/symbolic/r1_closed_shear.py)、
[独立有理・区間検算](../src/symbolic/r1_closed_shear_verify.py)。

```bash
python src/symbolic/r1_closed_shear.py --output /tmp/r1-forward.json
python src/symbolic/r1_closed_shear_verify.py --evidence /tmp/r1-forward.json --output /tmp/r1-verify.json
```

- **S1:** S. Koide, *Generalized Relativistic Magnetohydrodynamic Equations for Pair and Electron-Ion Plasmas* (2009), https://arxiv.org/abs/0902.4292 . 二流体と電磁場を区別する比較一次資料。ここで選んだEOS・gateの完成定理ではない。
- **S2:** D. S. Balsara et al., *A High-Order Relativistic Two-Fluid Electrodynamic Scheme ...* (2016), https://arxiv.org/abs/1603.06975 . full Maxwell displacement currentと動的二fluidを扱う比較。
- **S3:** D. Pugliese, J. A. Valiente Kroon, *On the evolution equations for ideal magnetohydrodynamics in curved spacetime*, arXiv:1112.1525v2, https://arxiv.org/html/1112.1525v2 . 単一charged-fluidのhyperbolic reduction。二流体・(2)を無条件に包含するとは扱わない。原稿自身がconstraint propagationの詳細を省略する点も区別する。
- **S4:** I. Cordeiro et al., *Nonlinear Causality and Strong Hyperbolicity of Einstein-Israel-Stewart Theories of Transient Relativistic Fluid Dynamics* (2026), arXiv:2607.05639v1, https://arxiv.org/html/2607.05639v1 . 非線形principal条件、Theorem 4、Einstein結合Section VIを参照。平衡時速度だけをfull theoremへ代入して済ませない。今回全証明の独立査読はしていない。

閲覧2026-10-08。Family 376の原本・台帳は前PR部分を保持し、今回のsource/geometry/QFTの各射程を混同しない。
