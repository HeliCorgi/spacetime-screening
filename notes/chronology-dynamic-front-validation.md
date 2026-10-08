# Dynamic drift-front: 再現・証拠の範囲

2026-10-09 JST。親PR #40 head `7410fa94786ffe43c74ade1e4dc00ee2ce355127`。
[解析本文](chronology-dynamic-front.md)。新規4ファイルのみ。

## 1. 実行方法

```bash
python src/symbolic/chronology_dynamic_front.py --output /tmp/dynamic-front.json
python src/symbolic/chronology_dynamic_front_verify.py --evidence /tmp/dynamic-front.json
python src/symbolic/chronology_dynamic_front_verify.py
```

依存は既存のSymPy/mpmathだけ。新しいdependency、CI/workflow、共有helperを追加しない。
2本は互いをimportしない。JSON連携なしでもそれぞれstandaloneで検査する。

## 2. 実際に検査したもの

- 4D計量からinverse、Christoffel、Ricci、scalar curvature、Einstein tensorを計算。
- `F=f(r)-q(t)` に対する全4成分のcovariant conservationを計算。
- `q=t` の3D初期Hamiltonian/momentum constraintsと必要なsourceの一致。
- logistic profileのsigned/absolute初期stress予算の厳密積分。
- moving Grant wallのdeterminant、timelike material tangent、intrinsic null nonaffinity。
- Hamilton方程式による独立のgeodesic/covector再導出。
- Dirichlet最大値原理のbarrier、logistic微分boundの代数、contraction、r/r' error、t0の有理包囲。
- forwardはexp(1/2)、verifierはexp(1/4)の別々の有理Taylor級数とtailを使用。
- conformal変更とsmooth potentialがprincipal null returnを消さないという解析的説明。
- 64/128/256分割のRK4 shooting。これは数値診断で、存在証明の代用ではない。

存在命題の直接法・微局所的伝播・IFT・compact-deformation条件の論証はノートに記述。
Python/Lean kernelでこれらの連続体定理を形式検証したとは報告しない。

## 3. 数値と解析的包囲を分離

| RK4分割 | t0（数値診断） |
|---|---:|
| 64 | 0.498714068040307495796654066043 |
| 128 | 0.498714068056889417263537133541 |
| 256 | 0.498714068057921744582303428415 |

連続する差の比は15と17の間にあることをassertしている。256の小さいshooting residualは連続体誤差ではない。
**解析的に保証した範囲**は、最大値原理と厳密剰余を含む
`0.4987095110074379 < t0 < 0.4987185542748360`。
全経路は `0<=r<=1/48`, `95/192<=t<=313/576`。
帰還covectorの倍率 `exp(1/2)` はこれらの数値rootの誤差に依存しない。

`|det D return_map|>17/64` は解析的bound。C2摂動を許す具体的半径の数値は未算出。
これを任意サイズのbackreactionの排除や、非線形SCEEの収束と呼ばない。

## 4. 負例・改変入力

zero boost、非周期psi、完全な経路を含まない切取りはno-go certificateとしない。
前段のESU refocusing controlの排除を主張しない。
有限negative RSETの可能性とstate positivity/NECを混同しない。

localでは16改変入力をCLIへ渡し、全てexit=1で拒否した:
parent、schema、一般no-go旗、物理的解旗、幾何旗、Hadamard旗、指数区間、時間区間、
contraction、error bound、holonomy、wall、conservation、switch stress、sourceの誤標識、radial kick。
改変用ファイルは別々に生成し、正常なforward出力は変更していない。

## 5. local / remote

local Python 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0で、新規2本、JSON連携、standalone、compile、
16改変テストを実行した。固定main source archiveのCI選別器20自己検査も成功。
新規文書のlocal参照先を確認した。**最新PRの全treeをlocal checkoutしたという主張ではない。**

remoteの累積PR差分検査は、この追記commitに対するGitHub ActionsとPR検証コメントで別に記録する。
過去headのsuccessを今回のheadへ流用しない。既存の軽量選別policyを維持し、理由なく全研究二版suiteを起動しない。

## 6. 未実施・非主張

物理的な壁の製造、initial total quantum energy、実際のRSETの構成、同じgのSCEE発展、
quantum wallを含む完全なinteracting theory、全形成時空のno-goは未達成。
検査成功はこれらをtrueにするものではない。
新しいLeanは追加していない。累積PRにある旧Leanの再検査を今回のQFT証明の形式化と取り違えない。
本稿は動的な幾何を設計し、その必要な量子条件が満たせないことを示した研究である。
