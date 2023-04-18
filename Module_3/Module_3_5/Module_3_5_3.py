from datetime import datetime, timedelta


def main(data): 
    data = datetime.strptime(data, '%d.%m.%Y %H:%M')
    time = timedelta(hours=data.hour, minutes=data.minute)
    weekday = data.weekday()
    d = {
        0: (timedelta(hours=9), timedelta(hours=21)),
        1: (timedelta(hours=9), timedelta(hours=21)),
        2: (timedelta(hours=9), timedelta(hours=21)),
        3: (timedelta(hours=9), timedelta(hours=21)),
        4: (timedelta(hours=9), timedelta(hours=21)),
        5: (timedelta(hours=10), timedelta(hours=18)),
        6: (timedelta(hours=10), timedelta(hours=18))
    }
    if d[weekday][0] <= time < d[weekday][1]:
        return (d[weekday][1] - time).seconds // 60
    else:
        return 'Магазин не работает'
      
      
if __name__ == '__main__':
    print(main(input()))
    
