# SA候補v7：Deutsch固定点で #25 のCを逃げられるか

**2026-09-27。基点 `fbc4e2bf567e00e021f94216f470198f5ce41880`（PR #25 merge後）。**

#25で固定したSA v5二入力部品はこれ以上最適化しない。本ノートでは、v6で (D_{\rm past}=0) を強制した operation-independent linear process を、実際に選択された未来操作ごとにloop stateを自己無撞着固定点で選ぶ Deutsch 型則へ変更したとき、明示的な過去受信分布と copy/NOT の自己無撞着性を同時に得られるかだけを計算する。

## 0. 結論

**数理toy modelとしてはCを逃げられる。分類は A=0 / B=1 / C=0。**

明示パラメータ

```math
a=\frac12,\qquad \eta=a^2=\frac14,\qquad
\lambda=1,\qquad c=\frac{\pi}{8}
```

を選び、selected bosonic loop modeの一周CPTP写像 (Phi_b) に

```math
\rho_b^*=\Phi_b(\rho_b^*)
```

を要求する。

固定点の受信分布は

```math
P(Y=+1\mid do(0))=\frac{1+e^{-1}}2,
\qquad
P(Y=-1\mid do(0))=\frac{1-e^{-1}}2,
```

```math
P(Y=+1\mid do(1))=\frac{1-e^{-1}}2,
\qquad
P(Y=-1\mid do(1))=\frac{1+e^{-1}}2,
```

したがって

```math
\boxed{D_{\rm past}=e^{-1}=0.36787944117144233\ldots>0.}
```

となる。全 (Y=\pm1) を保持し、postselectionは用いない。

さらに過去記録を未来へ戻した copy と NOT の full bosonic feedback mapにもDeutsch条件を適用すると、双方に正規化された固定点があり、受信分布は ((1/2,1/2)) に収束する。したがってv6の「同一kernelを全操作へ合成すると正規化できない」というCは、この**新しいoperation-dependent global law**の下では回避される。

ただし、このDeutsch固定点則をSchein–Aichelburg時空の3+1D半古典QFTから導出していない。よってAではない。

## 1. 一周する物理toy model

loop modeのquadratureを

```math
[X,P]=i
```

とし、真空分散を (V_X=V_P=1/2) とする。

### 1.1 過去側finite receiver

Ramsey qubitを (|+x\rangle) に準備し、

```math
U_R=e^{-i\lambda\sigma_zX},\qquad \lambda=1
```

で有限smearing済みmodeへ結合し、(sigma_y) を測る。全結果を保持する。

fieldだけのunconditional receiver mapは

```math
\mathcal M(\rho)=
\frac12e^{-iX}\rho e^{iX}
+\frac12e^{iX}\rho e^{-iX}.
```

これは (P) にランダムな (pm1) kickを与えるQND mapで、(X) marginalを変えない。

### 1.2 ordinary forward segment

過去receiverから未来senderまでの通常のforward segmentを、vacuum ancillaを持つpure-loss channel

```math
\mathcal L_\eta,\qquad
a=\sqrt\eta=\frac12
```

で表す。

### 1.3 future do(b) と frozen SA v5

未来senderは (b\in\{0,1\}) を自由に選び、#25の固定済み二入力を同じ符号で駆動する。selected mode上では一周あたり

```math
X\mapsto X+(-1)^b c,
\qquad c=\frac{\pi}{8}
```

のcoherent displacementとして正規化する。pulse shapeは再最適化しない。

一周mapは

```math
\Phi_b(\rho)
=
D_x[(-1)^bc]\,
\mathcal L_{1/4}(\mathcal M(\rho))\,
D_x[(-1)^bc]^\dagger.
```

## 2. Deutsch固定点を厳密に解く

Weyl characteristic functionを

```math
\chi(k_x,k_p)=
\operatorname{Tr}\!\left[
\rho e^{i(k_xX+k_pP)}
\right]
```

とする。

vacuumから一周mapを反復して極限を取ると、固定点は

```math
\boxed{
\chi_b^*(k_x,k_p)=
e^{i(-1)^b\pi k_x/4}
e^{-(k_x^2+k_p^2)/4}
\prod_{n=1}^{\infty}\cos(2^{-n}k_p)
}
```

となる。

従って

```math
\langle X\rangle_b=(-1)^b\frac{\pi}{4},
\qquad V_X=\frac12.
```

receiver back-actionの (P) kickはlossで一周ごとに (2^{-n}) へ減衰するので

```math
V_P=\frac12+\sum_{n=1}^{\infty}4^{-n}
=\frac56.
```

よって

```math
V_XV_P=\frac5{12}>\frac14.
```

固定点は (P) 方向には一般に非Gaussianだが、必要な (X) marginalはexact Gaussianである。

## 3. 過去側受信確率

Ramsey測定のeffectは

```math
M_y^\dagger M_y
=\frac12[1+y\sin(2X)],
\qquad y=\pm1.
```

(X\sim N((-1)^b\pi/4,1/2)) なので

```math
\langle\sin(2X)\rangle_b
=(-1)^b e^{-1}.
```

これから冒頭の (P(Y|do(b))) と

```math
D_{\rm past}=e^{-1}
```

を得る。これは未計算値の代入ではない。

## 4. copy / NOT も同じDeutsch則で閉じる

受信結果から誘導されるbinary kernelは

