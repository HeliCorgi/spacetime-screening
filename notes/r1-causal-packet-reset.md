# R1補足: 空間因果性、過渡shear、保持とresetの両立条件

2026-10-08。PR #40 の親 `d679f9585cc89518981ce03f6075bab8fb5256fd` に対する追加監査。
[有限資源監査](family376-finite-resource-matter-audit.md)、
[現行R1](r1-closed-shear-driver.md)の方程式・輸送係数・従来のassertは変更しない。
**全入力・任意長の有限資源相対論的埋込みの分類はDのまま。**
本稿の限定された排除結果は**同じ線形R1の「無改造・受動的な変位保持／reset」仕様**に関するCであり、
元R1の有限時間gate、Family 376、非線形流体、計算一般のno-goではない。

## 0. 今回追加した結果と出典の区別

添付依頼の原稿9件・候補4系統・11条件の監査は親版に保存済みである。
OpenAI/math の現mainも `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` と再確認した。
原稿を再度独立査読したとも、upstream Leanの全依存を再buildしたとも主張しない。
今回のL1–L4は、現R1式(12)の線形shear系を出発点に、本稿で導出する限定的な計算・補題である。
Family 376や一般的なIsrael–Stewart論文の既知定理として帰属させない。
連続体の全証明をLean形式化したものでも、独立査読済みの新定理でもない。

| 追加項目 | 結果 | 限界 |
|---|---|---|
| 空間を含む閉じた線形PDE | symmetrizer、局所energy flux、有限伝播、Sobolev安定性 | 正粘性の全非線形Einstein系ではない |
| 局在した初期電場 | 元R1のdensity compensationを任意のsmooth profileへ拡張できる | 初期拘束のみ。物理的準備は未構成 |
| resetと保持 | 変位を含む保存量、近似resetの定量的上限 | 同じ線形系、同じ初期族、指定したreset norm |
| 長時間の線形挙動 | 固定した非零波数では全modeが減衰し、変位も0に戻る | 非線形の無限時間挙動へは外挿しない |
| 数値scheme | 厳密な局所supportとenergy accountingを持つ最小stencil | 数値粘性を物理的発熱と別会計にする |
| 負例 | energyを厳密保存しても、一stepで遠隔格子に漏れるscheme | 連続体Maxwellの非因果性を意味しない |

## 1. 空間PDEを固定する

記号は親版に合わせる。`eta` はconformal time、`mu` は粘性、`tau` は緩和時間。
`w,Q,mu,tau` は正のrescaled定数、Qは親版の `q n0`。
背景は親版のradiation FLRW `g0=a(eta)^2(-deta^2+dx^2+dy^2+dz^2)`。
反対電荷種の一次速度・shear stressが相殺するsectorなので、初期条件に適合するmetric一次変分は0。
**有限振幅のmetricをg0へ固定してよいという意味ではない。**

`v(eta,y), E(eta,y), B(eta,y), Pi(eta,y)` を正種の横速度と電磁・shear振幅とする。

\[
w v_\eta=QE-\Pi_y,\qquad
E_\eta=B_y-2Qv,\qquad B_\eta=E_y,\qquad
\tau\Pi_\eta+\Pi=-\mu v_y. \tag{1}
\]

空間一方向への対称性制限であり、x,z方向も含む一般の非線形摂動ではない。
外部電流は指定しない。`-2Qv` は二流体の電流で、電場の反作用を保持する。
`v,E ~ sin(ky)`、`B,Pi ~ cos(ky)` を代入すると、親版式(12)の4x4 generatorに厳密に戻る。
ソースから軌道を逆算して自由なforcingを貼る操作を加えていない。

以下は局所問題ではR_y上、全energyの解釈では親版同様T³上を用いる。
R_y×T²の一様正密度背景は**全rest energyが無限**である。perturbationがcompactでも有限実験室と認定しない。
T³では全初期matter energyが有限だが、vacuum外部の有限装置を構成したわけではない。

### 1.1 smoothな局在データの初期拘束

