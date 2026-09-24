# Spacetime Screening

**研究目的：現実の3+1次元時空に、送信者が選んだ情報を過去へ届ける通信路を作れるか。**
幾何、支える量子物質、有限の装置、受信記録を同じ物理過程として成立させることを目指します。

## 重点Bの継続v5：二入力の制御と、非平衡な準備雑音

> **Aは未取得です。全SAの量子状態・過去の受信確率を未計算のまま成功扱いにはしていません。**
> 四次元RN内部では、二つの入力を変えれば、指定した二つの地平面出力を逆算できます。
> **次の難所は、その二入力を一人の外部送信者が準備できるかと、大域量子状態の構成です。**

| 今回の結果 | 意味と限界 |
|---|---|
| **全周波数の逆設計を利用** | 既存の4D散乱定理から有限Killingエネルギーの二入力を構成。有限周波数ODEも別実装で照合。地平面の全正則性や外部からの製造は未証明 |
| **片側だけの操作で代替？** | 反射側の信号差を全て零にする設計では不可。事前もつれだけでも、触らない入力の平均を変えられない。全通信方式の禁止ではない |
| **雑音を含む非平衡な準備** | 正のGaussian混合から追加共分散と全相対応力を導出。特定の準備雑音も第一尾を追加しない族があるが、基準状態の量子雑音は残る |
| **滑らかな有限パルスを改善** | 同じ台・積分値・第一尾相殺で、前回波形の入力エネルギーを約36.53%削減。受信誤り率や装置の総仕事を固定した比較ではない |
| **文献の重要な留保** | Taylorの正則状態にはLorentzian継続・物理解釈の未解決点がある。完成した全SA状態として移植しない |

**[研究ノート・式・出典・適用範囲](notes/sa-two-input-state-v5.md)** ／ [計算](src/symbolic/sa_two_input_state_v5.py) ／ [別実装の検算](src/symbolic/sa_two_input_state_verify_v5.py)

今回も一件のBの継続。未取得の過去分布はnullです。配布時点はローカル検算のみで、remote CI・PR・マージは未実施です。
原A基準と人間審査は維持し、以下の既存成果は全て保存しています。

---

## 二荷電殻の量子通信を検査 — v4（前回配布物の収録）

> **全経路の量子状態と、過去側の受信確率はまだ未取得です。今回の分類は A=0 / B=1 / C=2。**
> Schein–Aichelburg型の二荷電殻について、4Dの場の接合、特異境界での反射、有限時間の受信則を計算しました。
> **古典的な経路があることと、量子的な通信装置として成立することを分けています。**

| 今回確かめた部分 | 結果 |
|---|---|
| **殻を越える場の条件** | 4D波動方程式・時計対応・法線流束を照合。これだけでは大域量子状態は決まらない |
| **RN内部の特異点** | 二つの有限エネルギー境界条件で反射位相が変わる。両方が全SAで実現するとは未証明 |
| **一つの温度で両地平面を正則にする案** | **指定した平衡準備では不成立**。非平衡状態・片側の有限実験までは排除しない |
| **0と1の読み出し** | 等エネルギーの符号反転はエネルギー測定だけでは読めない。有限時間Ramsey測定の確率法則を導出 |
| **実際の過去通信確率** | **未計算・null**。必要な全SAの応答核と二点関数は未供給。局所真空の雑音対照を代入しない |

**[研究ノート：全式・境界条件・出典](notes/sa-quantum-record-v4.md)** ／ [候補台帳](architecture/sa-quantum-record-v4.json) ／ [再現workflow定義](.github/workflows/sa-quantum-record-v4.yml)

前回配布の計算・台帳・ノートを収録しました。現在のCI状況はPRのチェック欄に記録します。
ノート§7の未反映記載は元の配布時点の履歴です。PR #22・#23の内容を保持し、候補全体のBと限定的なCを区別しています。

---

## 継続v3：同じ外部空間への帰還と、四次元量子支持源

> **今回の追加分類：A=0 / B=1 / C=1。過去通信の完成例は未取得です。**
> 同じ外部空間の二口をつなぐ古典例で、実際に出発前へ帰還する経路と、必要な荷電殻の全応力を計算しました。
> **ただし負の支持源と時間差は入力です。人間が制御して作った量子通信路ではありません。**

| 今回詰めた部分 | 結果と範囲 |
|---|---|
| **消せない時間差と帰還経路** | **B**：一つの四次元MP外部を直接接合。指定した時間差で同じ実験室へ出発前に戻る古典経路。殻の負エネルギー・圧力・電荷も計算 |
| **有限厚さRNを中性自由共形場だけで支える** | **C**：指定した滑らかな形状はtrace方程式の遠方のべきが不一致。量子状態の選び直しだけでは救えない |
| **禁止の外側は？** | 計量の遠方応答、荷電・相互作用・質量付きの場、別の形状は別問題。実際にlapseを変えると先頭のtrace不一致は消せるが、完成解ではない |
| **受信確率とA判定** | 未計算の過去分布はnull。前回のRN安定性を新しい非球対称の殻へ移さず、異なる二模型を一台の装置として扱わない |

**[最新ノート：全導出・出典・37点の検算・残る課題](notes/charged-source-handle-v3.md)** ／ [候補台帳](architecture/charged-source-handle-v3.json) ／ [専用Actions](.github/workflows/architecture-charged-completion.yml)

原A基準と人間審査は維持。今回のBは古典構成の条件付き候補であり、正常な量子支持源・有限装置・時間差の形成・過去の受信記録は未構成です。

---

## Aを目指した継続：電荷付き四次元の候補

