# v10：CBSSLで3+1D renormalized stressを解き、regulated coreで R_sc=0 を作る

**2026-09-27。基点 `c27097e29e05275b56a922e5c63e0b99526d1da2`（CBSSL v9 merge後）。**

目的は、CBSSLを言葉だけのstate-selection lawで終わらせず、実在する4D renormalized stress-energy tensorを半古典Einstein方程式へ入れ、同じ3+1D coreで `R_sc=0` と明示的な過去bit分布を同時に得られるかを検査すること。

## 結論

**A=0 / B=1 / C=0。**

regulated coreには

```math
ds^2=-dt^2+dx^2+r_0^2d\Omega_2^2
```

を採用する。4D Christoffel/Ricciを直接再計算すると

```math
R=\frac{2}{r_0^2},\qquad
G^\mu{}_{\nu}
=\operatorname{diag}\!\left(-\frac1{r_0^2},-\frac1{r_0^2},0,0\right).
```

support sectorには A. A. Popov, *Semiclassical long throats of the wormholes* (Gravit. Cosmol. 20, 203 (2014), arXiv:1809.06202) のconstant-long-throat scalar RSETを使用する。これは「必要stressを逆定義」したものではなく、論文でrenormalizeされたquantum stressを使う。

`xi=-10000`, `m^2=1000`, `m_DS=m` とし、さらにclassical electrostatic field

```math
T^\mu{}_{\nu,EM}
=\frac{Q^2}{8\pi r^4}\operatorname{diag}(-1,-1,1,1)
```

を加えて、独立なEinstein方程式を `r,Q^2` について直接解いた。

80桁計算：

```text
r0 = 101.4933616691277848090930477809412531792577387412069 l_P
Q^2 = 20601.822061962252961632375628991644733357093389645794
|Q| = 143.533348257337928518916615024491059156964147471892
```

```text
<T^mu_nu>_q =
diag(+3.86265204502187e-6,+3.86265204502187e-6,
     -7.72529766430392e-6,-7.72529766430392e-6)

T^mu_nu_EM =
diag(-7.72529766430392e-6,-7.72529766430392e-6,
     +7.72529766430392e-6,+7.72529766430392e-6)
```

で、4成分すべてについて

```math
G^\mu{}_{\nu}-8\pi\left(
\langle T^\mu{}_{\nu}\rangle_{q,ren}
+T^\mu{}_{\nu,EM}
\right)=0
```

を満たす。

実際の最大residualは約 `9.01e-66`、CBSSLのpositive apparatus-frame contractionに対応するcore densityは

```text
R_sc / Vol(C) = 1.93e-130
```

である。したがって**このregulated 3+1D core model内では `R_sc=0`**。

これは巨視的wormholeではない。半径は約 `1.64e-33 m` で、Planck lengthの約101.5倍。

## Popov RSET

mixed componentsを

```math
\langle T^t{}_t\rangle_q
=\langle T^x{}_x\rangle_q
=\frac{1}{4\pi^2r^4}
\left[
0.00310+\frac1{720}\ln(m_{DS}^2r^2)
+\frac{P_t(\xi)}{m^2r^2}
\right],
```

```math
\langle T^\theta{}_\theta\rangle_q
=\langle T^\phi{}_\phi\rangle_q
=\frac{1}{4\pi^2r^4}
\left[
-0.00171-\frac1{720}\ln(m_{DS}^2r^2)
+\frac{P_\theta(\xi)}{m^2r^2}
\right],
```

```math
P_t=-\frac{\xi^3}{6}+\frac{\xi^2}{12}-\frac{\xi}{60}+\frac1{630},
\qquad
P_\theta=-2P_t
```

として実装した。論文に印刷された `0.00310,-0.00171` の精度を超える情報を捏造しない。

別検証器は `y=r^2,e=Q^2` で独立に解き直し、最大residual `2.15e-54`。論文の表示された近似閉形式との `r^2` 相対差は約 `4.30e-8` で、印刷係数の有限精度と整合する。

## chronology core

global toy closureとして

```math
(t,x)\sim(t-\Delta,x+L),
\qquad L=100r_0,\quad \Delta=2L
```

を置く。

generatorのnormは

```math
L^2-\Delta^2=-3L^2<0
```

なのでtimelike orbitを持ち、+x方向のnull traversalは

```math
\Delta t_{past}=\Delta-L=L>0
```

だけcoordinate pastへ戻る。

**これはmouthを人間が形成した解ではない。chronology quotientをtoyとして課している。**

## bitをsupport stressから分離する

通信bitには独立なreal Z2 order parameter `chi` を使う：

```math
V(\chi)=\frac{\lambda_\chi}{4}(\chi^2-v^2)^2.
```

