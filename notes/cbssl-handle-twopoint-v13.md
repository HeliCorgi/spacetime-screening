# CBSSL v13：handle の \(\Delta G^+_{\rm handle}\) を実際に構成する

**2026-09-28。基点：PR #31 head 735e51ad470df93f4e680169084a9fdf90c77556。**

v12 では quantum support field が見る safe spatial \(S^1\) と、past advance を作る causal handle を分離した。

残った一問は

\[
G^+_{\rm full}
=
G^+_{\rm safe}
+
\Delta G^+_{\rm handle}
\]

の \(\Delta G^+_{\rm handle}\) を本当に作れるか、である。

## 結論

二つの意味を分けないといけない。

~~~text
closed geometric handle image-state completion : C
UV-soft open Gaussian return-channel completion : B
~~~

従って v13 全体の記録は

~~~text
A = 0
B = 1
C = 1
~~~

とする。

**標準的な closed geometric handle の image sum は失敗。**
しかし **open-system の UV-soft return channel まで許せば、safe S1 state を壊さない nonzero smooth \(\Delta G^+_{\rm handle}\) は構成できる。**

その代償は明確で、後者は ordinary closed local QFT on a wormhole/time-machine spacetime ではない。

---

## 1. closed geometric handle：結局 handle 自身に null-loop singularity が出る

v12 の primitive loop は

\[
\ell_{\rm loop}
=
d_{\rm ext}
+
\tau_{\rm shortcut}
=
\frac54r
\]

で、clock shift は

\[
\Delta_{\rm clock}=2r.
\]

したがって actual loop は

\[
s^2
=
\ell_{\rm loop}^2-\Delta_{\rm clock}^2
=
-\frac{39}{16}r^2<0.
\]

short-throat flat-space approximation で、一回 traversal ごとの attenuation を

\[
0<q<1
\]

とし、n回 winding/image を \(q^{|n|}\) で重み付けしても、spacelike side では coincidence correction は

\[
\boxed{
\Delta\langle\phi^2\rangle_{\rm handle}
=
\frac{\operatorname{Li}_2(q)}
{2\pi^2s^2}
}
\]

となる。

point splitting の tensor scale は

\[
\boxed{
\Delta T_{\rm handle}
\sim
\frac{\operatorname{Li}_4(q)}
{\pi^2s^4}.
}
\]

つまり fixed attenuation \(q>0\) は zeta function を polylog に変えるだけで

\[
s^2\to0^+
\]

の singularity を消さない。

コードでは \(q=1/2\) で \(\Delta/\ell=0,0.5,0.9,0.99,0.999,0.9999\) を走査する。

結果は

\[
\Delta\phi^2\sim(s^2)^{-1},
\qquad
\Delta T\sim(s^2)^{-2}
\]

のまま。

v12 actual point は timelike side \(\Delta/\ell=1.6\)。spacelike image formula をそのまま解析接続して standard Hadamard state と呼ばない。

この branch は **C**。

### literature control

Visser は traversable wormhole の short closed spacelike geodesicsに対する Hadamard Green function と point-split stress を明示的に検討し、time-machine onset に近づく vacuum polarization の増大を議論している。

Kay–Radzikowski–Wald は compactly generated Cauchy horizon の base point で local Hadamard form が破綻し、renormalized \(\phi^2\) / stress tensor が ill-defined または singular になることを証明している。

今回の short-throat control はこれらの一般結論を全 handle geometry へ無条件に拡張するものではなく、v12 の一個の single-handle image completion を直接テストする。

---

## 2. fixed loss だけでは駄目なら、何を変える必要があるか

幾何 optics の high-frequency mode まで constant \(q>0\) で handle を通すと、arbitrarily short wavelength が closed null loop に乗るため singularity は残る。

従って singularity を消すには少なくとも

\[
q(\omega)\to0
\qquad
(\omega\to\infty)
\]

が必要。

これは standard transparent wormhole ではない。

**mouth interaction が UV で opaque になる**という新しい物理を入れる必要がある。

そこで次の open Gaussian channel を testbed にする。

---

## 3. UV-soft open Gaussian return channel

dimensionless frequency を

