"""Small dependency-free packaging check; behavioral quality is evaluated separately."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = root / 'realistic-travel-planner'
entry = (skill / 'SKILL.md').read_text(encoding='utf-8')
assert entry.startswith('---\n'), 'Missing frontmatter'
frontmatter = entry.split('---', 2)[1]
assert re.search(r'^name: realistic-travel-planner$', frontmatter, re.M)
assert re.search(r'^description: .+', frontmatter, re.M)
assert not re.search(r'\bTODO\b|\[TODO', entry), 'Unfinished scaffold'
for target in re.findall(r'\]\((references/[^)]+)\)', entry):
    assert (skill / target).is_file(), 'Missing reference ' + target
assert (skill / 'agents/openai.yaml').is_file()
assert (skill / 'scripts/audit_plan.py').is_file()
print('Package structure and linked references OK')
