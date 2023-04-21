import csv


with open('grades.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    for row in rows:
        print(row)
