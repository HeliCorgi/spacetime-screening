# A候補を探す：四次元の電荷付き薄殻と、量子支持・時計接続の検査

**2026-09-24。基点main: `89f55b1e3f559c7ffffd0665ce520816f122d52e`。**
[原プロトコル](../docs/4d-past-signalling-protocol.txt)のA基準は変更しない。
[初回バッチ](architecture-search-batch-v1.md)を上書きせず、肯定側へ進める新しい支持部品を探索した。

## 結論

**Aは未発見。追加の二つの記録はA=0 / B=1 / C=1。**
電荷による安定化を使うと、前回のSchwarzschild薄殻と違い、EOS勾配を4へ緩めなくても半径方向に安定な四次元の古典接合がある。
これは既知の[ER]・[E08]の機構を再現・具体化した結果で、新しい安定化原理の発見とはしない。
正常な量子物質と過去への制御可能な通信路まで完成したわけではない。

| 記録 | 分類 | 直接の根拠 |
|---|---|---|
| `rn-causal-slope-support` | **B（支持部品）** | 0<=eta<=1でも安定な領域、非極限の具体点、厳密な開領域の証明。ただし繰込み量子源・全装置・実際の時間機械化は未構成 |
| `rn-single-seam-offset` | **C（指定経路）** | 別々の二つの外部を一度だけつなぐ一定時計差は大域的時間関数を壊さず、過去通信にならない |

1,890組を厳密有理数で検査。外部領域の条件を満たす1,620組中179組が半径方向に安定で、270組は定義域不適合として除外した。
**除外を物理的Cの新候補として数えず、179/1620を自然界の成功確率とも解釈しない。**
加えて時計の15対照と、極限への4系列の資源・時間評価を行った。

## 1. なぜこの経路を選んだか

前回のSchwarzschild薄殻では0<=eta<=1の半径方向安定性に障害があり、eta=4で部分的に残った。
[ER]・[E08]は電荷がこの安定領域を広げることを示す。今回は一般相対論を変更せず、四次元Maxwell場を加える。
**etaはまずdp/dsigmaであり、数値が1以下というだけで物質の信号速度や完全な健全性は認定しない。**

変更は台帳に記録した：Q=0からQ!=0、eta=4から[0,1]、構成則の比較として表面P(X)を追加。
地平面を除く切り貼りという初期位相は仮定のままである。物理的な形成を解いたものではない。

## 2. 完全な3+1次元の幾何と必要源

以下c=1、M,Qは長さの次元を持つ幾何学パラメータ。応力式にはGを明示する。
二つのReissner–Nordstrom外部をr=a0で接続する：

```math
ds^2=-f(r)dt^2+f(r)^{-1}dr^2+r^2d\Omega_2^2,
\qquad f(r)=1-\frac{2M}{r}+\frac{Q^2}{r^2}.
```

|Q|<=Mではa0>r_plus=M+sqrt(M^2-Q^2)のみを採用。保持した領域に裸の特異点・地平面はない。
Qは半径方向摂動中に固定する。殻を中性とし、連続する法線方向の電場を選ぶので、両端の外向き電荷は符号が逆になる。
proper-radial座標lで `F_tl=Q sqrt(f)/r^2` とすると、`sqrt(-g) F^{lt}=Q sin(theta)` は連続で、殻のdelta電荷は不要。

四次元の全Einstein成分は

```math
G^\mu{}_\nu=\frac{Q^2}{r^4}\,\mathrm{diag}(-1,-1,1,1),
\qquad
(\rho,p_r,p_\perp)_{\rm EM}=\frac{Q^2}{8\pi G r^4}(1,-1,1).
```

生成器の球対称式と、別プログラムの四次元Christoffel・Ricciの直接計算を照合した。
角方向と面積4pi r^2を保持しており、二次元の共形場で支持を置き換えたものではない。

[ER]・[E08]のIsrael接合を使うと、静的殻は

```math
\sigma_0=-\frac{\sqrt{f_0}}{2\pi G a_0},\qquad
p_0=\frac{1-M/a_0}{4\pi G a_0\sqrt{f_0}}.
```

**これは幾何が要求する表面源で、正常な量子状態の繰込み応力として供給済みではない。**
薄殻という分布的古典近似を、滑らかな四次元の半古典解と混同しない。

## 3. 因果的な範囲の構成則で、半径方向安定性を回復する

局所的なaffine EOS `p=p0+eta(sigma-sigma0)` と保存則を使う。

