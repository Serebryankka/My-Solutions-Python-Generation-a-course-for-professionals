from collections import Counter
import csv


with open('name_log .csv', encoding='utf-8') as csv_file:
    for k, v in sorted(Counter(user[1] for user in list(csv.reader(csv_file))[1:]).items()):
        print(f'{k}: {v}')
        
