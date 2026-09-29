# CBSSL v11：Global RSET / Helical Chronology Quotient

**2026-09-28。基点 3e64a86e8f65b8a1dc3ec5e71159a9b9f3332551（CBSSL v10 / PR #29 merge後）。**

目的は v10 の local \(M_2\times S^2\) semiclassical closure を、helical chronology quotient 上の **global quantum state / topological RSET** まで延長し、同じ state を入れた backreaction と通信判定を再検査すること。

## 結論

今回検査した **「v10 の単純 helical quotient を標準 Hadamard image state で global completion する案」**は **A=0 / B=0 / C=1**。

理由は

\[
\text{Hadamard image state:}\qquad L^2-\Delta^2>0\iff \Delta<L,
\]

一方、v10 の one-null return が未来の sender より過去へ進むには

\[
\Delta t_{\rm past}=\Delta-L>0\iff \Delta>L.
\]

したがって **両条件に重なりがない**。境界 \(\Delta=L\) では image separation が null になり、二点関数と point-split RSET が発散する。発散は正則化して成功扱いにせず、そのまま結果として記録する。

この C は CBSSL という新法則一般の禁止ではない。非標準の非Hadamard prescription、別の global topology、別の SA completion を一括して棄却するものでもない。今回の C の範囲は、標準的な local QFT/Hadamard 条件を保った image-state completion である。

---

## 1. flat helical quotient：image sum から既知 Casimir を再現

まず

\[
ds^2=-dt^2+dx^2+dy^2+dz^2,\qquad
(t,x,y,z)\sim(t-\Delta,x+L,y,z)
\]

を取り、deck vector と invariant length を

\[
k^\mu=(-\Delta,L,0,0),\qquad
a^2\equiv k^2=L^2-\Delta^2
\]

とする。

### 1.1 spacelike branch

\(a^2>0\) なら Lorentz boost で ordinary spatial cylinder \(\mathbb R^{1,2}\times S^1_a\) へ移せる。Minkowski vacuum の Wightman function から

