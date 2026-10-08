# Family 376 有限資源監査の再現・検証範囲

2026-10-08。追加の親はPR #40 head `c074780bf48f6b9acda92a94c1b74b28f96f362c`。
[監査本文](family376-finite-resource-matter-audit.md)を参照。
既存R1の係数、物理assert、精度、依存、workflow、CI選別器は変更しない。

## 対象

追加4ファイル: 本記録、監査本文、
[独立Python control](../src/symbolic/family376_finite_resource_checks.py)、
[条件付きLean ledger](../src/lean/Family376FiniteResources.lean)。
R1のnonlinear gateを解いたとの報告ではない。CTC関連の判定は変更しない。

OpenAI/math現在SHAは `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`。
9稿のbuild subtreeを現在のGitHub contents metadataと旧取得ファイルのGit tree hashで照合し、9/9一致した。
scope文書 `lean/docs/376.md` のblobも同一。
全upstream Lean依存closure/comparatorの再buildや全原稿の独立査読ではない。

## 実行方法

```bash
python src/symbolic/family376_finite_resource_checks.py --output /tmp/finite-resource.json
python -m json.tool /tmp/finite-resource.json >/dev/null
lean src/lean/Family376FiniteResources.lean
```

追加scriptは既存R1をimportせず、指定した線形modeのエネルギー恒等式と別の資源controlsを検査する。
JSONの生成先は利用者が指定し、入力reference JSONを追加していない。
誤ったcurrent sign、heat欠落、非正の粘性/relaxation、DECとcausalityの混同、資源超過、radix margin喪失の負例を含む。
「負例が失敗した」をscript全体の不具合と扱わず、拒否が実際に発生したことをassertする。

## ローカルで実施したもの

Python 3.13.5 / SymPy 1.14.0 / mpmath 1.3.0。
新規scriptの全assert、--outputとJSON再読込、追加Pythonのcompileを実行した。
現在の係数w=Q=k=1, mu=1/1000, tau=1/100を保持する。

| midpointの分割数 | T=2のmax endpoint error | heat ledgerへの移送 |
|---|---:|---:|
| 32 | 0.00184887527234466129 | 0.000302970614918953268 |
| 64 | 0.000462632277247998121 | 0.000303499474683494014 |
| 128 | 0.000115683906154638117 | 0.000303632217590233343 |
| 256 | 0.0000289225912710806451 | 0.000303665436440016643 |

全stepのQ+heat残差は有理数演算で厳密に0。一般のmidpointエネルギー恒等式は本文に導出した。
参照値は80桁matrix exponential、誤差比は3.9964,3.9991,3.9998。
この収束比較は線形ODEの数値実験であり、interval-certifiedなnonlinear GR誤差ではない。
既存R1のT=pi/sqrt(3)の厳密包囲を置き換えていない。

ローカル環境にはLeanが無いため、新規Leanのkernel検査はremote PR CIで確認する。
リポジトリへのネットワークcloneは利用できず、ローカル文書リンク検査は既存取得ファイルと追加ファイルの参照先確認で行う。
これを現在のremote head全体のローカル再buildや全研究suiteの成功と呼ばない。

## PR CIの期待範囲と結果の記録

現行の選別器はmainからPR headまでの累積差分を使う。
正常なら初回のfamily376_bridge_checks.py、既存R1二本、新規有限資源scriptの計4 Pythonと、
既存二つ＋新規一つのstandalone Lean、累積Markdownを検査する。
実際の選択数・Python版・Lean版・checkout SHA・tree・success/failureは**完了を確認した検証コメント**に記録する。
この文書を追加した時点で未完了のremote実行をPASSと先取りしない。

追加コードは既存の入力/assertを変更しない。全研究Pythonの全件・二版実行は今回の予定範囲ではない。
upstream MathのLean 4.34.1/Mathlib/全comparatorと、repoのstandalone Lean 4.19.0は別である。
`#print axioms`の結果が空でも、コスト下限というphysical premiseを証明したことにはならない。

## 未証明の中心

有限時間の物理的準備、R1のnonlinear tube invarianceと計算可能な誤差定数、
全gate composition、全入力の有限資源compiler、任意長の安定したhalting detectorは未構成。
今回の判定Dを、CI成功によってAへ変更しない。
