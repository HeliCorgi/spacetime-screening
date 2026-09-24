# 四次元の量子支持源と、同じ外部空間の過去向き経路

**2026-09-24。基点 `2304cbc39b638491d20cb9ece2f44b05bb216426`（PR #21のマージ後）。**
[原プロトコル](../docs/4d-past-signalling-protocol.txt)と[前回RNノート](rn-a-target-candidate.md)を引き継ぐ。

## 1. 結論と、混ぜてはいけない二つの模型

**今回の追加分類は A=0 / B=1 / C=1。人間が制御可能な過去通信路は未構成。**

| ID | 判定 | 今回得たもの |
|---|---|---|
| `mp-same-exterior-handle` | B | 同じ外部空間の二口をつなぐ、真の古典的帰還経路。四次元の電磁場・角度依存する殻の応力と電荷・接合収支まで計算。ただし負の荷電殻と時間差は入力 |
| `rn-smooth-conformal-source` | C | 明記した滑らかなRN形状を、中性の自由共形量子場だけで支える案は、遠方のtrace方程式のべきが合わず不成立 |

**Cの形状とBの接合は異なる幾何である。両者の部分的成果を掛け合わせてAにしない。**
Aの定義・原validator・人間審査の条件は変更しない。
未取得の `P(Y|do(0))`、`P(Y|do(1))`、過去の識別度は全てnullで保存する。

## 2. 文献から借りた部分と、今回組み立てた部分

[Maj]の静電的Einstein–Maxwell解、[V89]のcut-and-paste法、[SA96]の同じ漸近領域へ戻る荷電ワームホールを参照する。
**[SA96]の内部はRNブラックホールで、内側Cauchy地平面を含む。今回その内部は使わない。**
その論文の「エネルギー条件を破らない」という結果も、今回の殻へ移さない。
今回は、等しい二中心のMP外部の二つの境界を直接同一視する別の分布的構成であり、必要な負の源を明示する。

[ABOPT25]には四次元RN上のBoulware真空の繰込み応力を計算するmode-sum手法と、先頭の静的反作用がある。
しかし、ブラックホール背景の状態・境界条件は、新しい滑らかな喉や時間差付き接合のものではない。
**その数値や係数を新背景へ流用して「量子支持を完成」とはしない。**
支持源の検査には、[Duff]の四次元の状態非依存trace anomalyを、明記した中性自由共形場に適用する。
以下の滑らかさの選択、二中心直接接合、具体的光路、残差と照合は今回の計算である。

## 3. 有限厚さRN：幾何が要求する全応力

自然単位 `c=hbar=1`、球対称性はこの模型にだけ課す。

```math
ds^2=-f(r(x))dt^2+\frac{dx^2}{f(r(x))}+r(x)^2d\Omega^2,
\qquad r(x)=a+\sqrt{x^2+\epsilon^2}-\epsilon,
\qquad f(r)=1-\frac{2M}{r}+\frac{Q^2}{r^2}.
```

`epsilon>0`、`a>r_+=M+sqrt(M^2-Q^2)`、`M>0`、`0<=Q^2<=M^2`。
全実数xに滑らかで、喉はx=0、保持領域にf=0はない。二つの漸近平坦端を持ち、時間の同一視はしない。
**これは支持物質を得るための指定形状で、既に量子論で実現した計量ではない。**

`v=r'(x), w=r''(x), f_r=df/dr` と書く。正規直交枠の全Einstein応力は

```math
8\pi G\rho=\frac{1-fv^2-2frw-rf_rv^2}{r^2},\qquad
8\pi Gp_r=\frac{-1+fv^2+rf_rv^2}{r^2},
```
```math
8\pi Gp_\perp=\frac{f_{rr}v^2+f_rw}{2}+\frac{f_rv^2}{r}+\frac{fw}{r}.
```

ここで `2frw` は積 `2*f*r*w` である。
径方向の古典Maxwell場は

