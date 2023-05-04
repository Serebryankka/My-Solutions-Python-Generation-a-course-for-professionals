print(''.join(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and not int(x) % 2, x.isupper(), x.lower()))))
