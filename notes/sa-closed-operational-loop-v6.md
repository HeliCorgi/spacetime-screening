# SA候補v6：#25二入力制御を未来操作から過去受信記録まで閉じる

**2026-09-26。基点：PR #25 head `82274b96f69fd9c6fceb5166fdf07672429d650d`。**
対象は Schein–Aichelburg (SA) の同一外部へ戻る二荷電殻背景と、PR #25 の Reissner–Nordström (RN) 内部二入力逆散乱である。
原 [4D Past-Signalling Architecture Search Protocol](../docs/4d-past-signalling-protocol.txt) の A/B/C 基準は変更しない。

## 0. 結論

**この閉じ方では C。A にはならない。**

PR #25 の二入力制御を使い、未来側 `do(b)`、共通量子状態、RN 内部散乱、過去側有限 Ramsey 受信器、測定、受信記録の通常の前向き保存まで一つの操作模型にした。
開いた `do(0)/do(1)` 実験だけを見れば、受信器の二値分布は

```math
P(Y=y\mid do(b))=
\frac12\left[1+y(-1)^b d\right],
\qquad
d=e^{-2\lambda^2V_{\rm eff}}\sin(2\lambda s),
\qquad y=\pm1,
```

となり、形式的な識別度は

```math
D_{\rm past}=|d|.
```

しかし、過去の受信記録を通常の記憶で未来送信器へ運び、その未来局所装置に **copy** と **NOT** の二つの通常操作を許すと、同じ後ろ向き kernel の全履歴重みは

```math
Z_{\rm copy}=1+d,
\qquad
Z_{\rm NOT}=1-d.
```

同じ操作非依存・線形・正規化された物理過程が両操作に対して確率総和1を与えるには

```math
\boxed{d=0}
```

しかない。従ってこの閉じた模型で実際に許される受信分布は

```math
\boxed{
P(Y=+1\mid do(0))=P(Y=-1\mid do(0))=rac12,
}
```
```math
\boxed{
P(Y=+1\mid do(1))=P(Y=-1\mid do(1))=rac12,
\qquad D_{\rm past}=0.
}
```

**未計算量を null のまま残した結論ではない。** 全 SA の `s,V_eff` を数値化できていなくても、もしその開いた実験が `D=|d|>0` を主張すれば、閉じた copy/NOT 実験の確率総和がちょうど `1±D` だけずれる。したがって、このモデルクラスでは未知の数値を求める前に C が成立する。

この C は **SA 幾何一般の禁止定理ではない**。操作ごとに大域境界条件や背景を変更する規則、非線形な最終状態条件、postselection、copy/NOT のような通常局所操作を禁止する理論はこの証明の外である。ただし、それらは PR #25 の「同じ準備・同じ物理過程で未来の選択だけを変える」モデルからの前提変更であり、新しい B として導出し直す必要がある。

## 1. 幾何と、閉じる意味

[SA] は Majumdar–Papapetrou (MP) 外部の二つの殻を、同じ拡張 RN 時空の異なる漸近領域へ接合する。論文は、第二の内部接合面を第一の causal future に置き、外部へ戻る観測者を任意に過去へ出せる時間同一視が残ることを述べる。ここではこの古典背景を **入力として許す**。形成・安定性の問題だけで C にしたわけではない。

過去側受信イベントを `R`、未来側送信イベントを `S` とし、MP 外部の通常の因果経路で `R -> S` がある。受信器は `R` で結果 `Y` を有限記録へ保存する。その記録を通常のメモリとして `S` まで運べる。

「閉じたモデル」とは、後ろ向きの場チャネルだけを切り出すのでなく、**その過去記録が普通に未来装置へ利用可能**な一つの実験を意味する。これにより未来局所装置は、外から `do(b)` で固定する実験だけでなく、保存された `Y` を読んで bit を準備する通常の CPTP / measure-and-prepare 操作も実行できる。

## 2. 未来送信操作と #25 二入力散乱

PR #25 と同じく、RN 内部の各周波数・角モードについて

```math
\begin{pmatrix}G_1\\G_2\end{pmatrix}
=
\begin{pmatrix}{\cal T}&\overline{\cal R}\\
{\cal R}&\overline{\cal T}
\end{pmatrix}
\begin{pmatrix}F_A\\F_B\end{pmatrix},
\qquad
|{\cal T}|^2-|{\cal R}|^2=1.
```

[KSR] の可逆散乱を使う。目標出力を

```math
(G_1^{(b)},G_2^{(b)})=((-1)^b g,0)
```

とすると、二入力は

```math
F_A^{(b)}=(-1)^b\overline{\cal T}g,
\qquad
F_B^{(b)}=-(-1)^b{\cal R}g.
```

これは **未来送信操作の定義**である。二つの特性入力を物理装置が準備できることをここでは最大限有利に仮定する。

PR #25 の `Q/M=.99` の低周波極限では

```text
|T|^2+|R|^2 = 1.1657304406250865...
```

で、第二入力が正の二入力エネルギー和に占める割合は

