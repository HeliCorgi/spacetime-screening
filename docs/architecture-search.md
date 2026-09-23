# 4D Past-Signalling Architecture Search — 実行手順と安全条件

## 目的と到達点

添付された [原プロトコル](4d-past-signalling-protocol.txt) を基に、有限の候補群を再現可能に探索し、候補ごとの記録・反証検査・Markdown報告を生成する初版です。
原文の全byteとSHA-256を保持します。原文§3.4とStage 5の表示式では等号が欠落しているため、実装上はそれぞれEinstein方程式の等式、全応力の和として**明示的に**解釈しました。原文自体は書き換えていません。

**初回結果：7候補・部分構成、2,282計算点、A=0 / B=3 / C=4。**
これは候補の分類数であり、自然界の可能性の統計ではありません。二次元の禁止式を四次元へ流用していません。
[科学的手法・出典・適用範囲](../notes/architecture-search-batch-v1.md)を参照してください。

## 実装範囲

この初版は、文献と仮定を固定した候補族を走査します。一般の計量・量子状態を自動生成して全ての連立方程式を解く汎用AI研究者ではありません。
文献の探索・モデル定義・式の導出は今回の研究作業で行い、Actionsは固定したモデルの計算・照合・記録を繰り返します。自動オンライン検索した文章を物理的な前提として無審査に採用しません。

| 原プロトコル | この版の処理 |
|---|---|
| Stage 1 文献・模型 | 著者、題名、年、URL、使った箇所、確認日を候補台帳に必須化 |
| Stage 2 幾何 | 真の3+1D計量、時間の同一視、接合条件を候補ごとに記録・検査 |
| Stage 3 量子源 | 計算できた繰込み応力と、幾何から要求しただけの応力を別ラベルにする |
| Stage 4 反作用 | 固定背景・分布的古典解・局所近似・半古典的自己無撞着性を区別 |
| Stage 5 全装置 | `complete=false` を許すが、何が未供給か必須。Aには認めない |
| Stage 6 安定性 | 薄殻の半径方向モードを計算。他モードや形成過程は未計算と記録 |
| Stage 7 介入通信 | 同じ準備で送信符号だけを変える対照。B候補の過去側分布は未取得のまま |
| 分類 | 候補ごとにA/B/Cの一つ。プログラムのエラーはCではなく実行失敗 |
| 独立検証 | 候補ごとに別プロセス／別Actionsジョブで異なる計算法を実行 |
| 出力 | JSON台帳からMarkdown報告を生成し、入力・実装・実行SHAを記録 |

各Stageの `completed` は**明記した限定検査の完了**であり、装置全体の完成ではありません。`partial` / `not_reached` も保存します。
Bの一部は支持源や安定性だけの**部分候補**です。過去通信を実証した結果として集計しません。

## ファイル

- [候補台帳](../architecture/batch-v1.json)：仮定、境界、場、状態、Stage、出典、未解決事項。
- [モデル計算](../scripts/architecture_models.py)：厳密代数、有限パラメータ走査、50/80桁計算。
- [検証・生成器](../scripts/architecture_search.py)：必須項目検査、分類、checksum、レポート生成。
- [別実装の反証検査](../scripts/architecture_verify.py)：モデル生成器をimportせず、微分・積分・行列逆転を別に行う。
- [負例テスト](../scripts/test_architecture_search.py)：不正なA、未取得確率の0埋め、次元違い、改竄、古い証明書などを拒否。
- [固定依存](../architecture/requirements.lock)：SymPy 1.14.0 / mpmath 1.3.0。
- [Actions workflow](../.github/workflows/architecture-search.yml)。

## ローカルで実行する

Python 3.12を基準とします。以下はリポジトリrootから実行します。

```bash
python -m pip install -r architecture/requirements.lock
python scripts/test_architecture_search.py
python scripts/architecture_search.py run --output /tmp/architecture/raw
python scripts/architecture_verify.py \
  --records /tmp/architecture/raw/candidates.json \
  --output /tmp/architecture/verification.json
python scripts/architecture_search.py finalize \
  --records /tmp/architecture/raw/candidates.json \
  --verification /tmp/architecture/verification.json \
  --output /tmp/architecture/verified --gate
```

`verified/report.md` は `verified/candidates.json` から生成します。`verification.json` は元の台帳ファイルと検証プログラムのSHA-256を含みます。
同じ数式への50/80桁再実行と、別手法による照合を区別しています。前者だけを独立な物理証明とは呼びません。

