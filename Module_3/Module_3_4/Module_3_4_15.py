from datetime import datetime, timedelta


def main(data):
    d = datetime.strptime(data, '%d.%m.%Y')
    return '\n'.join(map(lambda x: x.strftime('%d.%m.%Y'), (d - timedelta(days=1), d + timedelta(days=1))))

if __name__ == '__main__':
    main(input())
    
