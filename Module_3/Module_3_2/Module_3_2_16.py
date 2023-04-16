from datetime import date


def is_correct(dat):
    day, month, year = map(int, dat.split('.'))
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def main(data):
    count = 0
    result = []
    for d in data[:-1]:
        if is_correct(d):
            count += 1
            result.append('Корректная')
        else:
            result.append('Некорректная')
    result.append(str(count))
    return '\n'.join(result)
    
