# 二荷電殻の量子場・地平面・有限受信記録 — v4

**2026-09-24。読取開始: `2304cbc39b638491d20cb9ece2f44b05bb216426`。**
**適用基点はPR #22のマージ後main: `4ad470bc12187c4a9eee040ec9d34964cee5b446`。**
対象は Schein–Aichelburg [S96] の MP外部＋拡張RN内部を持つ二荷電殻。
別方式のPR #22（作業中にマージ）（MP外部の二境界を直接つなぐ構成）へ置き換えず、そのファイルも変更していない。
原則は [原プロトコル](../docs/4d-past-signalling-protocol.txt) の送信介入と有限受信記録である。

## 0. 結論と未達事項

**全二荷電殻時空で、地平面を越えて過去の受信器まで届く量子状態と数値的な同時確率は、今回も完成していない。**
「式に未取得の伝達係数・雑音を入れれば計算できる」ことを、実際の過去通信確率の取得とは呼ばない。

今回の具体的な進展は次の四つ。

1. **4Dの場の接合を導出**。両殻での時計対応・法線微分・KG流束の一致を確認。外部の非球対称なモード混合を残した。
2. **RN内部の場に必要な追加データを特定**。r=0の二つの有限エネルギー枝を示し、Dirichlet/Neumannという二つの局所的自己共役境界条件で反射位相が異なることを数値計算した。
3. **単一温度の平衡準備を条件付きで棄却**。同じKilling時計の一つのKMSパラメータで、非極限RNの外側・内側両方の分岐地平面を二側から正則に覆う条件は両立しない。全非平衡状態や片側の有限実験は排除しない。
4. **有限時間の位相感応受信器から全結果の確率法則を導出**。ただし、その式に必要な全SA時空の応答核と二点関数は未取得。局所の4D真空雑音を別に計算しても、それをSA全体の雑音へ代入しない。

分類は **A=0 / B=1 / C=2**。Bは全候補の継続、Cは単一平衡準備と、符号を読めない特定の受信方式。
三件の独立装置や自然界の成功確率ではない。以前のB全体をCへ変更したわけではない。

## 1. 物理入力を明示する

[S96] は、外部が同じMP時空、内部がRNの異なる漸近領域へ連なる古典構成を与える。
幾何と特異点を含む延長は入力で、人間が通常の初期空間から形成した解ではない。
今回のパラメータは、前回配布ノートと同じ

```math
R=1,\quad d=3,\quad U_0=2,\quad A=RU_0=2,
\quad m=1/5,\quad e=1/10.
```

RはMP側の球の座標半径、Aは殻の面積半径。物理的な長さを戻すと全長さにR、時間にR/cを掛ける。
以下は原則 `hbar=c=1`。m,eはRNの幾何パラメータで、素電荷そのものではない。

信号場は**中性・実・質量ゼロ・最小結合の4Dスカラー**とする。

```math
S_\phi=-\frac12\int d^4x\sqrt{-g}\,g^{ab}\nabla_a\phi\nabla_b\phi
+\int d^4x\sqrt{-g}\,J_b\phi,
\qquad J_b=(-1)^b j.
```

jは同じ装置領域に台を持つ実の滑らかなsource。ビットによって境界条件や初期真空を変更しない。
スカラーの殻上の追加作用は今回ゼロに固定する。非最小結合 `xi R phi^2` や殻作用を入れる場合、法線接合条件が変わり別の候補である。

## 2. 殻で場を接合する：4D方程式と時計・流束

MP外部は

```math
ds^2=-U^{-2}dT^2+U^2d\boldsymbol{x}^{\,2},\qquad \nabla_{\rm flat}^2U=0.
```

`sqrt(-g)=U^2` から、sourceのないところで

```math
\left[-U^4\partial_T^2+\nabla_{\rm flat}^2\right]\phi=0.
```

周波数Ωでは `(flat Delta + Omega^2 U^4) Phi_Omega=0`。
**Uが軸対称であって球対称ではないため、殻間の外部伝達を一つのl=0散乱係数へ置き換えられない。**
殻上でUが一定であることは、その外の領域全体で球面部分波が独立になることを意味しない。

RN内部では

