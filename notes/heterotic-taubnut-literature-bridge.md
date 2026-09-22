# 文献から埋めるTaub–NUTの未検証部分：状態空間と複素振幅の対照計算

**日付：2026-09-23。状態：既知模型の再現検算。Taub–NUTの6条件をPASSへ変更しない。**

接続するrepoの読取基点：`main` の `b830f842a8212ccd8284beaadd35bc2f08c99bec`。
[6条件監査](heterotic-taubnut-six-gate-audit.md)の「完全なBRST状態、正ノルム、大域的スペクトル、相互作用、操作的通信は未確立」という判定を維持する。

## 0. 今回やったこと

ユーザーが提示した文献を一次資料と照合し、優先順位の先頭2件について、別模型で実行できる対照計算を作った。

| 対照計算 | 実行した検査 | 結果 | まだ示していないもの |
|---|---|---|---|
| Quella–Schomerusのコンパクト非対称coset | 左右の許容集合、共通同一視群、接合行列、modular S/T整合性 | `k=2,3,4`でPASS。誤った追加同一視を入れた負例は棄却 | 非コンパクトheterotic Taub–NUTのHilbert空間・BRST cohomology |
| EGKRのNappi–Witten模型 | 半古典反射係数と有限レベル二点関数の複素値、絶対値、位相、大きいkの極限 | 指定例および表示された最低励起条件を満たす26組で一致関係を再現 | Taub–NUTのexact振幅、独立したNW波動ODE積分、過去通信 |

計算コード：

- [asymmetric_coset_gluing_benchmark.py](../src/symbolic/asymmetric_coset_gluing_benchmark.py)
- [nw_exact_reflection_benchmark.py](../src/symbolic/nw_exact_reflection_benchmark.py)

これは先行研究の再現であり、新規性や優先権の主張ではない。

## 1. Quella–Schomerusをどう使うか

[Q1, §2.3, 式(7)–(8), PDF pp.7–8]では、左右それぞれの許容ラベル集合とfield-identification群から

```math
\mathrm{All}=\mathrm{All}_L\cap\mathrm{All}_R,\qquad
\mathcal G_{\mathrm{id}}=\mathcal G_{\mathrm{id},L}\cap\mathcal G_{\mathrm{id},R},
```
```math
\mathcal H=\bigoplus_{[\mu,a]\in\mathrm{All}/\mathcal G_{\mathrm{id}}}
\mathcal H^L_{(\mu,a)}\otimes\overline{\mathcal H^R_{(\mu,a)^+}}
```

という構成を与える。右側には共役ラベルが入る。式(7)の直後には、**共通同一視群の作用に固定点がない**という仮定が明記されている。個別の左右同一視群について同じ仮定を課したという意味ではない。

重要なのは、左右で同一視できる関係をすべて集めてさらに商を取るのではなく、まず**共通部分**を確定すること。この手順と、branching、正しい表現の測度、gluingは、旧候補の電荷・ウェイトの相殺だけでは決まらない。

ここでの「heterotic CFT」は左右のchiral algebraが異なり得るという文脈でも使われている。これを、そのまま超対称heterotic stringのGSOやcritical completionの構成済みという意味に読まない。

### 1.1 実際に検算した非対称模型

[Q1, §4.2]の`p=q=1`に対応するコンパクト対照系を使う：

```math
G=SU(2)_k\times SU(2)_k,\qquad
\epsilon_L(h)=(1,h),\qquad\epsilon_R(h)=(h,1).
```

ラベルを `(l1,l2,m)` とし、`l1,l2=0,...,k` はspinの2倍、`m`は`2k`を法とするU(1)ラベルとする。

```math
\mathrm{All}_L:\quad l_2-m=0\pmod 2,\qquad
\mathrm{All}_R:\quad l_1-m=0\pmod 2.
```

個別の同一視は、親の単純カレントのラベルで

```math
\mathcal G_{\mathrm{id},L}=\{(0,0,0),(0,k,k)\},\quad
\mathcal G_{\mathrm{id},R}=\{(0,0,0),(k,0,k)\},
```

なので、共通群は自明。個別のparafermionラベルには `(l,m)~(k-l,m+k)` を使用するが、そのことから**全状態空間にも左右両方の商を追加する**ことはしない。

左右のchiral algebraをどちらも `SU(2) × parafermion` の順に並べると、接合は

