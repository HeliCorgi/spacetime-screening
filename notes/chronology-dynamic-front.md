# 動的formationの直接探索: moving Grant wallからsmooth drift-frontへ

2026-10-09 JST。PR #40、親 `7410fa94786ffe43c74ade1e4dc00ee2ce355127`。
[前段のESU/Ori/Grant解析](chronology-formation-mainline.md)と
[今回の再現記録](chronology-dynamic-front-validation.md)。署名(-+++)。

## 0. 到達点と証拠の水準

今回は一つの修正系列だけを追った:
**Grant cutを因果的なwallで開く → wallを有限厚化する → 切取りのないsmooth drift-frontへ変形する → 駆動を局在化する**。
ESUの永続的mean-SCEE構成は正の対照、Oriのcovector検査は失敗を検出する手段として用いる。
古い候補の追加リストやFamily 376のcompilerを必要条件にはしない。

中心結果は§3の**affine-time drift-frontクラスに対するno-Hadamard命題**。
非compactな横方向へ形成開始を逃がし、最初の有限位置の閉null円をなくしても、
変分問題から別のnull自己帰還が必ず存在する。単なる数値探索の不成功ではない。
logistic profileでは証人・初期拘束・局所保存則・有限の幾何学的stress予算を具体的に計算した。
有限厚potential、正のconformal変形、小さいmetric反作用、単純なholonomy echo、局在したswitchまで修復を検査した。

**結論:** この修正系列は、通常のglobal normally-hyperbolic bisolutionと全点の局所Hadamard性を含む
同時仕様を満たせない。全ての物質・全ての形成時空の一般no-goではない。
物理的な形成解、全RSET、SCEE発展を得たとの主張もしない。元問題全体の分類は4のままだが、
この具体的な動的クラスの同時仕様は解析的に排除した。

以下の変分適用、定量評価、修復判定は今回の導出。手法の優先権・独立査読済み・Lean形式証明とは称しない。
既知の基礎はHadamard/WF、特異性伝播、GH上の状態構成、KRW [K,Q]。
コードは幾何・有限計算・不等式を検査し、これらの連続体定理を自動証明しない。

## 1. ESUを形成の初期データへ使う際の制約

前段の時間商ESUと、その因果的な被覆 `R x S3` は同じ局所metricと熱RSETを持つ。
従って、同じ固定coupling/繰込み処方で、被覆にも自己無撞着な静的mean-SCEE解と正のHadamard熱状態がある。
ただし被覆はCTCを持たず、時間商は最初からCTCを持つ。
正のsmooth conformal factorは因果関係を変えないので、被覆のconformal変形だけでは形成できない。

「過去では同一視なし、後で時間を同一視」は一つの固定されたsmooth quotientではない。
また、connected spacetimeのisometryが開いた過去で恒等写像なら、点と微分を保つisometryの一意性から全体で恒等。
従って商を単に局所的にswitch-onする操作を、物質のCauchy発展と数えない。
形成には非conformalなmetric変化、または別に定義した接合/境界の力学が必要である。

**本稿の新しいdrift-frontはESUと同じ大域トポロジーではない。** ESUのbetaやRSETを新metricへ貼らない。
§4のfinite-stress計算もLambda=0での診断であり、ESUの正のLambdaを無断で変えて同じSCEE解だとしない。

## 2. 最初の設計: Grant cutのtimelikeな動的wall

前段のboostを `alpha=log 2`、driftをb=1とする。Rindler側で

\[
 g=dr^2+dz^2-r^2d\eta^2+dy^2,
 \quad (\eta,y)\sim(\eta+\alpha,y+b).
\]

`theta=eta/alpha`、`T=y-b theta` とすると

\[
 g=dr^2+dz^2+dT^2+2b\,dT d\theta+(b^2-\alpha^2r^2)d\theta^2,
 \quad\theta\sim\theta+1.
\tag{1}
\]

`0<r<b/alpha` では `g^{TT}=1-b^2/(alpha^2 r^2)<0`。有限annulusと周期zを使うこともできるが、
その場合は**内外両wallの場・stress・境界条件**が必要になる。
外wallを `r=R(T)` とし、Rが臨界半径b/alphaを横切る設計を試す。

\[
 h=(1+\dot R^2)dT^2+2b\,dT d\theta+C(T)d\theta^2+dz^2,
 \quad C=b^2-\alpha^2R^2,
\]
\[
 \det h=(1+\dot R^2)C-b^2.
\tag{2}
\]

