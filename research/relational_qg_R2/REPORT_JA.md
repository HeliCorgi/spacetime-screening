# 関係量子模型 R2：保存する動力学と、実験手順まで含めた予測

基点：R1 commit `4c600df0b331a19f9d21384bf58472bee01a5a16`。

**位置づけ：R1 の空間分解能カーネルを変えず、弱重力・非相対論的な物質運動、保存源、線形 TT 真空の応答を接続した研究版。完全な非線形量子重力ではない。**

## 0. 今回の自己修正

R1 の計算スクリプト3本を受領アーカイブから再実行した。既存の位相零点と束縛状態計算は再現した。その上で以下を追加した。

| R1 の隙間 | R2 の対処 | 限界 |
|---|---|---|
| 指定された静的源だけだった | 同じポテンシャルの多体 Hamiltonian と力の応力を構成 | 保持次数は Newtonian。完全な相対論的源ではない |
| 自由な位相に装置の反作用がなかった | 装置質量の変位も含めた分岐エネルギーを計算 | 分岐の準備・保持の全物質作用は未構成 |
| 確率の位相だけで真空雑音がなかった | 保存された四重極パルスと TT 場の放射・dephasing を同じ結合から計算 | R1 の保持実験全体と同じプロトコルではない |
| 放射は源を固定して比較しただけだった | 修正 Kepler 則、軌道エネルギー、先頭四重極流束をエネルギー収支で接続 | 非線形 1PN 補正・完全波形は未計算 |
| 空間平均化の因果的代償が定性的だった | 遅延 Green 関数と一様 boost の異方性を計算 | 厳密な短距離 microcausality は依然不成立 |

新しい基本パラメータは増やしていない。装置の質量・位置、パルス時間、波束幅、相対速度は実験の入力であり、新しい重力定数ではない。ただし、相互作用応力を含む保存源を先頭四重極放射に使うことは**保持次数を指定した有効理論の closure**であって、R1 の非線形完成を導いたという意味ではない。

本記録で新規に計算したものを NEW CALCULATION CANDIDATE、先行の概念・比較を文献節で区別する。独創性・優先権は主張しない。

## 1. 変更しない核と作用の範囲

R1 の同じ二つの頂点を使う：

$$
F_\ell(\mathbf k)=e^{-\ell^2\mathbf k^2/2},\qquad
K_\ell(r)=\frac{\operatorname{erf}(r/2\ell)}r.
$$

源にもプローブにも F が一回ずつ作用するので、交換応答には F² が現れる。重力場自体は線形 Fierz–Pauli の二偏極。有限な観測カーネルを、基礎場の CCR/Hadamard 特異構造を消した状態と取り違えない。

物質の静的近似を、次の動く多体模型へ拡張する：

$$
H_N=\sum_a\frac{\mathbf p_a^2}{2m_a}
-G\sum_{a<b}m_am_bK_\ell(|\mathbf x_a-\mathbf x_b|).
$$

有限 N・正の質量・固定された ell に対する模型である。自由 TT 場との相互作用は R1 の線形結合を使い、以下では保存された外部源、または先頭 Newtonian/quadrupole matching として扱う。相互作用を任意の運動量まで外挿した Hamiltonian 全体の下限を証明したとはしない。

## 2. 有限粒子系での「発散しない」を動力学へ格上げ

積分表示

$$
K_\ell(r)=\frac1{\sqrt\pi\ell}\int_0^1
 e^{-u^2r^2/(4\ell^2)}du
$$

から、中心を含めて K は滑らかであり、

$$
\|\partial_i\partial_jK_\ell\|_{\rm op}
\le\frac{1/2+1/e}{3\sqrt\pi\ell^3}
$$

という一様上界が得られる。導出では外積項に z exp(-z) <= 1/e を使う。

有限 N の力は全配置空間で globally Lipschitz。従って有限な初期位置・速度からの Newtonian 軌道は一意に全時間へ継続し、二粒子の一致位置は ODE の特異点ではない。

