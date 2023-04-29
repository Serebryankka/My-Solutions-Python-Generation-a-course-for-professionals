from collections import Counter
import csv, json


summary = Counter()
for i in range(1, 5):
    with open(f'quarter{i}.csv', encoding='utf-8') as csv_file:
        data = csv.reader(csv_file)
        next(data)
        for row in data:
            summary.update({row[0]: sum(map(int, row[1:]))})

with open('prices.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for k, v in data.items():
        summary[k] *= v
