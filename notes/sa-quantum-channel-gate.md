# 二荷電殻の量子通信：接合、有限パルス、地平面、受信記録

**2026-09-24。基点 `2304cbc39b638491d20cb9ece2f44b05bb216426`。**
対象はSchein–Aichelburg [SA]のMP外部＋二荷電殻＋拡張RN内部である。
同時進行のPR #22の「MP外部を直接接合する負の殻」とは別模型であり、その結果を混ぜない。
配布済みv3のSA検討を継続するが、未マージの配布ファイルへの依存を新設しない。

## 結論

**完全な二殻実験の過去の受信確率は、今回も得ていない。**
以下を実際に導出・検算し、Bを「近極限RN＋特定の有限パルス」という、さらに具体的な条件へ絞った。

| 計算したもの | 到達点 |
|---|---|
| 四次元場と二つの殻の接合 | 最小結合scalarの値・法線微分・時計対応・KG流束の条件を導出 |
| 有限パルスの地平面応答 | [KSR]の厳密な散乱結果を適用。有限入力でも散乱尾が生じ、通常の片側パルスは滑らかな通過と両立しない場合がある |
| 肯定側の波形 | 最初の危険な極の係数を厳密に零にする非零の有限パルスを構成。積分値は保持し、入力地平面でのKillingエネルギー比は約27.4517 |
| 0/1と有限受信器 | 同じ場の共分散を使う条件付きの記録付き確率式を導出。完全実験の平均・雑音は未取得 |
| 頑健性 | パルスの任意に小さい調整誤差が最初の特異な尾を復活させる。地平面の全正則性・量子雑音を解決したわけではない |

原[A/B/C定義](../docs/4d-past-signalling-protocol.txt)を変えない。
今回の主候補 `sa-shaped-horizon-pulse-v4` は **B**。
通常パルス＋固定された滑らかな地平面の組合せには、以下の範囲のC型障害がある。
一つの入力波形の変更を何台もの独立した装置として数えない。

## 1. 同じ四次元模型で、何を接続するか

自然単位 `hbar=c=1`、M,Qは長さ。MP外部は

```math
ds^2=-U^{-2}dT^2+U^2d\boldsymbol x^2,\qquad \nabla^2U=0.
```

[SA]の等電位二球の像解を用い、座標半径 `R=1`、中心 `z=±3`、`m1=1`、表面値 `U0=2`、面積半径 `A=RU0=2` とする。
内部は

```math
ds^2=-f(r)dt^2+dr^2/f(r)+r^2d\Omega_2^2,\qquad
f(r)=1-2M/r+Q^2/r^2,\qquad M=1/5.
```

前回の `Q/M=1/2` と、今回の `Q/M=.99,.999` を区別する。
近極限化は明示したパラメータ変更で、同じ支持殻の証明を失わないことを次に確認する。

[SA]の殻の応力を、法線をRNからMPへ向ける規約で書くと

```math
\sigma=-\frac{U_n}{4\pi G U_0^2}-\frac{1-\sqrt{f(A)}}{4\pi G A},\qquad
p_\Sigma=\frac{1-(1-M/A)/\sqrt{f(A)}}{8\pi G A}.
```

像漸化式の第二項以降の質量絶対値和は5/24以下、像への距離は同球で4/5より大、他球で24/5より大なので、全角度で

```math
-U_n\ge1-1/25-(5/24)(25/16+25/576)=216151/345600.
```

`1/2<=Q/M<1` 全体で `321/400<=f(A)<81/100`、したがって

```math
\sigma-|p_\Sigma|\ge\frac1{16\pi GR}\frac{1014173}{2474496}>0.
```

この証明は**必要な古典殻のDEC**で、荷電材料の状態方程式、放電、形成操作、殻の全安定性の証明ではない。
[SA]の時空は永遠の延長・時刻同一視・timelike特異点を入力として含む。普通の初期空間から製造した解ではない。

## 2. 場の方程式と、殻に本当に必要な条件

中性・実・質量ゼロ・最小結合scalarとする。殻上にscalarの追加相互作用は置かない。

```math
S_\phi=-\tfrac12\int d^4x\sqrt{-g}\,g^{ab}\partial_a\phi\partial_b\phi
-\int d^4x\sqrt{-g}\,J\phi,\qquad \Box_g\phi=J.
```

