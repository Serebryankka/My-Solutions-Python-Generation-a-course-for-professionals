from datetime import datetime, timedelta


def main(data):
    start, end = map(lambda x: datetime.strptime(x, '%H:%M'), data)
    #result = []
    while end - start >= timedelta(minutes=45):
        print(f'{start.strftime("%H:%M")} - {(start + timedelta(minutes=45)).strftime("%H:%M")}')
        #result.append(f'{start.strftime("%H:%M")} - {(start + timedelta(minutes=45)).strftime("%H:%M")}')
        start += timedelta(minutes=55)
    #return '\n'.join(result)


if __name__ == '__main__':
    main((input(), input()))
    
