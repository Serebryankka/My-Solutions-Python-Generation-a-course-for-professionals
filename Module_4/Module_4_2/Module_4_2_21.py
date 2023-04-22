import csv


with open('student_counts.csv', 'r', encoding='utf-8') as csv_file, open('sorted_student_counts.csv', 'w',
                                                                         encoding='utf-8',
                                                                         newline='') as result_file:
    reader = csv.DictReader(csv_file)
    fieldnames = [reader.fieldnames[0]] + sorted(reader.fieldnames[1:],
                                                 key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
    writer = csv.DictWriter(result_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        d = {k: v for k, v in [list(row.items())[0]]}
        d.update(dict(sorted(list(row.items())[1:], key=lambda x: (int(x[0].split('-')[0]), x[0].split('-')[1]))))
        writer.writerow(d)
        