4×4計量から導出した方程式は

```math
\Box_{\rm MP}\phi=-U^2\partial_T^2\phi+U^{-2}\nabla^2\phi,
```
```math
\Box_{\rm RN}\phi=-f^{-1}\partial_t^2\phi+
 r^{-2}\partial_r(r^2f\partial_r\phi)+r^{-2}\Delta_{S^2}\phi.
```

各殻で、未来向きに取った各局所静的時計について

```math
d\tau=dT/U_0=\sqrt{f(A)}\,dt,
```
```math
\phi_{\rm MP}|_\Sigma=\phi_{\rm RN}|_\Sigma,\qquad
U_0^{-1}\partial_n\phi_{\rm MP}|_\Sigma=
\sqrt{f(A)}\,\partial_r\phi_{\rm RN}|_\Sigma.
```

法線は両側で同じ向き。全RNブロックを一つの静的t座標で覆うとはしない。
後者は分布的な波動方程式に無許可の殻sourceを生じさせない条件であり、KG流束も一致させる。
局所周波数は `omega_RN=U0 sqrt(f(A))*omega_MP`。
二つの殻の間の大域的な時計対応は、これだけでは決まらない。

非最小結合を使うなら殻のdelta型曲率による条件変更が必要である。本計算ではそれを黙って落とさず、**最小結合を選ぶ**。
MP外部の波動問題は非球対称で、内部の球面調和モードを外側まで独立に伝わるものと仮定しない。

二点関数Wには、この条件を両引数で課し、波動方程式、正値性、局所CCR、Hadamard条件も同時に要求する。
殻の接合は伝達条件であり、量子状態・他の地平面の入力・特異点の境界条件を指定する代わりにはならない。

## 3. 内側地平面へ向かう散乱を、4Dの結果から計算する

内部で `phi=u_lm(t,r)Y_lm/r`、`dr*/dr=1/f` とすれば

```math
[-\partial_t^2+\partial_{r_*}^2-V_l]u_{lm}=0,\qquad
V_l=f\left[\frac{l(l+1)}{r^2}+\frac{f'}r\right].
```

これは四次元場の部分波であり、支持物理を二次元CFTに置換したものではない。
[KSR]のProposition 2.5は、二つの地平面の間の散乱係数について

```math
{\cal T}(0,l)=\frac{(-1)^l}{2}(r_-/r_++r_+/r_-),\qquad
{\cal R}(0,l)=\frac{(-1)^l}{2}(r_-/r_+-r_+/r_-),
```
```math
|{\cal T}|^2-|{\cal R}|^2=1
```

を与える。コードでは零周波数のLegendre解と保存量から別に照合する。
**これは一般の量子チャネルの透過確率ではない。** 特に `.5` では `T(0,0)=7`、`R(0,0)=-4 sqrt(3)` で、49を通信成功確率にしてはいけない。
また[KSR]の有限なdegenerate Killing energyは、自由落下系の応力有限性を保証しない。

### 有限の入力でも、出力の尾は有限時間で終わるとは限らない

[KSR] Theorem 5と証明の(3.32)–(3.34)を使う。
一方の外側地平面に `f(v)Y_00` を入れ、もう一方の入力を零に固定する。fは滑らかで有限の台を持つ。
今回の電荷比では `r_+!=3r_-` なので、l=0の最初の極の例外ではない。

```math
\widehat f(\omega)=\frac1{\sqrt{2\pi}}\int e^{-i\omega v}f(v)\,dv,
\qquad L[f]=\int e^{\kappa_+v}f(v)\,dv.
```

`L[f]!=0` なら、`T(omega,0)` の `omega=i kappa+` の非零留数により、該当するCauchy地平面上のtraceに

```math
\partial_v\phi\sim C e^{-\kappa_+v},\qquad C\ne0
```

という尾が出る。定理はCH_B上でv→∞、すなわち未来bifurcation sphere B+へ近づくtraceから、反対側のCH_A全点へのC1延長の失敗も与える。
**CH_Bの有限vにある全ての横断点で発散する、と読み替えてはいけない。** 実際のSA帰還経路がどの枝を使い、摂動がその先へどう伝わるかは未接続である。任意の殻時刻を、このvと同一視するものではない。
非負で非零のsmooth bumpならL[f]>0なので、入力が有限時間だからという理由では避けられない。
**これは[SA]外部の任意の送信器が必ずこの地平面データを作るという定理ではない。** 外部sourceから地平面traceへの準備・逆問題は別に残る。

