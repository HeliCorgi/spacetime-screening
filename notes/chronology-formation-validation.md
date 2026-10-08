# Chronology形成の本線: 再現・検証範囲

2026-10-08。読取親PR #40 `c6e6cda08ad73e457d135bcb9652a2355add9a9b`。
[解析本文](chronology-formation-mainline.md)。追加はこの2文書と独立Python3本のみ。
既存の研究式・assert・精度・依存・workflow・CI選別・Leanを変更しない。

## 1. 再現コマンド

```bash
python src/symbolic/chronology_null_return.py --output /tmp/null-return.json
python src/symbolic/chronology_null_return_verify.py \
  --evidence /tmp/null-return.json --output /tmp/null-return-verify.json
python src/symbolic/chronology_null_return_verify.py
python src/symbolic/chronology_esu_control.py --output /tmp/esu-control.json
python -m compileall -q src/symbolic/chronology_null_return.py \
  src/symbolic/chronology_null_return_verify.py src/symbolic/chronology_esu_control.py
```

verifierはforwardをimportしない。CIのstandalone実行は生成JSONを要求しない。
JSON連携は上のコマンドで別に検査する。失敗を成功へ置き換える処理はない。

## 2. 実施したローカル検査

Python **3.13.5** / SymPy **1.14.0** / mpmath **1.3.0**。

| 検査 | 結果 | 射程 |
|---|---|---|
| 新規forward | success | 2つの4D vacuum Ricci、nonaffinity、factorized waveの周期性・pullback、degenerate null branch、Grant証人・切取り・周期化 |
| 独立verifier standalone | success | Hamilton方程式、別のcovector計算、有理証人、別のlog2級数、周期修復 |
| forward JSON -> verifier | success | 固定SHA・幾何等式・帰還値・scope flagの照合 |
| 改変したJSON 12ケース | 全てexit=1で拒否 | 親SHA、Ori倍率、Ricci、零boost、波の周期性、形成flag、領域包含、壁の完成、一般no-go、null interval、compact drift |
| ESU script | success | KGの非特異点での式、trace invariants、両Einstein成分、周期の負例、全spectrum級数のroot bracket |
| 新規3本のcompile | success | 構文・bytecode検査 |
| 既存CI選別器の自己検査20件 | success | 固定main archiveの選別器。今回選別規則は変更しない |
| 追加2文書のlocal file links | success | 固定main archiveと新規5ファイルの作業copy。外部URL・anchorは検査対象外 |

今回、完全な最新PRのcheckoutをローカルで再取得したとは報告しない。
ローカル検査の対象は新規3本であり、累積PRの実行対象と結果はremote CIで別途確認する。
remoteの新head、synthetic merge tree、run、実行version、成功/失敗はPRの検証コメントに記録する。
過去headの成功を今回の成功へ流用しない。

## 3. 具体的な再計算の違い

forwardは一般計量からChristoffel/Ricciを計算し、verifierはHamiltonianを微分してOriのreturnを得る。
Grantのforwardはnull chordの接線、verifierはlowerしたcovectorとdeck pullbackを使う。
切取りのlog2判定はそれぞれatanh級数とlogの別の正項級数で行う。
追加drift周期は有理2例・無理2例を検査し、全B>0の証明は本文のpigeonhole論証で与える。

ESUは8000項の正項級数と解析的tailを60桁の外向きinterval演算で評価する。
occupation multiplicityを先に和する別のLambert級数も使う。
高温漸近式で計量を解いたとはしない。rootのseedを与えるだけで、端点の符号は全級数の包囲で保証する。
`mpmath.iv`のinterval arithmeticは数値ライブラリの実装を信頼するもので、Lean kernelで検証した証明ではない。
存在と一意性自体には本文の単調性と両端極限を用いる。

新しい草稿の導出時に、generic winding tangentのaffine性とEinstein trace成分の組合せを
直接計算で訂正してから最終検査した。既存repoのassertを緩めたものではない。
単独のsymbolic等式から自動的にHadamard状態やSCEEの存在を認定するflagは作らない。

## 4. 負例と過大主張の防止

`chronology_null_return_verify.py`は、WFの両covectorの同時スケールと片側スケールを区別する。
round S3の全周帰還では同じcovectorになるので、単なる閉null測地線の存在だけをno-go証人にしない。
閉じていないblack-hole generatorも排除しない。

Grantの端点が近くてもchord全体が領域外へ出る場合を検査する。
切取りにCTCが残る正しい幾何対照例を消さず、その周期的な有限化が別に失敗することを検査する。
XavierのP,Qを個別に周期関数と決めつけず、非単位Floquet係数を持つ合法なhも対照に残す。
ESUは実時間周期とKMS逆温度を区別し、Lambda=0の誤った静的rootを拒否する。

## 5. 未実施・証明していない事項

- 連続体の特異性伝播、Hadamard/CCR/positive state構成、今回の全解析的論証のLean形式化・独立査読。
- Ori、Xavier修復、Grant境界を含む非線形SCEE形成の数値発展。
- ESUの因果的初期準備、非線形安定性、stress fluctuationの小ささ、量子重力補正の全制御。
- 物理的な反射壁/接合装置を持つ有限Grant実験の構成。
- 全時空・全物質に対するchronology protectionの一般証明。
- Family 376 upstream Lean/Mathlib/全comparatorの再build。今回の最短経路には使わない。

最新の形成問題全体の分類4と、限定クラスへの排除、永続的ESUのmean-field構成を混同しない。