```math
8\pi G T^{\rm EM}_{\hat a\hat b}
=\frac{Q^2}{r^4}\mathrm{diag}(1,-1,1,1).
```

その差を、必要な追加支持源の**密度・径圧・横圧全部**として記録する。
保存則 `p_r'+(f'/2f)(rho+p_r)+2r'(p_r-p_perp)/r=0` を差の源についても検算した。
直接Christoffel/Ricci計算と、独立な曲率断面式による検算を行う。

### 3.1 負のnull積分は平滑化で消えない

```math
\rho+p_r=-\frac{f r''}{4\pi G r}<0.
```

漸近Killing energy E=1で規格化した径方向null線では `dx/dlambda=1` だから、

```math
\int T_{ab}k^ak^b\,d\lambda
=-\frac1{4\pi G}\int_{-\infty}^{\infty}\frac{r''}{r}\,dx
=-\frac1{4\pi G}\int_{-\infty}^{\infty}\frac{r'^2}{r^2}\,dx<0.
```

後の等号は部分積分で、両端のr'/rは零。
別検証器は前者ではなく、Raychaudhuriのexpansion二乗に対応する後者を積分する。
`epsilon -> 0` では `-1/(2 pi G a)` となり、前回の薄殻の規格化と一致する。
この負値の存在だけで、全ての量子場の禁止にはしない。

### 3.2 状態を選び直しても解けない、指定形状のtrace障害

Ricci scalarは厳密に

```math
R=\frac{2(1-r'^2)}{r^2}-\left(f_r+\frac{4f}{r}\right)r''.
```

`r'^2=1-epsilon^2/(r-a+epsilon)^2`、`r''=epsilon^2/(r-a+epsilon)^3` を代入すると、片側遠方で

```math
\lim_{r\to\infty}r^4R=-2\epsilon^2,\qquad
\lim_{r\to\infty}r^6\Box R=-24\epsilon^2,
\qquad
\lim r^6 C_{abcd}C^{abcd}=\lim r^6 E_4=48M^2.
```

`E_4=Riemann^2-4Ricci^2+R^2`。
前方計算のareal-radius極限と、別検証器のx座標のLaurent展開を照合する。

**ここで検査する源のクラスは限定する。**
有限個の中性・自由・質量ゼロの共形scalar、中性自由Dirac、独立した自由Maxwell場のみ。
境界・支持材・荷電場の相互作用・その他のtraceを持つ物質は入れない。
局所Hadamardな許容状態では、[Duff]の式より

```math
\langle T^a{}_a\rangle_{\rm ren}
=\frac{c_W C_{abcd}C^{abcd}-a_E E_4+\beta\Box R}{16\pi^2}.
```

`c_W=(N_s+6N_D+12N_v)/120`、`a_E=(N_s+11N_D+62N_v)/360`。
betaは任意の有限の繰込み規約に依存する係数を許す。四次元の局所曲率二乗項のtraceもBox Rへまとめられる。
漸近平坦性に合わせrenormalized Lambda=0、G有限とする。
古典Maxwell応力はtracelessなので、必要なtrace方程式の両側は

```math
-\frac{R}{8\pi G}
=\frac{\epsilon^2}{4\pi G r^4}+O(r^{-5}),\qquad
\langle T^a{}_a\rangle_{\rm ren}=O(r^{-6}).
```

**epsilon>0でr^-4係数が一致しない。したがって指定した形状は、この源のクラスでは半古典方程式を解けない。**
個々のGaussian状態やBoulware状態を選んだ失敗ではない。
有限のNやbetaを増やしても、固定した一つの模型の遠方のべきは変わらない。

**このCを荷電・相互作用場へ拡大しない。** ゲージ場との相互作用があれば、traceにbeta関数とF^2による項が現れ、ここではr^-4に寄与し得る。
質量、非共形結合、境界、支持物質、別の計量関数も今回の仮定外。
全量子状態・全RN近傍・全四次元ワームホールの禁止ではない。

### 3.3 否定の負例：計量を応答させれば、この一点の障害は外せる

