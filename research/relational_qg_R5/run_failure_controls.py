"""Actually launch the independent verifier on corrupted copies of the evidence."""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[1]
SOURCE=HERE/'results.json'
VERIFIER=REPO/'src/symbolic/relational_qg_r5_verify.py'
original=json.loads(SOURCE.read_text())
mutations=[]

def add(name, change):
    d=deepcopy(original); change(d); mutations.append((name,d))

add('wrong_equal_factor_phase',lambda d:d['selected_models'][0].update(bracketed_phase_node='0.8'))
add('wrong_scalar_tensor_coefficient',lambda d:d['certificate'].update(curvature_scalar_coefficient_in_R3_ansatz='1/3'))
add('full_gravity_overclaim',lambda d:d['shared_results'].update(full_consistent_gravity=True))
add('mismatched_factor_coefficients',lambda d:d['selected_models'][0].update(b='1/5'))
add('fabricated_small_kappa',lambda d:d['selected_models'][2].update(kappa='0.0001'))
add('fabricated_uniform_bound',lambda d:d['robustness_margins'][0].update(kappa_interval=['0.21650635','0.3']))
add('uniqueness_overclaim',lambda d:d['selected_models'][0].update(phase_node_unique='proved'))
add('stale_source',lambda d:d.update(source_sha256='0'*64))

def one(item):
    name,data=item
    with tempfile.TemporaryDirectory(prefix='r5-negative-') as t:
        path=Path(t)/'evidence.json'; output=Path(t)/'success.json'
        path.write_text(json.dumps(data)+'\n')
        r=subprocess.run([sys.executable,str(VERIFIER),'--evidence',str(path),'--output',str(output)],
                         capture_output=True,text=True,timeout=150)
        assert r.returncode!=0, f'{name}: corrupted evidence accepted'
        assert not output.exists(), f'{name}: success output incorrectly written'
        last=r.stderr.strip().splitlines()[-1]
        assert 'AssertionError:' in last, f'{name}: unrelated failure: {last}'
        return {'mutation':name,'exit_code':r.returncode,'success_file_written':False,
                'error':last}

if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=2) as pool:
        rows=list(pool.map(one,mutations))
    result={'base_evidence_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'verifier_sha256':hashlib.sha256(VERIFIER.read_bytes()).hexdigest(),
            'mutations':rows,'all_negative_controls_rejected':True}
    (HERE/'failure_controls.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