```math
\sigma'=-\frac{2(\sigma+p)}a,\qquad
V(a)=f(a)-(2\pi G a\sigma(a))^2,\qquad \dot a^2+V(a)=0.
```

mu=M/a0, z=Q^2/a0^2, f0=1-2mu+zとおくと

```math
H\equiv a_0^2V''(a_0)
=-4\mu+6z-\frac{2(\mu-z)^2}{f_0}
-2(1+2\eta)(1-3\mu+2z).
```

半径方向の線形安定の条件はH>0。[E08] Eq.(37)のDelta=-V''/2とも一致する。
Q=0へ戻すと、初回バッチのPoisson–Visser式を厳密に再現する。

極限電荷z=mu^2では因数分解される：

```math
H=2(1-\mu)(4\eta\mu-2\eta-1).
```

よって `1/2<eta<=1` では `(2eta+1)/(4eta)<mu<1` に安定域がある。
mu=1そのものはlapseが零になるので採用しない。eta<=1/2では、この極限電荷枝の0<mu<1に安定域はない。

### 非極限でも成立する具体点

```math
\mu=\frac9{10},\quad z=\frac{8099}{10000},\quad\eta=\frac34,
\qquad f_0=\frac{99}{10000},\qquad r_+/a_0=\frac{91}{100},
\qquad H=\frac{10097}{495000}>0.
```

M^2-Q^2=a0^2/10000>0であり、極限点のみに依存しない。
さらに次の箱全体で、外部条件・非極限条件・H>0・sigma+p>0を有理数区間演算で保証した：

```text
mu  in [0.899999, 0.900001]
z   in [0.809899, 0.809901]
eta in [0.7499,   0.7501]
```

生成器のH下限は `32595686839/1649500000000>0`。
別検証器はN=f0 Hを単位立方体のBernstein基底へ変換し、18係数の全てが正であることから
`H>=32678155241/1650500000000>0` を独立に得た。
これは丸めが小さいという主張ではなく、明示した開領域の存在証明である。

### 別計算による照合

b=p0-eta sigma0とおいて保存則を先に積分すると

```math
\sigma(a)=\left(\sigma_0+\frac{b}{1+\eta}\right)
\left(\frac{a_0}a\right)^{2(1+\eta)}-\frac{b}{1+\eta}.
```

これをポテンシャルへ戻し、50/80桁の数値二階微分を元のHと比較した。
別に、Israelの圧力式から直接得る加速度のJacobianが-V''/2になることを検査した。
**小摂動の半径方向安定性以上の結論は出さない。** 非球対称モード、殻の内部自由度、荷電粒子の生成、信号投入と時間差形成は未計算。

## 4. 正の運動項を持つ表面の式は書けるが、量子支持源はまだ足りない

形式的な表面有効作用として `X=-h^{ij}partial_i phi partial_j phi/2>0` とし、

```math
P(X)=C(X/X_0)^\alpha+B,\qquad
\sigma=2XP_X-P,\qquad
c_s^2=\frac{P_X}{P_X+2XP_{XX}}=\frac1{2\alpha-1}.
```

alpha=(1+1/eta)/2、C=(sigma0+p0)/(2alpha)>0、B=p0-Cを選ぶと、X=X0で必要なsigma0,p0とEOS勾配を合わせられる。
具体点ではalpha=7/6、P_X>0、P_X+2XP_XX>0となり、**この仮定した表面作用の内部音波**には正の運動項とc_s^2=3/4がある。

しかしB>0はエネルギー密度への**負の定数寄与**である。その四次元量子起源、境界・支持材・準備を作っていない。
埋込みや重力と結合した全摂動の健全性も、上の内部モードの検査では保証されない。
この作用を用意しただけで「正常な量子物質が見つかった」とはしない。

四次元の通常の古典canonical scalarでは、任意のポテンシャルUに対して

```math
T_{ab}k^ak^b=(k^a\nabla_a\phi)^2\ge0.
```

Uを負にするだけでは、次節の負の径方向null積分を供給できない。
**これは古典canonical scalarとMaxwellのみという完成案の障害で、量子場や一般物質への禁止ではない。**
また、ここに四次元平坦時空のQEIを無条件に適用してはいない。

## 5. 源の負値を小さくする極限にも、残る収支がある

### 殻と電磁場を別々に数える

殻のproper energyと、両側外部の電磁場のKilling energyは

```math
E_{\rm shell}=-\frac{2a_0\sqrt{f_0}}G,\qquad
E_{\rm EM,Killing}=\frac{Q^2}{Ga_0}.
```