```math
(l_1,[l_2,m])_L\quad\leftrightarrow\quad(l_2,[l_1,-m])_R
```

となる。これを全ての許容ラベルについて足し、非負整数の接合行列 `M` を作った。同じ左右module対が複数回現れる場合、その多重度を残す。

### 1.2 独立した整合性検査

構成した`M`を、有限個の既知のchiral S行列にかけて検査する。

```math
S^{SU(2)}_{ll'}=\sqrt{\frac2{k+2}}\sin\frac{\pi(l+1)(l'+1)}{k+2},
```
```math
S^{PF}_{(l,m),(l',m')}=\frac2{\sqrt{k(k+2)}}
\sin\frac{\pi(l+1)(l'+1)}{k+2}\,e^{i\pi mm'/k}.
```

`Z=χ^T M conjugate(χ)`という配列規約で`S^T M conjugate(S)=M`を確認。T変換については共形ウェイト差が整数であることを**有理数演算で厳密に**検査した。Sについては40桁・65桁の数値検算であり、形式的証明とは呼ばない。

| k | 許容triples | chiral空間の次元 | 65桁計算のS整合性最大残差 |
|---:|---:|---:|---:|
| 2 | 10 | 9 | 1.31e-66 |
| 3 | 24 | 24 | 5.24e-66 |
| 4 | 52 | 50 | 1.04e-65 |

`k=4`では非ゼロ接合要素が50個、最大多重度2、真空多重度1だった。

**負例検査：** `k=4`で、共通群ではなく左右の同一視が生成する群で余分に商を取ると、代表は14個になり、modular S整合性の残差は`0.75`となる。したがって、この実装は「過剰な同一視」を実際に検出する。

**適用範囲：** これはコンパクトな有理CFTの対照計算。Taub–NUTのholonomyやFableのw同一視をこの数値だけで否定・認定するものではない。

### 1.3 Taub–NUTに必要な入力

次の状態空間計算は、旧候補の量子数を入力する前に、最低限これを確定する必要がある。

1. 左右の親chiral algebra、全fermion・格子を含む埋め込み、レベル規約。
2. 非コンパクト表現の選択、連続ラベルの測度と重複度、spectral-flow sector。
3. 左右のbranching・global selectionと、共通field identification、固定点解消。
4. 左右接合、GSO、critical completion、許容補助場状態。
5. その空間での完全なBRST複体と物理的内積。

未知の項目を自動的に「自明」「全て許容」として埋めない。有限集合コードをそのまま連続表現の全空間の列挙器と呼ばない。

## 2. EGKRの複素反射振幅を再現

[N1]の規約は

```math
j_{NW}=-\tfrac12+is.
```

§2の半古典係数、式(2.44)を`R0`、式(4.25)の有限レベル係数を`Rk`と書く。脚注19の`ν(k)=1`を固定する。

```math
R_0=\frac{\Gamma(-2j-1)\Gamma(j+1+im)\Gamma(j+1-im')}
{\Gamma(2j+1)\Gamma(-j+im)\Gamma(-j-im')},
```
```math
\frac{R_k}{R_0}=F_k(s)=\frac{\Gamma(1-2is/k_{NW})}{\Gamma(1+2is/k_{NW})}.
```

実数sと正の実数kについて、分子分母は共役なので`|Fk|=1`。ただし一般に`Fk≠1`。ここでの`k_NW`をTaub–NUTのbosonic levelと同一視しない。

### 2.1 計算に使った独立したNW参照点

```math
k_{NW}=10,\quad j'_{SU(2)}=3,\quad m=3,\quad m'=-2,\quad s=\sqrt3/2.
```

この組は、論文で表示された内部運動量0・最低oscillator条件

```math
-j(j+1)-m^2+j'(j'+1)-m'^2=0
```

および`|m|,|m'|≤j'≤k_NW/2−1`を満たす。Taub–NUTの旧候補の置換ではない。ここでは論文に示されたこの必要条件を検査するのであって、別のBRST証明を提出するのではない。

45桁・80桁で比較した値は

```math
R_0=0.0043257984427387317675-0.0002848529958101642946\,i,
```
```math
R_k=0.0042985314784250260744+0.0005624060147367041594\,i,
```
```math
F_k=0.98088209518335786856+0.19460296849921399509\,i.
```

両方の反射率は

