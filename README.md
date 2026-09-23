# Spacetime Screening

**知りたいこと：送信者が選んだ情報を、実際に過去の受信者へ届けられるか。**
CTCの幾何、場の物理性、送受信記録の確率を区別して調べます。ブラックホールの特異点回避は別テーマです。

## 判定 — 2026-09-23

> **今回の固定背景スカラー模型では、過去通信案を「不可」として閉じます。**
>
> 指定した周期的Taub–NUT背景の内部で、**同じ事象へ違う運動量で戻る光の測地線**を構成しました。この経路に沿う特異性の伝播が、通常の局所交換関係・Hadamard条件と矛盾するため、必要な大域的スカラー量子場が存在しません。
>
> **地平面を渡ることや、密閉した環境を仮定しない否定です。** 外へ放射する環境を同じ自由場で完成する案にも適用されます。ただし、**完全な弦理論や自然界一般の過去通信を否定したわけではありません。**

| 対象 | 現在の判定 |
|---|---|
| **この模型のスカラー場で過去通信する** | **不可。** 同じ背景・大域的波動方程式・通常の局所条件が両立しません |
| **Taubを避け、NUT内部だけで装置を作る** | **同じ大域的自由場を使う限り不可。** 今回の証明は地平面を使いません |
| **放射を外へ逃がす量子環境を使う** | **同じ自由場による大域完成は不可。** 証人の光路は外部 `x>2` の内部だけを通ります |
| **初期相関・非Gaussian状態・測定記録による回復で救う** | **同じ場の方程式と局所条件を保つ限り救えません。** 特定の密度行列や戻り回路に依存しない障害です |
| **CTCの幾何や古典的な放射も消えたか** | **いいえ。** それらの存在と、健全な量子場・通信装置の存在は別です |
| **完全なheterotic string／自然界全体** | **今回の禁止の対象外。** 非局所性・全相互作用・計量変更まで解いた結果ではありません |

**[最新の証明：NUT内部の自己帰還null測地線と、模型内no-go](notes/nut-null-return-obstruction.md)**

## 何が決め手になったか

以前の「内部に閉じたnull測地線はない」は、**同じ位置・同じ方向で滑らかに周回する軌道**についての結果です。
今回は、**位置は同じでも、戻ったときの方向が違う測地線区間**を見つけました。前の結果と矛盾しません。

repoの背景 `k=8, delta=sqrt(8/5), lambda=sqrt(2/5)` で、北極側の正則な束座標を使うと：

| 経路の量 | 検算値（無次元） |
|---|---:|
| 出発・再来の径方向位置 | `x ≈ 14.20651030656` |
| 途中の径方向の最大値 | `x ≈ 53.28138841256` |
| 角方向の進み | `Delta phi = 6 pi`（3周） |
| 正則なfibre座標の進み | `Delta t_N = T`（1周期） |
| 径方向の共変運動量 | 始点 `+0.02673063925…`、終点 `−0.02673063925…` |

反射鏡や手で足した戻り写像ではなく、**実際の四次元計量のHamilton方程式を満たす自由null測地線**です。
経路の存在は高精度の根だけに依存せず、**整数区間演算・剰余評価・中間値の定理で保証**しています。全経路が `12<x<64` にあることも区間で確認しています。

## なぜ、この経路で模型を棄却できるのか

通常の局所量子場は、同じ点Pでの二点関数の特異性に、対応した運動量の組 `(P,k; P,-k)` だけを許します。
一方、波動方程式の特異性は光の測地線に沿って伝わります。

```math
(P,\kappa_0;P,-\kappa_0)
\longrightarrow
(P,\kappa_1;P,-\kappa_0),
\qquad \kappa_1\ne\kappa_0.
```

今回の光路はPへ違う運動量で戻るため、**同じ二点関数に、局所条件が禁止する特異性を要求してしまいます。**
分布的な交換子にも同じ矛盾があり、Hadamard性だけ捨てて通常のF-local自由場として救うこともできません。
既知の特異性伝播の議論を、今回の具体的なNUT光路へ適用した結果です。基本定理の新発見や独立査読済みとは主張しません。

