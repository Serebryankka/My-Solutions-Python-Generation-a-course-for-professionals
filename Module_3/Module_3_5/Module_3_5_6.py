from datetime import datetime
from collections import defaultdict

def main():
    data = map(lambda x: x[-10:], (input() for _ in range(int(input()))))
    result = defaultdict(int)
    for d in data:
        result[d] += 1
    max_date = 0
    for k, v in result.items():
        if v > max_date:
            max_date, max_dates = v, [k]
        elif v == max_date:
            max_dates.append(k)
        
    return '\n'.join(sorted(max_dates, key=lambda x: datetime.strptime(x, '%d.%m.%Y')))


if __name__ == '__main__':
    print(main())
    
