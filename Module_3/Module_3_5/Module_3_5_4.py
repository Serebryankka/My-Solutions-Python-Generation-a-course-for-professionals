from datetime import datetime, timedelta


def main(data):
    start, end = datetime.strptime(data[0], '%d.%m.%Y').date(), datetime.strptime(data[1], '%d.%m.%Y').date()
    #result = []
    while not (start.month + start.day) % 2:
        start += timedelta(days=1)
    while start <= end:
        if start.weekday() not in (0, 3):
            print(start.strftime('%d.%m.%Y'))
            #result.append(start.strftime('%d.%m.%Y'))
        start += timedelta(days=3)
    #return '\n'.join(result)
if __name__ == '__main__':
    main((input(), input()))
  
