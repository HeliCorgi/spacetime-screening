# AI / contributor restart instructions

このリポジトリで作業を再開するAI・コントリビューターは、最初にこの文書と
[CI運用ルール](docs/ci-policy.md)を読むこと。会話履歴がなくても、この方針を使う。
本筋の研究状況は [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md)、研究結果の解釈は
各ノートの最新の監査・訂正を参照する。

## CIの既定方針

**通常PRの軽量検査と、全件の再現性検査を分離する。**

| 変更 | 既定の検査 |
|---|---|
| README・ノート等の文書だけ | ローカルリンク／ファイル参照の軽量検査。研究計算は実行しない |
| 独立した計算スクリプト | PR累積差分の変更スクリプトをPython 3.12で実行 |
| 共有コード・入力／参照データ・依存・CI設定、または影響不明 | 影響を見落とさないようPython全件へフォールバック。通常PRでは3.12 |
| 週次・手動の完全検証 | 全研究スクリプトをPython 3.11／3.12、Leanも確認 |
| Leanのみの変更 | Lean検査。Python計算を理由なく重複実行しない |

実際の選択は `scripts/ci/checks.py plan` が記録する。インポート先になっている
スクリプトや動的読み込みは独立と決めつけず、全件へ拡大する。
**直近コミットだけを見てPR内の先行コード変更を検査から落とさない。**

## 作業開始から提出まで

1. 最新のmain、作業ブランチ、開いているPRと既存変更を確認する。他者の変更を上書きしない。
2. 計算・文書の編集前に `docs/ci-policy.md` を読み、必要な検査範囲を決める。
3. CIの選別を変更したら `python scripts/ci/test_checks.py` を実行する。
4. コミット済みのPR差分を確認するときは、例えば次を使う（未コミット変更は含まれない）：
   ```bash
   git fetch origin main
   python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
   python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
   python scripts/ci/checks.py run --plan /tmp/ci-plan.json
   ```
5. 新しい共有依存、動的実行、暗黙のファイル依存を導入する場合は、選別器の負例テストも
   追加する。解析できない関係を黙って無視しない。必要なら `plan --full` を使う。
6. まとまった変更をコミットしてPRを作る。通常の研究PRに全件二版の `Symbolic CI` を
   毎回手動起動しない。追加で全件が必要なら理由をPRに書く。
7. 報告にはcommit SHA、実行対象、Python版、CI run、success/failure/pendingを分けて記す。
   過去SHAの成功や一部成功を最新の全件PASSとして報告しない。許可なくマージしない。

## 維持する制約

- 精度、assert、負例、検査条件を弱めて高速化しない。失敗をsuccessに置き換えない。
- Python 3.11／3.12で同じassertが通ることは、独立した物理証明ではない。
- PR内の古い実行だけ自動キャンセルする。最新版の必要な検査を飛ばさない。
- 六条件Python検算は通常のPython選別器で一度実行する。旧専用workflowに重複追加しない。
- 必須チェック候補は集約ジョブ **`PR checks`**。既存のbranch protectionを勝手に解除しない。
- 書込権限がない場合はパッチを提出し、未コミットと明記する。「反映済み」と言わない。
- 研究上の未確立事項を、CI成功によってPASSへ格上げしない。
