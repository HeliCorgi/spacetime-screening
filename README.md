# Spacetime Screening

**知りたいこと：送信者が選んだ情報を、実際に過去の受信者へ届けられるか。**
CTC（閉じた時間的曲線）の幾何、弦の状態、受信確率を区別して調べます。ブラックホールの特異点回避も、別の研究として保存しています。

## 結論 — 2026-09-23

> **過去への情報送信は、まだ実証していません。**
>
> **今回進んだこと：** これまでのスカラー近似を通常の局所量子場として使うと、採用したTaub→NUT地平面で、健全な量子二点関数の延長に障害があることを確認しました。古典的な波を正則に調整するだけでは解消しません。
>
> **これは全弦理論・時間遡行一般の不可能性の証明ではありません。** 以下の「限定した経路の否定」と「一般問題の未判定」を分けます。

| 問い | 現在の答え |
|---|---|
| **選んだ情報を過去へ送れた？** | **未実証。** 過去の受信者の全結果を含む確率分布の差は得ていません。 |
| **これまでのスカラー案で、そのまま進める？** | **量子二点関数のHadamardな延長は不可。** 初期Hadamard状態・実・質量ゼロ場・指定したコンパクト延長の下での結論です。 |
| **完全な弦理論なら可能／不可能？** | **未判定。** 上の局所場の仮定を、実際の弦の応答がどう置き換えるかが残っています。 |

**[最新の研究ノート・導出・文献・再開点](notes/operational-past-signalling-focus.md)**

## 判定基準を「6項目の完走」から「実際の通信」へ変更

既存のCTCを使うために、因果構造を新たに変える必要はありません。全BRST cohomology・全スペクトルの完全な分類も、通信の存在を示すための必須作業ではありません。ただし、使用する操作・状態・観測量の物理的な正当性は確認します。

目標は、**同じ資源と同じ物理法則の下で許された二つの送信操作**を比べ、**実験室の時計で送信より前の、別のイベント**にある受信記録が区別できることです。雑音や損失があっても構いません。

```math
D_B=\frac12\sum_y|P(y_B\mid\mathrm{do}(b=0))-P(y_B\mid\mathrm{do}(b=1))|>0.
```

未来の成功フラグで後から選んだ結果だけを比較しません。受信時のherald・失敗も含め、利用可能な全記録を評価します。未知の応答を0と決めつけて「不可能」ともしません。[基準の変更点と誤差の扱い](notes/operational-past-signalling-focus.md#1-何が分かれば可能と言えるか)

## 今回の成果

**1. 単一モードから、量子場全体の条件へ進んだ。** 四次元では、診断用のdilaton-weightedスカラー作用が、滑らかな補助計量 `g_E=e^{-2Φ}g` 上の質量ゼロKlein–Gordon作用に正確に写ります。採用した延長のコンパクトな地平面と閉じたnull生成線を確認し、既知のKay–Radzikowski–Wald（KRW）定理を適用しました。定理そのものは先行研究です。

**2. 前回の正則sourceが、量子問題を解かない理由を特定。** 処方された古典的sourceは平均場を変えますが、線形場のconnected二点関数は変えません。「平均の波が通った」ことを「健全な量子通信媒体ができた」ことへ昇格させられません。全backreactionや全弦理論を解いたという結論ではありません。

**3. 「送れたように見える」偽陽性を検算。** 通常の3-qubit系では、未来のBell測定成功例だけを選ぶと過去のbitが完全に一致する例を作れます。それでも過去の**無条件分布の差は厳密に0**。2026年のnoisy P-CTC通信容量論文も確認し、「過去向きチャネルを仮定した能力」と「そのチャネルの物理的実現」を分けました。

[詳しい結果・仮定・反例・未計算事項](notes/operational-past-signalling-focus.md)

### 再現

```bash
python -m pip install -r requirements.txt
python src/symbolic/heterotic_taubnut_krw_bridge.py
python src/symbolic/operational_past_signal_probability.py
```

幾何・作用・確率行列は厳密代数、Gaussian検出模型の積分は50/80桁で比較。**コードのPASSは物理的な過去通信のPASSではありません。** KRWの定理と大域幾何の論証はノートで出典・仮定を明示しており、PythonやLeanによる形式証明とは呼びません。

## 前回までの成果と、次に進む場所

[前回の継続ノート](notes/heterotic-taubnut-operational-continuation.md)には、相対BRST、必要ラベル3組、Taub時間の混合、調整sourceからNUTへの古典スカラー接続を保存しています。[旧6条件監査](notes/heterotic-taubnut-six-gate-audit.md)と[文献対照検算](notes/heterotic-taubnut-literature-bridge.md)も監査履歴です。

**`99.813%` は外側スカラーODEの流束比であり、過去通信の成功率ではありません。** 古い無条件な `BRST / free-string PASS` の解釈は後の監査で訂正されています。

次は状態候補を増やすことより、**必要な一つの物理的な弦の操作・検出器の実時間応答が、今回の局所場の障害をどう回避するか**を調べます。回避を示したうえで、過去の検出確率と誤差を計算します。詳細は[最新ノート§6](notes/operational-past-signalling-focus.md#6-判定と次の課題)。

## ブラックホール研究（別テーマ）

こちらは **principal safety**：背景曲率が有限でも、摂動・拘束・運動項・4次元作用へ特異性を移しただけでは解決としません。

| 入口 | 内容 |
|---|---|
| [研究概要](SCREENING_RESEARCH_OVERVIEW.md) ／ [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) | ブラックホール側の成果・引き継ぎ |
| [principal-safe-screening](docs/principal-safe-screening.md) ／ [NOVELTY.md](NOVELTY.md) | 健全性・先行研究との区別 |
| **[時間遡行の最新ノート](notes/operational-past-signalling-focus.md)** | **過去通信の最新判定と再開点。時間遡行を指定されたらここから再開** |

## AI・コントリビューターの再開手順とCI

まず [AGENTS.md](AGENTS.md) と [CI運用ルール](docs/ci-policy.md) を読んでください。通常PRでは累積差分を検査し、独立scriptはPython 3.12、共有依存・データ・影響不明は全件へ拡大します。文書のみならリンク検査。Leanは関連変更時に実行します。

[PR checks](.github/workflows/pr-checks.yml) が対象と理由を記録し、[Symbolic CI](.github/workflows/symbolic-ci.yml) は週次・手動の全件再現性を検査します。精度・assertを弱めず、無関係な重複実行を減らします。

```bash
# コミット済みPRの累積差分（未コミット変更は含まれません）
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは [Apache-2.0](LICENSE)、研究文章・式・図は [CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・未解決の物理を区別して記録します。
