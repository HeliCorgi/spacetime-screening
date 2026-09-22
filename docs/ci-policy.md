# CI運用・AI再開ガイド

**方針決定：2026-09-23。通常PRは軽量、全件再現性は週次／手動。**
この文書は次に作業するAIにも適用するリポジトリの運用方針。
根本の入口は [AGENTS.md](../AGENTS.md)。科学的な結論・式・assertの強さは変更しない。

## 1. 検査の選び方

| 状況 | 実行 |
|---|---|
| 文書だけ | 変更Markdownのローカルファイルリンクを検査。研究Python／Leanを省略 |
| 独立した計算スクリプト | PR全体で追加・変更したスクリプト、Python 3.12 |
| 共有コード、入力・参照データ、Python依存、選別器／Python workflow | Python全件（PRは3.12） |
| 依存関係・差分を判定できない | 全件へ戻す。差分取得自体が失敗した場合はLeanも確認 |
| Leanファイル／Lean設定／Lean workflow | Lean 4.19.0の検査 |
| 完全な再現性検査 | Python 3.11／3.12で全件、Lean、選別器の自己検査 |

「省略」は失敗を無視する操作ではなく、PR差分にその種類の変更がないことを記録する。
**影響のある検査は維持する。** 同じPRでコード変更後に文章だけを追記しても、PR累積差分に
コードが残っているのでコード検査を再実行する。古い実行のキャンセルで無駄を抑える。

## 2. workflowの担当

- [`pr-checks.yml`](../.github/workflows/pr-checks.yml)：全PRで軽い選別・文書検査。
  必要なPython 3.12／Leanジョブを選び、最後に **`PR checks`** で結果を集約する。
  top-levelのpath filterは使わず、文書PRでも集約結果を返す。
- [`symbolic-ci.yml`](../.github/workflows/symbolic-ci.yml)：名称は **Symbolic CI** を維持。
  週次（月曜04:23 JST、日曜19:23 UTC）と `workflow_dispatch` のみ。
  通常PRやmainへの各マージで全件二版を重複実行しない。既存monitorはこの完全検査を報告する。
- [`chronology-six-gate.yml`](../.github/workflows/chronology-six-gate.yml)：再利用可能な **Lean checks**。
  Python六条件検算を再度実行しない。通常PRではLean変更時だけ呼び出し、完全検査では一度呼ぶ。
  単独手動起動も可能。

週次実行の設定はdefault branchにマージされてから有効。GitHub側のスケジュールは遅延し得る。
ブランチ上に実装されたことと、mainで方針が有効になったことを区別して報告する。

## 3. 自動選別の具体的な契約

[`scripts/ci/checks.py`](../scripts/ci/checks.py) が `ci-plan.json` を作る。

1. `git merge-base BASE HEAD` からHEADまでの **PR全体** の差分を使う。
   `--no-renames` で改名は削除＋追加として扱い、削除前の利用側も見落とさない。
2. 研究実行対象は、従来どおり `src/symbolic/` と `src/numerical/` の直下の `.py`。
   `__init__.py` は実行対象ではない。下位ディレクトリの共有module変更は全件扱い。
3. 両方のtree（実際のcheckoutとmerge-base）をASTで調べ、変更スクリプトをインポート／
   文字列参照する別moduleがあれば共有依存として全件へ拡大する。
4. 動的import、exec/eval、runpy、ディレクトリ列挙等がある場合は、独立性を推定せず全件へ戻す。
5. `data/`、`notes/data/`、依存ファイル、未知の種類の変更は全件扱い。
   参照JSONを変更したPRは「文書だけ」とは扱わない。
6. 差分・baseが読めないときは全件へ戻す。構文エラーも省略せず、実行前compileで失敗させる。
7. 計画には対象・理由・base/head・checkout SHA・Python版・Lean要否・shardを保存する。

これは任意のPythonプログラムの依存性証明器ではない。新しい実行機構、暗黙のI/O依存、
コード生成、サブプロセスでの間接実行を導入したら、全件へ拡大する規則と負例を追加すること。
CIの成功キャッシュを「依存が変わっていない証明」の代わりに使わない。

