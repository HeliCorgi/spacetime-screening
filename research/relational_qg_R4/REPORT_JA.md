# R4：正の lapse に対応する運動項と、非線形球対称初期データの実行可能な模型

基点：R3 `39fa44951a83d44d3bdae88ee6a0ab9b6ad5af34`。2026-09-30。

## 到達点と適用範囲

R4_2 は R3 の m=2 空間曲率作用を保持し、不均一な lapse N に対する運動項の演算子順序を修正した候補である。全非線形の時間発展、一般背景の安定性、量子重力の完成を主張しない。

今回の実装が入力から返すのは、漸近平坦・球対称・時間対称の物質初期データに対する、非線形 Hamiltonian 拘束の計量解と、trace 拘束を保存する lapse である。源の強さについて二次で打ち切らず、選んだ作用の非線形式を数値的に解く。数値離散化の近似と、理論自体の適用範囲は別である。

**新たに計算したこと：** 正の lapse による運動二次形式の反例と修正、全空間に写像した非線形初期値ソルバー、独立な強形式残差、ADM 境界と体積式の一致、質量感度と平均 lapse の一致。

**計算していないこと：** 全時刻の崩壊、非球対称の物理モード安定性、全背景の拘束階数、宇宙論、量子 loop、特異点一般の解消。

## 1. R3 の運動項を不均一な時計へ移すと何が起きるか

単位は必要な箇所以外 G=c=ell=1。Q=1+L/2、A=Q^2、S=Q^{-1}=A^{-1/2} とする。L は適切な境界条件を課した非負・自己共役の空間 rough Laplacian。

R3 の tracefree 運動二次形式は、実内積で

    T3[N] = (2/M_P^2) <p, (N A^{-1}+A^{-1} N)/2 p>.

N>0 と A^{-1}>0 だけでは、この反交換子の正値性は従わない。

平坦な周期方向 x に沿う、横・無跡テンソル p_yy=-p_zz を使う。正規直交な空間プロファイル sqrt(2) cos(x), sqrt(2) cos(5x) の二次元部分空間と

    N(x)=1+cos(4x)/2,
    1/2 <= N <= 3/2

を選ぶ。このとき

    A^{-1} = diag(4/9,4/729),
    N_matrix = [[1,1/4],[1/4,1]],
    K3 = [[4/9,41/729],[41/729,4/729]].

    det K3 = -385/531441,
    lambda_min(K3) = -0.00160440301166923605...

であり、負方向がある。

これは許容される全拘束背景上の physical ghost を証明したものではない。選んだ N は非線形 lapse 方程式の解とは限らない。示したのは「正の N と正の A だけで任意の off-shell 運動項を正とする推論」の反例である。

## 2. 新しい結合定数を足さず、順序を修正

R4 の運動項を

    T4[N] = (2/M_P^2) integral sqrt(gamma) N
             [(S_T p)^ij (S_T p)_ij - (1/2)(S_s tr p)^2]

に変える。trace 拘束 C=gamma_ij pi^ij=0 の上では、tracefree 部分は

    T4[N] = (2/M_P^2) <S p, N S p> >= 0

となる。N>0 と S の定義域・自己共役性を仮定する。これは全相互作用エネルギーの下界や安定性の証明ではない。

二モード制御では

    K4 = [[4/9,1/81],[1/81,4/729]],
    det K4 = 5/2187,
    lambda_min(K4) = 0.00514002045225183264...

である。

差は二重交換子

    K3-K4 = (1/2) [S,[S,N]].

N が空間一定なら差はゼロ。従って平坦背景の二次作用・二偏極・静的核 K2 は変更しない。非一様 lapse と運動量が関与する高次相互作用は変わる。これは明示的な模型修正であり、R3 の結果を変更なしの帰結として装わない。

全 canonical action は R3 の potential、matter、spatial constraints、C=0、ADM 境界を保持し、上記の運動項だけを入れ替える。変分では

    delta S = -S (delta Q) S