量子力学では、相互作用が実で有界な乗算演算子なので、自由な自己共役運動エネルギーに対する有界摂動である。さらに

$$
H_N\ge-\frac G{\sqrt\pi\ell}\sum_{a<b}m_am_b.
$$

この下界は N に関しておおむね N²。熱力学的安定性や N→∞ の制御まで意味しない。

直接の velocity-Verlet 計算では、保存的な二体軌道20000ステップを確認した。別の正面衝突制御では10000ステップ内に相対座標が10回ゼロを通過し、最大エネルギー誤差は約2.7e-8。新しい bounce 規則は追加していない。これは数値制御であり、上の継続定理の代用ではない。

**これは非相対論的な模型の粒子衝突の正則性である。曲率の有界性、測地線完全性、ブラックホールの解消を証明したものではない。**

## 3. 保存則：力を入れたら、その応力も入れる

粒子の運動量流だけでは、粒子が加速する場合に保存しない。対 a,b の力を F_ab、r_ab=x_a-x_b とし、

$$
\tau_{ij}(\mathbf x)=\sum_{a<b}F_{ab,i}r_{ab,j}
\int_0^1d\lambda\,\delta^3(\mathbf x-\mathbf x_b-\lambda\mathbf r_{ab})
$$

を加える。中心力なので tau は対称であり、分布の意味で

$$
\partial_j\tau_{ij}=-\sum_aF_{a,i}\delta^3(\mathbf x-\mathbf x_a).
$$

従って運動項と合わせて Newtonian の局所運動量保存を満たす。系全体のエネルギーと角運動量は同じ H_N の時間・回転対称性から保存される。これを完全な relativistic T_munu の構成と同一視しない。

特に質量二次モーメント I_ij=sum m x_i x_j に対し、

$$
\frac12\ddot I_{ij}=
\int d^3x\,[T^{\rm kinetic}_{ij}+\tau_{ij}]
$$

が成立する。加速する裸の質点だけを放射源にするのではなく、この保存源の四重極を使う。

### 時間依存の量子分岐には、exact な線形保存源も用意する

対称な定数 Q_ij と任意の滑らかな f(t,x) に対し、

$$
\Delta T^{00}=Q_{ij}\partial_i\partial_j f,\qquad
\Delta T^{0i}=-Q_{ij}\partial_t\partial_j f,\qquad
\Delta T^{ij}=Q_{ij}\partial_t^2 f
$$

とすれば、両側の微分交換だけで

$$\partial_\mu\Delta T^{\mu\nu}=0$$

が exact に成立する。forward は Fourier 多項式、verifier は実空間微分で別々に確認した。

これは二つの分岐の差であり、単独の正エネルギー物質ではない。共通背景への埋込みと物質作用の実現可能性は別に必要。密度だけへ時間窓を掛ける処方は、current/stress を欠くため負例として棄却した。

## 4. 遅延応答と雑音を同じ場から出す

以下 c=1。二頂点の scalar radial retarded factor は

$$
D_\ell^{\rm ret}(t,r)=
\frac{\theta(t)}{8\pi^{3/2}\ell r}
\left[e^{-(r-t)^2/(4\ell^2)}-e^{-(r+t)^2/(4\ell^2)}\right].
$$

r=0 は連続極限を使う。これは Fourier 積分と、通常の光円錐 Green 関数を空間 Gaussian で畳み込む計算が一致した。

$$
4\pi\int_0^\infty D_\ell^{\rm ret}(t,r)dt=K_\ell(r).
$$

従って静的核と時間応答は独立に選んでいない。ただし、0<t<r にも非零の裾がある。**過去時間へ応答しないことと、metric light cone の外で応答が厳密にゼロであることは異なる。** R2 は後者を満たしたと記録しない。

canonical TT 真空の各モードについて、同じ結合の対称 covariance は

$$
C_\lambda(\mathbf k,t)=
\frac{\hbar e^{-\ell^2k^2}}{2k}\cos(kt),
$$

