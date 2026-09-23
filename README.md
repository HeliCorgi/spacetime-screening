# Spacetime Screening

**研究目的：送信者が選んだ情報を、実際に過去の受信者へ届けられるか。**
CTCの幾何、物理的な媒体、受信記録を区別します。NUTの結果を保存し、別系統のワームホール案を検証しています。

## 今回：MMPワームホール + 時間差 + 低エネルギー相対モード

> **選んだ組合せを具体的に計算しました。標準Casimir真空を用いる先頭次数の受動構成では、過去通信は成立しません。**
>
> 相対モードは情報を運ぶ候補として残ります。しかし、時間差を入れた真空のエネルギー流まで喉の重力方程式へ入れると、**信号が入る時の入口と、出る時の出口を同時に保つ条件が、過去への到着条件と両立しません。**
>
> **全4D動的ワームホール・全量子状態・自然界全体の禁止ではありません。** 標準NS真空、近AdS2/JTの先頭近似、自由なmassless相対モードの直接通過を検証した結果です。

| 組合せの要素 | 今回の結果 |
|---|---|
| **低エネルギーの相対モードへ0・1を載せる** | 二次有効理論で、総電流を打ち消し、両符号の応力を揃える符号化を確認 |
| **時間差を付けても元の喉を使う** | そのままでは不可。真空の応力と流束が変わり、通過条件は下の不等式に制限される |
| **独立に支えたMMPペアをRoman ringへ並べる** | 各腕が同じ支持条件を保つ限り、一周しても到着は未来 |
| **全ての喉を一つのCasimirループで支える** | 明記した透明な単一ループ模型では、2本以上の喉を同時に支えられない |
| **すべての多口・能動制御・非定常構成も不可？** | 今回の対象外。分岐・複数サイクル・追加の負のnullエネルギーは別に解く必要がある |

**[最新ノート：MMPの時間差付き応力、喉の通過条件、相対モード、Roman ring](notes/mmp-timeshift-relative-mode-audit.md)**

## 決め手となる式

喉の光学的通過時間を `tau_w`、自分自身の二つの口の間の最短外部光行時間を `d>0`、時間差を `Delta>=0` とします。
時間差を入れた支持真空と先頭の重力方程式から、同じ自由null信号の入口・出口を開くには

```math
\Delta<\tau_w-d
```

が必要です。一方、外部経路で元の実験室へ戻って読出しを終えるには

```math
t_{\rm receive}-t_{\rm send}
=\tau_w+d+\tau_{\rm read}-\Delta
>2d+\tau_{\rm read}>0.
```

**高い透過率でも、到着する時刻は過去になりません。**
これは過去通信不能を仮定した式ではなく、時間差付きCasimir応力・共形異常・JTのnull拘束から得た、明記した先頭模型での必要条件です。
同時刻の二つの口の開きではなく、**入口の時刻と、そこから光が到着する出口の時刻**を比較しています。

支持に最も有利な最短ループの例 `tau_w=1,d=1/4` では、通過条件は遅くとも `Delta=0.75` で失われます。一周がnullになる `Delta=1.25` より前です。
これらは無次元比であり、装置の秒数や自然界での成功率ではありません。

## 文献を組み合わせる際に修正した点

MMPの支持源は、磁力線上を動くフェルミオンのCasimir効果です。時間差ゼロの応力を流用せず、左右向きの量子モードの周期を計算し直しました。
時間差を付けると流束が生じるため、**エネルギーを極小化するだけで静的解ができたとは言えません。** 非対角の重力方程式も検算しています。

2026年の透過研究が示す相対モードは、情報担体として保存します。ただし、Roman ringの4Dの幾何学的抑制係数を、この2D支持源や通信確率へ手で掛けることはできません。
[一次資料・採用した前提・全次数へ拡大できない範囲](notes/mmp-timeshift-relative-mode-audit.md)

## 再現

```bash
python -m pip install -r requirements.txt
python src/symbolic/mmp_timeshift_throat_gate.py
python src/symbolic/mmp_relative_mode_ring.py
```

共形異常・全JT成分・flavor変換は厳密代数。null積分・二状態の距離・Roman ringの係数は独立な50/80桁計算で照合します。
時計表示だけの偽の負時間、同時刻の口の比較、null/timelikeループへの真空の不正な解析接続も検査します。
**CI成功は検算の成功で、物理的な過去通信成功や自然界一般の禁止を意味しません。**

## この系統の次の判断基準

同じ受動的な組合せを、透過率や口の数だけ変えて再開しません。
[最新ノート§6](notes/mmp-timeshift-relative-mode-audit.md)で示した、必要な追加の負のnull積分を満たす状態・支持源、または複数サイクル等の別の全構成が必要です。
その存在を仮定で埋めず、量子状態・装置・背景と受信記録を同時に検証します。

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