など、計量による演算子変化を含める。有限個の補助場や状態の再選択は追加しない。時間対称 p=0 では運動項もその一次変分もゼロなので、R3 の非線形初期拘束・自己源計算は保持される。

## 3. 何を入力するか

    gamma_ij dx^i dx^j = exp(2 zeta(r)) (dr^2+r^2 dOmega^2),
    pi^ij=0,
    rho_c(r)=M_rest exp[-r^2/(2 sigma^2)]/(2 pi sigma^2)^(3/2).

rho_c は座標体積当たりの保存 rest-mass 密度であり、proper density は rho_c/exp(3 zeta)。この区別は epsilon が大きい場合に重要で、同じ座標 sigma は同じ物理半径の星を意味しない。

    epsilon=G M_rest/(c^2 ell),
    sigma=ell (配布 benchmark),
    zeta regular even at r=0,
    zeta~G M_ADM/(c^2 r) at infinity,
    N regular even, N(infinity)=1.

物質は瞬間的に静止している dust 型初期データ。圧力で支えられた静的な星ではない。計量と N が得られても、そのまま全時刻で静止する解とは呼ばない。

## 4. 球対称でも演算子を平坦なものへ置換しない

orthonormal Ricci の radial/angular eigenvalues を a,b とする。

    a=e^(-2 zeta)(-2 zeta''-2 zeta'/r),
    b=e^(-2 zeta)(-zeta''-3 zeta'/r-zeta'^2),
    R=a+2b,
    Delta f=e^(-2 zeta)[f''+(2/r+zeta')f'].

テンソル rough Laplacian には接続項がある。

    Delta_T a = Delta a-4 e^(-2 zeta)(1/r+zeta')^2(a-b),
    Delta_T b = Delta b+2 e^(-2 zeta)(1/r+zeta')^2(a-b).

選んだ m=2 potential の全式は

    V = R-Delta R+(1/4)Delta^2 R
        -a^2-2b^2+(1/4)(a Delta_T a+2b Delta_T b)
        +(1/2)R^2-(1/8)R Delta R.

拘束は

    exp(3 zeta) V = 16 pi rho_c.

曲率に関する展開はしていない。中心で有限でも rough Laplacian の接続項を落とすと、別の理論になる。

曲がった時間対称背景の trace variation での最高階 symbol は

    -M_P^2 sqrt(gamma) ell^4 (gamma^ij k_i k_j)^3/4.

球対称 conformal 変数では

    partial[exp(3 zeta) V]/partial[zeta^(6)] = -exp(-3 zeta).

正の空間計量なら最高階は elliptic。しかしこれは全作用素の核がないことや lapse が正であることを保証しない。その部分は次の数値診断で分けて記録する。

## 5. ADM 境界を落とさない弱形式と lapse

N の全 radial functional を積分すると

    integral r^2 exp(3 zeta) N V dr = 4 N_infinity M_ADM + W[N].

W は N,N',N'' に線形である。c=2/r+zeta' として、使用した式は

    W[N] = integral r^2 {
      exp(zeta)(4N' zeta'+2N zeta'^2+N' R')
      +(1/4)exp(-zeta)(N''+cN')(R''+cR')
      +exp(3 zeta)N(-a^2-2b^2+R^2/2)
      -(1/4)exp(zeta){N[a'^2+2b'^2+4(1/r+zeta')^2(a-b)^2]
                         +N'(a a'+2b b')}
      +(1/8)exp(zeta)(N R'^2+N' R R') } dr.

境界を含めた strong density との差が全微分になることを記号的に検証した。tensor contraction の product rule も別に検証した。

基底を b_j、zeta=sum a_j b_j、N=1+sum n_j b_j とし、

    W_i=W[b_i],
    J_ij=partial W_i/partial a_j,
    source_i=16 pi integral r^2 rho_normalized b_i dr

と置く。解く方程式は

    W_i=epsilon source_i,
    J^T n = -gradient_a W[1].

二番目は conformal metric variation、すなわち trace constraint を保存する lapse 方程式である。N=exp(-zeta) を手で置いてはいない。

ADM mass は独立に

    M_ADM=epsilon-W[1]/4

と、zeta の無限遠の 1/r 係数から読み取り、両者を照合する。

## 6. 実行方法と失敗条件

root requirements に NumPy/SciPy を追加する。既存 SymPy/mpmath の記号検算も使用する。新しい依存と JSON は既存 CI policy の full-Python fallback 対象で、選別器の条件を緩めない。

```bash
python -m pip install -r requirements.txt
python src/symbolic/relational_qg_r4_ordering.py
python src/numerical/relational_qg_r4_initial_data.py \
  --epsilon 0.01 0.1 0.5 1 2 4 --sigma 1 \
  --output /tmp/r4.json --profiles /tmp/r4-profiles.json
python src/symbolic/relational_qg_r4_verify.py \
  --evidence /tmp/r4.json --output /tmp/r4-verify.json
```

numerical と ordering は output 指定なしではファイルを書かない。verifier の evidence 省略時は、この研究ディレクトリのコミット済み results.json を読む。CI shard 間の生成物共有を仮定しない。

r=b tan(theta) で半径全域を有限区間へ写像し、u=b/sqrt(b^2+r^2)、基底 b_j=u T_j(2u-1) を用いる。基底は中心の偶対称性と無限遠の1/rを満たす。b=4、32/40 modes、240/320 quadrature nodes を比較する。b は数値写像の尺度であり新しい物理定数ではない。

チェックが落ちれば、計量や lapse を clip して成功にしない。

- 非線形 root の success と、投影残差 1e-9 未満。
- lapse の転置方程式残差 1e-9 未満。
- preconditioned radial Jacobian の最小特異値 1e-4 より大きいこと。
- 有限展開について N>=1-sum|n_j|>0。この bound に連続解近似誤差は含まない。
- 新しい160半径点で Hamiltonian と lapse の strong residual が規格化後 1e-6 未満。
- ADM surface/volume relative gap が 1e-6 未満。
- 二つの離散化間の主要観測量差が 1e-7 未満。

配布 CLI は 0<epsilon<=4 に制限する。この上限は確認した benchmark 範囲であり、物理的臨界密度を発見したという意味ではない。sigma を変える試行は可能だが、同じ基底で収束する保証はなく、上記 gate に通る必要がある。

## 7. 実際の非線形結果

sigma=ell の細かい離散化の結果。値は無次元。

| epsilon | zeta(0) | N(0) | M_ADM/M_rest | mean N |
|---:|---:|---:|---:|---:|
| 0.01 | 0.0049509922 | 0.9950620016 | 0.9979293981 | 0.9958640994 |
| 0.1 | 0.0491080103 | 0.9521576091 | 0.9797642577 | 0.9600432285 |
| 0.5 | 0.2359167263 | 0.7919781176 | 0.9084223730 | 0.8279900684 |
| 1 | 0.4458890633 | 0.6481944545 | 0.8371214856 | 0.7109616473 |
| 2 | 0.7891201333 | 0.4770122347 | 0.7349984358 | 0.5696539888 |
| 4 | 1.2554369789 | 0.3283677799 | 0.6140669818 | 0.4352152117 |

小さい epsilon の質量低下は R3 の二次自己源と一致する方向へ近づく。一方 epsilon>=1 の行は、二次近似の式へ数値を代入した結果ではない。選んだ nonlinear constraint を解いたものである。ただし物質分布は座標幅固定で、proper size も計量に従って変わる。

細かい離散化の preconditioned 最小特異値は epsilon=4 で約0.03291、有限展開の全域 lapse 下界は約0.32493。全点で正な lapse が単なる有限の半径サンプルだけに依存しないことを確認した。ただし有限展開自体の bound である。

主観測量の離散化差は最大2.6e-13。別の strong-form 誤差は最大約4.5e-9、ADM surface/volume gap は約6e-11以下だった。小さい離散化差だけから物理的に13桁正しいとは解釈しない。

reference epsilon=1 については、独立 verifier が元の sixth-derivative invariant action を直接 Euler 変分し、65桁演算で基底を再構成、別の5半径点で continuum residual を検査した。最大誤差は約1.6e-9。係数そのものは double precision である。

## 8. 同じ作用から出る質量と時計の感度関係

座標密度の形を固定した、この時間対称解の系列では

    d M_ADM/d M_rest = mean_rho N,
    mean_rho N = integral rho_normalized N d^3x.

J a'=source、J^T n=-gradient W[1] を使えば

    d M_ADM/d epsilon=1-(gradient W[1]) J^{-1} source/4
                     =1+n^T source/4
                     =mean_rho N.

これは拘束と lapse が同じ action variation から作られた結果である。任意の状態変化に対する普遍的な first law だとは主張しない。

epsilon=1 の独立5点差分では

    dM_ADM/dM_rest = 0.7109616472915173,
    mean_rho N    = 0.7109616472916851,
    difference    = 1.68e-13.

N は初期時刻で shift=0 の静止時計の固有時間率 d tau/dt で、無限遠で1に規格化される。このデータは静的星ではないので、N(0)を将来にわたる定常な観測赤方偏移と同一視しない。

rest dust の最初の座標加速度は

    ddot r|_0=-N exp(-2 zeta) N'

であり、同じ初期解から出力する。これは full time evolution を計算したことではない。

## 9. 残る物理的・数学的穴

1. 任意の曲がった背景における拘束作用素の global kernel、全局所物理モードの安定性は未証明。radial Galerkin Jacobian の可逆性とは異なる。
2. 非球対称摂動、非零運動量、dust shell crossing、長時間の lapse の符号・正則性を計算していない。
3. quantum measure、第二種拘束の量子化、loop counterterms、radiative stability は未解決。今回の計量は量子期待値 backreaction ではなく指定 matter の classical initial data。
4. preferred foliation と短距離の非局所性を保持する。完全な refoliation invariance や exact metric microcausality を回復したとはしていない。
5. R3 の宇宙論的な一様モードの問題は残る。特異点一般を防ぐ仕組み、真空エネルギーの値を与える仕組みは追加していない。
6. 球対称の有限な初期曲率から、特異点のない将来や regular black hole を推論しない。

今回の「使える」は、入力を指定し、条件を満たす初期計量・時計・質量を再現可能に計算でき、失敗なら非零終了する、という意味である。

## 10. 検証・CI

ローカル Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 / SymPy 1.14.0 / mpmath 1.3.0。

- 元の invariant action と境界込み弱形式の記号恒等式。
- old/new kinetic の厳密有理数行列と、独立な Fourier 積分。
- source strength の六点、各二解像度、全160点の残差。
- reference profile を forward を import せず65桁で強形式検査。
- old ordering、full-evolution overclaim、wrong ADM mass、changed lapse profile を検査器が拒否。
- epsilon=5、negative sigma を CLI が拒否。

既存 R3 head の remote run 36653761330 は failure。取得したログでは古い cbssl_uv_opaque_mouth_v14.py の min_d>0.6 assertion が原因で、R3追加計算の失敗ではなかった。ただし failure を success と読み替えない。R4はこの無関係な既存 assertion を緩めずに残す。最新 R4 run の結果は PR で別に記録する。

## 比較参照

- J. Bellorin and A. Restuccia, arXiv:1606.02606. 別の kinetic-conformal theory における second-class constraints、elliptic multiplier equations、正の reduced Hamiltonian。R4 の証明を提供する文献ではない。
- S. Mukohyama and K. Noui, arXiv:1905.02000. 空間共変性を保持する二自由度 Hamiltonian construction。今回の S N S ordering と球対称結果はここで計算したもの。

新規性の優先権は主張しない。既存論文の健全性をこの模型へ転用しない。