```math
f(r)=1-\frac{2m}{r}+\frac{e^2}{r^2},\qquad
\phi=e^{-i\omega t}\frac{u_{\omega l}(r)}rY_{lm},
```
```math
\frac{d^2u_{\omega l}}{dr_*^2}+
\left[\omega^2-f\left(\frac{l(l+1)}{r^2}+\frac{f'}r\right)\right]u_{\omega l}=0,
\qquad \frac{dr_*}{dr}=f^{-1}.
```

これは [ZLO20] の4D部分波方程式と一致する。lを指定して計算することと、場の理論を2D共形場へ変更することは別である。

殻の共通固有時は `d tau=dT/U0=sqrt(f(A)) dt`。従って

```math
\alpha=\frac{dt}{dT}=\frac1{U_0\sqrt{f(A)}},\qquad \Omega=\alpha\omega.
```

同じ向きの法線をRNからMPへ向け、sourceが殻上にない場合、変分原理の境界項から

```math
[\phi]=0,\qquad
\frac1{U_0}\partial_\rho\phi_{\rm MP}
=\sqrt{f(A)}\partial_r\phi_{\rm RN}.
```

この二つを二点関数の両引数にも課す必要がある。面積・固有時を共有しているので、KGの法線流束は点ごとに保存する。
これだけでは状態の正値性、反対称部（交換子）、Hadamard条件、大域的な自己整合性までは選べない。

## 3. 特異点を避ける粒子軌道だけでは、波の境界データは省略できない

SAのRN内部には `0<r<r_-` の静的領域とtimelike特異点r=0が残る。
そこで空間的波動演算子の自然なHilbert重みとエネルギー形式は

```math
w(r)\,dr=\frac{r^2}{f}\,dr,\quad p(r)=r^2f,
\quad {\cal E}_l[\Phi]=\int_0^{r_-}
\left[p|\Phi'|^2+l(l+1)|\Phi|^2\right]dr.
```

r=0の近くで `r_*~r^3/(3e^2)`、部分波ポテンシャルは

```math
V_l(r_*)\sim-\frac2{9r_*^2}.
```

したがってuの二枝は `r_*^(1/3), r_*^(2/3)`、元の場Φ=u/rでは **定数とrに比例する枝**になる。
両方とも `w~r^4/e^2` に対して局所L²で、上のbulkエネルギーも有限。
「正規化可能」「有限エネルギー」というだけでは片方を捨てられない。
RNで波動演算子の自己共役性と反射係数の関係を調べた先行研究が [MRT78]、一般的な枠組みは [HM95] にある。

境界形式は

```math
p(\overline\Phi\Psi'-\overline\Phi'\Psi)\big|_{0}.
```

例えば `Phi(0)=0` と `p Phi'(0)=0` は、ともにこの形式を零にし、内側静的領域で非負なエネルギー形式を持つ別々の実現である。
**両者が全SA時空へ整合的に延長できると証明したわけではない。** 大域条件が片方を選ぶ、あるいは両方を拒否する可能性も未判定。
r=0を新しい反射装置として実装できるとも主張しない。

### 3.1 零周波数での厳密な違い

l=0の静的方程式は `(p Phi')'=0`。二つの解を

```math
\Phi_N=1,\qquad
\Phi_D=\frac1{r_+-r_-}\ln\frac{r_-(r_+-r)}{r_+(r_--r)}
```

と取れる。内側地平面へ近づくと、前者のuは定数、後者はr_*に比例する。
このため連続スペクトルの小さい正周波数での反射位相は、それぞれ **+1と−1** に近づく。
単色モード自体を正常化された粒子状態と呼ばず、これは波束構成に使う散乱データとする。

### 3.2 有限周波数を数値計算

`s=-ln(1-r/r_minus)` とおくと、元の場Φのl=0方程式はr=0でも通常のODEになる。

```math
\Phi_{ss}=\frac{h}{r_+-r}\Phi_s
-\frac{\omega^2r^4}{(r_+-r)^2}\Phi,
\qquad h=r_-e^{-s},\quad r=r_--h.
```

基底を `exp(±i nu s)`、`nu=omega/(2 kappa_minus)` としてs=50まで積分した。
以下は**反射振幅の偏角（rad）**で、過去へ届く確率ではない。

