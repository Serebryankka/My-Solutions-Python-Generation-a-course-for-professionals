from datetime import datetime, timedelta


def main():
    today = datetime.strptime(input()[:-5], '%d.%m')
    seven_days = today + timedelta(weeks=1)
    if seven_days.year > today.year:
        today, seven_days = (seven_days + timedelta(days=-2)).replace(year=1900), today
    data = list(filter(lambda x: today < datetime(year=1900, month=x[1].month, day=x[1].day) <= seven_days,
                       map(lambda x: [x[0], datetime.strptime(x[1], '%d.%m.%Y')],
                           map(lambda x: x.rsplit(maxsplit=1), (input() for _ in range(int(input())))))))
    try:
        return max(data, key=lambda x: x[1])[0]
    except ValueError:
        return 'Дни рождения не планируются'

      
if __name__ == '__main__':
    print(main())
    
