# CBSSL v14：wormhole mouth を局所作用で UV 不透明にする

**2026-09-28。基点：PR #32 head 7f7fbec0b56c9592459e79b0c84a8be4ced8950c。**

v13 では phenomenological に

\[
q(u)=\frac12e^{-u^4}
\]

を置くと、実軸上では smooth な \(\Delta G^+_{\rm handle}\) と finite RSET を作れた。

v14 はこれをやめ、**mouth に局所作用を置いて UV opacity を導出**する。

## 結論

局所 UV opacity 自体は作れる。

しかし chronology loop まで閉じると

~~~text
natural two-mouth local filter  : C
four-stage local passive filter : C
v13 super-Gaussian causal audit : C
~~~

となる。

記録上は

~~~text
A = 0
B = 0
C = 3
~~~

とする。

重要なのは「mouth を UV で不透明にできない」のではない。

**できる。**
ただし、

1. 自然な2-mouth版では RSET convergence に減衰次数が足りず、
2. 4段まで積んで実軸 RSET を有限化すると、
3. past-advance feedback が上半平面poleを作り、stationary state が線形不安定

になる。

---

## 1. positive local mouth action

reduced normal channel の scalar \(\phi\) に対して timelike mouth sheet \(x=0\) 上へ

\[
S_{\rm sheet}
=
\frac12
\int dt
\left[
\zeta(\partial_t\phi)^2
-
\mu\phi^2
\right]_{x=0}
\]

を置く。

bulk は通常の

\[
S_{\rm bulk}
=
\frac12
\int dt\,dx
\left[
(\partial_t\phi)^2
-
(\partial_x\phi)^2
\right].
\]

\[
\zeta>0,\qquad \mu>0
\]

なら localized energy は

\[
H_{\rm sheet}
=
\frac12
\left[
\zeta(\partial_t\phi)^2
+
\mu\phi^2
\right]
\ge0.
\]

高次時間微分は使わない。

field equation を sheet の両側で積分すると

\[
[\partial_x\phi]
=
(\mu-\zeta\omega^2)\phi.
\]

左から unit amplitude を入れると exact transmission は

\[
\boxed{
t(\omega)
=
\frac{2i\omega}
{\zeta\omega^2+2i\omega-\mu}.
}
\]

dimensionless \(u=\omega r\) で

\[
\mu r=\zeta/r=1
\]

と規格化すると

\[
\boxed{
t(u)
=
\frac{2iu}{(u+i)^2}.
}
\]

energy transmission は

\[
\boxed{
|t|^2
=
\frac{4u^2}{(1+u^2)^2}.
}
\]

reflection は

\[
|r|^2
=
\frac{(u^2-1)^2}{(1+u^2)^2},
\]

従って

\[
|t|^2+|r|^2=1.
\]

これは open dissipative ansatz ではなく、一枚の sheet と field の scattering として flux-unitary。

さらに

\[
u\to0:
\qquad
t(u)\sim-2iu,
\]

\[
u=1:
\qquad
t(1)=1,
\]

\[
u\to\infty:
\qquad
t(u)\sim\frac{2i}{u}.
\]

従って

~~~text
IR opaque
signal band u=1 transparent
UV opaque
~~~

を同時に作れる。

brane-localized kinetic term が short-distance/high-frequency field behavior を大きく変えること自体は brane localization literature に既知の機構がある。

---

## 2. 一枚ずつ両mouthへ置くだけでは足りない

一回の chronology traversal が entrance / exit の2枚を通ると

\[
q_2(u)=t(u)^2.
\]

high frequency では

\[
q_2\sim u^{-2}.
\]

closed-null image の 4D point-split stress の absolute UV test は模式的に

\[
\int^\infty du\,
u^2|q(u)|.
\]

\(q_2\) では

\[
u^2|q_2|
\to4,
\]

なので

\[
\boxed{
\int^\infty du\,u^2|q_2|
=\infty.
}
\]

つまり

**「各mouthを一枚のpositive kinetic sheetでUV不透明にする」だけでは RSET divergence を消せない。**

これは C。

---

## 3. 4段 passive filter なら実軸 RSET は有限

chronology path に4段の同じ filter stage を通す engineered network を考える。

直接 chronology-path amplitude は

\[
q_4(u)=t(u)^4.
\]

従って

