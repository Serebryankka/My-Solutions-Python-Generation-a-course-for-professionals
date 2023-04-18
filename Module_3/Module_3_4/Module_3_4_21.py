from datetime import datetime, timedelta
import pandas as pd


def fill_up_missing_dates(dates):
    dat = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), dates))
    result = []
    for d in pd.date_range(min(dat), max(dat)):
        result.append(d.strftime('%d.%m.%Y'))
    return result