親版の `sin(ky)` を任意のsmooth periodic profile `chi(y)` に置き換える。
例えば `R=1/4 < pi`、

\[
\psi(y)=\begin{cases}\exp(1-[1-(y/R)^2]^{-1}),&|y|<R,\\0,&|y|\ge R,\end{cases}
\quad \chi(y)=\sin y\,\psi(y)
\]

を2pi周期で延長すればC∞、奇関数、平均0、`|chi|<=1` である。
初期データを

\[
E^x=\epsilon\chi(y),\quad B=0,\quad u_+=u_-=N,\quad\pi_\pm=0,
\quad e_\pm=e_0-\epsilon^2\chi(y)^2/4,\quad h_{ij}=\delta_{ij},\ K_{ij}=-H_0h_{ij}
\]

とし、親版EOSで同じ初期entropyからnを決める。
`epsilon^2<4e0` で正密度、総電荷0。
`rho_total=2e0`、`j=0`、`div E=partial_x E^x=0`、`div B=0` なので、
`H0^2=16pi G_N e0/3` は厳密なEinstein/Maxwell初期拘束を解く。
全matter初期切断energyは `2e0 L^3`。
この操作は準備済みデータの構成であり、driver製造・初期化の実験過程ではない。
非線形ではdensity gradient、縦流、quadratic stressとmetric反作用が残る。

## 2. L1: 線形PDEの因果性とwell-posedness

`z=(v,E,B,Pi)` として `z_eta+C z_y=R z` と書く。

\[
H=\operatorname{diag}(2w,1,1,2\tau/\mu)>0,\qquad HC=C^TH,
\quad HR+R^TH=\operatorname{diag}(0,0,0,-4/\mu). \tag{2}
\]

principal speedsは `±1, ±sqrt(mu/(tau w))`。

\[
q=wv^2+(E^2+B^2)/2+\tau\Pi^2/\mu,\quad
f=2v\Pi-EB,\quad
\boxed{q_\eta+f_y=-2\Pi^2/\mu}. \tag{3}
\]

`mu<=tau w` なら次の平方和が非負になる。

\[
q\pm f=(E\mp B)^2/2+w(v\pm\Pi/w)^2
 +(\tau/\mu-1/w)\Pi^2\ge0. \tag{4}
\]

従って `|f|<=q`。これは**線形perturbation normのflux bound**であり、matter stressのDEC/NECの証明ではない。
本sectorの条件だけで縦sound modesまで認定しない。親版の平衡縦速度は別に `c_L²=7/15` である。

初期supportを `[-R,R]` とし、例えば右の外部energyを
`Eout(eta)=integral_(R+eta)^infinity q dy` と取ると、

\[
E_{out}'=f(R+\eta)-q(R+\eta)-\int_{R+\eta}^\infty2\Pi^2/\mu\,dy\le0.
\]

初期外部energyが0なので、その領域で解は0。左側も同様。従って影響は光速を越えない。
T³では被覆上で同じ結果を使い、巻き戻りが始まる前に局所supportを読む。
`R=1/4, 0<=eta<=2` では `R+eta<pi` なので親版L=2piの区間を跨いで回り込まない。

係数は定数で、空間微分は方程式と可換。各整数sについて、

\[
\sum_{j=0}^s\int(\partial_y^jz)^TH(\partial_y^jz)dy
\le\sum_{j=0}^s\int(\partial_y^jz_0)^TH(\partial_y^jz_0)dy. \tag{5}
\]

Fourier側の解 `exp[(R-i xi C)eta] zhat0` は同じH-normでcontractiveなので、
H^sデータに対する存在・一意性・連続依存を与える。smoothデータのsmooth線形解も得られる。
一般の非平衡IS/Einstein系の共通切断symmetrizerやtube invarianceを(5)で代用しない。

### 2.1 finite-time preparationについて得られるもの

