import csv
#from collections import defaultdict

def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as csv_file:
        rows = csv.DictReader(csv_file)
        # d = defaultdict(list)
        # for row in rows:
        #     for k, v in row.items():
        #         d[k].append(v)
        # print(d)
        d = {}
        for row in rows:
            for k, v in row.items():
                d[k] = d.get(k, [])
                d[k].append(v)
        print(d)
        