これをそのままADM質量へ足すのは誤りで、圧力と重力の寄与がある。
圧力を含むKomarの収支は

```math
K_{\rm shell}=4\pi a_0^2\sqrt{f_0}(\sigma_0+2p_0)
=\frac{2(M-Q^2/a_0)}G,
\quad K_{\rm EM}=\frac{2Q^2}{Ga_0},
\quad K_{\rm shell}+K_{\rm EM}=\frac{2M}G.
```

二つの漸近端の質量に対応する恒等式を検査した。これは必要源の収支で、形成ポンプや実際の有限装置の予算を供給するものではない。

### 正規化したnull積分は電荷で消えない

両端でKilling energy E=1の径方向null geodesicを使う。
殻を横切るとき、正規直交成分k^t_hat=1/sqrt(f0)、k^l=1/sqrt(f0)である。
`T_shell=S delta(l)` をaffine parameterで積分すると

```math
\int_\gamma T_{ab}k^ak^b\,d\lambda
=\frac{\sigma_0}{\sqrt{f_0}}
=-\frac1{2\pi G a_0}.
```

Maxwellの径方向null成分は零。別実装ではRaychaudhuri方程式と、両側のexpansion二乗の積分から同じ値を得た。
**殻のproper energyを電荷調整で零へ近づけても、この正規化したnull積分は零へ近づかない。**
この事実だけで全ての量子支持源を排除するわけではない。

### 時間と負のproper energyのトレードオフ

Q=M、epsilon=1-M/a0>0として、両側r=2a0間の径方向光学的時間を測る。

```math
\frac{T_{\rm opt}}{a_0}
=2\left[1+2(1-\epsilon)\ln\frac{1+\epsilon}{\epsilon}
+(1-\epsilon)^2\left(\frac1\epsilon-\frac1{1+\epsilon}\right)\right].
```

| epsilon | T_opt/a0 | G abs(E_shell)/a0 | G abs(E_shell) T_opt/a0^2 |
|---:|---:|---:|---:|
| 0.1 | 25.3596957093 | 0.2 | 5.0719391419 |
| 0.01 | 214.3550851675 | 0.02 | 4.2871017033 |
| 0.001 | 2023.6153761061 | 0.002 | 4.0472307522 |
| 0.0001 | 20032.8388772118 | 0.0002 | 4.0065677754 |

```math
T_{\rm opt}/a_0\sim 2/\epsilon,\qquad
G|E_{\rm shell}|T_{\rm opt}/a_0^2\longrightarrow4.
```

cを戻すと光学時間の単位はa0/c。これは二つの外部間の未来向き通過時間で、過去通信時間ではない。
解析原始関数と、元の4D計量のnull方程式の数値積分を照合した。
数値的な安定周波数には、厳密に因数分解した式を使う。未整理の極限式で桁落ちを検出した際も、精度・許容差は緩めていない。

## 6. 一つの時計差を入れるだけでAにはならない

今回の二端模型に `t_right=t_left+Delta` という**一定の、一回だけの**接続を入れる。
すると

```math
T=\begin{cases}t_{\rm left}&\text{left},\\
t_{\rm right}-\Delta&\text{right}\end{cases},\qquad
g^{-1}(dT,dT)=-1/f<0
```

が全体の時間関数である。接続近傍では共通のproper-radial座標へ移ればよく、薄殻の有限なlapseも正である。
未来向き因果曲線に沿ってTは増加する。往路で+Deltaなら復路は-Deltaとなり、同じ時計へ戻る量から消える。
15の有限対照では、個別の座標時間差が負になる例を保持したまま、一周の経過時間が正であることを検査した。

これは[Morris–Thorne–Yurtsever]型の、同じ外部空間に別の経路を持つ時間機械を否定しない。
**その第二経路や口の移動・時間対応を、今回の局所RN外部へ手で追加した時点で、別の未構成な大域解が必要になる。**
本計算の透過や安定性に任意の負の遅延を掛け、Aにしてはいけない。

過去側の `P(Y|do(0))`、`P(Y|do(1))` は未構成なので台帳はnull。
幾何の条件付き因果障害と、完成した検出器で確率を実測・導出したことを分ける。

## 7. 新しい一次文献も確認したが、条件は移植しない

