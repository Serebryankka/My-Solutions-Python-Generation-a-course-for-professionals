import csv
from collections import defaultdict


with open('wifi.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    d = defaultdict(int)
    for row in reader:
        d[row['district']] += int(row['number_of_access_points'])
    for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0])):
        print(f'{k}: {v}')
      
