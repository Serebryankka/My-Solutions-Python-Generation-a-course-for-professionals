import calendar
from datetime import date


def get_all_mondays(year):
    result = []
    for month in range(1, 13):
        days_in_moth = calendar.monthrange(year, month)[1] + 1
        for day in range(1, days_in_moth):
            if calendar.weekday(year, month, day) == 0:
                result.extend([date(year, month, d) for d in range(day, days_in_moth, 7)])
                break
    return result
  
