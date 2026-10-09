# Return-germ剛性: 再現と検証の射程

2026-10-09。対象親: PR #40 `27e78fe8ab10566c2f54d787ba8e15e1ce0aa65a`。
[解析本文](chronology-return-rigidity.md)。今回の追加は本Markdown2件と独立Python2本のみ。
既存の方程式・係数・assert・精度・依存・workflow・CI選別・Leanを変更しない。

## 1. 結論の区分

| 出力 | 検証方法 | 言えること |
|---|---|---|
| return-germ剛性とchronology境界の排除 | 解析本文の証明。Hadamard/WF、特異性伝播、有限時間Hamilton flow、push-upを合成 | 明示した仮定下の解析的導出。独立査読・Lean形式化は未実施 |
| 零boostのcubic交差 | Hamilton系と別のEuler--Lagrange系から正確なscreen変分を計算 | 帰還倍率1でもreturn matrixが恒等でない |
| ESU refocusing | oscillator/Jacobi行列とround sphereの埋込み解を別計算 | 全近傍のgeodesic族が戻る。単なるsampleやfirst-jet判定ではない |
| massive ESUの負例 | mode固有値と整数奇偶性、本文のFourier完全性の議論 | 同じgeodesic flowでも指定低次項ではKG bisolutionは零のみ |
| 改変したJSONの拒否 | 26件の単独改変を独立verifierに渡す | 誤った有限計算値・過大なscope flagの混入を拒否。26個の物理定理を証明した意味ではない |

今回の解析的定理そのものをPythonが証明した、あるいは既存Leanの成功がそれを保証したとは報告しない。
新規の形成解、全形成過程の一般no-go、RSET/SCEEの数値発展は得ていない。

## 2. 初回解析時のローカル環境と実施内容

CPython **3.13.5**、SymPy **1.14.0**。
今回の新規コードにmpmathや新たな第三者依存は不要。

- forwardを実行し、JSON出力が正常に読めることを確認。
- 独立verifierをstandaloneとforward JSON連携の両方で実行し、成功。
- 新規2本のcompileに成功。
- 26種類の改変証拠を全てexit 1で拒否。
- 親mainの既存CI選別器の20自己テストに成功。
- 下記fixtureで新規4件の差分を計画し、Python2件・Markdown2件・Lean不要のtargeted選択を確認。
- 同じfixtureで新規2件の実行とMarkdown2件のローカルファイルリンク検査に成功。
- 新規4件だけのpatchの適用と、作業実体とのbyte一致を確認。

ここでfixtureは、会話に保存されたmain原本
`1ff10c4453f52f9f8f8c2c835a52812ce7faac90` のarchiveへ今回の4件を加えた**ローカル検査用tree**。
最新PRの全treeをcloneしたものではなく、fixtureで作るローカルcommit IDもGitHub上のcommitではない。
今回の対象ファイルがmain原本にも現在のPR追加ファイル一覧にも存在しないことを別に確認した。
このfixtureでの選別を、現在のPRの累積全差分の検査と呼ばない。

改変検査harnessは外部実行時間制限で途中停止したため、同じ26ケースの未実行分をresumeした。
最終の全26件がexit 1で拒否されたことを記録した。assert・判定閾値・テスト内容は緩めていない。
前半・resumeのログと最終集約JSONを配布用結果一式に保持する。

## 3. 再実行

リポジトリのrootで:

```bash
python src/symbolic/chronology_return_rigidity.py --output /tmp/return-rigidity.json
python src/symbolic/chronology_return_rigidity_verify.py --evidence /tmp/return-rigidity.json --output /tmp/return-rigidity-verified.json
python src/symbolic/chronology_return_rigidity_verify.py
python -m compileall -q src/symbolic/chronology_return_rigidity.py src/symbolic/chronology_return_rigidity_verify.py
python scripts/ci/test_checks.py
```

独立verifierはforwardをimportしない。Hamiltonian対Lagrangian、round sphere埋込み式、Fractionの反例を用いる。
この実装上の独立性は、解析的定理の独立査読と同じではない。

実際のPRへ反映後に累積差分を確認する場合は、既存のCI方針に従う:

```bash
git fetch origin main
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-return-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-return-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-return-plan.json
```

このコマンド列を記載したことと、最新PRの全累積差分について実行したことは別である。

## 4. 初回解析時の未反映記録と、その後のPR追記

初回解析のセッションではGitHubの読取操作で指定headと実内容を確認したが、書込操作を利用できず、
実行環境のgit/network経路も確保できなかった。その時点では4件を未反映の追加patchとして提供した。
初回解析時は新しいremote CI、Python 3.11/3.12での検査、全研究suite、新規Lean検査は未実施だった。
親headの過去のCI成功を今回の追加の成功へ読み替えない。

2026-10-09の追記作業では、同じ親headを読み直し、前回作成した解析本文・Python2本をbyte単位で保持して公開する。
この検証文書だけ、未反映だった初回と後続の公開作業を区別するために運用記録を更新した。
公開前にCPython 3.13.5 / SymPy 1.14.0でforward、独立verifier、JSON連携、standalone、compileを再実行し、全て成功。
既存ファイル・研究条件・assert・精度・依存・workflow・Leanは変更しない。mainへの直接変更やmergeも行わない。

公開commit、最新headに対応するremote CI run、実際の対象・結果は
[PR #40の検証コメント](https://github.com/HeliCorgi/spacetime-screening/pull/40) に記録する。
この文書の公開前ローカル検査だけを、累積PR全体のremote成功として報告しない。

原著の解析内容は引用元の本文に基づく。PDF screenshot取得にはcache missもあり、
取得できなかった図の内容や図からの数値を本証明の入力に使っていない。
既知の文献が今回のreturn-germ定理をそのまま証明済みだとは帰属させていない。