[MP26]は四次元M2 x S2のmassive scalarの1-loop応力と先頭量子反作用を計算し、調べた範囲で通過可能性が残るとする。
しかしclassical anisotropic supportが入力で、全自己無撞着解や過去の介入通信は与えていない。本文のEq.(84)周辺と議論も確認した。
**「量子補正後も通過可能」をAとして借用せず、RN殻への応力係数の流用もしない。** この文献探索のみを新しい計算候補件数に入れない。

[E24]では殻の電荷、原点を通る線形EOS、熱力学的関係が今回と異なる。
その安定結果を、今回のneutral shellとaffine EOSの熱力学的安定性へ転用しない。

## 8. 再現・反証・引き継ぎ

```bash
python -m pip install -r architecture/requirements.lock
python scripts/test_architecture_search.py
python scripts/test_architecture_rn_search.py
python scripts/architecture_rn_search.py run --output /tmp/rn/raw
python scripts/architecture_rn_verify.py --records /tmp/rn/raw/candidates.json --output /tmp/rn/verification.json
python scripts/architecture_rn_search.py finalize --records /tmp/rn/raw/candidates.json --verification /tmp/rn/verification.json --output /tmp/rn/verified --gate
```

[台帳](../architecture/rn-a-target-v2.json)からJSON・Markdownを生成する。[専用workflow](../.github/workflows/architecture-rn-search.yml)は別jobで検算し、raw・検証記録・最終reportを保存する。
既存validator、Aの人間審査条件、原プロトコル、初回バッチは変更しない。A主張の自動clearanceは禁止のまま。
旧49テストに加え22テストを実行。候補生成器をimportしない別検算が、全1,890点、開領域、全4D曲率、非線形EOS微分、null積分・時計を確認する。
**同じAIによる別実装であり、独立研究者・別AIによる査読ではない。**

通常PRでは新規workflow・共有スクリプト・台帳の影響があるため、既存方針の全研究Python3.12 fallbackも維持する。
最新SHAのremote結果はPRの完了コメントに記録する。ローカルcloneはDNS失敗のため、全repoをローカル実行したとはしない。

### Aへ進めるための次の具体的対象

今回の179点をさらに増やすだけではAへ近づいた証拠にならない。
優先するのは、非極限の証明箱の周囲で、有限厚さの量子支持物質からsigma,pと構成応答を導くこと、および同じ外部を結ぶ第二経路と口の操作を同一の4D解へ組み込むことである。
その上で同一の準備資源・法則の下の二操作に対し、過去の有限受信記録の確率差を計算する。
状態・装置・時間対応のどれも、欲しい答えを入力する自由パラメータにはしない。

## 一次資料と利用箇所

- **[ER]** E. F. Eiroa, G. E. Romero, *Linearized stability of charged thin-shell wormholes*, General Relativity and Gravitation **36**, 651–659 (2004), [arXiv:gr-qc/0303093](https://arxiv.org/abs/gr-qc/0303093)。RN接合と電荷安定化。幾何の製造・電荷維持まで扱う論文ではない。
- **[E08]** E. F. Eiroa, *Stability of thin-shell wormholes with spherical symmetry*, Physical Review D **78**, 024018 (2008), [arXiv:0805.1403](https://arxiv.org/abs/0805.1403)。Eqs.(9)–(13),(35)–(37)、特に独立なDelta式。PDFテキストを確認。スクリーンショット取得はサービスエラーで失敗し、図の数値は使用していない。
- **[E24]** E. F. Eiroa, G. Figueroa-Aguirre, M. L. Penafiel, S. E. Perez Bergliaffa, *Dynamical and thermodynamical stability of a charged thin-shell wormhole*, EPJC **84**, 1160 (2024), [arXiv:2408.14328v3](https://arxiv.org/abs/2408.14328v3)。異なる殻・EOSの適用範囲比較。
- **[MTY]** M. S. Morris, K. S. Thorne, U. Yurtsever, *Wormholes, Time Machines, and the Weak Energy Condition*, PRL **61**, 1446 (1988), [DOI](https://doi.org/10.1103/PhysRevLett.61.1446)。同じ外部の経路を含む時間機械の条件付き構成との比較。単一seamのTは本ノートの導出。
- **[MP26]** H. Mehulic, T. Prokopec, *Quantum backreaction and stability of topological wormholes*, [arXiv:2603.11724v1](https://arxiv.org/abs/2603.11724v1) (2026)。本文の四次元1-loop計算と自己無撞着性の留保を文献監査したのみ。その数値解を今回再現したとはしない。

文献確認日2026-09-24。文献の既知結果、今回の再導出・具体点・区間証明、未構成な物理を区別する。
