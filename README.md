# Spacetime Screening

**研究目的：現実の3+1次元時空に、送信者が選んだ情報を過去へ届ける通信路を作れるか。**
幾何、支える量子物質、有限の装置、受信記録を同じ物理過程として成立させることを目指します。

## 現在地 — 2026-09-24：量子状態から、装置と初期重力応答まで

> **正常な四次元量子場で、喉が要求する密度と全圧力を一点では再現できました。**
> 前回の球対称波束の圧力不一致は、異方的なスクイーズ波束で改善できます。
>
> **ただし、その同じ状態から重力を求めると、今回できたのは通常空間の極微小な初期摂動です。ワームホールや過去通信路を生成したわけではありません。**
>
> 持続する支持源についても、有限Casimir装置と、滑らかな負の線源の四次元量子応力を検査しました。
> **人間が制御可能な過去通信装置は未成立。自然界全方式の禁止ともしていません。**

| 今回の問い | 結果 |
|---|---|
| **正常な量子場で、密度だけでなく全圧力を合わせる？** | **一点では可能。** 正規化されたスクイーズ状態から全応力を計算 |
| **その状態が実際に作る重力は？** | **先頭Gで初期拘束・初期加速度まで構成。** 1m喉の一点一致でも共形因子の変化は全空間で `4.19×10^-35` 未満 |
| **有限Casimir装置を負の全支持源にする？** | **指定した独立セルでは不可。** DEC支柱のエネルギーは負の真空エネルギーの3倍以上 |
| **負のstringを滑らかにし真空で支える？** | **指定した四次元共形coreに障害。** 一Maxwellの低曲率自己支持は不可。指定profileは全厚さでtrace不一致 |
| **全4Dの支持法も禁止した？** | **いいえ。** 有限ring全体、別の物質・境界・大N・全時間発展を一括して否定しない |

**[最新ノート：状態構成・初期Einstein方程式・有限装置・四次元traceと出典](notes/four-dimensional-source-completion.md)**

## 肯定的に進んだ点：同じ状態から重力まで計算

通常の質量ゼロscalarの異方的波束をスクイーズすると、原点で

```math
\langle T_{\hat a\hat b}\rangle=\mathrm{diag}(-A_s,-A_s,A_s,A_s),
\qquad A_s=\frac{4(1-e^{-2s})}{\pi^2a^4}>0
```

を作れます（`hbar=c=1`）。Ellis喉の全応力比と一致します。
ただし状態全体のエネルギーは正で、中央の負値は短時間です。
1m喉への一点一致・s=.5では、波束幅は約 `6.40×10^-18m`、中心負値の時間幅は約 `5.86×10^-27s`。

同じ状態の密度から、3+1形式の先頭Gで

```math
\nabla^2\chi=-2\pi G\rho,\qquad \gamma_{ij}=(1+\chi)^4\delta_{ij}
```

を異方性を残して解きました。運動量拘束と全初期Einstein成分を満たす加速度も確認しています。
**得たのはR³上の微小な初期摂動です。** 全時間の半古典解、揺らぎの制御、局所pump、空間の位相の生成は未完成です。

## 支持源の障害：負の真空部分だけを取り出さない

**有限の平行板Casimir装置**では、引力を支える支柱も重力源です。支柱にDECを課す範囲で

```math
E_{\rm strut}\ge3|E_{\rm Cas}|,\qquad E_{\rm all}\ge2|E_{\rm Cas}|>0.
```

