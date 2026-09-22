# Spacetime Screening

ブラックホールの特異点回避と、CTCを含む弦理論背景の物理的実現可能性を検証する研究リポジトリです。中心となる問いは、**「幾何が書ける」ことと「健全な物理過程として使える」ことは同じか**、です。完成した量子重力理論やタイムマシンを主張していません。

## 時間遡行：いま何が分かっている？

> **過去へ選んだ情報を送れることは、まだ示せていません。**  
> CTCを含む背景はありますが、下の6条件すべてを通過した物理的な通信過程はありません。これは時間遡行一般の不可能性の証明でもありません。

| 検証条件 | 現在地 |
|---|---|
| **1. 完全なBRST物理状態** | 必要な電荷・ウェイトの算術は一致。完全なcohomologyの認定は未完了。 |
| **2. 正ノルム・正常化** | Taub側のスカラーモードでは正で有限の初期KGノルム。完全な弦の物理内積は未確立。 |
| **3. 全弦スペクトルに含まれる** | GSO・大域的接合・全射影が未完了。既存のSU(2)状態例の一つには具体的な誤りを確認。 |
| **4. 逆反作用に耐える** | 特定のスカラー初期準備は地平面で非正則な枝を生む。回避する調整解もあり、全状態の排除ではない。 |
| **5. NUT到達と因果構造** | 固定背景のCTCは既存。到達と「新たに因果構造を変えること」は別。 |
| **6. 選んだ情報を過去へ送る** | 操作的な信号は未実証。完全な時空でなおchronalな受信点への通常の因果的帰還は不可。 |

**重要：`99.813%` は指定した外側スカラー波動方程式の流束比です。時間遡行や情報送信の成功確率ではなく、完全な弦の透過確率としても未認定です。** 古いノートの無条件な `BRST / free-string PASS` は、後の監査で解釈を訂正しています。

### 今回、実際に追加した結果

**Taubの時間発展を計算。** 指定した有限時刻の正周波数スカラーデータから `|β|² = 0.002668579603…` の未来基底への混合が出ます。一方、混合をゼロにした準備も構成できるので、「必ず壊れる」とは言えません。この数値は粒子・情報の過去送信成功率ではありません。

**状態の式を具体的に反証。** 既存ノートの `(K⁺₋₁)^(k w)|0⟩` は、`k=4, w=2` では主張された重み16を持たず、可積分真空表現ではnullです。これは特定の代表式の誤りであり、全ての候補状態やspectral flowを否定するものではありません。

**限定した帰還禁止をLeanで確認。** 因果的な信号supportとpush-up性を仮定すると、過去の受信点へ戻れるならその点もCTC上にあります。Leanが検証したのはこの条件付き論理であり、弦理論全体の因果性や時間遡行の普遍的禁止ではありません。

**詳しい導出・6条件の判定・文献：** [6条件監査ノート](notes/heterotic-taubnut-six-gate-audit.md)  
**再現可能な計算：** [Python](src/symbolic/chronology_six_gate_checks.py) ／ [Lean](src/lean/ChronologySixGate.lean) ／ [数値結果](notes/data/chronology_six_gate_checks.json)

## ブラックホール研究の本筋

本筋は **principal safety**：背景曲率が有限でも、物理的な摂動、拘束、運動項、4次元作用に特異性を移しただけでは解決としません。二ベクトル模型、非多項式QTG、非局所QTGなどを比較しています。

従来の詳細READMEは、本文をそのまま [SCREENING_RESEARCH_OVERVIEW.md](SCREENING_RESEARCH_OVERVIEW.md) に保存しました。時間遡行の脇道と本筋の研究を混同せずに読めます。

| 読みたいもの | 入口 |
|---|---|
| ブラックホール研究の詳細と既存成果 | [従来の研究概要](SCREENING_RESEARCH_OVERVIEW.md) |
| 本筋の引き継ぎ・次の課題 | [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) |
| 健全性の判定基準 | [principal-safe-screening](docs/principal-safe-screening.md) |
| 新規性・既知結果の区別 | [NOVELTY.md](NOVELTY.md) |
| 時間遡行についての最新の6条件判定 | [six-gate audit](notes/heterotic-taubnut-six-gate-audit.md) |

## 再現と検証

```bash
python -m pip install sympy==1.14.0 mpmath==1.3.0
python src/symbolic/chronology_six_gate_checks.py --json /tmp/six-gate.json
```

Lean 4.19.0がある場合：

```bash
lean src/lean/ChronologySixGate.lean
```

[専用GitHub Actions](.github/workflows/chronology-six-gate.yml) がPython 3.11／3.12とLeanを検査します。コードcommit `1a18f679…` の専用run #1は3jobとも成功。数値検算は50桁／80桁で比較しています。**CIは記述した計算を検査するもので、6条件の物理的成立を保証しません。**

## ライセンス

コードは [Apache-2.0](LICENSE)、研究文章・式・図は [CC BY 4.0](LICENSE-DOCS)。計算の再現、先行研究、条件付きの推論、未解決の物理を区別して記録します。
