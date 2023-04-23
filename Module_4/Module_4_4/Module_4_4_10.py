import json
from collections import defaultdict


with open('countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    result = defaultdict(list)
    for d in data:
        result[d['religion']].append(d['country'])
with open('religion.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=3)
