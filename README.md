# Spacetime Screening

**知りたいこと：送信者が選んだ情報を、実際に過去の受信者へ届けられるか。**
CTCの幾何、場の物理性、送受信記録の確率を区別して調べます。ブラックホールの特異点回避は別テーマとして保存しています。

## 判定 — 2026-09-23

> **現行のTaub–NUT通信案は、失敗としてクローズします。**
>
> 棄却するのは、**「通常の局所スカラー量子場をTaubで準備し、同じ理論のまま固定背景の地平面を越えて通信する」案**です。必要な大域的な場の条件がKRW定理と両立せず、正則な古典波や回路の固定点を足しても解消しません。
>
> **これは「自然界では過去通信が絶対に不可能」という証明ではありません。** NUT内部だけに定義した別の大域量子論や、完全な弦の実時間過程は区別します。

| 問い | 答え |
|---|---|
| **この既存案を、物理的な過去通信の成功として採用できる？** | **できません。現行案は棄却。** 仮定を固定した局所場の地平面越しの完成に障害があります。 |
| **送受信器から同時確率を導けた？** | **局所場の条件の下では導出済み。** 下の式は記録bitを保持し、全受信結果を含みます。CTC処方を選んだ式ではありません。 |
| **NUT内部の局所通信も不可能？** | **いいえ。条件付きの局所通信は可能。** それと長い実験室履歴を、一つの大域的に整合した実験へ拡張できるかは別です。 |
| **計量・波動方程式・周期性だけで、その大域確率が決まる？** | **その手順では決まりません。** NUTでは通常の「遅延」という支持条件が選別力を失います。任意の核を足す案も局所交換関係に違反します。 |
| **完全な弦理論／自然界全体で可能か不可能か？** | **この研究から二択の証明は得られていません。** 未取得の確率を0にしたり、局所の結果を全時空へ移したりしません。 |

**[最新ノート：場・検出器からの導出、現行案を棄却する範囲、条件付き肯定、再開条件](notes/taubnut-field-detector-closure.md)**

## 今回の前進：回路の処方選びから、場の相互作用へ

### 1. 選択bitと受信記録の同時確率を導出

局所自由場に結合する送信器と受信qubitを使い、bitの記録Rも保持すると、正当なA→B相互作用順序の下で

```math
P(R=b,Y=y)=\frac{p_b}{2}\left[1+y(-1)^b e^{-2V_B}\sin(2\Delta_{AB})\right],
\qquad D_B=e^{-2V_B}|\sin(2\Delta_{AB})|.
```

`Delta_AB` は送受信領域間の場の交換子、`V_B` は受信領域の量子雑音です。これらが正しい場理論から得られ、実験の順序と準備が許されていれば、確率は正規化され、記録したbitが受信統計に現れます。
**実際のTaub–NUT全体の値を代入できた、という結果ではありません。** 非零の交換子だけでも不十分で、真に先に読んだ記録は後の通常操作で変わらないことも検算しました。

### 2. 実際のNUT作用素で「遅延核を選ぶ」手順を検査

第一NUT領域では、十分にfibreを周回すれば任意の二点が互いにfuture timelikeに結ばれます。このため通常の因果的支持条件は領域全体を許し、核の選別に使えません。
実際の波動作用素のbisolutionを明示して曖昧さを確認しましたが、**それを自由に交換子へ加えると局所性を壊す**負例も検出しました。
またHopf bundleのChern数は1なので、全時空の被覆としてtだけをほどく簡単なimage-sum構成は使えません。

### 3. 条件付きで「送れる側」の構成も保存

NUT内部で短いA→Bのnull経路と、長いB→Aの実験室timelike経路を構成しました。小さな局所領域の普通の場の通信は非零の識別可能性を持ち得ます。
**これを、過去の記録・後のbit選択を含む一つの大域実験にできれば過去通信になります。** その大域拡張を仮定だけで済ませないことが、現行案と成功例の境目です。

## なぜ「もっと6条件を埋める」で続行しないのか

