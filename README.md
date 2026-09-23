# Spacetime Screening

**研究目的：現実の3+1次元時空に、送信者が選んだ情報を過去の受信者へ届ける通信路を作れるか。**
計量の存在、支える量子物質、準備と制御、受信記録の確率を分けて検証します。

## 現在地 — 2026-09-24：四次元で計算した結果

> **実在する四次元論文を使い、幾何・必要な全応力・負エネルギー状態・信号の散乱・質量による時計制御を具体化しました。**
>
> **条件付きの古典的過去経路は書けます。しかし、人間が作れる物理的な過去通信装置は、まだ成立していません。** 特殊なワームホールを支える負の重力源と、その量子状態を保った時刻接続を供給できていません。
>
> **二次元の禁止式を四次元へ流用した結果ではありません。** 滑らかな巨視的な喉は通常スカラーの短時間QEI診断で不適合ですが、薄層や別のring幾何へ、そのまま同じ上限を当てません。

| 四次元で調べた部分 | 結果 |
|---|---|
| **幾何と必要な物質** | 球対称の喉の全Einstein応力を計算。密度だけでなく、径方向・横方向の圧力にも条件があります |
| **通常の量子場で負のエネルギーを作る** | `d³k`で規格化した有限エネルギー状態を構成。ただし今回の状態の圧力・持続時間は支持要求と不一致 |
| **人が制御する質量で時間差を作る** | Frolov–Krtouš–Zelnikov（2023）のring模型の時刻接続を再現。ただし負のstringと既存の位相を仮定しています |
| **情報が喉を通るか** | 球面薄殻の部分波散乱、有限時間source、未来側の無条件受信分布を検算。過去側の同時確率ではありません |
| **現実の装置として採用できるか** | **未成立。** 負の支持源・形成・安定性・量子反作用・過去の記録まで、一つの実験として完成していません |

**[最新ノート：3+1次元の全導出・文献・数値・適用範囲](notes/four-dimensional-controlled-past-channel.md)**

## 条件付きの肯定：正の質量による時計制御

[Ring wormholes and time machines — Frolov, Krtouš, Zelnikov (2023)](https://arxiv.org/abs/2305.03887) は、同じ外部空間に二つの口を持つ既存のringワームホールについて、片口を囲む正の質量shellから、物理的な時刻接続を導きます。
弱場・遠い口という近似で、shell質量M、ring半径a、shellの短半軸R、口の距離Lについて

```math
I_C\simeq\frac{GM}{ac^2}\left[\arctan\frac aR-\frac aL\right],
\qquad t_3-t_0=B_{\rm opt}-(e^{I_C}-1)t_2.
```

後者が負なら、同じ外部の出発位置へ送信前に戻る古典的経路になります。時計の表示替えではありません。
ただし、この模型のringは**負の線エネルギー `mu=-c^4/(4G)`**を要求します。正の質量を配置できることは、この異常な支持源を製造できることを意味しません。
**球面喉の透過率とringの時間式は別幾何です。掛け合わせて一台の成功例にはしません。**

## 支持源の診断：四次元では全応力と時間幅が重要

滑らかなEllis喉では、半径bに対し中央の密度は `rho=-c^4/(8 pi G b²)`。
1mなら約 `-4.82×10^42 J/m³` が必要です。これは必要なsourceであって、支払えば製造できる費用ではありません。

通常の四次元scalarのtimelike量子エネルギー不等式を、境界のない短時間・局所平坦近似で使うと、`cT=f b` に対して

```math
b\lesssim\sqrt{N\pi^3/6}\,\ell_P/f^2.
```

N=1、f=.01の単一スケール診断では `b≲3.67×10^-31m`。
**曲率補正を全て制御した絶対定理でも、全物質への禁止でもありません。** 薄層epsilonを持つ別のcollarでは、対応する必要条件は `epsilon³≲N pi³ ell_P² b/(12 f⁴)` です。1mの喉で約 `4.07×10^-21m` という薄層スケールが残りますが、実現する状態は未構成です。
[Ford–Romanの四次元制約](https://arxiv.org/abs/gr-qc/9510071) ／ [Fewster–Evesonのtimelike QEI](https://arxiv.org/abs/gr-qc/9805024)

## 再現

```bash
python -m pip install -r requirements.txt
python src/symbolic/wormhole_4d_geometry_support.py
python src/symbolic/scalar_4d_negative_packet.py
python src/symbolic/wormhole_4d_signal_scattering.py
python src/symbolic/ring_4d_mass_clock_control.py
```

全四次元metric・応力保存・部分波を厳密代数で検算し、独立した50/80桁の運動量積分、エネルギー、球Bessel接合、受信分布を照合します。
SI定数の入力精度や近似誤差が50桁になるわけではありません。CIはこれらの式の再現検査で、過去通信の成功・全4D解・独立査読・Lean形式検証を意味しません。

## 保存：MMPの先頭近似で何を閉じたか

[MMPの時間差・相対モード・Roman ring](notes/mmp-timeshift-relative-mode-audit.md)と[状態非依存QEI](notes/mmp-negative-null-energy-audit.md)を保存しています。
固定した時間ホロノミー・透明なunitary 2D CFT・先頭JT・直接null通過という模型では、必要な負の積分に対し `I_total>=0`。同じ支持場の状態を準備し直すだけでは救えません。
**この限定結果は、今回の四次元の別の支持源を禁止する根拠としては使いません。**

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
通常PRは累積差分の影響対象を検査し、独立scriptはPython 3.12、共有依存・入力・影響不明は全件へ拡大します。
[PR checks](.github/workflows/pr-checks.yml)と[Symbolic CI](.github/workflows/symbolic-ci.yml)を分離し、assert・精度を弱めません。

```bash
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは[Apache-2.0](LICENSE)、研究文章・式・図は[CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・仮説・未解決の物理を区別して記録します。