```math
r_\pm=M\pm\sqrt{M^2-Q^2},\qquad
\kappa_\pm=\frac{r_+-r_-}{2r_\pm^2},\qquad
p=\frac{\kappa_+}{\kappa_-}=\left(\frac{r_-}{r_+}\right)^2<1.
```

正則な地平面座標 `Vbar=-exp(-kappa- v)` では、尾が作る振幅差は `O(|Vbar|^p)` で有限でも、その微分は発散し得る。
この尾のstressのスケーリングは

```math
(\partial_{\bar V}\phi)^2\sim {C^2\over\kappa_-^2}|\bar V|^{2p-2}.
```

| Q/M | p | 最初の尾のstressのべき 2p−2 | 次の外側極に由来する項の形式的なべき 4p−2 |
|---:|---:|---:|---:|
| .5 | .005154776143 | −1.989690448 | −1.979380895 |
| .99 | .5666248905 | −.8667502190 | +.2664995620 |
| .999 | .8361393260 | −.3277213480 | +1.344557304 |

右端は「次の極がその項を与える場合」のべきで、全モード・全枝の漸近展開を求めた数値ではない。
正則な基準Hadamard状態が供給された場合、そのsmooth coherent displacementの相対応力は、地平面の手前では `Delta<T_ab>_ren=T_ab[phi]`。
上の発散は、その基準状態と固定された滑らかな計量を該当枝まで保つ案に対する障害である。全非線形反作用の最終形や、全通信不能を導いたわけではない。
場の値が有界で応力が発散する場合があるため、有限時間の検出器応答まで必ず発散するとは結論しない。

## 4. 肯定側：最初の尾を消す有限パルス

`z=kappa+ v` とし

```math
h(z)=\begin{cases}\exp[-1/(1-z^2)]&|z|<1,\\0&|z|\ge1,\end{cases}
\qquad f_0(v)=h(\kappa_+v),\qquad
f_1(v)=h(\kappa_+v)+h'(\kappa_+v).
```

h'はz微分。両方とも滑らかで、台は同じ有限区間。部分積分から

```math
\int e^z[h(z)+h'(z)]dz=0,\qquad
\int[h(z)+h'(z)]dz=\int h(z)dz>0.
```

**極の係数を零にした結果であり、通信を零にして誤魔化したものではない。** 零周波数の積分値は保持する。
ただし「積分値非零」は、完成した過去の測定分布差ではない。
送信候補は `f_b=(-1)^b f1`。前処理や選別ではなく、初期の波形を変える操作として提案する。
ここで指定しているのは**外側地平面での特性データ**であり、実際の有限の殻外送信器から作れたとはまだ言わない。

一般には

```math
f_N=\prod_{n=1}^N\left(1+\frac{1}{n}\partial_z\right)h,
\quad
\int e^{mz}f_Ndz=\prod_{n=1}^N(1-m/n)\int e^{mz}h dz
```

なので、最初のN個の指定された指数momentを消せる。全ての極に非零留数があるとは未確認であり、Nを「必要な制御数」と断定しない。
`.99` では `p>1/2` であり、最初の外側極を消した後の次の外側極は、べきの上ではC1障害を作らない。
`p>1/2` の条件は `Q/M>sqrt(1-(3-2 sqrt(2))^2)≈.9851714310`。
内側極、共鳴、別の枝、他の角モード、量子共分散、特異点からの入力は未処理である。**一つのmomentの相殺を、地平面正則性の十分条件にしない。**

### 波形のエネルギー代償

同じ振幅・同じ台・同じ積分値で比べる。`int |Y_00|^2 dOmega=1` とした地平面のKillingエネルギーは、共通係数を除けば `int (df/dv)^2 dv`。

```math
\int(h')^2dz=0.40958706075277012817\ldots,
```
```math
\int(h''+h')^2dz=11.243854872151635756\ldots,
```
```math
\boxed{E_1/E_0=27.451684756561468282\ldots.}
```

