import csv
from datetime import datetime


with open('meetings.csv', 'r', encoding='utf-8') as csv_file:
    data = list(csv.reader(csv_file))
    for friend in sorted(data[1:], key=lambda x: datetime.strptime(f'{x[2]} {x[3]}', '%d.%m.%Y %H:%M')):
        print(f'{friend[0]} {friend[1]}')
      
