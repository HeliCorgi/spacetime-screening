# Spacetime Screening

**知りたいこと：送信者が選んだ情報を、実際に過去の受信者へ届けられるか。**
CTCの幾何、場の物理性、送受信記録の確率を区別して調べます。ブラックホールの特異点回避は別テーマとして保存しています。

## 今回の結論 — 2026-09-23

> **測定・コピー・反転を接続したときの、場の状態変化と応力まで計算しました。**
>
> **新しく棄却した構成：** 送信に使う場の観測量Aを、そのまま保存して戻す周回装置。測定が加える量子雑音はコピーでも反転でも消せず、非零の交換子がある限り、通常の正則な固定状態がありません。
>
> **過去通信全体の不可能性ではありません。** 実際のNUTの戻り写像や全背景応答を解いたわけではなく、損失・観測量の混合・場と装置の初期相関がある構成は別に検証が必要です。

| 調べたこと | 現在の答え |
|---|---|
| **コピーとNOTで場は本当に変わる？** | **変わります。** 測定結果に基づく制御は、量子揺らぎと背景を駆動する応力を操作ごとに変えます |
| **同じAを保存して戻す装置で周回できる？** | **明記した模型では不可。** Gaussian近似によらず、正則な周回固定状態がありません |
| **損失を入れても全て不可能？** | **そこまでは言えません。** 正の環境雑音付き減衰模型では、一つの観測量に有限の定常分散が残ります |
| **背景の応答も全部解けた？** | **スカラーの応力・dilaton sourceまで。** 全計量・装置・環境・弦の反作用解は未導出です |
| **小さな反作用でCTCは必ず消える？** | **いいえ。** NUT内部の厳密にtimelikeな閉曲線は十分小さい計量摂動で残ります |
| **選んだ情報を過去へ送れた？** | **まだ成功例は得ていません。** 下の計算は物理的な大域NUT通信確率ではありません |

**[最新ノート：場の応答・応力・固定状態不存在の証明・残る条件](notes/field-feedback-background-response.md)**

## 核心：測定の影響は「古典波を加える」だけではない

同じ場の受信測定から得た記録yを、後の送信制御へ渡します。固定0／固定1／コピー／NOTを、全結果を保持する正規化された量子操作として計算しました。

コピー／NOTの後の場は一般にGaussianではなく、**connected二点関数も変化**します。これは「処方された古典sourceだけではconnected二点関数を変えない」という先行結果とは別です。測定と条件付き操作を含めた違いです。

一方、送信に使う場の観測量Aについては、どの制御方式でも厳密に

```math
\mathcal E_f^*(e^{isA})=\cos(s\Delta_{AB})e^{isA},
\qquad \operatorname{Var}'(A)=\operatorname{Var}(A)+\Delta_{AB}^{\,2}
```

となります。右の分散式は二次モーメントが有限な場合です。
**戻り部がAを変えないなら、この雑音が一周ごとに加わります。** 左の式から、無限分散へ逃げても正則な固定状態がないことまで証明しました。時空の周期性だけで、実際の戻り部がこの仮定を満たすとはしていません。

## 背景への影響：操作依存の応力と、その限界

コピーとNOTは、場の相関を通じて異なる応力を作ります。局所の正当な場理論で、その差を同じ背景上のpoint splittingから求めました。符号は一律に正ではありません。

Taub–NUTの実際の計量・dilatonを使う検算では、**元のスカラー応力だけを、保存された重力sourceとして使えない**ことも確認しました。dilatonとのエネルギー交換、装置の応力、環境の雑音が必要です。これらを落として「反作用を解いた」とはしません。

また、小さな計量摂動は内部CTCを必ず消すわけではありません。**場の状態が不整合になることと、幾何のCTCが消えることは別の結果です。**

## 検算の対照値

正準量子系 `A=0.7P, B=0.6Q`、初期分散1/2の独立な波動関数積分では：

| 操作 | Qの二次モーメント | Pの二次モーメント |
|---|---:|---:|
| 固定0／固定1 | 0.99 | 0.86 |
| コピー | 0.4039518861 | 0.86 |
| NOT | 1.5760481139 | 0.86 |