**未定義の受信確率を0と置いたのではありません。通信に必要な大域的な媒体そのものが、この模型では成立しないという棄却です。**

## 前回の放射応答は、何が変わったか

前回求めた外向き応答 `Im Y_n>0` は、古典的な波動方程式の結果として維持します。
今回分かったのは、**その応答を持つ通常のスカラー量子環境を、同じ外部NUT領域全体に完成できない**ということです。
光路が `x>12` だけを通るので、`x=2` や無限遠の境界条件を選び直すだけでは、この矛盾を取り除けません。
[外向き応答・環境の前回ノート](notes/nut-reservoir-return-audit.md)は、監査履歴として保持しています。

## 再現

```bash
python -m pip install -r requirements.txt
# 整数区間演算による存在証明書（標準ライブラリのみ）
python src/symbolic/nut_null_return_certificate.py
# 全Hamilton方程式・束の閉合・独立した50/80桁検算
python src/symbolic/nut_null_return_geometry.py
```

**CIは幾何の代数・存在証明書の検査です。** 特異性伝播と局所条件の矛盾はノート中の解析的証明で、PythonやLeanによる形式証明とは区別します。独立査読・Lean検証は未実施です。

## 以前の結果と適用境界

| ノート | 保存した成果 |
|---|---|
| [環境付き戻り経路](notes/nut-reservoir-return-audit.md) | 密閉型の条件付き障害、全一modeの減衰対照、実NUTの外向き放射応答 |
| [場・背景source](notes/field-feedback-background-response.md) | 非Gaussianな場・応力の操作依存性、保存型の障害、dilaton Ward項 |
| [接続検査と反証試行](notes/chronology-loophole-attack.md) | 自由なフィードバックに対する条件付きno-go、滑らかな周期的null軌道の不存在（自己帰還区間は除外しない） |
| [場・送受信器からの判定](notes/taubnut-field-detector-closure.md) ／ [KRW監査](notes/operational-past-signalling-focus.md) | 局所の同時確率、束構造、Taub準備での地平面の障害 |
| [受信記録付きCTC回路](notes/chronology-operational-channel-test.md) ／ [初期の継続](notes/heterotic-taubnut-operational-continuation.md) | 処方依存の固定点と通信の区別、状態候補・古典接続 |
| [旧6条件監査](notes/heterotic-taubnut-six-gate-audit.md) ／ [文献対照](notes/heterotic-taubnut-literature-bridge.md) | 状態代表の訂正、条件付きLean補題、別模型の接合 |

**99.813%は外側スカラーODEの流束比で、過去通信の成功率ではありません。** 主観的な「可能10%」も、今回の結果で校正された数値には変換しません。

## 再開する場合

同じ背景・同じ大域的自由場のまま、別の浴状態や戻り回路を足して再開しません。
[最新ノート§4–5](notes/nut-null-return-obstruction.md)の前提を具体的に変更する必要があります。例えば、経路を含む領域の計量・位相・定義域を変える、または通常の自由場を非局所的・全弦的な理論へ置き換える場合は別問題です。
このモデル内no-goを、全反作用でCTCの幾何が消える証明や自然界の普遍的禁止へ拡大しません。

## ブラックホール研究（別テーマ）

**principal safety**：背景曲率が有限でも、摂動・拘束・運動項・4次元作用へ特異性を移しただけでは解決としません。
[研究概要](SCREENING_RESEARCH_OVERVIEW.md) ／ [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) ／ [判定基準](docs/principal-safe-screening.md) ／ [NOVELTY.md](NOVELTY.md)。

## AI・コントリビューターのCI手順

まず[AGENTS.md](AGENTS.md)と[CI運用ルール](docs/ci-policy.md)を読んでください。
通常PRは累積差分を検査し、独立scriptはPython 3.12、共有依存・入力・影響不明は全件へ拡大します。文書のみならリンク検査、Leanは関連変更時に実行します。
[PR checks](.github/workflows/pr-checks.yml)と[Symbolic CI](.github/workflows/symbolic-ci.yml)を使い分け、既存assert・精度を弱めません。

```bash
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは[Apache-2.0](LICENSE)、研究文章・式・図は[CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・仮説・未解決の物理を区別して記録します。