交差項は境界項となって零。この比は殻外の電源・送信装置の仕事や、受信誤り率を固定した最適化の答えではない。
積分はz上と、別実装の `z=tanh u` 上で比較。50/80桁の一致は物理近似の精度を意味しない。

### 無限の精度で調整したことを隠さない

誤差を `f1+epsilon h` とすると

```math
L[f1+\epsilon h]=\epsilon L[h].
```

どんな非零の誤差でも、最初の尾は復活する。消去条件は連続な線形汎関数のkernel、すなわちcodimension-one条件で、入力の任意の小さな一般摂動に対して開いた正則性領域ではない。
有限のカットオフでは許容差を定義できるが、そのまま厳密な地平面通過を意味しない。
例えば規格化した微分の係数を1以下に保つ指標は `|epsilon|<=|Vbar|^(1-p)`。
`.99`、`|Vbar|=10^-12` では約 `6.30e-6`。これは単位prefactorの指標で、実装装置の校正仕様ではない。

## 5. 送信0・1と、有限の量子受信記録

ここは**条件付きの解析式**と**未取得の実験確率**を分ける。
完全な接合模型の零平均で正のGaussian状態Wと、同じ準備・境界条件で定まるsource応答phi_Jが得られたと仮定する。
coherent符号化では

```math
\langle\Phi\rangle_b=(-1)^b\phi_J,\qquad
W_{b,\rm connected}=W,\qquad
\langle T_{ab}\rangle_b-\langle T_{ab}\rangle_W=T_{ab}[\phi_J]
```

が成り立つ範囲がある。**0と1の投入前・読出し前の応力は同じ**なので、符号反転では地平面問題を隠せない。
この恒等式の使用には同じ基準状態を用い、各ビットに都合のよい別の真空を選ばない。

受信器を場と初期に無相関な縮退した二準位系、初期状態を `|+x>`、相互作用をコンパクトで滑らかな結合による `lambda sigma_z Phi(F)` とする。
受信器worldtube内に通常の局所的な時間順序があるとする。自由場の交換子がc-numberなので、その相互作用の時間順序は全体位相にしか寄与せず、`U_R=exp[-i lambda sigma_z Phi(F)]` を使える。
読出しはsigma_y、記録は `y=±1`。

```math
s_F=\int F\phi_J\,d{\rm vol},\qquad
V_F=\tfrac12\langle\{\Phi(F),\Phi(F)\}\rangle_{W,\rm connected},
```
```math
P(R=b,Y=y)=\frac{p_b}{2}\left[1+y(-1)^b e^{-2\lambda^2V_F}\sin(2\lambda s_F)\right].
```

有限の受信結合、全部の結果、保存した選択bitを含む。事後選別の確率ではない。[D22]は局所場を介する通信の参考で、このSA時空を解いた論文ではない。
別検証器はPauli行列とGaussianスペクトル積分から照合する。

**今回は、実際の二殻時空のW・phi_Jを大域的に求めていないので、過去のs_F,V_Fは数値化できていない。**
検算用Gaussianの数値を代入したものを、実装装置の確率として出力しない。
全実験の `P(Y|do(0)),P(Y|do(1)),D_past` は未計算・null。
この一般式を得たことを、ユーザーが求めた「地平面横断後の受信記録まで同じ実験で計算」の完了とは報告しない。

## 6. 殻の整合だけでは残る、量子問題の入力

### 内部の特異点境界

RNの内側の静的領域 `0<r<r_-` では、radial scalarのSturm–Liouville形は

```math
-(\Delta R')'+l(l+1)R=\omega^2 wR,\qquad
\Delta=r^2f\to Q^2,\quad w=r^2/f\sim r^4/Q^2.
```

r→0で `R=c0+c1 r+...` の二解がともにこの重みで二乗可積分。
境界形式は `Q^2(c0^* d1-c1^* d0)` で、外側の殻条件からは消えない。
例えばDirichletや `Q^2 R'(0)=beta R(0)`（実beta）が異なる自己共役境界を与え、beta>=0なら対応する静的領域の形式は

```math
\int_0^{r_-}[\Delta|R'|^2+l(l+1)|R|^2]dr+\beta|R(0)|^2\ge0.
```

