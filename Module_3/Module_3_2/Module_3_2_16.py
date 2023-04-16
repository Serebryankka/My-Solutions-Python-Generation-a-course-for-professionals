from datetime import date


def is_correct(d):
    day, month, year = map(int, d.split('.'))
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def main():
    a = input()
    data = []
    while a != 'end':
        data.append(a)
        a = input()
    count = 0
    result = []
    for d in data:
        if is_correct(d):
            count += 1
            result.append('Корректная')
        else:
            result.append('Некорректная')
    result.append(str(count))
    return '\n'.join(result)
if __name__ == '__main__':
    print(main())
    
