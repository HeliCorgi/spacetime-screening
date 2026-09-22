# Spacetime Screening

ブラックホールの特異点回避と、CTC（閉じた時間的曲線）を含む弦理論背景が、健全な物理過程として使えるかを調べる研究リポジトリです。

## 時間遡行：過去へ、選んだ情報を送れた？

> **まだ実証できていません。6条件をすべて通過した弦の通信過程はありません。**
>
> 今回は、状態候補の検算と、外部sourceでNUT側へ正則なスカラー応答を作る計算まで進みました。
> **これは完全な弦状態でも、過去への情報送信でもありません。時間遡行一般の不可能性の証明でもありません。**

### 現在地 — 2026-09-23

| 必要な確認 | 判定 | 一言でいうと |
|---|---|---|
| **1. 完全なBRST物理状態** | **未認定** | 仮定した相対Abelianゲージ複体は検算。全heterotic cohomologyはまだ。 |
| **2. 正ノルム・正常化可能** | **スカラーでは部分成立** | Taub上の正で有限なKGノルムは作れる。弦の物理内積は別。 |
| **3. 全弦スペクトルで許容** | **未認定** | 必要条件を満たす候補を3組列挙。GSO・全射影・左右接合は未完了。 |
| **4. 逆反作用込みで維持** | **未認定／障害あり** | 調整sourceなら正則だが、小さな誤差で非正則成分が戻る。全backreactionは未計算。 |
| **5. NUT到達・因果構造変更** | **アクセスのスカラー例のみ** | 固定背景で正則に接続できる例。物理的な弦の到達・背景の構造変更は未認定。 |
| **6. 選んだ情報を過去へ届ける** | **未実証** | 同じ準備の2設定から、過去の受信確率の差を得ていない。 |

**CTCのある幾何 → スカラーの接続例 → 完全な弦状態の到達 → 操作的な過去通信**は、別々の検証段階です。
既存のCTCを使うだけなら、新たに因果構造を変えること自体は必須ではありません。動的な形成・変更を求める場合は、追加で検証します。

**最新の導出・6条件の判定・限界：** [操作的信号に向けた継続ノート](notes/heterotic-taubnut-operational-continuation.md)  
**前回の監査：** [six-gate audit](notes/heterotic-taubnut-six-gate-audit.md)

### 今回、何を計算した？

**状態候補を具体化。** 仮定した2つのAbelianゲージ電流の相対BRST複体について、grade 0〜3の行列とhomotopyを検査しました。同じ背景の制限したansatzでは、必要な電荷・重み条件を満たす正周波数候補が3組あります。**全string spectrumへの所属はまだ証明していません。**

**地平面の障害を1例から広げた。** 3候補のスカラー診断では、過去の正周波数modeから未来の非正則成分が生じます。混合の二乗は約 `0.0776154 / 0.0196993 / 0.00520611`。principal-continuous scalar族の一般式でも混合は非零です。**どれも情報送信の成功確率ではありません。**

**正則に通す構成例と、その弱点を両方確認。** 同じ初期データから、有限時間の外部sourceで未来地平面を正則に渡るscalar modeを作り、NUTの `x=2` まで接続しました。ただしsourceは空間的に広がった処方で、局所的な弦の送信装置ではありません。小さなsource誤差で非正則成分が再発します。

**数字の読み違いに注意：`99.813%` は指定した外側スカラー波動方程式の流束比です。**
時間遡行・情報送信の成功率でも、認定済みのexact string透過確率でもありません。古いノートの無条件な `BRST / free-string PASS` は、後の監査で解釈を訂正しています。

### 今回の計算を再現

```bash
python -m pip install -r requirements.txt
python src/symbolic/heterotic_taubnut_relative_brst_complex.py
python src/symbolic/heterotic_taubnut_horizon_transfer_family.py
python src/symbolic/heterotic_taubnut_retarded_source_control.py
```

相対複体は厳密な整数・有理数検算、数値計算は50桁／80桁の比較です。適用範囲・sourceの定義・未計算の物理は[継続ノート](notes/heterotic-taubnut-operational-continuation.md)に記録しています。**CIの成功は実装した検算の成功であり、6条件の成立ではありません。**

### 前回までの成果

[6条件監査](notes/heterotic-taubnut-six-gate-audit.md)には、有限Taub時刻の準備からの混合、特定のSU(2) descendant式の誤り、chronalな過去の受信者への帰還に関する条件付きLean補題があります。
[文献対照検算](notes/heterotic-taubnut-literature-bridge.md)では、別模型の非対称coset接合とNappi–Wittenの複素反射振幅を再現しました。これらのPASSをTaub–NUTの未検証条件へ移してはいません。

## ブラックホール研究の本筋

こちらは **principal safety**：背景曲率が有限でも、摂動・拘束・運動項・4次元作用に特異性を移しただけでは解決としません。時間遡行の研究とは区別しています。

| 読みたいもの | 入口 |
|---|---|
| ブラックホール研究の詳細と既存成果 | [研究概要](SCREENING_RESEARCH_OVERVIEW.md) |
| ブラックホール側の引き継ぎ | [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) |
| 健全性の判定基準 | [principal-safe-screening](docs/principal-safe-screening.md) |
| 新規性・既知結果の区別 | [NOVELTY.md](NOVELTY.md) |
| **時間遡行の最新結果と再開点** | **[継続ノート](notes/heterotic-taubnut-operational-continuation.md)** |
| 時間遡行についての前回の6条件判定 | [six-gate audit](notes/heterotic-taubnut-six-gate-audit.md) |

## AI・コントリビューターの再開手順とCI

まず [AGENTS.md](AGENTS.md) と [CI運用ルール](docs/ci-policy.md) を読んでください。ユーザーが時間遡行を指定している場合は、ブラックホール側の引き継ぎではなく上の継続ノートから再開します。

| 変更／実行の目的 | 自動検査 |
|---|---|
| README・ノートだけ | ローカルリンク等の軽量検査 |
| 独立した計算スクリプト | PR累積差分の影響対象をPython 3.12で検査 |
| 共有コード・依存・入力データ・影響不明 | Python全件へ拡大 |
| 週次／手動の完全検証 | 全スクリプトをPython 3.11／3.12、Leanも確認 |
| Leanの変更 | Lean検査。PythonだけのPRでは重複実行しない |

[PR checks](.github/workflows/pr-checks.yml) が対象と理由を記録し、[Symbolic CI](.github/workflows/symbolic-ci.yml) は週次・手動の全件再現性を検査します。精度・assertを弱めず、無関係な重複実行を減らします。

```bash
# コミット済みPRの累積差分（未コミット変更は含まれません）
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは [Apache-2.0](LICENSE)、研究文章・式・図は [CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・未解決の物理を区別して記録します。
