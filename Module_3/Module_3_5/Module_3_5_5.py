from datetime import datetime


def main():
    data = map(str.split, (input() for _ in range(int(input()))))
    result = []
    min_date = 0
    count = 1
    for emp in data:
        name, surname, date = emp
        d = datetime.strptime(date, '%d.%m.%Y')
        try:
            if d == min_date:
                count += 1
                result = [f'{date} {count}']
            elif d < min_date:
                min_date = d
                result = [f'{date} {name} {surname}']
                count = 1
        except TypeError:
            min_date = d
    return ''.join(result)

if __name__ == '__main__':
    print(main())
    