\[
q_4\sim\frac{16}{u^4}.
\]

signal band では

\[
q_4(1)=1.
\]

一方、

\[
|q_4|
=
\left(
\frac{2u}{1+u^2}
\right)^4.
\]

二点関数側の absolute spectral control は

\[
\int_0^\infty du\,|q_4|
=
\frac{\pi}{2}.
\]

RSET側は

\[
\boxed{
\int_0^\infty du\,
u^2|q_4|
=
\frac{5\pi}{2}
<\infty.
}
\]

従って **real-frequency UV divergence は消せる。**

v12 の past advance を

\[
a
=
\frac{
\Delta_{\rm clock}
-
d_{\rm ext}
-
\tau_{\rm shortcut}
}{r}
=
\frac34
\]

と書く。

feedback denominator は

\[
D_4(u)
=
1
-
q_4(u)e^{-iau}.
\]

実軸では \(D_4=0\) は起きない。

\[
|q_4|=1
\]

になれるのは \(u=1\) だけだが、

\[
e^{-ia}
=
e^{-3i/4}
\neq1.
\]

numerical scan でも \(0<u<20\) で denominator は有限のまま。

ここだけ見れば v13 の目的だった

~~~text
UV finite two-point/RSET
signal-band transmission
~~~

は局所作用から作れたように見える。

---

## 4. ところが upper-half-plane に不安定poleが出る

causal stability は real axis だけでは判定できない。

\[
u=iy,
\qquad y>0
\]

へ解析接続すると

\[
t(iy)
=
\frac{2y}{(1+y)^2}.
\]

従って N-stage filter は

\[
q_N(iy)
=
\left[
\frac{2y}{(1+y)^2}
\right]^N.
\]

past advance factor は

\[
e^{-iau}
\to
e^{ay}.
\]

よって feedback gain は

\[
\boxed{
{\cal G}_N(y)
=
\left[
\frac{2y}{(1+y)^2}
\right]^N
e^{ay}.
}
\]

有限 \(N\) では

\[
y\to0:
\quad
{\cal G}_N(y)\to0,
\]

一方

\[
y\to\infty:
\quad
{\cal G}_N(y)
\sim
\left(\frac{2}{y}\right)^N
e^{ay}
\to\infty
\]

for every \(a>0\)。

従って連続性から必ず

\[
{\cal G}_N(y_*)=1
\]

を満たす \(y_*>0\) が存在する。

これは

\[
D_N(iy_*)=0
\]

すなわち upper-half-plane pole。

### 実際のpole

\[
a=3/4
\]

では

~~~text
N=2 : y* = 2.296508313484674...
N=4 : y* = 9.273959245421315...
N=6 : y* = 18.72684416216217...
N=8 : y* = 29.37568443570611...
~~~

4段版では

\[
\boxed{
\omega_* r
=
i\,9.273959245421\ldots
}
\]

なので mode は指数増大する。

growth time は

\[
\tau_{\rm grow}/r
=
1/y_*
=
0.1078288\ldots.
\]

つまり 4段化は real-axis RSET を有限にするが stationary chronology branch は線形不安定。

これを success にはしない。

---

## 5. causal delay を足せば安定化できるか

filter 自体に ordinary positive delay \(\tau_f\) があると

\[
q_N
\to
q_Ne^{+iu\tau_f/r}.
\]

upper imaginary axis では

\[
{\cal G}_N(y)
\sim
y^{-N}
e^{(a-\tau_f/r)y}.
\]

従って finite-N family で asymptotic pole を避けるには少なくとも

\[
\boxed{
\tau_f/r
\ge a.
}
\]

しかし net past advance は

\[
a_{\rm net}
=
a-\tau_f/r.
\]

従って

\[
\tau_f/r\ge a
\quad\Rightarrow\quad
a_{\rm net}\le0.
\]

つまり

**causal positive delay を十分入れて feedback を安定化すると、その delay が past advance を食い潰す。**

この filter family では

~~~text
stable
past-directed
finite-RSET
~~~

の三つを同時に取れない。

---

## 6. v13 の super-Gaussian cutoff も causal-realizability を監査

v13 は

\[
q_{13}(u)
=
\frac12e^{-u^4}
\]

を real frequency profile として使った。

real axis では

\[
|q_{13}|\le1/2
\]

で非常に良く減衰する。