同じr(x)のまま遠方のlapseに

```math
\delta f(r)=\frac{2\epsilon^2\log(r/L)}{r^2}
```

を加えると、`lim r^4 R_new=0` になることを厳密に確認した。
**これはtraceの先頭項を合わせる修正案であって、全半古典解ではない。**
元のRN lapseを固定したCの適用範囲が、計量の応答を許す問題とは違うことを示す。

### 3.4 支持場と、信号のtest fieldの健全性も分ける

同じ滑らかな計量上で、別のminimally coupled scalarを調べる。
角運動量l、質量m_phiを残して四次元KG方程式を分解すると、`dr_*/dx=1/f` について

```math
V_l=f\left[\frac{l(l+1)}{r^2}+m_\phi^2+
\frac{f_r r'^2+f r''}{r}\right]\ge0.
```

外部でf>0、f_r>0、r''>0、m_phi^2>=0なので、標準の自己共役境界条件の空間作用素は非負。
そのtest fieldには負の固有値による指数成長モードはない。
**これは背景を支える量子源の構成でも、全重力摂動の安定性でも、共形scalarの結果でもない。**

## 4. 同じ外部空間の二口：四次元MPの直接接合

前回の、二つの独立した外部の一回の接続では一定時計差を消せた。
今回は、その前提を明示的に変える。二つの口は**同じ一つの外部空間**にある。

```math
ds^2=-U^{-2}dt^2+U^2d\mathbf X^2,\qquad
U=1+\frac m{r_+}+\frac m{r_-},\qquad
r_\pm=\left|\mathbf X\mp\frac d2\hat z\right|.
```

`m>0`、中心の距離d、各中心から座標半径aの球を除く。`d>2a>0`。
電磁場はGaussian規約 `L_EM=-F^2/(16pi)`、`A_t=1/(sqrt(G) U)`。
中心の特異点・地平面を除去した外部では、U>0かつflat Laplacian U=0。
これはRN計量を足した近似ではなく、正確なEinstein–Maxwell外部解[Maj]である。
コードでは一般のU(x,y,z)から全Einstein成分とMaxwell方程式を計算し、残差がLaplacian Uだけになることを確認する。

二つのtimelike境界を、z反射と

```math
t_{\rm right}=t_{\rm left}+\Delta
```

で同一視する。等しい二中心は反射対称だから、時刻成分・角成分を含む第一基本形式が一致する。
**Uは境界上で角度依存する。平均して球対称のRN殻に置き換えない。**
これはΔを入力した永続的な接合模型で、有限の操作でΔを形成した解ではない。

### 4.1 角度依存を含む殻の応力・電荷・力の釣り合い

一つの中心から他方へ向く極軸を取り、`u=cos(theta)`、

```math
s=\sqrt{d^2+a^2-2da u},\quad U=1+m/a+m/s,
\quad U_n=-m/a^2-m(a-du)/s^3.
```

nの向きは各境界から保持する外部へ向かう向き。
混合成分の外的曲率は

```math
K^t{}_t=-U_n/U^2,\qquad
K^\theta{}_\theta=K^\phi{}_\phi=1/(Ua)+U_n/U^2.
```

Israel条件とMaxwell jumpから、接合面を一回数えた源は

```math
\sigma=-\frac{U+aU_n}{2\pi G U^2a},\qquad
p=\frac1{4\pi G Ua},\qquad
q_s=-\frac{U_n}{2\pi\sqrt G U^2}.
```

```math
U+aU_n=1+\frac{m(d^2-da u)}{s^3}>0,
\qquad \sigma<0,\qquad \sigma+2p=q_s/\sqrt G.
```

q_sは選んだA_tの符号の表面固有電荷密度。bulkの向きを逆に選べば電荷の符号も逆になる。
分布的な殻のstressだけでなく電磁場のsurface currentを含める。
接線方向のWard関係は

```math
\partial_\theta p+(\sigma+p)\partial_\theta\log(U^{-1})
=\frac{U_n U_\theta}{2\pi G U^3}.
```

