from collections import defaultdict
import json


with open('food_services.json ', 'r', encoding='utf-8') as f:
    d = defaultdict(lambda : ('', 0))
    for rest in json.load(f):
        seats_count = int(rest['SeatsCount'])
        if seats_count > d[rest['TypeObject']][1]:
            d[rest['TypeObject']] = (rest['Name'], seats_count)
for k, v in sorted(d.items(), key=lambda x: x[0]):
    print(f'{k}: {v[0]}, {v[1]}')
  