しかし passive causal transfer function としては upper half plane 全体の解析性・boundedness も必要。

\[
u
=
Re^{i\pi/4}
\]

とすると

\[
u^4=-R^4,
\]

従って

\[
\boxed{
|q_{13}|
=
\frac12e^{R^4}
}
\]

となって発散する。

例：

~~~text
R=1   : |q| ≈ 1.359...
R=1.5 : |q| ≈ 78.9...
R=2   : |q| ≈ 4.44e6
~~~

従って v13 の \(e^{-u^4}\) profile は

**real-axis regulator としては使えるが、passive causal H-infinity mouth transfer としては採用できない。**

v13 B は causal microscopic realization の gate を通すと、この特定 profile について C へ落ちる。

---

## 7. 何が分かったか

「wormhole を UV で透明にしない」は可能。

今回の局所 sheet は

- local
- positive localized energy
- second-order in time
- exact unitary scattering
- UV opaque
- signal band transparent

を満たす。

問題はそこではない。

問題は **past advance を feedback loop として閉じた瞬間**。

finite-stage causal filter の inverse-power UV suppression は、upper imaginary axis で chronology advance の

\[
e^{ay}
\]

に必ず負ける。

従って今回の class では

\[
\boxed{
\text{UV opacity alone does not cure chronology instability.}
}
\]

---

## 8. 判定

| candidate | UV opaque | real-axis RSET | causal stability | past advance | verdict |
|---|---:|---:|---:|---:|---:|
| 1 sheet / mouth | yes | **diverges** | not reached | yes | **C** |
| 4-stage local passive filter | yes | **finite** | **unstable UHP pole** | yes | **C** |
| v13 \(e^{-u^4}\) filter | yes on real axis | finite | **not passive causal H∞** | formal | **C** |

今回新しい B は置かない。

---

## 9. 残るescape route

今回の結果が直接潰しているのは

- finite-stage
- passive
- local-in-time
- rational/polynomial UV filter
- stationary negative-delay feedback

の class。

残る可能性は別物理になる。

1. infinite-dimensional continuum filter with nontrivial spectral measure
2. nonstationary mouth interaction
3. chronology sector自体のnonlinear CBSSL dynamics
4. non-passive active stabilization
5. full quantum gravity where the mouth is not representable as a stationary linear transfer function

ただし causal positive delayだけで安定化する方法は、今回の accounting では advance を消す。

---

## 10. 再現

~~~bash
python src/symbolic/cbssl_uv_opaque_mouth_v14.py \
  --output /tmp/cbssl-v14.json

python src/symbolic/cbssl_uv_opaque_mouth_verify_v14.py \
  --evidence /tmp/cbssl-v14.json \
  --output /tmp/cbssl-v14-verify.json
~~~

forward は

- local action
- exact transmission/reflection
- flux unitarity
- N=2 RSET divergence
- N=4 exact spectral integrals
- real-frequency feedback
- upper-half-plane roots
- causal delay tradeoff
- v13 super-Gaussian causal audit

を計算。

verifier は別実装で scattering flux、beta-function integrals、bisection pole、delay tradeoff を再計算する。

---

## 11. 文献

- G. Dvali, G. Gabadadze, M. Shifman, *(Quasi)Localized Gauge Field on a Brane: Dissipating Cosmic Radiation to Extra Dimensions?*, arXiv:hep-th/0010071. Brane-localized kinetic term が高周波/短距離 behavior を変える比較参照。
- A. Donini, *A scalar field coupled to a brane in M4 x S1. Part I*, arXiv:1512.03978. Scalar brane coupling と brane-localized kinetic term の exact spectrum。
- S.-Y. Lin, *Unruh-DeWitt detectors as mirrors: Dynamical reflectivity and Casimir effect*, arXiv:1806.00816. 局所 oscillator-field interaction から frequency-dependent reflectivity を作る比較参照。
- M. Visser, *Hawking's chronology protection conjecture: singularity structure of the quantum stress-energy tensor*, arXiv:hep-th/9303023.
- B. S. Kay, M. J. Radzikowski, R. M. Wald, arXiv:gr-qc/9603012.

**scope:** v14 は「local positive UV opacityを入れれば v13 の smooth handle state を microscopic に救えるか」を試した。mouth filter単体は作れたが、finite-stage passive stationary chronology feedbackは不安定で失敗した。
