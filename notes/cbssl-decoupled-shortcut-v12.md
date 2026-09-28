# CBSSL v12：causal shortcut と topological identification を分離する

**2026-09-28。基点：PR #30 head 669b263e832d2f1d040706a13119470677caead4。**

v11 では simple helical quotient の同じ \((L,\Delta)\) に quantum state が見る topological image separation と過去向き causal return を両方背負わせたため、\(\Delta<L\) と \(\Delta>L\) が直接衝突した。

v12 はこの二つを別の幾何パラメータに分ける。

## 結論

今回の respec は **A=0 / B=1 / C=0** まで戻る。

**v11 の代数的 no-overlap は外れた。**

明示的 witness として

\[
A_{\rm topo}=4r,\qquad
d_{\rm ext}=r,\qquad
\tau_{\rm shortcut}=\frac r4,\qquad
\Delta_{\rm clock}=2r
\]

を取ると

\[
\tau_{\rm shortcut}+d_{\rm ext}
=\frac54r
<
2r
=
\Delta_{\rm clock}
<
4r
=
A_{\rm topo}.
\]

従って

\[
\Delta t_{\rm loop}
=
\tau_{\rm shortcut}+d_{\rm ext}-\Delta_{\rm clock}
=
-\frac34r,
\]

すなわち classical past advance は

\[
\boxed{D_t^{\rm advance}=\frac34r>0}
\]

になる一方、quantum support state の image sum は **純空間の** \(x\sim x+A_{\rm topo}\) だけを見る。

つまり v11 の Hadamard topology と past advance の同一変数衝突は消える。

ただし、これで A にはならない。安全な \(S^1\) sector の global RSET と backreaction は閉じられたが、**別に導入した causal handle 自体の global support-field two-point function / RSET はまだ未構成**だからである。

---

## 1. geometry を分離する

safe quantum-topology sector は

\[
\mathcal M_{\rm safe}
=
\mathbb R_t\times S^1_x(A_{\rm topo})\times S^2(r)
\]

とする。

local metric は v10 と同じ

\[
ds^2=-dt^2+dx^2+r^2d\Omega_2^2,\qquad x\sim x+A_{\rm topo}.
\]

重要なのは、ここには time shift が無いこと。deck vector は純空間なので

\[
k^2=A_{\rm topo}^2>0.
\]

この spatial compactification は cylinder-type Hadamard state を持てる。

これと独立に causal shortcut を二 worldtube 間の traversable handle として入れる。

- exterior shortest mouth separation: \(d_{\rm ext}\)
- handle traversal time: \(\tau_{\rm shortcut}\)
- mouth clock offset: \(\Delta_{\rm clock}\)

とすると、一周の coordinate time は

\[
\Delta t_{\rm loop}
=
\tau_{\rm shortcut}+d_{\rm ext}-\Delta_{\rm clock}.
\]

従って classical CTC 条件は

\[
\boxed{\Delta_{\rm clock}>d_{\rm ext}+\tau_{\rm shortcut}}.
\]

これは \(A_{\rm topo}\) と独立。

Morris–Thorne–Yurtsever 型の traversable-wormhole time-shift mechanism に対応する。ただし今回は formation dynamics を作らず、**eternal prescribed handle/time shift** として置く。

---

## 2. safe \(S^1\) 上の actual mode sum

support scalar のうち、まず massless conformal scalar を

\[
\mathbb R_t\times S^1_A\times S^2_r
\]

上で mode 分解する。

sphere harmonic \(\ell\) は 1+1 dimensional field として

\[
M_\ell^2=\frac{\ell(\ell+1)+1/3}{r^2}
\]

を持つ。

periodic \(S^1\) の topological energy は各 \(\ell\) について

\[
E_\ell^{\rm topo}
=
-\frac{(2\ell+1)M_\ell}{\pi}
\sum_{p=1}^\infty
\frac{K_1(p A M_\ell)}{p}.
\]

\(A=\alpha r\)、\(\alpha=4\) を固定する。

energy derivative から \(\rho_{\rm topo},p_x^{\rm topo},p_\Omega^{\rm topo}\) を計算する。

mixed components を

\[
T^t{}_t=\frac{c_t}{r^4},\qquad
T^x{}_x=\frac{c_x}{r^4},\qquad
T^\theta{}_\theta=T^\phi{}_\phi=\frac{c_\Omega}{r^4}
\]

とすると、収束した mode sum は

~~~text
c_t
= +0.0003911532498709034640995872238806...

c_x
= -0.0013135652650630378856936929316968...

c_theta
= +0.0004612060075960672107970528539081...
~~~

を与える。

conformal state-dependent correction なので

\[
c_t+c_x+2c_\Omega=0
\]

を数値的に検証する。

mode truncation は

~~~text
low : lmax=20, pmax=12
high: lmax=24, pmax=15
~~~

で比較し、最大相対差は \(10^{-9}\) 未満。

