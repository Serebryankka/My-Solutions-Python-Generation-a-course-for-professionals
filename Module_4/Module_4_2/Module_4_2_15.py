import csv
from collections import defaultdict

with open('data.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    d = defaultdict(int)
    for row in reader:
        d[row['email'].rsplit('@')[1]] += 1
        
with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as csv_file_res:
    writer = csv.DictWriter(csv_file_res, fieldnames=['domain', 'count'])
    writer.writeheader()
    for k, v in sorted(d.items(), key=lambda x: x[1]):
        writer.writerow({'domain': k, 'count': v})
      