既存CTCの利用に、新しい因果構造の生成は必須ではありません。全BRST cohomology・全スペクトルの分類や、受信後の入力状態の完全保存も要求しません。
必要なのは、使う状態・操作・観測量の物理性、正の確率、装置を含む自己無撞着な実験です。

**Taub準備の通常局所場案は、これらの一部が両立しないので止めます。** NUT-onlyの別完成やfull stringの回避を、同じ定理で一括排除はしません。
作業仮説としては、通常の局所装置の完成が量子場／背景の応答に阻まれる可能性を優先しますが、これは全弦のbackreactionの予測ではありません。
[否定・肯定・仮説の適用境界](notes/taubnut-field-detector-closure.md#6-最終判断仮説再開条件)

## 再現

```bash
python -m pip install -r requirements.txt
python src/symbolic/taubnut_nut_green_selection.py
python src/symbolic/field_receiver_joint_probability.py
```

inverse metric・4D波動作用素・局所性の負例・Weyl積・記録付き確率は厳密代数。
null経路とGaussian波動関数の独立積分は50/80桁で比較します。**対照計算の数値をTaub–NUTの成功確率として表示しません。**
CI成功は検算の成功です。大域幾何の論証や既知KRWをPython／Leanで形式証明したという意味でもありません。

## これまでの成果を保存

| ノート | 保持している結果 |
|---|---|
| [量子場・KRW](notes/operational-past-signalling-focus.md) | 指定した地平面でのF-local／Hadamard延長の障害、古典sourceがconnected二点関数を変えないこと、後選別の偽陽性 |
| [受信記録付きCTC回路](notes/chronology-operational-channel-test.md) | 設定別固定点の距離`48/73`と、特定のDeutsch product処方での記録bitとの相関0の違い。Taub–NUTの有効理論ではない |
| [前回の継続](notes/heterotic-taubnut-operational-continuation.md) | 相対BRST、必要ラベル3組、Taub時間の混合、調整sourceによる古典スカラー接続 |
| [旧6条件監査](notes/heterotic-taubnut-six-gate-audit.md) | 状態代表の訂正、準備依存の障害、chronalな受信点への条件付きLean補題 |
| [文献対照検算](notes/heterotic-taubnut-literature-bridge.md) | 別模型のcoset接合と複素反射振幅 |

**`99.813%`は外側スカラーODEの流束比で、過去通信の成功率ではありません。** 古い無条件な`BRST / free-string PASS`の解釈は後の監査で訂正されています。

## 再開するときに必要なもの

[最新ノート§6](notes/taubnut-field-detector-closure.md#6-最終判断仮説再開条件)から再開してください。
別modeや別のCTC回路を追加するだけで現行案を再開しません。**失敗した仮定を置き換える大域場・状態・送受信instrumentを明示し、使う相関関数と記録の大域的整合性を確かめる**ことが再開条件です。
NUT-onlyを検証する場合は、その独立した大域完成が対象で、Taub搬入の禁止を転用しません。

## ブラックホール研究（別テーマ）

こちらは**principal safety**：背景曲率が有限でも、摂動・拘束・運動項・4次元作用へ特異性を移しただけでは解決としません。
[研究概要](SCREENING_RESEARCH_OVERVIEW.md) ／ [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) ／ [判定基準](docs/principal-safe-screening.md) ／ [NOVELTY.md](NOVELTY.md)。

## AI・コントリビューターのCI手順

まず[AGENTS.md](AGENTS.md)と[CI運用ルール](docs/ci-policy.md)を読んでください。
通常PRでは累積差分の影響対象を検査します。独立scriptはPython 3.12、共有依存・データ・影響不明は全件へ拡大。
文書のみならリンク検査、Leanは関連変更時に実行します。
[PR checks](.github/workflows/pr-checks.yml)が対象と理由を記録し、[Symbolic CI](.github/workflows/symbolic-ci.yml)は週次・手動の全件再現性を検査します。精度・assertを弱めません。

```bash
# コミット済みPRの累積差分（未コミット変更は含まれません）
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは[Apache-2.0](LICENSE)、研究文章・式・図は[CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・仮説・未解決の物理を区別して記録します。
