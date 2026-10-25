"""Read-only closeout checks; does not execute the model or verify web claims."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
AGENT = ROOT / 'agents/creation_agent'
BASELINE = 'a378256'
REVIEWED = 'ad5040fcca3ec15ad23d210bc2066863180952cc'


def run(*args):
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    print('$ ' + ' '.join(str(a) for a in args).replace(sys.executable, 'python'))
    print(result.stdout.strip())
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    return result.stdout


def check_shape(data, schema, path='$'):
    # Only the keywords used by the frozen course schemas are implemented.
    supported = {'$schema', 'title', 'type', 'required', 'properties', 'items', 'additionalProperties'}
    if set(schema) - supported:
        raise ValueError('Unsupported schema keyword; update this supplemental check explicitly.')
    kinds = {'object': dict, 'array': list, 'string': str}
    assert isinstance(data, kinds[schema['type']]), path + ': wrong type'
    if isinstance(data, dict):
        assert set(schema.get('required', [])) <= set(data), path + ': missing fields'
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False:
            assert not (set(data) - set(props)), path + ': extra fields'
        for key, value in data.items():
            if key in props:
                check_shape(value, props[key], path + '.' + key)
    elif isinstance(data, list):
        for i, value in enumerate(data):
            check_shape(value, schema['items'], f'{path}[{i}]')
    elif isinstance(data, str):
        assert data.strip(), path + ': empty string (supplemental content check)'


def main():
    print('Assignment 2 closeout verification')
    print('Run time:', datetime.now(ZoneInfo('America/New_York')).isoformat())
    print('Reviewed response snapshot:', REVIEWED)
    print('These are file/contract checks, not model runs or factual validation.')
    run(sys.executable, 'tools/check_frozen_core.py')
    frozen = [line.split('  ', 1)[1] for line in (ROOT / 'FROZEN_CORE_SHA256.txt').read_text().splitlines() if line.strip()]
    diff = run('git', 'diff', BASELINE, '--', 'FROZEN_CORE_SHA256.txt', *frozen)
    assert not diff.strip(), 'Frozen files or manifest differ from scaffold baseline'
    print('PASS: all 7 protected files and the manifest match the initial scaffold commit.')
    input_schema = json.loads((ROOT / 'core/input_schema.json').read_text())
    output_schema = json.loads((ROOT / 'core/output_schema.json').read_text())
    for case in ['primary', 'contrast_1']:
        f = AGENT / 'cases' / (case + '.json')
        check_shape(json.loads(f.read_text()), input_schema)
        print('PASS: populated input fields:', f.relative_to(ROOT))
    cases = [json.loads((AGENT / 'cases' / (c + '.json')).read_text()) for c in ['primary', 'contrast_1']]
    assert cases[0]['emerging_technology'] == cases[1]['emerging_technology']
    assert cases[0]['adoption_posture'] != cases[1]['adoption_posture']
    for filename in ['primary_response.json', 'contrast_1_response.json', 'primary_response_v2.json', 'contrast_1_response_v2.json']:
        f = AGENT / 'responses' / filename
        run(sys.executable, 'tools/validate_response.py', str(f.relative_to(ROOT)))
        data = json.loads(f.read_text())
        check_shape(data, output_schema)
        expected = '0.2-student' if '_v2' in filename else '0.1-student'
        assert data['agent']['version'] == expected
        for marker in ['filecite', 'chatgpt-content-reference', '\ue200', '\ue202']:
            assert marker not in f.read_text(), 'Internal citation marker in ' + filename
        original = subprocess.check_output(['git', 'show', REVIEWED + ':' + str(f.relative_to(ROOT))], cwd=ROOT)
        assert f.read_bytes() == original, 'Closeout changed historical output: ' + filename
        print('PASS: schema fields, array item types, version, citation hygiene and preservation:', filename)
    metadata = json.loads((AGENT / 'agent_metadata.json').read_text())
    assert metadata['version'] == '0.2-student'
    with tempfile.TemporaryDirectory(prefix='assignment2-prompts-') as tmp:
        for case in ['primary', 'contrast_1']:
            out = Path(tmp) / (case + '.txt')
            run(sys.executable, 'tools/build_prompt.py', '--agent', 'agents/creation_agent', '--case', f'agents/creation_agent/cases/{case}.json', '--out', str(out))
            packet = out.read_text()
            assert (ROOT / 'core/common_instructions.md').read_text() in packet
            assert (AGENT / 'specialist_instructions.md').read_text() in packet
            assert '0.2-student' in packet
            saved = AGENT / 'records/prompts' / (case + '_v2_rebuilt.txt')
            assert saved.read_bytes() == out.read_bytes(), 'Saved prompt is not reproducible'
            print('PASS: rebuilt prompt matches saved closeout packet:', case)
    print('SHA256 of reviewed agent artifacts:')
    paths = [AGENT / 'specialist_instructions.md', AGENT / 'agent_metadata.json']
    paths += [AGENT / 'cases' / (c + '.json') for c in ['primary', 'contrast_1']]
    paths += sorted((AGENT / 'responses').glob('*.json'))
    for path in paths:
        print(hashlib.sha256(path.read_bytes()).hexdigest(), str(path.relative_to(ROOT)))
    print('ALL CLOSEOUT CHECKS PASSED')


if __name__ == '__main__':
    main()