```math
|R_0|^2=|R_k|^2=0.0000187936733964228622995\ldots,
```

だが、複素比の位相は

```math
\arg F_k=0.19585266404654346602\ldots\;\mathrm{rad}.
```

つまり、**反射率だけをテストするコードでは、有限レベル補正を丸ごと落とすバグが検出できない**。

### 2.2 同じ式を二度置くだけにしない検査

Gamma積による係数に加え、式(3.31)の別表現

```math
|R|^2=\frac{\cosh(2\pi\omega_+)+\cosh(2\pi(s-\omega_-))}
{\cosh(2\pi\omega_+)+\cosh(2\pi(s+\omega_-))},\quad
\omega_\pm=(m\pm m')/2
```

と比較した。`k_NW=8,10`、最低oscillatorの表示条件と`s>0,ω_->0`を満たす26組を列挙し、率の一致を確認。80桁計算の最大残差は`3.2e-81`以下だった。これは列挙した条件の範囲の再現であり、全string spectrumの列挙ではない。

さらにkを`10,20,40,100,1000,10000`へ増やすと複素比は1へ収束する。連続なlog-Gammaの規約で位相は

```math
\phi_k(s)=-2\operatorname{Im}\log\Gamma(1+2is/k),\qquad
\partial_s\phi_k=-\frac4k\operatorname{Re}\psi(1+2is/k).
```

この微分式を数値微分と照合した。大k展開も

```math
\phi_k=\frac{4\gamma_Es}{k}-\frac{16\zeta(3)s^3}{3k^3}+O(k^{-5})
```

に一致する。規約依存の位相微分を、そのまま観測者の時間遅延や過去応答と解釈しない。

repoで使っていた`j_repo=1/2+is`とは`j_NW=j_repo−1`でCasimirが一致する。ただし、これはCasimirの辞書であって、埋め込み、レベル、Cartan charge、左右接合まで同じになることを意味しない。

**未実施：** NW波動方程式の独立した数値積分、二点関数の世界面path integralからの再導出。今回の結果は、論文の半古典／exact係数とその一致関係の再現である。

## 3. ②と⑤を接続する、もう一つの理由

[H1, 式(123), PDF p.33]の地平面応力のmode kernelには、散乱係数の絶対値だけでなく、複素係数の積の実部を取る干渉項がある。したがって将来の実装では、反射・透過の率だけでなく**複素係数と基底規約を保存**する必要がある。規約による個別位相は相殺するよう、一貫した組合せで使う。

これはNWのGamma補正をRNdSやTaub–NUTへ移植してよいという意味ではない。別模型の二つの例が、同じソフトウェア上の要件を教える、という接続である。

## 4. 文献別の検証記録と用途

| ID | 固定した参照版／確認範囲 | 次に使うところ | この文献だけでは認定しないもの |
|---|---|---|---|
| Q1 | hep-th/0212119v3。§2.3、式(7)–(8)、固定点仮定、§4.2を確認 | branching、共通selection、field identification、gluing、modular検査 | 非コンパクトheterotic模型のno-ghost／GSO／全BRST |
| N1 | hep-th/0204189v2。式(2.44)、(3.31)、(4.19)、(4.22)–(4.25)、脚注19を確認 | scalar coefficientとexact二点関数を区別する複素振幅対照系 | Taub–NUTに同じ補正を掛ける操作 |
| D3 | 2105.12130v2。abstractと`3ptf_ancillary.nb`の掲載を確認 | 親WZWの三点関数・flowとfusionの検査 | Notebookの実行済み、Taub–NUT coset三点関数完成 |
| D4 | 2107.01481v2。abstract、Ward/KZ検査の記述と`4ptf_ancillary.nb`の掲載を確認 | 親WZW四点関数の部品と検証 | 2021年の提案式をそのまま全heterotic振幅の証明とすること |
| P3 | 2212.05877v1／2023 journal。abstractで三点提案の証明との対応を確認 | D3の証明版の出典 | D4の四点関数までこの論文が証明したとの主張 |
| K1 | 1902.02991v4。版履歴の式(5.16b)訂正、§4の振幅比較を確認 | ghost/picture込みのheterotic productsとcontact/exchange | Taub–NUT固有のCFT結合係数が既知になること |
| H1 | 1912.06047v2。式(122)–(128)、§5.3–5.4、図10を確認 | 複素散乱係数→二点関数差→mode sum→renormalized応力 | 単一β、二null-fluid invariant、RNdS結論をそのままTaub–NUTの応力とすること |
| I1 | hep-th/0310158v2。書誌・abstractを確認。この回は§3–4全式の独立検算をしていない | heterotic Gödel/AdSのspectrum／一loop対照系 | Gödel instabilityをTaub–NUTの不安定性定理にすること |