横断時もdet h=-b^2で非退化。material tangent
`U=partial_T-(1/b)partial_theta`（pullback座標で）は

\[
 h(U,U)=\dot R^2-\alpha^2R^2/b^2.
\]

例えば局所的な `R=b/alpha+vT`, `0<v<1` を十分狭い横断区間で選べばUはtimelike。
**「wallがCTC閾値へ達するには直ちに超光速」という拒否は誤り**であり、このkinematic修復は通る。
ただしkinematicsからwallの作用、Israel接合、有限energyの製造過程は従わない。

### 2.1 wallを量子的に完成しようとすると

C=0でwall内部の `K=partial_theta` は閉null測地線になり、

\[
 \nabla^h_KK=\kappa K,\qquad \kappa=\alpha\dot R,
 \quad {k_{\rm out}\over k_{\rm in}}=e^{-\alpha\dot R}.
\tag{3}
\]

従って、このworldvolumeに通常の線形KG型wall自由度を置き、その全点Hadamard性を保つ案は
非単位returnで失敗する。これは**wall自由度をそのように選んだ模型**の排除であり、
全ての物質wallやbulk fieldに自動的に適用した定理ではない。

速度を横断時だけ零へflattenしても、Cがsmoothに正から負へ変わる場合の近傍windingを調べる必要がある。
`D=sqrt(b^2-(1+Rdot^2)C)>0`、
`theta=psi-q(T), q'=(1+Rdot^2)/(b+D)`、`X=integral D dT` とすると
`h=2dX dpsi+C(T(X))dpsi^2+dz^2`。
前段§5と同じ、局所の短いnull方向と外を巻くnull方向の不一致が残る。
ゼロboostだけではこのwallモデルを修復できない。

音速の小さい現象論的wallやfieldを置かない理想鏡は(3)の直接対象外。
しかしそれでbulkのW、反射に必要なboundary-Hadamard条件、wallのRSET/保存則が完成するわけではない。
通常のGH内部のHadamard parametrixを反射点へそのまま用いることも不可 [B]。

### 2.2 有限厚の物質へ置き換える修復

固定された完全なbulk上のsmoothな壁場Dとprobe phiに、例えば

\[
 S_{D,\phi}=\int[-\tfrac12(\nabla D)^2-U(D)
 -\tfrac12(\nabla\phi)^2-\tfrac12(m^2+V(D))\phi^2]\,dV
\]

を用いると、古典的なon-shell exchangeは

\[
 \nabla_\mu T_\phi^{\mu}{}_{\nu}=-\tfrac12\phi^2\nabla_\nu V,
 \quad \nabla_\mu T_D^{\mu}{}_{\nu}=+\tfrac12\phi^2\nabla_\nu V.
\tag{4}
\]

量子的にも対応するmatched renormalized Ward identityが必要で、Vを外部指定して反作用を捨てない。
これは保存則を修復する具体的なcoupling案だが、本稿でcoupled solutionを得たわけではない。

**有限でsmoothなpotentialはprincipal symbolを変えない。** 完全なGrant geometryへ壁を有限厚化しただけなら、
切取りで消えていたbulk null chordは再び存在し、特異性を伝播する。
大きいmass gapや低周波の反射率は、そのUV/WF障害を消さない。
理想的な完全反射・境界での作用素domain変更は別問題であり、smooth potentialへの議論と混同しない。
そこで次に、wallだけでなくbulk metricそのものを変える。

## 3. 第二の設計: 境界のないsmooth drift-front

\[
 M=\mathbb R_t\times S^1_\ell\times\mathbb R_r\times S^1_{L_z},\qquad
 g=-2dt\,d\psi+[f(r)-\gamma t]d\psi^2+dr^2+dz^2,
 \quad\gamma>0.
\tag{5}
\]

fはsmoothかつ下に有界。具体例は `gamma=ell=Lz=1`, `f(r)=1/(1+exp r)`。
この例は(1)の座標書換えだとは主張しない。
fがaffineなら(5)は局所的にflatなboost/drift型であり、非linear fはsmoothな曲率源を入れる修復である。
全座標はこのbenchmarkでは無次元。全体を一定長さスケールの二乗で拡大しても、以下のreturn obstructionは変わらない。

`det g=-1`, `g^{tt}=gamma t-f`。具体例ではt<0の全領域がGH。
実際、F=f-t>0でcausal curveは

\[
 F(\dot\psi-\dot t/F)^2+\dot r^2+\dot z^2\le \dot t^2/F
\]