右辺は電磁jumpによる力であり、落とせば角方向の釣り合いが失われる。
反射対称な接合は法線方向の平均外的曲率・bulk stressの差も整合する。
**この源は幾何から求めた負の荷電殻で、正常な量子状態から供給した物質ではない。**

### 4.2 一つの源としての収支

実際の角度依存の面積要素 `U^2 a^2 dOmega` で積分すると、

```math
E_{\rm shell,proper}=-\frac{2a}{G}(1+m/d),\qquad
Q_{\rm shell}=\frac{2m}{\sqrt G},\qquad
M_{\rm ADM}=\frac{2m}{G}.
```

同一視した殻を二回数えない。最後のADM値はUの一つの無限遠での漸近係数による。
負のproper energy、電磁場のエネルギー、ADM質量を単純に足して製造予算としない。
負の源を作る装置、電荷の保持、pump、時間差準備、有限厚さ化の全収支は未供給。

### 4.3 同じ時計へ戻る、明示した光の経路

向かい合う二つの球面点を、外部の対称軸に沿って結ぶ。
左中心からの距離sはaからd-aまで動き、径方向null条件から

```math
T_{\rm axis}=\int_a^{d-a}\left(1+\frac m s+\frac m{d-s}\right)^2ds
```
```math
=d-2a+4m\log\frac{d-a}{a}
+m^2\left[2\left(\frac1a-\frac1{d-a}\right)
+\frac4d\log\frac{d-a}{a}\right].
```

右から左への接合横断は-Δ、その後外部を左から右へ未来向きに進むから

```math
t_{\rm return}-t_{\rm send}=T_{\rm axis}-\Delta.
```

**Δ>T_axisは、この特定経路で過去へ帰還する十分条件。T_axisが大域的な最短経路とは証明していない。**
したがってΔ<T_axisを「CTC無し」の必要十分判定に使わない。
Δ=0ではtが大域的に貼り合うため、明示的な未来向き対照になる。
接合を越える時間差は外部に既にある同じ時刻の基準と比較され、別宇宙の時計原点の付け替えでは消せない。

単位長L0を用い `m=L0, a=.1L0, d=10L0, Delta=60L0` とすると、

| 量 | 値（c=1） |
|---|---:|
| T_axis/L0 | 49.81650713857199365794868963 |
| 面上のU | 11.10101010101010101010101010 |
| (Delta-T_axis)/L0 | 10.18349286142800634205131037 |
| 実験室の固有時の余裕/L0 | 0.91734831053810066229579593 |

最後は `(Delta-T_axis)/U`。秒に直すとL0/cを掛ける。
理想薄殻での通過遅延は零。有限厚さ、readoutや物理的なsourceが生む遅延は含んでいない。
**この表は実現装置の送信成功率でも、形成に必要な時間でもない。**
幾何学的な余裕があり、十分短い局所経路を追加して実験室を接合面から離すことも可能だが、受信器は未構成である。

## 5. Aへ進む際に残る具体的な接続

1. MPの負の荷電殻を有限厚さの四次元量子物質に置換し、その同じ状態の全繰込み応力・電流と計量を連立させる。
2. 所与のΔではなく、有限の準備・制御過程からΔを形成できるかを計算する。途中の地平面、量子揺らぎ、電荷散逸を含める。
3. 同じ全模型の受信器・記憶・送信操作について、無条件の受信分布を比較する。

[ER04]から借りた前回のRN半径方向安定性は、今回の角度依存する荷電接合へ移らない。
四次元sourceのtraceを満たすことも、全応力・局所性・正値性・初期境界条件の代わりにはならない。
原プロトコルのAを満たすまで、BはBとして記録する。

## 6. 検証・再現

