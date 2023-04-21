import csv
from collections import defaultdict


with open('salary_data.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    d = defaultdict(lambda: [0, 0])
    for row in rows:
        d[row['company_name']][0] += int(row['salary'])
        d[row['company_name']][1] += 1
    for row in sorted(d.items(), key=lambda item: item[1][0] / item[1][1]):
        print(row[0])