一候補を独立プロセスで調べる例：

```bash
python scripts/architecture_verify.py \
  --records /tmp/architecture/raw/candidates.json \
  --candidate-id fkz-mass-controlled-ring \
  --output /tmp/architecture/tasks/fkz-mass-controlled-ring.json
# 他の候補についても各々実行してからcollectする。
python scripts/architecture_search.py collect \
  --records /tmp/architecture/raw/candidates.json \
  --directory /tmp/architecture/tasks \
  --output /tmp/architecture/verification.json
```

`collect` は一つでも候補が欠ける、重複する、元の台帳や検証実装のhashが違う、失敗を含む場合に停止します。
再実行時に実装や入力を変更したら、raw台帳も再生成します。古い検算を新しい結果へ流用しません。

## Aの誤認定を防ぐ

未計算の確率は `{"computed": false, "distribution": null, "reason": "..."}`、未計算の識別度もnullです。
`0` は実際に同一分布を導出した対照だけに使います。エルゴ領域、ワームホールの存在、CTC、透過率、半径方向安定性は、そのまま識別度になりません。

Aには少なくとも、実際の過去受信で `D > error_bound`、全応力・全装置・半古典的自己無撞着性・適切な安定性・初期境界整合性・有限の受信記録が必要です。
これらの入力flagは科学的証明の代わりではありません。必要な証拠が揃ったという**主張**も、必ず人間と独立研究者が審査する対象です。

`finalize --gate` はAを含む場合、成果物を保存した後に**非零終了**します。自動承認・自動マージ機能はありません。成功・失敗を含む全結果を記録します。
このworkflowはリポジトリ保護設定を変更しません。CIを必須チェックにするかは管理者の別操作であり、今回設定済みとはしません。

## Actionsと既存CIの関係

`4D architecture search` は関連ファイルを変更するPR、または明示的な手動実行で動きます。無期限の自律計算を予約するscheduleは設けません。

1. `generate`：固定依存をinstall、プロトコルの負例テスト、候補生成、全必須項目検査、raw成果物を保存。
2. `verify`：候補ごとのmatrix。A/Bを含む全候補へ別実装の検算ジョブを作り、最大4並列で動かす。
3. `report`：必要ジョブが成功した場合のみhashと候補網羅性を検査し、台帳・Markdown・検証記録を出力。A主張は自動clearanceを阻止。

全jobが `contents: read`。認証情報をcheckoutに保持せず、書き込み・マージ処理を持ちません。
Actions自体も固定commitを参照します。文献は実行時にネットワークから取り込みません。
成果物はrawの全計算点、検証記録、最終JSON、Markdown、実行commit hashを含み、30日保存の設定です。

既存の `PR checks` は変更せず維持します。**今回はCI／共有インフラの追加なので、既存選別器は通常方針どおり全研究Pythonへフォールバックする想定です。**
その既存ジョブと、新しい探索・反証ジョブは別です。既存130本の実行を、新規探索の成功で代用しません。Leanを変更していないので、理由なく追加実行しません。

## 独立性・未達事項

反証検査は別アルゴリズム・別プロセス／ジョブですが、作成者は同一のAIです。**独立研究者、別AI研究員、査読者による科学的検証は未実施**です。
原プロトコル§8の独立科学レビューの要求を、この数値照合だけで完了扱いしません。

初回では多口・複数ループ、移動する口の全時間発展、分岐型の量子支持、相互作用場、全noise kernel、局所製造装置をまだ解いていません。
その領域は `coverage.not_assessed_now` に置き、B/Cの件数へ水増ししません。

新しい模型を追加する場合は、台帳、モデル関数、検証関数、ID registry、判定根拠、負例テストを一緒に更新します。
探索の失敗や未実装をCに割り当てるdefault分岐はありません。仮定の変更は `assumption_changes` に記載します。

## この配布時点の状態

今回の検算はローカルPython 3.13.5で実行しました。GitHubのmainを読取確認しましたが、このセッションで公開されたGitHub toolには書き込みactionがなく、CLI接続も使えませんでした。
したがって **PR作成・remote Actions実行・マージは未実施**です。以前のCI成功を今回の成功として引用しません。
この文書とworkflowは適用用パッチに含みます。repoへ適用・実行された後は、生成台帳の実checkout SHAと新しいActions結果を確認してください。
