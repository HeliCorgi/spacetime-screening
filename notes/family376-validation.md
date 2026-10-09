# Family 376 監査の検証記録

2026-10-08。[監査本文](family376-fluid-gr-bridge-audit.md)／[定理台帳](family376-theorem-ledger.md)。

## 原本と変更範囲

spacetime base: `1ff10c4453f52f9f8f8c2c835a52812ce7faac90`。
OpenAI/math source: `adc7f1241b42e322a6451854ab7e4b4c146bf78a`。
現mainとopen PRを確認し、既存draft PR #39は変更していない。別branch `audit/family376-gr-bridge-20261008` に追加した監査であり、mainへの直接変更やmergeは行わない。

最終変更は監査Markdown4件、独立Python1件、standalone Lean1件。既存研究script、assert、精度、依存、CI選別器は変更しない。原本を取得するためにbranch上で一時利用したread-only source-collection workflowは最終差分から除去する。

## 原本収集と、証明再検査の区別

GitHub Actions [run 37726298911](https://github.com/HeliCorgi/spacetime-screening/actions/runs/37726298911) は成功。固定math SHAの9稿・TeX・selected comparator設定・scope文書・関連sourceを保存し、hashを生成した。外部原稿のコードはこの収集jobでは実行していない。

**このrunはLean buildではない。** Original OpenAI/mathのLean 4.34.1／Mathlib／comparatorの全推移的closureは本監査で再実行していない。original sourceのstatement・scope・selected solution entryを照合したことと、全証明の独立検証を区別する。

## 新しいPython検査

`src/symbolic/family376_bridge_checks.py` はローカルPython **3.13.5**, SymPy **1.14.0**で実行。以下を検査する。

| 検査 | 検査の意味 |
|---|---|
| shearの発散、移流、residual、curl | prescribed NS forceの恒等式と、pure gravitational potentialへの置換の負例 |
| kinetic energy、viscous dissipation、power | 標準energy balanceと、非自明steady flowの正の投入仕事 |
| slow-time scaling、onto／bounded clock | 固定viscosityでのnaive rescalingと、有限累積clockの誤用を拒否 |
| **5292例**の有理tape更新 | base8・偶数digit・空列／blankを含む、有限列の代数検算 |
| normal-volume compensationとcoding gaps | det1条件の必要性、一様precisionを有限prefixから推定しないための対照 |
| ADM inverse \(g^{tt}=-N^{-2}\) | vector \(\partial_t\) とcovector \(dt\) のnormの混同を拒否 |

無効digit・方向、normal compensationの欠落、naive force rescaling、vector/covector混同を負例として検査する。生成したJSONを読込できることも確認する。

```bash
python src/symbolic/family376_bridge_checks.py --output /tmp/family376-evidence.json
python -m json.tool /tmp/family376-evidence.json
```

**これらの成功は、upstream full compiler、GR solver、positive Hadamard state、finite RSET、CTC existence／undecidabilityのいずれの証明でもない。** JSONの`not_proved`欄にこの制限を保持する。

## 新しいLean lemma

`src/lean/Family376Bridge.lean` はimportのない **Lean 4.19.0** 用ファイル。新しいaxiomやsorryは使わず、三つのlemmaについて `#print axioms` を行う。repository既存のLean workflowで検査する。

- `no_regular_horizon_compiler`：immediately-halting witnessと、KRW型obstructionを仮定したcompiler仕様の矛盾。
- `no_chronal_ctc_compiler`：全出力をchronal classに制限したCTC detectorの矛盾。
- `undecidability_transfer`：source algorithm class・target algorithm class・effective composition・iff reductionを仮定したgeneric transfer。

physical premiseを引数としている点は定理statementに露出する。KRW、Lorentz geometry、NS、QFT、具体的halting problemをこのファイルで形式化したとはいわない。`Decidable`とTuring computabilityを取り違えない。

ローカル環境にはLean executableがないため、このファイルのkernel検査はremote CIへ分離する。remoteの完了状態・head SHA・run ID・axiom出力は**本PRの検証コメント**に記録する。source collection runや前PRの成功を代用しない。

## 差分CIと再現性

```bash
python scripts/ci/checks.py plan --base BASE --head HEAD --plan /tmp/family376-plan.json
python scripts/ci/checks.py docs --plan /tmp/family376-plan.json
python scripts/ci/checks.py run --plan /tmp/family376-plan.json
```

remoteでは現在PRの累積差分に対する通常のPR checksを使用する。ローカルは同じupstreamファイル内容から作ったworkspace commitをBASEに使い、remote SHAの別名とは扱わない。ローカルselectorは `mode=targeted`、追加Python1件、Markdown4件、`lean=true` を選別した。選ばれたPython1件はexit=0、4 Markdownのlocal-file linksはPASS。external URLと見出しanchorの生存はこのdocs検査の対象外。remote selectorが全件を必要と判断した場合は選別結果を弱めない。今回は全150件を二Python版で再実行したとは主張しない。

ローカルworkspaceの原本commitは `c143268a4898f9626aacdf8dd6064c6fca0db358`。この値はupstream commit SHAではなく、取得した原本内容をローカルでversion管理するために生成したもの。