**これは式を検証する比較模型で、Taub–NUTの通信成功率ではありません。** コピーとNOTで応答が異なる一方、制御できない方向の測定雑音は共通に残ります。

## 再現

```bash
python -m pip install -r requirements.txt
python src/symbolic/field_feedback_backreaction.py
python src/symbolic/taubnut_feedback_stress.py
```

Weyl演算子・応力・保存則は厳密演算。無限次元の波動関数による独立積分と幾何学的対照値を50/80桁で照合します。積分のGaussian尾部には解析的上界を置いています。Fock cutoffではありません。
**CI成功は実装した検算の成功で、自然界の過去通信の成功／普遍的不可能性の証明ではありません。**
会話の「可能10%」は主観的な見立てであり、今回の結果から校正された事後確率には変換していません。

## 以前の結果と適用境界を保存

| ノート | 保持している結果 |
|---|---|
| [逃げ道の反証・接続検査](notes/chronology-loophole-attack.md) | 操作非依存の線形processに自由なフィードバックを接続する条件付きno-go。第一NUT内部に閉じたnull測地線はないという反証限界 |
| [場・送受信器からの判定](notes/taubnut-field-detector-closure.md) | 記録付き局所確率、NUTの遅延核の選別不能性、Hopf束、Taub準備の固定背景局所場案の棄却 |
| [量子場・KRW](notes/operational-past-signalling-focus.md) | 指定地平面のF-local／Hadamard延長の障害、古典sourceの限界、後選別の偽陽性 |
| [受信記録付きCTC回路](notes/chronology-operational-channel-test.md) | 特定のDeutsch product処方での記録相関0。Taub–NUTの有効理論ではない |
| [前回の継続](notes/heterotic-taubnut-operational-continuation.md) | 相対BRST、必要ラベル3組、地平面の混合、調整sourceによる古典接続 |
| [旧6条件監査](notes/heterotic-taubnut-six-gate-audit.md) ／ [文献対照検算](notes/heterotic-taubnut-literature-bridge.md) | 状態代表の訂正、条件付きLean補題、別模型のcoset接合と複素振幅 |

**99.813%は外側スカラーODEの流束比で、過去通信の成功率ではありません。** 古い無条件なBRST／free-string PASSの解釈は後の監査で訂正されています。

## 次の再開点

[最新ノート](notes/field-feedback-background-response.md)の§4–7から。保存型の戻り部は棄却し、実際のNUTでAを混合・減衰させる戻り写像と、その環境・装置・dilaton sourceの同時整合性が次の検証対象です。
比較模型の減衰率をNUTの予測と見なさず、記録flag・全場の正値性・大域gluing・過去の受信確率を区別します。
全BRST／全スペクトルの分類、新規CTC形成、入力状態の完全保存を自動的な先行必須条件には戻しません。

## ブラックホール研究（別テーマ）

こちらは**principal safety**：背景曲率が有限でも、摂動・拘束・運動項・4次元作用へ特異性を移しただけでは解決としません。
[研究概要](SCREENING_RESEARCH_OVERVIEW.md) ／ [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) ／ [判定基準](docs/principal-safe-screening.md) ／ [NOVELTY.md](NOVELTY.md)。

## AI・コントリビューターのCI手順

まず[AGENTS.md](AGENTS.md)と[CI運用ルール](docs/ci-policy.md)を読んでください。
通常PRでは累積差分の影響対象を検査します。独立scriptはPython 3.12、共有依存・データ・影響不明は全件へ拡大。
文書のみならリンク検査、Leanは関連変更時に実行します。
[PR checks](.github/workflows/pr-checks.yml)が対象と理由を記録し、[Symbolic CI](.github/workflows/symbolic-ci.yml)は週次・手動の全件再現性を検査します。精度・assertを弱めません。

```bash
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは[Apache-2.0](LICENSE)、研究文章・式・図は[CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・仮説・未解決の物理を区別して記録します。
