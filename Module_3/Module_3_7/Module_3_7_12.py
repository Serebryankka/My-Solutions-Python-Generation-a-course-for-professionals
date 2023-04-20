import calendar
from datetime import date


def get_days_in_month(year, month):
    n = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
         'September': 9, 'October': 10, 'November': 11, 'December': 12}

    return [date(year, n[month], i) for i in range(1, calendar.monthrange(year, n[month])[1]+1)]
  
