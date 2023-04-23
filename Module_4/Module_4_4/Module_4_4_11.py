import json
import csv
from collections import defaultdict


with open('playgrounds.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    d = defaultdict(lambda: defaultdict(list))
    for row in reader:
        d[row['AdmArea']][row['District']].append(row['Address'])
with open('addresses.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=3, ensure_ascii=False)
