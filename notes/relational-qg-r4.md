# Relational QG R4：非線形初期データと正の lapse

R3 の m=2 potential を保持し、非一様 lapse に対する kinetic ordering を
S N S に修正した。平坦二次作用と p=0 の初期拘束は変えない。

[全導出・適用範囲](../research/relational_qg_R4/REPORT_JA.md)

[数値ソルバー](../src/numerical/relational_qg_r4_initial_data.py) ／
[記号検査](../src/symbolic/relational_qg_r4_ordering.py) ／
[独立検証](../src/symbolic/relational_qg_r4_verify.py)

実行可能になったのは、座標 Gaussian rest density を与えた、漸近平坦・
球対称・時間対称の nonlinear metric/lapse boundary-value problem。
初期固有時間率と ADM mass sensitivity が同じ lapse で結び付く。

全非線形 evolution、一般の物理モード安定性、cosmology、quantum completion、
特異点一般の解消を PASS としていない。