> **今回の追加分類：A=0 / B=1 / C=1。Aの成功基準は変更していません。**
> 電荷を加えると、前回のSchwarzschild型と異なり、EOS勾配0〜1でも半径方向に安定な喉が得られます。
> **ただし、正常な量子支持源・全装置・過去の受信確率はまだ構成していません。**

| Aへ向けて検査した部分 | 結果 |
|---|---|
| **電荷付き薄殻の安定性** | 1,890組を検査。外部として有効な1,620組中179組が半径方向安定。非極限の開領域も厳密に証明 |
| **状態方程式を具体化** | 内部モードが正の運動項を持つ表面有効作用は書ける。ただし負の真空エネルギー項の4D量子起源は未供給 |
| **負の支持源を小さくする極限** | proper energyは減るが、光学的通過時間は発散し、正規化した径方向null積分は負のまま |
| **時計差だけで過去へ送れるか** | 別々の外部を一度つなぐ一定時計差は消去可能。真の過去向き経路には別の大域構成が必要 |

**[最新ノート・実在論文・再現手順](notes/rn-a-target-candidate.md)** ／ [候補台帳](architecture/rn-a-target-v2.json) ／ [専用Actions](.github/workflows/architecture-rn-search.yml)

179点は179台の時間機械でも成功確率でもありません。既知の電荷安定化の再現と、量子支持・時計接続の適用範囲の検査です。
A主張は引き続き人間の審査が必要で、自動マージしません。初回バッチと以前の研究結果は以下に保持します。

---

## 重点B：二荷電殻の量子通信と、有限パルスの地平面検査

> **過去の受信確率はまだ未取得。AではなくBの継続です。**
> 四次元の場の接合条件と、送信0・1／有限受信器の条件付き確率式まで接続しました。
> **有限時間の入力でも散乱尾が生じます。その最初の尾を打ち消す波形を得ましたが、微小な誤差で復活します。**

| 今回の前進 | 限界 |
|---|---|
| 二荷電殻で場の値・法線微分・時計・KG流束を接続 | 大域的な量子状態とsource応答は未取得 |
| 近極限の内部電荷 `Q/M=.99` と、先頭散乱尾を消す有限パルス | 相殺は一つの極だけ。全地平面・全量子雑音の正則性ではない |
| 波形の積分値を保持し、地平面入力エネルギー比 `27.4517` を計算 | 人間の送信器の準備仕事や、等誤り率での最適値ではない |
| 同じ基準状態で0・1を符号化する有限受信記録の式 | 未取得の平均・雑音を自由な数値で埋めず、過去分布はnull |

**[全導出・一次文献・再現・何が未完成か](notes/sa-quantum-channel-gate.md)**

これはSchein–AichelburgのRN内部を通る案です。別のMP直接接合や、以前の地平面なし薄殻の安定性と合成していません。
[コード1](src/symbolic/sa_quantum_channel_gate.py)／[別検算](src/symbolic/sa_quantum_channel_verify.py)。CI成功は過去通信成功でも独立査読でもありません。

---

## 四次元アーキテクチャ探索 — 初回バッチ

> **原プロトコルに沿う探索・記録・反証検査の初版です。7候補／部分構成、2,282計算点で A=0・B=3・C=4。**
> **過去通信の成功例は得ていません。** Bは未検証の仮定が残る候補、Cは指定した範囲での障害です。分類数は自然界の確率ではありません。

| 初回探索 | 判定 |
|---|---|
| 通常の四次元局所source／未時間差接続の回転型 | **C**：それぞれの時間構造では、後の操作が過去の記録を変える経路を作れない |
| Schwarzschild薄殻、EOS勾配0〜1 | **C**：指定した受動的な半径方向安定性を満たさない |
| 同じ薄殻、EOS勾配4へ変更 | **B**：100点中14点が半径方向安定。物質・全安定性・過去の確率は未構成 |
| 質量で時刻接続を制御するFKZリング | **B**：負の支持源を仮定した古典的経路。量子装置として未成立 |
| 独立した支柱付きCasimirセルを負の総線源にする | **C**：明記した支持条件では装置全体のエネルギーが正 |
| 別スケールの厚さを持つ四次元collar | **B**：24点中18点が局所平坦QEIの必要条件を通るだけ。自己支持状態は未供給 |

**[科学的結果・実在論文・適用範囲](notes/architecture-search-batch-v1.md)** ／ **[実行手順と未実装範囲](docs/architecture-search.md)** ／ [候補台帳](architecture/batch-v1.json) ／ [原プロトコル](docs/4d-past-signalling-protocol.txt)

台帳から機械可読JSONとMarkdown報告を生成します。全候補を別実装で検算し、未計算の受信確率は0ではなくnullにします。
**A主張は自動clearanceを停止し、人間の審査を必須にします。** この版は自動マージを行いません。
反証検査は同じ作成者による別プログラムであり、独立研究者の査読ではありません。全模型空間の網羅でもありません。

```bash
python -m pip install -r architecture/requirements.lock
python scripts/test_architecture_search.py
python scripts/architecture_search.py run --output /tmp/architecture/raw
python scripts/architecture_verify.py --records /tmp/architecture/raw/candidates.json --output /tmp/architecture/verification.json
python scripts/architecture_search.py finalize --records /tmp/architecture/raw/candidates.json --verification /tmp/architecture/verification.json --output /tmp/architecture/verified --gate
```

[Actions定義](.github/workflows/architecture-search.yml)は生成・候補ごとの反証・報告を分離します。**この配布時点ではローカル検算のみで、リモート実行済みとはしていません。**
既存のNUT・MMP・四次元支持源の成果は以下に保持しています。

---

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