を満たす。任意の閉じた負時間slabで `|dr/dt|,|dz/dt|<=1/sqrt(-t)`、
`|dpsi/dt|<=2/(-t)`。横方向の完備性と合わせ、有限位置へ終端するinextendible curveが中間時刻で消えることはない。
従って負のt切断はこの過去領域のCauchy面で、単なる小さいGH chartの選択ではない。
未来向きはglobal null vector partial_tで固定できる。t<=0へ未来曲線が逆向きに横断できないため、過去にCTCを隠していない。

一方、任意のt>0に対し十分大きいrでは `f(r)<t`。一定t,r,zのpsi円はtimelike。
**形成開始のinfimumはt=0、位置は無限遠へ逃げ、t=0の有限点には閉null psi円がない。**
`t=f(r)` は個々のKilling円の符号変化であって、実際のchronology/Cauchy horizonと同定しない。
これがcompactな最初の円とOri型の単純検査を避けるために行った変更である。

### 3.1 命題: このaffine-timeクラスには必ず別のbad null returnがある

**仮定:** (5)の全M、gamma,ell>0、f in C-infinity(R)でinf f> -infinity。
通常のsmooth normally hyperbolic場のglobal bisolution Wと全点の局所Hadamard性を要求する。
**結論:** そのようなWは存在しない。positivityの選択より前の矛盾である。

証明は、null rayの存在を仮定せず構成する。
任意のr0を固定し、r(0)=r(ell)=r0のH1曲線について

