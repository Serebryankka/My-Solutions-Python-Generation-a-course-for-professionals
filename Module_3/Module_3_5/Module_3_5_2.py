from datetime import date
from collections import defaultdict


def main():
    d = date(1, 1, 13)
    y = 1
    result = defaultdict(int)
    while d != date(9999, 12, 13):
        for m in range(1, 13):
            d = date(y, m, 13)
            result[d.weekday()] += 1
        y += 1
    for k, v in sorted(result.items()):
        print(v)


if __name__ == '__main__':
    main()
    
