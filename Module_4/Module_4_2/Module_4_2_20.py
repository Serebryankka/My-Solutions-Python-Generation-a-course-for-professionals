import csv
from collections import defaultdict


def condense_csv(filename, id_name):
    with open(filename, 'r', encoding='utf-8') as f, open('condensed.csv', 'w', encoding='utf-8',
                                                          newline='') as csv_file:
        reader = csv.reader(f)
        header = [id_name]
        d = defaultdict(lambda: defaultdict())
        for row in reader:
            id_, property_ = row[0], row[1]
            if property_ not in header:
                header.append(property_)
            d[id_][id_name] = id_
            d[id_][property_] = row[2]  # value

        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        writer.writerows(d.values())
