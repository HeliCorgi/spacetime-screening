# R1 closed shear: 検証範囲と再現

2026-10-08。[解析本文](r1-closed-shear-driver.md)。PR #40の続き。

## 原本と変更

- 親head: `0ab94331d8aef62148acac1d89e3235979e6ea83`。
- 親tree: `64009fadfcfe4d2dee063689af61f6d305e66885`。会話に保存された固定原本と既存PRの6ファイルから再構成し、`git write-tree`で一致を確認した。
- この追記は解析2 Markdown、独立Python2本、既存R1文書の進捗pointerだけ。
- 既存の物理assert、精度、CI選別、依存、workflow、Lean theoremを変更しない。
- この文書のSHA自己参照は行わない。実際のremote head、synthetic merge、run/jobはPR検証コメントに記録する。

## ローカルで実施した内容

Python **3.13.5** / SymPy **1.14.0** / mpmath **1.3.0**。

1. 順方向scriptのexact symbolic checksと50/80桁のmatrix-exponential diagnostics。
2. 標準ライブラリだけの独立verifier。Fraction、整数sqrt、Machin pi、外向き75桁整数interval、32次Taylor剰余。
3. `forward --output` のJSONを `verifier --evidence` で読み込むend-to-end検査。
4. 非対応条件を棄却する負例。過大電場による負密度、未補償のEinstein拘束、電流符号反転、凍結外部E、短すぎるrelaxation、isentropic粘性閉鎖、entropy項の削除、許容外の大きなstress tube。
5. PR累積差分を使うCI selector、文書ローカルリンク、選択された独立Pythonを検査する。

順方向のsamplingはdiagnosticのみ。0.26%と0.18%は本文のenergy/relaxation積分からの全時間上界である。
終点の各intervalは指定された線形ODEの解を包囲する。非線形Einstein解のintervalではない。

## 再現コマンド

```bash
python src/symbolic/r1_closed_shear.py --output /tmp/r1-forward.json
python src/symbolic/r1_closed_shear_verify.py --evidence /tmp/r1-forward.json --output /tmp/r1-independent.json
python -m json.tool /tmp/r1-forward.json > /dev/null
python -m json.tool /tmp/r1-independent.json > /dev/null
python scripts/ci/test_checks.py
# リモートから取得した実際のmain refを使うこと。
python scripts/ci/checks.py plan --base origin/main --head HEAD --plan /tmp/r1-pr-plan.json
python scripts/ci/checks.py docs --plan /tmp/r1-pr-plan.json
python scripts/ci/checks.py run --plan /tmp/r1-pr-plan.json
```

期待される累積選択は元の `family376_bridge_checks.py` と新規2本の**計3本**、
Markdown6件、既存PR内のLean変更である。baseが変われば実際のplanに従う。
独立verifierはforwardをimportせず、単独実行でも固定モデルを検査する。
正負caseで入力JSONを改変した検査も別に行い、改変した数値や非線形認定flagを受理しない。

## 認定していない事項

- full nonlinear Einstein–Maxwell–二粘性流体の時間発展計算。
- 共通Cauchy frameでの非線形energy estimateと、その定数・具体的振幅のinterval certificate。
- 元のR1で許容する任意pulse、固定physical-wavelength、任意輸送係数のgate。
- driverをゼロ状態から製造する過程、永久reset、停止後も保持されるmemory。
- NS universal compiler、無限実行の有限資源・noise robustness。
- Hadamard state、RSET、quantum fluctuations、SCEE、CTC。
- 連続体Einstein/IS/MaxwellのLean形式化。既存Leanの成功はこれらを意味しない。
- upstream Family 376全Lean dependency closureの再buildや、最新IS preprintの独立査読。

本文の非粘性局所存在論、非線形の凍結rest-symbol補題、線形のrigorous intervalを別々に扱う。
**全体のR1は部分達成。** 失敗を成功へ変換するfallbackや精度の緩和を導入しない。