\[
u=\omega r
\]

とする。

return map を modewise に

\[
\boxed{
a
\mapsto
q(u)e^{iu\theta}a
+
\sqrt{1-q(u)^2}\,b
}
\]

とする。

ここで

\[
q(u)
=
\frac12e^{-u^4},
\qquad
\theta
=
\frac{
\tau_{\rm shortcut}
+
d_{\rm ext}
-
\Delta_{\rm clock}
}{r}
=
-\frac34.
\]

\(b\) は environment mode。

これは \(|q(u)|<1\) の pure-loss Gaussian channel で、environment を含めれば ordinary unitary dilation を持つ。

environment は gauge-invariant Gaussian state とし

\[
N(u)
=
10^{-2}e^{-u^4}
\]

の occupation を持たせる。

occupation map は

\[
n'
=
q^2n
+
(1-q^2)N.
\]

従って unique fixed point は

\[
\boxed{n_*(u)=N(u)}.
\]

anomalous covariance は0。

return phase \(e^{iu\theta}\) は mean/cross-return phaseへ効くが、gauge-invariant fixed occupationそのものは phase invariant。

---

## 4. explicit nonzero \(\Delta G^+_{\rm handle}\)

safe state の Wightman function に対する fixed-state correction は

\[
\boxed{
\Delta G^+_{\rm handle}(x,x')
=
\int
\frac{d^3k}
{2(2\pi)^3\omega}
N(\omega r)
\left[
e^{-ik\cdot(x-x')}
+
e^{+ik\cdot(x-x')}
\right].
}
\]

これは nonzero。

しかも correction は symmetric なので Wightman antisymmetric part、すなわち CCR を変えない。

また

\[
N(u)\sim e^{-u^4}
\]

なので全ての momentum moment が有限で、\(\Delta G^+_{\rm handle}\) は \(C^\infty\)。

従って safe Hadamard state に加えても local Hadamard singularity は変わらない。

### positivity

\(N(u)\ge0\) なので standard gauge-invariant quasifree occupation stateとして positive。

従ってこの open model 内では

~~~text
positive state    = yes
CCR preserved     = yes
Hadamard preserved= yes
nonzero Delta G+  = yes
~~~

まで通る。

---

## 5. coincidence と RSET

spatial coincidence で

\[
\Delta\langle\phi^2\rangle
=
\frac{1}{2\pi^2r^2}
\int_0^\infty
du\,
uN(u).
\]

\[
\int_0^\infty
u e^{-u^4}du
=
\frac{\sqrt\pi}{4}
\]

なので

\[
\boxed{
\Delta\langle\phi^2\rangle
=
\frac{N_0}{8\pi^{3/2}r^2}.
}
\]

energy density は

\[
\rho_H
=
\frac{1}{2\pi^2r^4}
\int_0^\infty
du\,
u^3N(u).
\]

\[
\int_0^\infty
u^3 e^{-u^4}du
=
\frac14
\]

より

\[
\boxed{
\rho_H
=
\frac{N_0}{8\pi^2r^4}.
}
\]

isotropic local mode bath として

\[
\boxed{
\Delta T^\mu{}_{\nu,H}
=
\rho_H
\operatorname{diag}
(-1,1/3,1/3,1/3).
}
\]

trace は0、constant core では保存される。

これは closed geometric image RSET ではなく、**open Gaussian handle fixed-state RSET**。

---

## 6. backreaction をもう一度 solve

v12 の

- Popov local RSET
- electrostatic stress
- safe \(S^1\) topological RSET
- axion winding

へ上の finite handle RSET を追加する。

再び

\[
(r,Q^2,f^2)
\]

を解く。

結果：

~~~text
r
= 101.4934092093366163923693455382825215758... l_P

Q^2
= 20601.80940956709659271493373502532281230...

f^2
= 6.0427319670168532427301892063817524975e-8 l_P^-2
~~~

3×3 Jacobian は

~~~text
det J
= 2.17069421468806221606460209276e-16
~~~

で nonzero。

safe core + open handle state correction について semiclassical residual は数値0に再solveできる。

---

## 7. これは何を達成して、何を達成していないか

### 達成

- \(\Delta G^+_{\rm handle}\) を explicit integral として構成
- nonzero
- positive quasifree
- CCR preserved
- smooth / Hadamard preserving
- finite \(\Delta\langle\phi^2\rangle\)
- finite RSET
- safe \(S^1\) state を壊さない
- v12 regulated coreを再solve
- low-frequency return gain \(q(0)=1/2\) を保持

### 未達

これは **closed geometric wormhole QFT ではない**。

mouth を

\[
q(\omega)=\frac12e^{-(\omega r)^4}
\]

という frequency-dependent open channel で置き換え、environment mode を追加している。

従って

1. reservoir/apparatus の stress-energy
2. この frequency-dependent mouth map を生む microscopic local action
3. reservoirも含めた full chronology-cut algebra
4. finite mouth/transition geometry
5. formation dynamics
6. stability

は未完成。

とくに reservoir を trace out した support-field RSET だけで gravity accounting complete としてはいけない。

---

## 8. communication

v10-v12 の Z2 receiver control は

\[
P(+|do0)
=
0.9986501019683699\ldots
\]

\[
P(+|do1)
=
0.0013498980316301\ldots
\]

\[
D_{\rm past}
=
0.9973002039367398\ldots.
\]

open handle の low-frequency return gain は

\[
q(0)=1/2
\]

なので return channel 自体は zero ではない。

ただし signal sector と support-field Gaussian channel の complete common apparatus state はまだ構成していないため

~~~text
globally certified communication = false
~~~

を維持する。

---

## 9. 判定

| completion | state | RSET | backreaction | verdict |
|---|---|---|---|---|
| closed geometric image handle | null-loop divergence / timelike continuation not accepted | divergent at onset | not admissible | **C** |
| UV-soft open Gaussian handle | positive, CCR, Hadamard-preserving | finite | regulated core re-solved | **B** |

Aにはしない。

後者で新たに犠牲にしたのは

- closed-system locality at the mouths
- transparent high-frequency geometry
- support field aloneのunitarity
- reservoir-free gravity accounting

である。

---

## 10. 再現

~~~bash
python src/symbolic/cbssl_handle_twopoint_v13.py \
  --output /tmp/cbssl-v13.json

python src/symbolic/cbssl_handle_twopoint_verify_v13.py \
  --evidence /tmp/cbssl-v13.json \
  --output /tmp/cbssl-v13-verify.json
~~~

forward は closed image/polylog branch と open Gaussian branch を両方計算。

verifier は forward を import せず、

- fixed-q null divergence
- Gaussian occupation integrals
- fixed covariance
- alternative \(y=r^2,Q^2\) core solve
- receiver distribution

を再計算する。

---

## 11. 文献

- M. Visser, *From wormhole to time machine: Comments on Hawking's Chronology Protection Conjecture*, Phys. Rev. D 47, 554 (1993), arXiv:hep-th/9202090.
- M. Visser, *Hawking's chronology protection conjecture: singularity structure of the quantum stress-energy tensor*, Nucl. Phys. B416, 895 (1994), arXiv:hep-th/9303023.
- M. Visser, *van Vleck determinants: traversable wormhole spacetimes*, Phys. Rev. D49, 3963 (1994), arXiv:gr-qc/9311026.
- B. S. Kay, M. J. Radzikowski, R. M. Wald, *Quantum Field Theory on Spacetimes with a Compactly Generated Cauchy Horizon*, Commun. Math. Phys. 183, 533 (1997), arXiv:gr-qc/9603012.
- J. Tolksdorf, R. Verch, *Quantum physics, fields and closed timelike curves: The D-CTC condition in quantum field theory*, arXiv:1609.01496. CTC spacetime上でも量子場 algebra の非標準 construction があり得ることの比較。今回のopen Gaussian channelの導出元ではない。

**scope:** closed local geometric handleとしての \(\Delta G^+_{\rm handle}\) は今回失敗。open UV-soft Gaussian return channelまで理論を拡張すれば explicit smooth \(\Delta G^+_{\rm handle}\) は作れる。これは「幾何の問題を解いた」のではなく、mouth physics を新しい open-system sectorへ移した結果である。