```text
|R|^2/(|T|^2+|R|^2) = 0.07108437544798896...
```

である。これは確率ではなく、逆設計で第二 port が非零であることの定量化である。**以下の C は、この7.1%という値には依存しない。**

## 3. 量子状態を明示する

有限受信モード `Phi(F)` について、同じ準備を使う零平均 Gaussian seed `omega_0` を置く。受信モードの connected variance を

```math
V_{\rm eff}=V_0+\boldsymbol m^T\Sigma\boldsymbol m\ge0
```

とする。`Sigma` は PR #25 で導入した bit 非依存の Gaussian 準備雑音で、量子真空共分散そのものではない。

二入力 source が作る滑らかな coherent 解を `u` とし、受信 smearing に対する平均を

```math
s=u(F)
```

とする。bit 状態の受信モード特性関数は

```math
\chi_b(t)=
\exp\left[-\frac12V_{\rm eff}t^2+i(-1)^b s t\right].
```

従って 0/1 は同じ connected covariance を持ち、平均だけが反転する。これは各 bit に都合のよい別真空を選ぶ処方ではない。

**全 SA 上の Hadamard seed の存在を、この式で証明したわけではない。** 今回の C は、その seed と散乱を候補に有利に仮定してもなお残る運用整合性の障害である。

## 4. 有限受信器と測定

受信器は `R` の有限 worldtube 内にある二準位系。初期状態を `|+x>` とし、有限時間 smearing を吸収した相互作用を

```math
U_R=\exp[-i\lambda\sigma_z\Phi(F)]
```

とする。読出しは `sigma_y`、全結果 `Y=+1,-1` を保存する。Gaussian 特性関数を `t=2lambda` で評価すると

```math
\langle\sigma_y\rangle_b
=(-1)^b e^{-2\lambda^2V_{\rm eff}}\sin(2\lambda s).
```

よって

```math
d\equiv e^{-2\lambda^2V_{\rm eff}}\sin(2\lambda s),
```
```math
P(Y=y\mid do(b))=\frac12[1+y(-1)^bd].
```

具体的に

```math
P(Y=+1\mid do(0))=(1+d)/2,
\quad P(Y=-1\mid do(0))=(1-d)/2,
```
```math
P(Y=+1\mid do(1))=(1-d)/2,
\quad P(Y=-1\mid do(1))=(1+d)/2.
```

したがって、**開いたチャネルだけなら**

```math
D_{\rm past}
=\frac12\sum_y|P(y\mid do(0))-P(y\mid do(1))|
=|d|.
```

ここまでは「Aの候補式」であり、まだ閉じていない。

## 5. 閉路：受信記録を普通に未来へ戻す

`Y=+1` を古典 bit `r=0`、`Y=-1` を `r=1` とする。上の受信 kernel は

```math
K(r\mid b)=\frac12[1+(-1)^{r+b}d].
```

受信記録 `r` は外部 MP を普通に未来へ運ばれ、`S` の局所 controller に入力される。

### copy

```math
b=r.
```

全履歴の重みは

```math
Z_{\rm copy}=\sum_r K(r\mid r)=1+d.
```

### NOT

```math
b=1-r.
```

全履歴の重みは

```math
Z_{\rm NOT}=\sum_r K(r\mid1-r)=1-d.
```

この copy/NOT は特殊な時間旅行処方ではなく、過去で作られた通常の classical record を未来で読み、次の送信 bit を準備する局所操作である。

**同じ operation-independent kernel `K` が通常の確率法則で両操作と合成されるなら、両方で `Z=1` が必要。** よって

```math
1+d=1,
\qquad1-d=1
\quad\Longrightarrow\quad
\boxed{d=0}.
```

この結論は `s` と `V_eff` の未計算値に依存しない。

## 6. 「最後に正規化し直す」は rescue にならない

copy を確率 `q`、NOT を確率 `1-q` で未来装置がローカルに選ぶと、閉路全体の重みは

```math
Z(q)=1+(2q-1)d.
```

各未来操作ごとに最後に全履歴を正規化する処斸を入れると、実際に選ばれた copy の比率は

```math
q'=\frac{q(1+d)}{1+(2q-1)d}.
```

従って

```math
q'-q=
\frac{2q(1-q)d}{1+(2q-1)d}.
```

未来で自由に選んだはずの controller 分布まで、閉路のグローバル正規化で再重み付けされる。これは通常の `do` intervention の affine mixture ではなく、future-operation-dependent な postselection / final-boundary rule である。

原プロトコルは、通信差が future boundary condition や postselection から来るものを成功と数えない。従ってこの rescue は **現行Aではない**。

## 7. 定量化：null を使わずに、どこで失敗するか

今回、`s,V_eff` の全 SA 数値を求めていない。しかし不足を「unknown」で止めず、**もし開いたチャネルが主張する佩別度を `D=|d|` と置いた場合の閉路不整合を直接測る**：

```math
|Z_{\rm copy}-1|=|Z_{\rm NOT}-1|=D.
```

また固定された no-signal kernel `K_0(r|b)=1/2` へ戻すために必要な各 column の total-variation 修正は

