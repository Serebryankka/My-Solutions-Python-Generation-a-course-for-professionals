from datetime import datetime, timedelta


def main(data):
    d1, *data = map(lambda x: datetime.strptime(x, '%d.%m.%Y'), data.split())
    result = []
    for d in data:
        result.append(abs((d - d1).days))
        d1 = d
    return result

if __name__ == '__main__':
  print(main(input()))
  
