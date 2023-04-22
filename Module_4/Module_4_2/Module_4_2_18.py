import csv
from collections import defaultdict
from datetime import datetime


with open('name_log.csv', 'r', encoding='utf-8') as old_log_file:
    reader = csv.DictReader(old_log_file)
    d = defaultdict(list)
    for row in reader:
        d[row['email']].append((row['username'], row['dtime']))

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as new_log_file:
    writer = csv.DictWriter(new_log_file, fieldnames=['username', 'email', 'dtime'])
    writer.writeheader()
    for k, v in sorted(d.items()):
        v = max(v, key=lambda x: datetime.strptime(x[1], '%d/%m/%Y %H:%M'))
        writer.writerow({'username': v[0], 'email': k, 'dtime': v[1]})
        