`chi=+v,-v` では

```math
\partial\chi=0,\qquad V=0,\qquad T_{\mu\nu}^{signal}=0.
```

未来の `do(b)` はreturning order parameterを `(-1)^b v` へreset/biasするcomplete local operation。CBSSL chronology consistencyは対応するfixed pointを選ぶ。future outcome postselectionは使わない。

したがって**bit 0/1でsupport RSETもsolved metricも変化しない**。

## finite receiver

past worldtubeで `chi` の符号を測り、apparatus noiseを

```math
n\sim N(0,\sigma^2),\qquad v/\sigma=3,
\qquad Y=\operatorname{sign}(\bar\chi+n)
```

とする。

```math
P(Y=+1\mid do(0))=\Phi(3)
=0.99865010196836990547\ldots,
```

```math
P(Y=+1\mid do(1))=1-\Phi(3)
=0.00134989803163009453\ldots.
```

従って

```math
\boxed{
D_{past}
=\operatorname{erf}(3/\sqrt2)
=0.99730020393673981095\ldots>0.
}
```

receiverはhelical null returnによりsenderより過去側に置ける。

## global RSETを0扱いしない

ここがAへ上げない核心。

Popovのconstant-core RSETを、timelike helical quotient上の**full global state-dependent RSETそのもの**だとは主張しない。global topology/image contributionを

```math
\delta T^t{}_t,\qquad \delta T^\theta{}_\theta
```

として残す。

現rootで2本のsemiclassical residual `F=(E_t,E_theta)` のJacobianは

```text
det dF/d(r,Q^2)
= 3.605757766897522e-14 != 0
```

なのでimplicit-function theoremにより、十分小さいstatic/spherical/diagonal correctionならnearby `r,Q^2` を再調整して `R_sc=0` を保てる。

一次応答は

```text
8 pi J^-1 =
[[-6.5689016877e6, -6.5689016877e6],
 [ 2.6667997737e9,  9.1563573515e-2]]
```

で定量化した。

ただし大きな補正、`T^t_t != T^x_x`、off-diagonal flux、time dependence、non-Hadamard状態ならこの2-parameter retuningでは足りず、metric ansatzを拡張する必要がある。

## なぜまだAでないか

今回初めて同一toy core内で

- actual published 3+1D renormalized support RSET
- direct 4D Einstein tensor
- nonlinear semiclassical solve
- `R_sc=0`
- bit 0/1で同一background stress
- finite receiver
- explicit `P(Y|do(0))`, `P(Y|do(1))`
- `D_past>0`

を同時に置いた。

それでも **B** なのは：

1. chronology quotient上のCBSSL-selected support fieldのfull two-point function / nonlocal RSETをまだ計算していない。
2. asymptotically-flat finite mouths / transition apparatusを構成せずhelical quotientを課している。
3. full CBSSL stateのdynamical stability、cutoff/cut independenceを証明していない。

## 次の一問

pulseやreceiver tuningには戻らない。

> **helical chronology quotient上でCBSSLが選ぶsupport scalarの3+1D two-point functionを構成し、Popov local termへ加わるnonlocal/topological `delta<T_mn>_ren` をmode/image sumで計算する。そのtensorを入れた拡張semiclassical equationsで `R_sc=0` が生き残るか判定する。**

Jacobianがnonzeroなので、小さいsymmetry-preserving correctionならlocal existenceは保証される。勝負はactual correctionがその範囲に入るか、Hadamard/positivity自体が破綻するか。

## 再現

```bash
python src/symbolic/cbssl_rset_core_v10.py --output /tmp/v10.json
python src/symbolic/cbssl_rset_core_verify_v10.py \
  --evidence /tmp/v10.json --output /tmp/v10-verify.json
```

forwardは4D curvature、50/80桁solve、RSET、`R_sc`、IFT Jacobian、receiver distributionを計算。verifierはforwardをimportせず、product-curvature identity、`y=r^2` の独立root、Z2 receiverを再計算する。

## 文献

- A. A. Popov, *Semiclassical long throats of the wormholes*, Gravit. Cosmol. **20**, 203 (2014), https://arxiv.org/abs/1809.06202
- S. Jiang, J. Jiang, *Stress-energy tensor of quantized scalar fields in a zero-tidal wormhole*, Phys. Rev. D **114**, 025001 (2026), https://arxiv.org/abs/2603.01003
- [CBSSL v9](chronology-backreaction-selection-v9.md)

**scope:** Popovのpublished RSETはそのconstant-long-throat model内で使う。新しいglobal CTC quotientのexact RSETへ黙って昇格させない。そのmissing correctionが次の計算対象。
