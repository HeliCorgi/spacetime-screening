# Spacetime Screening

**研究目的：送信者が選んだ情報を、実際に過去の受信者へ届けられるか。**
CTCの幾何、物理的な媒体、受信記録を区別します。NUTの結果を保存し、別系統のワームホール案を検証しています。

## 今回：負の量子エネルギーを注入すれば、MMPの支持不足を救えるか

> **同じ先頭MMP/JT模型の共形場を、別の量子状態に準備するだけでは救えません。**
>
> **負のエネルギーパルスを持つ正規化された状態は構成しました。** しかし、信号が喉を通る全経路で必要なのは、重み付きnullエネルギーが厳密に負であることです。状態非依存の量子エネルギー不等式と共形異常を合わせると、問題の時間差ではその積分が0以上になります。
>
> **前回の「標準真空では失敗」から前進しました。** 同じ理論の許容される非定常状態・混合・相関でも、この必要条件を越えられません。ただし、**全4Dの装置・別の量子場・境界や時空の変更まで禁止した結果ではありません。**

| 今回の問い | 結果 |
|---|---|
| **負のエネルギーを持つ状態は本当に作れる？** | **理論上の状態として構成。** unitaryな準備とfermion二点関数から応力を求めました |
| **その負値で喉を支えられる？** | **同じ先頭模型では不可。** 必要条件 `I_total<0` に対して、QEIは `I_total>=0` を要求 |
| **もっと強いパルス・非定常状態・量子相関なら？** | 同じCFTの許容状態である限り、下限は状態に依存しません。少数のパルスの探索失敗ではありません |
| **装置のエネルギーを増やせば？** | 有限の準備エネルギーには、さらに厳密に正の下界があります。状態を準備する仕事も計算しました |
| **量子エネルギー不等式は普通の長いMMP解も禁止する？** | **しません。** 信号経路がchiral円周を巻く領域では別の重みが必要で、真空の支持が残ります |
| **自然界の過去通信は全部不可能？** | **今回の結論ではありません。** 2Dの不等式を4Dのnull線へそのまま使うことはできません |

**[最新ノート：状態の構成・準備仕事・QEIによる禁止の証明と適用範囲](notes/mmp-negative-null-energy-audit.md)**

## 決め手：負のパルスの深さではなく、全通過経路の積分

喉の光学的通過時間を `tau_w=pi ell`、共形場の中心電荷を `c` とします。
同じ光信号の入口・出口を開くには、先頭JT方程式から

```math
B_L+B_R=-\kappa I_\rho>0
\quad\Longrightarrow\quad I_\rho<0
```

が必要です。ところが、対応するchiral周期が `L=C+Delta>=2 tau_w` の場合、

```math
I_\rho=\underbrace{\frac c{24}}_{\text{共形異常}}
+2\ell\int_0^{2\tau_w}\sin^2\!\frac v{2\ell}\,
\langle T_{vv}\rangle_\rho\,dv
\ \ge\ \frac c{24}-\frac c{24}=0.
```

**量子論が許す負の平均は、異常項を相殺するところまで。両口を開く厳密な負値には届きません。**
有限エネルギーで `L>2 tau_w` なら正の下界も得られます。円周QEIから導出しており、巻き数やCasimir項を落とした直線の公式の流用ではありません。

自分自身の二つの口の最短外部光行時間が `d>0` なら、問題の条件は `Delta>=tau_w-d` で全支持チャネルに成立します。
従って前回の

```math
\Delta<\tau_w-d,\qquad
 t_{\rm receive}-t_{\rm send}>2d+\tau_{\rm read}>0
```

という制限が、**標準真空だけでなく、同じ共形場への状態準備でも残ります**。
固定時間ホロノミー・透明な共形支持場・直接null通過・先頭近似という範囲は維持します。CTC形成後へ不正に公式を解析接続した結果ではありません。

## 実際に構成した負エネルギー状態

真空へsmoothな共形unitaryを作用させ、負のパルスと周囲の応力を全部保持しました。
`tau_w=1,d=1/4,Delta=1,c=1` の比較では、救済に必要なのは `I_extra<-0.008744855967...`。

| 準備した状態 | 真空に対する追加null積分 | 判定 |
|---|---:|---|
| 弱い共形パルスの一例 | −0.0005802162654 | 支持不足を減らすが、足りない |
| 中心の負値を大きくした別例 | +0.04234814651 | 点ではより負でも、経路平均は悪化 |
| **同じ理論の許容状態全体に対する下限** | **−0.008744855967…以上** | **必要な厳密不等号を越えられない** |

これは実際の装置のジュール数や成功確率ではなく、規格化した理論内の値です。
状態を準備する理想的な2D制御Hamiltonianと、その正の仕事を示しましたが、4DのMMP装置・ポンプの応力まで構成したとはしません。

## MMP・相対モード・Roman ringの先行結果

[前回ノート](notes/mmp-timeshift-relative-mode-audit.md)には、時間差付きCasimir応力の流束、JT全方程式、相対モードの等エネルギー符号化、二つの単純ring構成の監査を保存しています。