\[
G_{\rm quot}^+(x,x')
=\sum_{n\in\mathbb Z}G_M^+(x,\gamma^n x'),
\]

\[
\Delta G_{\rm topo}^+(x,x')
=\sum_{n\neq0}G_M^+(x,\gamma^n x')
\]

を構成する。

coincidence では

\[
\Delta\langle\phi^2\rangle
=\sum_{n\neq0}\frac{1}{4\pi^2n^2a^2}
=\frac{1}{12a^2}.
\]

image term は \(n^{-2}\) で収束する。forward code は \(L=5,\Delta=3,a^2=16\) を control にし、N=8,32,128,512 の partial sum と integral-test tail bound を比較する。

### 1.2 point splitting と topological RSET

flat massless scalar の topological part は local Hadamard singularity を持たないので、非自明 image に point-splitting operator を直接掛ける。

各 image の微分を明示的に取り、和を取ると

\[
\boxed{
\Delta\langle T_{\mu\nu}\rangle_{\rm topo}
=
\frac{\pi^2}{90a^4}
\left(\eta_{\mu\nu}-4e_\mu e_\nu\right),
}
\]

ここで \(e^\mu=k^\mu/a\) は compact spacelike direction の unit vector。

compact direction に適応した orthonormal frame では

\[
\Delta\langle T_{\hat a\hat b}\rangle
=
\frac{\pi^2}{90a^4}
\operatorname{diag}(-1,-3,1,1),
\]

従って

\[
\rho_{\rm Cas}=-\frac{\pi^2}{90a^4}.
\]

これは periodic massless scalar の既知 Casimir tensor と一致する。RSET image term は \(n^{-4}\) で収束する。

また

\[
\nabla^\mu T_{\mu\nu}=0,\qquad
T_{\mu\nu}=T_{\nu\mu},\qquad
T^\mu{}_\mu=0
\]

を満たし、flat space なので local curvature trace anomaly も 0。さらに

\[
T_{\mu\nu}T^{\mu\nu}
=
12\left(\frac{\pi^2}{90a^4}\right)^2.
\]

forward と verifier は別々に image sum / tensor contraction を実装する。

---

## 2. chronology horizon：発散を結果として残す

\[
a^2=L^2-\Delta^2\to0^+
\]

では

\[
\Delta\langle\phi^2\rangle\sim a^{-2},
\qquad
\Delta\langle T_{\hat a\hat b}\rangle\sim a^{-4},
\qquad
T_{\mu\nu}T^{\mu\nu}\sim a^{-8}.
\]

したがって null deck orbit に近づくと topological correction は有限の小補正ではない。

forward は \(\Delta/L=0,0.5,0.9,0.99,0.999,0.9999\) を走査する。独立 verifier は \(a^2\) を10倍ずつ小さくし、RSET invariant が毎回 \(10^4\) 倍になることを検査する。

**この発散は subtraction して有限化しない。** local Minkowski/Hadamard singularity の subtraction は n=0 term に対応し、ここで発散しているのは nontrivial image が null-related になる global/topological singularityだからである。

De Lorenci–Moreira の spinning-circle analysis でも、spacelike identification は ordinary cylinder に写り、chronology horizon で compact length が 0 へ落ちて vacuum fluctuation / stress が発散する。timelike helical coordinate を global time として量子化した別の有限そうな式は Hadamard state ではない、と明示されている。

Kay–Radzikowski–Wald は compactly generated Cauchy horizon で Hadamard form が破綻する一般結果を与える。ただし今回の SA helical horizon が同定理の全仮定を満たすと未証明のまま適用範囲を拡張しない。

---

## 3. v10 の \(\Delta=2L\) を global RSET で再判定

v10 は

\[
L=100r_0,\qquad \Delta=2L
\]

なので

\[
a^2=L^2-\Delta^2=-3L^2<0.
\]

これは timelike deck vector の領域。

一方、flat image-state construction が Hadamard cylinder として成立するのは \(a^2>0\)。従って **v10 branch へ Casimir tensor を \(a^2<0\) として解析接続し、それを global RSET と呼ぶことはしない**。

v10 の local support root

    r0 = 101.493361669127784809... l_P
    Q^2 = 20601.8220619622529616...

は local \(M_2\times S^2\) effective problem では残る。しかし global chronology state の検査結果は次の通り。

| gate | v11 |
|---|---|
| local v10 algebraic RSET root | PASS（既存結果） |
| spacelike quotient image/Casimir control | PASS |
| global Hadamard image state at \(\Delta=2L\) | **FAIL** |
| chronology-horizon finiteness | **FAIL / divergent** |
| global finite RSET on v10 branch | **FAIL** |
| enlarged semiclassical solve | **not admissible / no solution certified** |
| state regularity | **FAIL for tested image completion** |
| dynamical stability | **not established** |

v10 の IFT Jacobian は「十分小さい static/spherical/diagonal extra RSET」への局所応答しか保証しない。chronology horizon の \(a^{-4}\) 発散はその仮定を外れる。

比較用に safe side で Casimir scale \(\pi^2/(90a^4)\) が v10 の electrostatic support scale

\[
\frac{Q^2}{8\pi r_0^4}
=7.7252976643\times10^{-6}\;l_P^{-4}
\]

と等しくなるのは

    a = 10.9152956495707027... l_P

である。null limit に近づけば topological term はこれを超えて発散する。

---

## 4. SA geometry へ拡張するとどこまで構成できるか

既存 SA の MP exterior は cylindrical coordinates で

\[
ds^2
=-U^{-2}dT^2
+U^2(d\rho^2+\rho^2d\phi^2+dz^2).
\]

静的 time translation と axial rotation が使える局所領域では、helical identification 候補を

\[
\gamma:(T,\phi)\mapsto(T-\Delta,\phi+\alpha)
\]

と書ける。

deck orbit の局所 norm は

\[
\boxed{
\ell^2
=
U^2\rho^2\alpha^2
-\frac{\Delta^2}{U^2}.
}
\]

したがって local chronology horizon は \(\ell^2=0\)。\(U\) を orbit 近傍で固定して読むと

\[
\rho_h=\frac{\Delta}{\alpha U^2}.
\]

v4 の shell-local control \(U_0=2,\rho=1,\alpha=2\pi\) なら

    Delta_critical = 8 pi
                   = 25.1327412287183459...

となる。

spacelike orbit region で global base state \(G^+_{\rm local}\) が供給されれば形式上

\[
G^+_{\rm quot}
=
\sum_n G^+_{\rm local}(x,\gamma^n x'),
\qquad
\Delta G^+_{\rm topo}
=
\sum_{n\neq0}G^+_{\rm local}(x,\gamma^n x')
\]

を試せる。

ただし現在の SA program にはその **一個の global positive Hadamard \(G^+_{\rm local}\)** がまだ無い。既存 v4 で既に、二 shell の sewing、外側・内側 RN horizon、timelike singularity r=0 の self-adjoint boundary completion、positivity / CCR / Hadamard regularity を同時に満たす state が未構成である。

さらに helical orbit が null へ近づくと local short-image sector だけでも

\[
\Delta\langle\phi^2\rangle\sim\frac{1}{12\ell^2},
\qquad
\Delta\langle T_{\hat a\hat b}\rangle
\sim\frac{\pi^2}{90\ell^4}
\]

となる。

従って **不足している mode data を任意に補って full SA sum が収束したとはしない**。今回の SA 拡張の結果は、full mode sum の未完成そのものと chronology-horizon asymptotic divergence の二点。

また v10 の translational \(M_2\) throat identification を、そのまま sewn SA 全体の global deck isometry とみなす根拠もない。SA に移すと identification 自体の幾何学的実装を再構成する必要がある。

---

## 5. semiclassical backreaction

拡張式

\[
G_{\mu\nu}
=
8\pi G
\left(
T_{\mu\nu}^{\rm local}
+\Delta T_{\mu\nu}^{\rm topo}
+T_{\mu\nu}^{\rm EM}
+T_{\mu\nu}^{\rm CBSSL}
\right)
\]

を解くには、まず同じ global state から得られる有限な \(\Delta T_{\mu\nu}^{\rm topo}\) が必要。

spacelike flat control branch ではこれは明示的に得られ、保存則・対称性・trace を通る。

しかし v10 chronology branch \(\Delta=2L\) には、今回採用した Hadamard image prescription の global RSET が存在しない。したがって **その branch について enlarged semiclassical equation を有限 tensor equation として solve したとはしない**。

null boundary に近づけて continuation を試みても topological RSET は \(a^{-4}\) で発散するため、v10 の small-correction IFT retuning の適用域に入らない。

結論：

    self-consistent global geometry/state solution found = false

これは root finder が失敗したという意味ではなく、**root finder に入れるべき admissible global RSET が先に失敗した**という判定。

---

## 6. 通信判定を分離して記録

v10 の独立 Z2 signal sector の local/formal 数値は変更しない。

\[
P(Y=+1\mid do(0))
=0.99865010196836990547\ldots,
\]

\[
P(Y=+1\mid do(1))
=0.00134989803163009453\ldots,
\]

\[
D_{\rm past}
=0.99730020393673981095\ldots>0.
\]

しかし v11 ではこれを通信成功判定と分離する。

| 項目 | 判定 |
|---|---|
| \(D_{\rm past}>0\) in isolated Z2 toy signal | yes |
| global quotient state Hadamard | **no for tested v10 image completion** |
| global renormalized RSET finite | **no** |
| semiclassical backreaction self-consistent | **no certified solution** |
| state regularity | **fail** |
| dynamical stability | **unproved** |
| globally certified past communication | **no** |
| protocol A | **no** |

従って **\(D_{\rm past}>0\) だけで A にしない**。

---

## 7. このモデルで犠牲になっている物理

### 7.1 global hyperbolicity / ordinary initial-value QFT

過去 advance を作るには timelike quotient が必要だが、標準 Hadamard image vacuum を構成できるのは spacelike quotient 側。過去通信を入れた時点で ordinary globally-hyperbolic initial-value QFT の土台を外している。

### 7.2 standard linear quantum dynamics

CBSSL 自体が chronology sector にだけ導入した **non-affine state-selection law**。標準 QFT や既存 quantum gravity から導出された法則ではない。

### 7.3 full SA state / singular boundary physics

RN の timelike singularity で self-adjoint boundary law を追加する必要があり、非極限 RN の二 horizon を一つの two-sided KMS 温度で同時正則化できない。全 SA の positive Hadamard state は未構成。

### 7.4 topology の dynamical formation

helical identification や SA handle は global topology として入力している。有限 mouth、transition layer、形成過程、装置 stress を ordinary Cauchy data から生成していない。

### 7.5 controlled semiclassical expansion

v10 は \(r_0\simeq101.5l_P\)、\(\xi=-10000\) という極端な effective parameter を使う。Popov の printed coefficients 自体は有限精度で、数値 solver の \(10^{-60}\) residual を物理の60桁精度とは解釈できない。高次曲率 counterterm、stress fluctuation、stochastic gravity は未解決。

### 7.6 dynamical stability

期待値 RSET を restricted static ansatz に入れた mean-field closure であり、non-spherical modes、time-dependent perturbations、RSET fluctuation に対する安定性を証明していない。

この六点は「細部」ではなく、A 判定から独立に明示すべき physics cost。

---

## 8. 再現

    python src/symbolic/cbssl_global_rset_v11.py --output /tmp/cbssl-v11.json

    python src/symbolic/cbssl_global_rset_verify_v11.py \
      --evidence /tmp/cbssl-v11.json \
      --output /tmp/cbssl-v11-verify.json

forward は flat image sum、point splitting、Casimir tensor、収束 tail bound、chronology-horizon scaling、v10 gate、SA local helical norm、通信 gate を計算。

verifier は forward を import せず、別の image partial sum、tensor invariant、causal-domain algebra、horizon scaling、SA norm、formal receiver を再計算する。

ローカル control は Python 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0 で実行。remote Python 3.12 CI は PR の最新 head の結果だけを受け入れ対象とし、完了前に PASS と主張しない。

---

## 9. 文献と適用範囲

- V. A. De Lorenci, E. S. Moreira Jr., *Vacuum polarization on the spinning circle*, arXiv:gr-qc/0112055. spacelike helical identification の cylinder mapping、chronology horizon の vacuum divergence、non-Hadamard helical-time prescription の問題。
- B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, Commun. Math. Phys. 183 (1997), arXiv:gr-qc/9603012. chronology/Cauchy horizon で Hadamard condition が破綻する一般結果。今回の SA horizon へ仮定未確認で全面適用しない。
- F. Schein, P. C. Aichelburg, *Traversable Wormholes in Geometries of Charged Shells*, Phys. Rev. Lett. 77, 4130 (1996), arXiv:gr-qc/9606069. SA classical geometry。
- A. A. Popov, *Semiclassical long throats of the wormholes*, Gravit. Cosmol. 20, 203 (2014), arXiv:1809.06202. v10 local support RSET。
- E. R. Bezerra de Mello, A. A. Saharian, *Fermionic vacuum polarization by a cosmic string in compactified cosmic string spacetime*, arXiv:1107.2557. compact direction の image/topological decomposition の比較参照。場種は異なるので係数を流用しない。

**scope:** v11 は「global state を入れれば v10 の成功がそのまま残る」と仮定せず、まず標準 image-state testbed を通した。その結果、past-advance condition と Hadamard image-state condition が両立せず、境界では topological RSET が発散するため、v10 simple helical quotient の global completion は C とした。
