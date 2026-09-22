# Spacetime Screening

ブラックホールの特異点回避と、CTC（閉じた時間的曲線）を含む弦理論背景が、健全な物理過程として使えるかを調べる研究リポジトリです。

## 過去へ、選んだ情報を送れる？

> **物理的に送れることは、まだ実証していません。一般に不可能とも証明していません。**
>
> 今回は「6条件を全部埋める」から、**送信者の選択と、過去の受信記録が本当に結び付くか**へ研究の中心を移しました。
> **CTCがある／波が届く／定常解が違う、だけでは通信成功にしません。**

### 今回わかったこと — 2026-09-23

| 検査 | 結果 | 意味 |
|---|---|---|
| **NUT内の帰還経路** | 固定背景で二つの未来向きtimelike円弧を確認 | 受信→送信の実験室経路と、送信→受信の帰還経路は書ける。装置や情報の実現ではない |
| **送信bitを別々に固定した回路** | 異なる正常化されたCTC固定点が得られる | これだけでは「選んだ情報を送れた」とは言えない |
| **選択bitの記録・受信器も含む回路** | 指定したDeutsch product処方では**bitとの相関が0** | この具体的プロトコルは記録付き通信テストを通らない |
| **最初からbitとの相関を入れた別処方** | 同じ周辺固定点でも非零の相関 | その相関を物理法則から導く必要がある。手で入れただけでは証拠にならない |
| **実際のTaub–NUT上の量子通信** | **未導出** | 上の有限回路を弦理論から導けていない。回路の0も非零も、自然界の結論へ移さない |

**今回の進展は、見かけの通信成功を見抜く検査を作ったことです。**
受信器の測定作用も含む厳密計算で、「0・1それぞれに答えがある」ことと、「一つの実験で選んだbitが受信記録に届く」ことの違いを確認しました。後から都合のよい試行だけを残す偽の信号も検出します。

**[最新ノート：導出・検算・限界・次の再開点](notes/chronology-operational-channel-test.md)**

### 必須条件も見直しました

既存のCTCを使う可能性を調べるだけなら、**新たに因果構造を変える必要はありません**。全BRST cohomology・全string spectrumの分類を先に終える必要もなく、使う符号化・操作・受信器が物理的に許されることを示せばよい、という方針に変えました。受信時に状態が変わることも失敗とはしません。

ただし、物理的な状態・正常化された確率・実験全体の逆反作用の整合性は省略しません。**「同じ準備」を受信結果まで同じに固定して、時間遡行を定義で禁止することもしません。** 旧6条件の修正理由は最新ノート§1–2にあります。

### 何ができれば「送れた」と言える？

実験室の時計で受信Bが送信Aより先であり、同じ外部準備と法則の下で送信操作を変えると、**選別していない受信結果の分布が変わること**が中心です。bitを選ぶ物理装置も記録し、前からある相関や境界条件の入れ替えを通信と取り違えないようにします。

NUT内の受信者はCTC領域にいるので、chronalな過去の受信者への帰還禁止をそのまま適用できません。ここを現在の検討対象として残します。Taubから装置を持ち込むことや、CTCを最初から作ることは追加の問題として区別します。

### 再現

```bash
python -m pip install -r requirements.txt
python src/symbolic/chronology_reference_bit_channel.py
python src/symbolic/taubnut_receiver_event_geometry.py
```

回路は30組のparameter、unitary・Choi・正常化・固定点・選択記録・負例を整数／有理数で検査します。幾何も厳密な根号式で検算します。**CI成功はこれらの検査の成功で、物理的な過去通信の成功ではありません。**

### 前回までの成果

[前回の継続ノート](notes/heterotic-taubnut-operational-continuation.md)：相対BRST複体、必要ラベル3組、地平面での混合、外部sourceからNUTへ正則なスカラー応答を作る例。全弦状態・局所送信装置としては未認定です。

[6条件監査](notes/heterotic-taubnut-six-gate-audit.md)：特定のSU(2)状態式の訂正、準備に依存するスカラーの障害、chronalな過去の受信者への条件付きLean補題。[文献対照検算](notes/heterotic-taubnut-literature-bridge.md)：別模型のcoset接合と複素反射振幅。

**`99.813%` は外側スカラーODEの流束比であり、過去通信の成功率ではありません。** 古い無条件な `BRST / free-string PASS` の解釈も、後の監査で訂正しています。

## ブラックホール研究の本筋

こちらは **principal safety**：背景曲率が有限でも、摂動・拘束・運動項・4次元作用に特異性を移しただけでは解決としません。時間遡行の研究とは区別しています。

| 読みたいもの | 入口 |
|---|---|
| ブラックホール研究の詳細と既存成果 | [研究概要](SCREENING_RESEARCH_OVERVIEW.md) |
| ブラックホール側の引き継ぎ | [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md) |
| 健全性の判定基準 | [principal-safe-screening](docs/principal-safe-screening.md) |
| 新規性・既知結果の区別 | [NOVELTY.md](NOVELTY.md) |
| **時間遡行の最新結果と再開点** | **[通信判定ノート](notes/chronology-operational-channel-test.md)** |
| 時間遡行についての前回の6条件判定 | [six-gate audit](notes/heterotic-taubnut-six-gate-audit.md) |

## AI・コントリビューターの再開手順とCI

まず [AGENTS.md](AGENTS.md) と [CI運用ルール](docs/ci-policy.md) を読んでください。時間遡行の続きは[通信判定ノート](notes/chronology-operational-channel-test.md)§6から。旧6条件の全分類やブラックホール側へ自動的に戻らないでください。

| 変更／実行の目的 | 自動検査 |
|---|---|
| README・ノートだけ | ローカルリンク等の軽量検査 |
| 独立した計算スクリプト | PR累積差分の影響対象をPython 3.12で検査 |
| 共有コード・依存・入力データ・影響不明 | Python全件へ拡大 |
| 週次／手動の完全検証 | 全スクリプトをPython 3.11／3.12、Leanも確認 |
| Leanの変更 | Lean検査。PythonだけのPRでは重複実行しない |

[PR checks](.github/workflows/pr-checks.yml) が対象と理由を記録し、[Symbolic CI](.github/workflows/symbolic-ci.yml) は週次・手動の全件再現性を検査します。精度・assertを弱めず、無関係な重複実行を減らします。

```bash
# コミット済みPRの累積差分（未コミット変更は含まれません）
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/ci-plan.json
python scripts/ci/checks.py docs --plan /tmp/ci-plan.json
python scripts/ci/checks.py run --plan /tmp/ci-plan.json
```

## ライセンス

コードは [Apache-2.0](LICENSE)、研究文章・式・図は [CC BY 4.0](LICENSE-DOCS)。再現結果・条件付き推論・未解決の物理を区別して記録します。