```bash
python -m pip install -r architecture/requirements.lock
python scripts/test_architecture_search.py
python scripts/test_architecture_charged_search.py
python scripts/architecture_charged_search.py run --output /tmp/charged/raw
python scripts/architecture_charged_verify.py --records /tmp/charged/raw/candidates.json --output /tmp/charged/verification.json
python scripts/architecture_charged_search.py finalize --records /tmp/charged/raw/candidates.json --verification /tmp/charged/verification.json --output /tmp/charged/verified --gate
```

[候補台帳](../architecture/charged-source-handle-v3.json)から全必須項目・七段階・出典・仮定変更を含むJSONとMarkdownを生成する。
新規25テスト＋元49テスト。37点（RN18、MP19）は50/80桁を相対1e-40で照合。
生成器をimportしない別プログラムは直接の四次元テンソル・数値微分・異なる積分で検査する。
不正なA昇格、欠損、古い証明書、NaN、符号変更、入力hash変更を拒否し、計算失敗を物理的Cへ変換しない。
専用[Actions](../.github/workflows/architecture-charged-completion.yml)はread-onlyで生成と別検証を分離、全結果を保存する。
コード・入力・原プロトコルのhash、実行checkout SHA、Python版を成果物に記録する。

**別実装も同じAIの作成で、独立研究者・別AIの査読ではない。**
CIは実装した検算だけを保証する。解析的な大域接合の論証、全物理の健全性、量子支持源をCIで証明したとはしない。
Lean形式証明は今回実施しない。実際のremote状態とrunはPRの完了記録に残す。

## 7. 実在する一次文献

- **[Maj]** S. D. Majumdar, *A Class of Exact Solutions of Einstein's Field Equations*, Phys. Rev. **72**, 390 (1947), [DOI](https://doi.org/10.1103/PhysRev.72.390)。harmonicな静電的外部解。
- **[V89]** M. Visser, *Traversable wormholes: Some simple examples*, Phys. Rev. D **39**, 3182–3184 (1989), [arXiv:0809.0907](https://arxiv.org/abs/0809.0907), [DOI](https://doi.org/10.1103/PhysRevD.39.3182)。1989年の論文を2008年にarXivへ収録。非球対称のcut-and-pasteと異常源。
- **[SA96]** F. Schein and P. C. Aichelburg, *Traversable Wormholes in Geometries of Charged Shells*, Phys. Rev. Lett. **77**, 4130–4133 (1996), [gr-qc/9606069](https://arxiv.org/abs/gr-qc/9606069), [DOI](https://doi.org/10.1103/PhysRevLett.77.4130)。外部MPのEq.(1)、同じ漸近領域への接続。今回そのRN内部は使わず、正の支持源の主張も継承しない。
- **[Duff]** M. J. Duff, *Twenty Years of the Weyl Anomaly*, Class. Quantum Grav. **11**, 1387–1404 (1994), [hep-th/9308075](https://arxiv.org/abs/hep-th/9308075), [DOI](https://doi.org/10.1088/0264-9381/11/6/004)。四次元traceのEq.(21)–(23)、自由場の係数Eq.(30)–(31)。ゲージ相互作用の項を無視して適用範囲を広げない。
- **[ABOPT25]** J. Arrechea, C. Breen, A. Ottewill, L. Pisani, P. Taylor, *The renormalized stress-energy tensor for scalar fields in the Boulware state with applications to extremal black holes*, Phys. Rev. D **111**, 085009 (2025), [arXiv:2409.04528v2](https://arxiv.org/abs/2409.04528v2), [DOI](https://doi.org/10.1103/PhysRevD.111.085009)。四次元RSET手法の監査。RNの状態・数値を新しい喉へ流用せず、今回このmode-sumの再実装は行わない。
- **[ER04]** E. F. Eiroa and G. E. Romero, *Linearized stability of charged thin-shell wormholes*, Gen. Relativ. Gravit. **36**, 651–659 (2004), [gr-qc/0303093](https://arxiv.org/abs/gr-qc/0303093)。前回の球対称RN安定化との比較だけに用いる。

閲覧日2026-09-24。本文の式・解析を参照し、図の読取りによる値は使っていない。
