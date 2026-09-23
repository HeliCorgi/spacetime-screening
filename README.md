# Spacetime Screening

**知りたいこと：送信者が選んだ情報を、実際に過去の受信者へ届けられるか。**
CTCの幾何、場の物理性、送受信記録の確率を区別して調べます。ブラックホールの特異点回避は別テーマとして保存しています。

## 現在の結論 — 2026-09-23

> **環境へ雑音を逃がす戻り経路を検証しました。密閉して環境を再利用する案には、前回より広い不成立条件が得られました。**
>
> **ただし、NUTの外側へ放射する経路は塞がれていません。** 実際のスカラー波動方程式から、外向き放射の非零の応答を計算しました。
>
> **過去への情報送信の成功例、自然界全体での不可能性の証明は、どちらも得ていません。** 密閉型の棄却と、開放型に必要な環境・装置・背景の条件を分けます。

| 検証対象 | 今回の答え |
|---|---|
| **環境まで混ぜて戻せば、前回の測定雑音を消せる？** | **明記した密閉構成では不可。** 固定送信時、測定記録を使わない任意のunitary戻りにも、場＋再利用環境の密度行列の固定点がありません |
| **環境を毎回新しくできるなら？** | **比較模型では定常状態を構成可能。** 一つの観測量だけでなく全一modeに有限エネルギー状態が存在。NUTに新品の環境を供給できた証明ではありません |
| **実際のNUTに放射の逃げ先はある？** | **スカラーの外向き応答は非零。** 任意の減衰率ではなく、実計量と明示した外向き境界条件から計算しました |
| **その環境を普通の無記憶bathとして使える？** | **一周での自動採用は不可。** 中性の定常bathにはKilling周期で相関が再来します。局所的減衰と大域的な環境供給は別です |
| **装置・背景込みで過去通信を実現できた？** | **まだ実現していません。** 放射のエネルギー収支は具体化しましたが、全bath状態・装置source・全計量応答・大域的受信確率は未導出です |

**[最新ノート：密閉環境の証明・実NUTの外向き応答・肯定対照・適用範囲](notes/nut-reservoir-return-audit.md)**

## 1. 「捨てた環境」も戻すと、定常状態が成立しない

前回は「送信観測量Aを保存する戻り部」を棄却しました。今回はその制約を外し、場と再利用環境を**任意のunitaryで混合して戻す場合**を調べました。

固定送信では、受信測定を全結果込みで足した操作は二つのunitaryの混合です。固定状態があるなら純度恒等式から両枝の出力が一致しなければならず、非零のWeyl交換子があると正規化・連続性と矛盾します。
**Gaussian性、有限分散、場と環境の無相関性を仮定しない**否定です。

ただし、独立準備の受信probe、密度行列で閉じる循環系、測定記録を戻り部で使わないことが前提です。記録を使う回復、開放無限bath、通常の密度行列に還元できない大域的場の状態まで禁止しません。
有限Fock cutoffの最大混合状態が示す偽の固定点も検査しました。

## 2. NUTの実計量から、放射の応答を計算した

中性スカラーの径方向方程式をexactに解き、無限遠へ外向きの波を選んだときの境界応答を求めました。

```math
\mathcal Y_n(x_b)=(x_b^2-1)\frac{R_{\rm out}'(x_b)}{R_{\rm out}(x_b)},
\qquad \operatorname{Im}\mathcal Y_n=\frac{s_n}{|R_{\rm out}(x_b)|^2}>0.
```

repoの背景で、最小角枝・境界x_b=2の場合：

| 時間mode n | 外向き応答 Y_n |
|---|---|
| 2 | −0.3406003797 + 4.0937865594 i |
| 3 | −0.3198176365 + 6.9176461608 i |
| 4 | −0.3423269307 + 9.3607497789 i |

**これは実際のNUTスカラー作用素の数値で、通信成功率や減衰率ではありません。** 外向き境界条件は候補環境として明記した追加入力です。これだけで正しい大域的retarded核・浴の量子状態・雑音は決まりません。

正の外向きエネルギー流束も得られました。定常・周期的な装置なら、流出を支える仕事や他の境界からの流入が必要です。dilatonとの交換を含むWard恒等式からKillingエネルギー収支を整理しましたが、全背景の反作用を解いたとはしません。

## 3. 成立する減衰模型も、過去通信と区別する

**毎回新しい無相関な環境を供給する**比較模型には、全一modeの正常な定常状態があります。固定0・1は明示的に構成し、コピー・NOTはエネルギー上界とcompactnessで存在を示しました。