### massive nonconformal field

v10 の massive scalar は

\[
m^2=1000,\qquad \xi=-10000.
\]

新 root 近傍で最低 angular mode でも

~~~text
m_eff,l=0^2
= 998.0584245627...

A m_eff,l=0
= 12825.5452431...
~~~

なので shortest image の \(K_1(A m_{\rm eff})\) 自体が

~~~text
log10 K1 ≈ -5572.02
~~~

まで落ちる。

従ってこの compactification scale では massive topology term は \(O(e^{-A m_{\rm eff}})\) として、retained model precision より圧倒的に小さい。

**0 と偽装はしない。** 指数抑制として記録する。

---

## 3. そのままだと v10 core は閉じない

safe compactification を入れれば全部解決、ではない。

v10 の product core は

\[
G^t{}_t=G^x{}_x=-\frac1{r^2}.
\]

Popov local term と electrostatic term も \(T^t{}_t=T^x{}_x\) だった。

しかし \(S^1\) Casimir は

\[
T^t{}_t\neq T^x{}_x.
\]

従って compactification を入れただけでは

\[
E_t-E_x
=
-8\pi\frac{c_t-c_x}{r^4}\neq0.
\]

v10 root 付近では

~~~text
E_t - E_x ≈ -4.04e-10
~~~

となる。

数値として小さくても、**exact semiclassical closure では失敗**。これを success に丸めない。

---

## 4. minimal anisotropy compensator：axion winding

追加自由度を一個だけ入れる。

dimensionless periodic axion \(\vartheta\) を

\[
\vartheta(x+A)=\vartheta(x)+2\pi
\]

の winding-number-one sector に置く。

action を

\[
S_\vartheta
=
-\frac{f^2}{2}
\int\sqrt{-g}(\nabla\vartheta)^2
\]

とすると

\[
\partial_x\vartheta=\frac{2\pi}{A}.
\]

energy density を

\[
W
=
\frac{f^2}{2}\left(\frac{2\pi}{A}\right)^2
=
\frac{2\pi^2f^2}{A^2}
\]

と書けば

\[
T^\mu{}_{\nu,\rm wind}
=
\operatorname{diag}(-W,+W,-W,-W).
\]

これは Casimir の \(t/x\) anisotropy と逆向き。

Einstein equations を \((r,Q^2,f^2)\) の3変数で直接解く。

---

## 5. safe-sector semiclassical solve

方程式は

\[
G^\mu{}_\nu
=
8\pi
\left[
T^\mu{}_{\nu,\rm Popov}
+
T^\mu{}_{\nu,\rm EM}
+
\Delta T^\mu{}_{\nu,S^1}
+
T^\mu{}_{\nu,\rm wind}
\right].
\]

高精度 numerical root：

~~~text
r
= 101.4934144364441593877640584688312542952... l_P

Q^2
= 20601.81047060214773724409726794828203489...

A_topo
= 405.973657745776637551056233875... l_P

f^2
= 6.7071373107626554796016376825883302237e-8 l_P^-2

f
= 2.5898141459885988273541362639252935e-4 l_P^-1
~~~

winding energy density は

~~~text
W
= 8.0328790762338049617388474353e-12 l_P^-4
~~~

で

\[
2W=\frac{c_t-c_x}{r^4}
\]

を満たす。

3変数 Jacobian は

~~~text
det d(E_t,E_x,E_theta)/d(r,Q^2,f^2)
≈ 2.17069298494404e-16
~~~

で nonzero。

従って safe \(S^1\) topology sector については、v10 core を nearby \((r,Q^2,f^2)\) へ retune して self-consistent closure を復元できる。

---

## 6. causal shortcut witness

new safe-sector root の \(r\) を使って

\[
A_{\rm topo}=4r
\]

に固定する。

別 handle は

\[
d_{\rm ext}=r,\qquad
\tau_{\rm shortcut}=\frac r4,\qquad
\Delta_{\rm clock}=2r.
\]

したがって \(d_{\rm ext}<A_{\rm topo}/2\) で、指定した exterior path が shortest。

さらに

\[
\tau_{\rm shortcut}+d_{\rm ext}
=
1.25r
<
2r
=
\Delta_{\rm clock}
<
4r
=
A_{\rm topo}.
\]

数値では

~~~text
A_topo       ≈ 405.9736577458 l_P
d_ext        ≈ 101.4934144364 l_P
tau_shortcut ≈ 25.3733536091 l_P
Delta_clock  ≈ 202.9868288729 l_P
past advance ≈ 76.1200608273 l_P
~~~

となる。

従って

~~~text
safe spatial topology = yes
classical past advance = yes
same deck vector       = no
~~~

という parameter region を明示できた。

---

## 7. それでも global quantum state はまだ未完成

今回計算した

\[
\Delta G^+_{S^1},
\qquad
\Delta T_{\mu\nu,S^1}
\]

