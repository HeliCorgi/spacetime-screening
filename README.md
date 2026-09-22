# Spacetime Screening

**知りたいこと：送信者が選んだ情報を、実際に過去の受信者へ届けられるか。**
CTC（閉じた時間的曲線）の幾何、弦の状態、受信確率を区別して調べます。ブラックホールの特異点回避も、別の研究として保存しています。

## 結論 — 2026-09-23

> **過去への情報送信は、まだ実証していません。一般に不可能とも証明していません。**
>
> **量子場側：** これまでのスカラー近似を通常の局所量子場として使うと、採用したTaub→NUT地平面で、健全な量子二点関数の延長に障害があります。古典的な波を正則に調整するだけでは解消しません。
>
> **通信判定側：** 受信器と選択bitの記録を含む対照回路を計算しました。CTCがある／波が届く／定常解が違う、だけでは通信成功にしません。
>
> **これらは全弦理論・時間遡行一般の不可能性の証明ではありません。** 局所量子場の障害、仮定した回路の結果、実際の弦の通信を区別します。

| 問い | 現在の答え |
|---|---|
| **選んだ情報を過去へ送れた？** | **未実証。** 実際のTaub–NUT上で、過去の受信者の全結果を含む確率分布の差は得ていません。 |
| **これまでのスカラー案で、そのまま進める？** | **量子二点関数のHadamardな延長は不可。** 初期Hadamard状態・実・質量ゼロ場・指定したコンパクト延長の下での結論です。 |
| **NUT内に帰還経路はある？** | 固定背景で、受信→送信の実験室経路と送信→受信の帰還経路を、二つの未来向きtimelike円弧として確認。装置や情報の実現ではありません。 |
| **異なるCTC固定点があれば通信成功？** | **それだけでは不足。** 指定したDeutsch product処方の記録付き回路ではbitとの相関が0。初期相関を許す別処方では非零ですが、その処方を物理法則から導く必要があります。 |
| **完全な弦理論なら可能／不可能？** | **未判定。** 局所場の障害を実際の弦の応答がどう回避するか、どの送受信統計が導かれるかが残っています。有限回路の0も非零も、自然界の結論へ移しません。 |

**量子場側の導出・仮定：** [KRW適用と確率判定ノート](notes/operational-past-signalling-focus.md)  
**通信判定側の導出・検算：** [受信記録付きCTC回路ノート](notes/chronology-operational-channel-test.md)

## 判定基準を「6項目の完走」から「実際の通信」へ変更

既存のCTCを使うために、因果構造を新たに変える必要はありません。全BRST cohomology・全スペクトルの完全な分類も、通信の存在を示すための必須作業ではありません。ただし、使用する操作・状態・観測量の物理的な正当性は確認します。受信時の吸収や状態変化は失敗とはせず、通信過程全体の逆反作用と自己無撞着性を確認します。

目標は、**同じ資源と同じ物理法則の下で許された二つの送信操作**を比べ、**実験室の時計で送信より前の、別のイベント**にある受信記録が区別できることです。雑音や損失があっても構いません。

```math
D_B=\frac12\sum_y|P(y_B\mid\mathrm{do}(b=0))-P(y_B\mid\mathrm{do}(b=1))|>0.
```