| omega/kappa_minus | Dirichletの位相 | Neumannの位相 |
|---:|---:|---:|
| 0.02 | 3.140089816259 | -0.041969908427 |
| 0.2 | 3.114690441397 | -0.417534214855 |
| 2 | 1.018201916234 | 2.678728763542 |

同じ入力波・同じ場の方程式でも、境界の選択が位相感応測定へ影響する。
ただし |R|=1 の位相変化だけでは、最適な復号後の通信能力が失われたことを意味しない。既知の位相なら較正可能。
また、ここで計算したのは **内側静的RN領域の散乱**。S1からS2までの完全な伝達振幅ではない。

50/80桁の二回の積分は最大差 `1.45e-43` 未満。
別プログラムは元のSturm形式をCayley midpoint＋Richardsonで積分し、最大差 `4.29e-12` 未満で照合した。
s=50以遠については、回転生成子からの摂動のGronwall評価により、反射振幅の残差に `1.64e-21` 未満の解析的上限がある。
**この末尾上限と、数値ODE全体の丸め・打切り誤差保証は別。後者の厳密区間証明はしていない。**

### 3.3 外側から内側までの零周波数接続も単なる減衰ではない

RNの両地平面の間で、l=0、外側の入射基底を `exp(-i omega r_*)` とすると、内側の二枝は

```math
B_0=\frac12\left(\frac{r_-}{r_+}+\frac{r_+}{r_-}\right),\qquad
C_0=\frac12\left(\frac{r_-}{r_+}-\frac{r_+}{r_-}\right),\qquad B_0^2-C_0^2=1.
```

指定例では `B0=7, C0=-4 sqrt(3)`。これは零周波数の接続係数。
**49や48を透過確率へ変換してはいけない。** 地平面間ではrが時間的で、量子共分散・両枝の相関を別に供給する必要がある。
この計算にもMP外部のモード混合は含まれない。

## 4. 一つの平衡状態で全経路を覆う試みは通らない

ここで初めて追加の状態仮定を置く：

- 同じ静的Killing時計に対する**一つの**逆温度beta。
- 中性自由場の、Euclidean解析接続で与えるKMS平衡状態を各静的領域で使う。
- 両方の非退化な分岐地平面を二側からHadamardに覆うことを要求。

局所の4D計量の法線二平面はEuclidean化すると `d rho²+kappa² rho² dt_E²`。
滑らかな原点には `beta*kappa=2pi` が必要。[SW15] の静的分岐地平面・HHI構成はこの必要条件の根拠と範囲を説明している。
**同論文の存在定理を、非大域双曲なSA全体へ適用してはいない。**

共通のMP時計で表面重力を測ると

```math
\kappa_\pm^{(T)}=\alpha\frac{r_+-r_-}{2r_\pm^2},\qquad
\frac{\kappa_-^{(T)}}{\kappa_+^{(T)}}=\left(\frac{r_+}{r_-}\right)^2>1.
```

指定例では

```text
kappa_plus^(T) R  = 0.69408557088274257
kappa_minus^(T) R = 134.64902289551016
ratio             = 97 + 56 sqrt(3) = 193.99484522385713
```

一つのbetaが両方の正則条件を満たすことはできない。
殻の時計の倍率は両者へ同じように掛かり、倍率の選び直しでは救えない。
これは**この単一平衡ansatzのC判定**。Unruh型、非平衡、非定常、片側の地平面しか要求しない状態、極限RNは別途検討が必要。

[ZLO20] は通常のRNで特定状態のRSET流束を計算している。そこで得られる数値を、今回の二殻境界と特異点境界を持つ状態へ移していない。
今回、全SAのmode-sum RSETは未計算。

## 5. 送信0・1と、有限時間の記録をどう結ぶか

### 5.1 等エネルギーの符号化と、受信器の落とし穴

適切な共通ゼロ平均Gaussian状態と、同じ応答作用素が**存在すれば**、sourceの±符号は平均場を±varphiに変え、connected二点関数は変えない。

```math
\langle\phi\rangle_b=(-1)^b\varphi,\qquad W_b^{\rm conn}=W_0,
\qquad \langle T_{ab}\rangle_b=\langle T_{ab}\rangle_0+T_{ab}[\varphi].
```

