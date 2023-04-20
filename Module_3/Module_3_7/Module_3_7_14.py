import calendar
from datetime import date


def main(year):
    result = []
    for month in range(1, 13):
        for day in range(1, 8):
            if calendar.weekday(year, month, day) == 3:
                result.append(date(year, month, day+14).strftime('%d.%m.%Y'))
                break
    return '\n'.join(result)


if __name__ == '__main__':
    print(main(int(input())))
    
