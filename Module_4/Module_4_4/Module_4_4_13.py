from datetime import datetime
import json


my_start = datetime(1900, 1, 1, 10)
my_end = datetime(1900, 1, 1, 12)
with open('pools.json', 'r', encoding='utf-8') as f:
    data = []
    for d in json.load(f):
        start, end = [datetime.strptime(time, '%H:%M') for time in d['WorkingHoursSummer']['Понедельник'].split('-')]
        if my_start >= start and my_end <= end:
            data.append({'Address': d['Address'], 'DimensionsSummer': (d['DimensionsSummer']['Length'],
                                                                       d['DimensionsSummer']['Width'])})
pool = max(data, key=lambda x: x['DimensionsSummer'])
print(f'''{pool['DimensionsSummer'][0]}x{pool['DimensionsSummer'][1]}
{pool['Address']}''')