```math
\boxed{\operatorname{TV}(K_d(\cdot|b),K_0(\cdot|b))=D/2.}
```

つまり `D` を非零にするほど、同じ大きさの正規化欠陥が閉じた copy/NOT 実験に現れる。

コード中の単なる数値対照として `lambda=1,V=.5,s=.2` を入れると

```text
d = D = 0.14325900215041577...
Z_copy = 1.14325900215041577...
Z_NOT  = 0.85674099784958422...
```

となる。**この数値は SA から得た受信データではなく、欠陥の大きさを確認する control である。**

## 8. 量子版：一人の forward laboratory として閉じる

過去受信入力から未来送信出力まで（記憶・controller を含む）を一の forward laboratory とみなし、外部の「時間機械部分」を一つの process とする。局所操作を通常の CP map、確率を線形な Born 型 pairing とし、**全 CPTP 操作に対して確率総和1**を要求する。

[OCB] の process-matrix 条件の一人版では、許される process は

```math
W=\rho_{\rm in}\otimes I_{\rm out}
```

の形に限られ、laboratory output からその input への signal を持たない。
今回の別検証コードは qubit の Pauli 基底でこの normalization 条件を再度解き、16係数中13個の独立制約から同じ形を得る。

これは process-matrix という別の CTC 処方を **採用して通信を作る**話ではない。むしろ「局所量子操作は通常のもの、global process は全局所 CPTP 操作に正規化された確率を与える」という #25 の線形量子模型を閉じた時の整合性検査である。

## 9. 最終分類

### C — `sa-two-input-closed-operational-v6`

明示した模型：

1. SA の固定4D背景と時間同一視を許す。
2. PR #25 の二入力を sender が両方制御できることまで許す。
3. 同じ Gaussian seed と bit-antisymmetric coherent displacementを使う。
4. RN 散乱後、過去側に有限 Ramsey receiver を置く。
5. `Y` を有限 classical record として普通に未来へ保存する。
6. 未来 laboratory では standard local CPTP / measure-and-prepare operation（少なくとも copy と NOT）を許す。
7. 背景/process は、その未来操作の選択に依存せず、線形・正規化された同じ物理過程である。

この条件では

```math
\boxed{
P(Y|do(0))=P(Y|do(1))=(1/2,1/2),
\qquad D_{\rm past}=0.
}
```

従って **A=0 / C=1**。

### この C から逃げるには

少なくとも一つを変更する必要がある：

- global boundary condition / background を future operation ごとに変える；
- 通常の線形・affine な確率合成を捨てる；
- operation-dependent postselection / final-state normalization を導入する；
- copy/NOT 等の通常局所操作を物理法則で禁止する；
- 受信記録を未来へ保存できないようにする。

これらは今回のCの論理的な escape だが、**現行プロトコルのAをそのまま満たす escape ではない**。新しい物理則を導出し、同じ `do(0)/do(1)` の自由選択・全装置・正規化確率を再構成する必要がある。

## 10. 再現

```bash
python src/symbolic/sa_closed_loop_v6.py --output /tmp/sa-v6/forward.json
python src/symbolic/sa_closed_loop_verify_v6.py \
  --evidence /tmp/sa-v6/forward.json --output /tmp/sa-v6/verification.json
```

順方向コードは二入力代数、Ramsey kernel、copy/NOT、`Q/M=.99` の第二入力比率を計算する。
別検証器は互いを import せず、classical feedback と一人 quantum process の normalization subspace、Gaussian Ramsey 則を別に再導出する。

## 11. 一次文献

- **[SA]** F. Schein, P. C. Aichelburg, *Traversable Wormholes in Geometries of Charged Shells*, PRL **77**, 4130–4133 (1996). https://arxiv.org/abs/gr-qc/9606069 。同一外部へ戻る古典背景と time identification。量子整合性の出典ではない。
- **[KSR]** C. Kehle, Y. Shlapentokh-Rothman, *A scattering theory for linear waves on the interior of Reissner–Nordström black holes*, Ann. Henri Poincaré **20**, 1583–1650 (2019). https://arxiv.org/abs/1804.05438 。PR #25 の二入力散乱と可逆性。
- **[OCB]** O. Oreshkov, F. Costa, C. Brukner, *Quantum correlations with no causal order*, Nature Communications **3**, 1092 (2012). https://arxiv.org/abs/1105.4464 。局所 CP map と global normalization を使う process 条件。今回の qubit 一人版はコードで再導出。
- **[D22]** E. Tjoa, K. Gallock-Yoshimura, *Channel capacity of relativistic quantum communication with rapid interaction*, PRD **105**, 085011 (2022). https://arxiv.org/abs/2202.12301 。場＋有限量子受信器の通信解析の参考。SA時空を解いた論文ではない。

**適用範囲を越えて「自然界では過去通信が一般に不可能」とは結論しない。** 今回得たのは、#25を standard linear/composable quantum operation と普通の forward record まで含めて閉じた場合の明確なC型障害である。