未来の成功フラグで後から選んだ結果だけを比較しません。受信時のherald・失敗も含め、利用可能な全記録を評価します。未知の応答を0と決めつけて「不可能」ともしません。[基準の変更点と誤差の扱い](notes/operational-past-signalling-focus.md#1-何が分かれば可能と言えるか)

bitを選ぶ物理装置の記録も含め、相関を介入確率と取り違えないようにします。**「同じ準備」を受信結果まで同じに固定して、時間遡行を定義で禁止することもしません。** 外から与える準備と法則を固定しても、ループ内部の解は操作に応じて変わり得ます。[通信判定ノート§1–2](notes/chronology-operational-channel-test.md)

## 量子場側の成果：地平面の障害と確率の偽陽性

**1. 単一モードから、量子場全体の条件へ進んだ。** 四次元では、診断用のdilaton-weightedスカラー作用が、滑らかな補助計量 `g_E=e^{-2Φ}g` 上の質量ゼロKlein–Gordon作用に正確に写ります。採用した延長のコンパクトな地平面と閉じたnull生成線を確認し、既知のKay–Radzikowski–Wald（KRW）定理を適用しました。定理そのものは先行研究です。

**2. 前回の正則sourceが、量子問題を解かない理由を特定。** 処方された古典的sourceは平均場を変えますが、線形場のconnected二点関数は変えません。「平均の波が通った」ことを「健全な量子通信媒体ができた」ことへ昇格させられません。全backreactionや全弦理論を解いたという結論ではありません。

**3. 「送れたように見える」偽陽性を検算。** 通常の3-qubit系では、未来のBell測定成功例だけを選ぶと過去のbitが完全に一致する例を作れます。それでも過去の**無条件分布の差は厳密に0**。2026年のnoisy P-CTC通信容量論文も確認し、「過去向きチャネルを仮定した能力」と「そのチャネルの物理的実現」を分けました。

[詳しい結果・仮定・反例・未計算事項](notes/operational-past-signalling-focus.md)

## 通信判定側の成果：選択bitと過去の受信記録

**受信器の測定作用と選択記録を含めて計算。** bitを0・1それぞれに固定した回路では、例として固定点の距離 `48/73` が得られます。しかし一つの記録付き混合実験を指定したDeutsch product処方で解くと、`P(b,y)=1/4`、bitとの相関は0です。初期相関を許す別処方では、同じ周辺固定点でも非零の相関が得られます。**どの相関・接続規則が物理から導かれるかを示す必要があり、この有限回路はTaub–NUTから導いた有効理論ではありません。**

**NUT内の受信者を、幾何だけで誤って排除しない。** NUT内の受信者はCTC領域にいるので、chronalな過去の受信者への帰還禁止をそのまま適用できません。ここを検討対象として残します。Taubから装置を持ち込むことや、CTCを最初から作ることは追加の問題として区別します。経路が書けることは、時計・記憶・駆動装置の実現や、量子場側の障害の解消を意味しません。

[詳しい回路・受信事象・適用範囲](notes/chronology-operational-channel-test.md)

### 再現

```bash
python -m pip install -r requirements.txt
# 量子場・確率判定
python src/symbolic/heterotic_taubnut_krw_bridge.py
python src/symbolic/operational_past_signal_probability.py
# 受信記録付き回路・NUT内の受信事象
python src/symbolic/chronology_reference_bit_channel.py
python src/symbolic/taubnut_receiver_event_geometry.py
```

幾何・作用・確率行列は厳密代数、Gaussian検出模型の積分は50/80桁で比較。受信記録付き回路は30組のparameterでunitary・Choi・正常化・固定点・選択記録・負例を検査します。**コードのPASSは物理的な過去通信のPASSではありません。** KRWの定理と大域幾何の論証はノートで出典・仮定を明示しており、PythonやLeanによる形式証明とは呼びません。

## 前回までの成果と、次に進む場所

[前回の継続ノート](notes/heterotic-taubnut-operational-continuation.md)には、相対BRST、必要ラベル3組、Taub時間の混合、調整sourceからNUTへの古典スカラー接続を保存しています。[旧6条件監査](notes/heterotic-taubnut-six-gate-audit.md)と[文献対照検算](notes/heterotic-taubnut-literature-bridge.md)も監査履歴です。

**`99.813%` は外側スカラーODEの流束比であり、過去通信の成功率ではありません。** 古い無条件な `BRST / free-string PASS` の解釈は後の監査で訂正されています。

次は状態候補を増やすことより、**必要な一つの物理的な弦の操作・検出器の実時間応答が、局所場の障害をどう回避し、選択記録を含む受信統計をどう定めるか**を調べます。回避や接続規則を仮定で埋めず、過去の検出確率と誤差を計算します。[量子場側の次の課題](notes/operational-past-signalling-focus.md#6-判定と次の課題)と[通信判定側の次の課題](notes/chronology-operational-channel-test.md)§6を合わせて参照してください。

## ブラックホール研究（別テーマ）

こちらは **principal safety**：背景曲率が有限でも、摂動・拘束・運動項・4次元作用へ特異性を移しただけでは解決としません。

| 入口 | 内容 |
|---|---|
| [研究概要](SCREENING_RESEARCH_OVERVIEW.md) ／ [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) | ブラックホール側の成果・引き継ぎ |
| [principal-safe-screening](docs/principal-safe-screening.md) ／ [NOVELTY.md](NOVELTY.md) | 健全性・先行研究との区別 |
| **[量子場・KRWノート](notes/operational-past-signalling-focus.md)** | **局所量子場の障害と、その適用範囲** |
| **[受信記録付き通信判定ノート](notes/chronology-operational-channel-test.md)** | **送受信プロトコルの判定。時間遡行の続きは上のノートと併読** |

## AI・コントリビューターの再開手順とCI

まず [AGENTS.md](AGENTS.md) と [CI運用ルール](docs/ci-policy.md) を読んでください。時間遡行の続きは上の二つのノートから。旧6条件の全分類やブラックホール側へ自動的に戻らないでください。通常PRでは累積差分を検査し、独立scriptはPython 3.12、共有依存・データ・影響不明は全件へ拡大します。文書のみならリンク検査。Leanは関連変更時に実行します。

[PR checks](.github/workflows/pr-checks.yml) が対象と理由を記録し、[Symbolic CI](.github/workflows/symbolic-ci.yml) は週次・手動の全件再現性を検査します。精度・assertを弱めず、無関係な重複実行を減らします。

```bash
# コミット済みPRの累積差分（未コミット変更は含まれません）
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは [Apache-2.0](LICENSE)、研究文章・式・図は [CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・未解決の物理を区別して記録します。
