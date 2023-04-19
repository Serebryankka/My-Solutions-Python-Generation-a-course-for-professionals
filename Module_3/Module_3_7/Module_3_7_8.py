import calendar


def main(data):
    year, month = data.split()
    n = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11,
         'Dec': 12}
    return calendar.month(int(year), n[month])
  
  
if __name__ == '__main__':
    print(main(input()))
    