よって0/1の平均応力は同じ。しかし背景状態のconnected二点関数が地平面で不適合なら、滑らかなcoherent変位を加えても修復しない。
平均応力の一成分の相殺だけを、Hadamard状態の構成と同一視しない。

さらに、基底状態から始める通常のUDW検出器で**エネルギー／励起だけを読む**と、この符号化は見分けられない。
場のparityと検出器のZを同時に掛けると、相互作用とエネルギー測定は不変、ビットだけが反転する。
parity不変の共通背景状態の下では全次数で `P_energy(.|0)=P_energy(.|1)`。
これはこの符号＋読出し方式のCであり、光や場が通らないという主張ではない。

### 5.2 有限時間の位相感応Ramsey受信器

受信器は初期状態 `|+x>`、相互作用中はgaplessとし、有限の固有時区間と空間領域に台を持つhで結合する。

```math
H_R(\tau)=\chi(\tau)\sigma_z\phi(F_\tau),\qquad
\Phi(h)=\int d\tau\,\chi(\tau)\phi(F_\tau).
```

coupling強度はhへ含める。自由場の交換子がc-number、`sigma_z²=I` なので、時間順序による第二Magnus項は結果に影響しない全体位相。
有限時間でも受信unitaryは `U_R=exp[-i sigma_z Phi(h)]` と同じ読出し統計を与える。
この仕組みは [TG22] の場と検出器を用いる情報通信研究と関連するが、同論文の大域双曲性をCTC領域へ移してはいない。

**物理的な共通応答核とGaussian二点関数が得られた場合に限り**

```math
m_h=\int h(x)G_{\rm resp}(x,x')j(x')\,d{\rm vol}_x d{\rm vol}_{x'},\qquad
V_h=\langle\Phi(h)^2\rangle_{0,\rm conn}
```

から、y=±1のsigma_y測定と選択ビット記録R=bについて

```math
\boxed{P(R=b,Y=y)=\frac{p_b}{2}
[1+y(-1)^b e^{-2V_h}\sin(2m_h)]},
```
```math
D_Y=e^{-2V_h}|\sin(2m_h)|.
```

を得る。全結果を含み、事後選別しない。
**G_respという名前は、CTC上の応答処方を新しく選んだものではない。** 実験全体から導くべき未取得の作用素の記号。
場の接合だけを満たす任意のGreen関数を代入すればよい、とはしていない。
任意の一周回路へ上式をそのまま貼り合わせてもいない。

現時点では全SAの `m_h,V_h` はともに未取得。式が閉じた形であることを、全SAの二つの実験を計算したことにはしない。
台帳の `P_Y_do_0,P_Y_do_1,D` はnullのまま。

### 5.3 雑音を任意に置かないための、独立した4D対照

4D Minkowski真空の慣性点状受信器、`chi(t)=sin^4(pi t/T)` (0<t<T) の分散を、実際のWightman関数から求めると

```math
V_{\rm flat}=\frac1{4\pi^2}\int_0^\infty dk\,k\left|\int_0^Tdt\,\chi(t)e^{ikt}\right|^2
=0.08317814081012577966\ldots.
```

同じ値を時間領域の `-int int chi'(t)chi'(t') log|t-t'|/(4pi²)` から別計算した。
周波数128pi/Tより上の積分は正で、上限 `2.048e-16` を持つ。50/80桁比較も実施。
時間は有限、点状結合は理想化、C³スイッチは適切なsmooth近似の極限で扱える。
**この値は局所4Dの雑音対照であり、SAの地平面を含むV_hへ代入していない。**
現実の装置の空間的な広がり、gap制御、電源・記録の応力もこの対照では供給していない。

## 6. 再開点

優先対象は、追加の安定点の走査ではなく次の連立問題：

- 二殻・RNの残る特異境界・全ての必要な入射データを含むKG伝播。
- 正値性と交換関係を満たし、実験が通る地平面で正則な**非平衡候補状態**。
- その同じ状態のRSETとバックリアクション、有限送信sourceとRamsey受信記録。

D/N境界は勝手にビットごとに選ばず、実装または基礎理論から共通に定める必要がある。
今回の単一平衡Cを除いても、B全体が肯定されたわけではない。

## 7. 再現・検証・GitHub状態

