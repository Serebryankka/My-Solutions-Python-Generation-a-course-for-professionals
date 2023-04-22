import csv
from collections import defaultdict


with open('prices.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    d = defaultdict(list)
    r = next(reader)
    min_value = [r['Магазин'], min(map(lambda x: (x[0], int(x[1])), list(r.items())[1:]), key=lambda x: (x[1], x[0]))]

    for row in reader:
        a = min(map(lambda x: (x[0], int(x[1])), list(row.items())[1:]), key=lambda x: (x[1], x[0]))
        if a[1] < min_value[1][1]:
            min_value = [row['Магазин'], a]
        elif a == min_value[1] and row['Магазин'] < min_value[0]:
            min_value[0] = row['Магазин']

    print(f'{min_value[1][0]}: {min_value[0]}')
