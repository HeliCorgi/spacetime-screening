# R1 空間因果性・reset監査: 再現と検証範囲

2026-10-08。親PR #40 head `d679f9585cc89518981ce03f6075bab8fb5256fd`、
親tree `6031903fc2ab325fb93eb614eb514240918844b0`。
[導出本文](r1-causal-packet-reset.md)。今回の差分は新規Markdown2本と独立Python2本のみ。
既存の方程式、mu/tau、assert、精度、依存、CI選別、workflow、Leanは変更しない。

## 再現

```bash
python src/symbolic/r1_causal_packet.py --output /tmp/r1-causal.json
python src/symbolic/r1_causal_packet_verify.py \
  --evidence /tmp/r1-causal.json --output /tmp/r1-causal-verify.json
```

forwardは局所PDE・flux・modal reduction・保存量・Hurwitz minorsを記号計算する。
33cellの局所stencilと物理的発熱／数値拡散の別会計には有理数を用いる。
9cellのcentered midpointの遠隔leakは厳密な非零有理数として検出する。

verifierはforwardをimportしない。順序を変えた5変数generatorからFractionのGauss消去で
保存量を求め、別のscalar stencilから収支を計算する。
principal-minor 30個と3組の有理parameterのHurwitz minorsも独立計算する。
一般parameterの定理は本文の導出によるもので、この有限サンプルを証明の代わりにしない。
modeの数値は行列指数ではなくLaplace留数から再計算する。

`--evidence` では親SHA、規格化保存量、reset bound、nonlinear未認定flag、
heat／numerical diffusion、指定された5時刻のmodal値、acausal negative controlの分類を照合する。
JSONの全ての文章や任意のproofを検証する万能verifierではない。

## ローカルで実施したもの

Python **3.13.5**、SymPy **1.14.0**、mpmath **1.3.0**。

| 対象 | 結果と範囲 |
|---|---|
| 新規forward | 成功、JSON出力・読込成功 |
| 独立verifier、forward JSON連携 | 成功 |
| verifier単独実行 | 成功、forwardに依存せず再計算 |
| 追加Python2本のcompile | 成功 |
| repo既存CI選別器の自己検査 | 20件成功。選別器は変更していない |
| 改変JSONの拒否 | 8件全てexit 1。誤った親、保存量、reset bound、非線形認定、heat欠落、数値拡散欠落、変位改変、因果性の偽認定 |

L1–L4の限定された数学的論証と、数値実験を分離する。
forwardの長時間sampleはlinear asymptoticsの証明ではなく、本文の固有vector論証と整合する診断。
格子診断の1次収束は64/128/256/512cellの誤差比
`2.14548718015, 2.08935682179, 2.04739976212`。
最終max errorは `0.00146698329407872425`。閾値は結果に合わせて緩めていない。

局所stencilのgrid impulseはsmoothな物理packetではない。
smooth packetの有限伝播は本文の局所energy proof、grid impulseは実装の厳密なsupport検査である。
数値拡散はphysical heatに混ぜず別項として出力する。

## GitHub側の検証

最新commit SHAとPR累積差分のCI結果は、完了を確認した時点のPR #40コメントで記録する。
この文書内の上表はlocal実行であり、過去headのremote成功を最新headの成功として転記していない。
通常PRの選別に従い、累積差分の既存Family/R1 scriptも必要な対象として残す。
今回はupstream Leanや全研究suiteの手動全件実行を起動する変更ではない。

ローカル環境は、今回の4追加ファイルと既存の固定原本archiveを使って検査した。
remoteの最新全checkoutをローカルでcloneして再実行したとは主張しない。
追加Git blobとローカルのテスト実体のhashを照合し、remote変更が4追加だけであることを別に確認する。

## 未実施・未証明

- 正粘性Einstein–二流体の非線形全gate-time estimate、共通切断tube invariance、計算可能なC_*、具体的epsilonの認定。
- driverの物理的準備、vacuum外部を持つ有限装置、latch/memory/resetの閉じた実装。
- nonlinear全時間安定性、任意長compiler、停止検出とのcomputable iff reduction。
- OpenAI/mathの全証明の独立査読、Lean 4.34.1/Mathlib/全comparator再build。
- CTC、Hadamard、RSET、SCEEの新しい解や一般no-go。

既存Lean3ファイルがPRの累積差分により再検査されても、今回の連続体PDE proofが形式化されたという意味ではない。
総合埋込み分類D、元R1は部分達成のまま。Cは本文で明示した受動的linear保持/reset仕様のみに付ける。