```math
K=\frac12
\begin{pmatrix}
1+d&1-d\\
1-d&1+d
\end{pmatrix},
\qquad d=e^{-1}.
```

copy (b=r) に対するDeutsch consistencyは

```math
p=Kp,
```

NOT (b=1-r) では

```math
p=KXp,
\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

非自明固有値はそれぞれ (d), (-d) で、(|d|<1)。従って両方の一意な正規化固定点は

```math
p^*=(1/2,1/2).
```

classical recordだけでなく、measurement Kraus、pure-loss Kraus、outcome-dependent displacementを含むfull bosonic CPTP maps

```math
\Phi_{\rm copy}(\rho)
=\sum_yD_x(yc)\,
\mathcal L(M_y\rho M_y^\dagger)\,
D_x(yc)^\dagger,
```

```math
\Phi_{\rm NOT}(\rho)
=\sum_yD_x(-yc)\,
\mathcal L(M_y\rho M_y^\dagger)\,
D_x(-yc)^\dagger
```

もFock cutoff (N=10,14) で直接反復した。

| cutoff | do(0) (P(+)) | do(1) (P(+)) | copy (P(+)) | NOT (P(+)) |
|---:|---:|---:|---:|---:|
| 10 | 0.683913382584 | 0.316086617416 | 0.5 | 0.5 |
| 14 | 0.683939684055 | 0.316060315945 | 0.5 | 0.5 |
| exact do | 0.683939720586 | 0.316060279414 | — | — |

(N=14) の最後のFrobenius stepは do(0/1)で約 (9.76\times10^{-15})、copyで (5.00\times10^{-15})、NOTで (4.10\times10^{-15})。これはcutoff収束診断であり無限次元誤差証明ではない。

## 5. なぜAではないか

このtoy modelは、A判定で欲しかったoperational quantityをすべて数値化している：

- future senderの (do(0),do(1))
- 同じreceiver
- 全測定結果
- (P(Y|do(0)))
- (P(Y|do(1)))
- (D_{\rm past}=e^{-1}>0)
- copy/NOTも自己無撞着fixed pointを持つ

それでもAではない理由は一つの物理的な核心に集約される。

> **Deutschのoperation-dependent fixed-point selection lawを、SA二殻の3+1D scalar QFTの境界・初期値問題から導いていない。**

Deutsch型CTC量子論ではこの固定点則を追加原理として置く。Aaronson–WatrousもDeutsch causal consistencyをevolution mapのfixed pointとして定式化する。一方、別のCTC量子処方が非等価であることも知られている。従って

```math
\rho=\Phi_E(\rho)
```

をSA時空の通常QFTから自動的に得られる境界条件として扱うことはできない。

full operation-dependent (langle T_{\mu\nu}\rangle_{\rm ren}) とEinstein backreactionも未計算だが、その前に固定点則そのものの物理的由来を決める必要がある。

**分類：A=0 / B=1 / C=0。**

## 6. 次の計算問題は一つだけ

pulse、detector、loss parameterの最適化には戻らない。

> **SA二殻接合を含む3+1D scalar QFTについて、in-in / Schwinger–Keldysh propagatorから「receiver interaction → ordinary forward segment → future two-port source → SA return」の一周reduced superoperator (Phi_E^{SA}) を導出し、物理的なboundary/initial-value prescriptionが実際に operation-dependent fixed-point condition (ho=\Phi_E^{SA}(\rho)) を強制するか判定する。**

これがYESなら、同じstateのRSET/backreactionを評価してA判定へ進める根拠になる。NOならDeutsch escapeはCになる。

## 7. 再現

```bash
python src/numerical/sa_deutsch_fixed_point_v7.py --output /tmp/sa-v7/forward.json
python src/symbolic/sa_deutsch_fixed_point_verify_v7.py \
  --evidence /tmp/sa-v7/forward.json --output /tmp/sa-v7/verification.json
```

forwardはexact algebraに加え、receiver Kraus、pure-loss Kraus、bit/outcome-dependent displacementをFock cutoff (N=10,14) で直接反復する。verifierはforwardをimportせず、固定点mean/variance、binary copy/NOT、TVをexact algebraで再導出し、evidence hashとB判定を検査する。

## 8. 文献

- D. Deutsch, *Quantum mechanics near closed timelike lines*, Phys. Rev. D **44**, 3197 (1991). https://doi.org/10.1103/PhysRevD.44.3197
- S. Aaronson, J. Watrous, *Closed Timelike Curves Make Quantum and Classical Computing Equivalent*, Proc. R. Soc. A **465**, 631–647 (2009). https://arxiv.org/abs/0808.2669
- H. D. Politzer, *Path integrals, density matrices, and information flow with closed timelike curves*, Phys. Rev. D **49**, 3981 (1994). https://doi.org/10.1103/PhysRevD.49.3981
- F. Schein, P. C. Aichelburg, *Traversable Wormholes in Geometries of Charged Shells*, Phys. Rev. Lett. **77**, 4130 (1996). https://arxiv.org/abs/gr-qc/9606069

**このBを「Deutschの理論が正しい証拠」や「SAで過去通信が可能な証拠」とは扱わない。** 今回示したのは、#25のCが依存していたoperation-independent linear processをDeutsch fixed-point lawへ明示的に置き換えると、内部整合したtoy levelでは正の (D_{\rm past}) を実際に作れる、というescapeの定量化である。
