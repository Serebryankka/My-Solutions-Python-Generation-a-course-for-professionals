import calendar


def main(data):
    year, month = map(int, data.split())
    return calendar.monthrange(year, month)[1]


if __name__ == '__main__':
    main(input())
    