研究対象が16本以上なら4つの独立runnerへ分割する。各shardは `selected[i::4]` であり、
全体で各対象をちょうど一度実行する。runner内は直列のままにして書込競合を避ける。
別scriptの生成物に依存する検査を新設した場合は、先に依存順序を明示し、shardを横断して
生成ファイルが共有されると仮定しない。各scriptの所要秒数をActions summaryへ記録する。

## 4. 文書検査の範囲

Markdownのインライン／参照式リンクから、リポジトリ内のファイル・ディレクトリの存在を確認する。
コードフェンス内の例は対象外。外部URL・見出しanchorの生存確認はしない。
削除・改名時は、変更されていないMarkdownもその削除対象へのリンクだけ調べる。
過去の無関係なリンクを一斉に修正するためのPRではない。

新しいMarkdown構文に対応する必要があれば、検査器のテストを追加する。
通常のPRでarXiv等へ大量のネットワークアクセスをしてCIを重くしない。

## 5. 次のAIが使う手順

まず最新のmainと開いたPRを確認する。未コミット／他者の変更を保護する。
`AGENTS.md`、この文書、必要な研究引き継ぎを読む。

```bash
# CI自身の検査（標準ライブラリのみ）
python scripts/ci/test_checks.py

# コミット済みのPR全体を計画。未コミット・未追跡の編集は含まれない。
git fetch origin main
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python -m pip install -r requirements.txt
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

ローカル作業中は、新規・変更scriptを直接実行して検算してからコミットする。
全件が本当に必要な場合だけ：

```bash
python scripts/ci/checks.py plan --full --plan /tmp/ci-full.json
python scripts/ci/checks.py run --plan /tmp/ci-full.json
# ローカルは現在のPythonで実行する。二版の検査をしたことにはならない。
```

リモートの全件二版検査はActionsの **Symbolic CI → Run workflow** で対象refを指定する。
CLIが接続済みなら `gh workflow run symbolic-ci.yml --ref BRANCH` を利用できる。
自動PR検査とは別に手動起動した理由をPR本文へ残す。

## 6. 受け入れ検査と、安全な再開

20件の自己検査には、文書だけ、新規独立script、PR途中コード＋最後の文書、共有import、
削除、改名、入力データ、未知の変更、構文エラー、動的列挙、Lean分離、差分取得失敗、
shardの重複／漏れ、リンク切れ、実行失敗、タイムアウト、空の全件検査を含む。
新規の選別経路を追加するときは、正常系だけでなく「必要な検査が消えない」負例も追加する。

PRの集約ジョブは、必要と判定したジョブがsuccessでなければ成功しない。
必要なジョブのcancelled/failureを、不要ジョブのskippedと混同しない。
通常PRの古い実行のみ自動キャンセルし、手動の完全検査を勝手に中断しない。

必須チェックを設定する場合の候補は **`PR checks`**。従来の
`symbolic (Python 3.11)`／`symbolic (Python 3.12)` を必須としている環境では、
管理者がルールを移行する必要がある。PRを通すために保護を無断解除しない。

## 7. 結果報告に必ず残すこと

- 変更commit SHAとPR、実際に実行したrunのURL／ID。
- 対象一覧とPython版、Leanを実行したか、全件か対象限定か。
- local / remote、success / failure / pending、未実施項目。
- 完全検査を追加起動した場合の理由。失敗時は再実行の前に失敗箇所を確認する。

同じcommitへの変更を小分けにpushし続けない。検算・文書をまとめてpushする。
「次のAIが確認する」ことと「今このrunの完了を確認した」ことを区別する。
CI成功は実装された検査の成功であり、BRST物理状態・量子重力・時間遡行の証明ではない。

## 8. 設計の公式参照

- GitHub Actions workflow syntax：PR差分、path filter、必須チェック、schedule、concurrency。
  https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- Reuse workflows：`workflow_call` を使ったLeanジョブの一元化。
  https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
- Concurrency：古いPR runのキャンセルと、完全検査とのgroup分離。
  https://docs.github.com/en/actions/concepts/workflows-and-actions/concurrency

閲覧日：2026-09-23。runnerやactionの更新と、この検査方針の変更は別のPRで扱う。