遅延関数は theta(t) exp(-ell²k²) sin(kt)/k。雑音だけを任意に除くことはできない。

### 保存された有限パルスの dephasing

Q を symmetric trace-free とし、f=exp[-t²/(2tau²)] w_sigma(x)、w_sigma を単位積分の Gaussian とする。分岐の質量四重極差は

$$\Delta I_{ij}(t)=2Q_{ij}e^{-t^2/(2\tau^2)}.$$

場の二つの最終状態は coherent states となり、その重なりは

$$
|\langle\mathrm{env}_1|\mathrm{env}_0\rangle|=e^{-\Gamma},\qquad
\Gamma=\frac{4GQ_{ij}Q_{ij}\tau^2}
{5\hbar(\ell^2+\sigma^2+\tau^2)^3}.
$$

ここでも c=1、tau は長さの単位である。SI では tau→c tau、GQ²/hbar→GQ_mass²/(hbar c) とする。

計算には Frobenius 正規化の TT polarization sum を使った。角度積分は integral dOmega Q Lambda Q=(8pi/5)QijQij。verifier は独立に graviton number N=int dE/(hbar omega) と Gamma=N/2 から一致を確認した。coherent-state overlap の Gram matrix が正であるため、この prescribed-history の dephasing は CP map になる。

例：GQ²/(hbar ell⁴)=0.01、sigma/ell=0.2。

| tau/ell | Gamma | visibility |
|---:|---:|---:|
|1|0.0009423223|0.9990581215|
|2|0.0002499530|0.9997500782|
|4|0.0000258703|0.9999741301|
|8|0.0000018609|0.9999981391|

これは R1 の保持実験そのものではなく、保存された source pulse の制御例。ノイズを無視できると主張するためには実際の軌道・装置源をこの計算へ入れる必要がある。極短パルスに外挿する際も、源の応力と弱重力条件を確認する。

## 5. 修正 Kepler 則、軌道安定性、量子スペクトルの一致

M=mA+mB、mu=mA mB/M、x=r/ell と定義する。

$$
J(x)=\operatorname{erf}(x/2)-\frac{x}{\sqrt\pi}e^{-x^2/4},
\qquad J'(x)=\frac{x^2}{2\sqrt\pi}e^{-x^2/4}>0.
$$

円軌道は

$$
\Omega^2(r)=\frac{GM}{r^3}J(r/\ell).
$$

静的応答から独立に角周波数を当てはめていない。中心では

$$
\boxed{\Omega_0^2=\frac{GM}{6\sqrt\pi\ell^3}},\qquad
\Omega=\Omega_0\left(1-\frac{3r^2}{40\ell^2}+O(r^4/\ell^4)\right).
$$

J/x³=(1/(2sqrt(pi))) integral_0^1 u² exp(-x²u²/4)du なので 0<Omega<=Omega0 が全 r>0 で成立する。

円軌道の radial epicycle は

$$
\omega_r^2=GM\left[\frac{J}{r^3}+\frac{dJ/dr}{r^2}\right]>0.
$$

従って保持した Newtonian 模型では全円軌道が半径摂動に対して安定。

| r/ell | Omega/Omega0 | omega_r/Omega |
|---:|---:|---:|
|0.1|0.9992503883|1.9992500737|
|0.5|0.9814905307|1.9812968429|
|1|0.9287450557|1.9257883290|
|2|0.7539343721|1.7151092252|
|4|0.3981480832|1.1604397268|

量子二体 Hamiltonian の中心展開は

$$
H_{\rm rel}\simeq \frac{p^2}{2\mu}
-\frac{G\mu M}{\sqrt\pi\ell}
+\frac12\mu\Omega_0^2r^2+O(r^4).
$$

**古典円軌道の周波数上限と、量子束縛状態の中心の oscillator frequency は同じ Omega0。** 別の一致条件を追加したのではない。quartic 補正も R1 の -9/64 を再現した。

