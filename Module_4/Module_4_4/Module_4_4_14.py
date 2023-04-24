from collections import defaultdict
import json
import csv


with open('exam_results.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    d = defaultdict(lambda: defaultdict(int))
    for row in reader:
        d[row['email']]['name'] = row['name']
        d[row['email']]['surname'] = row['surname']
        if int(row['score']) > d[row['email']]['best_score']:
            d[row['email']]['best_score'] = int(row['score'])
            d[row['email']]['date_and_time'] = row['date_and_time']
        d[row['email']]['email'] = row['email']
with open('best_scores.json', 'w', encoding='utf-8') as f:
    json.dump(sorted(d.values(), key=lambda x: x['email']), f, ensure_ascii=False, indent=3)
    