これは[Costa–Matsasの四次元論文](https://arxiv.org/abs/2112.08881)の結果を再現したものです。
全Casimir幾何の禁止でも、正の全質量を持つ全ワームホールの禁止でもありません。

**滑らかな負のconical core**は、境界のない自由共形場の四次元Weyl anomalyで検査しました。
明記した直線product計量と減衰条件では

```math
\sup(-R)\,\ell_P^2\ge\frac{6\pi}{c_W}
```

が必要です。一Maxwellなら右辺は `60 pi`。検査したprofileは、遠方のtraceのべきも合いません。
**有限toroidal ring、質量付き・minimal scalar、境界、大N全体へこの禁止を拡大しません。**

## 実在する別の四次元候補

Kainの[量子化Einstein–Dirac–Maxwellワームホール](https://arxiv.org/abs/2308.00049)は、正常なフェルミオンを使う静的な候補です。
一方、[調べた初期値の時間発展ではブラックホール形成と信号の捕捉](https://arxiv.org/abs/2305.11217)が報告されています。
静的解、全繰込み応力、安定化された装置は別の確認事項です。今回その数値解は再実行していません。

## 再現と検証の範囲

```bash
python -m pip install -r requirements.txt
python src/symbolic/scalar_4d_squeezed_support.py
python src/symbolic/scalar_4d_semiclassical_initial_data.py
python src/symbolic/casimir_4d_finite_apparatus.py
python src/symbolic/ring_4d_conformal_core.py
```

全応力・保存・初期Einstein成分・四次元不変量・traceを厳密代数で検算し、独立した50/80桁の積分を照合します。
SI定数や近似の物理精度が80桁になるわけではありません。
**CI成功は検算の成功で、独立査読・Lean形式証明・過去通信の成功ではありません。**

## 保存：前回の四次元の経路・支持・信号

[前回ノート](notes/four-dimensional-controlled-past-channel.md)の全計算を維持します。
[FKZのring論文](https://arxiv.org/abs/2305.03887)には、既存の特殊ワームホールの片口を正の質量で囲み、時刻接続を変える古典構成があります。
必要な負の線源 `mu=-c^4/(4G)` と非自明な位相を人間が作れるかは別問題です。
球面薄殻の部分波散乱と未来側の無条件受信分布も保存しますが、**別幾何の透過率をringの時間式へ掛け、一台の装置にはしません。**

## 保存：MMPの先頭近似

[MMPの時間差・相対モード・Roman ring](notes/mmp-timeshift-relative-mode-audit.md)と[状態非依存QEI](notes/mmp-negative-null-energy-audit.md)を保存しています。
固定した時間ホロノミー・透明なunitary 2D CFT・先頭JT・直接null通過という模型では、必要な負の積分に対して `I_total>=0`。
同じ支持場の状態を変えるだけでは救えません。**この限定結果を四次元の別の支持源へ流用しません。**

## 保存：Taub–NUT固定背景スカラー模型

**指定した周期的NUT全体に、通常の局所交換関係／Hadamard条件を保つ大域的自由スカラー場を置く案は、模型内で不成立。**
[自己帰還null測地線の禁止証明](notes/nut-null-return-obstruction.md)を維持します。
同じ事象へ異なる共変運動量で帰還する光路が、局所量子場の特異性条件と矛盾します。

| 保存した量 | 値・検証 |
|---|---|
| 出発・帰還の位置 | `x ≈ 14.20651030656` |
| 最大半径 | `x ≈ 53.28138841256` |
| 閉合 | fibre座標1周期、角方向3周、径方向運動量は反転 |
| 存在保証 | 整数区間演算・剰余評価・中間値の定理。光路は `12<x<64` |

古典ODE解の消失ではなく、大域的な通常の量子媒体への完成の不成立です。
完全な弦理論・計量変更・自然界一般へ拡大しません。独立査読・Lean形式検証は未実施です。

## 以前の結果と適用境界

| ノート | 保存した成果 |
|---|---|
| [環境付き戻り経路](notes/nut-reservoir-return-audit.md) | 密閉型の障害、減衰対照、NUTの古典的外向き放射応答 |
| [場・背景source](notes/field-feedback-background-response.md) | 非Gaussianな場・応力差、保存型の障害、dilaton Ward項 |
| [接続検査](notes/chronology-loophole-attack.md) | 自由なフィードバックの条件付きno-go、周期軌道と自己帰還区間の区別 |
| [場・送受信器](notes/taubnut-field-detector-closure.md) ／ [KRW](notes/operational-past-signalling-focus.md) | 局所の同時確率、Taub準備での地平面の障害 |
| [CTC回路](notes/chronology-operational-channel-test.md) ／ [初期継続](notes/heterotic-taubnut-operational-continuation.md) | 処方と通信の区別、状態候補・古典接続 |
| [旧6条件](notes/heterotic-taubnut-six-gate-audit.md) ／ [文献対照](notes/heterotic-taubnut-literature-bridge.md) | 状態代表の訂正、条件付きLean補題、別模型の接合 |

**99.813%は外側スカラーODEの流束比で、過去通信の成功率ではありません。** 会話の「可能10%」も校正された統計ではありません。

## ブラックホール研究（別テーマ）

**principal safety**：背景曲率が有限でも、病理を摂動・拘束・運動項・四次元作用へ移しただけでは解決としません。
[研究概要](SCREENING_RESEARCH_OVERVIEW.md) ／ [引き継ぎ](RESEARCH_HANDOFF.md) ／ [判定基準](docs/principal-safe-screening.md) ／ [NOVELTY](NOVELTY.md)。

## AI・コントリビューターのCI手順

[AGENTS.md](AGENTS.md)と[CI運用ルール](docs/ci-policy.md)を最初に読んでください。
通常PRは累積差分の影響対象を検査。独立scriptはPython 3.12、共有依存・入力・影響不明は全件へ拡大します。
[PR checks](.github/workflows/pr-checks.yml)と[Symbolic CI](.github/workflows/symbolic-ci.yml)を分離し、assert・精度を弱めません。

```bash
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは[Apache-2.0](LICENSE)、研究文章・式・図は[CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・仮説・未解決の物理を区別して記録します。