## 6. 放射で落ちる軌道を、同じエネルギーで追う

共通重心が選んだ foliation に静止し、epsilon=GM/(c²ell)<<1、v/c<<1 とする。R1 の線形放射結合へ前節の conserving quadrupole matching を適用すると、

$$
P_{\rm quad}=\frac{32G\mu^2r^4\Omega^6}{5c^5}
 e^{-4\ell^2\Omega^2/c^2}.
$$

円軌道のエネルギーは

$$
E_c=-G\mu M K_\ell(r)+\frac{G\mu M}{2r}J(r/\ell),
$$

$$
\frac{dE_c}{dr}=\frac{G\mu M}{2}
\left[\frac J{r^2}+\frac{dJ/dr}r\right]>0.
$$

よって adiabatic balance は

$$\boxed{\dot r=-P_{\rm quad}/E_c'(r)}.$$

中心近傍では

$$
\dot r=-\frac{16G\mu\Omega_0^4}{5c^5}
 e^{-4\ell^2\Omega_0^2/c^2}r^3+O(r^5).
$$

点粒子・古典・adiabatic 模型を形式的に最後まで継続すると、r~t^(-1/2)、Omega0-Omega~t^(-1)、P~t^(-2)。有限時間で r=0 には達しない。位相は無限回回り得るが、周波数は無限大にならない。

**物理的な連星の実際の終点と断定しない。** 有限サイズが重なるか、作用角 L~hbar になるとこの古典軌道近似を止める。量子クロスオーバーの目安は

$$
\frac{r_Q}{\ell}\sim\left(\frac{6\sqrt\pi}{g}\right)^{1/4},\qquad
g=\frac{\mu^2GM\ell}{\hbar^2}.
$$

その先に先ほどの量子 oscillator が現れるのが、この模型内部での整合した記述の切替えである。

### R1 の「高周波放射が弱まる」への制限

この弱重力の自己束縛系では

$$
\frac{P_{\rm quad}}{P_{\rm quad,no\ form\ factor}}
\ge \exp\left[-\frac{2\epsilon}{3\sqrt\pi}\right].
$$

epsilon=0.01 なら form factor だけによる低下は最大約0.37542%。大きな指数抑制を、この弱重力自己束縛系から自由に引き出せるわけではない。

この相対補正は O(epsilon) なので、計算していない nonlinear/post-Newtonian 補正と同程度になり得る。**これを完全な1PN精度の数値予言として報告しない。** 先頭次数の flux とモデル内部の form-factor effect を分けて記録する。

## 7. 0.654976… は、装置を無視した条件付きの零点

R1 の二つの狭い点プローブでは d0/ell=0.654976082566… を再現した。

しかし branch b=0,1 ごとに質量 m のプローブと質量 eta*m の反作用体を置き、

$$
A_b:\quad (x_m,x_{\rm rec})=(bd,-s-bd/\eta),
$$

$$
B_b:\quad (x_m,x_{\rm rec})=((3+b)d,3d+s-bd/\eta)
$$

とすると、各装置の全質量と重心は branch 間で同じである。全ての装置間の組の同じ K を加えると、位相零点は変わる。

| s/ell | eta | d*/ell |
|---:|---:|---:|
|装置なし|—|0.654976082566|
|5|100|0.734316617303|
|10|100|0.670678329218|
|100|100|0.655001506214|

装置を重くするとその変位は小さくなるが、質量×変位は残り得る。重いことだけを理由に gravitational phase を捨てない。装置を十分遠ざけると、この例は点プローブ値へ戻る。

全配置の長さが ell より小さく、各装置の branch 差の全質量・dipole moment がゼロなら、K の r² 項は cross phase に寄与しない。次の項は

$$
\Delta\mathcal K=
\frac{3}{80\sqrt\pi\ell^5}
\Delta M_{2,A}\Delta M_{2,B}+\cdots
$$

となる（一直線の場合）。これは全実験に対する普遍的な零点の主張を否定する具体例であり、R1 の指定された条件下の数学的な根を誤りとするものではない。

## 8. preferred frame の代償を測れる式へする

R1 の F は空間スライス依存。preferred frame に対し速度 beta*c で動く系の静止座標では、

$$
\widetilde K_\beta(\mathbf q)=
\frac{4\pi e^{-\ell^2(q_\perp^2+\gamma^2q_\parallel^2)}}{\mathbf q^2},
\qquad \gamma=(1-\beta^2)^{-1/2}.
$$

従って

$$
K_\beta=K+\ell^2\beta^2\partial_z^2K+O(\beta^4).
$$

遠方にも、等方系にはなかった quadrupolar tail が現れる：

$$
K_\beta\simeq\frac1r+
\frac{\ell^2\beta^2}{r^3}(3\cos^2\theta-1).
$$

点プローブだけの位相零点も

$$
\frac{d_*}{\ell}=d_0+
\beta^2[0.02592657483+0.24970831680\cos^2\theta]+O(\beta^4).
$$

これは full Schwinger 積分の数値根と比較した。自己無撞着な宇宙の preferred frame をここで選んだのではない。どの frame が物理的かは模型の追加構造として残る。

## 9. まだ成功にしないこと

完全非線形・一般共変な作用、constraint algebra、追加モードの安定性、真空エネルギーの決定、量子ループによる係数の安定性、強い場の崩壊、物質装置の microscopic completion は残る。

保存された線形源を作れたことは、dynamical gravity の全 Ward identity を閉じたことではない。F を partial から covariant derivative へ単純に書き換えるだけでは、metric variation と operator variation の項を失う。

F(0)=1 なので一様な真空エネルギーは消えない。空間的な非局所性も、計算によってなくなったのではなく定量化された。

R2 が達成したのは、**限界を隠した万能理論ではなく、同じ結合から力・運動・量子スペクトル・保存された放射・真空雑音・装置依存性を追える弱重力モデル**である。

## 再現・検証

リポジトリの既存依存 sympy と mpmath のみ。新しい Python dependency や workflow の変更はない。

```bash
python src/symbolic/relational_qg_r2_dynamics.py --output /tmp/r2.json
python src/symbolic/relational_qg_r2_verify.py --evidence /tmp/r2.json --output /tmp/r2-verify.json
```

forward は50桁、verifier は60桁の計算を使う。数学的な再現桁数と物理的精度は別。CI では output/evidence 引数なしでも両方が独立に実行され、shard 間の生成ファイル共有は不要。

保存された [results.json](results.json) と [verification.json](verification.json) は今回の実行出力。verifier は forward を import せず、位相は signed density と二分法、retarded function は光円錐畳込み、noise は graviton number、軌道は有効ポテンシャルの二階微分、boost は exact Schwinger 積分から検算した。

## 先行研究との関係

- S. Deser, *Self-Interaction and Gauge Invariance*, https://arxiv.org/abs/gr-qc/0411023 ：線形 spin-2 の保存源と非線形 self-coupling の区別。R2 の非線形完成を代わりに証明する文献ではない。
- A. Belenchia et al., *Quantum Superposition of Massive Objects and the Quantization of Gravity*, https://arxiv.org/abs/1807.07015 ：重心保存と重力四重極・放射を無視できない点の比較。R2 の装置配置の数値零点は今回の計算。
- B. L. Hu and E. Verdaguer, *Stochastic Gravity: Theory and Applications*, https://arxiv.org/abs/0802.0658 ：期待値だけと noise を含めた理論の違い。ここでの coherent graviton overlap は特定の線形 source model の計算。
- C. M. Will, *The Confrontation between General Relativity and Experiment*, https://arxiv.org/abs/1403.7377 ：偏極、preferred-frame effects、放射・post-Newtonian 精度を分けて扱う比較。

文献の結論を新しいカーネルへ無条件に移植していない。本記録の導出・assert の成立域に限定する。
