from datetime import datetime, timedelta


def num_of_sundays(year):
    d = datetime(year, 1, 1)
    count = 0
    while d.year < year + 1:
        if d.weekday() == 6:
            count += 1
        d += timedelta(days=1)
    return count
  
