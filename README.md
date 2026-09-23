# Spacetime Screening

**知りたいこと：送信者が選んだ情報を、実際に過去の受信者へ届けられるか。**
CTCの幾何、場の物理性、送受信記録の確率を区別して調べます。ブラックホールの特異点回避は別テーマとして保存しています。

## 現在の結論 — 2026-09-23

> **過去通信の物理的な成功例は得ていません。今回は、残る肯定側の逃げ道を反証しようとしました。**
>
> **追加で排除したクラス：** 操作に依存しない一つの線形通信路を使い、通常の前向き実験室でコピー・反転を含む任意の操作を自由に接続でき、全結果が正規化される過去通信装置。この三条件では信号差が0になります。
>
> **残ったもの：** 操作によって大域的な場・背景が変わる構成、許される操作や確率法則が通常と異なる構成など。これらを含めた自然界全体の不可能性は証明していません。

| 調べた逃げ道 | 判定 | 読み違えてはいけない点 |
|---|---|---|
| **弱く雑音のある過去通信を、普通の装置へ自由に接続する** | **条件付きで不可** | 以下の線形性・操作非依存性・自由なフィードバックが仮定。CTCだけからは従わない |
| **通常の局所場をTaubから地平面越しに使う** | **以前の棄却を維持** | 初期Hadamard状態・固定背景・指定したコンパクト延長でのKRW障害 |
| **NUT内部にも閉じた光の測地線があるから全て発散する** | **この否定の試みは失敗** | 対象の第一NUT領域内に閉じたnull測地線はない。加速したCTCや装置信号は否定していない |
| **exactな弦補正や小さい種エネルギーなら安全** | **その保証はない** | 地平面のboostは残る。ただし全弦振幅の発散・装置の破壊は未証明 |
| **既知のCTC量子場・ワームホール論文が過去通信を保証する** | **その読み替えは不可** | 特殊模型の存在、摂動への頑健性、通過可能性、過去への通信を区別する |

**[最新ノート：逃げ道への反証試行、仮定、計算、反証できなかった点](notes/chronology-loophole-attack.md)**

## 今回の中心結果：受信ビットをコピー／反転して返せるか

前回は、自由場と送受信器の相互作用から、開いた局所実験の確率を導きました。

```math
K(y\mid b)=\frac{1+(-1)^{y+b}d}{2},\qquad
 d=e^{-2V_B}\sin(2\Delta_{AB}),\qquad D_B=|d|.
```

ここでbは送信ビット、yは受信記録、V_Bは場の雑音、Delta_ABは送受信領域に広がりを持たせた交換子です。実際の大域NUTの値を取得したという式ではありません。

**同じ核Kを変えず**、過去の受信記録yを後の送信器へ運び、コピーまたはNOTで返すと、全履歴の重みは

```math
Z_{\rm copy}=1+d,\qquad Z_{\rm NOT}=1-d.
```

両方を確率の総和1にするにはd=0が必要です。完全伝送でなくても成立し、有限の雑音だけでは回避できません。
量子版も、既知のone-party process定理の `W=rho_input tensor I_output` に一致します。厳密なChoi行列と全フィードバックの検査を追加しました。

**これは全自然法則のno-goではありません。** 長いB→A実験室を自由な一つのinstrumentと見なせること、外側の過程が操作非依存で線形なことが前提です。
操作を変えると大域的な核も変わる、コピー／NOTが物理的に実装できない、非線形な確率法則になる、といった回避には別の実証が要ります。分母だけを手で足して成功とはしません。
[導出・誤差下限・量子版・適用範囲](notes/chronology-loophole-attack.md)

## 否定に都合の悪い結果も残す

対象のexact heterotic計量では、第一NUT領域のnull測地線の径方向ポテンシャルが単調です。

```math
\left(\frac{D}{x^2-1}\right)'=-\frac{2(x+\delta)(\delta x+1)}{(x^2-1)^2}<0.
```

径方向の折り返しは極大しかなく、内部で閉じたnull測地線を作れません。**地平面の光の反復を、NUT内部の全経路に持ち込む反証は使えない**と分かりました。これはNUT-onlyの量子論や通信装置を構成できたという肯定ではありません。

一方、地平面の局所boost倍率は従来どおり約33.416。低エネルギーの種運動量でも反復像の相対エネルギーを全周回数で一様に小さくできません。ただし、この運動量診断だけで実際の衝突や全弦理論の破綻は証明しません。
[幾何の証明・数値対照・string文献の反例と限界](notes/chronology-loophole-attack.md)

## 再現

```bash
python -m pip install -r requirements.txt
# 今回の追加：操作論的no-goと、NUTの幾何への反証試行
python src/symbolic/operational_feedback_consistency.py
python src/symbolic/taubnut_loophole_geometry.py
# 同じPRの先行成果：場・送受信器と実際のNUT作用素
python src/symbolic/field_receiver_joint_probability.py
python src/symbolic/taubnut_nut_green_selection.py
```

process行列・Hamiltonianは厳密演算、数値対照は50/80桁で比較。既存assert・精度は維持しています。
**CI成功は実装した検算の成功であり、自然界の過去通信の成功／普遍的不可能性の証明ではありません。**
会話の「可能10%」は主観的な見立てです。校正した尤度はなく、今回の検査数を使って機械的に1%などへ変更しません。

## 以前の結果と適用境界を保存

| ノート | 保持している結果 |
|---|---|
| [場・送受信器からの判定](notes/taubnut-field-detector-closure.md) | 選択記録を保持した局所確率、NUTの遅延核の選別不能性、Hopf束、Taub準備の固定背景局所場案の棄却 |
| [量子場・KRW](notes/operational-past-signalling-focus.md) | 指定した地平面でのF-local／Hadamard延長の障害、古典sourceがconnected二点関数を変えないこと、後選別の偽陽性 |
| [受信記録付きCTC回路](notes/chronology-operational-channel-test.md) | 設定別固定点の距離48/73と、特定のDeutsch product処方での記録相関0。Taub–NUTの有効理論ではない |
| [前回の継続](notes/heterotic-taubnut-operational-continuation.md) | 相対BRST、必要ラベル3組、Taub時間の混合、調整sourceによる古典スカラー接続 |
| [旧6条件監査](notes/heterotic-taubnut-six-gate-audit.md) ／ [文献対照検算](notes/heterotic-taubnut-literature-bridge.md) | 状態代表の訂正、条件付きLean補題、別模型のcoset接合と複素振幅 |

**99.813%は外側スカラーODEの流束比で、過去通信の成功率ではありません。** 古い無条件なBRST／free-string PASSの解釈は後の監査で訂正されています。

## 次の再開点

[最新ノート§7](notes/chronology-loophole-attack.md#7-今回閉じたクラスと本当に残った課題)を参照してください。
次は同じ場・装置でコピー／NOT／固定送信を実装したとき、**大域的な場や背景の応答が操作ごとに核Kをどう変えるか、あるいは操作を本当に禁止するか**を調べます。
別の局所モードや回路を増やすだけで棄却済み案を復活させません。NUT-onlyにTaub搬入の禁止を転用せず、受信記憶・選択flag・正値性・大域gluingを同時に検査します。
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
