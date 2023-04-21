with open('titanic.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv_file.read()
    table = [r.split(';') for r in reader.splitlines()]
    del table[0]
    for k in sorted(filter(lambda x: '1' == x[0] and float(x[-1]) < 18, table), key=lambda x: (x[2]), reverse=True):
        print(k[1])
      
