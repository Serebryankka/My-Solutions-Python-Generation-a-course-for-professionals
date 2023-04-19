import calendar


def main(data):
    year, month, day = map(int, data.split('-'))
    return calendar.day_name[calendar.weekday(year, month, day)]
  

if __name__ == '__main__':
    print(main(input()))
    