しかし同じbathを再利用すると、bathの雑音と場との相関が残ります。またNUTの周期Killing作用に沿う中性の観測量では、相関が一周後に戻ります。普通の無記憶減衰を一周の模型として使うには、環境交換とその相関処理を物理的に説明する必要があります。

別々に選んだ固定状態の受信分布が異なることと、一つの実験で記録した送信bitが過去の受信者へ届くことも区別します。**定常状態の存在だけでは通信成功にしません。**

## 再現

```bash
python -m pip install -r requirements.txt
python src/symbolic/closed_reservoir_return.py
python src/symbolic/nut_outgoing_reservoir.py
```

純度・Kraus・Weyl・環境共分散・径方向ODEは厳密代数で検算。外向き応答と全一mode固定状態の特性関数は50/80桁で照合します。
無限次元の不存在・存在の解析的証明はノートに記載し、有限行列のテストやLean形式証明と同一視しません。
**CI成功は検算の成功で、物理的過去通信の成功／普遍的不可能性の証明ではありません。** 主観的な「可能10%」を今回の検査数で減らすこともしません。

## 以前の結果と適用境界を保存

| ノート | 保持している結果 |
|---|---|
| [場・背景sourceの応答](notes/field-feedback-background-response.md) | コピー／NOTの非Gaussianな場・応力差、A保存型の正則固定状態不存在、dilaton Ward項、小摂動でも残るCTC |
| [逃げ道の反証・接続検査](notes/chronology-loophole-attack.md) | 操作非依存の線形processと自由なフィードバックの条件付きno-go。第一NUT内部に閉じたnull測地線はない |
| [場・送受信器からの判定](notes/taubnut-field-detector-closure.md) | 記録付き局所確率、遅延核の選別不能性、Hopf束、Taub準備の固定背景局所場案の棄却 |
| [量子場・KRW](notes/operational-past-signalling-focus.md) | 指定地平面のF-local／Hadamard延長の障害、古典sourceの限界、後選別の偽陽性 |
| [受信記録付きCTC回路](notes/chronology-operational-channel-test.md) | 特定のDeutsch product処方での記録相関0。Taub–NUTの有効理論ではない |
| [前回の継続](notes/heterotic-taubnut-operational-continuation.md) | 相対BRST、必要ラベル3組、地平面の混合、調整sourceによる古典接続 |
| [旧6条件監査](notes/heterotic-taubnut-six-gate-audit.md) ／ [文献対照検算](notes/heterotic-taubnut-literature-bridge.md) | 状態代表の訂正、条件付きLean補題、別模型のcoset接合と複素振幅 |

**99.813%は外側スカラーODEの流束比で、過去通信の成功率ではありません。** 古い無条件なBRST／free-string PASSの解釈は後の監査で訂正されています。

## 次の再開点

[最新ノート§7](notes/nut-reservoir-return-audit.md#7-再開条件と再現)から。密閉して記録を使わずに戻す案は棄却し、残る開放系では、**今回の外向き応答と整合する浴の量子状態・周期相関・記録を含むinstrument・装置の境界流**を同時に構成する必要があります。
任意のetaや新鮮な環境を手で足して成功にせず、NUT-onlyにTaub搬入の禁止も転用しません。全BRST分類、新規CTC形成、入力状態の完全保存を自動的な先行必須条件には戻しません。

## ブラックホール研究（別テーマ）

こちらは**principal safety**：背景曲率が有限でも、摂動・拘束・運動項・4次元作用へ特異性を移しただけでは解決としません。
[研究概要](SCREENING_RESEARCH_OVERVIEW.md) ／ [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) ／ [判定基準](docs/principal-safe-screening.md) ／ [NOVELTY.md](NOVELTY.md)。

## AI・コントリビューターのCI手順

まず[AGENTS.md](AGENTS.md)と[CI運用ルール](docs/ci-policy.md)を読んでください。
通常PRは累積差分の影響対象を検査します。独立scriptはPython 3.12、共有依存・入力・影響不明は全件へ拡大。文書のみならリンク検査、Leanは関連変更時に実行します。
[PR checks](.github/workflows/pr-checks.yml)が対象と理由を記録し、[Symbolic CI](.github/workflows/symbolic-ci.yml)は週次・手動の全件再現性を検査します。精度・assertを弱めません。

```bash
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは[Apache-2.0](LICENSE)、研究文章・式・図は[CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・仮説・未解決の物理を区別して記録します。