は **safe spatial circle** の topological term。

一方、causal handle 自体は別の global topology / boundary relation を導入する。

full state は模式的には

\[
G^+_{\rm full}
=
G^+_{\rm local}
+
\Delta G^+_{S^1}
+
\Delta G^+_{\rm handle}.
\]

今回できたのは \(\Delta G^+_{S^1}\) まで。

\[
\Delta G^+_{\rm handle}
\]

と、それに由来する

\[
\Delta T_{\mu\nu,\rm handle}
\]

は未計算。

**safe compactification の有限 RSET を、handle の missing RSET の代用にはしない。**

---

## 8. chronology horizon をどう扱ったか

今回の handle/time shift は **eternal prescribed** とした。

従って「globally hyperbolic initial region から clock shift を成長させ、chronology horizon を形成する過程」は解いていない。

これは v11 の null-image divergence をすり抜けた証明ではない。仮定を変更した。

もし

- ordinary globally hyperbolic initial state
- dynamical handle/time-shift formation
- compactly generated Cauchy horizon

を要求するなら、Kay–Radzikowski–Wald の base-point obstruction を再検査する必要がある。

つまり v12 が買ったものは **same-parameter algebraic contradiction removal** であって chronology protection の解決ではない。

---

## 9. communication gate

v10 の zero-local-stress Z2 signal receiver law は conditional control として置ける。

\[
P(Y=+1|do(0))
=
0.99865010196836990547\ldots
\]

\[
P(Y=+1|do(1))
=
0.00134989803163009453\ldots
\]

\[
D_{\rm past}
=
0.99730020393673981095\ldots
\]

かつ classical shortcut witness は \(D_t^{\rm advance}>0\)。

ただし full handle state が無いので

~~~text
globally_certified = false
~~~

のまま。

| gate | v12 |
|---|---|
| safe spatial Hadamard topology | PASS |
| safe \(S^1\) topological RSET | PASS |
| Casimir convergence | PASS |
| constant-core anisotropy without compensator | FAIL |
| with axion winding | PASS |
| safe-sector semiclassical backreaction | PASS |
| independent classical past-advance region | PASS |
| causal handle global support-field state | **missing** |
| causal handle RSET | **missing** |
| finite manufactured handle | **missing** |
| stability | **unproved** |
| protocol A | **no** |
| classification | **B** |

---

## 10. 今回追加で犠牲になった物理

v11 の cost に加えて二つ増える。

### 10.1 extra winding matter

Casimir anisotropy を吸収するため periodic axion sector を追加した。これは Popov+EM だけで自然に出たものではない。

### 10.2 eternal time-shift handle

chronology horizon formation の直接問題を避けるため、clock offset を最初から持つ handle を入力した。

そのため ordinary Cauchy data からの formation、clock-offset generation cost、chronology-horizon crossing を解いていない。

この二つは A 判定では独立に精算が必要。

---

## 11. 再現

~~~bash
python src/symbolic/cbssl_decoupled_shortcut_v12.py \
  --output /tmp/cbssl-v12.json

python src/symbolic/cbssl_decoupled_shortcut_verify_v12.py \
  --evidence /tmp/cbssl-v12.json \
  --output /tmp/cbssl-v12-verify.json
~~~

forward は \(S^1\times S^2\) conformal scalar mode sum、truncation convergence、massive-field exponential suppression、Popov local RSET、EM stress、axion winding、3-variable semiclassical root、3x3 Jacobian、shortcut inequality witness、conditional receiver を計算。

verifier は forward を import せず、短い独立 mode sum、winding anisotropy elimination、\(y=r^2,Q^2\) の alternative root、shortcut inequality、receiver lawを再計算する。

---

## 12. 文献・比較対象

- M. S. Morris, K. S. Thorne, U. Yurtsever, *Wormholes, Time Machines, and the Weak Energy Condition*, Phys. Rev. Lett. 61, 1446 (1988). Traversable wormhole の mouth clock offset を time-machine mechanism へ使う基本参照。
- B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, Commun. Math. Phys. 183 (1997), arXiv:gr-qc/9603012. Dynamically formed compactly generated chronology horizon へ戻る場合の QFT obstruction。
- D. N. Page, *Stress Tensors for Instantaneous Vacua in 1+1 Dimensions*, arXiv:gr-qc/9603005. Closed spatial curve の periodic massless Casimir control。
- M. A. Valuyan, *Casimir energy calculation for massive scalar field on spherical surfaces: an alternative approach*, arXiv:1810.05895. Periodic massive scalar on compact topologies の Casimir comparison。
- A. A. Popov, *Semiclassical long throats of the wormholes*, arXiv:1809.06202. v10/v12 local support RSET。

**scope:** v12 は「causal shortcut と quantum topological identification の長さを分ければ、v11 の直接矛盾を外せるか」を検査した。答えは yes。ただし full chronology-handle quantum state は別問題として残り、今回は B まで。
