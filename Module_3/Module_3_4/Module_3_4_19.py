from datetime import datetime, timedelta


def main(data):
    d = datetime.strptime(data, '%d.%m.%Y')
    result = []
    count = 2
    while count != 12:
        result.append(d)
        d += timedelta(days=count)
        count += 1
    return '\n'.join(map(lambda x: x.strftime('%d.%m.%Y'), result))
  