D3/D4のNotebookは掲載の確認のみで、今回は実行していない。K1の完全なproducts、H1のRNdS数値曲線、I1のpartition functionも再現未実施。すべてを「再現済み」とまとめない。

H1の参照点 `r_c=100, r_+=2, r_-=1.95` は原文図10で確認した。実装時にはこのケースを独立に再現し、IR相殺・角運動量和・繰込み・極限交換まで確認する。[H1]の結論は任意の背景への普遍定理ではなく、係数が特殊にゼロとなる例にも原文が言及する。

## 5. 次の実装単位

今回の2対照計算を既存の6条件検査の前段に置く。`PASS`は方法の対照検査が通ったという意味に限定する。

**状態空間側：** Taub–NUTの完全な入力データを揃え、左右branchingと接合を構成する。未知入力を埋めないまま旧量子数のmembershipだけを判定しない。

**相関関数側：** NWの複素係数を再現できる規約を固定した上で、Taub–NUTの実際の射影付き二点関数を導く。親WZW相関関数、非対称gauge／holonomy projection、fermion、GSO、global prescription、物理的二点pairingを分離して記録する。

いずれが進んでも、操作可能な過去通信の条件6は独立に残る。非ゼロ相関関数、位相差、modular invarianceは、同じ初期準備から送信者の選択で過去の受信確率を変えることを示さない。

## 6. 再現と公開状態

```bash
python -m pip install mpmath==1.3.0
python src/symbolic/asymmetric_coset_gluing_benchmark.py \
  --json notes/data/asymmetric_coset_gluing_benchmark.json
python src/symbolic/nw_exact_reflection_benchmark.py \
  --json notes/data/nw_exact_reflection_benchmark.json
```

ローカル実行：Python 3.13.5、mpmath 1.3.0で両方PASS。
既存のTaub–NUT計算、Lean、CI workflow、6条件の判定は変更していない。
リモートへのcommit、PR作成、Actions起動はこの成果物には含まれない。
READMEへの追記と新規ファイルを含む適用パッチを同梱する。対象は読取基点のmain。baseが進んだ場合はREADMEの差分を確認して適用する。

## 7. 一次資料

- **Q1:** T. Quella, V. Schomerus, *Asymmetric Cosets*, JHEP 02 (2003) 030. [hep-th/0212119v3](https://arxiv.org/abs/hep-th/0212119v3)
- **N1:** S. Elitzur, A. Giveon, D. Kutasov, E. Rabinovici, *From Big Bang to Big Crunch and Beyond*, JHEP 06 (2002) 017. [hep-th/0204189v2](https://arxiv.org/abs/hep-th/0204189v2)
- **D3:** A. Dei, L. Eberhardt, *String correlators on AdS3: Three-point functions*, JHEP 08 (2021) 025. [2105.12130v2](https://arxiv.org/abs/2105.12130v2)
- **D4:** A. Dei, L. Eberhardt, *String correlators on AdS3: Four-point functions*. [2107.01481v2](https://arxiv.org/abs/2107.01481v2)
- **P3:** D. Bufalini, S. Iguri, N. Kovensky, *A proof for string three-point functions in AdS3*, JHEP 02 (2023) 246. [2212.05877v1](https://arxiv.org/abs/2212.05877v1)
- **K1:** H. Kunitomo, T. Sugimoto, *Heterotic string field theory with cyclic L-infinity structure*. [1902.02991v4](https://arxiv.org/abs/1902.02991v4)
- **H1:** S. Hollands, R. M. Wald, J. Zahn, *Quantum Instability of the Cauchy Horizon in Reissner–Nordström–deSitter Spacetime*. [1912.06047v2](https://arxiv.org/abs/1912.06047v2)
- **I1:** D. Israël, *Quantization of heterotic strings in a Goedel/Anti de Sitter spacetime and chronology protection*, JHEP 01 (2004) 042. [hep-th/0310158v2](https://arxiv.org/abs/hep-th/0310158v2)
