import csv


a = int(input()) - 1

with open('deniro.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in sorted(reader, key=lambda x: int(x[a]) if x[a].isdigit() else x[a]):
        print(row)
      