相対モードは通常の未来向き通信の情報担体として残ります。**高透過率と、過去向きの通路の支持は別問題です。**
独立に支えたMMPペアの接続と、一つの透明な支持ループの共有は先行の条件で不成立ですが、任意の分岐・複数サイクルの全ネットワークを禁止した結果ではありません。

## 再現と検証の範囲

```bash
python -m pip install -r requirements.txt
# 今回：状態非依存の支持限界、実際の共形状態と準備仕事
python src/symbolic/mmp_negative_null_qei.py
python src/symbolic/conformal_negative_energy_preparation.py
# 同じ研究PRの先行計算
python src/symbolic/mmp_timeshift_throat_gate.py
python src/symbolic/mmp_relative_mode_ring.py
```

JT null拘束・共形異常・円周変換・finite-work bound・fermion point splittingは厳密代数で検算。
独立な50/80桁でnull積分・準備仕事・QEIを照合します。既知のVirasoro表現・QEIの定理と、その適用の解析的証明はノートに記載しています。
**CI成功は実装した検算の成功で、全証明のLean形式検証・独立査読・4Dの完全解を意味しません。**

## この系統を再開する条件

同じ共形場のsqueezing・状態選択・準備仕事だけを変え、今回の支持不足を埋める探索は閉じます。
再検討には、境界／sewingや時間依存幾何を変更する、非共形・高次元の支持源を対応する有効方程式へ入れる、先頭近似外の補正を制御する等、**禁止の前提を物理的に変更する入力**が必要です。
量子エネルギー不等式の次元とdomainを確認し、装置・状態・背景・受信記録を一つの構成として評価します。

## 保存：Taub–NUT固定背景スカラー模型の結論

**指定した周期的NUT全体に、通常の局所交換関係／Hadamard条件を保つ大域的自由スカラー場を置く案は、模型内で不成立。**
[自己帰還null測地線による禁止証明](notes/nut-null-return-obstruction.md)を維持します。地平面を使わず、同じ事象へ異なる共変運動量で帰還する光路が、局所量子場の特異性条件と矛盾します。

| 保存した量 | 値・検証 |
|---|---|
| 出発・帰還の径方向位置 | `x ≈ 14.20651030656` |
| 途中の最大半径 | `x ≈ 53.28138841256` |
| 閉合 | 正則なfibre座標で1周期、角方向3周。径方向運動量は反転 |
| 存在保証 | 整数区間演算・剰余評価・中間値の定理。光路全体は `12<x<64` |

古典的な外向きODE解が消えるのではなく、同じ外部NUT全体に通常の量子媒体として完成できない、という結論です。完全な弦理論・計量変更・自然界一般へ拡大しません。独立査読・Lean形式検証は未実施です。

## 以前の結果と適用境界

| ノート | 保存した成果 |
|---|---|
| [環境付き戻り経路](notes/nut-reservoir-return-audit.md) | 密閉型の障害、減衰対照、NUTの古典的外向き放射応答 |
| [場・背景source](notes/field-feedback-background-response.md) | 非Gaussianな場・応力差、保存型の障害、dilaton Ward項 |
| [接続検査](notes/chronology-loophole-attack.md) | 自由なフィードバックの条件付きno-go、滑らかな周期軌道と自己帰還区間の区別 |
| [場・送受信器](notes/taubnut-field-detector-closure.md) ／ [KRW](notes/operational-past-signalling-focus.md) | 局所の同時確率、Taub準備での地平面の障害 |
| [CTC回路](notes/chronology-operational-channel-test.md) ／ [初期継続](notes/heterotic-taubnut-operational-continuation.md) | 処方と通信の区別、状態候補・古典接続 |
| [旧6条件](notes/heterotic-taubnut-six-gate-audit.md) ／ [文献対照](notes/heterotic-taubnut-literature-bridge.md) | 状態代表の訂正、条件付きLean補題、別模型の接合 |

**99.813%は外側スカラーODEの流束比で、過去通信の成功率ではありません。** 会話の「可能10%」も、校正された統計ではありません。

## ブラックホール研究（別テーマ）

**principal safety**：背景曲率が有限でも、病理を摂動・拘束・運動項・4次元作用へ移しただけでは解決としません。
[研究概要](SCREENING_RESEARCH_OVERVIEW.md) ／ [引き継ぎ](RESEARCH_HANDOFF.md) ／ [判定基準](docs/principal-safe-screening.md) ／ [NOVELTY](NOVELTY.md)。

## AI・コントリビューターのCI手順

[AGENTS.md](AGENTS.md)と[CI運用ルール](docs/ci-policy.md)を最初に読んでください。
通常PRは累積差分を検査し、独立scriptはPython 3.12、共有依存・入力・影響不明は全件へ拡大します。
[PR checks](.github/workflows/pr-checks.yml)と[Symbolic CI](.github/workflows/symbolic-ci.yml)を分離し、assert・精度を弱めません。

```bash
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは[Apache-2.0](LICENSE)、研究文章・式・図は[CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・仮説・未解決の物理を区別して記録します。