```bash
python -m pip install -r architecture/requirements.lock
python scripts/test_architecture_search.py
python scripts/sa_quantum_verify_v4.py --tests
mkdir -p /tmp/sa-v4
python src/symbolic/sa_quantum_junction_v4.py > /tmp/sa-v4/junction.json
python src/numerical/sa_inner_scattering_v4.py --output /tmp/sa-v4/scattering.json
python scripts/sa_quantum_verify_v4.py --junction /tmp/sa-v4/junction.json --scattering /tmp/sa-v4/scattering.json --output /tmp/sa-v4/verification.json
python scripts/sa_quantum_report_v4.py --evidence /tmp/sa-v4 --tests
python scripts/sa_quantum_report_v4.py --evidence /tmp/sa-v4 --output /tmp/sa-v4/verified --gate
```

量子状態・境界条件・source・装置を変えて再開する場合は別の入力記録とする。
この版の未取得確率を埋めるだけでは、元のA判定を通らない。

ローカルPython3.13.5 / SymPy1.14.0 / mpmath1.3.0。
元のA判定を変更せず、原49テスト、新規物理12テスト、新規報告12テストが成功した。
別計算器は元の生成器をimportせず、入力・コードのSHA256と全候補の未取得確率を照合する。
別プログラム検証も同じAIが作成。独立研究者の査読・Lean・全130研究計算・remote CIは未実施。

本セッションのGitHubは読取操作のみ。`git ls-remote` もDNS失敗したため、コミット・PR・mergeは実施していない。
最新mainを再確認し、作業中にマージされたPR #22のREADME追記をbyte単位で保持したうえで、
新main基点の適用パッチを納品する。PR #22の科学的構成やファイルを上書きしない。

## 8. 実在する出典と借りた範囲

- **[S96]** F. Schein, P. C. Aichelburg, *Traversable Wormholes in Geometries of Charged Shells*, Phys. Rev. Lett. **77**, 4130–4133 (1996). https://arxiv.org/abs/gr-qc/9606069 ; DOI 10.1103/PhysRevLett.77.4130. 二殻の幾何・固有時接合・同一外部の因果構造。量子通信の完成を示す論文ではない。
- **[MRT78]** M. Martellini, C. Reina, A. Treves, *Klein-Gordon field in a naked-singularity background*, Phys. Rev. D **17**, 2573 (1978). https://doi.org/10.1103/PhysRevD.17.2573. RNの波動演算子と反射への境界条件の問題。今回は公開abstractを確認し、内側静的領域のendpoint解析と数値は独自に再導出した。
- **[HM95]** G. T. Horowitz, D. Marolf, *Quantum Probes of Spacetime Singularities*, Phys. Rev. D **52**, 5670–5675 (1995). https://arxiv.org/abs/gr-qc/9504028. 特異点での量子発展と自己共役性という枠組み。全SAの状態の存在定理として使わない。
- **[SW15]** K. Sanders, *On the construction of Hartle-Hawking-Israel states across a static bifurcate Killing horizon*, Lett. Math. Phys. **105**, 575–640 (2015). https://arxiv.org/abs/1310.5537. 分岐地平面と熱的正則性・その仮定。大域双曲な存在定理をSA全体へ適用しない。
- **[ZLO20]** N. Zilberman, A. Levi, A. Ori, *Quantum fluxes at the inner horizon of a spherical charged black hole*, Phys. Rev. Lett. **124**, 171302 (2020). https://arxiv.org/abs/1906.11303. 4D部分波方程式とRNの特定状態のRSET。流束係数の二殻への流用なし。
- **[TG22]** E. Tjoa, K. Gallock-Yoshimura, *Channel capacity of relativistic quantum communication with rapid interaction*, Phys. Rev. D **105**, 085011 (2022). https://arxiv.org/abs/2202.12301. Weyl/Gaussian型の場・検出器通信の参考。今回の有限時間gapless測定はc-number交換子から再導出した。論文のCTC非存在領域という仮定を除去した証明ではない。

文献確認日2026-09-24。PDF本文テキストを使用。Sanders論文の先頭ページは描画も確認したが、
SA論文の図のscreenshot取得は失敗した。SAのPenrose図の新たな目視検証・全大域経路の数値再現は主張しない。
上の新しい数値は図から読み取ったものではない。