同じ線形PDEのゼロ初期データから、何のdriver perturbationも加えずにpulseが自発的に生じることは一意性に反する。
非零の準備済み電場は必要な入力資源である。
さらに、初期差または追加の操作がある領域と観測点の距離をDとすれば、
このsectorでその差を届けるにはconformal timeで少なくともDが必要。
これは準備時間の**必要条件**であり、指定電場を作る装置の存在・総仕事・Einstein拘束の伝播を証明しない。
事前に用意された相関や遠隔driverを、距離Dの局所操作だけだったと読み替えてはいけない。

## 3. L2: 変位保存量とresetの定量的障害

ここからは一つの**非零波数** `k>0`。親版のmode変数を `v,E,B,P`、
正種の一次comoving変位を `d'=v, d(0)=0` とする。

\[
v'=QE/w+kP/w,\quad E'=-kB-2Qv,\quad B'=kE,
\quad\tau P'+P=-\mu kv. \tag{6}
\]

計算を直接代入すると、

\[
\boxed{J=wk v-QB+\tau k^2P+\mu k^3d,\quad J'=0}. \tag{7}
\]

現R1の初期族 `v(0)=B(0)=P(0)=d(0)=0` ではJ=0であり、E(0)は任意でよい。
これにより

\[
\boxed{d={QB-wkv-\tau k^2P\over\mu k^3}}. \tag{8}
\]

**同時に `v=B=P=0` へresetすると、dも0である。**
Eをどう残しても、この三変数の厳密resetと非零shear保持は両立しない。
ただしこれは元R1に後から加える「保持・reset」仕様の排除であり、元の有限区間gate自体の失敗を意味しない。
有限時刻の読み出しに記録を別装置へ移すこと、残存fieldも含めて次のgateを設計することは排除していない。

近似resetの定量版は

\[
|d|\le{Q|B|+wk|v|+\tau k^2|P|\over\mu k^3}. \tag{9}
\]

親版の `w=Q=k=1, mu=1/1000, tau=1/100` では、

\[
d=1000B-1000v-10P.
\]

epsilonを除いたdimensionless modeで `|v|,|B|,|P|<=10^-6` と要求すれば
`|d|<=201/100000=0.00201`。従って `d>=3/5` という保持仕様とは矛盾する。
異なる単位や未規格化の実振幅へこの数値閾値を無断で移さない。

残す必要があるmodal wave/storage energyにも下界を付けられる。

\[
\mathcal Q=wv^2/2+(E^2+B^2)/4+\tau P^2/(2\mu),\qquad
\boxed{\mathcal Q\ge{\mu^2k^6d^2\over2wk^2+4Q^2+2\mu\tau k^4}}. \tag{10}
\]

(7)とweighted Cauchy–Schwarzによる。背景を含む全matter energyの下界とは別。
`v=P=0` に限定すると `B=mu k^3d/Q`、従って磁場部分だけで `mu²k⁶d²/(4Q²)` が必要。
非零の残留fieldを持てることから、無入力でその状態を永久保持できるとはまだ言えない。

### 3.1 局在packetでの対応する保存量

(1)と `d_eta=v` から、

\[
\boxed{\partial_\eta(wv_y-QB-\tau\Pi_{yy}-\mu d_{yyy})=0}. \tag{11}
\]

初期 `v=B=Pi=d=0` なら括弧内は0。
周期的なpacket全体を `v=B=Pi=0` にすると `d_yyy=0` なのでdは空間定数。
初期Eの平均が0なら、平均v,Eの閉じた零modeも0のままで平均d=0。従って**packet全体のd=0**。
R上でdがcompact supportを保つ有限区間なら、`d_yyy=0` とcompact性からもd=0になる。
これをR上の有限total rest energyの証明に読み替えない。

## 4. L3: 受動的に放置した非零modeは線形変位を消す

(6)では `Q,w,k,mu,tau>0` を固定する。
固有vectorに対するenergy identity `Q'=-P²/mu` から全固有値の実部は非正。
虚軸上の固有値があれば、その固有vectorはP=0でなければならない。
最後の方程式がv=0、第一がE=0、第二がB=0を強制し、非零の固有vectorに矛盾する。
従って全固有値は実部が厳密に負で、各固定modeの全変数は指数減衰する。
Jordan blockがある場合の有限次の多項式因子も指数減衰を妨げない。
(8)より、同じ初期族について**dも0へ戻る**。

独立な確認として、特性多項式を分母tau*wを払って書くと

\[
p(\lambda)=\tau w\lambda^4+w\lambda^3
 +[2Q^2\tau+\mu k^2+\tau wk^2]\lambda^2
 +(2Q^2+wk^2)\lambda+\mu k^4.
\]

Hurwitz minorsは

\[
\Delta_2=\mu wk^2>0,\quad\Delta_3=2\mu wQ^2k^2>0,
\quad\Delta_4=\mu k^4\Delta_3>0.
\]

Q=0ではMaxwellのundamped modeがあり、k=0では零modeが残る。
mu=0では(8)で割れず、非粘性の半周期に `v=B=P=0` かつ `d=2/3` は可能。
これらを排除しないと定理文が誤る。負例として検査している。
また全波数に共通な減衰定数を本証明から推定しない。

親版の係数を変えず、同じ `T=pi/sqrt(3)` で再計算した参考値:

| conformal time | d（epsilonを除く） |
|---|---:|
| T | 0.666266072922878423035577461730 |
| 2T | -1.156935833786291765169865855e-7 |
| 1000 | 0.359983987416714100331412788495 |
| 10000 | 0.0186734238511709230374100350564 |
| 60000 | 7.926911776394703532040920183e-11 |

変位は単調減少ではなく、減衰する振動である。大きな時間のsampleから極限を推測したのではない。
独立verifierは行列指数を使わず、Laplace像 `dhat=Q(tau s+1)/p(s)` の留数から再計算する。
**非線形剰余がこの長時間も小さいという定理はない。線形の極限を非線形物質源の不存在へ外挿しない。**

## 5. L4: energy-conservingとcausal stencilは別

### 5.1 独立な空間support・収支テスト

(1)の定数係数を使い、CFL=1、`Delta eta=Delta y=h` のlocal Lax–Friedrichs輸送を

\[
z_j^*={(I+C)z_{j-1}+(I-C)z_{j+1}\over2}
\]

とする。その前後に各格子点内だけのR-sourceのimplicit midpoint半stepを入れる。
`H(I±C)>=0` なので輸送はH-normでcontractive。sourceも(2)によりcontractive。
一stepにつき一cellだけ影響が広がるため、h=dtの数値coneは光coneを越えない。
33cell、h=1/8、中心のgrid impulse、6stepについて、外部は**有理数として厳密に0**。
このimpulseテストをsmooth continuum initial dataの実験と称しない。

sourceの失うenergyを緩和発熱として加算し、輸送の人工的なenergy損失を別に記録する。
毎stepで `field energy + source heat + numerical diffusion = initial energy` を厳密に検査する。
**数値粘性を物理的な発熱に足して完成したthermodynamic modelと呼ばない。**

別のsmooth Fourier-mode収束診断では、L=8、k=pi/4、T=1、同じw,Q,mu,tauを使う。
親版のk=1・T=pi/sqrt(3)の区間証明書とは別の試験である。

| grid cells | steps | max endpoint error |
|---:|---:|---:|
| 64 | 8 | 0.013463759828030313 |
| 128 | 16 | 0.006275385820346228 |
| 256 | 32 | 0.003003501247323467 |
| 512 | 64 | 0.001466983294078724 |

比は約2.1455,2.0894,2.0474で一次収束と整合する。
これは数値的診断であり、全非線形PDEの収束や誤差上界の証明ではない。

### 5.2 負例: norm保存だけでは有限伝播は通らない

光速1のMaxwell characteristic一つをscalar advectionとして、周期9cell・dx=1のcentered derivative Dで離散化する。
Dはskewで、implicit midpointの `M=(I-dt D/2)^-1(I+dt D/2)` は厳密に `M^TM=I`。
しかしdt=1/4で一cellの初期値から、3cell離れた成分へ

\[
(M e_0)_3=2130530/4447739401\ne0
\]

が一stepで出る。局所energyの保存と、厳密なdiscrete domain of dependenceは独立である。
これは前回の**modeだけのmidpoint会計の誤りではない**。それが空間因果性も証明したと読むことを防ぐ負例。
このschemeが連続体の因果解へ収束できないという主張でもない。

## 6. 依頼の11条件への差分

| 条件 | 今回追加した支持 | 未解決のままの部分 |
|---|---|---|
| finite total energy | T³の初期拘束族と有限の線形perturbation norm | full nonlinearの一様energy、製造・memory・reset装置 |
| compact/finite support | smooth局在摂動とL1のsupport bound | vacuum外部を持つ全物質の有限装置 |
| finite-time preparation | L1からの必要な伝播時間 | 実際の閉じた準備過程と資源見積り |
| finite propagation | transverse線形PDEの光cone bound | 共通切断でのfull nonlinear characteristic制御 |
| hyperbolicity | 正の定数symmetrizer H | 非線形の一様symmetrizerとtube invariance |
| DEC/NEC | 親版の初期正密度の射程を保持 | q-fluxをDECと同一視しない。全非線形発展は未認定 |
| smoothness | smooth初期値の線形発展 | nonlinear Sobolev bound |
| stability | 全時間の線形H^s contraction | nonlinear安定性、noise下での符号記録 |
| well-posed IVP | Fourier解とenergy estimateによる線形IVP | Einstein・二種の非平衡構成則を含む全系 |
| backreaction | 一次metricの相殺を保持 | O(epsilon²)の同じmetricでの全gate-time estimate |
| conservation | 局所wave/heat flux、変位保存量、離散収支 | 全stressと準備・保持装置まで含む非線形解 |

従って総合Dは変更しない。L2–L3のCは無改造・受動linear reset仕様だけに適用する。
Family 376のTM符号化を(1)へ忠実に写したとは主張しない。NSは依然非圧縮parabolicで別の初期値問題。
原稿のexact-data universality、有限prefix、任意長の同一有限資源実験を混同しない。

## 7. 次の一問と停止判定基準

**元R1の固定された正粘性構成則を保ち、共通Cauchy切断上で `0<=eta<=pi/sqrt(3)` の非線形発展に対し、
計算可能な剰余定数C_*と具体的な非零epsilonを与えられるか。**
ここには縦流・density/entropy変化・quadratic Maxwell stress・Einstein拘束伝播・physical frame変換を含める。

本稿のreset排除はこの有限時間存在問題を解かない。元R1は永久保持や完全resetを成功条件にしていないからである。
全gate-timeの非線形boundが得られた後、複数gateへ進む場合は残存field/heatも次の初期状態に渡す必要がある。
勝手に全変数をresetして非零dだけを残すcompilerはL2の整合性検査に失敗する。
別memoryやlatchを追加する場合は、その作用・stress・有限energy・有限伝播・保存則を再度証明する。
CTC/Hadamard/RSET/SCEEの判定はこの有限GH slabの問題とは別であり、今回変更しない。

## 8. 原著との適用範囲

- [現行R1の固定式・仮定](https://github.com/HeliCorgi/spacetime-screening/blob/d679f9585cc89518981ce03f6075bab8fb5256fd/notes/r1-closed-shear-driver.md): (1),(6)の入力。L1–L4の帰属元ではない。
- [Family 376 scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/376.md): 原稿・形式化の境界。今回全依存を再buildしない。
- Bemfica, Disconzi, Noronha, *Causality of the Einstein-Israel-Stewart Theory with Bulk Viscosity*, [arXiv:1901.06701v2](https://arxiv.org/abs/1901.06701v2): shear/diffusionなしのbulk系。今回の二shear-fluidの完成証明に使わない。
- Cordeiro, Bemfica, Speranza, Noronha, *Nonlinear causality and strong hyperbolicity of baryon-rich Israel-Stewart hydrodynamics*, [arXiv:2510.01512v1](https://arxiv.org/abs/2510.01512v1): 適用するなら構成則の全係数・仮定の照合が必要。本稿はabstractのscope確認に留め、全定理の適用は主張しない。

[実装と再現記録](r1-causal-packet-validation.md)。