[IW]の静的・非大域的双曲的背景の方法と整合する。**これは全CTC時空の量子化ではない。**
特異点からの因果的影響を受けない局所の領域だけなら、その境界を必要としない場合もある。
古典的なcarrierがr=0に当たらないことだけから、全場の境界問題が一意とするのは避ける。

### 正則な地平面状態の既存結果

[T20]はRNのCauchy地平面でHadamardな状態を構成する。したがって「RNの地平面を含む量子状態は全て不可能」は使わない。
ただしその状態を二殻へ接合して、外側から準備可能な一つの状態として得たわけではない。
[ZLO20]は別の標準状態で量子流束を計算する。数値係数をSA背景の値として流用しない。
これらの結果、全角モードの共分散と、有限sourceからのcoherent応答を同時に接合することが残る。

## 7. 検証と再現

```bash
python src/symbolic/sa_quantum_channel_gate.py --output /tmp/sa/gate.json
python src/symbolic/sa_quantum_channel_verify.py --output /tmp/sa/verification.json
```

2本は互いをimportしない。前者は四次元作用素・接合・原変数の積分、後者は別の静的radial解・変数変換積分・受信器の行列計算を検証する。
両方の既定実行が計算を完走するので、既存の研究Python選別器で検査できる。新しいworkflowや依存、原A validatorは変更しない。
追加のB診断記録は後者のJSONに全必須項目と未取得確率を含めるが、既存固定バッチの候補集合へ自動登録したものではない。

実施：local Python3.13.5/SymPy1.14.0/mpmath1.3.0、50/80桁、異なる積分表現を40桁閾値で比較。
[KSR]の解析的散乱定理自体をPythonやLeanで証明したわけではない。1個の有限パルスを全時空でPDE時間発展したわけでもない。
**独立研究者・別AIの査読、Lean形式化、全モードRSET、外側送信器と地平面後の受信確率は未実施。**
PDF本文の抽出テキストを確認した。web screenshotは取得エラーのため、Penrose図の独立目視確認を実施したとはしない。
remote CIの実施SHA・run・結果はPRの完了コメントに追記する。文書作成時の予測を成功として扱わない。

## 8. 一次文献と使用箇所

- **[SA]** F. Schein, P. C. Aichelburg, *Traversable Wormholes in Geometries of Charged Shells*, PRL **77**, 4130 (1996). https://arxiv.org/abs/gr-qc/9606069 。古典幾何・殻接合・同じ外部のCTC。[SA]自体が内部地平面問題を指摘する。
- **[KSR]** C. Kehle, Y. Shlapentokh-Rothman, *A scattering theory for linear waves on the interior of Reissner–Nordström black holes*, Ann. Henri Poincare **20**, 1583–1650 (2019), arXiv v2 (2018). https://arxiv.org/abs/1804.05438 。Proposition2.5、Theorems3–5、特に(3.32)–(3.34)。定理の輸入と、今回のmoment消去・数値特化を区別した。
- **[T20]** P. Taylor, *Regular Quantum States on the Cauchy Horizon of a Charged Black Hole*, CQG **37**, 045004 (2020), arXiv v2 (2019). https://arxiv.org/abs/1904.05941 。正則な地平面状態の存在。SA大域状態への無条件な移植はしない。
- **[ZLO20]** N. Zilberman, A. Levi, A. Ori, *Quantum fluxes at the inner horizon of a spherical charged black hole*, PRL **124**, 171302 (2020). https://arxiv.org/abs/1906.11303 。通常RNの特定状態の繰込み流束。今回そのmode sumを再計算していない。
- **[IW]** A. Ishibashi, R. M. Wald, *Dynamics in Non-Globally-Hyperbolic Static Spacetimes II: General Analysis of Prescriptions for Dynamics*, CQG **20**, 3815–3826 (2003). https://arxiv.org/abs/gr-qc/0305012 。静的領域での境界データの扱い。全SAの処方決定ではない。
- **[D22]** E. Tjoa, K. Gallock-Yoshimura, *Channel capacity of relativistic quantum communication with rapid interaction*, PRD **105**, 085011 (2022), arXiv v5 (2023). https://arxiv.org/abs/2202.12301 。場の状態・交換子・検出器を使う通信解析の参考。今回の有限smooth couplingの受信器式は独自に導出した。
