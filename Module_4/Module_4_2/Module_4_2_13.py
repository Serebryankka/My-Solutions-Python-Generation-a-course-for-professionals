import csv
from collections import defaultdict


with open('salary_data.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    d = defaultdict(lambda:defaultdict(int))
    for row in rows:
        d[row['company_name']]['salary'] += int(row['salary'])
        d[row['company_name']]['count'] += 1
    for row in sorted(d.items(), key=lambda item: item[1]['salary'] / item[1]['count']):
        print(row[0])
      