\[
 I[r]=\frac12\int_0^\ell e^{\gamma s/2}\{(r')^2+f(r)\}\,ds
\tag{6}
\]

を最小化する。定数曲線との比較とfの下界から、最小化列のH1 normは有界。
固定端点とCauchy--Schwarzから像も有界で、1次元H1のC0へのcompact embeddingにより部分列が一様収束する。
f項はそのcompactな像上で収束し、kinetic項はweak lower semicontinuous。
従って最小値が達成される。Euler--Lagrange方程式とODE regularityからsmoothな解

\[
 r''+\frac\gamma2r'=\frac12f'(r),\qquad r(0)=r(\ell)=r_0
\tag{7}
\]

が得られる。このqualitative存在に、小さいf'やf''は不要。なお全体で|f'|が有界なら、
fに下界がなくても、線形の負成長をkinetic二次項が支配するので同じ直接法が成立する。
これはaffineな横profileも包含する拡張である。

次にnull条件から

\[
 t'+\frac\gamma2t=\frac12\{f(r)+(r')^2\},\qquad
 t_0={\int_0^\ell e^{\gamma s/2}[f(r)+(r')^2]ds\over2(e^{\gamma\ell/2}-1)}.
\tag{8}
\]

このt0を初期値とすればt(ell)=t(0)。zは一定にする。
Christoffelから `Gamma^psi_{psi psi}=-gamma/2`。
(7),(8)はnull条件と全測地線方程式を満たし、

\[
 {d\psi\over d\lambda}=e^{\gamma\psi/2},\qquad
 k_t=-{d\psi\over d\lambda},\qquad
 {k_t(\ell)\over k_t(0)}=e^{\gamma\ell/2}\ne1.
\tag{9}
\]

従って同じ点へ戻るnull geodesic segmentのaffine covectorが異なる。
前段の特異性伝播 [K,Q] は `(p,k_in;p,-k_in)` から `(p,k_out;p,-k_in)` を強制し、
局所Hadamard対角条件と矛盾する。片方だけのscale変更はWFの同時conicityでは吸収できない。

これはnoncompact horizonであることを理由にKRWをそのまま適用したのではない。
また、証人を切取り外へ出すGrant cutには適用できない。**全経路の包含が命題の仮定**である。
この命題は今回の変分構成による既知の微局所的方法の適用で、一般手法の新規性を主張しない。

### 3.2 logistic例の検証可能な証人

ell=gamma=1、r0=0。logistic fについて
`|f'|<=1/4`, `|f''|<=1/4`, `|f'''|<=1/8`。
Dirichlet演算子 `L=d^2/ds^2+(1/2)d/ds` のinverse normは最大値原理より1/6以下。
例えば `s(1-s)/(3/2)` がpositive barrierになる。
(7)はcontraction係数1/48の固定点問題で、唯一の解と `0<=r<=1/48` を得る。

最初のiterateは

\[
 r_1(s)={1-e^{-s/2}\over4(1-e^{-1/2})}-{s\over4}.
\]

`f'(r)+1/4=tanh^2(r/2)/4<=r^2/16` を用いると

\[
 |r-r_1|\le\delta_r={1\over442368},\qquad
 |r'-r_1'|\le\delta_v={5\over221184},\qquad |r_1'|<1/12.
\tag{10}
\]

微分のboundはr-r1にRolleの点を取り、first-order積分因子と `e^(1/2)<5/3` を用いる。
(8)でfを `1/2-r1/4`、r'をr1'に代えた値は

\[
 t_{app}=\frac7{16}+{e^{1/2}\over64(e^{1/2}-1)^2}.
\]

正の規格化weightによる平均なので

\[
 |t_0-t_{app}|\le\delta_r/4+{1\over5308416}
 +\delta_v(1/6+\delta_v)
 ={221209\over48922361856}.
\tag{11}
\]

有理Taylor級数と厳密tailから、外向きに丸めた表示で

\[
 0.4987095110074379<t_0<0.4987185542748360,
 \quad0\le r\le1/48,\quad 95/192\le t(s)\le313/576.
\tag{12}
\]

実際の証人は有限の時空boxに入る。数値shootingは `t0~0.498714068058` を返すが、
存在と(12)の保証はroot residualや有限sampleからの推測ではない。
独立verifierはHamilton方程式から導出し、`exp(1/4)`を別に有理包囲して二乗する。

## 4. 同じ幾何のsource、拘束、資源を監査する

まず(5)でgamma=1。4D tensorから

\[
 R_{\psi\psi}=-f''/2,\quad R=0,\quad G_{\mu\nu}=R_{\mu\nu},\quad\nabla G=0.
\tag{13}
\]

Lambda=0、有限curvature countertermを零とした**診断**なら必要なtensorは
`T_req=-f'' dpsi^2/(16 pi G)`。これは物質や量子状態の存在証明ではない。
logistic fではr>0でf''>0なので、通常のNEC物質のみでは支えられない。
量子stateのpositivityは点ごとのNECではないから、この符号だけで全量子sourceを禁止しない。

t<0、F=f-tで `N=sqrt(F)partial_t+partial_psi/sqrt(F)`。
`h=diag(F,1,1)`、`K=-Lie_N h/2` により

\[
 K_{ij}=\begin{pmatrix}\sqrt F/2&f'/(2\sqrt F)&0\\f'/(2\sqrt F)&0&0\\0&0&0\end{pmatrix},
\]
\[
 R^{(3)}+K^2-K_{ij}K^{ij}=-f''/F=16\pi G\rho_{req},
 \quad D_j(K^j{}_i-\delta^j_iK)=(f''/(2\sqrt F),0,0)=8\pi G j_i.
\tag{14}
\]

従って必要sourceと初期拘束は整合し、stressの局所保存も満たす。
しかし `T_req=G/(8pi G)` を物理的sourceの構成だとする逆定義は禁止したままである。

初期t=-1、ell=Lz=1では、幾何学的なabsolute matter-energy診断は有限:

\[
 \int_{\Sigma}|\rho_{req}|d\Sigma
 ={1\over16\pi G}\int_0^1{|1-2u|\over\sqrt{1+u}}du
 ={4\sqrt6-(14+10\sqrt2)/3\over16\pi G}.
\tag{15}
\]

signed値は `(14-10 sqrt2)/(48 pi G)<0`。densityに伴うnull fluxも同じabsolute integralで有限。
metricはsmooth・Lorentzで、全ての有限点で曲率tensorは有限。
**それでも§3の量子障害は残る。** finiteな幾何stressからHadamard性を推定できない。

実際のWがこのtensorを与えるか、全量子energyが有限か、装置の準備費用は未構成。
正のLambdaを持つESUの理論でflat asymptotic endを使うには、Lambda項と真空応力のmatchingも必要。
(15)をその費用まで含む答えにしない。asymptotic compact-circle Casimirの差引きも勝手に零にしない。
有限countertermやmassの選択は、§3のWの非存在を変えない。

## 5. 失敗箇所の修復を続ける

### 5.1 準備を有限時間へ: global switchの圧力を見落とさない

`F=f(r)-q(t)` とし、qを早期には負の定数、後にはtに滑らかに接続する。
例えばq=tとなる領域をt>=0に取れば、(12)の証人全体は変更されない。
この修復によりearly geometryをstationaryにできるが、未来のHadamard障害は残る。
さらに同じtensor計算は

\[
 R=-\ddot q,\quad G_{\psi\psi}=-f''/2,\quad
 G_{rr}=G_{zz}=\ddot q/2,
\tag{16}
\]

を与える。switch中の横圧力は両無限遠で一定、非零。
normal-frameのrhoだけを計算するとこの費用を落とす。
横方向へ任意の固定非零速度でboostした観測者のenergyには `Gamma_v^2 v^2 q''/(16 pi G)` が残り、
非compact endでそのabsolute積分は発散する。
従ってglobalな同時switchを、有限範囲・有限伝播の装置としては認定できない。
この事実を「有限energyから全てのno-goが従う」とは一般化しない。

### 5.2 switchを局在化する修復: 最初のcompactな円が戻る

smooth compact bump chi(r)を使い、

\[
 F(t,r)=f(r)+1-a(t)\chi(r),\quad0\le\chi\le1.
\tag{17}
\]

外は固定のchronal metric。a=0の過去から増加させる。
`a_* = min_{chi>0}(f+1)/chi` は有限位置r*で達成される。
最初の閾値で `F=F_r=0`。この点のpsi円はambientな閉null geodesicで、

\[
 \kappa=F_t/2=-\dot a\chi/2,\qquad
 \mathcal A=\exp(\dot a\chi\ell/2)>1 \quad(\dot a>0).
\tag{18}
\]

従って空間的な局在化をした修復は、最初の閉円でのHadamard障害を再導入する。
符号を打ち消すholonomy設計も、最初の単調な開きではF_tの符号が一定なので不可能。

a'を閾値だけ零にする場合、(18)だけで排除しない。
さらに駆動を有限時間pulseとしてgを初期のGH metricへ戻す修復は、次の明示的条件下でKRWにかかる。
**g=g0がcompactな時空集合Kの外で一致、g0の完全な外部にはuniformな因果速度boundとproperな空間座標があり、
初期SはKの過去のCauchy切断で、穴・未指定のincoming boundaryを持たない**、とする。
H+(S)のpast generatorがKに一度も入らなければ、g0の過去曲線としてSへ達し矛盾する。
Kへ達した後の外部excursionは、Kの最大外部時刻からSまでの有限slabにあり、速度boundにより共通の有限半径内にある。
従ってpast tailは共通compact集合へ閉じ込められ、compact generationが得られる [K,H]。
この**compact-deformation repair**は初期Hadamardを全点へ保てない。
有限総energyだけ、あるいはradiative tailを持つ任意の有限準備から、この強いsupport条件を自動的には導かない。

### 5.3 大きいwall mass、conformal response、反作用による修復

(4)の有限potentialはlocal conservationを修復できても、null principal symbolを変えない。
同じmetricを保持する有限のsmooth matrix potentialを持つ多成分normally-hyperbolic系でも同じ問題がある。
任意のstrongly interacting QFTをこの線形bisolution命題に含めない。

正のsmooth Omegaで `g_tilde=Omega^2 g` とした場合、null Hamiltonianは
`H_tilde=Omega^-2 H`。H=0上で `X_Htilde=Omega^-2 X_H`。
従ってcotangent orbitと帰還covectorは不変。conformal responseでLambdaやstressを調整しても、
この幾何のHadamard障害は消えない。

さらにlogistic証人はsmall **nonconformal** backreactionにも安定である。
初期t0とr'(0)を未知数とするreturn mapのradial variation Jは
`J''+J'/2=f''(r)J/2`, `J(0)=0,J'(0)=1`。
Volterra評価で `||J||<=16/15`, `|J(1)-2(1-e^-1/2)|<=1/15` なので

\[
 J(1)>17/24,\quad|\partial_{t0}(t(1)-t0)|>3/8,
 \quad |\det D\mathcal R|>17/64.
\tag{19}
\]

z方向も加えた3x3 mapでは追加factor `2(1-e^-1/2)>3/4`。
null条件はt'について非退化に解ける。ODE continuous dependenceとIFTにより、
証人のcompact近傍・同じidentificationを保つC2-small metric変形にも自己帰還が存在し、covector mismatchは残る。
**これはopen neighborhoodの解析的存在であり、許容C2半径の数値を算出したとは主張しない。**
強い非conformalな変化や経路の領域外への排除は再検査が必要。

### 5.4 boost echoだけを消す修復も十分でない

一般F(t,r,psi)の同じcross-term形式では

\[
 {d\log|p_t|\over d\psi}=-F_t/2,\qquad
 {dp_r\over d\lambda}=F_r p_t^2/2.
\tag{20}
\]

時間依存を往復させて最初の積分を零にしても、経路全体でF_r<0ならradial covector kickは厳密に負。
self-returnを維持したままfull cotangent returnを恒等にすることはできない。
時間側だけでなく横方向のlensも変える必要がある。
ただしF_tやF_rの符号を変えた全てのmetricに自己帰還が必ずある、とは(20)から言えない。
ESUのfull refocusingは重要な負例: returnを見つけただけ、holonomy=1だけではno-goにならない。

## 6. 同じ模型に対する同時監査

| 条件 | smooth drift-frontで実際に分かったこと |
|---|---|
| 因果的initial data | t<0の全領域はGH。negative sliceを明示。CTCはt<=0へ隠していない |
| 動的chronology violation | 任意のt>0にCTC円あり。time quotientを後付けしたのではない |
| 有限資源 | Lambda=0の幾何学的absolute stress診断(15)は有限。物理的準備・global quantum energy・有限装置は未認定 |
| positivity/CCR | GH過去のHadamard state存在枠組み [Q] は使える。ただし特定の有限総energy stateやSCEE初期解は未構成 |
| Hadamard extension | §3の証人により全M上の通常bisolutionは不可能。positivityを選び直しても救えない |
| RSET | 初期GHで適切な状態なら局所定義可能。要求されたglobal Hadamard RSETは供給できない。全成分の発散とは主張しない |
| SCEE/backreaction | 診断Gをsourceと逆定義せず、不成立を明示。conformal変更とC2-small変更は上記障害を修復しない |
| 局所保存 | geometryのBianchi、(4)のexchangeは整合。物質/量子状態の存在と別 |
| QEI/ANEC | NEC符号違反は指摘するが、それだけで全量子stateを排除しない。任意の非共形場に同一QEIを当てない |
| boundary | ideal wallとsmooth potentialを分離。反射点の一般化Hadamard、Israel接合、壁energyを未計算のまま完成扱いしない |

どこか一つが破れた時点で同時仕様の成功認定はしないが、その理由を他の段階へ偽って移さない。
ここでの不成立はSCEEのroot finderの失敗ではなく、必要なWがないという構成上の矛盾である。

## 7. 元問題に残る自由度を狭く特定する

壁の有限厚化だけ、bounded-below transverse profileの平滑化だけ、boostだけのecho、conformal retuning、
小さいbackreaction、regularなcompact-support pulseは、この修正系列を完成しない。
回避には **証人を非摂動的に除去し、しかも切取りを物理的に完成する**変更が必要。
例えばF_tとF_rをともに変えるnonseparable return geometryを試す場合にも、
全cotangent帰還写像・近接非局所null接続・初期Wの伝播を先に検査し、その後で同じgのRSET/SCEEを閉じる必要がある。
その変更を「整合な仮説」の段階から存在認定へ格上げしていない。

未解決なのは特定の文献の欠落ではなく、非compactなincoming structureや未指定wallへ費用を押し出さずに、
上記のreturn障害を外れる局所力学と量子stateを同時に作ること。
本稿の命題はこのaffine-time classと明示したrepairに対するno-goであり、一般no-goや拡張理論での形成成功とは区別する。

## 出典と実装

- [K] Kay--Radzikowski--Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, CMP 183 (1997) 533--556, https://arxiv.org/abs/gr-qc/9603012 . 基礎的なWF/chronology障害。今回の変分front命題を原著の定理として引用しない。
- [Q] Khavkine--Moretti, *Algebraic QFT in Curved Spacetime and quasifree Hadamard states*, https://arxiv.org/abs/1412.5945 . GH上の状態・CCR・Hadamardの枠組み。
- [H] Hawking, *Chronology protection conjecture*, PRD 46 (1992) 603, https://doi.org/10.1103/PhysRevD.46.603 . 有限領域の形成とcompact generationの議論。有限energyだけの定理にしない。
- [B] Dappiaggi--Ferreira, *Hadamard states for a scalar field in anti-de Sitter spacetime with arbitrary boundary conditions*, PRD 94 (2016) 125016, https://arxiv.org/abs/1610.01049 . 反射による特異性とboundary条件の区別。今回のmoving wallにそのまま適用した存在定理ではない。
- 新しい2026年の一般Robin-boundary preprint (arXiv:2609.24465)はabstractを確認したが全文取得に失敗したため、本稿の証明の入力に使わない。
- [計算](../src/symbolic/chronology_dynamic_front.py) / [独立検証](../src/symbolic/chronology_dynamic_front_verify.py)。原著の全proof、ESUのnoise/stability、連続体QFTのLean化を今回実施したとはしない。
